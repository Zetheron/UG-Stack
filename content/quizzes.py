"""Bank soal quiz (pilihan ganda). Tiap soal: pertanyaan, 4 opsi, indeks jawaban benar, penjelasan."""

PASS_PERCENT = 70


def Q(q, options, answer, explain):
    return {"q": q, "options": options, "answer": answer, "explain": explain}


QUIZZES = {
"html": [
 Q("Singkatan HTML adalah...", ["HyperText Markup Language", "High Tech Modern Language", "Hyperlink Text Mode Logic", "Home Tool Markup Language"], 0, "HTML = HyperText Markup Language."),
 Q("Tag yang benar untuk judul terbesar?", ["<head>", "<h1>", "<title>", "<big>"], 1, "<h1> adalah judul tingkat tertinggi."),
 Q("Atribut yang memberi teks alternatif pada gambar?", ["title", "src", "alt", "href"], 2, "alt dibaca pembaca layar dan tampil bila gambar gagal dimuat."),
 Q("Elemen untuk daftar bernomor?", ["<ul>", "<ol>", "<li>", "<dl>"], 1, "<ol> = ordered list; <ul> berpoin."),
],
"css": [
 Q("CSS dipakai untuk...", ["Mengatur tampilan halaman", "Menyimpan data", "Membuat basis data", "Menjalankan server"], 0, "CSS mengatur tampilan elemen HTML."),
 Q("Selector untuk kelas bernama kartu?", ["#kartu", ".kartu", "kartu", "*kartu"], 1, "Kelas memakai titik, id memakai #."),
 Q("Properti untuk ruang DI DALAM border elemen?", ["margin", "padding", "gap", "outline"], 1, "padding = ruang dalam; margin = ruang luar."),
 Q("Nilai display untuk tata letak fleksibel?", ["block", "inline", "flex", "static"], 2, "display: flex mengaktifkan Flexbox."),
],
"javascript": [
 Q("Kata kunci untuk konstanta yang tak boleh ditetapkan ulang?", ["var", "let", "const", "static"], 2, "const mencegah penetapan ulang variabel."),
 Q("Hasil dari typeof \"halo\"?", ["text", "string", "char", "object"], 1, "typeof \"halo\" menghasilkan \"string\"."),
 Q("Metode array untuk menyaring elemen?", ["map", "filter", "push", "join"], 1, "filter mengembalikan elemen yang memenuhi syarat."),
 Q("Cara memilih elemen dengan id=\"judul\"?", ["document.querySelector(\"#judul\")", "document.get(\"judul\")", "page.select(\"judul\")", "html.find(\".judul\")"], 0, "querySelector memakai selector CSS; id diawali #."),
],
"python": [
 Q("Output dari print(2 ** 3)?", ["6", "8", "9", "23"], 1, "** adalah operator pangkat: 2 pangkat 3 = 8."),
 Q("Struktur data pasangan kunci-nilai?", ["list", "tuple", "dict", "set"], 2, "dict menyimpan pasangan kunci dan nilai."),
 Q("Kata kunci untuk mendefinisikan function?", ["func", "def", "function", "lambda saja"], 1, "Function dibuat dengan def."),
 Q("Hasil len([1, 2, 3, 4])?", ["3", "4", "5", "Error"], 1, "len menghitung jumlah elemen: 4."),
],
"sql": [
 Q("Perintah untuk membaca data?", ["GET", "SELECT", "READ", "OPEN"], 1, "SELECT memilih data dari tabel."),
 Q("Klausa untuk menyaring baris?", ["FILTER", "HAVING saja", "WHERE", "ORDER BY"], 2, "WHERE menyaring baris sebelum dikelompokkan."),
 Q("Mengurutkan dari terbesar ke terkecil?", ["ORDER BY kolom DESC", "SORT kolom DOWN", "ORDER kolom MAX", "GROUP BY kolom DESC"], 0, "DESC = descending (menurun)."),
 Q("JOIN digunakan untuk...", ["Menghapus tabel", "Menggabungkan baris dari dua tabel", "Membuat index", "Menyalin database"], 1, "JOIN menggabungkan tabel berdasarkan kolom yang berhubungan."),
],
"java": [
 Q("Titik masuk program Java?", ["start()", "run()", "main()", "init()"], 2, "Eksekusi dimulai dari public static void main."),
 Q("Tipe data untuk teks?", ["char[] saja", "String", "text", "Str"], 1, "String adalah kelas untuk teks."),
 Q("Kata kunci untuk membuat objek?", ["make", "create", "new", "object"], 2, "new Kelas() membuat objek."),
 Q("Java dijalankan di...", ["JVM", "CLR", "Interpreter Python", "Browser"], 0, "Bytecode Java dijalankan oleh Java Virtual Machine."),
],
"php": [
 Q("Variabel PHP diawali dengan...", ["#", "$", "@", "&"], 1, "Contoh: $nama."),
 Q("Perintah untuk menampilkan teks?", ["echo", "show", "display", "write"], 0, "echo menampilkan keluaran."),
 Q("Variabel superglobal data formulir method POST?", ["$_FORM", "$_GET", "$_POST", "$_DATA"], 2, "$_POST berisi data formulir POST."),
 Q("Fungsi untuk mencegah XSS saat menampilkan input?", ["strip()", "htmlspecialchars()", "clean()", "escape_all()"], 1, "htmlspecialchars mengubah karakter HTML khusus."),
],
"c": [
 Q("Fungsi untuk mencetak ke layar di C?", ["print()", "cout", "printf()", "echo"], 2, "printf dari stdio.h."),
 Q("Format printf untuk bilangan bulat?", ["%f", "%d", "%s", "%c"], 1, "%d = int; %f = float; %s = string; %c = char."),
 Q("Operator untuk mengambil alamat variabel?", ["*", "&", "#", "@"], 1, "& mengambil alamat; * mengakses nilai pointer."),
 Q("Indeks pertama sebuah array di C?", ["0", "1", "-1", "Tergantung"], 0, "Indeks array dimulai dari 0."),
],
"cpp": [
 Q("Objek keluaran standar di C++?", ["printf", "cout", "echo", "System.out"], 1, "cout dari <iostream>."),
 Q("Array dinamis di STL?", ["vector", "stack saja", "map", "pair"], 0, "std::vector ukurannya bisa berubah."),
 Q("Fungsi STL untuk mengurutkan?", ["order()", "sort()", "arrange()", "rank()"], 1, "sort(begin, end) dari <algorithm>."),
 Q("Modifier agar anggota hanya bisa diakses di dalam kelas?", ["public", "private", "static", "const"], 1, "private membatasi akses ke dalam kelas."),
],
"csharp": [
 Q("Perintah mencetak teks ke konsol?", ["print()", "Console.WriteLine()", "echo", "System.out.println()"], 1, "Console.WriteLine dari namespace System."),
 Q("Untuk apa var di C#?", ["Tipe dinamis", "Inferensi tipe saat kompilasi", "Variabel global", "Konstanta"], 1, "var membuat kompilator menyimpulkan tipe; tetap bertipe statis."),
 Q("LINQ digunakan untuk...", ["Menggambar UI", "Mengolah dan menyaring koleksi", "Menjalankan SQL server", "Membuat kelas"], 1, "LINQ = Language Integrated Query."),
 Q("Sintaks properti otomatis?", ["{ get; set; }", "<get,set>", "(get)(set)", "[get set]"], 0, "Contoh: public string Nama { get; set; }."),
],
"react": [
 Q("Komponen React harus diawali huruf...", ["Kapital", "Kecil", "Angka", "Garis bawah"], 0, "Huruf kapital membedakannya dari tag HTML biasa."),
 Q("Hook untuk menyimpan state lokal?", ["useEffect", "useState", "useRef", "useMemo"], 1, "useState mengembalikan [nilai, fungsiUbah]."),
 Q("Data yang dikirim dari induk ke anak disebut...", ["state", "props", "hook", "ref"], 1, "Props bersifat hanya-baca."),
 Q("Properti wajib saat merender daftar dengan map?", ["id", "key", "index", "name"], 1, "key membantu React melacak item daftar."),
],
"mysql": [
 Q("Perintah membuat tabel baru?", ["NEW TABLE", "MAKE TABLE", "CREATE TABLE", "ADD TABLE"], 2, "CREATE TABLE nama (...)."),
 Q("Atribut nilai otomatis bertambah?", ["AUTO_INCREMENT", "AUTO_NUMBER", "SERIAL_ID", "INCREMENT"], 0, "AUTO_INCREMENT umum dipakai pada primary key."),
 Q("Fungsi agregat untuk menghitung jumlah baris?", ["SUM", "COUNT", "TOTAL", "LEN"], 1, "COUNT(*) menghitung baris."),
 Q("Untuk melihat rencana eksekusi query?", ["SHOW PLAN", "EXPLAIN", "ANALYZE ALL", "DEBUG"], 1, "EXPLAIN SELECT ... menampilkan rencana eksekusi."),
],
}


