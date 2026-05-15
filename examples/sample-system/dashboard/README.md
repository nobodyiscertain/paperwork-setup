# Dashboard

`python render.py` writes `index.html`. Open that file in any modern browser.

The dashboard is a thin presentation layer. It reads what slash commands (`/sod`, `/eod`, `/prep`) wrote to disk and surfaces it in one view. It does not compute anything on its own.

## Layout

- `render.py` — CLI entry. Orchestrates section rendering and HTML composition.
- `_markdown.py` — Tiny stdlib-only markdown → HTML. Doctested.
- `_assets/style.css` — Source CSS. Inlined into `index.html` at gen-time.
- `_assets/app.js` — Source JS. Inlined into `index.html` at gen-time.
- `index.html` — Generated output. Fully self-contained: no external CSS, no external JS, no font CDN, no internet required to open.

## Refresh cycle

The dashboard is a snapshot of what's on disk. Run the commands first, then re-render:

1. Morning: run `/sod`. (This also runs `/prep` for each calendar event.)
2. Evening: run `/eod`.
3. Run `python dashboard/render.py`.
4. Refresh the browser.

The footer shows when the file was generated. If it looks stale, re-run.

## Customization

The default styling is restrained on purpose so your data leads. To change it:
- Edit `_assets/style.css` directly. Re-run `render.py` and refresh.
- Or ask Claude to restyle it. ("Match this screenshot." "Make it more Notion-like." "Restyle in a Verge aesthetic.") Claude edits the real CSS file, not a Python string.

The toggle in the top-right cycles theme: System / Light / Dark. Choice persists in `localStorage`.

## Adding a section

The 3-step recipe — works for adding a Health section, a Weekly section, a Customer Delight section, anything new:

1. **Write a section function** in `render.py`:
   ```python
   def health_section(target):
       text = safe_read(ROOT / "journal" / str(target.year) / f"{target.isoformat()}-health.md")
       if not text:
           return _panel("Team health", _empty("No snapshot yet.", "/health"))
       return _panel("Team health", render_markdown(text))
   ```

2. **Add it to `DAILY_SECTIONS`** (or create a new tab in `TABS`):
   ```python
   DAILY_SECTIONS = [sod_section, schedule_section, prep_cards_section, health_section, eod_section]
   ```

3. **Done.** The existing `_panel` and `_empty` helpers give you the empty state, the header, and styling for free.

Don't compute new things in the renderer. Compute them in a slash command, save the result to a file, then add a section here that reads it. This keeps one source of truth per concept.

## What lives only in the browser

Theme choice (`localStorage.theme`), tab state (URL hash), library card expansion state are **browser-local** and intentionally invisible to Claude. Never store decisions or task state there. If a future feature ties behavior to one of these, move that state to a file in the repo so the agent can read it back.

## Security notes

The generated `index.html` opens via `file://`, which has unusual same-origin semantics in some browsers. The renderer ships with:
- A strict Content-Security-Policy meta tag (no network, no external scripts).
- URL-scheme allowlist on markdown links (`javascript:` / `data:` become `#`).
- Filename and size validation on every file read.

This file contains internal management notes. Don't post it publicly. Treat it as you would any document you authored.

## Sample journal shape

`/sod` writes today's journal under H2 blocks. Roughly:

```markdown
## SOD

Today's focus: ship the GEO rollout doc. Carry-overs from yesterday: review Sara's PR.

## Schedule

- 09:30 — 1:1 with Sara — [link](journal/2026/2026-05-15-prep-sara.md)
- 11:00 — Eng leads sync
- 14:00 — Focus block

## EOD

Shipped GEO doc. Sara's PR reviewed and merged. Tomorrow: write the Q3 brief.
```

The dashboard extracts each H2 block and renders it under the matching section.
