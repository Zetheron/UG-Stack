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
