"""Penyimpanan data JSON multi-backend: Berkas lokal, Penyimpanan Perangkat (APK), dan PostgreSQL (Neon)."""
import json
import os
import ssl
import tempfile
import threading
import urllib.parse

LOCK = threading.RLock()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_DIR = DEFAULT_DATA_DIR


class StorageError(Exception):
    """Kesalahan saat membaca atau menyimpan data."""


def get_data_dir() -> str:
    """Pilih folder data: prioritas DATA_DIR (untuk pengujian), UG_DATA_DIR, /tmp (di Vercel), lalu folder data/."""
    if DATA_DIR != DEFAULT_DATA_DIR:
        return str(DATA_DIR)
    env_dir = os.environ.get("UG_DATA_DIR", "").strip()
    if env_dir:
        return env_dir
    if os.environ.get("VERCEL"):
        return os.path.join(tempfile.gettempdir(), "ugstack_data")
    return str(DATA_DIR)


def _check_writable_dir(d: str) -> None:
    """Pastikan direktori target valid dan dapat ditulis (kompatibel di Linux maupun Windows)."""
    if not d or "\x00" in str(d):
        raise StorageError("Path folder data tidak valid.")
    norm = os.path.normpath(str(d)).replace("\\", "/")
    # Cegah path virtual Linux (/proc, /sys, /dev, /root) agar tetap gagal saat diuji di Windows
    if norm in ("/proc", "/sys", "/dev", "/root") or norm.startswith(("/proc/", "/sys/", "/dev/", "/root/")):
        raise StorageError(f"Folder tidak bisa ditulis: {d}")
    if os.path.isfile(d):
        raise StorageError(f"Path adalah berkas, bukan folder: {d}")
    parent = os.path.dirname(os.path.abspath(d))
    if parent and os.path.isfile(parent):
        raise StorageError(f"Induk path adalah berkas, bukan folder: {parent}")
    if os.path.exists(d) and (os.stat(d).st_mode & 0o200) == 0:
        raise StorageError(f"Folder hanya-baca (tidak bisa ditulis): {d}")


class FileBackend:
    label = "berkas"

    def __init__(self, data_dir: str | None = None):
        self._dir = data_dir

    def _base(self) -> str:
        return self._dir if self._dir is not None else get_data_dir()

    def _path(self, name: str) -> str:
        clean = os.path.basename(name)
        return os.path.join(self._base(), clean)

    def read(self, name: str) -> str | None:
        p = self._path(name)
        if not os.path.exists(p):
            return None
        try:
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
        except OSError as e:
            raise StorageError(f"Gagal membaca berkas {name}: {e}") from e

    def write(self, name: str, text: str) -> None:
        base = self._base()
        _check_writable_dir(base)
        p = self._path(name)
        tmp = p + ".tmp"
        try:
            os.makedirs(base, exist_ok=True)
            _check_writable_dir(base)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(text)
            os.replace(tmp, p)
        except OSError as e:
            try:
                if os.path.exists(tmp):
                    os.remove(tmp)
            except OSError:
                pass
            raise StorageError(f"Gagal menyimpan berkas {name}: {e}") from e

    def delete(self, name: str) -> None:
        p = self._path(name)
        try:
            if os.path.exists(p):
                os.remove(p)
        except OSError as e:
            raise StorageError(f"Gagal menghapus berkas {name}: {e}") from e

    def list_names(self, prefix: str = "") -> list[str]:
        base = self._base()
        try:
            if not os.path.isdir(base):
                return []
            return sorted(
                f for f in os.listdir(base)
                if f.startswith(prefix) and not f.endswith(".tmp") and os.path.isfile(os.path.join(base, f))
            )
        except OSError:
            return []