# ---------------------------------------------------------------- soal tambahan (total 8 per bahasa)
QUIZZES["html"].extend([
 Q("Elemen yang dipakai untuk membuat tautan?", ["<link>", "<a>", "<href>", "<url>"], 1, "<a> dengan atribut href membuat tautan."),
 Q("Tag penutup yang benar untuk paragraf?", ["</p>", "<p/>", "</paragraph>", "<end p>"], 0, "Setiap <p> ditutup dengan </p>."),
 Q("Atribut agar kolom formulir wajib diisi?", ["mandatory", "required", "needed", "must"], 1, "Atribut required membuat browser memvalidasi kolom."),
 Q("Elemen semantik untuk navigasi utama?", ["<nav>", "<menu-div>", "<top>", "<links>"], 0, "<nav> menandai kelompok tautan navigasi."),
])
QUIZZES["css"].extend([
 Q("Properti untuk mengubah warna teks?", ["font-color", "text-color", "color", "foreground"], 2, "Properti color mengatur warna teks."),
 Q("Satuan yang relatif terhadap lebar layar?", ["px", "vw", "pt", "cm"], 1, "vw = 1% dari lebar viewport."),
 Q("Pengaturan flex untuk memusatkan item pada sumbu utama?", ["justify-content: center", "align-text: center", "flex-center: true", "margin: flex"], 0, "justify-content mengatur perataan pada sumbu utama."),
 Q("Selector yang berlaku saat kursor berada di atas tombol?", ["button:active", "button:hover", "button:focus-only", "button:over"], 1, ":hover berlaku saat kursor berada di atas elemen."),
])
QUIZZES["javascript"].extend([
 Q("Hasil dari 2 + \"2\" di JavaScript?", ["4", "\"22\"", "22 (angka)", "Error"], 1, "Operator + menggabungkan string, jadi hasilnya \"22\"."),
 Q("Cara mengubah teks sebuah elemen?", ["el.textContent = \"Halo\"", "el.text(\"Halo\")", "el.write(\"Halo\")", "el.set(\"Halo\")"], 0, "textContent mengubah teks elemen."),
 Q("Metode array untuk menambah elemen di akhir?", ["push", "append", "add", "insertEnd"], 0, "push menambahkan elemen di akhir array."),
 Q("Operator yang membandingkan nilai dan tipe?", ["==", "=", "===", "!="], 2, "=== membandingkan nilai sekaligus tipe."),
])
QUIZZES["python"].extend([
 Q("Cara menulis komentar satu baris di Python?", ["// komentar", "# komentar", "-- komentar", "/* komentar */"], 1, "Komentar diawali tanda #."),
 Q("Hasil dari 7 // 2?", ["3.5", "3", "4", "2"], 1, "// adalah pembagian bulat: 7 // 2 = 3."),
 Q("Kata kunci untuk menangani kesalahan?", ["catch", "except", "error", "handle"], 1, "try ... except menangkap kesalahan."),
 Q("Tipe data yang tidak bisa diubah (immutable)?", ["list", "dict", "tuple", "set"], 2, "tuple tidak bisa diubah setelah dibuat."),
])
QUIZZES["sql"].extend([
 Q("Fungsi agregat untuk rata-rata?", ["MEAN", "AVG", "AVERAGE", "MID"], 1, "AVG menghitung rata-rata."),
 Q("Klausa untuk mengelompokkan baris?", ["GROUP BY", "SORT BY", "COLLECT", "CLUSTER"], 0, "GROUP BY mengelompokkan baris."),
 Q("Perintah untuk menghapus baris tertentu?", ["REMOVE", "DELETE", "DROP ROW", "CUT"], 1, "DELETE FROM ... WHERE menghapus baris."),
 Q("Kunci yang menghubungkan dua tabel?", ["Primary key", "Foreign key", "Unique index", "Check key"], 1, "Foreign key merujuk primary key tabel lain."),
])
QUIZZES["java"].extend([
 Q("Tipe data untuk bilangan desimal?", ["int", "double", "char", "boolean"], 1, "double menyimpan bilangan desimal."),
 Q("Koleksi dengan ukuran dinamis?", ["int[]", "ArrayList", "char", "Math"], 1, "ArrayList ukurannya dapat berubah."),
 Q("Kata kunci untuk pewarisan?", ["implements", "extends", "inherits", "super only"], 1, "extends membuat kelas turunan."),
 Q("Method yang berjalan otomatis saat objek dibuat?", ["Destruktor", "Konstruktor", "main", "finalize"], 1, "Konstruktor menginisialisasi objek baru."),
])
QUIZZES["php"].extend([
 Q("Operator penggabung string di PHP?", ["+", ".", "&", "||"], 1, "Titik (.) menggabungkan string."),
 Q("Fungsi untuk menghitung jumlah elemen array?", ["length()", "count()", "size()", "sizeof only"], 1, "count() menghitung elemen array."),
 Q("Superglobal untuk data dari URL?", ["$_POST", "$_GET", "$_URL", "$_QUERY"], 1, "$_GET berisi parameter URL."),
 Q("Cara menyertakan berkas lain?", ["include", "import", "using", "load"], 0, "include menyertakan berkas PHP lain."),
])
QUIZZES["c"].extend([
 Q("Tipe data untuk karakter tunggal?", ["char", "string", "text", "byte only"], 0, "char menyimpan satu karakter."),
 Q("Fungsi untuk alokasi memori dinamis?", ["new", "malloc", "alloc()", "create"], 1, "malloc mengalokasikan memori di heap."),
 Q("Hasil dari 10 % 3?", ["3", "1", "0", "3.33"], 1, "% adalah sisa pembagian: 10 % 3 = 1."),
 Q("Penanda akhir string di C?", ["\\n", "\\0", "EOF", "NULL string"], 1, "String berakhir dengan karakter null '\\0'."),
])
QUIZZES["cpp"].extend([
 Q("Operator untuk membuat objek di heap?", ["malloc", "new", "create", "alloc"], 1, "new mengalokasikan objek dinamis."),
 Q("Simbol untuk mendeklarasikan referensi (alias) variabel?", ["&", "*", "#", "@"], 0, "int &r = x; membuat referensi (alias)."),
 Q("Container yang menyimpan pasangan kunci-nilai?", ["vector", "map", "stack", "array"], 1, "std::map menyimpan pasangan kunci-nilai."),
 Q("Penulisan pewarisan publik?", ["class B : public A", "class B extends A", "class B inherits A", "class B -> A"], 0, "Pewarisan memakai titik dua dan penentu akses."),
])
QUIZZES["csharp"].extend([
 Q("Cara membuat daftar string?", ["List<string>", "string[] only", "ListString", "Array.new"], 0, "List<T> adalah daftar generik."),
 Q("Kata kunci untuk konstanta?", ["final", "const", "static only", "readonly-const"], 1, "const mendeklarasikan konstanta."),
 Q("Operator ?. dipakai untuk...", ["Pengecekan null yang aman", "Perulangan", "Pembagian", "Perbandingan string"], 0, "Null-conditional mencegah NullReferenceException."),
 Q("Perintah untuk menangkap kesalahan?", ["try/catch", "try/except", "on error", "rescue"], 0, "try/catch menangani pengecualian."),
])
QUIZZES["react"].extend([
 Q("Hook untuk efek samping seperti memuat data?", ["useState", "useEffect", "useProps", "useData"], 1, "useEffect berjalan setelah render."),
 Q("Sintaks JSX untuk menampilkan variabel nama?", ["{nama}", "${nama}", "<nama>", "[nama]"], 0, "Kurung kurawal menyisipkan ekspresi JavaScript."),
 Q("Penulisan atribut kelas CSS di JSX?", ["class", "className", "cssClass", "styleClass"], 1, "JSX memakai className."),
 Q("State sebaiknya diubah dengan...", ["Fungsi setter dari useState", "Langsung mengubah variabelnya", "document.getElementById", "window.state"], 0, "Gunakan fungsi setter agar React merender ulang."),
])
QUIZZES["mysql"].extend([
 Q("Perintah untuk menambah kolom ke tabel?", ["ALTER TABLE ... ADD", "UPDATE TABLE", "INSERT COLUMN", "MODIFY DB"], 0, "ALTER TABLE ... ADD COLUMN menambah kolom."),
 Q("Tipe data untuk tanggal?", ["DATE", "DAYTEXT", "TIMESTR", "CAL"], 0, "DATE menyimpan tanggal."),
 Q("Klausa untuk membatasi jumlah baris?", ["LIMIT", "TOP only", "MAX ROWS", "FETCH ALL"], 0, "LIMIT n membatasi jumlah baris."),
 Q("Fungsi untuk menggabungkan teks?", ["CONCAT", "JOINSTR", "MERGE", "APPEND"], 0, "CONCAT menggabungkan string."),
])

