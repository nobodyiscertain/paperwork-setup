"""Dashboard renderer for Sample Manager's management system.

Reads markdown files that /sod, /eod, and /prep wrote.
Inlines CSS+JS from _assets/ and writes a self-contained index.html.
Stdlib only. Python 3.9+.

Run:  python dashboard/render.py
Open: dashboard/index.html
"""
from __future__ import annotations

import hashlib
import html
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _markdown import render_markdown, split_into_h2_blocks  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = Path(__file__).resolve().parent
ASSETS = DASHBOARD / "_assets"
OUT = DASHBOARD / "index.html"

JOURNAL_HEADINGS = {"sod": "SOD", "schedule": "Schedule", "eod": "EOD"}

FILENAME_OK = re.compile(r"^[A-Za-z0-9._-]+\.md$")
MAX_FILE_BYTES = 1_000_000


def safe_read(path: Path) -> str:
    if not path.exists():
        return ""
    if not FILENAME_OK.match(path.name):
        print(f"skip (bad filename): {path.name}", file=sys.stderr)
        return ""
    if path.stat().st_size > MAX_FILE_BYTES:
        print(f"skip (too large): {path.name}", file=sys.stderr)
        return ""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"skip (not utf-8): {path.name}", file=sys.stderr)
        return ""
    return text.replace("\x00", "")


def journal_path(target: date) -> Path:
    return ROOT / "journal" / str(target.year) / f"{target.isoformat()}.md"


def prep_card_paths(target: date) -> list[Path]:
    year_dir = ROOT / "journal" / str(target.year)
    if not year_dir.exists():
        return []
    return sorted(year_dir.glob(f"{target.isoformat()}-prep-*.md"))


def _panel(title: str, body: str, meta: str = "") -> str:
    meta_html = f'<span class="panel-meta">{html.escape(meta)}</span>' if meta else ""
    return (
        f'<section class="panel">'
        f'<div class="panel-head"><h2>{html.escape(title)}</h2>{meta_html}</div>'
        f'<div class="panel-body">{body}</div>'
        f'</section>'
    )


def _empty(title: str, command: str) -> str:
    return (
        f'<div class="empty">'
        f'<span class="empty-glyph" aria-hidden="true">&#9676;</span>'
        f'<p class="empty-title">{html.escape(title)}</p>'
        f'<p class="empty-hint">Run <code class="cmd">{html.escape(command)}</code> in your terminal, '
        f'then re-run <code>python dashboard/render.py</code>.</p>'
        f'</div>'
    )


def sod_section(target: date) -> str:
    text = safe_read(journal_path(target))
    blocks = split_into_h2_blocks(text)
    body = blocks.get(JOURNAL_HEADINGS["sod"], "").strip()
    if not body:
        return _panel("Start of day", _empty("Nothing here yet.", "/sod"))
    return _panel("Start of day", render_markdown(body))


def schedule_section(target: date) -> str:
    text = safe_read(journal_path(target))
    blocks = split_into_h2_blocks(text)
    body = blocks.get(JOURNAL_HEADINGS["schedule"], "").strip()
    if not body:
        sod = blocks.get(JOURNAL_HEADINGS["sod"], "").strip()
        if sod:
            return _panel("Schedule", '<p class="hint">Schedule lives inside today\'s start-of-day briefing.</p>')
        return _panel("Schedule", _empty("No schedule captured yet.", "/sod"))
    count = sum(1 for ln in body.splitlines() if ln.strip().startswith("-"))
    meta = f"{count} {'event' if count == 1 else 'events'}" if count else ""
    return _panel("Schedule", render_markdown(body), meta=meta)


def prep_cards_section(target: date) -> str:
    cards = prep_card_paths(target)
    if not cards:
        return _panel("Meeting prep", _empty("No prep cards for today.", "/sod"))
    parts = []
    today_prefix = f"{target.isoformat()}-prep-"
    for card in cards:
        slug = card.stem.removeprefix(today_prefix) if card.stem.startswith(today_prefix) else card.stem
        body = safe_read(card)
        parts.append(
            f'<details>'
            f'<summary><span class="prep-slug">{html.escape(slug)}</span></summary>'
            f'<div class="prep-body">{render_markdown(body)}</div>'
            f'</details>'
        )
    meta = f"{len(cards)} {'card' if len(cards) == 1 else 'cards'}"
    return _panel("Meeting prep", "".join(parts), meta=meta)


