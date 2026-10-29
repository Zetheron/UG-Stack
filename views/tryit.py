"""Halaman Simulasi: Live Code Sandbox (Python/SQL/Web) & Visualizer Algoritma Step-by-Step."""
import flet as ft
from components.code_editor import SAMPLES
from components.ui import GREEN, card, chip, green_button, pad, page_banner, section_heading
from services import simulator


def create_tryit_view(page: ft.Page, lang_name: str = "Python", initial_code: str | None = None,
                      go=None, mobile: bool = False) -> ft.Control:
    lang_key = lang_name if lang_name in SAMPLES else "Python"
    code_tf = ft.TextField(
        value=initial_code if initial_code else SAMPLES.get(lang_key, SAMPLES["Python"]),
        multiline=True,
        min_lines=9,
        max_lines=15,
        text_style=ft.TextStyle(font_family="monospace", size=13),
        border_radius=8,
    )
    lang_dd = ft.Dropdown(
        label="Bahasa",
        value=lang_key,
        width=180,
        options=[ft.dropdown.Option(k, k) for k in SAMPLES.keys()],
    )
    output_text = ft.Text(
        simulator.run_code(lang_key, code_tf.value),
        font_family="monospace",
        size=13,
        color="#00FF66",
        selectable=True,
    )

    def on_lang_change(e):
        chosen = lang_dd.value or "Python"
        code_tf.value = SAMPLES.get(chosen, SAMPLES["Python"])
        output_text.value = simulator.run_code(chosen, code_tf.value)
        if getattr(output_text, "page", None):
            code_tf.update()
            output_text.update()

    lang_dd.on_change = on_lang_change

    def run_editor(e):
        chosen = lang_dd.value or "Python"
        output_text.value = simulator.run_code(chosen, code_tf.value or "")
        if getattr(output_text, "page", None):
            output_text.update()

    algo_dd = ft.Dropdown(
        label="Level",
        value="binary_search",
        width=220,
        options=[
            ft.dropdown.Option("binary_search", "Binary Search O(log n)"),
            ft.dropdown.Option("merge_sort", "Merge Sort O(n log n)"),
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
        if getattr(algo_steps_col, "page", None):
            algo_summary.update()
            algo_steps_col.update()

    run_algo()

    return ft.Column([
        page_banner("UG-Stack Spaces", "Ruang eksperimen kode", mobile),
        ft.Container(
            padding=pad(mobile),
            content=ft.Column([
                ft.Row([
                    ft.TextButton("❮ Kembali ke Beranda", on_click=lambda e: go("home") if go else None),
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
                        content=ft.Row([output_text], scroll=ft.ScrollMode.AUTO),
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
