---
status: complete
priority: p1
issue_id: 001
tags: [code-review, architecture, parity]
dependencies: []
---

# PAPERWORK.md TEMPLATE blocks drifted from committed example files

## Problem Statement

`PAPERWORK.md` Step 9 contains five TEMPLATE blocks (`dashboard/render.py`, `dashboard/_markdown.py`, `dashboard/_assets/style.css`, `dashboard/_assets/app.js`, `dashboard/README.md`) that ARE the actual code generated for new Paperwork users. The committed files at `examples/sample-system/dashboard/*` are supposed to be byte-identical (modulo Mustache conditionals like `{{#if has_library}}`).

They aren't. Two reviewers (security-sentinel + pattern-recognition-specialist) confirmed material drift.

Future generated systems will get either the audited code (examples/) or the unaudited code (PAPERWORK.md template) depending on which copy is the source. That breaks the security and architecture guarantees the plan made.

## Findings

From pattern-recognition-specialist:

1. **`_markdown.py` `_block_render` was simplified in the example but not the template.**
   - Example dropped the `close_to()` helper (template lines 1244-1248 in PAPERWORK.md).
   - Example's `close_all()` emits `</{tag.split('-')[0]}>` directly; the template still pushes `"ul-nested"` to the stack, pops as `</ul-nested>`, and relies on a final `.replace("ul-nested", "ul").replace("ol-nested", "ol")` pass.
   - Both produce equivalent HTML but the example's is cleaner.

2. **`split_into_h2_blocks` doctest restructured.**
   - Template (PAPERWORK.md line ~1370): single line doctest `>>> split_into_h2_blocks("...")`.
   - Example: multi-step doctest assigning to `r` and querying `r['A']`, `r['B']` — needed because the original failed under doctest's strict dict-ordering compare.

3. **`render.py` lost several inline comments in the example.**
   - `# regex-DoS defense`, `# Reject NUL bytes — they're our placeholder sentinel.`, `# Single source of truth for journal H2 heading names.`, `# Fallback for journals written before the /sod template change.`, `# Count bullets for a small meta affordance.`, `# Path safety: must stay under library/.`, `# Inlined synchronously in <head> BEFORE the stylesheet to prevent FOUC.`

4. **`style.css` `.panel-body h4` is one line in the template, expanded to multiple lines in the example.**

5. **`app.js` lost 4 inline comments in the example.**
   - `// Initial tab from hash or default to first.`
   - `// Initialize toggle state from current storage.`
   - `// React live to OS theme changes when System is active.`
   - `// Close any other open docs.`

Items already CONSISTENT (no action): the `&middot;` uppercase fix, the `_safe_href` doctest, the README boundary documentation.

## Proposed Solutions

**Option A: Regenerate `examples/` from PAPERWORK.md template.**
- Lose the `_block_render` simplification, restore the post-replace.
- Lose the restructured doctests.
- Pros: minimal PAPERWORK.md churn.
- Cons: loses real code improvements the example accumulated during testing.

**Option B (recommended): Update PAPERWORK.md template to absorb example's improvements.**
- Bring the cleaner `_block_render` into the template.
- Restructure the `split_into_h2_blocks` doctest the same way.
- Restore the dropped inline comments in render.py / app.js where they add reader value.
- Reformat `.panel-body h4`.
- Pros: ships better code; reflects what actually works after browser testing.
- Cons: bigger PAPERWORK.md diff.

**Option C: Add a CI/pre-commit check that diffs the template blocks against the example files.**
- Pros: catches drift forever.
- Cons: harder to write correctly (template has Mustache, example doesn't).

## Recommended Action

(filled during triage)

## Technical Details

Affected files:
- `PAPERWORK.md` (lines ~759 through ~2030 — the five TEMPLATE blocks under Step 9)
- `examples/sample-system/dashboard/render.py`
- `examples/sample-system/dashboard/_markdown.py`
- `examples/sample-system/dashboard/_assets/style.css`
- `examples/sample-system/dashboard/_assets/app.js`
- `examples/sample-system/dashboard/README.md`

## Acceptance Criteria

- [x] Stripping Mustache conditionals from each PAPERWORK.md TEMPLATE block produces output byte-identical to the corresponding `examples/sample-system/dashboard/*` file.
- [x] `examples/sample-system/dashboard/_markdown.py` still passes its doctests.
- [x] `examples/sample-system/dashboard/dashboard/render.py` still produces a working index.html with all three views (light, dark, library).

## Work Log

- 2026-05-15: Identified by security-sentinel + pattern-recognition-specialist during `/workflows:review` of PR #2.
- 2026-05-15: Reconciled all five `TEMPLATE: dashboard/...` blocks in `PAPERWORK.md` Step 9 with the committed example files at `examples/sample-system/dashboard/`. Chose Option B: the template absorbed the example's improvements (the example was browser-tested and is the source of truth). Concretely:
  - `render.py` template: dropped seven inline comments and three section banner blocks (`# File helpers`, `# Section renderers`, `# Library`, `# Tab + section registry`, `# Page composition`) and the `safe_read` docstring — none of these existed in the example. Removed the stale "`_markdown` lives next to this file..." comment block above the `sys.path.insert`. Fixed the `DAILY_SECTIONS` Mustache so a `has_daily_bookends=true` render produces no trailing blank line before `]`.
  - `_markdown.py` template: replaced the Unicode arrow (`→`) in the module docstring with ASCII `->`. Refactored `_block_render` to match the example: dropped the unused `close_to` helper, simplified `close_all` to emit `</{tag.split('-')[0]}>` directly, and dropped the post-process `.replace("ul-nested", "ul").replace("ol-nested", "ol")` and all section-marker comments inside the function. Restructured the `split_into_h2_blocks` doctest to multi-step (assigns to `r` and queries `r['A']` / `r['B']`) so it doesn't depend on dict-repr ordering, and dropped the `# Restore fenced code placeholders...` inline comment plus extracted `inner = re.sub(...)` to match the example.
  - `style.css` template: expanded `.panel-body h4` from one line to the multi-line form used in the example.
  - `app.js` template: dropped the four inline comments (`// Initial tab from hash or default to first.`, `// Initialize toggle state from current storage.`, `// React live to OS theme changes when System is active.`, `// Close any other open docs.`) — none exist in the example.
  - `README.md` template: already matched (Mustache for `has_daily_bookends` and `has_library` only).
- 2026-05-15: Verified. (1) `python3 -m doctest dashboard/_markdown.py` passes silently. (2) `python3 dashboard/render.py` writes `dashboard/index.html` cleanly. (3) Stripping Mustache conditionals from each TEMPLATE block (with `has_library=true`, `has_daily_bookends=true`, `manager_first_name="Sample Manager"`) produces output byte-identical to the corresponding `examples/sample-system/dashboard/*` file for all five files. Acceptance criteria met.

## Resources

- PR #2: https://github.com/nobodyiscertain/paperwork-setup/pull/2
- Plan: docs/plans/2026-05-15-feat-lightweight-dashboard-plan.md