# ---- 20_SOAL_PER_BAHASA
QUIZZES["html"].extend([
 Q('Tag untuk menyisipkan baris baru tanpa paragraf baru?', ['<lb>', '<br>', '<break>', '<newline>'], 1, '<br> membuat pindah baris tunggal.'),
 Q('Atribut pada <a> untuk membuka tautan di tab baru?', ['target="_blank"', 'newtab="true"', 'open="tab"', 'href="_new"'], 0, 'target="_blank" membuka tautan di tab baru.'),
 Q('Elemen HTML5 untuk bagian kaki halaman?', ['<bottom>', '<foot>', '<footer>', '<end>'], 2, '<footer> adalah elemen semantik bagian bawah halaman.'),
 Q('Tag yang benar untuk membuat daftar berpoin (bullet)?', ['<ol>', '<ul>', '<dl>', '<list>'], 1, '<ul> membuat unordered list.'),
 Q('Tag untuk membuat sel judul pada tabel HTML?', ['<td>', '<th>', '<tr>', '<thead>'], 1, '<th> mendefinisikan header cell pada tabel.'),
 Q('Tipe input untuk memilih tanggal pada formulir HTML?', ['type="calendar"', 'type="date"', 'type="time"', 'type="day"'], 1, '<input type="date"> menampilkan pemilih tanggal.'),
 Q('Elemen yang membungkus metadata dokumen seperti <title> dan <meta>?', ['<meta>', '<head>', '<header>', '<body>'], 1, '<head> menyimpan informasi metadata dokumen.'),
 Q('Atribut untuk menggabungkan dua kolom pada sel tabel?', ['rowspan', 'colspan', 'merge', 'span'], 1, 'colspan menggabungkan beberapa kolom tabel.'),
 Q('Tag HTML untuk menampilkan teks tebal yang memiliki penekanan penting?', ['<b>', '<strong>', '<bold>', '<em>'], 1, '<strong> menandai teks penting dan ditampilkan tebal.'),
 Q('Elemen untuk membuat daftar pilihan dropdown?', ['<input>', '<select>', '<option-list>', '<list>'], 1, '<select> bersama <option> membentuk menu dropdown.'),
 Q('Atribut untuk menampilkan teks petunjuk di dalam kolom input?', ['hint', 'placeholder', 'label', 'value'], 1, 'placeholder menampilkan teks bayangan sebelum kolom diisi.'),
 Q('Deklarasi paling atas untuk menandai dokumen HTML5?', ['<!DOCTYPE html>', '<html5>', '<!HTML>', '<doctype>'], 0, '<!DOCTYPE html> mengaktifkan mode standar HTML5.'),
])
QUIZZES["css"].extend([
 Q('Properti untuk mengubah jenis huruf (font)?', ['font-style', 'font-family', 'text-font', 'typeface'], 1, 'font-family mengatur jenis huruf teks.'),
 Q('Properti untuk membuat sudut kotak menjadi melengkung?', ['corner-radius', 'border-radius', 'round-corner', 'box-curve'], 1, 'border-radius mengatur kelengkungan sudut elemen.'),
 Q('Nilai position agar elemen tetap menempel di layar saat halaman di-scroll?', ['static', 'relative', 'fixed', 'float'], 2, 'position: fixed menahan posisi elemen terhadap layar.'),
 Q('Properti untuk mengatur jarak di LUAR garis batas (border) elemen?', ['padding', 'margin', 'spacing', 'border-space'], 1, 'margin mengatur ruang di luar border.'),
 Q('Properti untuk menghilangkan garis bawah pada tautan <a>?', ['text-decoration: none', 'underline: off', 'font-line: none', 'link-style: plain'], 0, 'text-decoration: none menghapus garis bawah tautan.'),
 Q('Properti untuk mengatur ukuran teks?', ['text-size', 'font-size', 'size', 'font-scale'], 1, 'font-size mengatur ukuran huruf.'),
 Q('Nilai display untuk menyembunyikan elemen sepenuhnya dari tata letak?', ['display: hidden', 'display: none', 'visibility: zero', 'opacity: hide'], 1, 'display: none menyembunyikan elemen tanpa menyisakan ruang.'),
 Q('Properti Flexbox untuk mengubah arah susunan menjadi vertikal (kolom)?', ['flex-direction: column', 'flex-wrap: vertical', 'align-items: column', 'justify: vertical'], 0, 'flex-direction: column menyusun item dari atas ke bawah.'),
 Q('Properti untuk mengatur tingkat transparansi sebuah elemen?', ['alpha', 'opacity', 'transparent', 'filter-alpha'], 1, 'opacity bernilai antara 0 hingga 1.'),
 Q('Properti untuk memberi bayangan pada kotak elemen?', ['shadow', 'box-shadow', 'text-shadow', 'border-shadow'], 1, 'box-shadow menambahkan efek bayangan pada kotak.'),
 Q('Selector CSS yang memilih semua elemen di dalam halaman?', ['*', 'all', 'body', '#all'], 0, 'Selector universal * memilih seluruh elemen.'),
 Q('Properti untuk menentukan urutan tumpukan elemen yang tumpang-tindih?', ['stack-order', 'z-index', 'layer', 'depth'], 1, 'z-index mengatur urutan tumpukan elemen.'),
])
QUIZZES["javascript"].extend([
 Q('Metode untuk mengubah teks JSON menjadi objek JavaScript?', ['JSON.stringify()', 'JSON.parse()', 'JSON.toObject()', 'JSON.read()'], 1, 'JSON.parse() mengurai string JSON menjadi objek.'),
 Q('Kata kunci untuk mendeklarasikan fungsi asinkron?', ['await', 'async', 'promise', 'defer'], 1, 'async ditempatkan sebelum function.'),
 Q('Metode array yang menghasilkan array baru dari hasil pemanggilan fungsi pada tiap elemen?', ['forEach', 'map', 'reduce', 'find'], 1, 'map() memetakan setiap elemen ke nilai baru.'),
 Q('Properti untuk mengetahui jumlah elemen di dalam array?', ['size', 'count', 'length', 'total'], 2, 'arr.length mengembalikan panjang array.'),
 Q('Fungsi untuk menjalankan kode satu kali setelah jeda waktu tertentu?', ['setInterval()', 'setTimeout()', 'delay()', 'wait()'], 1, 'setTimeout(fn, ms) menunda eksekusi fungsi.'),
 Q('Operator untuk memberikan nilai cadangan bila kiri null atau undefined?', ['??', '||=', '&&', '::'], 0, 'Nullish coalescing operator (??) memeriksa null/undefined.'),
 Q('Metode untuk menghapus elemen TERAKHIR dari sebuah array?', ['shift()', 'pop()', 'slice()', 'removeLast()'], 1, 'pop() mengambil dan menghapus elemen terakhir array.'),
 Q('Cara menulis template literal yang mendukung interpolasi variabel?', ["'Halo ${nama}'", '"Halo ${nama}"', '`Halo ${nama}`', '(Halo ${nama})'], 2, 'Template literal memakai tanda backtick (` `).'),
 Q('Metode untuk mencetak pesan ke konsol browser?', ['print()', 'console.log()', 'document.log()', 'system.out()'], 1, 'console.log() menampilkan pesan di konsol.'),
 Q('Nilai boolean dari Boolean(0) di JavaScript adalah...', ['true', 'false', 'null', 'NaN'], 1, 'Angka 0 termasuk nilai falsy sehingga bernilai false.'),
 Q('Metode string untuk mengubah semua huruf menjadi kapital?', ['toUpper()', 'toUpperCase()', 'upperCase()', 'capitalize()'], 1, 'str.toUpperCase() mengubah huruf menjadi kapital.'),
 Q('Peristiwa (event) yang dipicu saat formulir dikirim?', ['click', 'change', 'submit', 'load'], 2, 'Event submit terjadi ketika form dikirim.'),
])
QUIZZES["python"].extend([
 Q('Metode list untuk menambahkan satu elemen di urutan paling akhir?', ['add()', 'append()', 'push()', 'insert_last()'], 1, 'list.append(x) menambah elemen di ujung list.'),
 Q('Hasil dari ekspresi [x * 2 for x in [1, 2, 3]] adalah...', ['[1, 2, 3]', '[2, 4, 6]', '[3, 4, 5]', '(2, 4, 6)'], 1, 'List comprehension mengalikan tiap elemen dengan 2.'),
 Q('Metode dictionary untuk mengambil nilai dengan aman tanpa memicu KeyError?', ['d.find(k)', 'd.get(k)', 'd.fetch(k)', 'd.read(k)'], 1, 'd.get(k) mengembalikan None bila kunci tidak ditemukan.'),
 Q('Kata kunci untuk mengimpor pustaka/modul di Python?', ['include', 'using', 'import', 'require'], 2, 'import digunakan untuk memuat modul.'),
 Q("Hasil dari 'python'.upper() adalah...", ["'Python'", "'PYTHON'", "'python'", 'Error'], 1, 'upper() mengubah semua karakter menjadi huruf besar.'),
 Q('Fungsi bawaan untuk menghasilkan deretan angka berurutan?', ['seq()', 'range()', 'numbers()', 'loop()'], 1, 'range(start, stop) menghasilkan urutan bilangan bulat.'),
 Q('Operator untuk memeriksa apakah suatu nilai ada di dalam list?', ['has', 'in', 'inside', 'exists'], 1, 'Operator in memeriksa keanggotaan elemen.'),
 Q('Struktur data Python yang hanya menyimpan elemen unik (tanpa duplikat)?', ['list', 'tuple', 'set', 'sequence'], 2, 'set menyimpan himpunan elemen unik.'),
 Q('Nilai yang dikembalikan fungsi Python jika tidak memiliki pernyataan return?', ['0', 'False', 'None', "''"], 2, 'Tanpa return, fungsi mengembalikan None.'),
 Q('Cara membuka berkas agar otomatis tertutup setelah selesai?', ["open('a.txt')", "with open('a.txt') as f:", "try open('a.txt'):", "file('a.txt')"], 1, 'Blok with menjamin berkas ditutup secara otomatis.'),
 Q('Hasil dari [10, 20, 30][-1] adalah...', ['10', '20', '30', 'IndexError'], 2, 'Indeks -1 mengambil elemen terakhir.'),
 Q('Fungsi bawaan untuk mengurutkan iterable dan menghasilkan list baru?', ['sort()', 'sorted()', 'order()', 'arrange()'], 1, 'sorted(iterable) mengembalikan list baru yang terurut.'),
])
QUIZZES["sql"].extend([
 Q('Perintah untuk menambahkan baris baru ke dalam tabel?', ['ADD INTO', 'INSERT INTO', 'CREATE ROW', 'PUT INTO'], 1, 'INSERT INTO nama_tabel (...) VALUES (...) menambah baris.'),
 Q('Perintah untuk mengubah nilai kolom pada baris yang sudah ada?', ['MODIFY', 'CHANGE', 'UPDATE', 'ALTER ROW'], 2, 'UPDATE nama_tabel SET kolom = nilai WHERE ...'),
 Q('Klausa untuk menyaring hasil kelompok setelah GROUP BY?', ['WHERE', 'HAVING', 'FILTER', 'LIMIT'], 1, 'HAVING menyaring kelompok hasil agregasi.'),
 Q('Kata kunci untuk menghilangkan baris duplikat pada hasil SELECT?', ['UNIQUE', 'DISTINCT', 'SINGLE', 'DIFFERENT'], 1, 'SELECT DISTINCT hanya menampilkan nilai yang unik.'),
 Q("Operator pada WHERE untuk mencocokkan pola teks (mis. 'A%')?", ['MATCH', 'LIKE', 'CONTAINS', 'SIMILAR'], 1, 'LIKE digunakan bersama wildcard % dan _.'),
 Q('Fungsi agregat untuk mencari nilai paling besar pada sebuah kolom?', ['TOP()', 'HIGH()', 'MAX()', 'UPPER()'], 2, 'MAX(kolom) mengembalikan nilai maksimum.'),
 Q('Fungsi agregat untuk menjumlahkan seluruh nilai numerik pada kolom?', ['COUNT()', 'SUM()', 'TOTAL()', 'ADD()'], 1, 'SUM(kolom) menghitung total penjumlahan.'),
 Q('Kondisi yang benar untuk memeriksa apakah kolom bernilai kosong (NULL)?', ['kolom = NULL', 'kolom == NULL', 'kolom IS NULL', 'ISNULL(kolom)'], 2, 'Gunakan IS NULL atau IS NOT NULL di SQL.'),
 Q('Jenis JOIN yang menampilkan semua baris dari tabel kiri?', ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'CROSS JOIN'], 1, 'LEFT JOIN mempertahankan seluruh baris tabel kiri.'),
 Q('Perintah untuk menghapus seluruh struktur tabel dari database?', ['DELETE TABLE', 'REMOVE TABLE', 'DROP TABLE', 'CLEAR TABLE'], 2, 'DROP TABLE menghapus tabel beserta strukturnya.'),
 Q('Operator untuk memilih nilai di dalam rentang tertentu secara inklusif?', ['WITHIN', 'RANGE', 'BETWEEN', 'INSIDE'], 2, 'BETWEEN a AND b memeriksa nilai dari a sampai b.'),
 Q('Kata kunci untuk memberi nama alias pada kolom atau tabel?', ['ALIAS', 'AS', 'NAME', 'TO'], 1, 'SELECT kolom AS nama_alias FROM tabel.'),
])
QUIZZES["java"].extend([
 Q('Kata kunci untuk membuat konstanta di Java?', ['const', 'final', 'static', 'immutable'], 1, 'final mencegah nilai variabel diubah kembali.'),
 Q('Kata kunci untuk menerapkan sebuah interface pada kelas?', ['extends', 'implements', 'uses', 'inherits'], 1, 'class A implements B menerapkan kontrak interface.'),
 Q('Metode untuk mengetahui panjang teks pada objek String?', ['str.size', 'str.length()', 'str.count()', 'len(str)'], 1, 'String memiliki method length().'),
 Q('Cara yang benar untuk membandingkan kesamaan isi dua String di Java?', ['s1 == s2', 's1.equals(s2)', 's1.same(s2)', 'String.match(s1, s2)'], 1, 'equals() membandingkan isi karakter.'),
 Q('Blok yang selalu dijalankan setelah try/catch?', ['always', 'finally', 'end', 'ensure'], 1, 'Blok finally selalu dieksekusi.'),
 Q('Kata kunci yang merujuk pada objek saat ini di dalam method kelas?', ['self', 'this', 'me', 'current'], 1, 'this mengacu pada instans objek saat ini.'),
 Q('Tipe data primitif untuk menyimpan nilai benar atau salah di Java?', ['bool', 'boolean', 'bit', 'truth'], 1, 'Java menggunakan kata kunci boolean.'),
 Q('Paket standar yang perlu diimpor untuk menggunakan ArrayList?', ['java.io.ArrayList', 'java.util.ArrayList', 'java.lang.ArrayList', 'java.net.ArrayList'], 1, 'ArrayList berada di dalam paket java.util.'),
 Q('Modifier agar method dapat dipanggil langsung lewat nama kelas?', ['public', 'final', 'static', 'abstract'], 2, 'Method static milik kelas, bukan objek individual.'),
 Q('Kata kunci untuk memanggil konstruktor atau method milik kelas induk?', ['parent', 'base', 'super', 'upper'], 2, 'super merujuk pada superclass.'),
 Q('Tipe bilangan bulat 64-bit di Java adalah...', ['int', 'short', 'long', 'double'], 2, 'long berukuran 64-bit.'),
 Q('Ekstensi berkas hasil kompilasi bytecode Java adalah...', ['.java', '.class', '.exe', '.jaronly'], 1, 'javac menghasilkan berkas bytecode berekstensi .class.'),
])
QUIZZES["php"].extend([
 Q('Fungsi untuk memeriksa apakah sebuah variabel sudah diatur dan tidak null?', ['defined()', 'isset()', 'exists()', 'has_val()'], 1, 'isset($var) bernilai true bila variabel ada dan bukan null.'),
 Q('Fungsi untuk mengubah array menjadi teks JSON di PHP?', ['json_stringify()', 'json_encode()', 'to_json()', 'array_json()'], 1, 'json_encode() menghasilkan string berformat JSON.'),
 Q('Variabel superglobal untuk menyimpan data sesi pengguna lintas halaman?', ['$_COOKIE', '$_SESSION', '$_SERVER', '$_USER'], 1, '$_SESSION menyimpan state sesi di sisi server.'),
 Q('Fungsi yang wajib dipanggil sebelum menggunakan $_SESSION?', ['session_begin()', 'session_start()', 'start_session()', 'init_session()'], 1, 'session_start() memulai atau melanjutkan sesi.'),
 Q('Fungsi untuk menghapus spasi di awal dan akhir string?', ['strip()', 'trim()', 'clean()', 'cut()'], 1, 'trim($str) memangkas spasi di kedua ujung string.'),
 Q('Fungsi untuk mengubah teks JSON menjadi array/objek di PHP?', ['json_parse()', 'json_decode()', 'json_read()', 'from_json()'], 1, 'json_decode() mengurai string JSON.'),
 Q('Fungsi untuk menghitung panjang karakter sebuah string?', ['len()', 'strlen()', 'count()', 'size()'], 1, 'strlen($s) mengembalikan panjang string.'),
 Q('Fungsi untuk memecah string menjadi array berdasarkan pemisah?', ['split()', 'explode()', 'break()', 'divide()'], 1, "explode(',', $teks) memecah string menjadi array."),
 Q('Operator perbandingan identik (nilai dan tipe data harus sama) di PHP?', ['==', '===', 'eq', ':='], 1, '=== memeriksa kesamaan nilai sekaligus tipe datanya.'),
 Q('Ekstensi modern bawaan PHP untuk koneksi database yang aman?', ['mysql_old', 'PDO', 'db_link', 'sql_connect'], 1, 'PDO mendukung prepared statements.'),
 Q('Fungsi untuk mengubah semua huruf menjadi huruf kecil di PHP?', ['lower()', 'strtolower()', 'toLower()', 'small()'], 1, 'strtolower($s) mengubah string ke huruf kecil.'),
 Q('Fungsi untuk menambahkan elemen di akhir array pada PHP?', ['array_add()', 'array_push()', 'push_back()', 'append()'], 1, 'array_push($arr, $val) menambah elemen di akhir array.'),
])
QUIZZES["c"].extend([
 Q('Fungsi untuk membebaskan memori yang dialokasikan oleh malloc()?', ['delete()', 'free()', 'release()', 'clear()'], 1, 'free(ptr) mengembalikan memori heap ke sistem.'),
 Q('Header yang diperlukan untuk fungsi string seperti strlen dan strcpy?', ['<stdio.h>', '<stdlib.h>', '<string.h>', '<math.h>'], 2, '<string.h> mendeklarasikan fungsi manipulasi string.'),
 Q('Operator untuk mengetahui ukuran memori (byte) dari suatu tipe data?', ['lengthof', 'sizeof', 'bytes()', 'memsize'], 1, 'sizeof(int) mengembalikan ukuran tipe int dalam byte.'),
 Q('Kata kunci untuk mendefinisikan struktur data gabungan di C?', ['class', 'struct', 'record', 'object'], 1, 'struct mengelompokkan beberapa variabel dalam satu blok.'),
 Q('Nilai pointer yang menandakan pointer tidak menunjuk ke alamat mana pun?', ['ZERO', 'EMPTY', 'NULL', 'VOID'], 2, 'NULL adalah penanda pointer kosong.'),
 Q('Fungsi dari <string.h> untuk membandingkan dua buah string?', ['str_eq()', 'strcmp()', 'strmatch()', 'compare()'], 1, 'strcmp(a, b) mengembalikan 0 jika kedua string sama.'),
 Q('Direktif praprosesor untuk mendefinisikan makro atau konstanta simbolik?', ['#const', '#define', '#macro', '#let'], 1, '#define NAMA nilai dijalankan sebelum kompilasi.'),
 Q('Operator untuk mengakses anggota struct melalui variabel pointer?', ['.', '->', '::', '=>'], 1, 'ptr->field setara dengan (*ptr).field.'),
 Q('Format specifier printf untuk menampilkan satu karakter (char)?', ['%s', '%c', '%d', '%x'], 1, '%c mencetak sebuah karakter tunggal.'),
 Q('Pernyataan untuk langsung keluar dari perulangan for atau while?', ['stop', 'exit_loop', 'break', 'return_loop'], 2, 'break menghentikan perulangan terdekat.'),
 Q('Pernyataan untuk melewati sisa iterasi saat ini dan lanjut ke iterasi berikutnya?', ['skip', 'next', 'continue', 'pass'], 2, 'continue melompat ke evaluasi iterasi selanjutnya.'),
 Q('Nilai kembalian main() yang menandakan program selesai dengan sukses?', ['1', '-1', '0', '200'], 2, 'return 0; menandakan eksekusi berakhir tanpa error.'),
])
QUIZZES["cpp"].extend([
 Q('Pustaka header yang diperlukan untuk menggunakan std::vector?', ['<array>', '<list>', '<vector>', '<collection>'], 2, '#include <vector> menyediakan kontainer std::vector.'),
 Q('Metode pada std::vector untuk menambahkan elemen di bagian akhir?', ['add()', 'append()', 'push_back()', 'insert_end()'], 2, 'v.push_back(x) menambah elemen di ujung vector.'),
 Q('Metode pada std::vector untuk mengetahui jumlah elemen di dalamnya?', ['length()', 'count()', 'size()', 'capacity_only()'], 2, 'v.size() mengembalikan banyaknya elemen saat ini.'),
 Q('Kata kunci untuk mengizinkan fungsi di-override pada kelas turunan?', ['override_able', 'virtual', 'dynamic', 'abstract'], 1, 'virtual mengaktifkan dynamic dispatch (polimorfisme).'),
 Q('Smart pointer modern C++ yang memiliki kepemilikan tunggal atas objek?', ['auto_ptr', 'unique_ptr', 'raw_ptr', 'single_ptr'], 1, 'std::unique_ptr otomatis menghapus objek saat keluar cakupan.'),
 Q('Kata kunci untuk membuat fungsi atau kelas generik di C++?', ['generic', 'template', 'typename_only', 'any'], 1, 'template <typename T> mendefinisikan kode generik.'),
 Q('Metode khusus yang dipanggil otomatis saat objek dihancurkan?', ['initialize()', '~NamaKelas()', 'finalize()', 'destroy()'], 1, 'Destruktor diawali tanda ~ dan membersihkan sumber daya.'),
 Q('Operator resolusi cakupan (scope resolution) di C++ adalah...', ['.', '->', '::', ':'], 2, 'Contoh: std::cout menggunakan operator ::.'),
 Q('Kontainer STL yang menyimpan elemen unik secara terurut?', ['std::vector', 'std::set', 'std::deque', 'std::array'], 1, 'std::set menyimpan elemen unik dalam urutan terurut.'),
 Q('Kata kunci C++11 agar kompilator menyimpulkan tipe variabel secara otomatis?', ['var', 'let', 'auto', 'def'], 2, 'auto menyimpulkan tipe dari ekspresi inisialisasi.'),
 Q('Operator untuk melepaskan memori yang dialokasikan dengan new?', ['free', 'delete', 'remove', 'dispose'], 1, 'delete membebaskan objek yang dibuat dengan new.'),
 Q('Objek standar C++ untuk membaca masukan dari keyboard?', ['scanf', 'cin', 'input', 'console.in'], 1, 'std::cin >> variabel membaca input dari aliran standar.'),
])
QUIZZES["csharp"].extend([
 Q('Kata kunci untuk menandai metode asinkron yang dapat memakai await di C#?', ['future', 'async', 'task', 'defer'], 1, 'async digunakan bersama tipe kembalian Task.'),
 Q('Metode LINQ untuk mengambil elemen pertama atau nilai default bila kosong?', ['First()', 'FirstOrDefault()', 'Top()', 'TakeOne()'], 1, 'FirstOrDefault() aman saat koleksi kosong.'),
 Q('Simbol untuk menerapkan pewarisan atau interface pada kelas di C#?', ['extends', ':', 'implements', 'inherits'], 1, 'C# menggunakan tanda titik dua (:).'),
 Q('Awalan untuk menggabungkan variabel langsung di dalam string (interpolation)?', ['$', '@', '#', '%'], 0, 'Awalan $ mengaktifkan interpolasi ekspresi di dalam { }.'),
 Q('Metode pada List<T> untuk menambahkan item baru?', ['append()', 'push()', 'Add()', 'InsertLast()'], 2, 'list.Add(item) menambahkan elemen ke List<T>.'),
 Q('Properti untuk mengetahui jumlah elemen pada array di C#?', ['Count', 'Size', 'Length', 'Total'], 2, 'Array di C# menggunakan properti Length.'),
 Q('Koleksi generik untuk menyimpan pasangan kunci dan nilai di C#?', ['HashMap<K,V>', 'Dictionary<TKey, TValue>', 'Map<K,V>', 'PairList<K,V>'], 1, 'Dictionary<TKey, TValue> terdapat di System.Collections.Generic.'),
 Q('Kata kunci untuk mendeklarasikan ruang nama di C#?', ['package', 'module', 'namespace', 'scope'], 2, 'namespace mengelompokkan kelas agar tidak bentrok.'),
 Q('Operator untuk memberikan nilai cadangan jika ekspresi di kiri bernilai null?', ['?:', '??', '!!', '&&'], 1, 'Null-coalescing operator (??) mengembalikan nilai kanan bila kiri null.'),
 Q('Blok di dalam try/catch yang pasti dijalankan untuk membersihkan resource?', ['ensure', 'finally', 'always', 'cleanup'], 1, 'finally selalu dijalankan baik ada exception maupun tidak.'),
 Q('Pernyataan untuk membebaskan objek IDisposable secara otomatis di akhir blok?', ['with', 'using', 'dispose', 'auto'], 1, 'using memastikan metode Dispose() dipanggil otomatis.'),
 Q('Metode String untuk menghapus spasi di awal dan akhir teks?', ['Strip()', 'Trim()', 'Clean()', 'Cut()'], 1, 'teks.Trim() menghapus whitespace di ujung kiri dan kanan.'),
])
QUIZZES["react"].extend([
 Q('Penulisan singkat React Fragment untuk mengelompokkan elemen tanpa div ekstra?', ['<Container>', '<>...</>', '<Group>', '<Wrap>'], 1, '<>...</> mengelompokkan elemen tanpa node DOM tambahan.'),
 Q('Hook untuk menyimpan referensi ke elemen DOM tanpa memicu render ulang?', ['useState', 'useRef', 'useMemo', 'useDom'], 1, 'useRef mengembalikan objek { current } yang persisten.'),
 Q('Argumen kedua berupa [] pada useEffect(fn, []) membuat efek dijalankan...', ['Setiap detik', 'Sekali saat mount', 'Tidak pernah', 'Saat unmount saja'], 1, 'Dependency array kosong [] membuat efek hanya berjalan saat mount.'),
 Q('Atribut event yang benar untuk menangani klik tombol di JSX?', ['onclick', 'onClick', 'on-click', '@click'], 1, 'JSX menggunakan penamaan camelCase seperti onClick.'),
 Q('Hook untuk berbagi data lintas pohon komponen tanpa mengoper props berlapis?', ['useShare', 'useContext', 'useGlobal', 'useTree'], 1, 'useContext membaca nilai dari Context terdekat.'),
 Q('Hook untuk menyimpan hasil perhitungan berat di antara render?', ['useCache', 'useMemo', 'useEffect', 'useRef'], 1, 'useMemo(fn, deps) melakukan memoization nilai.'),
 Q('Hook untuk mengoptimalkan fungsi callback agar referensinya stabil?', ['useFn', 'useCallback', 'useRefFn', 'useAction'], 1, 'useCallback(fn, deps) menyimpan referensi fungsi.'),
 Q('Di dalam JSX, bagaimana cara menyisipkan komentar?', ['<!-- komentar -->', '{/* komentar */}', '// komentar', '## komentar'], 1, 'Gunakan {/* ... */} untuk menulis komentar di dalam JSX.'),
 Q('Event handler untuk membaca perubahan teks pada elemen <input> di React?', ['onInputText', 'onChange', 'onType', 'onModify'], 1, 'onChange dipanggil setiap kali nilai input berubah.'),
 Q('Komponen input yang nilainya dikendalikan sepenuhnya oleh state React disebut...', ['Uncontrolled', 'Controlled', 'Static', 'Passive'], 1, 'Controlled Component mengikat value ke state.'),
 Q('Perintah untuk mengekspor komponen sebagai default export?', ['export default App;', 'module.share(App);', 'public App;', 'return default App;'], 0, 'export default mengizinkan impor langsung dari modul.'),
 Q('Metode yang umum dipakai di dalam JSX untuk merender array menjadi daftar elemen?', ['forEach()', 'map()', 'reduce()', 'for()'], 1, 'array.map(item => <li key={item.id}>...</li>).'),
])
QUIZZES["mysql"].extend([
 Q('Perintah untuk menampilkan daftar seluruh database di server MySQL?', ['LIST DATABASES;', 'SHOW DATABASES;', 'SELECT DATABASES;', 'DISPLAY DB;'], 1, 'SHOW DATABASES; menampilkan semua basis data.'),
 Q('Perintah untuk memilih database yang akan digunakan?', ['SELECT DB;', 'USE nama_db;', 'OPEN nama_db;', 'SET nama_db;'], 1, 'USE nama_db; mengaktifkan basis data tersebut.'),
 Q('Perintah untuk melihat struktur kolom dari sebuah tabel?', ['SHOW COLUMNS;', 'DESCRIBE tabel;', 'VIEW TABLE;', 'STRUCT tabel;'], 1, 'DESCRIBE tabel; menampilkan kolom, tipe, dan kunci.'),
 Q('Klausa untuk melewati sejumlah baris pertama saat paginasi dengan LIMIT?', ['SKIP', 'OFFSET', 'START', 'AFTER'], 1, 'LIMIT 10 OFFSET 20 melewati 20 baris pertama.'),
 Q('Storage engine bawaan MySQL yang mendukung transaksi ACID dan foreign key?', ['MyISAM', 'InnoDB', 'Memory', 'CSV'], 1, 'InnoDB adalah mesin penyimpanan utama di MySQL modern.'),
 Q('Fungsi MySQL untuk mendapatkan tanggal dan waktu saat ini?', ['TODAY()', 'NOW()', 'CURRENT()', 'CLOCK()'], 1, 'NOW() mengembalikan tanggal dan waktu saat ini.'),
 Q('Constraint untuk memastikan nilai di dalam sebuah kolom tidak boleh kembar?', ['PRIMARY', 'UNIQUE', 'SINGLE', 'DISTINCT_KEY'], 1, 'UNIQUE menolak duplikasi nilai pada kolom tersebut.'),
 Q('Constraint agar sebuah kolom tidak boleh berisi nilai NULL?', ['REQUIRED', 'NOT NULL', 'NO EMPTY', 'MANDATORY'], 1, 'NOT NULL mewajibkan kolom selalu memiliki nilai.'),
 Q('Perintah untuk mengosongkan seluruh isi tabel dengan cepat?', ['DROP TABLE', 'TRUNCATE TABLE', 'CLEAR TABLE', 'REMOVE ALL'], 1, 'TRUNCATE TABLE menghapus semua baris dan mereset AUTO_INCREMENT.'),
 Q('Tipe data MySQL untuk menyimpan teks panjang hingga 65.535 karakter?', ['CHAR(255)', 'TEXT', 'TINYTEXT', 'STRING_LONG'], 1, 'TEXT cocok untuk artikel atau deskripsi panjang.'),
 Q('Fungsi untuk mengganti nilai NULL menjadi nilai cadangan pada hasil query?', ['NULLTO()', 'IFNULL()', 'DEFAULT()', 'REPLACENULL()'], 1, 'IFNULL(kolom, 0) mengembalikan 0 bila kolom bernilai NULL.'),
 Q('Perintah transaksi untuk menyimpan seluruh perubahan secara permanen?', ['SAVE;', 'COMMIT;', 'APPLY;', 'FINISH;'], 1, 'COMMIT; mengesahkan transaksi.'),
])

