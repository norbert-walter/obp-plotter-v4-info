#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mt_po.py — MT für Sphinx-.po mit Google Translate (API-Key, v2) + reST-Masking.

Env:
  GOOGLE_API_KEY        # dein API-Key (v2)
  TARGET_LANG=de|en|... # Zielsprache (default: de)
  REWRITE_FUZZY=true    # geänderte Einträge neu befüllen (default: true)
  REWRITE_FILLED=false  # geprüfte, gefüllte Einträge überschreiben (default: false)
  DNT=Foo,Bar           # Optional: "Do Not Translate"-Liste (Komma-getrennt)
Usage:
  python scripts/mt_po.py [po_dir]  # default: locale/<TARGET_LANG>/LC_MESSAGES
"""
import os, sys, re, html, requests
import polib
from typing import Dict, List, Tuple

TARGET_LANG     = os.getenv("TARGET_LANG", "de").strip()
REWRITE_FUZZY   = os.getenv("REWRITE_FUZZY", "true").lower() == "true"
REWRITE_FILLED  = os.getenv("REWRITE_FILLED", "false").lower() == "true"
DNT_LIST        = [s.strip() for s in os.getenv("DNT", "").split(",") if s.strip()]

# --- Google v2 via API key ----------------------------------------------------
def google_translate(text: str, target: str) -> str:
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_API_KEY missing")
    url = "https://translation.googleapis.com/language/translate/v2"
    # v2 akzeptiert Arrays (batch) bis 128 Elemente – hier 1:1 für Einfachheit. :contentReference[oaicite:2]{index=2}
    r = requests.post(url, params={"key": key}, json={"q": text, "target": target, "format": "text"}, timeout=30)
    r.raise_for_status()
    data = r.json()
    out = data["data"]["translations"][0]["translatedText"]
    return html.unescape(out)  # API liefert teils HTML-Entities

# --- Masking: reST-Markup & Platzhalter schützen -----------------------------
MASK_PATTERNS: List[re.Pattern] = [
    re.compile(r"``[^`]+``"),                # inline code
    re.compile(r":[\w.-]+:`[^`]+`"),         # :role:`...`
    re.compile(r"`[^`]+`_"),                 # `text`_
    re.compile(r"\*\*[^*\n]+\*\*"),          # **bold**
    re.compile(r"\*[^*\s][^*\n]*\*"),        # *italic*
    re.compile(r"\|[^|\n]+\|"),              # |subst|
    # Platzhalter:
    re.compile(r"%\([^)]+\)[#0\- +]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[hlL]?[diouxXeEfFgGcrs%]"),
    re.compile(r"%(?:\d+\$)?[diouxXeEfFgGcrs%]"),
    re.compile(r"\{[^\{\}\n]+\}"),
]

def build_dnt_patterns(lst: List[str]) -> List[re.Pattern]:
    return [re.compile(re.escape(p)) for p in lst]

DNT_PATTERNS = build_dnt_patterns(DNT_LIST)

def mask_text(s: str) -> Tuple[str, Dict[str, str]]:
    table: Dict[str, str] = {}; i = 0
    def sub_all(pats, txt):
        nonlocal i
        for pat in pats:
            def repl(m):
                nonlocal i
                k = f"[[[[M{i}]]]]"; table[k] = m.group(0); i += 1; return k
            txt = pat.sub(repl, txt)
        return txt
    s = sub_all(MASK_PATTERNS, s)
    if DNT_PATTERNS: s = sub_all(DNT_PATTERNS, s)
    return s, table

def unmask_text(s: str, table: Dict[str, str]) -> str:
    for k, v in table.items():
        s = s.replace(k, v)
    return s

def translate_preserving_markup(text: str) -> str:
    masked, table = mask_text(text)
    out = google_translate(masked, TARGET_LANG.lower())
    return unmask_text(out, table)

# --- Helpers ------------------------------------------------------------------
def need_nplurals(po: polib.POFile) -> int:
    m = re.search(r"nplurals\s*=\s*(\d+)", po.metadata.get("Plural-Forms", "") or "")
    return int(m.group(1)) if m else 2

def should_translate_entry(e: polib.POEntry) -> bool:
    if not e.msgid.strip():
        return False
    has_translation = bool(e.msgstr.strip()) if not e.msgid_plural else any((v or "").strip() for v in e.msgstr_plural.values())
    is_fuzzy = "fuzzy" in (e.flags or [])
    if not has_translation: return True
    if is_fuzzy and REWRITE_FUZZY: return True
    if REWRITE_FILLED: return True
    return False

def process_plural(e: polib.POEntry, nplurals: int) -> bool:
    changed = False
    for i in range(nplurals):
        current = e.msgstr_plural.get(i, "")
        if current.strip() and not REWRITE_FILLED and not ("fuzzy" in e.flags and REWRITE_FUZZY):
            continue
        src = e.msgid if i == 0 else (e.msgid_plural or e.msgid)
        translated = translate_preserving_markup(src)
        if e.msgstr_plural.get(i, "") != translated:
            e.msgstr_plural[i] = translated; changed = True
    if "fuzzy" not in e.flags: e.flags.append("fuzzy"); changed = True or changed
    return changed

def process_po_file(path: str) -> bool:
    po = polib.pofile(path)
    npl = need_nplurals(po)
    changed_any = False
    for e in po:
        if not should_translate_entry(e):
            continue
        if e.msgid_plural:
            if process_plural(e, npl): changed_any = True
            continue
        new_txt = translate_preserving_markup(e.msgid)
        if e.msgstr != new_txt:
            e.msgstr = new_txt; changed_any = True
        if "fuzzy" not in e.flags:
            e.flags.append("fuzzy"); changed_any = True
    if changed_any:
        po.save(path); print(f"Updated {path}")
    return changed_any

def default_po_dir() -> str:
    return os.path.join("locale", TARGET_LANG.lower(), "LC_MESSAGES")

if __name__ == "__main__":
    po_dir = sys.argv[1] if len(sys.argv) > 1 else default_po_dir()
    if not os.path.isdir(po_dir):
        sys.stderr.write(f"PO directory not found: {po_dir}\n"); sys.exit(2)
    print(f"Google v2 MT for {TARGET_LANG} in {po_dir} (REWRITE_FUZZY={REWRITE_FUZZY}, REWRITE_FILLED={REWRITE_FILLED})")
    for root, _, files in os.walk(po_dir):
        for fn in files:
            if fn.endswith(".po"):
                process_po_file(os.path.join(root, fn))
