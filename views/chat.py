"""Tampilan Ruang Diskusi (Chat) Mahasiswa, Dosen, Admin & Bot Asisten UG-Stack."""
import flet as ft
from components.dashboard_theme import user_avatar_badge
from components.i18n_ui import translate_tree
from components.ui import GREEN, card, chip, green_button, pad, page_banner, section_heading
from services import auth, chat


def create_chat_view(page: ft.Page, go=None, mobile: bool = False, user=None, *args, **kwargs) -> ft.Control:
    if isinstance(go, bool):
        mobile = go
        go = args[0] if args and callable(args[0]) else kwargs.get("go")
    active_user = user if user is not None else getattr(page, "_ug_user", None)
    state = {"channel": "umum"}
    msg_col = ft.Column(spacing=8)
    tf = ft.TextField(hint_text="Tulis pesan atau ketik @bot...", expand=True, border_radius=8)
    ch_buttons_row = ft.Row(wrap=True, spacing=6)

    def render(do_update=False):
        ui_lang = getattr(page, "_ug_lang", "id")
        msgs = chat.list_messages(state["channel"])
        msg_col.controls = [
            card(ft.Column([
                ft.Row([
                    user_avatar_badge(m.get("username", ""), auth.get_avatar(m.get("username", "")), size=26),
                    ft.Text(f"{m.get('username')}" + (f" ({m.get('npm')})" if m.get('npm') else ""), weight=ft.FontWeight.BOLD, size=13),
                    chip(m.get("role", "mahasiswa").upper(), "#FFD2D7" if m.get("role") == "admin" else "#D9EEE1"),
                    ft.Text(m.get("time", ""), size=11, color=ft.colors.ON_SURFACE_VARIANT),
                ], spacing=6, wrap=True, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Text(m.get("text", ""), size=13, selectable=True),
            ], spacing=4), padding=12) for m in msgs
        ] or [ft.Text("Belum ada data.", size=13)]
        translate_tree(msg_col, ui_lang)
        for btn in ch_buttons_row.controls:
            active = btn.data == state["channel"]
            btn.bgcolor = GREEN if active else None
            btn.color = ft.colors.WHITE if active else None
        if do_update and page:
            page.update()

    def send(e=None, text=""):
        u = active_user or getattr(page, "_ug_user", None)
        if not u:
            page.show_snack("Silakan login terlebih dahulu.")
            if callable(go):
                try:
                    go("auth")
                except TypeError:
                    pass
            return
        val = text or tf.value
        ok, msg = chat.send_message(u, state["channel"], val)
        if ok:
            tf.value = ""
            render(do_update=True)
        else:
            page.show_snack(msg)

    tf.on_submit = send

    def set_ch(c):
        state["channel"] = c
        render(do_update=True)

    ch_buttons_row.controls = [
        ft.ElevatedButton("#umum", data="umum", bgcolor=GREEN, color=ft.colors.WHITE, on_click=lambda e: set_ch("umum")),
        ft.ElevatedButton("#tanya-dosen", data="tanya-dosen", on_click=lambda e: set_ch("tanya-dosen")),
        ft.ElevatedButton("#python-web", data="python-web", on_click=lambda e: set_ch("python-web")),
        ft.ElevatedButton("#algoritma", data="algoritma", on_click=lambda e: set_ch("algoritma")),
    ]

    render()
    return ft.Column([
        page_banner("Ruang Diskusi & Tanya Dosen", "Kanal diskusi mahasiswa, dosen, dan Bot Asisten UG-Stack.", mobile),
        ft.Container(padding=pad(mobile), content=ft.Column([
            ch_buttons_row,
            card(ft.Column([
                ft.Row([tf, green_button("Kirim", lambda e: send())]),
                ft.Row([
                    ft.TextButton("Tanya Bot: Pencarian Biner", on_click=lambda e: send(text="@bot Jelaskan binary search")),
                    ft.TextButton("Tanya Bot: Pengurutan Gabung", on_click=lambda e: send(text="@bot Jelaskan merge sort")),
                ], wrap=True),
            ], spacing=6)),
            section_heading("Pesan Terbaru"),
            msg_col,
        ], spacing=12))
    ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)


get_chat_view = create_chat_view
