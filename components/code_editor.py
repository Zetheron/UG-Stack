import flet as ft

SAMPLES = {
    "HTML": "<!DOCTYPE html>\n<html>\n<head>\n  <title>HTML Tutorial</title>\n</head>\n<body>\n  <h1>This is a Heading</h1>\n  <p>This is a paragraph.</p>\n</body>\n</html>",
    "CSS": "body {\n  background-color: lightblue;\n}\nh1 {\n  color: navy;\n  text-align: center;\n}",
    "JavaScript": "function myFunction() {\n  console.log('Hello from UG-Stack JavaScript!');\n}\nmyFunction();",
    "Python": "def ug_stack_welcome(user):\n    print(f'Selamat Datang {user} di UG-Stack!')\n\nug_stack_welcome('Mahasiswa Gunadarma')",
    "SQL": "SELECT * FROM Customers\nWHERE Country='Indonesia'\nORDER BY CustomerName;",
    "PHP": "<?php\n$nama = \"Mahasiswa Gunadarma\";\necho \"Halo, \" . $nama . \"!\";\n?>",
    "Java": "public class Main {\n  public static void main(String[] args) {\n    System.out.println(\"Halo dari Java UG-Stack!\");\n  }\n}",
    "C": "#include <stdio.h>\n\nint main(void) {\n  printf(\"Halo dari C UG-Stack!\\n\");\n  return 0;\n}",
    "C++": "#include <iostream>\nusing namespace std;\n\nint main() {\n  cout << \"Halo dari C++ UG-Stack!\" << endl;\n  return 0;\n}",
    "C#": "using System;\n\nclass Program {\n  static void Main() {\n    Console.WriteLine(\"Halo dari C# UG-Stack!\");\n  }\n}",
    "React": "function App() {\n  return <h1>Halo dari React UG-Stack!</h1>;\n}\nexport default App;",
    "MySQL": "SELECT nama, prodi, ipk FROM mahasiswa\nWHERE ipk >= 3.5\nORDER BY ipk DESC;",
}

HOME_TABS = ("HTML", "CSS", "JavaScript", "Python", "SQL")


def create_editor_section(on_tryit_click=None):
    code_text = ft.Text(SAMPLES["HTML"], font_family="monospace", color="#00FF66", size=13, selectable=True)
    active_lang = {"value": "HTML"}

    def change_tab(lang):
        active_lang["value"] = lang
        code_text.value = SAMPLES[lang]
        for btn in tab_buttons.controls:
            if btn.text == lang:
                btn.bgcolor = "#04AA6D"
                btn.color = ft.colors.WHITE
            else:
                btn.bgcolor = ft.colors.with_opacity(0.35, ft.colors.OUTLINE)
                btn.color = ft.colors.ON_SURFACE
        code_text.update()
        tab_buttons.update()

    def handle_tryit(e):
        if not on_tryit_click:
            return
        lang = active_lang["value"]
        try:
            on_tryit_click(lang, SAMPLES[lang])
        except TypeError:
            on_tryit_click(lang)

    tab_buttons = ft.Row([
        ft.ElevatedButton(
            lang,
            on_click=lambda e, l=lang: change_tab(l),
            bgcolor="#04AA6D" if i == 0 else ft.colors.with_opacity(0.35, ft.colors.OUTLINE),
            color=ft.colors.WHITE if i == 0 else ft.colors.ON_SURFACE,
        )
        for i, lang in enumerate(HOME_TABS)
    ], scroll=ft.ScrollMode.AUTO, spacing=8, alignment=ft.MainAxisAlignment.CENTER)

    return ft.Container(
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=ft.padding.symmetric(vertical=35, horizontal=20),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Text("What do you want to learn?", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE, text_align=ft.TextAlign.CENTER),
                ft.Text("Mulai latihan koding interaktif langsung di browser kamu.", color=ft.colors.ON_SURFACE_VARIANT, text_align=ft.TextAlign.CENTER),
                ft.Container(height=10),
                tab_buttons,
                ft.Container(height=15),
                ft.Container(
                    bgcolor=ft.colors.SURFACE,
                    border_radius=10,
                    border=ft.border.all(1, ft.colors.with_opacity(0.35, ft.colors.OUTLINE)),
                    padding=20,
                    content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.STRETCH, controls=[
                        ft.Row([
                            ft.Text("Code Example:", weight=ft.FontWeight.BOLD, size=16, color=ft.colors.ON_SURFACE),
                            ft.Container(expand=True),
                            ft.Icon(ft.icons.CODE, color=ft.colors.ON_SURFACE_VARIANT)
                        ]),
                        ft.Container(
                            bgcolor="#282A35",
                            padding=15,
                            border_radius=6,
                            content=ft.Column([code_text], spacing=0)
                        ),
                        ft.Container(height=10),
                        ft.Row([
                            ft.ElevatedButton(
                                "Try it Yourself ❯",
                                bgcolor="#04AA6D",
                                color=ft.colors.WHITE,
                                style=ft.ButtonStyle(padding=ft.padding.symmetric(horizontal=25, vertical=15)),
                                on_click=handle_tryit
                            )
                        ])
                    ])
                )
            ]
        )
    )
