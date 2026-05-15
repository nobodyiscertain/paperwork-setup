#!/usr/bin/env bash
# PostToolUse hook: strip trailing whitespace and ensure final newline on
# markdown files. Silent success on non-markdown.

set -u

input=$(cat)
file=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)

[ -z "$file" ] && exit 0
case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0

# Strip trailing whitespace in place.
sed -i 's/[[:space:]]*$//' "$file"

# Ensure final newline.
if [ -s "$file" ] && [ "$(tail -c 1 "$file" | wc -l)" -eq 0 ]; then
  printf '\n' >> "$file"
fi

exit 0