class ClientStorageBackend:
    """Backend penyimpanan perangkat Flet (SharedPreferences) untuk APK Android/iOS."""
    label = "perangkat"
    PREFIX = "ugstack:"

    def __init__(self, client_storage, prefix: str = "ugstack:"):
        self.cs = client_storage
        self.PREFIX = prefix

    def _key(self, name: str) -> str:
        return self.PREFIX + os.path.basename(name)

    def read(self, name: str) -> str | None:
        k = self._key(name)
        try:
            if isinstance(self.cs, dict):
                val = self.cs.get(k, self.cs.get(name))
            else:
                val = self.cs.get(k)
                if val is None and hasattr(self.cs, "get_keys"):
                    for existing in (self.cs.get_keys("") or []):
                        if existing == name or existing.endswith(":" + name) or existing.endswith("." + name):
                            val = self.cs.get(existing)
                            break
            if val is None:
                return None
            return val if isinstance(val, str) else json.dumps(val, ensure_ascii=False)
        except Exception as e:
            raise StorageError(f"Gagal membaca penyimpanan perangkat ({name}): {e}") from e

    def write(self, name: str, text: str) -> None:
        k = self._key(name)
        try:
            if isinstance(self.cs, dict):
                self.cs[k] = text
            else:
                self.cs.set(k, text)
        except Exception as e:
            raise StorageError(f"Gagal menyimpan ke penyimpanan perangkat ({name}): {e}") from e

    def delete(self, name: str) -> None:
        k = self._key(name)
        try:
            if isinstance(self.cs, dict):
                self.cs.pop(k, None)
            else:
                self.cs.remove(k)
        except Exception:
            pass

    def list_names(self, prefix: str = "") -> list[str]:
        full_prefix = self.PREFIX + prefix
        try:
            if isinstance(self.cs, dict):
                keys = list(self.cs.keys())
            elif hasattr(self.cs, "get_keys"):
                keys = self.cs.get_keys(full_prefix) or []
            else:
                keys = []
            res = []
            for k in keys:
                if k.startswith(full_prefix):
                    res.append(k[len(self.PREFIX):])
            return sorted(res)
        except Exception:
            return []


class PostgresBackend:
    """Backend PostgreSQL (Neon) menggunakan tabel key-value `ug_kv`."""
    label = "postgres"

    def __init__(self, connect_fn):
        self._connect_fn = connect_fn
        self._conn = None
        self._ready = False

    @classmethod
    def from_url(cls, url: str) -> "PostgresBackend":
        if not url or not isinstance(url, str):
            raise StorageError("DATABASE_URL kosong atau tidak valid.")
        parsed = urllib.parse.urlparse(url.strip())
        if parsed.scheme not in ("postgres", "postgresql", "postgresql+pg8000"):
            raise StorageError(f"Skema DATABASE_URL tidak valid: {parsed.scheme}")
        host = parsed.hostname
        database = urllib.parse.unquote((parsed.path or "").lstrip("/"))
        if not host or not database:
            raise StorageError("DATABASE_URL harus memuat host dan nama database.")
        try:
            port = int(parsed.port) if parsed.port else 5432
        except ValueError as e:
            raise StorageError("Port DATABASE_URL tidak valid.") from e

        user = urllib.parse.unquote(parsed.username or "")
        password = urllib.parse.unquote(parsed.password or "")
        qs = urllib.parse.parse_qs(parsed.query)
        sslmode = (qs.get("sslmode", ["require"])[0] or "require").lower()

        def connect():
            import pg8000.dbapi

            kwargs = dict(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database,
                timeout=15,
            )
            if sslmode not in ("disable", "allow"):
                ctx = ssl.create_default_context()
                if sslmode in ("require", "prefer"):
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                kwargs["ssl_context"] = ctx
            return pg8000.dbapi.connect(**kwargs)

        return cls(connect)

    def _exec(self, sql: str, params: tuple = (), fetch: str | None = None):
        last_err = None
        for _ in range(2):
            try:
                if self._conn is None:
                    self._conn = self._connect_fn()
                    self._ready = False
                cur = self._conn.cursor()
                if not self._ready:
                    cur.execute("CREATE TABLE IF NOT EXISTS ug_kv (k TEXT PRIMARY KEY, v TEXT NOT NULL)")
                    self._conn.commit()
                    self._ready = True
                cur.execute(sql, params)
                out = None
                if fetch == "one":
                    out = cur.fetchone()
                elif fetch == "all":
                    out = cur.fetchall()
                self._conn.commit()
                if hasattr(cur, "close"):
                    cur.close()
                return out
            except Exception as e:
                last_err = e
                try:
                    if self._conn is not None and hasattr(self._conn, "rollback"):
                        self._conn.rollback()
                except Exception:
                    pass
                try:
                    if self._conn is not None and hasattr(self._conn, "close"):
                        self._conn.close()
                except Exception:
                    pass
                self._conn = None
                self._ready = False
        raise StorageError(f"Kesalahan database PostgreSQL: {last_err}") from last_err

    def read(self, name: str) -> str | None:
        row = self._exec("SELECT v FROM ug_kv WHERE k = %s", (os.path.basename(name),), fetch="one")
        if not row:
            return None
        return row[0] if isinstance(row, (tuple, list)) else str(row)

    def write(self, name: str, text: str) -> None:
        k = os.path.basename(name)
        self._exec(
            "INSERT INTO ug_kv (k, v) VALUES (%s, %s) "
            "ON CONFLICT (k) DO UPDATE SET v = EXCLUDED.v",
            (k, text),
        )

    def delete(self, name: str) -> None:
        self._exec("DELETE FROM ug_kv WHERE k = %s", (os.path.basename(name),))

    def list_names(self, prefix: str = "") -> list[str]:
        rows = self._exec("SELECT k FROM ug_kv ORDER BY k", fetch="all") or []
        names = [r[0] if isinstance(r, (tuple, list)) else str(r) for r in rows]
        return sorted(n for n in names if n.startswith(prefix))


