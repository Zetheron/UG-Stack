import flet as ft

_BTN_STYLE = ft.ButtonStyle(
    shape=ft.RoundedRectangleBorder(radius=8),
    padding=ft.padding.symmetric(horizontal=16, vertical=10),
    elevation=0,
)


def create_app_banner(on_tryit_click=None, on_pwa_install=None):
    return ft.Container(
        padding=ft.padding.symmetric(vertical=24, horizontal=32),
        content=ft.Container(
            bgcolor=ft.colors.PRIMARY_CONTAINER,
            padding=28,
            border_radius=12,
            border=ft.border.all(1, ft.colors.with_opacity(0.18, ft.colors.OUTLINE)),
            content=ft.ResponsiveRow([
                ft.Column([
                    ft.Text("UG-Stack Adventure App", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                    ft.Text(
                        "Learn to code by playing a game! Available on mobile and desktop devices.",
                        size=14, color=ft.colors.ON_SURFACE_VARIANT
                    ),
                    ft.Container(height=8),
                    ft.Row([
                        ft.ElevatedButton(
                            content=ft.Row([ft.Icon(ft.icons.PHONE_IPHONE, size=18), ft.Text("App Store")], spacing=6, tight=True),
                            bgcolor="#282A35", color=ft.colors.WHITE, style=_BTN_STYLE,
                            on_click=lambda e: on_pwa_install("iOS") if on_pwa_install else None
                        ),
                        ft.ElevatedButton(
                            content=ft.Row([ft.Icon(ft.icons.ANDROID, size=18), ft.Text("Google Play")], spacing=6, tight=True),
                            bgcolor="#282A35", color=ft.colors.WHITE, style=_BTN_STYLE,
                            on_click=lambda e: on_pwa_install("Android") if on_pwa_install else None
                        ),
                        ft.OutlinedButton(
                            content=ft.Text("Try now in Browser", color=ft.colors.ON_SURFACE),
                            style=_BTN_STYLE,
                            on_click=lambda e: on_tryit_click("HTML") if on_tryit_click else None
                        )
                    ], wrap=True, spacing=10, run_spacing=10)
                ], col={"xs": 12, "md": 8}, spacing=6),
                ft.Column([
                    ft.Container(
                        content=ft.Icon(ft.icons.SMARTPHONE, size=72, color="#04AA6D"),
                        alignment=ft.alignment.center
                    )
                ], col={"xs": 12, "md": 4}, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=16)
        )
    )
