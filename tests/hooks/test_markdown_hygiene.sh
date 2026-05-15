#!/usr/bin/env bash
# Smoke test: markdown-hygiene strips trailing whitespace and ensures final newline.
set -u

HOOK=".claude/hooks/markdown-hygiene.sh"
TMP=$(mktemp --suffix=.md)
PASS=0
FAIL=0

cleanup() { rm -f "$TMP"; }
trap cleanup EXIT

# Case 1: trailing whitespace gets stripped.
printf 'Line one with trailing spaces   \nLine two\n' > "$TMP"
echo "{\"tool_input\":{\"file_path\":\"$TMP\"}}" | bash "$HOOK" >/dev/null 2>&1
if grep -q ' $' "$TMP"; then
  echo "FAIL  trailing whitespace not stripped"
  FAIL=$((FAIL+1))
else
  echo "PASS  trailing whitespace stripped"
  PASS=$((PASS+1))
fi

# Case 2: missing final newline gets added.
printf 'No final newline' > "$TMP"
echo "{\"tool_input\":{\"file_path\":\"$TMP\"}}" | bash "$HOOK" >/dev/null 2>&1
if [ "$(tail -c 1 "$TMP" | wc -l)" -eq 1 ]; then
  echo "PASS  final newline added"
  PASS=$((PASS+1))
else
  echo "FAIL  final newline not added"
  FAIL=$((FAIL+1))
fi

# Case 3: non-markdown file is left alone.
TMP_TXT=$(mktemp --suffix=.txt)
printf 'leave me alone   \n' > "$TMP_TXT"
echo "{\"tool_input\":{\"file_path\":\"$TMP_TXT\"}}" | bash "$HOOK" >/dev/null 2>&1
if grep -q ' $' "$TMP_TXT"; then
  echo "PASS  non-markdown left alone"
  PASS=$((PASS+1))
else
  echo "FAIL  non-markdown was modified"
  FAIL=$((FAIL+1))
fi
rm -f "$TMP_TXT"

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