_backend = None


def set_backend(backend) -> None:
    global _backend
    with LOCK:
        _backend = backend


def reset_backend() -> None:
    global _backend
    with LOCK:
        _backend = None


def use_client_storage(client_storage) -> ClientStorageBackend:
    b = ClientStorageBackend(client_storage)
    set_backend(b)
    return b


def get_backend():
    global _backend
    with LOCK:
        if _backend is not None:
            return _backend
        if DATA_DIR != DEFAULT_DATA_DIR:
            return FileBackend()
        url = os.environ.get("DATABASE_URL", "").strip()
        if url:
            _backend = PostgresBackend.from_url(url)
            return _backend
        _backend = FileBackend()
        return _backend


def backend_label() -> str:
    return getattr(get_backend(), "label", "berkas")


def using_files() -> bool:
    return backend_label() == "berkas"


def peek_json(name: str):
    """Baca JSON tanpa membuat berkas bawaan bila belum ada."""
    with LOCK:
        raw = get_backend().read(name)
        if raw is None:
            return None
        try:
            return json.loads(raw)
        except (json.JSONDecodeError, TypeError, ValueError):
            return None


def load_json(name: str, default):
    """Baca JSON; jika belum ada simpan nilai bawaan. Jika rusak, cadangkan ke .corrupt lalu pulihkan."""
    with LOCK:
        backend = get_backend()
        raw = backend.read(name)
        if raw is None:
            save_json(name, default)
            return json.loads(json.dumps(default))
        try:
            return json.loads(raw)
        except (json.JSONDecodeError, TypeError, ValueError):
            try:
                backend.write(name + ".corrupt", raw)
            except Exception:
                pass
            save_json(name, default)
            return json.loads(json.dumps(default))


def save_json(name: str, data) -> None:
    with LOCK:
        text = json.dumps(data, ensure_ascii=False, indent=2)
        get_backend().write(name, text)


def delete_json(name: str) -> None:
    with LOCK:
        get_backend().delete(name)


def list_names(prefix: str = "") -> list[str]:
    with LOCK:
        return get_backend().list_names(prefix)