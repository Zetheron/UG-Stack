"""Pencarian di dalam materi bawaan (bahasa, pelajaran, cheat sheet) mendukung Bahasa Indonesia & Inggris."""
from content import i18n_content_en as C
from content.languages import LANGS
from content.lessons import LESSONS
from content.reference import REFERENCE


def search_content(query: str) -> dict:
    q = (query or "").strip().lower()
    result = {"languages": [], "lessons": [], "reference": []}
    if len(q) < 2:
        return result
    for lang in LANGS:
        tag_en = C.TAGLINE_EN.get(lang["key"], "").lower()
        if q in lang["name"].lower() or q in lang["tagline"].lower() or q in tag_en:
            result["languages"].append(lang)
    for key, lessons in LESSONS.items():
        en_lessons = C.LESSONS_EN.get(key, [])
        for i, lesson in enumerate(lessons):
            t_en, b_en = en_lessons[i] if i < len(en_lessons) else ("", "")
            haystack = f"{lesson['title']} {lesson['body']} {lesson['code']} {t_en} {b_en}".lower()
            if q in haystack:
                result["lessons"].append({
                    "lang": key,
                    "index": i,
                    "title": lesson["title"],
                    "snippet": lesson["body"].split("\n\n")[0].strip(),
                })
    for key, items in REFERENCE.items():
        en_refs = C.REF_EN.get(key, [])
        for i, (syntax, desc) in enumerate(items):
            d_en = en_refs[i].lower() if i < len(en_refs) else ""
            if q in syntax.lower() or q in desc.lower() or q in d_en:
                result["reference"].append({"lang": key, "syntax": syntax, "desc": desc})
    return result
