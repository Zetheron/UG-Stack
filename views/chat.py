"""Tampilan Ruang Diskusi (Chat)."""
import flet as ft
from components.ui import GREEN, card, chip, green_button, pad, page_banner, section_heading
from services import chat, roles

def create_chat_view(page: ft.Page, user=None, go=None, mobile: bool = False) -> ft.Control:
    state = {"channel": "umum"}
    msg_col = ft.Column(spacing=8)
    tf = ft.TextField(hint_text="Tulis pesan atau ketik @bot...", expand=True, border_radius=8)

    def render():
        msgs = chat.list_messages(state["channel"])
        msg_col.controls = [
            card(ft.Column([
                ft.Row([
                    ft.Text(f"{m.get('username')}" + (f" ({m.get('npm')})" if m.get('npm') else ""), weight=ft.FontWeight.BOLD, size=13),
                    chip(m.get("role", "mhs").upper(), "#FFD2D7" if m.get("role") == "admin" else "#D9EEE1"),
                    ft.Text(m.get("time", ""), size=11, color=ft.colors.ON_SURFACE_VARIANT),
                ], spacing=6),
                ft.Text(m.get("text", ""), size=13),
            ], spacing=3), padding=10) for m in msgs
        ] or [ft.Text("Belum ada data.", size=13)]
        if getattr(msg_col, "page", None):
            msg_col.update()

    def send(e=None, text=""):
        if not user:
            page.show_snack("Silakan login terlebih dahulu.")
            if go: go("auth")
            return
        val = text or tf.value
        ok, msg = chat.send_message(user, state["channel"], val)
        if ok:
            tf.value = ""
            render()
        else: page.show_snack(msg)

    def set_ch(c):
        state["channel"] = c
        render()

    render()
    return ft.Column([
        page_banner("Ruang Diskusi & Tanya Dosen", "Kanal diskusi mahasiswa, dosen, dan Bot Asisten UG-Stack.", mobile),
        ft.Container(padding=pad(mobile), content=ft.Column([
            ft.Row([
                ft.ElevatedButton("#umum", on_click=lambda e: set_ch("umum")),
                ft.ElevatedButton("#tanya-dosen", on_click=lambda e: set_ch("tanya-dosen")),
                ft.ElevatedButton("#python-web", on_click=lambda e: set_ch("python-web")),
                ft.ElevatedButton("#algoritma", on_click=lambda e: set_ch("algoritma")),
            ], wrap=True, spacing=6),
            card(ft.Column([
                ft.Row([tf, green_button("Kirim", lambda e: send())]),
                ft.Row([
                    ft.TextButton("Tanya Bot: Binary Search", on_click=lambda e: send(text="@bot Jelaskan binary search")),
                    ft.TextButton("Tanya Bot: Merge Sort", on_click=lambda e: send(text="@bot Jelaskan merge sort")),
                ], wrap=True),
            ], spacing=6)),
            section_heading("Pesan Terbaru"),
            msg_col,
        ], spacing=12))
    ], spacing=0)
