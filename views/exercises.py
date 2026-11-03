import flet as ft

from components.ui import GREEN, card, chip, dark_button, green_button, page_banner, pad
from content.languages import LANGS
from content.lessons import LESSONS
from content.quizzes import PASS_PERCENT
from services import quiz as quiz_service
from services import quiz_admin
from views.tryit import create_simulator_cards


def get_exercises_view(page: ft.Page, user, mobile: bool, on_open_quiz, on_tryit=None):
    results = quiz_service.get_results(user["username"]) if user else {}
    cards = []
    for l in LANGS:
        rec = results.get(l["key"])
        if rec and rec.get("passed_at"):
            status = chip(f"Lulus - terbaik {rec['best']}%", "#C8E6C9")
        elif rec:
            status = chip(f"Terbaik {rec['best']}% (belum lulus)", "#FFE0B2")
        else:
            status = chip("Belum dicoba", "#EEEEEE")
        sample_code = LESSONS[l["key"]][0]["code"]
        action_buttons = [green_button("Mulai quiz ❯", lambda e, k=l["key"]: on_open_quiz(k))]
        if on_tryit:
            action_buttons.append(
                dark_button("Try it Yourself ❯", lambda e, n=l["name"], c=sample_code: on_tryit(n, c))
            )
        cards.append(
            card(
                col={"xs": 12, "sm": 6, "md": 4},
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Row(
                                    [
                                        ft.Text(l["icon"], size=24),
                                        ft.Text(f"Quiz {l['name']}", size=17, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                                    ],
                                    spacing=10,
                                ),
                                status,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            wrap=True,
                        ),
                        ft.Text(
                            f"{len(quiz_admin.get_questions(l['key']))} soal pilihan ganda. Lulus bila nilai minimal {PASS_PERCENT}%.",
                            size=13,
                            color=ft.colors.ON_SURFACE_VARIANT,
                        ),
                        ft.Container(height=2),
                        ft.Row(action_buttons, wrap=True, spacing=8),
                    ],
                    spacing=10,
                ),
            )
        )
    note = (
        "Login agar skor tersimpan dan Anda bisa mendapatkan sertifikat."
        if not user
        else f"Skor Anda tersimpan otomatis, {user['username']}."
    )
    sim_cards = create_simulator_cards("Python")
    return ft.Column(
        [
            page_banner("Latihan dan Quiz", "Uji pemahaman Anda setelah mempelajari tiap bahasa.", mobile),
            ft.Container(
                padding=pad(mobile),
                content=ft.Column(
                    [
                        ft.Text(note, size=14, color=ft.colors.ON_SURFACE_VARIANT),
                        ft.ResponsiveRow(cards, spacing=16, run_spacing=16),
                        ft.Divider(height=24, color=ft.colors.with_opacity(0.15, ft.colors.OUTLINE)),
                        ft.ResponsiveRow(sim_cards, spacing=16, run_spacing=16),
                    ],
                    spacing=16,
                ),
            ),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )


def get_quiz_view(page: ft.Page, lang: dict, user, mobile: bool, on_back, on_login, on_certificate, on_retry, on_lesson, on_tryit=None):
    key = lang["key"]
    questions = quiz_admin.get_questions(key)
    groups, feedback = [], []
    q_controls = []
    for i, q in enumerate(questions):
        rg = ft.RadioGroup(content=ft.Column([ft.Radio(value=str(j), label=opt) for j, opt in enumerate(q["options"])], spacing=0))
        fb = ft.Text("", size=13)
        groups.append(rg)
        feedback.append(fb)
        q_controls.append(
            card(
                ft.Column(
                    [
                        ft.Text(f"{i + 1}. {q['q']}", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.ON_SURFACE),
                        rg,
                        fb,
                    ],
                    spacing=8,
                )
            )
        )

    result_box = ft.Column(spacing=10)
    submit_btn = green_button("Periksa jawaban", lambda e: submit())

    def submit():
        answers = [int(g.value) if g.value is not None else None for g in groups]
        if None in answers:
            page.show_snack("Jawab semua soal terlebih dahulu.")      # validasi input
            return
        res = quiz_service.grade(key, answers)
        for i, d in enumerate(res["details"]):
            groups[i].disabled = True
            feedback[i].value = ("✓ Benar. " if d["correct"] else "✗ Kurang tepat. ") + d["explain"]
            feedback[i].color = "#1B7F3B" if d["correct"] else "#C62828"
        submit_btn.disabled = True
        color = "#C8E6C9" if res["passed"] else "#FFE0B2"
        verdict = "Selamat, Anda lulus! 🎉" if res["passed"] else f"Belum lulus (minimal {PASS_PERCENT}%). Pelajari lagi lalu coba kembali."
        controls = [
            ft.Container(
                bgcolor=color,
                padding=18,
                border_radius=12,
                content=ft.Column(
                    [
                        ft.Text(
                            f"Nilai: {res['percent']:.0f}%  ({res['correct']} dari {res['total']} benar)",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLACK,
                        ),
                        ft.Text(verdict, size=14, color="#212121"),
                    ],
                    spacing=4,
                ),
            )
        ]
        buttons = [dark_button("Ulangi quiz", lambda e: on_retry(key)), dark_button("Kembali ke pelajaran", lambda e: on_lesson(key))]
        if user:
            ok, msg = quiz_service.save_result(user["username"], key, res)
            controls.append(ft.Text(msg, size=12, color=ft.colors.ON_SURFACE_VARIANT))
            if res["passed"]:
                buttons.insert(0, green_button("Lihat sertifikat ❯", lambda e: on_certificate(key)))
        else:
            controls.append(ft.Text("Login untuk menyimpan skor dan mendapatkan sertifikat.", size=13, color=ft.colors.ON_SURFACE_VARIANT))
            buttons.insert(0, green_button("Login", lambda e: on_login()))
        controls.append(ft.Row(buttons, wrap=True, spacing=8))
        result_box.controls = controls
        page.update()

    top_actions = [ft.TextButton("❮ Semua quiz", on_click=lambda e: on_back())]
    if on_tryit:
        top_actions.append(
            green_button("Try it Yourself ❯", lambda e: on_tryit(lang["name"], LESSONS[key][0]["code"]))
        )

    return ft.Column(
        [
            page_banner(f"Quiz {lang['name']}", f"{len(questions)} soal. Lulus bila nilai minimal {PASS_PERCENT}%.", mobile),
            ft.Container(
                padding=pad(mobile),
                content=ft.Column(
                    [
                        ft.Row(top_actions, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, wrap=True),
                        *q_controls,
                        submit_btn,
                        result_box,
                    ],
                    spacing=14,
                ),
            ),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
