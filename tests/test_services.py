import os
import shutil
import tempfile
import unittest

from services import auth, modules, progress, storage, validators
from services.storage import StorageError

ADMIN = {"username": "admin", "role": "admin"}
MHS = {"username": "budi_01", "role": "mahasiswa"}


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ug_test_")
        storage.reset_backend()
        storage.DATA_DIR = self.tmp
        auth.init_data()

    def tearDown(self):
        storage.reset_backend()
        storage.DATA_DIR = storage.DEFAULT_DATA_DIR
        shutil.rmtree(self.tmp, ignore_errors=True)


class TestLoginAuth(BaseCase):
    def test_T01_login_berhasil(self):
        ok, msg, user = auth.login("admin", "Admin123")
        self.assertTrue(ok)
        self.assertEqual(user["role"], "admin")

    def test_T02_login_gagal_password_salah(self):
        auth.register("budi_01", "Rahasia123", "Rahasia123")
        ok, msg, user = auth.login("budi_01", "salah123")
        self.assertFalse(ok)
        self.assertIsNone(user)
        self.assertIn("Sisa percobaan: 2", msg)

    def test_T03_login_input_kosong(self):
        ok, msg, _ = auth.login("", "")
        self.assertFalse(ok)
        self.assertIn("wajib diisi", msg)

    def test_T04_akun_terkunci_setelah_3_kali_gagal(self):
        auth.register("budi_01", "Rahasia123", "Rahasia123")
        for _ in range(3):
            auth.login("budi_01", "salah123")
        ok, msg, _ = auth.login("budi_01", "Rahasia123")
        self.assertFalse(ok)
        self.assertTrue("dikunci" in msg.lower() or "terkunci" in msg.lower())

    def test_T05_password_tidak_disimpan_polos(self):
        auth.register("siti_01", "Rahasia123", "Rahasia123")
        raw = open(os.path.join(self.tmp, "users.json"), encoding="utf-8").read()
        self.assertNotIn("Rahasia123", raw)
        self.assertNotIn("Admin123", raw)

    def test_T06_registrasi_valid_dan_username_ganda(self):
        self.assertTrue(auth.register("siti_01", "Rahasia123", "Rahasia123")[0])
        ok, msg = auth.register("siti_01", "Rahasia123", "Rahasia123")
        self.assertFalse(ok)
        self.assertIn("sudah dipakai", msg)


class TestValidasi(BaseCase):
    def test_T07_validasi_registrasi(self):
        self.assertFalse(auth.register("", "Rahasia123", "Rahasia123")[0])
        self.assertFalse(auth.register("ab", "Rahasia123", "Rahasia123")[0])
        self.assertFalse(auth.register("siti_01", "pendek1", "pendek1")[0])
        self.assertFalse(auth.register("siti_01", "semuahuruf", "semuahuruf")[0])
        self.assertFalse(auth.register("siti_01", "Rahasia123", "Beda1234")[0])

    def test_T08_validasi_modul(self):
        self.assertFalse(validators.validate_module("", "Python", "Pemula", 30, "")[0])
        self.assertFalse(validators.validate_module("Judul Valid", "TidakAda", "Pemula", 30, "")[0])
        self.assertFalse(validators.validate_module("Judul Valid", "Python", "Master", 30, "")[0])
        self.assertFalse(validators.validate_module("Judul Valid", "Python", "Pemula", "abc", "")[0])
        self.assertFalse(validators.validate_module("Judul Valid", "Python", "Pemula", 0, "")[0])


class TestCRUD(BaseCase):
    def test_T09_tambah_modul(self):
        awal = len(modules.list_modules())
        ok, _ = modules.add_module(ADMIN, "Belajar Flask", "Python", "Menengah", 45, "Web mikro")
        self.assertTrue(ok)
        self.assertEqual(len(modules.list_modules()), awal + 1)

    def test_T10_mahasiswa_tidak_boleh_ubah_data(self):
        self.assertFalse(modules.add_module(MHS, "Modul X", "Python", "Pemula", 20, "")[0])
        self.assertFalse(modules.update_module(MHS, 1, "Modul X", "Python", "Pemula", 20, "")[0])
        self.assertFalse(modules.delete_module(MHS, 1)[0])

    def test_T11_pencarian_filter_sorting(self):
        daftar = modules.list_modules()
        py = modules.search_modules(daftar, query="python", bahasa="Python", sort_by="durasi", descending=False)
        self.assertTrue(all(m["bahasa"] == "Python" for m in py))
        self.assertEqual([m["durasi"] for m in py], sorted(m["durasi"] for m in py))
        kosong = modules.search_modules(daftar, query=" kata_tidak_mungkin_ada ")
        self.assertEqual(kosong, [])

    def test_T12_ubah_modul(self):
        ok, _ = modules.update_module(ADMIN, 1, "HTML5 Modern", "HTML", "Menengah", 55, "Diperbarui")
        self.assertTrue(ok)
        self.assertEqual(modules.get_module(1)["judul"], "HTML5 Modern")
        self.assertFalse(modules.update_module(ADMIN, 999, "Judul", "HTML", "Pemula", 20, "")[0])

    def test_T13_hapus_modul_dan_progres_terkait(self):
        progress.toggle_done("budi_01", 2)
        self.assertIn(2, progress.get_done("budi_01"))
        self.assertTrue(modules.delete_module(ADMIN, 2)[0])
        self.assertNotIn(2, progress.get_done("budi_01"))
        self.assertFalse(modules.delete_module(ADMIN, 2)[0])


class TestProgresDanFile(BaseCase):
    def test_T14_progres_dan_persentase(self):
        done = progress.toggle_done("budi_01", 1)
        self.assertEqual(progress.percent(done, [1, 2, 3, 4]), 25.0)
        done = progress.toggle_done("budi_01", 1)
        self.assertEqual(progress.percent(done, [1, 2, 3, 4]), 0.0)
        self.assertEqual(progress.percent([1], []), 0.0)

    def test_T15_data_tersimpan_dan_terbaca_kembali(self):
        modules.add_module(ADMIN, "Modul Tersimpan", "SQL", "Pemula", 25, "")
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "modules.json")))
        judul = [m["judul"] for m in modules.list_modules()]
        self.assertIn("Modul Tersimpan", judul)

    def test_T16_file_json_rusak_ditangani(self):
        with open(os.path.join(self.tmp, "modules.json"), "w", encoding="utf-8") as f:
            f.write("{bukan json valid")
        data = storage.load_json("modules.json", [{"id": 1, "judul": "Cadangan"}])
        self.assertEqual(data[0]["judul"], "Cadangan")
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "modules.json.corrupt")))

    def test_T17_folder_tidak_bisa_ditulis(self):
        penghalang = os.path.join(self.tmp, "bukan_folder")
        with open(penghalang, "w", encoding="utf-8") as f:
            f.write("x")
        storage.DATA_DIR = os.path.join(penghalang, "sub")
        storage.reset_backend()
        with self.assertRaises(StorageError):
            storage.save_json("uji.json", [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
