"""Halaman Simulasi Real-Time: Live Code Sandbox & Visualizer Algoritma Step-by-Step."""
import flet as ft
from components.code_editor import SAMPLES
from components.ui import GREEN, card, chip, green_button, pad, page_banner, section_heading
from services import simulator


def get_tryit_view(*args, **kwargs) -> ft.Control:
    page = kwargs.get("page")
    lang_name = kwargs.get("lang_name", kwargs.get("lang", "Python"))
    initial_code = kwargs.get("initial_code", kwargs.get("code", None))
    on_back_click = kwargs.get("on_back_click", kwargs.get("go", None))
    mobile = bool(kwargs.get("mobile", False))

    rem = list(args)
    if rem and hasattr(rem[0], "controls"):
        page = rem.pop(0)
    if rem and isinstance(rem[0], str):
        lang_name = rem.pop(0)
    if rem:
        if callable(rem[0]):
            on_back_click = rem.pop(0)
        elif isinstance(rem[0], str):
            initial_code = rem.pop(0)
    if rem:
        if isinstance(rem[0], str):
            initial_code = rem.pop(0)
        elif callable(rem[0]):
            on_back_click = rem.pop(0)

    lang_key = lang_name if lang_name in SAMPLES else "Python"
    output_text = ft.Text(
        "",
        font_family="monospace",
        size=13,
        color="#00FF66",
        selectable=True,
    )

    def run_editor(e=None):
        chosen = lang_dd.value or "Python"
        output_text.value = simulator.run_code(chosen, code_tf.value or "")
        try:
            if getattr(output_text, "page", None):
                output_text.update()
        except Exception:
            pass

    code_tf = ft.TextField(
        value=initial_code if initial_code else SAMPLES.get(lang_key, SAMPLES["Python"]),
        multiline=True,
        min_lines=9,
        max_lines=15,
        text_style=ft.TextStyle(font_family="monospace", size=13),
        border_radius=8,
        on_change=run_editor,
    )
    lang_dd = ft.Dropdown(
        label="Bahasa",
        value=lang_key,
        width=180,
        options=[ft.dropdown.Option(k, k) for k in SAMPLES.keys()],
    )
    output_text.value = simulator.run_code(lang_key, code_tf.value)

    def on_lang_change(e):
        chosen = lang_dd.value or "Python"
        code_tf.value = SAMPLES.get(chosen, SAMPLES["Python"])
        output_text.value = simulator.run_code(chosen, code_tf.value)
        try:
            if getattr(output_text, "page", None):
                code_tf.update()
                output_text.update()
        except Exception:
            pass

    lang_dd.on_change = on_lang_change

    algo_dd = ft.Dropdown(
        label="Level",
        value="binary_search",
        width=220,
        options=[
            ft.dropdown.Option("binary_search", "Binary Search O(log n)"),
            ft.dropdown.Option("linear_search", "Linear Search O(n)"),
            ft.dropdown.Option("merge_sort", "Merge Sort O(n log n)"),
            ft.dropdown.Option("insertion_sort", "Insertion Sort O(n^2)"),
        ],
    )
    arr_tf = ft.TextField(label="Judul modul", value="42, 15, 8, 99, 23, 4, 16, 55", expand=True)
    target_tf = ft.TextField(label="Durasi (menit)", value="23", width=130)
    algo_summary = ft.Text("", weight=ft.FontWeight.BOLD, size=13, color=GREEN)
    algo_steps_col = ft.Column(spacing=6)

    def run_algo(e=None):
        steps, summary = simulator.simulate_algorithm(
            algo_dd.value or "binary_search",
            arr_tf.value or "",
            target_tf.value or "",
        )
        algo_summary.value = summary
        algo_steps_col.controls = [
            ft.Container(
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=10,
                border_radius=8,
                content=ft.Text(st, font_family="monospace", size=12, color=ft.colors.ON_SURFACE),
            )
            for st in steps
        ]
        try:
            if getattr(algo_steps_col, "page", None):
                algo_summary.update()
                algo_steps_col.update()
        except Exception:
            pass

    algo_dd.on_change = run_algo
    arr_tf.on_change = run_algo
    target_tf.on_change = run_algo
    run_algo()

    def handle_back(e):
        if callable(on_back_click):
            try:
                on_back_click("exercises")
            except TypeError:
                try:
                    on_back_click(e)
                except TypeError:
                    on_back_click()

    return ft.Column([
        page_banner("UG-Stack Spaces", "Ruang eksperimen kode", mobile),
        ft.Container(
            padding=pad(mobile),
            content=ft.Column([
                ft.Row([
                    ft.TextButton("❮ Semua quiz", on_click=handle_back),
                    chip("Try Spaces", "#D9EEE1"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, wrap=True),
                card(ft.Column([
                    section_heading("Contoh Kode:"),
                    ft.Row([lang_dd, green_button("Run ❯", run_editor)], spacing=12, wrap=True),
                    code_tf,
                    ft.Text("Hasil Eksekusi Output:", weight=ft.FontWeight.BOLD, size=14),
                    ft.Container(
                        bgcolor="#1E1F26",
                        padding=15,
                        border_radius=8,
                        content=ft.Column([output_text], spacing=0),
                    ),
                ], spacing=10)),
                card(ft.Column([
                    section_heading("Simulasi"),
                    ft.ResponsiveRow([
                        ft.Column([algo_dd], col={"xs": 12, "md": 3}),
                        ft.Column([arr_tf], col={"xs": 12, "md": 5}),
                        ft.Column([target_tf], col={"xs": 6, "md": 2}),
                        ft.Column([green_button("Run ❯", run_algo)], col={"xs": 6, "md": 2}),
                    ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    algo_summary,
                    algo_steps_col,
                ], spacing=10)),
            ], spacing=18),
        ),
    ], spacing=0)


create_tryit_view = get_tryit_view
