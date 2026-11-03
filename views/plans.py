import flet as ft

from components.ui import GREEN, card, page_banner, pad
from services import enrollment

PLAN_DATA = [
    ("basic", "Basic", "Gratis (demo)", ["Akses semua tutorial", "Tanpa iklan", "Dukungan komunitas"], False),
    ("pro", "Pro Plus", "Gratis (demo)", ["Semua fitur Basic", "Quiz dan sertifikat tanpa batas", "Roadmap pribadi"], True),
    ("lifetime", "Lifetime", "Gratis (demo)", ["Akses selamanya", "Dukungan prioritas", "Semua kursus mendatang"], False),
]


def get_plans_view(page: ft.Page, user, mobile: bool, on_login, on_changed):
    current = enrollment.get_info(user["username"])["plan"] if user else None

    def choose(key):
        if not user:
            page.show_snack("Login terlebih dahulu untuk memilih paket.")
            on_login()
            return
        ok, msg = enrollment.set_plan(user["username"], key)
        page.show_snack(msg)
        if ok:
            on_changed()

    cards = []
    for key, name, price, features, popular in PLAN_DATA:
        active = key == current
        cards.append(
            ft.Container(
                col={"xs": 12, "sm": 6, "md": 4},
                padding=24,
                border_radius=12,
                bgcolor=ft.colors.SECONDARY_CONTAINER if popular else ft.colors.SURFACE,
                border=ft.border.all(
                    2 if popular else 1,
                    "#9B51E0" if popular else ft.colors.with_opacity(0.18, ft.colors.OUTLINE),
                ),
                content=ft.Column(
                    [
                        ft.Text(name, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE, text_align=ft.TextAlign.CENTER),
                        ft.Text(price, size=24, weight=ft.FontWeight.BOLD, color=GREEN, text_align=ft.TextAlign.CENTER),
                        ft.Divider(height=12, color=ft.colors.with_opacity(0.15, ft.colors.OUTLINE)),
                        *[
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=GREEN, size=18),
                                    ft.Text(f, color=ft.colors.ON_SURFACE_VARIANT, size=13, expand=True),
                                ],
                                spacing=8,
                            )
                            for f in features
                        ],
                        ft.Container(height=8),
                        ft.ElevatedButton(
                            "✓ Paket aktif" if active else "Pilih paket",
                            disabled=active,
                            bgcolor="#9B51E0" if popular else GREEN,
                            color=ft.colors.WHITE,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8),
                                padding=ft.padding.symmetric(horizontal=20, vertical=13),
                                elevation=0,
                            ),
                            on_click=lambda e, k=key: choose(k),
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                ),
            )
        )
    note = (
        f"Paket Anda saat ini: {enrollment.PLANS[current]}."
        if current
        else ("Anda belum memilih paket." if user else "Login untuk memilih paket.")
    )
    return ft.Column(
        [
            page_banner("Pilih Paket Belajar", "Mode demo kampus: paket aktif tanpa pembayaran.", mobile, "#9B51E0"),
            ft.Container(
                padding=pad(mobile),
                content=ft.Column(
                    [
                        ft.Text(note, size=14, color=ft.colors.ON_SURFACE_VARIANT),
                        ft.ResponsiveRow(cards, spacing=16, run_spacing=16),
                    ],
                    spacing=16,
                ),
            ),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
