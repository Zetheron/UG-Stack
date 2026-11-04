import flet as ft

from components.ui import LOGO_URLS, lang_logo

COURSES = [
    ("HTML", "The building blocks of every webpage", "#D9EEE1"),
    ("CSS", "Style and layout for web pages", "#FFF4A3"),
    ("JavaScript", "Interactive and dynamic web pages", "#E7E9EB"),
    ("Python", "Popular language for web, data & AI", "#F3E5F5"),
    ("SQL", "Query and manage databases", "#E8EAF6"),
    ("PHP", "A web server programming language", "#FFD2D7"),
    ("jQuery", "A JS library for developing web pages", "#E1F5FE"),
    ("Java", "Object-oriented programming language", "#FFF8E1"),
    ("C++", "A powerful general-purpose language", "#E8F5E9"),
    ("C#", "A multi-paradigm programming language", "#F3E5F5"),
    ("React", "Building user interfaces for web", "#E0F7FA"),
    ("MySQL", "Relational database management system", "#E1F5FE"),
]


def create_course_card(title, desc, color_bg, on_select_course=None):
    return ft.Container(
        bgcolor=ft.colors.SURFACE,
        padding=20,
        border_radius=12,
        border=ft.border.all(1, ft.colors.with_opacity(0.18, ft.colors.OUTLINE)),
        col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
        on_click=lambda e: on_select_course(title) if on_select_course else None,
        ink=True,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=[
                ft.Container(
                    width=54,
                    height=54,
                    bgcolor=color_bg,
                    border_radius=12,
                    alignment=ft.alignment.center,
                    content=lang_logo(title, 32),
                ),
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE, text_align=ft.TextAlign.CENTER),
                ft.Container(
                    height=38,
                    alignment=ft.alignment.center,
                    content=ft.Text(desc, text_align=ft.TextAlign.CENTER, color=ft.colors.ON_SURFACE_VARIANT, size=12),
                ),
                ft.ElevatedButton(
                    f"Learn {title}",
                    bgcolor="#282A35",
                    color=ft.colors.WHITE,
                    width=160,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(horizontal=16, vertical=10),
                        elevation=0,
                    ),
                    on_click=lambda e: on_select_course(title) if on_select_course else None,
                ),
            ],
        ),
    )


def create_courses_grid(on_select_course=None, on_more_courses=None):
    cards = [create_course_card(title, desc, bg, on_select_course) for title, desc, bg in COURSES]

    return ft.Container(
        padding=ft.padding.symmetric(vertical=32, horizontal=32),
        bgcolor=ft.colors.SURFACE,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
            controls=[
                ft.Text("Popular Courses", size=26, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE, text_align=ft.TextAlign.CENTER),
                ft.ResponsiveRow(spacing=16, run_spacing=16, controls=cards),
                ft.Container(
                    padding=ft.padding.only(top=8),
                    alignment=ft.alignment.center,
                    content=ft.ElevatedButton(
                        "And 40+ more ❯",
                        bgcolor="#04AA6D",
                        color=ft.colors.WHITE,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(horizontal=24, vertical=12),
                            elevation=0,
                        ),
                        on_click=lambda e: on_more_courses() if on_more_courses else None,
                    ),
                ),
            ],
        ),
    )
