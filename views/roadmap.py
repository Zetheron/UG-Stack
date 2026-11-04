import flet as ft

from components.ui import GREEN, card, green_button, lang_logo, page_banner, pad
from content.languages import BY_KEY
from content.pages import ROADMAP


def get_roadmap_view(page: ft.Page, mobile: bool, on_open_lang):
    tracks = []
    for t in ROADMAP:
        steps = []
        for n, (key, note) in enumerate(t["steps"], 1):
            lang = BY_KEY[key]
            steps.append(ft.Row([
                ft.Container(ft.Text(str(n), color=ft.colors.WHITE, weight=ft.FontWeight.BOLD), bgcolor=GREEN, width=28, height=28,
                             border_radius=14, alignment=ft.alignment.center),
                lang_logo(lang["key"], 22),
                ft.Column([ft.Text(lang["name"], size=14, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                           ft.Text(note, size=12, color=ft.colors.ON_SURFACE_VARIANT)], spacing=0, expand=True),
                ft.TextButton("Mulai ❯", on_click=lambda e, k=key: on_open_lang(k)),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=10))
        tracks.append(card(col={"xs": 12, "md": 6}, content=ft.Column([
            ft.Text(f"{t['icon']} {t['title']}", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
            ft.Text(t["desc"], size=13, color=ft.colors.ON_SURFACE_VARIANT),
            ft.Divider(height=8, color=ft.colors.with_opacity(0.15, ft.colors.OUTLINE)),
            *steps], spacing=8)))
    return ft.Column([
        page_banner("Alur Belajar Pemrograman", "Tidak yakin harus mulai dari mana? Pilih jalur yang sesuai tujuan Anda.", mobile),
        ft.Container(padding=pad(mobile), content=ft.ResponsiveRow(tracks, spacing=16, run_spacing=16)),
    ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)
