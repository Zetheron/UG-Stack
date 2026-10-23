# Panduan: Menayangkan UG-Stack di Vercel (Gratis) dengan Database Neon

> Status: **eksperimen**. WebSocket di Vercel Functions masih beta, dan titik masuk Flet untuk Vercel ini belum pernah saya jalankan
> di Vercel sungguhan. Ikuti langkah di bawah; bila gagal, kirim log (lihat bagian "Jika gagal") atau pakai cadangan Render (`PANDUAN_DEPLOY.md`).

## Kenapa build sebelumnya gagal
Log Vercel: `PYTHON_ENTRYPOINT_NOT_FOUND ... main.py does not export a top-level "app"`.
Vercel mencari variabel tingkat atas bernama `app` (aplikasi ASGI). Sekarang `main.py` mengekspornya: bila variabel lingkungan `VERCEL`
(otomatis diisi Vercel) ada, `app = flet.fastapi.app(main)`; di komputer dan APK nilainya `None` sehingga tidak mengganggu.

## Langkah 1 - Database Neon
1. Neon Console -> **New Project** -> salin **Connection string** (`postgresql://USER:PASSWORD@ep-xxxx.../neondb?sslmode=require`).
2. Tabel `ug_kv` dibuat otomatis saat aplikasi pertama kali dipakai.

## Langkah 2 - Project Vercel
1. Vercel -> **Add New -> Project** -> pilih repo `UG-Stack` (atau buka project yang sudah ada -> **Deployments -> Redeploy** setelah `git push`).
2. **Framework Preset**: biarkan terdeteksi (FastAPI) atau **Other**. Root Directory dikosongkan.
3. **Settings -> Environment Variables** (Production dan Preview):
   | Nama | Isi |
   |---|---|
   | `DATABASE_URL` | connection string Neon |
   | `UG_ADMIN_KEY` | kunci rahasia admin (teks acak min. 20 karakter; lihat `PANDUAN_ADMIN_KODE.md`) |
4. Berkas yang dipakai Vercel: `requirements.txt` (flet, fastapi, uvicorn, pg8000) dan `.python-version` (3.12). Tidak ada `vercel.json`.
5. Klik **Deploy**.

## Langkah 3 - Uji
1. Buka alamat `https://nama-proyek.vercel.app`. Pemuatan pertama bisa 5-20 detik (instance baru + klien Flet).
2. Daftar sebagai mahasiswa (NPM sebagai username), login, tambah progres.
3. Di Neon -> **SQL Editor** jalankan `select name from ug_kv;`. Harus muncul `users.json`, `progress.json`, dst. Itu bukti data tersimpan di database.
4. Tutup tab, buka lagi, login: data harus tetap ada. Admin: ketuk judul kartu login 7 kali lalu masukkan kode dari `tools/admin_generator.html`.

## Hal yang perlu Anda ketahui
- **Koneksi putus berkala.** WebSocket di Vercel ditutup saat fungsi mencapai durasi maksimum. Aplikasi memulihkan login otomatis
  (token sesi di perangkat, hash di database: 12 jam untuk mahasiswa/dosen, 30 menit untuk admin), tetapi isian form yang belum disimpan hilang.
- **Beberapa instance.** Kunci tulis hanya melindungi satu instance. Dua perubahan data yang persis bersamaan di instance berbeda bisa saling menimpa
  (jarang terjadi pada skala tugas). Perbaikan lanjutan: kunci di sisi database.
- **Kuota gratis.** Koneksi WebSocket memakai kuota yang sama dengan Vercel Functions; banyak pengguna terhubung lama dapat menghabiskannya.
  Pantau di Vercel -> Usage.
- **Beta.** Fitur WebSocket bisa berubah; jika bermasalah di Vercel, pindah ke Render (`PANDUAN_DEPLOY.md`) tanpa mengubah kode.
- **Keamanan.** Repo Anda publik: jangan menaruh `DATABASE_URL` atau `UG_ADMIN_KEY` di berkas. Isi hanya di Environment Variables Vercel.

## Jika gagal
- **Build gagal:** Deployments -> klik deployment -> **Build Logs**, kirim 20-30 baris terakhir.
- **Halaman putih / "reconnecting":** Deployments -> **Runtime Logs** (cari error saat Anda membuka halaman), dan Konsol browser (F12 -> Console, bagian merah).
- **"Database tidak dapat diakses":** periksa `DATABASE_URL` (harus utuh, berakhiran `?sslmode=require`).
