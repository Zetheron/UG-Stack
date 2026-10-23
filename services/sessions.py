"""Sesi login yang bisa dipulihkan: token acak disimpan di perangkat pengguna, hash-nya di penyimpanan server.

Dipakai agar pengguna tidak keluar sendiri ketika koneksi WebSocket terputus (mis. batas durasi fungsi di Vercel atau layanan
yang "tidur"). Token tidak pernah disimpan polos di server; sesi admin lebih singkat (30 menit).
"""
import hashlib
import secrets
import time

from . import storage

SESSIONS_FILE = "sessions.json"
TTL = {"admin": 30 * 60, "dosen": 12 * 3600, "mahasiswa": 12 * 3600}


def _hash(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


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


def restore(token: str, now: float = None):
    """Mengembalikan pengguna publik {username, role, must_change} bila token valid, atau None."""
    if not token or len(token) < 20:
        return None
    now = time.time() if now is None else now
    try:
        rec = storage.load_json(SESSIONS_FILE, {}).get(_hash(token))
        if not rec or rec["exp"] <= now:
            return None
        for u in storage.load_json("users.json", []):
            if u["username"].lower() == rec["username"].lower() and u["role"] == rec["role"]:
                return {"username": u["username"], "role": u["role"],
                        "must_change": bool(u.get("must_change")) and u["role"] != "admin"}
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