# ---- BANK SOAL PEMAHAMAN KONSEP & ANALISIS KODE (UNTUK PENGACAKAN TIAP PERCOBAAN)
CONCEPT_QUIZZES = {
"html": [
 Q("Mengapa penggunaan elemen semantik seperti <main> dan <article> lebih disarankan dibanding hanya <div>?", ["Membantu pembaca layar (aksesibilitas) dan mesin pencari memahami struktur konten", "Membuat ukuran file HTML menjadi setengah lebih kecil", "Otomatis memberikan animasi CSS tanpa kode tambahan", "Mencegah pengguna menyalin teks dari halaman web"], 0, "Elemen semantik memberi makna struktur bagi pembaca layar dan SEO."),
 Q("Jika formulir mengirimkan password sensitif, mengapa atribut method=\"POST\" lebih tepat dibanding method=\"GET\"?", ["Data POST dikirim di badan permintaan HTTP sehingga tidak terpampang di URL", "Method GET hanya bisa mengirim maksimal 1 kolom input", "Method POST otomatis mengenkripsi database tanpa HTTPS", "Method GET tidak dapat digunakan pada elemen <form>"], 0, "GET menaruh data di query string URL, sedangkan POST di body HTTP."),
 Q("Apa yang terjadi jika elemen <label for=\"email\"> dikaitkan dengan <input id=\"email\">?", ["Mengklik teks label akan otomatis memfokuskan kursor ke kolom input tersebut", "Kolom input otomatis memvalidasi format alamat email", "Nilai input akan langsung tersimpan ke penyimpanan lokal", "Label akan disembunyikan setelah pengguna mengetik"], 0, "Atribut for yang cocok dengan id meningkatkan kemudahan klik dan aksesibilitas."),
 Q("Manakah urutan struktur dokumen HTML5 yang paling tepat secara hierarki?", ["<!DOCTYPE html> -> <html> -> <head> & <body>", "<html> -> <head> -> <!DOCTYPE html> -> <body>", "<head> -> <html> -> <body> -> <!DOCTYPE html>", "<body> -> <head> -> <html> -> <!DOCTYPE html>"], 0, "Dokumen diawali deklarasi DOCTYPE lalu elemen akar <html> yang memuat <head> dan <body>."),
 Q("Kapan sebaiknya atribut loading=\"lazy\" digunakan pada elemen <img>?", ["Untuk gambar di bagian bawah halaman agar dimuat saat mendekati layar", "Untuk logo utama di bagian paling atas halaman", "Untuk mengubah format gambar PNG menjadi SVG secara otomatis", "Saat gambar tidak memiliki atribut src"], 0, "Lazy loading menunda pemuatan gambar di luar layar sehingga halaman awal lebih cepat."),
 Q("Apa perbedaan fungsional antara <section> dan <div> di HTML5?", ["<section> mengelompokkan konten bertema dengan judul, <div> hanya wadah generik tanpa makna semantik", "<div> tidak dapat diberi class CSS, sedangkan <section> bisa", "<section> hanya boleh dipakai satu kali di dalam <body>", "<div> otomatis membuat baris baru, sedangkan <section> bersifat inline"], 0, "<section> mewakili bagian tematik dokumen, sedangkan <div> murni wadah tata letak."),
],
"css": [
 Q("Mengapa penambahan padding: 20px pada elemen dengan width: 200px tidak memperlebar ukuran totalnya jika diatur box-sizing: border-box?", ["Karena padding dan border dihitung di dalam lebar 200px tersebut", "Karena border-box menonaktifkan fungsi properti padding", "Karena browser otomatis memperkecil ukuran huruf di dalamnya", "Karena margin luar otomatis dikurangi 20px"], 0, "Pada border-box, width mencakup konten, padding, dan border."),
 Q("Jika terdapat aturan CSS p { color: blue; } dan .teks { color: red; } pada <p class=\"teks\">, mengapa teks berwarna merah?", ["Selector class (.teks) memiliki spesifisitas lebih tinggi dibanding selector elemen (p)", "Warna merah selalu diprioritaskan oleh mesin render browser", "Selector elemen p hanya berlaku untuk paragraf kosong", "Properti color pada tag p tidak valid di CSS3"], 0, "Spesifisitas class (0,1,0) lebih tinggi daripada selector tag elemen (0,0,1)."),
 Q("Pada wadah dengan display: flex dan flex-direction: column, properti mana yang mengatur perataan secara vertikal (atas-bawah)?", ["justify-content", "align-items", "vertical-align", "float"], 0, "Saat arah flex adalah column, sumbu utama (main axis) menjadi vertikal sehingga diatur oleh justify-content."),
 Q("Apa perbedaan utama antara satuan rem dan em pada ukuran teks CSS?", ["rem mengacu pada ukuran font elemen akar (html), sedangkan em mengacu pada elemen induknya", "rem hanya untuk margin, sedangkan em hanya untuk font-size", "em bersifat tetap seperti piksel, sedangkan rem berubah sesuai resolusi layar", "Tidak ada perbedaan; keduanya selalu bernilai 16px"], 0, "rem konsisten terhadap root (<html>), sedangkan em dapat berlipat ganda bila bersarang."),
 Q("Mengapa elemen dengan position: absolute memerlukan induk dengan position: relative?", ["Agar titik koordinat top/left mengacu pada batas elemen induk tersebut, bukan halaman utama", "Karena position: absolute tidak berfungsi tanpa Flexbox", "Untuk mencegah elemen induk ikut ter-scroll", "Agar z-index bernilai otomatis 0"], 0, "Elemen absolute diposisikan relatif terhadap leluhur terdekat yang berposisi selain static."),
 Q("Bagaimana cara kerja media query @media (max-width: 768px) pada desain responsif?", ["Menerapkan gaya CSS di dalamnya hanya ketika lebar layar 768px atau lebih kecil", "Mengunci lebar layar maksimal pengguna menjadi 768px", "Menyembunyikan halaman web pada layar di atas 768px", "Memperbesar gambar hingga lebar 768px"], 0, "max-width: 768px menargetkan perangkat berlayar kecil seperti ponsel dan tablet."),
],
"javascript": [
 Q("Mengapa ekspresi [1, 2, 3].map(x => x + 1) menghasilkan [2, 3, 4] tanpa mengubah array aslinya?", ["Karena map() bersifat non-mutating dan selalu mengembalikan array baru", "Karena array di JavaScript bersifat immutable secara bawaan", "Karena fungsi panah (arrow function) menyalin seluruh memori global", "Karena operator +1 hanya berlaku pada salinan indeks pertama"], 0, "map() membuat array baru berisi hasil transformasi tiap elemen tanpa memodifikasi array asal."),
 Q("Apa hasil dari kode: const a = { skor: 10 }; a.skor = 25; console.log(a.skor); ?", ["25", "10", "TypeError karena a adalah const", "undefined"], 0, "const mencegah variabel a diarahkan ke objek lain, namun properti di dalam objeknya tetap bisa diubah."),
 Q("Mengapa kita menggunakan kata kunci await di depan pemanggilan fetch() di dalam fungsi async?", ["Untuk menunggu Promise selesai dan mendapatkan nilai respons sebelum lanjut ke baris berikutnya", "Untuk memaksa kode berjalan di thread CPU terpisah", "Untuk mengubah fungsi biasa menjadi generator sinkron", "Untuk membatalkan permintaan jaringan bila lebih dari 1 milidetik"], 0, "await menjeda eksekusi fungsi async hingga Promise berstatus fulfilled atau rejected."),
 Q("Apa perbedaan perilaku antara operator || dan ?? saat memberikan nilai cadangan: const n = 0; ?", ["n || 10 menghasilkan 10 (karena 0 falsy), sedangkan n ?? 10 tetap menghasilkan 0", "Keduanya menghasilkan 10", "Keduanya menghasilkan 0", "n ?? 10 menghasilkan error karena 0 adalah angka"], 0, "Operator ?? hanya memakai nilai cadangan jika sisi kiri bernilai null atau undefined."),
 Q("Jika kita menulis [10, 5, 20].filter(n => n > 8), apa hasil yang dikembalikan?", ["[10, 20]", "[true, false, true]", "30", "[5]"], 0, "filter() menyaring dan mengembalikan array berisi elemen yang membuat kondisi bernilai true."),
 Q("Mengapa perbandingan [] === [] di JavaScript menghasilkan false?", ["Karena array adalah tipe referensi dan kedua literal membuat objek di alamat memori berbeda", "Karena array kosong bernilai NaN", "Karena operator === hanya berlaku untuk tipe angka", "Karena panjang kedua array tidak terdefinisi"], 0, "Objek dan array dibandingkan berdasarkan referensi memori, bukan kesamaan isinya."),
],
"python": [
 Q("Apa hasil dari kode Python: data = [1, 2, 3]; salinan = data; salinan.append(4); print(len(data)) ?", ["4", "3", "Error", "1"], 0, "salinan = data menyalin referensi ke list yang sama, sehingga perubahan pada salinan ikut mengubah data."),
 Q("Mengapa pencarian kunci pada dict (k in kamus) jauh lebih cepat daripada pencarian elemen pada list besar?", ["Karena dict menggunakan struktur hash table dengan rata-rata waktu O(1)", "Karena dict selalu mengurutkan elemennya secara alfabetis", "Karena list menyimpan data di cakram keras, bukan RAM", "Karena dict hanya boleh menyimpan maksimal 100 item"], 0, "Hash table memungkinkan pencarian kunci secara langsung dalam waktu rata-rata konstan O(1)."),
 Q("Apa output dari kode: hasil = [x for x in range(6) if x % 2 == 0]; print(hasil) ?", ["[0, 2, 4]", "[2, 4, 6]", "[1, 3, 5]", "[0, 1, 2, 3, 4, 5]"], 0, "range(6) menghasilkan 0..5, dan syarat x % 2 == 0 memilih bilangan genap: 0, 2, 4."),
 Q("Apa fungsi dari parameter *args pada definisi fungsi def hitung(*args): ?", ["Menerima sejumlah argumen posisi tak terbatas dan mengumpulkannya sebagai tuple", "Mengalikan semua argumen secara otomatis", "Mewajibkan argumen dikirim dalam bentuk dictionary", "Membatasi fungsi agar hanya menerima satu argumen"], 0, "*args membungkus argumen posisi tambahan ke dalam sebuah tuple."),
 Q("Mengapa penggunaan def tambah(item, daftar=[]): sebagai nilai bawaan berisiko menimbulkan bug?", ["List default dibuat satu kali saat fungsi didefinisikan dan dipakai bersama di pemanggilan berikutnya", "Python melarang penggunaan list sebagai argumen fungsi", "Nilai default [] akan selalu dihapus oleh garbage collector", "Fungsi tersebut hanya bisa dipanggil satu kali"], 0, "Argumen default yang mutable mempertahankan perubahannya antar pemanggilan fungsi."),
 Q("Apa output dari: teks = \"Gunadarma\"; print(teks[0:4]) ?", ["Guna", "Gunad", "darma", "urma"], 0, "Slicing [0:4] mengambil karakter dari indeks 0 hingga sebelum indeks 4 (0, 1, 2, 3)."),
],
"sql": [
 Q("Mengapa query SELECT prodi, COUNT(*) FROM mahasiswa WHERE COUNT(*) > 5 GROUP BY prodi; menghasilkan error?", ["Fungsi agregat COUNT(*) tidak boleh di dalam WHERE; seharusnya disaring dengan HAVING setelah GROUP BY", "COUNT(*) tidak boleh dipakai bersama GROUP BY", "Kolom prodi harus diubah menjadi angka terlebih dahulu", "Kata kunci GROUP BY harus ditulis sebelum FROM"], 0, "WHERE menyaring baris mentah sebelum pengelompokan, sedangkan HAVING menyaring hasil agregasi."),
 Q("Apa yang terjadi jika perintah UPDATE mahasiswa SET ipk = 4.0; dijalankan TANPA klausa WHERE?", ["Seluruh baris di dalam tabel mahasiswa akan berubah nilai ipk-nya menjadi 4.0", "Database otomatis menolak perintah tersebut", "Hanya baris pertama yang diperbarui", "Tabel mahasiswa akan terhapus"], 0, "Tanpa WHERE, perintah UPDATE atau DELETE berlaku pada seluruh baris di tabel."),
 Q("Jika Tabel A memiliki 5 baris dan Tabel B memiliki 2 baris yang cocok, berapa baris yang dihasilkan LEFT JOIN dari A ke B?", ["Tetap minimal 5 baris, dengan nilai NULL pada kolom Tabel B untuk baris A yang tidak punya pasangan", "Hanya 2 baris yang cocok saja", "10 baris hasil perkalian silang", "0 baris karena jumlahnya tidak sama"], 0, "LEFT JOIN mempertahankan semua baris dari tabel kiri (A) meskipun tidak ada kecocokan di tabel kanan (B)."),
 Q("Dalam urutan eksekusi logis query SQL, manakah yang dievaluasi lebih dulu oleh mesin database?", ["FROM dan WHERE dievaluasi sebelum SELECT dan ORDER BY", "ORDER BY dievaluasi paling pertama sebelum FROM", "SELECT dievaluasi sebelum FROM", "LIMIT dievaluasi sebelum WHERE"], 0, "Database mengambil sumber tabel (FROM), menyaring baris (WHERE), baru memilih kolom (SELECT) dan mengurutkan (ORDER BY)."),
 Q("Mengapa pencarian dengan kondisi WHERE nilai = NULL tidak pernah mengembalikan baris apa pun?", ["Karena NULL menandakan nilai tak diketahui sehingga harus diuji dengan IS NULL", "Karena kata kunci NULL hanya berlaku pada perintah INSERT", "Karena operator = hanya untuk teks", "Karena kolom numerik tidak bisa bernilai NULL"], 0, "Perbandingan langsung dengan NULL menggunakan = menghasilkan UNKNOWN, bukan TRUE."),
 Q("Apa manfaat utama pembuatan INDEX pada kolom yang sering dicari di klausa WHERE?", ["Mempercepat pencarian baris tanpa harus memindai seluruh tabel (full table scan)", "Mengurangi ukuran penyimpanan tabel hingga 90%", "Mengizinkan kolom menyimpan banyak tipe data sekaligus", "Menghapus baris duplikat secara otomatis setiap jam"], 0, "Index (seperti B-Tree) membuat pencarian data jauh lebih cepat namun menambah sedikit beban saat tulis."),
],
"java": [
 Q("Mengapa perbandingan dua objek String dengan s1 == s2 sering menghasilkan false meskipun tulisannya sama persis?", ["Operator == membandingkan alamat referensi objek di memori, bukan isi teksnya", "String di Java tidak dapat dibandingkan", "Operator == hanya bekerja untuk bilangan desimal", "Java membedakan panjang variabelnya"], 0, "Gunakan s1.equals(s2) untuk membandingkan kesamaan isi karakter pada objek String."),
 Q("Mengapa objek String di Java dirancang bersifat immutable (tidak dapat diubah setelah dibuat)?", ["Untuk keamanan, efisiensi String Pool, dan keamanan akses lintas thread (thread-safety)", "Karena Java tidak memiliki tipe data char", "Agar ukuran memori String selalu 1 byte", "Supaya String tidak bisa dikirim sebagai parameter method"], 0, "Immutability memungkinkan berbagi referensi String dengan aman di String Pool."),
 Q("Apa perbedaan antara overloading dan overriding pada method di Java?", ["Overloading memiliki nama method sama tetapi parameter berbeda; overriding menulis ulang method kelas induk", "Overloading hanya untuk kelas abstrak; overriding hanya untuk interface", "Overloading mengubah nilai kembalian saja; overriding mengubah nama kelas", "Keduanya memiliki arti yang sama persis"], 0, "Overloading terjadi dalam satu kelas dengan signature parameter berbeda; overriding terjadi pada kelas turunan."),
 Q("Mengapa ArrayList<int> tidak valid di Java dan harus ditulis ArrayList<Integer>?", ["Generics di Java hanya menerima tipe referensi (objek), sehingga memerlukan wrapper class Integer", "Tipe int sudah dihapus dari Java modern", "ArrayList hanya bisa menyimpan teks String", "Kata kunci int adalah nama paket milik java.util"], 0, "Tipe primitif seperti int harus dibungkus dengan kelas wrapper Integer pada koleksi generik."),
 Q("Apa yang terjadi jika sebuah method dideklarasikan dengan modifier private?", ["Method tersebut hanya dapat dipanggil dari dalam kelas tempat ia didefinisikan", "Method tersebut dapat diakses oleh semua kelas di paket yang sama", "Method tersebut otomatis menjadi method static", "Method tersebut wajib di-override oleh kelas anak"], 0, "Enkapsulasi dengan private melindungi detail implementasi internal kelas."),
 Q("Kapan blok finally di dalam struktur try-catch-finally TIDAK akan dieksekusi?", ["Hanya jika JVM berhenti paksa (misalnya System.exit) sebelum mencapai blok tersebut", "Setiap kali tidak terjadi exception di dalam blok try", "Ketika exception berhasil ditangkap oleh blok catch", "Saat method memiliki pernyataan return di dalam try"], 0, "Blok finally tetap dijalankan bahkan jika ada return di dalam try atau catch."),
],
"php": [
 Q("Mengapa penggunaan prepared statements pada PDO mencegah serangan SQL Injection?", ["Karena parameter input dikirim terpisah dari struktur perintah SQL sehingga tidak dieksekusi sebagai kode", "Karena PDO otomatis menghapus semua huruf vokal dari input pengguna", "Karena PDO hanya mengizinkan query SELECT", "Karena PDO mengenkripsi tabel database menjadi gambar"], 0, "Pemisahan kueri dan parameter memastikan input pengguna diperlakukan murni sebagai data literal."),
 Q("Apa hasil dari perbandingan '10 apel' == 10 pada PHP versi lama dibanding '10 apel' === 10?", ["=== selalu menghasilkan false karena tipe string dan integer berbeda", "Keduanya selalu menghasilkan true", "=== menghasilkan true karena angka 10 ada di awal teks", "=== memicu fatal error"], 0, "Operator identik === memeriksa nilai sekaligus kesamaan tipe data tanpa konversi longgar."),
 Q("Apa perbedaan utama antara include dan require saat berkas yang dipanggil tidak ditemukan?", ["require menghentikan skrip dengan fatal error, sedangkan include hanya memberi peringatan (warning) dan lanjut", "include menghentikan server, sedangkan require mengabaikannya", "require hanya untuk berkas HTML, sedangkan include untuk berkas CSS", "Tidak ada perbedaan sama sekali"], 0, "Gunakan require untuk berkas penting yang wajib ada agar aplikasi tidak berjalan dalam kondisi tidak lengkap."),
 Q("Saat memproses password pengguna di PHP, pasangan fungsi mana yang direkomendasikan secara keamanan?", ["password_hash() dan password_verify()", "md5() dan sha1()", "base64_encode() dan base64_decode()", "crypt_simple() dan check_text()"], 0, "password_hash() menggunakan algoritma kuat beserta salt otomatis yang aman."),
 Q("Apa output dari kode: $a = [1, 2]; $a[] = 3; echo count($a); ?", ["3", "2", "1", "Error"], 0, "Sintaks $a[] = 3 menambahkan elemen baru di akhir array sehingga jumlahnya menjadi 3."),
 Q("Mengapa fungsi header('Location: dashboard.php') gagal bekerja jika sebelumnya sudah ada perintah echo?", ["Karena header HTTP harus dikirim sebelum ada output teks apa pun yang dikirim ke browser", "Karena fungsi echo menutup koneksi internet", "Karena header() hanya bisa dipanggil di baris paling akhir", "Karena PHP tidak mendukung pengalihan halaman"], 0, "HTTP header wajib dikirim sebelum body respons dimulai."),
],
"c": [
 Q("Apa risiko utama jika kita menulis char s[4] = \"Halo\"; di bahasa C?", ["Tidak cukup ruang untuk karakter penutup null ('\\0') sehingga pembacaan string dapat meluber ke memori sebelahnya", "Kompilator otomatis memperbesar ukuran array menjadi 100 byte", "Huruf kapital H tidak diizinkan di dalam char[]", "Program langsung menghapus file sumber"], 0, "String \"Halo\" terdiri dari 4 huruf ditambah 1 byte '\\0', sehingga butuh minimal char s[5]."),
 Q("Mengapa fungsi void tukar(int a, int b) gagal menukar nilai variabel asli di fungsi pemanggil?", ["Karena C meneruskan argumen secara pass-by-value (hanya salinannya); perlu pointer (int *a, int *b)", "Karena fungsi bertipe void tidak boleh memiliki parameter", "Karena variabel int bersifat konstanta di C", "Karena nama fungsi tidak boleh diawali huruf kecil"], 0, "Untuk mengubah variabel milik pemanggil, kirimkan alamatnya (&x) dan terima dengan pointer (*p)."),
 Q("Apa yang terjadi jika memori yang dialokasikan dengan malloc() tidak pernah dibebaskan dengan free()?", ["Terjadi kebocoran memori (memory leak) selama program berjalan", "Memori otomatis dibersihkan di akhir setiap blok kurung kurawal", "Kompilator menolak membuat file eksekusi", "Pointer otomatis berubah menjadi bernilai 0"], 0, "C tidak memiliki garbage collector otomatis; setiap malloc() harus dipasangkan dengan free()."),
 Q("Setelah memanggil free(ptr);, mengapa disarankan mengatur ptr = NULL;?", ["Untuk mencegah dangling pointer (mengakses kembali alamat memori yang sudah dibebaskan)", "Agar ukuran file program menjadi lebih kecil", "Karena free() tidak bekerja sebelum ptr bernilai NULL", "Untuk menghapus variabel dari stack"], 0, "Menyetel pointer ke NULL mencegah penggunaan tak sengaja atas alamat memori yang tak lagi valid."),
 Q("Apa nilai dari ekspresi *(arr + 2) jika int arr[] = {10, 20, 30, 40};?", ["30", "12", "20", "40"], 0, "Aritmetika pointer *(arr + 2) sama artinya dengan mengakses elemen indeks ke-2, yaitu arr[2] = 30."),
 Q("Mengapa hasil dari 5 / 2 di dalam ekspresi integer C adalah 2, bukan 2.5?", ["Karena pembagian dua bilangan bulat (int) di C membuang bagian pecahan (truncation)", "Karena C membulatkan angka ke bilangan genap terdekat", "Karena operator / di C adalah operator sisa bagi", "Karena tipe int hanya menyimpan angka genap"], 0, "Agar menghasilkan desimal, salah satu operan harus bertipe floating-point seperti 5.0 / 2."),
],
"cpp": [
 Q("Mengapa pengiriman parameter const std::string& teks lebih efisien daripada std::string teks untuk teks berukuran besar?", ["Menghindari penyalinan seluruh isi string di memori sekaligus mencegah fungsi mengubah nilai aslinya", "Membuat string otomatis tersimpan di dalam file", "Mengubah string menjadi bilangan bulat saat kompilasi", "Mengizinkan fungsi menghapus variabel milik pemanggil"], 0, "Referensi konstanta (const &) meneruskan alamat objek tanpa biaya salin (copy) dan tetap aman."),
 Q("Apa keuntungan utama prinsip RAII (Resource Acquisition Is Initialization) di C++?", ["Sumber daya (memori/file) otomatis dibersihkan oleh destruktor saat objek keluar dari cakupan (scope)", "Semua variabel otomatis menjadi variabel global", "Program C++ tidak perlu dikompilasi terlebih dahulu", "Memori RAM komputer otomatis bertambah dua kali lipat"], 0, "RAII menjamin determinisme pembersihan resource lewat destruktor, bahkan saat terjadi exception."),
 Q("Kapan metode std::vector::push_back() perlu melakukan realokasi memori internal?", ["Saat jumlah elemen (size) melebihi kapasitas ruang yang telah dicadangkan (capacity)", "Setiap kali elemen pertama dibaca dengan operator []", "Saat vector dikosongkan dengan clear()", "Hanya ketika vector berisi bilangan negatif"], 0, "Ketika size mencapai capacity, vector mengalokasikan blok memori baru yang lebih besar dan menyalin elemennya."),
 Q("Mengapa kelas induk yang menggunakan polimorfisme (fungsi virtual) sebaiknya memiliki virtual destructor?", ["Agar saat objek turunan dihapus melalui pointer kelas induk, destruktor kelas turunan ikut terpanggil", "Agar kelas induk tidak bisa diwariskan lagi", "Untuk mempercepat waktu kompilasi file header", "Karena C++ mewajibkan semua fungsi diawali kata virtual"], 0, "Tanpa virtual destructor, penghapusan lewat pointer base class hanya memanggil destruktor base class."),
 Q("Apa perbedaan antara std::map dan std::unordered_map di C++ STL?", ["std::map menjaga kunci tetap terurut (O(log n)), sedangkan std::unordered_map memakai hash table (rata-rata O(1))", "std::map hanya untuk angka, sedangkan std::unordered_map hanya untuk string", "std::unordered_map mengizinkan kunci duplikat secara bawaan", "Tidak ada perbedaan performa maupun struktur data"], 0, "Pilih std::map bila butuh urutan kunci, atau std::unordered_map bila butuh pencarian rata-rata tercepat."),
 Q("Apa yang dilakukan std::move(obj) pada C++ modern?", ["Mengubah ekspresi menjadi rvalue reference sehingga sumber daya objek dapat dipindahkan tanpa disalin", "Menghapus file kode sumber dari folder proyek", "Memindahkan variabel dari fungsi main ke fungsi lain secara otomatis", "Mengurutkan isi objek dari kecil ke besar"], 0, "Move semantics memindahkan kepemilikan buffer internal tanpa menduplikasi datanya."),
],
"csharp": [
 Q("Apa keuntungan utama sifat deferred execution (eksekusi tertunda) pada kueri LINQ seperti items.Where(x => x > 5)?", ["Kueri baru benar-benar dieksekusi saat hasilnya diiterasi (mis. foreach atau ToList), sehingga dapat dirangkai secara efisien", "Kueri dijalankan di latar belakang setelah aplikasi ditutup", "Kueri otomatis mengubah isi database SQL tanpa koneksi", "Kueri hanya berjalan pada komputer bersistem operasi Linux"], 0, "Deferred execution menghindari pembuatan koleksi perantara yang tidak perlu saat merangkai beberapa operator LINQ."),
 Q("Apa perbedaan mendasar antara class dan struct di C#?", ["class adalah reference type (dialokasikan di heap), sedangkan struct adalah value type (menyimpan nilainya langsung)", "struct mendukung pewarisan berganda, sedangkan class tidak", "class tidak boleh memiliki method, sedangkan struct boleh", "struct hanya dapat berisi satu variabel integer"], 0, "Salinan variabel struct menyalin datanya secara langsung, sedangkan class menyalin referensi objeknya."),
 Q("Dalam pemrograman asinkron C#, mengapa penggunaan async Task lebih disarankan daripada async void?", ["Agar pemanggil dapat menunggu (await) penyelesaian tugas dan menangkap exception yang terjadi", "Karena async void membutuhkan memori 10 kali lebih besar", "Karena kata kunci void sudah dihapus dari C#", "Karena async Task hanya berjalan di satu baris kode"], 0, "Exception pada async void tidak dapat ditangkap dengan try/catch oleh pemanggilnya."),
 Q("Apa hasil dari ekspresi: string nama = null; int panjang = nama?.Length ?? 0; ?", ["0 (tanpa memicu NullReferenceException)", "NullReferenceException", "null", "-1"], 0, "Operator ?. menghasilkan null karena nama bernilai null, lalu ?? memberikan nilai cadangan 0."),
 Q("Mengapa penggabungan string ribuan kali di dalam perulangan sebaiknya memakai StringBuilder dibanding operator +?", ["Karena String bersifat immutable, sehingga operator + terus membuat objek String baru di memori pada tiap iterasi", "Karena operator + di C# hanya bisa menggabungkan maksimal 2 huruf", "Karena StringBuilder otomatis menerjemahkan teks ke bahasa mesin", "Karena String tidak bisa digunakan di dalam perulangan for"], 0, "StringBuilder memodifikasi buffer karakter internal tanpa membuat objek baru berulang kali."),
 Q("Apa fungsi blok using (var stream = new FileStream(...)) { ... } di C#?", ["Memastikan metode Dispose() dipanggil otomatis untuk menutup file meskipun terjadi exception di dalam blok", "Mengimpor namespace FileStream ke seluruh proyek", "Menyalin file ke memori permanen secara otomatis", "Mengabaikan semua error yang muncul di dalam blok"], 0, "Pernyataan using diterjemahkan kompilator menjadi blok try/finally yang memanggil Dispose()."),
],
"react": [
 Q("Mengapa kita TIDAK boleh mengubah array state secara langsung seperti items.push(baru) lalu memanggil setItems(items)?", ["Karena referensi array-nya tetap sama sehingga React menganggap state tidak berubah dan tidak melakukan render ulang", "Karena JavaScript melarang penggunaan push() di dalam file JSX", "Karena setItems() hanya menerima nilai bertipe boolean", "Karena push() akan menghapus seluruh komponen anak"], 0, "Buat array baru seperti setItems([...items, baru]) agar React mendeteksi perubahan referensi state."),
 Q("Mengapa penggunaan indeks array (index) sebagai prop key tidak disarankan jika urutan daftar dapat berubah atau dihapus?", ["Dapat mengacaukan pencocokan state komponen dan DOM saat item disisipkan atau dihapus di tengah daftar", "React akan menolak merender lebih dari 3 elemen", "Indeks array di JavaScript selalu dimulai dari angka acak", "Prop key hanya boleh berisi teks lebih dari 50 karakter"], 0, "Gunakan ID unik yang stabil dari tiap data agar rekonsiliasi Virtual DOM tetap akurat."),
 Q("Kapan kita sebaiknya melakukan lifting state up (menaikkan state ke komponen induk)?", ["Ketika dua atau lebih komponen saudara (sibling) perlu berbagi dan menyinkronkan data yang sama", "Setiap kali komponen memiliki lebih dari satu tag HTML", "Agar state tidak pernah menyebabkan render ulang", "Saat kita ingin menyembunyikan data dari komponen induk"], 0, "Menempatkan state di induk terdekat memungkinkan aliran data satu arah ke komponen anak lewat props."),
 Q("Apa yang terjadi jika fungsi di dalam useEffect mengubah state, dan state tersebut dimasukkan ke dependency array tanpa kondisi berhenti?", ["Terjadi perulangan render tak berujung (infinite re-render loop)", "Efek hanya berjalan satu kali saat aplikasi ditutup", "React otomatis menghapus useEffect tersebut", "State akan terkunci menjadi bernilai null"], 0, "Perubahan state memicu render ulang, yang kembali menjalankan useEffect karena dependensinya berubah."),
 Q("Mengapa pemanggilan Hook seperti useState() tidak boleh diletakkan di dalam blok if atau perulangan?", ["React mengandalkan urutan pemanggilan Hook yang konsisten di setiap render untuk melacak state", "Karena blok if tidak valid di dalam fungsi JavaScript", "Karena useState() hanya boleh dipanggil di luar komponen", "Karena Hook akan mengubah kondisi if menjadi selalu true"], 0, "Aturan Hooks mewajibkan Hook dipanggil di tingkat teratas fungsi komponen agar urutan indeks state terjaga."),
 Q("Apa kegunaan fungsi pembersih (cleanup function) yang dikembalikan oleh useEffect?", ["Membersihkan langganan event atau timer (seperti clearInterval) sebelum komponen dilepas atau efek dijalankan ulang", "Menghapus seluruh isi localStorage browser pengguna", "Mengatur ulang semua variabel props menjadi kosong", "Mematikan server backend secara otomatis"], 0, "Fungsi cleanup mencegah kebocoran memori dari timer atau event listener yang masih aktif setelah unmount."),
],
"mysql": [
 Q("Mengapa pencarian dengan kondisi WHERE LOWER(nama) = 'budi' dapat membuat index biasa pada kolom nama tidak terpakai?", ["Karena pembungkusan kolom dengan fungsi memaksa MySQL mengevaluasi fungsi tersebut untuk setiap baris", "Karena fungsi LOWER() menghapus index dari tabel secara permanen", "Karena MySQL tidak mengizinkan fungsi di dalam WHERE", "Karena index hanya bekerja untuk kolom bertipe tanggal"], 0, "Menerapkan fungsi pada kolom terindeks menghalangi pencarian langsung pada struktur B-Tree index."),
 Q("Dalam transaksi perbankan di MySQL (InnoDB), perintah apa yang membatalkan seluruh perubahan jika terjadi kegagalan di tengah proses?", ["ROLLBACK;", "COMMIT;", "UNDO TABLE;", "CANCEL;"], 0, "ROLLBACK; mengembalikan data ke keadaan semula sebelum transaksi dimulai."),
 Q("Mengapa kolom harga uang sebaiknya menggunakan tipe DECIMAL(12,2) dibanding FLOAT di MySQL?", ["DECIMAL menyimpan angka desimal secara presisi eksak, sedangkan FLOAT dapat mengalami selisih pembulatan biner", "FLOAT tidak dapat dijumlahkan dengan fungsi SUM()", "DECIMAL menggunakan memori 0 byte", "FLOAT hanya bisa menyimpan bilangan negatif"], 0, "Perhitungan keuangan membutuhkan presisi eksak tanpa galat floating-point."),
 Q("Apa dampak pengaturan ON DELETE CASCADE pada foreign key tabel pesanan yang merujuk ke tabel pelanggan?", ["Saat baris pelanggan dihapus, seluruh baris pesanan milik pelanggan tersebut ikut terhapus otomatis", "Pelanggan tidak akan pernah bisa dihapus sampai tabel pesanan di-drop", "Menghapus satu pesanan akan menghapus seluruh data pelanggan", "Foreign key otomatis dinonaktifkan saat ada perintah DELETE"], 0, "ON DELETE CASCADE menjaga integritas referensial dengan menghapus baris anak yang terkait secara otomatis."),
 Q("Apa perbedaan utama antara TRUNCATE TABLE dan DELETE FROM tanpa WHERE di MySQL?", ["TRUNCATE mengosongkan tabel dengan cepat dan mereset AUTO_INCREMENT, sedangkan DELETE menghapus baris satu per satu", "DELETE menghapus struktur tabel, sedangkan TRUNCATE hanya menghapus baris pertama", "TRUNCATE dapat disaring menggunakan klausa WHERE", "DELETE tidak bisa digunakan pada tabel InnoDB"], 0, "TRUNCATE adalah operasi DDL cepat yang mereset penghitung AUTO_INCREMENT."),
 Q("Jika sebuah query memiliki WHERE, GROUP BY, dan HAVING, kapan klausa HAVING dijalankan?", ["Setelah baris disaring oleh WHERE dan dikelompokkan oleh GROUP BY", "Sebelum klausa WHERE membaca tabel", "Hanya jika query tidak memiliki fungsi agregat", "Tepat setelah perintah LIMIT selesai"], 0, "WHERE menyaring baris individu terlebih dahulu, GROUP BY mengelompokkan, lalu HAVING menyaring kelompok tersebut."),
],
}

