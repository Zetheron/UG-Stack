import flet as ft

from components.ui import GREEN, card, chip, green_button, page_banner, pad
from content.languages import LANGS
from content.lessons import LESSONS


def get_tutorials_view(page: ft.Page, mobile: bool, on_open_lang, on_roadmap):
    cards = []
    for l in LANGS:
        cards.append(
            card(
                col={"xs": 12, "sm": 6, "md": 4},
                padding=0,
                on_click=lambda e, k=l["key"]: on_open_lang(k),
                content=ft.Column(
                    [
                        ft.Container(
                            bgcolor=l["color"],
                            padding=ft.padding.symmetric(horizontal=18, vertical=14),
                            border_radius=ft.border_radius.only(top_left=12, top_right=12),
                            content=ft.Row(
                                [
                                    ft.Text(l["icon"], size=24),
                                    ft.Text(f"Tutorial {l['name']}", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                ],
                                spacing=10,
                            ),
                        ),
                        ft.Container(
                            padding=18,
                            content=ft.Column(
                                [
                                    ft.Container(
                                        height=38,
                                        content=ft.Text(l["tagline"], size=13, color=ft.colors.ON_SURFACE_VARIANT),
                                    ),
                                    ft.Row(
                                        [
                                            chip(l["level"]),
                                            chip(l["group"], "#E1F5FE"),
                                            chip(f"{len(LESSONS[l['key']])} pelajaran", "#E7F9F0"),
                                        ],
                                        wrap=True,
                                        spacing=6,
                                    ),
                                    green_button("Mulai belajar ❯", lambda e, k=l["key"]: on_open_lang(k)),
                                ],
                                spacing=12,
                            ),
                        ),
                    ],
                    spacing=0,
                ),
            )
        )
    return ft.Column(
        [
            page_banner("Tutorial UG-Stack", "Pilih bahasa, belajar bertahap, lalu uji dengan quiz.", mobile),
            ft.Container(
                padding=pad(mobile),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Bingung mulai dari mana?", size=14, color=ft.colors.ON_SURFACE_VARIANT),
                                ft.TextButton("Lihat Alur Belajar ❯", on_click=lambda e: on_roadmap()),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            wrap=True,
                        ),
                        ft.ResponsiveRow(cards, spacing=16, run_spacing=16),
                    ],
                    spacing=16,
                ),
            ),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
