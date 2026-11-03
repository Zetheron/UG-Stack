import flet as ft


def create_save_progress_section(on_primary_click=None, primary_label="Sign Up For Free"):
    return ft.Container(
        padding=ft.padding.symmetric(horizontal=32, vertical=16),
        content=ft.Container(
            bgcolor=ft.colors.PRIMARY_CONTAINER,
            padding=ft.padding.symmetric(horizontal=32, vertical=32),
            border_radius=12,
            border=ft.border.all(1, ft.colors.with_opacity(0.18, ft.colors.OUTLINE)),
            content=ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            ft.Text("Save your progress. Everywhere.", size=26, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                            ft.Text(
                                "Create a free account to track your progress, score points, and log in from anywhere.",
                                size=14,
                                color=ft.colors.ON_SURFACE_VARIANT,
                            ),
                            ft.Container(height=6),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color="#04AA6D", size=18), ft.Text("Track your progress", size=13, color=ft.colors.ON_SURFACE)], spacing=8),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color="#04AA6D", size=18), ft.Text("Earn free certificates", size=13, color=ft.colors.ON_SURFACE)], spacing=8),
                            ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color="#04AA6D", size=18), ft.Text("Access interactive quizzes", size=13, color=ft.colors.ON_SURFACE)], spacing=8),
                        ],
                        col={"xs": 12, "md": 6},
                        spacing=8,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                bgcolor=ft.colors.SURFACE,
                                padding=24,
                                border_radius=12,
                                border=ft.border.all(1, ft.colors.with_opacity(0.18, ft.colors.OUTLINE)),
                                content=ft.Column(
                                    [
                                        ft.Text("Start in one click", weight=ft.FontWeight.BOLD, size=18, color=ft.colors.ON_SURFACE),
                                        ft.Text(
                                            "Login atau daftar untuk membuka dashboard modul dan progres belajar.",
                                            size=13,
                                            color=ft.colors.ON_SURFACE_VARIANT,
                                        ),
                                        ft.Container(height=4),
                                        ft.ElevatedButton(
                                            primary_label,
                                            bgcolor="#04AA6D",
                                            color=ft.colors.WHITE,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                padding=ft.padding.symmetric(horizontal=22, vertical=14),
                                                elevation=0,
                                            ),
                                            on_click=lambda e: on_primary_click() if on_primary_click else None,
                                        ),
                                    ],
                                    spacing=10,
                                ),
                            )
                        ],
                        col={"xs": 12, "md": 6},
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=24,
                run_spacing=20,
            ),
        ),
    )


def create_career_spaces_sections(on_cert_click=None, on_spaces_click=None):
    btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=8),
        padding=ft.padding.symmetric(horizontal=20, vertical=13),
        elevation=0,
    )
    career_card = ft.Container(
        bgcolor=ft.colors.SURFACE,
        padding=28,
        border_radius=12,
        border=ft.border.all(1, ft.colors.with_opacity(0.18, ft.colors.OUTLINE)),
        col={"xs": 12, "md": 6},
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Kickstart your career", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                                ft.Text("Get certified by completing a course today!", size=13, color=ft.colors.ON_SURFACE_VARIANT),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.Icon(ft.icons.VERIFIED, size=40, color="#04AA6D"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    "Get Certified",
                    bgcolor="#04AA6D",
                    color=ft.colors.WHITE,
                    style=btn_style,
                    on_click=lambda e: on_cert_click() if on_cert_click else None,
                ),
            ],
            spacing=8,
        ),
    )

    spaces_card = ft.Container(
        bgcolor="#1E262E",
        padding=28,
        border_radius=12,
        border=ft.border.all(1, ft.colors.with_opacity(0.15, ft.colors.WHITE)),
        col={"xs": 12, "md": 6},
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Build and host websites", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                ft.Text("Create your own website with UG-Stack Spaces.", size=13, color="#B0BEC5"),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.Icon(ft.icons.TERMINAL, size=40, color="#04AA6D"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    "Try Spaces",
                    bgcolor="#04AA6D",
                    color=ft.colors.WHITE,
                    style=btn_style,
                    on_click=lambda e: on_spaces_click() if on_spaces_click else None,
                ),
            ],
            spacing=8,
        ),
    )

    return ft.Container(
        padding=ft.padding.symmetric(horizontal=32, vertical=12),
        content=ft.ResponsiveRow([career_card, spaces_card], spacing=16, run_spacing=16),
    )
