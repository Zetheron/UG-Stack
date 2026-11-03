"""Komponen UI bersama bergaya UG-Stack Minimalis (hijau #04AA6D, gelap #282A35)."""
import flet as ft

GREEN = "#04AA6D"
DARK = "#282A35"
LIGHT_GREEN = ft.colors.PRIMARY_CONTAINER
SIDEBAR = ft.colors.SURFACE_VARIANT

_BTN_STYLE = ft.ButtonStyle(
    shape=ft.RoundedRectangleBorder(radius=8),
    padding=ft.padding.symmetric(horizontal=18, vertical=12),
    elevation=0,
)


def pad(mobile: bool) -> int:
    return 16 if mobile else 32


def link_text(text: str, url: str, size: int = 13, color: str = GREEN) -> ft.Text:
    """Teks tautan yang bisa membungkus baris (aman untuk judul panjang)."""
    return ft.Text(
        spans=[ft.TextSpan(text, ft.TextStyle(color=color, decoration=ft.TextDecoration.UNDERLINE), url=url)],
        size=size,
    )


def chip(text: str, bg: str = "#FFF4A3", fg: str = ft.colors.BLACK) -> ft.Container:
    return ft.Container(
        ft.Text(text, size=11, weight=ft.FontWeight.W_600, color=fg),
        bgcolor=bg,
        padding=ft.padding.symmetric(horizontal=10, vertical=4),
        border_radius=8,
    )


def page_banner(title: str, subtitle: str = "", mobile: bool = False, accent: str = GREEN) -> ft.Container:
    return ft.Container(
        bgcolor=DARK,
        padding=ft.padding.symmetric(vertical=28 if not mobile else 20, horizontal=pad(mobile)),
        content=ft.Column(
            [
                ft.Text(
                    title,
                    size=28 if not mobile else 22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(width=48, height=3, bgcolor=accent, border_radius=2),
                ft.Text(
                    subtitle,
                    size=14,
                    color="#C8CCD4",
                    text_align=ft.TextAlign.CENTER,
                )
                if subtitle
                else ft.Container(),
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def section_heading(text: str) -> ft.Text:
    return ft.Text(text, size=19, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE)


def green_button(text: str, on_click, **kw) -> ft.ElevatedButton:
    kw.setdefault("style", _BTN_STYLE)
    return ft.ElevatedButton(text, bgcolor=GREEN, color=ft.colors.WHITE, on_click=on_click, **kw)


def dark_button(text: str, on_click, **kw) -> ft.ElevatedButton:
    kw.setdefault("style", _BTN_STYLE)
    return ft.ElevatedButton(text, bgcolor=DARK, color=ft.colors.WHITE, on_click=on_click, **kw)


def card(content, col=None, bg=ft.colors.SURFACE, padding=20, on_click=None) -> ft.Container:
    return ft.Container(
        content=content,
        col=col,
        bgcolor=bg,
        padding=padding,
        border_radius=12,
        border=ft.border.all(1, ft.colors.with_opacity(0.18, ft.colors.OUTLINE)),
        on_click=on_click,
        ink=bool(on_click),
    )


def code_block(page: ft.Page, code: str, title: str = "Contoh kode") -> ft.Container:
    def copy(e):
        page.set_clipboard(code)
        page.show_snack("Kode disalin ke clipboard.")

    return ft.Container(
        bgcolor="#1E1F26",
        border_radius=10,
        padding=ft.padding.only(left=16, right=8, top=4, bottom=14),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(title, size=11, color="#9AA0A6", weight=ft.FontWeight.W_500),
                        ft.IconButton(
                            ft.icons.COPY,
                            icon_size=15,
                            icon_color="#9AA0A6",
                            tooltip="Salin kode",
                            on_click=copy,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Text(code, font_family="monospace", size=13, color="#E6E6E6", selectable=True),
            ],
            spacing=0,
        ),
    )
