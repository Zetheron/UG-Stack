import flet as ft


def create_footer(on_footer_link=None):
    def make_link(text):
        return ft.TextButton(
            content=ft.Text(text, color=ft.colors.GREY_400, size=13),
            on_click=lambda e: on_footer_link(text) if on_footer_link else None,
            style=ft.ButtonStyle(padding=ft.padding.symmetric(horizontal=4, vertical=4)),
        )

    def make_col(title, links):
        return ft.Column(
            [
                ft.Text(title, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, size=15),
                ft.Container(height=4),
                *links,
            ],
            col={"xs": 6, "sm": 6, "md": 3},
            spacing=4,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

    return ft.Container(
        bgcolor="#1E262E",
        padding=ft.padding.symmetric(horizontal=32, vertical=36),
        content=ft.Column(
            [
                ft.ResponsiveRow(
                    [
                        make_col(
                            "Top Tutorials",
                            [
                                make_link("Python Tutorial"),
                                make_link("HTML Tutorial"),
                                make_link("CSS Tutorial"),
                                make_link("JavaScript Tutorial"),
                                make_link("SQL Tutorial"),
                            ],
                        ),
                        make_col(
                            "Top References",
                            [
                                make_link("Python Reference"),
                                make_link("HTML Reference"),
                                make_link("CSS Reference"),
                                make_link("JS Reference"),
                            ],
                        ),
                        make_col(
                            "Top Examples",
                            [
                                make_link("Python Examples"),
                                make_link("HTML Examples"),
                                make_link("CSS Examples"),
                            ],
                        ),
                        make_col(
                            "Get Certified",
                            [
                                make_link("HTML Certificate"),
                                make_link("Python Certificate"),
                                make_link("Front End Certificate"),
                            ],
                        ),
                    ],
                    spacing=20,
                    run_spacing=24,
                ),
                ft.Divider(color=ft.colors.with_opacity(0.15, ft.colors.WHITE), height=32),
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.PUBLIC,
                            icon_color=ft.colors.GREY_300,
                            icon_size=20,
                            tooltip="Website Utama",
                            on_click=lambda e: on_footer_link("Website UG-Stack") if on_footer_link else None,
                        ),
                        ft.IconButton(
                            ft.icons.CAMERA_ALT,
                            icon_color=ft.colors.GREY_300,
                            icon_size=20,
                            tooltip="Instagram Resmi",
                            on_click=lambda e: on_footer_link("Instagram Official") if on_footer_link else None,
                        ),
                        ft.IconButton(
                            ft.icons.CHAT,
                            icon_color=ft.colors.GREY_300,
                            icon_size=20,
                            tooltip="Komunitas Discord",
                            on_click=lambda e: on_footer_link("Discord Community") if on_footer_link else None,
                        ),
                        ft.IconButton(
                            ft.icons.WORK,
                            icon_color=ft.colors.GREY_300,
                            icon_size=20,
                            tooltip="Profil LinkedIn",
                            on_click=lambda e: on_footer_link("LinkedIn") if on_footer_link else None,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                ),
                ft.Row(
                    [
                        ft.Text(
                            "© 2026 UG-Stack. Platform Edukasi Koding Berbasis Full Python (Flet).",
                            color=ft.colors.GREY_500,
                            size=12,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=10,
        ),
    )
