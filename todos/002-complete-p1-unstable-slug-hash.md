---
status: complete
priority: p1
issue_id: 002
tags: [code-review, python, bug]
dependencies: []
---

# Unstable per-process slug fallback breaks aria-controls and bookmarks

## Problem Statement

In `library_cards()`, when a library doc's filename stem fails the `SLUG_OK` regex, we fall back to a generated slug:

```python
if not SLUG_OK.match(slug):
    slug = f"doc-{abs(hash(slug)) % (10**8):08d}"
```

Python's built-in `hash()` is salted per-process by `PYTHONHASHSEED` (default: random). The same library file gets a **different slug on every render**. Consequences:

- `<button aria-controls="doc-XXXXXXXX">` and `<section id="doc-XXXXXXXX">` go out of sync if anything ever calls back to a slug from outside the same render — they won't, currently, but any future feature that does (deep links, search index, export) will silently break.
- Any user who bookmarks `#doc-XXXXXXXX` loses that link on the next render.
- Tests that snapshot the generated HTML diff on every run.

The vast majority of library files will have `SLUG_OK`-matching stems (alphanumeric + hyphens). The fallback only fires for filenames like `My Notes.md` or `1on1_template.md`. But when it fires it's silently wrong.

## Findings

- `examples/sample-system/dashboard/render.py:178-179`
- Same code in `PAPERWORK.md` Step 9 TEMPLATE block for `dashboard/render.py`.

Flagged by kieran-python-reviewer and security-sentinel.

## Proposed Solutions

**Option A (recommended): Use `hashlib.sha1` for stable hashing.**

```python
import hashlib
# ...
if not SLUG_OK.match(slug):
    slug = f"doc-{hashlib.sha1(slug.encode('utf-8')).hexdigest()[:8]}"
```

- Pros: deterministic across runs and Python versions. Two lines of change. Cryptographic strength not needed; sha1 short prefix is fine for an ID.
- Cons: very minor — adds `import hashlib` at the top of render.py.

**Option B: Normalize the slug via `re.sub` rather than hashing.**

```python
if not SLUG_OK.match(slug):
    slug = re.sub(r"[^a-z0-9-]+", "-", slug.lower()).strip("-")[:80] or "untitled"
```

- Pros: human-readable slugs. `"My Notes"` → `"my-notes"`.
- Cons: collision risk when two files reduce to the same normalized slug (`"My Notes!"` and `"My Notes?"` both → `"my-notes"`).

## Recommended Action

(filled during triage)

## Technical Details

Affected files:
- `examples/sample-system/dashboard/render.py:178-179`
- `PAPERWORK.md` Step 9 render.py TEMPLATE block (same code)

Imports needed:
- `import hashlib`

## Acceptance Criteria

- [ ] Same library file produces the same slug across two consecutive `python dashboard/render.py` runs.
- [ ] Same slug across two different Python invocations with different `PYTHONHASHSEED` values.
- [ ] Existing doctest in `_markdown.py` still passes.
- [ ] PAPERWORK.md template mirrors the example fix.

## Work Log

- 2026-05-15: Identified by kieran-python-reviewer during `/workflows:review` of PR #2.
- 2026-05-15: Applied Option A. Added `import hashlib` to `examples/sample-system/dashboard/render.py` and replaced the `abs(hash(slug))` fallback with `hashlib.sha1(slug.encode('utf-8')).hexdigest()[:8]`. Mirrored both edits in the `PAPERWORK.md` Step 9 `dashboard/render.py` TEMPLATE block. Verified `python3 dashboard/render.py` runs clean, and that a fixture `library/My_Test.md` produces the identical id `doc-2150bc1d` under `PYTHONHASHSEED=0`, `=42`, and `=12345`. Fixture removed; dashboard re-rendered.

## Resources

- PR #2: https://github.com/nobodyiscertain/paperwork-setup/pull/2
