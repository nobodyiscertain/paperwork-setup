#!/usr/bin/env bash
# PostToolUse hook for paperwork-setup.
# Mechanical principles check on markdown edits. Currently enforces:
#   Principle 8: no em dashes (U+2014).
#
# Judgment-heavy principles (e.g., Principle 7, jargon in user-facing copy)
# require distinguishing meta-instructions from real uses. Those live in the
# paperwork-principles-reviewer subagent and the /paperwork-lint skill, not
# in this hook, to keep the hook false-positive-free.
#
# Reads CC tool-event JSON on stdin. Exits 2 with a message on violation so
# Claude sees the failure inline.

set -u

input=$(cat)
file=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)

[ -z "$file" ] && exit 0
case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0

# Principle 8: no em dashes (U+2014).
if dash_hits=$(grep -nF '—' "$file" 2>/dev/null); then
  printf 'PAPERWORK PRINCIPLES VIOLATION in %s\n\nPrinciple 8 (no em dashes - use period, comma, or rewrite):\n%s\n' "$file" "$dash_hits" >&2
  exit 2
fi

exit 0
