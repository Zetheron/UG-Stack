"""Simulator Eksekusi Python, SQL & Visualizer Algoritma."""
import ast, io, re, time

def run_python_safe(code: str) -> str:
    try:
        tree = ast.parse(code, mode="exec")
    except SyntaxError as e:
        return f"[SyntaxError] Baris {e.lineno}: {e.msg}"
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal)):
            return "[Keamanan Sandbox] Import/sistem dinonaktifkan di simulator web."
    buf = io.StringIO()
    def p(*args, sep=" ", end="\n"):
        buf.write(sep.join(str(a) for a in args) + end)
    safe_env = {"__builtins__": {
        "abs": abs, "len": len, "range": range, "sum": sum, "min": min, "max": max,
        "sorted": sorted, "int": int, "str": str, "float": float, "list": list, "dict": dict,
        "print": p, "True": True, "False": False, "None": None,
    }}
    try:
        exec(compile(tree, "<sandbox>", "exec"), safe_env, safe_env)
    except Exception as e:
        return f"{buf.getvalue()}\n[{type(e).__name__}] {e}".strip()
    res = buf.getvalue().strip()
    return res if res else "[Program selesai dijalankan tanpa output print()]"

def run_code(lang: str, code: str) -> str:
    l = (lang or "Python").strip().lower()
    if l == "python":
        return run_python_safe(code)
    if "sql" in l:
        return "ID | Nama Mahasiswa      | Prodi           | IPK\n---+--------------------+-----------------+-----\n 1 | Dina Putri         | Informatika     | 3.85\n 2 | Siti Rahma         | Informatika     | 3.92\n 3 | Budi Santoso       | Sistem Info     | 3.60\n\n(Hasil simulasi query database)"
    return f"[Status 200 OK] Program {lang} Berhasil Dijalankan!"

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
        try: target = int(text_target.strip())
        except ValueError: target = arr[0]
        l, r = 0, len(arr) - 1
        found = False
        while l <= r:
            m = (l + r) // 2
            steps.append(f"Cek mid [{m}] = {arr[m]} (target: {target})")
            if arr[m] == target:
                steps.append(f"✓ DITEMUKAN pada indeks {m}!")
                found = True
                break
            elif arr[m] < target: l = m + 1
            else: r = m - 1
        if not found: steps.append(f"✗ Target {target} tidak ditemukan.")
        dur = (time.perf_counter() - t0) * 1000
        return steps, f"Binary Search selesai dalam {dur:.3f} ms (kompleksitas O(log n))."
    # Merge sort default
    arr = list(data[:15])
    steps.append(f"Data awal: {arr}")
    def ms(s):
        if len(s) <= 1: return s
        mid = len(s) // 2
        left, right = ms(s[:mid]), ms(s[mid:])
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: res.append(left[i]); i += 1
            else: res.append(right[j]); j += 1
        res += left[i:] + right[j:]
        steps.append(f"Gabung: {left} + {right} -> {res}")
        return res
    out = ms(arr)
    steps.append(f"✓ Hasil akhir: {out}")
    dur = (time.perf_counter() - t0) * 1000
    return steps, f"Merge Sort selesai dalam {dur:.3f} ms (kompleksitas stabil O(n log n))."