def eod_section(target: date) -> str:
    text = safe_read(journal_path(target))
    blocks = split_into_h2_blocks(text)
    body = blocks.get(JOURNAL_HEADINGS["eod"], "").strip()
    if not body:
        return _panel("End of day", _empty("Not captured yet.", "/eod"))
    return _panel("End of day", f'<details open><summary>Day\'s recap</summary><div>{render_markdown(body)}</div></details>')


FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
KV_RE = re.compile(r"^([a-zA-Z_][\w-]{0,40}):\s*(.{0,500})$")
SLUG_OK = re.compile(r"^[a-z0-9-]{1,80}$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines()[:50]:
        kv = KV_RE.match(line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return meta, text[m.end():]


def humanize(stem: str) -> str:
    return stem.replace("-", " ").replace("_", " ").strip().capitalize()


def first_paragraph(body: str, limit: int = 140) -> str:
    for para in body.split("\n\n"):
        clean = para.strip()
        if clean and not clean.startswith("#"):
            return clean[:limit] + ("..." if len(clean) > limit else "")
    return ""


def library_cards() -> list[dict]:
    lib = ROOT / "library"
    if not lib.exists():
        return []
    docs: list[dict] = []
    for path in sorted(lib.rglob("*.md")):
        if not FILENAME_OK.match(path.name):
            print(f"skip library (bad filename): {path.name}", file=sys.stderr)
            continue
        try:
            path.resolve().relative_to(lib.resolve())
        except ValueError:
            print(f"skip library (path escape): {path.name}", file=sys.stderr)
            continue
        raw = safe_read(path)
        meta, body = parse_frontmatter(raw)
        slug = path.stem
        if not SLUG_OK.match(slug):
            slug = f"doc-{hashlib.sha1(slug.encode('utf-8')).hexdigest()[:8]}"
        title = meta.get("title") or humanize(path.stem)
        summary = meta.get("summary") or first_paragraph(body)
        captured = meta.get("captured") or datetime.fromtimestamp(path.stat().st_mtime).date().isoformat()
        tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
        docs.append({
            "slug": slug,
            "title": title,
            "summary": summary,
            "captured": captured,
            "tags": tags,
            "body_html": render_markdown(body),
        })
    docs.sort(key=lambda d: d["title"].lower())
    return docs


def render_library_panel() -> str:
    docs = library_cards()
    if not docs:
        return _panel("Library", _empty("Empty library.", "drop a markdown file in library/"))
    cards = []
    bodies = []
    for d in docs:
        tag_html = "".join(
            f'<span class="tag">{html.escape(t)}</span>' for t in d["tags"][:4]
        )
        # data-tags is a v2 hook: enables client-side tag filtering without re-architecting
        cards.append(
            f'<button class="library-card" type="button" '
            f'aria-expanded="false" aria-controls="doc-{html.escape(d["slug"], quote=True)}" '
            f'data-doc-slug="{html.escape(d["slug"], quote=True)}" '
            f'data-tags="{html.escape(",".join(d["tags"]), quote=True)}">'
            f'<h3>{html.escape(d["title"])}</h3>'
            f'<p class="card-summary">{html.escape(d["summary"])}</p>'
            f'<div class="card-meta"><time>{html.escape(d["captured"])}</time>{tag_html}</div>'
            f'</button>'
        )
        bodies.append(
            f'<section class="doc-body" id="doc-{html.escape(d["slug"], quote=True)}" hidden>'
            f'<button class="doc-close" type="button">Close</button>'
            f'<article>{d["body_html"]}</article>'
            f'</section>'
        )
    return (
        f'<header class="hero hero-library">'
        f'<p class="eyebrow">LIBRARY &middot; {len(docs)} {"DOC" if len(docs) == 1 else "DOCS"}</p>'
        f'<h1>Reference shelf</h1>'
        f'</header>'
        f'<div class="library-grid">{"".join(cards)}</div>'
        f'{"".join(bodies)}'
    )


DAILY_SECTIONS = [
    sod_section,
    schedule_section,
    prep_cards_section,
    eod_section,
]

TABS = [
    {"id": "daily", "label": "Daily"},
    {"id": "library", "label": "Library"},
]


CSP = (
    "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; "
    "img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'"
)


def render_hero(target: date) -> str:
    eyebrow = "TODAY &middot; " + target.strftime("%A, %B %-d").upper()
    headline = "Your day at a glance"
    return (
        f'<header class="hero">'
        f'<p class="eyebrow">{eyebrow}</p>'
        f'<h1>{headline}</h1>'
        f'</header>'
    )


def render_tabs() -> str:
    if len(TABS) == 1:
        return ""
    items = []
    for i, tab in enumerate(TABS):
        selected = "true" if i == 0 else "false"
        tabindex = "0" if i == 0 else "-1"
        items.append(
            f'<button role="tab" id="tab-{tab["id"]}" '
            f'aria-controls="panel-{tab["id"]}" aria-selected="{selected}" '
            f'tabindex="{tabindex}">{html.escape(tab["label"])}</button>'
        )
    return f'<div role="tablist" aria-label="Sections">{"".join(items)}</div>'


def render_daily_panel(target: date) -> str:
    sections = "".join(fn(target) for fn in DAILY_SECTIONS)
    hidden = "" if TABS[0]["id"] == "daily" else " hidden"
    return (
        f'<section role="tabpanel" id="panel-daily" aria-labelledby="tab-daily" tabindex="0"{hidden}>'
        f'{render_hero(target)}'
        f'{sections}'
        f'</section>'
    )


def render_library_tabpanel() -> str:
    return (
        f'<section role="tabpanel" id="panel-library" aria-labelledby="tab-library" tabindex="0" hidden>'
        f'{render_library_panel()}'
        f'</section>'
    )


def render_theme_toggle() -> str:
    return (
        '<fieldset class="theme-toggle" role="radiogroup" aria-label="Color theme">'
        '<button role="radio" aria-checked="true"  data-theme-choice="system">System</button>'
        '<button role="radio" aria-checked="false" data-theme-choice="light">Light</button>'
        '<button role="radio" aria-checked="false" data-theme-choice="dark">Dark</button>'
        '</fieldset>'
    )


PRE_PAINT_SCRIPT = """(function(){
  var stored = localStorage.getItem('theme');
  if (stored === 'light' || stored === 'dark') {
    document.documentElement.dataset.theme = stored;
  }
  document.documentElement.style.colorScheme =
    stored || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
})();"""


def render_page(target: date) -> str:
    css = (ASSETS / "style.css").read_text(encoding="utf-8")
    js = (ASSETS / "app.js").read_text(encoding="utf-8")
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    favicon = (
        "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
        "<rect width='32' height='32' rx='6' fill='%231f3a5f'/>"
        "<rect x='8' y='10' width='16' height='2' fill='%23fbfaf7'/>"
        "<rect x='8' y='15' width='16' height='2' fill='%23fbfaf7'/>"
        "<rect x='8' y='20' width='10' height='2' fill='%23fbfaf7'/>"
        "</svg>"
    )

    library_panel_html = render_library_tabpanel() if any(t["id"] == "library" for t in TABS) else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<title>Paperwork &mdash; {target.strftime('%B %-d')}</title>
<link rel="icon" type="image/svg+xml" href="{favicon}">
<script>{PRE_PAINT_SCRIPT}</script>
<style>{css}</style>
</head>
<body>
<div class="wrap">
  <header class="top-bar">
    <div class="brand">Paperwork</div>
    {render_theme_toggle()}
  </header>
  {render_tabs()}
  {render_daily_panel(target)}
  {library_panel_html}
  <footer class="footer">
    <small>Generated <time>{generated}</time> &middot; Contains internal management notes &mdash; handle accordingly.</small>
  </footer>
</div>
<script>{js}</script>
</body>
</html>
"""


def main() -> int:
    target = date.today()
    OUT.write_text(render_page(target), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
