---
status: complete
priority: p2
issue_id: 003
tags: [code-review, security, defense-in-depth]
dependencies: []
---

# NUL-byte hardening in `_safe_href` for defense-in-depth

## Problem Statement

`_safe_href` rejects URLs containing control chars `\x01`–`\x0f` (minus the whitespace ones), but `\x00` is not in the list:

```python
CONTROL_CHARS = "\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f"
```

If a URL containing `\x00` ever reaches `_safe_href`, `urlparse` returns `scheme=""` (which is in `SAFE_SCHEMES`), so the URL is passed through. The crafted input `[x](javascript\x00:alert(1))` would render as a working `javascript:` URL after browser-side URL normalization.

**Current code is NOT exploitable** because every caller of `render_markdown` reads via `safe_read`, which strips NUL bytes (`return text.replace("\x00", "")` at `render.py:46`). But:

- This is a single-point-of-failure: every future caller of `render_markdown` must funnel through `safe_read`, or the guarantee breaks silently.
- Defense-in-depth is the recommended posture for security-sensitive escapers.

## Findings

- Reported by security-sentinel as P1, but on review the existing `safe_read` strip makes it non-exploitable. Demoting to P2 hardening.
- `examples/sample-system/dashboard/_markdown.py:24` defines `CONTROL_CHARS` without `\x00`.
- `examples/sample-system/dashboard/_markdown.py:40-41` is where `_safe_href` checks the URL for control chars.

## Proposed Solutions

**Option A (recommended): Add `\x00` to the control char list and reject any URL with empty scheme that also contains `:`.**

```python
CONTROL_CHARS = "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f"

def _safe_href(url: str) -> str:
    url = url.strip()
    if any(c in url for c in CONTROL_CHARS):
        return "#"
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    # Defense in depth: reject "relative" URLs that look like scheme-with-control-char-bypass
    if not scheme and ":" in url.split("/", 1)[0]:
        return "#"
    return url if scheme in SAFE_SCHEMES else "#"
```

- Pros: closes the latent bypass even if `safe_read` is ever skipped.
- Cons: very minor — adds 3 lines.

**Option B: Document the `safe_read` dependency loudly and add a unit test.**

- Pros: zero behavior change.
- Cons: doesn't prevent the bypass; just makes future contributors more careful.

## Recommended Action

(filled during triage)

## Technical Details

Affected files:
- `examples/sample-system/dashboard/_markdown.py:24, 40-41`
- `PAPERWORK.md` Step 9 `_markdown.py` TEMPLATE block (mirror)

## Acceptance Criteria

- [ ] `render_markdown("[x](javascript\x00:alert(1))")` returns a link with `href="#"`.
- [ ] Existing doctest still passes.
- [ ] PAPERWORK.md template mirrors the fix.
- [ ] Doctest added covering the NUL bypass case.

## Work Log

- 2026-05-15: Identified by security-sentinel during `/workflows:review` of PR #2. Confirmed non-exploitable in current code; promoted to defense-in-depth fix.
- 2026-05-15: Added `\x00` to `CONTROL_CHARS` and added a secondary check rejecting relative URLs containing `:` before any `/` in `examples/sample-system/dashboard/_markdown.py`. Mirrored the change in PAPERWORK.md Step 9 template. Added doctest `_safe_href("javascript" + chr(0) + ":alert(1)")` → `'#'` (used `chr(0)` because doctest's `exec` rejects literal NUL bytes in source). Verified: full doctest suite passes; `dashboard/render.py` runs clean.

## Resources

- PR #2: https://github.com/nobodyiscertain/paperwork-setup/pull/2
