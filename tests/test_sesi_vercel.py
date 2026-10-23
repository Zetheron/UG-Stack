"""Pengujian: pemulihan sesi login dan kesiapan titik masuk Vercel."""
import ast
import json
import os
import shutil
import tempfile
import unittest

from services import auth, sessions, storage

ADMIN = {"username": "admin", "role": "admin"}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.environ["FLET_APP_STORAGE_DATA"] = self.tmp
        storage.reset_backend()
        auth.init_data()
        auth.reset_lock()
        auth.register("budi123", "Rahasia123", "Rahasia123")
        self.mhs = {"username": "budi123", "role": "mahasiswa"}
        self.now = 1_800_000_000.0

    def tearDown(self):
        storage.reset_backend()
        shutil.rmtree(self.tmp, ignore_errors=True)
        os.environ.pop("FLET_APP_STORAGE_DATA", None)
        os.environ.pop("VERCEL", None)


class TestSesi(Base):
    def test_T69_buat_dan_pulihkan_sesi(self):
        token = sessions.create(self.mhs, self.now)
        self.assertGreater(len(token), 30)
        user = sessions.restore(token, self.now + 60)
        self.assertEqual((user["username"], user["role"]), ("budi123", "mahasiswa"))
        for bad in (None, "", "pendek", "x" * 40):
            self.assertIsNone(sessions.restore(bad, self.now))
        raw = json.dumps(storage.load_json(sessions.SESSIONS_FILE, {}))
        self.assertNotIn(token, raw)                                         # token tidak disimpan polos di server

    def test_T70_masa_berlaku_admin_lebih_singkat(self):
        t_admin = sessions.create(ADMIN, self.now)
        t_mhs = sessions.create(self.mhs, self.now)
        later = self.now + 3600                                              # 1 jam kemudian
        self.assertIsNone(sessions.restore(t_admin, later))                  # admin 30 menit
        self.assertIsNotNone(sessions.restore(t_mhs, later))                 # mahasiswa 12 jam
        self.assertIsNone(sessions.restore(t_mhs, self.now + 13 * 3600))
        sessions.create(self.mhs, self.now + 13 * 3600)                      # sesi kedaluwarsa dibersihkan saat membuat sesi baru
        self.assertEqual(len(storage.load_json(sessions.SESSIONS_FILE, {})), 1)

    def test_T71_pencabutan_sesi(self):
        t1, t2 = sessions.create(self.mhs, self.now), sessions.create(self.mhs, self.now)
        sessions.revoke(t1)
        self.assertIsNone(sessions.restore(t1, self.now))
        self.assertIsNotNone(sessions.restore(t2, self.now))
        sessions.revoke_user("BUDI123")
        self.assertIsNone(sessions.restore(t2, self.now))
        t3 = sessions.create(self.mhs, self.now)
        self.assertTrue(auth.reset_password(ADMIN, "budi123", "Sementara123")[0])      # reset password mencabut sesi
        self.assertIsNone(sessions.restore(t3, self.now))
        t4 = sessions.create(self.mhs, self.now)
        self.assertTrue(auth.set_role(ADMIN, "budi123", "dosen")[0])                   # ubah peran mencabut sesi
        self.assertIsNone(sessions.restore(t4, self.now))
        t5 = sessions.create({"username": "budi123", "role": "dosen"}, self.now)
        self.assertTrue(auth.delete_user(ADMIN, "budi123")[0])                         # akun dihapus
        self.assertIsNone(sessions.restore(t5, self.now))

    def test_T72_peran_berubah_di_data_membuat_token_tidak_valid(self):
        token = sessions.create(self.mhs, self.now)
        users = storage.load_json("users.json", [])
        for u in users:
            if u["username"] == "budi123":
                u["role"] = "dosen"                                               # diubah langsung di data
        storage.save_json("users.json", users)
        self.assertIsNone(sessions.restore(token, self.now))


class TestVercel(Base):
    def test_T73_main_py_mengekspor_app_tingkat_atas(self):
        """Vercel butuh variabel tingkat atas `app` di main.py (kesalahan PYTHON_ENTRYPOINT_NOT_FOUND)."""
        with open(os.path.join(ROOT, "main.py"), encoding="utf-8") as f:
            tree = ast.parse(f.read())
        names = [t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)]
        self.assertIn("app", names)
        funcs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
        self.assertIn("_make_asgi_app", funcs)
        self.assertIn("main", funcs)
        self.assertLess(funcs.index("main"), funcs.index("_make_asgi_app"))        # app dibuat setelah main didefinisikan

    def test_T74_berkas_penyiapan_vercel(self):
        with open(os.path.join(ROOT, "requirements.txt"), encoding="utf-8") as f:
            req = f.read().lower()
        for pkg in ("flet==0.23.1", "fastapi", "uvicorn", "pg8000"):
            self.assertIn(pkg, req)
        with open(os.path.join(ROOT, ".python-version"), encoding="utf-8") as f:
            self.assertRegex(f.read().strip(), r"^3\.(11|12|13)$")
        self.assertFalse(os.path.exists(os.path.join(ROOT, "vercel.json")))        # tidak ada konfigurasi lama yang salah

    def test_T75_di_vercel_tanpa_database_memakai_tmp(self):
        os.environ.pop("FLET_APP_STORAGE_DATA")
        os.environ["VERCEL"] = "1"
        base = storage.get_data_dir()
        self.assertTrue(base.startswith(tempfile.gettempdir()))
        self.assertTrue(os.access(base, os.W_OK))


if __name__ == "__main__":
    unittest.main(verbosity=2)
