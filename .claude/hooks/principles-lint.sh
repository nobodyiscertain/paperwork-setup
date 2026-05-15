#!/usr/bin/env bash
# PostToolUse hook for paperwork-setup.
# Reads CC tool-event JSON on stdin, extracts the edited file path, and
# checks markdown files against Principles 7 (no jargon) and 8 (no em dashes).
# Exits 2 with a message on violation so Claude sees the failure inline.

set -u

input=$(cat)
file=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)

# Not a file we care about: silently succeed.
[ -z "$file" ] && exit 0
case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0

violations=""

# Principle 8: no em dashes (U+2014).
if dash_hits=$(grep -nF '—' "$file" 2>/dev/null); then
  violations+=$'Principle 8 violation (em dashes - use period, comma, or rewrite):\n'
  violations+="$dash_hits"$'\n'
fi

# Principle 7: no jargon in user-facing text.
# Skip lines that contain the literal phrase "Don't say" (those are
# meta-instructions about what NOT to use).
jargon_re='MCP server|agent loop|context window|tool call'
if jargon_hits=$(grep -nE "$jargon_re" "$file" 2>/dev/null | grep -v "Don't say"); then
  violations+=$'Principle 7 violation (jargon in user-facing text):\n'
  violations+="$jargon_hits"$'\n'
fi

if [ -n "$violations" ]; then
  printf 'PAPERWORK PRINCIPLES VIOLATION in %s\n\n%s\n' "$file" "$violations" >&2
  exit 2
fi

exit 0
