"""Tiny markdown -> HTML for the dashboard. Stdlib only.

Supports: ATX headings (H1-H4), paragraphs, bulleted/numbered lists (one
level of nesting), bold, italic, inline code, fenced code blocks,
blockquotes, links, horizontal rules. Unknown markdown degrades to literal
escaped text.

Security invariants:
1. Escape BEFORE applying markdown rules.
2. Fenced code blocks extracted to \\x00FENCED{i}\\x00 placeholders first.
3. Link URLs pass through a scheme allowlist.

Run tests with:  python -m doctest dashboard/_markdown.py -v
"""
from __future__ import annotations

import html
import re
from urllib.parse import urlparse

SAFE_SCHEMES = {"http", "https", "mailto", ""}
FENCE_RE = re.compile(r"```(?P<info>[\w-]{0,30})?\n(?P<body>.*?)\n```", re.DOTALL)
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
CONTROL_CHARS = "\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f"


def _safe_href(url: str) -> str:
    """Allowlist URL schemes. Return '#' for unsafe URLs.

    >>> _safe_href("https://example.com")
    'https://example.com'
    >>> _safe_href("javascript:alert(1)")
    '#'
    >>> _safe_href("data:text/html,<script>alert(1)</script>")
    '#'
    >>> _safe_href("/relative/path")
    '/relative/path'
    """
    url = url.strip()
    if any(c in url for c in CONTROL_CHARS):
        return "#"
    scheme = urlparse(url).scheme.lower()
    return url if scheme in SAFE_SCHEMES else "#"


def _mask_fenced(text: str) -> tuple[str, list[str]]:
    """Replace fenced code blocks with placeholders. Returns (masked, blocks)."""
    blocks: list[str] = []
    def stash(m: "re.Match[str]") -> str:
        info = (m.group("info") or "").strip()
        info = info if re.match(r"^[A-Za-z0-9_-]{0,30}$", info) else ""
        body = html.escape(m.group("body"), quote=False)
        cls = f' class="lang-{info}"' if info else ""
        blocks.append(f"<pre><code{cls}>{body}</code></pre>")
        return f"\x00FENCED{len(blocks) - 1}\x00"
    return FENCE_RE.sub(stash, text), blocks


def _inline(line: str) -> str:
    """Apply inline markdown rules to an already-escaped line."""
    line = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", line)
    line = re.sub(r"\*\*([^*\n]+)\*\*", r"<strong>\1</strong>", line)
    line = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", line)
    line = re.sub(
        r"\[([^\]\n]{1,200})\]\(([^)\n\s]{1,500})\)",
        lambda m: f'<a href="{html.escape(_safe_href(m.group(2)), quote=True)}">{m.group(1)}</a>',
        line,
    )
    return line


def _block_render(text: str) -> str:
    """Block-level state machine. Handles headings, lists (1-level nesting),
    blockquotes, horizontal rules, and paragraphs."""
    out: list[str] = []
    stack: list[str] = []

    def close_all() -> None:
        while stack:
            tag = stack.pop()
            out.append(f"</{tag.split('-')[0]}>")

    lines = text.split("\n")
    for raw_line in lines:
        line = raw_line.rstrip()

        if not line.strip():
            close_all()
            continue

        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if m:
            close_all()
            level = len(m.group(1))
            out.append(f"<h{level}>{_inline(m.group(2))}</h{level}>")
            continue

        if re.match(r"^[-*_]{3,}$", line.strip()):
            close_all()
            out.append("<hr>")
            continue

        if line.lstrip().startswith(">"):
            if not stack or stack[-1] != "blockquote":
                close_all()
                out.append("<blockquote>")
                stack.append("blockquote")
            body = line.lstrip()[1:].lstrip()
            out.append(f"<p>{_inline(body)}</p>")
            continue

        ul_match = re.match(r"^(\s{0,4})[-*+]\s+(.+)$", line)
        if ul_match:
            indent = len(ul_match.group(1))
            if indent >= 2:
                if not stack or stack[-1] != "ul-nested":
                    out.append("<ul>")
                    stack.append("ul-nested")
            else:
                while stack and stack[-1] == "ul-nested":
                    out.append("</ul>")
                    stack.pop()
                if not stack or stack[-1] != "ul":
                    close_all()
                    out.append("<ul>")
                    stack.append("ul")
            out.append(f"<li>{_inline(ul_match.group(2))}</li>")
            continue

        ol_match = re.match(r"^(\s{0,4})\d+\.\s+(.+)$", line)
        if ol_match:
            indent = len(ol_match.group(1))
            if indent >= 2:
                if not stack or stack[-1] != "ol-nested":
                    out.append("<ol>")
                    stack.append("ol-nested")
            else:
                while stack and stack[-1] == "ol-nested":
                    out.append("</ol>")
                    stack.pop()
                if not stack or stack[-1] != "ol":
                    close_all()
                    out.append("<ol>")
                    stack.append("ol")
            out.append(f"<li>{_inline(ol_match.group(2))}</li>")
            continue

        if not stack or stack[-1] != "p":
            close_all()
            out.append("<p>")
            stack.append("p")
            out.append(_inline(line))
        else:
            out.append("<br>" + _inline(line))

    close_all()
    return "".join(out)


def render_markdown(text: str) -> str:
    """Render a markdown string to safe HTML.

    >>> render_markdown("**bold**")
    '<p><strong>bold</strong></p>'
    >>> render_markdown("[ok](https://example.com)")
    '<p><a href="https://example.com">ok</a></p>'
    >>> render_markdown("[bad](javascript:alert)")
    '<p><a href="#">bad</a></p>'
    >>> render_markdown("`<script>`")
    '<p><code>&lt;script&gt;</code></p>'
    >>> render_markdown("# Heading")
    '<h1>Heading</h1>'
    """
    if not text:
        return ""
    text, fenced = _mask_fenced(text)
    text = html.escape(text, quote=False)
    text = _block_render(text)
    for i, block in enumerate(fenced):
        text = text.replace(f"\x00FENCED{i}\x00", block)
    return text


def split_into_h2_blocks(text: str) -> "dict[str, str]":
    """Split a markdown document into {h2-heading: body} pairs.

    Fenced code blocks are masked first so '## not a heading' inside ```...```
    doesn't split a block. Content before the first H2 is dropped.

    >>> r = split_into_h2_blocks("## A\\nbody a\\n## B\\nbody b")
    >>> r['A']
    'body a'
    >>> r['B']
    'body b'
    """
    if not text:
        return {}
    masked, blocks_list = _mask_fenced(text)
    blocks: dict[str, str] = {}
    matches = list(H2_RE.finditer(masked))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(masked)
        body = masked[m.end():end].strip()
        for j, block in enumerate(blocks_list):
            inner = re.sub(r"<[^>]+>", "", block)
            body = body.replace(f"\x00FENCED{j}\x00", "```\n" + inner + "\n```")
        blocks[heading] = body
    return blocks
