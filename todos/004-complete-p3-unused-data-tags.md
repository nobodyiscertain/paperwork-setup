---
status: complete
priority: p3
issue_id: 004
tags: [code-review, cleanup, yagni]
dependencies: []
---

# Unused `data-tags` attribute on library cards

## Problem Statement

`render.py:210` emits a `data-tags="<comma-separated>"` attribute on every `.library-card` button. `app.js` never reads it. There's no tag filter UI in v1.

The plan called out this attribute as a "v2 hook to leave now" so future client-side filtering wouldn't require re-architecting. Performance-oracle and code-simplicity-reviewer both flagged it as currently dead.

## Findings

- `examples/sample-system/dashboard/render.py:210`
- `PAPERWORK.md` Step 9 render.py TEMPLATE block (mirror)

## Proposed Solutions

**Option A: Drop the attribute.**
- Pros: less dead code; smaller HTML.
- Cons: when v2 adds tag filters, this code needs to come back.

**Option B (recommended): Keep it.**
- Pros: explicit v2 hook documented in the plan; cost is ~30 bytes per card.
- Cons: looks like dead code to a reader of the source.

If keeping: add a one-line comment at the emission site: `# v2 hook: client-side tag filter will read this`.

## Recommended Action

(filled during triage — leaning toward keep + comment.)

## Technical Details

Affected files:
- `examples/sample-system/dashboard/render.py:210`
- `PAPERWORK.md` Step 9 render.py TEMPLATE block

## Acceptance Criteria

- [x] Decision documented (keep + comment OR drop) and applied consistently to example and template.

## Work Log

- 2026-05-15: Flagged by code-simplicity-reviewer and performance-oracle.
- 2026-05-15: Resolved — kept `data-tags` as intentional v2 hook; added explanatory comment above `cards.append` in `examples/sample-system/dashboard/render.py` and mirrored it in the `PAPERWORK.md` TEMPLATE block. Verified `python3 dashboard/render.py` runs clean and generated HTML still contains `data-tags=`.

## Resources

- PR #2: https://github.com/nobodyiscertain/paperwork-setup/pull/2
