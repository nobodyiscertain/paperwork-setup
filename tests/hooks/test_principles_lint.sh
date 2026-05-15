#!/usr/bin/env bash
# Smoke test: run principles-lint.sh against fixtures and assert exit codes.
set -u

HOOK=".claude/hooks/principles-lint.sh"
FIXTURES="tests/hooks/fixtures"
PASS=0
FAIL=0

run_case() {
  local label="$1" file="$2" expected_exit="$3"
  local payload
  payload=$(printf '{"tool_input":{"file_path":"%s"}}' "$file")
  set +e
  echo "$payload" | bash "$HOOK" >/dev/null 2>&1
  local actual=$?
  set -e
  if [ "$actual" -eq "$expected_exit" ]; then
    echo "PASS  $label  (exit $actual)"
    PASS=$((PASS+1))
  else
    echo "FAIL  $label  expected exit $expected_exit, got $actual"
    FAIL=$((FAIL+1))
  fi
}

run_case "clean.md exits 0"                  "$FIXTURES/clean.md"          0
run_case "em-dash.md exits 2"                "$FIXTURES/em-dash.md"        2
run_case "jargon.md exits 0 (deferred to subagent)"      "$FIXTURES/jargon.md"         0
run_case "jargon-allowed.md exits 0"         "$FIXTURES/jargon-allowed.md" 0
run_case "non-markdown skipped"              "/tmp/not-a-real-file.txt"    0

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
