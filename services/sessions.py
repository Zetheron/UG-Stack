"""Sesi login yang bisa dipulihkan: token acak disimpan di perangkat pengguna, hash-nya di penyimpanan server.

Dipakai agar pengguna tidak keluar sendiri ketika koneksi WebSocket terputus (mis. batas durasi fungsi di Vercel atau layanan
yang "tidur"). Token tidak pernah disimpan polos di server; sesi admin lebih singkat (30 menit).
"""
import hashlib
import hmac
import json
import os
import secrets
import time

from . import storage

SESSIONS_FILE = "sessions.json"
TTL = {"admin": 30 * 60, "dosen": 12 * 3600, "mahasiswa": 12 * 3600}
ACTIVE_SLIDE_SECONDS = 12 * 3600


def _hash(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def _backup_secret() -> bytes:
    raw = os.getenv("FLET_SECRET_KEY") or os.getenv("UG_ADMIN_KEY") or "ugstack-session-secret-2026"
    return raw.encode("utf-8")


def sign_user_backup(user: dict, now: float = None) -> str:
    """Buat cadangan sesi bertanda tangan HMAC untuk disimpan di perangkat klien (anti-logout saat container serverless berganti)."""
    if not isinstance(user, dict) or not user.get("username") or not user.get("role"):
        return ""
    ts = time.time() if now is None else now
    payload = {
        "username": user["username"],
        "role": user["role"],
        "must_change": bool(user.get("must_change")) and user["role"] != "admin",
        "npm": user.get("npm", ""),
        "full_name": user.get("full_name", ""),
        "exp": ts + 24 * 3600,
    }
    body = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    sig = hmac.new(_backup_secret(), body.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"{sig}.{body}"


def verify_user_backup(signed_str: str, now: float = None):
    """Verifikasi cadangan sesi dari klien bila penyimpanan sementara (/tmp) di server sempat di-reset."""
    if not signed_str or "." not in signed_str:
        return None
    sig, body = signed_str.split(".", 1)
    expected = hmac.new(_backup_secret(), body.encode("utf-8"), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, expected):
        return None
    try:
        data = json.loads(body)
    except ValueError:
        return None
    ts = time.time() if now is None else now
    if not isinstance(data, dict) or data.get("exp", 0) <= ts:
        return None
    uname = (data.get("username") or "").strip()
    role = (data.get("role") or "").strip()
    if not uname or not role:
        return None
    try:
        users = storage.load_json("users.json", [])
        for u in users:
            if u["username"].lower() == uname.lower():
                if u["role"] != role:
                    return None
                pub = {
                    "username": u["username"],
                    "role": u["role"],
                    "must_change": bool(u.get("must_change")) and u["role"] != "admin",
                }
                if u.get("npm") or data.get("npm"):
                    pub["npm"] = u.get("npm") or data.get("npm")
                if u.get("full_name") or data.get("full_name"):
                    pub["full_name"] = u.get("full_name") or data.get("full_name")
                if u.get("avatar"):
                    pub["avatar"] = u["avatar"]
                return pub
        if role == "admin" and uname.lower() == "admin":
            return {"username": "admin", "role": "admin", "must_change": False}
    except storage.StorageError:
        pass
    pub = {"username": uname, "role": role, "must_change": bool(data.get("must_change"))}
    if data.get("npm"):
        pub["npm"] = data["npm"]
    if data.get("full_name"):
        pub["full_name"] = data["full_name"]
    return pub


def create(user: dict, now: float = None):
    """Buat sesi untuk pengguna. Mengembalikan token (disimpan di perangkat) atau None bila gagal."""
    now = time.time() if now is None else now
    token = secrets.token_urlsafe(32)
    try:
        with storage.LOCK:
            data = {h: r for h, r in storage.load_json(SESSIONS_FILE, {}).items() if r["exp"] > now}   # buang yang kedaluwarsa
            data[_hash(token)] = {"username": user["username"], "role": user["role"],
                                  "exp": now + TTL.get(user["role"], 3600)}
            storage.save_json(SESSIONS_FILE, data)
    except storage.StorageError:
        return None
    return token


def touch(token: str) -> None:
    """Perpanjang masa aktif sesi saat pengguna aktif berinteraksi di aplikasi."""
    if not token or len(token) < 20:
        return
    now = time.time()
    h = _hash(token)
    try:
        with storage.LOCK:
            data = storage.load_json(SESSIONS_FILE, {})
            rec = data.get(h)
            if rec and rec.get("exp", 0) > now:
                new_exp = now + max(TTL.get(rec.get("role"), 3600), ACTIVE_SLIDE_SECONDS)
                if new_exp - rec["exp"] > 300:
                    rec["exp"] = new_exp
                    storage.save_json(SESSIONS_FILE, data)
    except storage.StorageError:
        pass


def restore(token: str, now: float = None):
    """Mengembalikan pengguna publik {username, role, must_change} bila token valid, atau None."""
    if not token or len(token) < 20:
        return None
    is_live = now is None
    now = time.time() if is_live else now
    h = _hash(token)
    try:
        sessions_map = storage.load_json(SESSIONS_FILE, {})
        rec = sessions_map.get(h)
        if rec is None and is_live and hasattr(storage, "_MEM_CACHE"):
            storage._MEM_CACHE.pop(SESSIONS_FILE, None)
            storage._MEM_CACHE.pop("users.json", None)
            sessions_map = storage.load_json(SESSIONS_FILE, {})
            rec = sessions_map.get(h)
        if not rec or rec["exp"] <= now:
            return None
        users = storage.load_json("users.json", [])
        for u in users:
            if u["username"].lower() == rec["username"].lower() and u["role"] == rec["role"]:
                if is_live:
                    touch(token)
                pub = {"username": u["username"], "role": u["role"],
                       "must_change": bool(u.get("must_change")) and u["role"] != "admin"}
                if u.get("npm"):
                    pub["npm"] = u["npm"]
                if u.get("full_name"):
                    pub["full_name"] = u["full_name"]
                if u.get("avatar"):
                    pub["avatar"] = u["avatar"]
                return pub
        if is_live and rec.get("role") == "admin" and rec.get("username", "").lower() == "admin":
            touch(token)
            return {"username": "admin", "role": "admin", "must_change": False}
    except storage.StorageError:
        return None
    return None                                    # akun sudah dihapus atau perannya berubah


def revoke(token: str) -> None:
    if not token:
        return
    try:
        with storage.LOCK:
            data = storage.load_json(SESSIONS_FILE, {})
            if data.pop(_hash(token), None) is not None:
                storage.save_json(SESSIONS_FILE, data)
    except storage.StorageError:
        pass


def revoke_user(username: str) -> None:
    """Cabut semua sesi pengguna (dipakai saat password direset, peran berubah, atau akun dihapus)."""
    try:
        with storage.LOCK:
            data = storage.load_json(SESSIONS_FILE, {})
            kept = {h: r for h, r in data.items() if r["username"].lower() != username.lower()}
            if len(kept) != len(data):
                storage.save_json(SESSIONS_FILE, kept)
    except storage.StorageError:
        pass
