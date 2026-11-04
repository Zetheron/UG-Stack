"""Komponen tema Dashboard Modern Dark-Glass (terinspirasi ModyLearn) untuk Panel Admin, Dosen, dan Mahasiswa."""
import flet as ft

BG_MAIN = "#0B0A14"
BG_SIDEBAR = "#100E1E"
BG_CARD = "#151226"
BG_CARD_ALT = "#1B1730"
BORDER_SUBTLE = "#262240"
TEXT_PRIMARY = "#F9FAFB"
TEXT_MUTED = "#9CA3AF"
ACCENT_ORANGE = "#F59E0B"
ACCENT_GREEN = "#04AA6D"


def glass_card(content: ft.Control, col=None, padding=20, bg=BG_CARD, border_color=BORDER_SUBTLE, radius=16) -> ft.Container:
    return ft.Container(
        content=content,
        col=col,
        bgcolor=bg,
        padding=padding,
        border_radius=radius,
        border=ft.border.all(1, border_color),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=18,
            color=ft.colors.with_opacity(0.28, "#000000"),
            offset=ft.Offset(0, 6),
        ),
    )


def kpi_glow_card(label: str, value_str: str, icon_name: str, glow_color: str, sub_label: str = "", col=None) -> ft.Container:
    """Kartu KPI bergaya ModyLearn dengan nilai besar di kiri dan kotak ikon berpendar (glow) di kanan."""
    icon_box = ft.Container(
        width=48,
        height=48,
        border_radius=14,
        bgcolor=ft.colors.with_opacity(0.16, glow_color),
        border=ft.border.all(1, ft.colors.with_opacity(0.45, glow_color)),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=24,
            color=ft.colors.with_opacity(0.38, glow_color),
            offset=ft.Offset(0, 0),
        ),
        content=ft.Icon(icon_name, color=glow_color, size=22),
    )
    left_items = [
        ft.Text(label, size=11, weight=ft.FontWeight.W_600, color=TEXT_MUTED),
        ft.Text(str(value_str), size=28, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
    ]
    if sub_label:
        left_items.append(ft.Text(sub_label, size=11, color=TEXT_MUTED))

    return glass_card(
        col=col or {"xs": 12, "sm": 6, "md": 4},
        padding=22,
        content=ft.Row(
            [
                ft.Column(left_items, spacing=4, expand=True),
                icon_box,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def top_bar(title: str, subtitle: str, right_controls: list = None) -> ft.Container:
    """Header atas pada area konten utama Dashboard dengan indikator '● Data langsung'."""
    live_pill = ft.Container(
        bgcolor="#0E291E",
        border=ft.border.all(1, "#10B981"),
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=12, vertical=6),
        content=ft.Text("● Data langsung", size=11, weight=ft.FontWeight.BOLD, color="#34D399"),
    )
    actions = [
        ft.Container(
            width=36,
            height=36,
            border_radius=18,
            bgcolor=BG_CARD,
            border=ft.border.all(1, BORDER_SUBTLE),
            alignment=ft.alignment.center,
            content=ft.Icon(ft.icons.NOTIFICATIONS_NONE_ROUNDED, color=TEXT_MUTED, size=18),
        ),
        live_pill,
    ]
    if right_controls:
        actions.extend(right_controls)

    return ft.Row(
        [
            ft.Column(
                [
                    ft.Text(title, size=28, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                    ft.Text(subtitle, size=13, color=TEXT_MUTED),
                ],
                spacing=2,
            ),
            ft.Row(actions, spacing=10, wrap=True, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        wrap=True,
    )


def activity_trend_card(extra_bottom: ft.Control = None, col=None) -> ft.Container:
    """Kartu grafik tren aktivitas bulanan bergaya kurva/batang berpendar."""
    points = [
        ("JAN", 0.28, "#8B5CF6"),
        ("MAR", 0.42, "#A855F7"),
        ("MEI", 0.88, "#F97316"),
        ("JUL", 0.56, "#FB923C"),
        ("SEP", 0.48, "#C084FC"),
        ("NOV", 0.64, "#F59E0B"),
    ]
    bars = []
    for month, ratio, color in points:
        bar_h = int(24 + ratio * 95)
        bars.append(
            ft.Column(
                [
                    ft.Container(
                        width=12,
                        height=12,
                        border_radius=6,
                        bgcolor=BG_CARD,
                        border=ft.border.all(2.5, color),
                        shadow=ft.BoxShadow(blur_radius=10, spread_radius=1, color=ft.colors.with_opacity(0.6, color)),
                    ),
                    ft.Container(
                        width=22,
                        height=bar_h,
                        border_radius=ft.border_radius.only(top_left=6, top_right=6, bottom_left=2, bottom_right=2),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors.with_opacity(0.55, color), ft.colors.with_opacity(0.06, color)],
                        ),
                    ),
                    ft.Text(month, size=10, weight=ft.FontWeight.BOLD, color=TEXT_MUTED),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.END,
                spacing=4,
                expand=True,
            )
        )

    chart_area = ft.Container(
        height=170,
        padding=ft.padding.only(top=12, left=8, right=8, bottom=4),
        border=ft.border.only(bottom=ft.BorderSide(1, BORDER_SUBTLE)),
        content=ft.Row(bars, alignment=ft.MainAxisAlignment.SPACE_AROUND, vertical_alignment=ft.CrossAxisAlignment.END),
    )

    badge = ft.Container(
        bgcolor="#271B18",
        border=ft.border.all(1, "#F59E0B"),
        border_radius=18,
        padding=ft.padding.symmetric(horizontal=12, vertical=5),
        content=ft.Text("📅 ANALITIK 2026", size=10, weight=ft.FontWeight.BOLD, color="#FBBF24"),
    )

    body_items = [
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Tren Aktivitas & Progres", size=17, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                        ft.Text("RINGKASAN AKTIVITAS BULANAN", size=10, weight=ft.FontWeight.W_600, color=TEXT_MUTED),
                    ],
                    spacing=2,
                ),
                badge,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True,
        ),
        chart_area,
    ]
    if extra_bottom is not None:
        body_items.append(extra_bottom)

    return glass_card(
        col=col or {"xs": 12, "lg": 8},
        padding=22,
        content=ft.Column(body_items, spacing=14),
    )


def categories_donut_card(total_modules: int, col=None) -> ft.Container:
    """Kartu cincin donat kategori bahasa/modul di sisi kanan seperti desain referensi."""
    cats = [
        ("Pengembangan Web", "38%", "#F97316", 0.38),
        ("Data & Basis Data", "25%", "#8B5CF6", 0.25),
        ("Umum", "22%", "#10B981", 0.22),
        ("Sistem", "15%", "#3B82F6", 0.15),
    ]
    ring_stack = ft.Stack(
        [
            ft.ProgressRing(value=1.0, width=148, height=148, stroke_width=16, color="#8B5CF6", bgcolor="#231E3D"),
            ft.ProgressRing(value=0.68, width=148, height=148, stroke_width=16, color="#F97316", bgcolor=ft.colors.TRANSPARENT),
            ft.ProgressRing(value=0.32, width=148, height=148, stroke_width=16, color="#10B981", bgcolor=ft.colors.TRANSPARENT),
            ft.Container(
                width=148,
                height=148,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Text(str(total_modules), size=26, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                        ft.Text("TOTAL MODUL", size=9, weight=ft.FontWeight.BOLD, color=TEXT_MUTED),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                ),
            ),
        ],
        width=148,
        height=148,
    )

    legend_rows = []
    for label, pct_str, color, _ in cats:
        legend_rows.append(
            ft.Container(
                padding=ft.padding.symmetric(vertical=6, horizontal=10),
                bgcolor=BG_CARD_ALT,
                border_radius=8,
                content=ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Container(width=10, height=10, border_radius=5, bgcolor=color),
                                ft.Text(label, size=12, color=TEXT_MUTED),
                            ],
                            spacing=8,
                        ),
                        ft.Text(pct_str, size=12, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            )
        )

    return glass_card(
        col=col or {"xs": 12, "lg": 4},
        padding=22,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Kategori Modul", size=17, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                        ft.Container(
                            width=32,
                            height=32,
                            border_radius=8,
                            bgcolor=BG_CARD_ALT,
                            border=ft.border.all(1, BORDER_SUBTLE),
                            alignment=ft.alignment.center,
                            content=ft.Icon(ft.icons.GRID_VIEW_ROUNDED, size=16, color=TEXT_MUTED),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(content=ring_stack, alignment=ft.alignment.center, padding=ft.padding.symmetric(vertical=8)),
                ft.Column(legend_rows, spacing=6),
            ],
            spacing=12,
        ),
    )


