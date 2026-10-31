"""Simulator Eksekusi Python, SQL, Web & Visualizer Algoritma Step-by-Step."""
import ast
import io
import re
import time

_SAFE_BUILTINS = {
    "abs": abs, "all": all, "any": any, "bin": bin, "bool": bool, "chr": chr,
    "dict": dict, "divmod": divmod, "enumerate": enumerate, "filter": filter,
    "float": float, "format": format, "hex": hex, "int": int, "isinstance": isinstance,
    "len": len, "list": list, "map": map, "max": max, "min": min, "ord": ord,
    "pow": pow, "range": range, "reversed": reversed, "round": round, "set": set,
    "sorted": sorted, "str": str, "sum": sum, "tuple": tuple, "zip": zip,
    "True": True, "False": False, "None": None,
}

_SAMPLE_ROWS = [
    {"id": 1, "npm": "50421001", "nama": "Dina Putri", "prodi": "Informatika", "ipk": 3.85, "Country": "Indonesia", "CustomerName": "Dina Putri"},
    {"id": 2, "npm": "50421002", "nama": "Budi Santoso", "prodi": "Sistem Informasi", "ipk": 3.60, "Country": "Indonesia", "CustomerName": "Budi Santoso"},
    {"id": 3, "npm": "50421003", "nama": "Siti Rahma", "prodi": "Informatika", "ipk": 3.92, "Country": "Indonesia", "CustomerName": "Siti Rahma"},
    {"id": 4, "npm": "50421004", "nama": "Andi Wijaya", "prodi": "Teknik Komputer", "ipk": 3.45, "Country": "Singapore", "CustomerName": "Andi Wijaya"},
]


def run_python_safe(code: str) -> str:
    try:
        tree = ast.parse(code, mode="exec")
    except SyntaxError as e:
        return f"[SyntaxError] Baris {e.lineno}: {e.msg}"
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal)):
            return "[Keamanan Sandbox] Import/sistem dinonaktifkan di simulator web."
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            return "[Keamanan Sandbox] Akses atribut internal tidak diizinkan."
    buf = io.StringIO()
    lines_cnt = {"n": 0}

    def p(*args, sep=" ", end="\n"):
        lines_cnt["n"] += 1
        if lines_cnt["n"] > 150:
            raise RuntimeError("Batas output terlampaui (maks. 150 baris).")
        buf.write(sep.join(str(a) for a in args) + end)

    safe_env = {"__builtins__": dict(_SAFE_BUILTINS, print=p, input=lambda prompt="": "Mahasiswa_UG")}
    try:
        exec(compile(tree, "<sandbox>", "exec"), safe_env, safe_env)
    except Exception as e:
        return f"{buf.getvalue()}\n[{type(e).__name__}] {e}".strip()
    res = buf.getvalue().strip()
    return res if res else "[Program selesai dijalankan tanpa output print()]"


def run_code(lang: str, code: str) -> str:
    l = (lang or "Python").strip()
    low = l.lower()
    if low == "python":
        return run_python_safe(code)
    if "sql" in low:
        rows = list(_SAMPLE_ROWS)
        if "ipk >= 3.5" in code.lower():
            rows = [r for r in rows if r["ipk"] >= 3.5]
        elif "country='indonesia'" in code.lower().replace(" ", ""):
            rows = [r for r in rows if r["Country"] == "Indonesia"]
        lines = ["ID | NPM      | Nama Mahasiswa   | Prodi            | IPK", "---+----------+------------------+------------------+-----"]
        for r in rows:
            lines.append(f" {r['id']} | {r['npm']} | {r['nama']:<16} | {r['prodi']:<16} | {r['ipk']:.2f}")
        lines.append(f"\n({len(rows)} baris ditemukan)")
        return "\n".join(lines)
    if low == "javascript":
        logs = re.findall(r"console\.log\((.*?)\)", code)
        if logs:
            return "\n".join(x.strip("'\"`") for x in logs)
    if low in ("c", "c++", "java", "c#", "php"):
        prints = re.findall(r'(?:printf|cout\s*<<|println|WriteLine|echo)\s*\(?\s*"([^"]*)"', code)
        if prints:
            return "\n".join(p.replace("\\n", "\n") for p in prints)
    return f"[Status 200 OK] Program {l} Berhasil Dijalankan!"


def simulate_algorithm(algo: str, text_nums: str, text_target: str = "") -> tuple[list[str], str]:
    try:
        data = [int(x.strip()) for x in text_nums.replace(";", ",").split(",") if x.strip()]
    except ValueError:
        return ["Input harus angka bulat dipisahkan koma."], "Input tidak valid."
    if not data:
        return ["Masukkan deretan angka."], "Data kosong."
    steps = []
    t0 = time.perf_counter()
    if algo == "binary_search":
        arr = sorted(data[:20])
        steps.append(f"Data diurutkan terlebih dahulu: {arr}")
        try:
            target = int(text_target.strip())
        except ValueError:
            target = arr[0]
        l, r = 0, len(arr) - 1
        found = False
        while l <= r:
            m = (l + r) // 2
            steps.append(f"Cek mid [{m}] = {arr[m]} (target: {target})")
            if arr[m] == target:
                steps.append(f"✓ DITEMUKAN pada indeks {m}!")
                found = True
                break
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        if not found:
            steps.append(f"✗ Target {target} tidak ditemukan.")
        dur = (time.perf_counter() - t0) * 1000
        return steps, f"Binary Search selesai dalam {dur:.3f} ms (kompleksitas O(log n))."

    if algo == "linear_search":
        arr = list(data[:20])
        try:
            target = int(text_target.strip())
        except ValueError:
            target = arr[-1]
        steps.append(f"Data: {arr} | Target: {target}")
        found = False
        for i, v in enumerate(arr):
            steps.append(f"Cek indeks [{i}] = {v}")
            if v == target:
                steps.append(f"✓ DITEMUKAN pada indeks {i}!")
                found = True
                break
        if not found:
            steps.append(f"✗ Target {target} tidak ditemukan.")
        dur = (time.perf_counter() - t0) * 1000
        return steps, f"Linear Search selesai dalam {dur:.3f} ms (kompleksitas O(n))."

    if algo == "insertion_sort":
        arr = list(data[:15])
        steps.append(f"Data awal: {arr}")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            steps.append(f"Sisipkan {key}: {arr}")
        dur = (time.perf_counter() - t0) * 1000
        return steps, f"Insertion Sort selesai dalam {dur:.3f} ms (kompleksitas O(n^2))."

    arr = list(data[:15])
    steps.append(f"Data awal: {arr}")

    def ms(s):
        if len(s) <= 1:
            return s
        mid = len(s) // 2
        left, right = ms(s[:mid]), ms(s[mid:])
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i]); i += 1
            else:
                res.append(right[j]); j += 1
        res += left[i:] + right[j:]
        steps.append(f"Gabung: {left} + {right} -> {res}")
        return res

    out = ms(arr)
    steps.append(f"✓ Hasil akhir: {out}")
    dur = (time.perf_counter() - t0) * 1000
    return steps, f"Merge Sort selesai dalam {dur:.3f} ms (kompleksitas stabil O(n log n))."