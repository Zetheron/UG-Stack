"""Layanan ruang diskusi (Chat) dan Bot Asisten UG-Stack."""
from datetime import datetime
from services import audit, roles, storage

CHAT_FILE = "chat_messages.json"
CHANNELS = ("umum", "tanya-dosen", "python-web", "algoritma")

SEED_MESSAGES = [
    {
        "id": 1, "channel": "umum", "username": "admin", "npm": "STAFF", "role": "admin",
        "text": "Selamat datang di Ruang Diskusi UG-Stack! Gunakan kanal #tanya-dosen atau ketik @bot untuk bertanya materi.",
        "time": "2026-10-29 08:00",
    },
    {
        "id": 2, "channel": "tanya-dosen", "username": "bot_ugstack", "npm": "AI", "role": "dosen",
        "text": "Halo! Saya Asisten Bot UG-Stack. Tanyakan konsep pemrograman atau algoritma di sini.",
        "time": "2026-10-29 08:01",
    },
]

BOT_KB = [
    (("binary search", "pencarian biner"), "Binary Search bekerja pada data terurut dengan membagi rentang pencarian menjadi dua: O(log n). Coba langsung di menu Simulasi!"),
    (("merge sort", "pengurutan"), "Merge Sort membagi daftar secara rekursif lalu menggabungkannya secara terurut (Divide & Conquer) dengan kompleksitas stabil O(n log n)."),
    (("insertion sort",), "Insertion Sort menyisipkan elemen ke posisi tepat satu per satu. Cepat untuk data kecil O(n), namun rata-rata O(n^2)."),
    (("python", "list", "dict"), "Di Python, list [1, 2, 3] menyimpan data urut, sedangkan dict {'kunci': 'nilai'} menyimpan pasangan key-value."),
    (("sql", "select", "join"), "Gunakan SELECT kolom FROM tabel WHERE kondisi; dan JOIN untuk merelasikan dua tabel."),
    (("npm", "login", "sinkron"), "Anda dapat login menggunakan Username maupun NPM mahasiswa yang sudah ditautkan ke akun Anda."),
]

def list_messages(channel: str = "umum") -> list[dict]:
    ch = channel if channel in CHANNELS else "umum"
    msgs = storage.load_json(CHAT_FILE, SEED_MESSAGES)
    return [m for m in msgs if m.get("channel", "umum") == ch][-80:]

def send_message(user: dict | None, channel: str, text: str) -> tuple[bool, str]:
    if not user:
        return False, "Silakan login terlebih dahulu."
    clean = (text or "").strip()
    if not clean:
        return False, "Pesan tidak boleh kosong."
    ch = channel if channel in CHANNELS else "umum"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    with storage.LOCK:
        msgs = storage.load_json(CHAT_FILE, SEED_MESSAGES)
        nid = max((m.get("id", 0) for m in msgs), default=0) + 1
        msgs.append({
            "id": nid, "channel": ch, "username": user.get("username", "anonim"),
            "npm": user.get("npm", ""), "role": user.get("role", "mahasiswa"),
            "text": clean, "time": now_str,
        })
        low = clean.lower()
        ans = next((a for keys, a in BOT_KB if any(k in low for k in keys)), None)
        if ans or "@bot" in low:
            reply = ans or "Pertanyaan menarik! Silakan jelajahi materi di menu Tutorial atau coba kodenya di menu Simulasi."
            msgs.append({
                "id": nid + 1, "channel": ch, "username": "bot_ugstack", "npm": "AI",
                "role": "dosen", "text": reply, "time": now_str,
            })
        storage.save_json(CHAT_FILE, msgs[-200:])
    return True, "Pesan terkirim."

def delete_message(actor: dict | None, msg_id: int) -> tuple[bool, str]:
    if not roles.is_staff(actor):
        return False, "Hanya admin atau dosen yang boleh menghapus pesan."
    with storage.LOCK:
        msgs = storage.load_json(CHAT_FILE, SEED_MESSAGES)
        new_msgs = [m for m in msgs if m.get("id") != msg_id]
        if len(new_msgs) == len(msgs):
            return False, "Pesan tidak ditemukan."
        storage.save_json(CHAT_FILE, new_msgs)
    return True, "Pesan dihapus."