def sidebar_shell(brand_title: str, nav_buttons: list, user: dict, profile_actions: list, col=None) -> ft.Container:
    """Sidebar kiri bergaya ModyLearn dengan logo di atas, menu di tengah, dan kartu profil di bawah."""
    initial = (user.get("username") or "U")[0].upper()
    role_upper = (user.get("role") or "mahasiswa").upper()

    brand = ft.Container(
        padding=ft.padding.only(left=6, right=6, top=4, bottom=12),
        border=ft.border.only(bottom=ft.BorderSide(1, BORDER_SUBTLE)),
        content=ft.Row(
            [
                ft.Container(
                    width=40,
                    height=40,
                    border_radius=12,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=["#A855F7", "#F97316"],
                    ),
                    alignment=ft.alignment.center,
                    content=ft.Icon(ft.icons.AUTO_AWESOME, color=ft.colors.WHITE, size=20),
                ),
                ft.Column(
                    [
                        ft.Text(brand_title, size=15, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                        ft.Text("UG-Stack", size=11, weight=ft.FontWeight.W_600, color=TEXT_MUTED),
                    ],
                    spacing=0,
                ),
            ],
            spacing=10,
        ),
    )

    profile_card = ft.Container(
        bgcolor=BG_CARD,
        border=ft.border.all(1, BORDER_SUBTLE),
        border_radius=14,
        padding=12,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=36,
                            height=36,
                            border_radius=18,
                            bgcolor=BG_CARD_ALT,
                            border=ft.border.all(1, "#3B345E"),
                            alignment=ft.alignment.center,
                            content=ft.Text(initial, size=14, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                        ),
                        ft.Column(
                            [
                                ft.Text(user.get("username", ""), size=13, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                                ft.Text(role_upper, size=10, weight=ft.FontWeight.W_600, color=TEXT_MUTED),
                            ],
                            spacing=0,
                            expand=True,
                        ),
                    ],
                    spacing=10,
                ),
                ft.Divider(height=8, color=BORDER_SUBTLE),
                ft.Row(profile_actions, wrap=True, spacing=6, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ],
            spacing=8,
        ),
    )

    return ft.Container(
        col=col or {"xs": 12, "md": 3, "lg": 3},
        bgcolor=BG_SIDEBAR,
        padding=16,
        border_radius=18,
        border=ft.border.all(1, BORDER_SUBTLE),
        content=ft.Column(
            [
                brand,
                ft.Column(nav_buttons, spacing=6),
                ft.Divider(height=12, color=BORDER_SUBTLE),
                profile_card,
            ],
            spacing=12,
        ),
    )


def sidebar_nav_btn(label: str, active: bool, on_click) -> ft.ElevatedButton:
    """Tombol navigasi sidebar dengan pendaran oranye hangat saat aktif."""
    return ft.ElevatedButton(
        text=label,
        bgcolor="#2B1C19" if active else BG_CARD,
        color="#FBBF24" if active else "#D1D5DB",
        width=280,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=14, vertical=12),
            shape=ft.RoundedRectangleBorder(radius=12),
            side=ft.BorderSide(1, ACCENT_ORANGE if active else BORDER_SUBTLE),
            elevation=0,
        ),
        on_click=on_click,
    )
