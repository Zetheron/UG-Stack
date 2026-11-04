import flet as ft


def create_hero_section(on_search=None, on_roadmap_click=None, on_primary_click=None,
                        primary_label="Create Free Account", progress_text=None):
    search_tf = ft.TextField(
        hint_text="Search e.g. Python, HTML, SQL...",
        bgcolor=ft.colors.SURFACE,
        border_radius=10,
        border_color=ft.colors.with_opacity(0.2, ft.colors.OUTLINE),
        color=ft.colors.ON_SURFACE,
        suffix=ft.IconButton(
            ft.icons.SEARCH,
            icon_color="#04AA6D",
            icon_size=20,
            tooltip="Cari",
            on_click=lambda e: on_search(search_tf.value) if on_search else None,
        ),
        content_padding=ft.padding.symmetric(horizontal=16, vertical=10),
        on_submit=lambda e: on_search(search_tf.value) if on_search else None
    )

    left_content = ft.Container(
        col={"xs": 12, "md": 6},
        padding=ft.padding.symmetric(vertical=8),
        content=ft.Column([
            ft.Text("Learn to Code", size=36, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(
                "With Gunadarma's largest web developer learning platform.",
                size=15, color="#C8CCD4", weight=ft.FontWeight.W_500
            ),
            ft.Container(height=8),
            search_tf,
            ft.TextButton(
                content=ft.Text(
                    "Not Sure Where To Begin?",
                    color="#04AA6D",
                    size=13,
                    weight=ft.FontWeight.W_600,
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                ),
                on_click=lambda e: on_roadmap_click() if on_roadmap_click else None
            )
        ], spacing=8),
    )

    badge = ft.Container(
        content=ft.Text("PRO FEATURES", size=10, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
        bgcolor="#FFF4A3", padding=ft.padding.symmetric(horizontal=8, vertical=4), border_radius=6
    )
    top_row = [badge]
    if progress_text:
        top_row.append(ft.Text(progress_text, color="#00FF66", weight=ft.FontWeight.BOLD, size=12))

    feature = lambda t: ft.Row([ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color="#04AA6D", size=16),
                                ft.Text(t, color="#E5E9F0", size=13)], spacing=8)

    pro_card = ft.Container(
        bgcolor="#1E262E",
        padding=24,
        border_radius=12,
        border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.WHITE)),
        col={"xs": 12, "md": 6},
        content=ft.Column([
            ft.Row(top_row, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, wrap=True),
            ft.Text("Upgrade Your Learning Experience", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Divider(color=ft.colors.with_opacity(0.15, ft.colors.WHITE), height=12),
            feature("Progress tracking & analytics"),
            feature("Ad-free learning environment"),
            feature("Interactive quizzes & practice"),
            feature("Official UG-Stack Certificates"),
            ft.Container(height=6),
            ft.ElevatedButton(
                primary_label,
                bgcolor="#04AA6D",
                color=ft.colors.WHITE,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=ft.padding.symmetric(horizontal=20, vertical=12),
                    elevation=0,
                ),
                on_click=lambda e: on_primary_click() if on_primary_click else None
            )
        ], spacing=8)
    )

    return ft.Container(
        bgcolor="#282A35",
        padding=ft.padding.symmetric(vertical=36, horizontal=32),
        content=ft.ResponsiveRow([left_content, pro_card], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=24, run_spacing=20)
    )
