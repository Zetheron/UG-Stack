import base64
import os

import flet as ft

from components.ui import GREEN
from services import auth

PRESET_AVATARS = [
    ("🐍 Python", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"),
    ("⚛️ React", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg"),
    ("☕ Java", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg"),
    ("🟨 JS", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"),
    ("🌐 HTML", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg"),
    ("🐬 MySQL", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg"),
]


def _render_avatar_preview(username: str, avatar_str: str, size: int = 72) -> ft.Container:
    clean = (avatar_str or "").strip()
    if clean:
        if clean.startswith("data:image/") and "," in clean:
            b64 = clean.split(",", 1)[1]
            inner = ft.Image(src_base64=b64, width=size, height=size, fit=ft.ImageFit.COVER, border_radius=size // 2)
        elif clean.startswith(("http://", "https://")):
            inner = ft.Image(src=clean, width=size, height=size, fit=ft.ImageFit.COVER, border_radius=size // 2)
        else:
            inner = ft.Image(src_base64=clean, width=size, height=size, fit=ft.ImageFit.COVER, border_radius=size // 2)
    else:
        initial = (username or "U")[0].upper()
        inner = ft.Text(initial, size=int(size * 0.42), weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    return ft.Container(
        width=size,
        height=size,
        border_radius=size // 2,
        bgcolor="#1B1730",
        border=ft.border.all(2, "#04AA6D"),
        alignment=ft.alignment.center,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=inner,
    )


def open_change_password(page: ft.Page, user: dict, forced: bool = False, on_done=None):
    """Dialog ganti password. forced=True: tidak bisa ditutup sebelum berhasil (password sementara)."""
    old = ft.TextField(label="Password lama", password=True, can_reveal_password=True, color=ft.colors.ON_SURFACE, autofocus=True)
    new = ft.TextField(label="Password baru (min. 8, huruf + angka)", password=True, can_reveal_password=True, color=ft.colors.ON_SURFACE)
    conf = ft.TextField(label="Ulangi password baru", password=True, can_reveal_password=True, color=ft.colors.ON_SURFACE)
    msg = ft.Text("", size=13, color=ft.colors.RED_700)
    width = max(250, min(380, (page.width or 400) - 70))

    def save(e=None):
        ok, text = auth.change_password(user["username"], old.value, new.value, conf.value)
        if ok:
            user["must_change"] = False
            page.dialog.open = False
            page.show_snack(text)
            if on_done:
                on_done()
            page.update()
        else:
            msg.value = text
            page.update()

    conf.on_submit = save
    note = "Password Anda masih sementara/bawaan. Ganti sekarang untuk melanjutkan." if forced else "Pilih password baru yang kuat."
    actions = [ft.ElevatedButton("Simpan", bgcolor=GREEN, color=ft.colors.WHITE, on_click=save)]
    if not forced:
        actions.insert(0, ft.TextButton("Batal", on_click=lambda e: (setattr(page.dialog, "open", False), page.update())))
    page.dialog = ft.AlertDialog(
        modal=True, title=ft.Text("Ganti Password"),
        content=ft.Container(width=width, content=ft.Column(
            [ft.Text(note, size=13), old, new, conf, msg], tight=True, scroll=ft.ScrollMode.AUTO)),
        actions=actions)
    page.dialog.open = True
    page.update()


def open_change_avatar(page: ft.Page, user: dict, on_done=None):
    """Dialog unggah / ganti foto profil (mendukung FilePicker lokal, URL gambar, dan avatar preset)."""
    current_avatar = user.get("avatar") or auth.get_avatar(user["username"])
    state = {"avatar": current_avatar}

    preview_holder = ft.Container(
        alignment=ft.alignment.center,
        content=_render_avatar_preview(user["username"], state["avatar"], 76),
    )
    url_tf = ft.TextField(
        label="URL Foto (https://...) atau data:image/...",
        value=current_avatar if current_avatar.startswith("http") else "",
        color=ft.colors.ON_SURFACE,
        border_radius=8,
    )
    msg = ft.Text("", size=12, color=ft.colors.RED_700)
    width = max(260, min(420, (page.width or 440) - 60))

    def refresh_preview(new_val: str):
        state["avatar"] = new_val
        preview_holder.content = _render_avatar_preview(user["username"], new_val, 76)
        msg.value = ""
        page.update()

    def on_url_change(e):
        val = (url_tf.value or "").strip()
        if val:
            refresh_preview(val)

    url_tf.on_change = on_url_change

    def on_file_picked(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        f = e.files[0]
        fpath = getattr(f, "path", None)
        if not fpath or not os.path.isfile(fpath):
            msg.value = "Di browser web, silakan tempel URL gambar atau pilih avatar di bawah."
            page.update()
            return
        try:
            if os.path.getsize(fpath) > 1_000_000:
                msg.value = "Ukuran foto terlalu besar (maksimal 1 MB)."
                page.update()
                return
            with open(fpath, "rb") as fh:
                raw = fh.read()
            ext = os.path.splitext(fpath)[1].lower().lstrip(".") or "png"
            mime = "jpeg" if ext == "jpg" else ext
            data_uri = f"data:image/{mime};base64,{base64.b64encode(raw).decode('ascii')}"
            url_tf.value = ""
            refresh_preview(data_uri)
        except OSError:
            msg.value = "Gagal membaca file foto."
            page.update()

    picker = getattr(page, "_ug_avatar_picker", None)
    if picker is None:
        picker = ft.FilePicker(on_result=on_file_picked)
        page._ug_avatar_picker = picker
        if picker not in page.overlay:
            page.overlay.append(picker)
    else:
        picker.on_result = on_file_picked

    def pick_file(e):
        try:
            picker.pick_files(
                allow_multiple=False,
                allowed_extensions=["png", "jpg", "jpeg", "webp", "gif"],
            )
        except Exception:
            msg.value = "Silakan tempel URL gambar atau pilih avatar di bawah."
            page.update()

    preset_btns = [
        ft.OutlinedButton(
            label,
            on_click=lambda e, u=url: (setattr(url_tf, "value", u), refresh_preview(u)),
        )
        for label, url in PRESET_AVATARS
    ]

    def save(e=None):
        candidate = (url_tf.value or "").strip() or state["avatar"]
        ok, text = auth.set_avatar(user["username"], candidate)
        if ok:
            if candidate:
                user["avatar"] = candidate
            else:
                user.pop("avatar", None)
            page.dialog.open = False
            page.show_snack(text)
            if on_done:
                on_done()
            page.update()
        else:
            msg.value = text
            page.update()

    def remove_photo(e):
        ok, text = auth.set_avatar(user["username"], "")
        if ok:
            user.pop("avatar", None)
            page.dialog.open = False
            page.show_snack(text)
            if on_done:
                on_done()
            page.update()
        else:
            msg.value = text
            page.update()

    page.dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Ubah Foto Profil"),
        content=ft.Container(
            width=width,
            content=ft.Column(
                [
                    preview_holder,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "📁 Pilih File Foto",
                                bgcolor="#282A35",
                                color=ft.colors.WHITE,
                                on_click=pick_file,
                            ),
                            ft.OutlinedButton("Hapus Foto", on_click=remove_photo),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        wrap=True,
                        spacing=8,
                    ),
                    url_tf,
                    ft.Text("Atau pilih avatar cepat:", size=12, color=ft.colors.ON_SURFACE_VARIANT),
                    ft.Row(preset_btns, wrap=True, spacing=6, run_spacing=6),
                    msg,
                ],
                tight=True,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            ),
        ),
        actions=[
            ft.TextButton("Batal", on_click=lambda e: (setattr(page.dialog, "open", False), page.update())),
            ft.ElevatedButton("Simpan", bgcolor=GREEN, color=ft.colors.WHITE, on_click=save),
        ],
    )
    page.dialog.open = True
    page.update()
