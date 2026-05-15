# Paperwork Automations Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add Claude Code automations to the paperwork-setup repo so that edits to `PAPERWORK.md` (and other markdown) are mechanically checked against the 9 Principles, plus give maintainers two on-demand skills (`/paperwork-lint`, `/dry-run-generation`) and two specialist reviewer subagents.

**Architecture:** All automations live under `.claude/` so they ship with the repo. Two PostToolUse hooks run on every `*.md` Edit/Write (principles lint + whitespace hygiene). Two subagents (`paperwork-principles-reviewer`, `command-consistency-reviewer`) carry the high-level review prompts. Two skills (`paperwork-lint`, `dry-run-generation`) bundle on-demand workflows. Hook scripts read CC's stdin JSON via `jq`, extract the file path, and exit 2 with a message on violation so Claude sees the failure inline.

**Tech Stack:** Bash + jq for hook scripts. Markdown for subagent and skill definitions. JSON for `.claude/settings.json`.

> **Update during implementation (commit `da39a9f`):** the principles-lint hook was narrowed from "em dashes + jargon" to "em dashes only." Verifying against PAPERWORK.md surfaced 5 jargon hits, all agent-facing meta-instructions ("Don't say MCP server", "Avoid jargon like X"), not user-facing copy. Distinguishing them mechanically required a brittle whitelist that risked letting real violations through. Cleaner split: mechanical rules (em dashes) stay in the hook for zero false positives; judgment rules (jargon) live in the `paperwork-principles-reviewer` subagent and `/paperwork-lint` skill.

---

## Pre-flight Notes

- **Repo shape:** content-only. No package.json, no tests, no source. The "code" is `PAPERWORK.md` (~930 lines), `README.md`, `LICENSE`. Verification = run hook scripts directly with mock stdin.
- **Principles file:** `PAPERWORK.md` lines 904–920 (the 9 numbered principles). Reviewer subagents reference these by line range.
- **False-positive shape for jargon checks:** lines that contain `Don't say` are explicit instructions to the AI agent about what NOT to use — those must be excluded from jargon matches. Em dashes (`—`, U+2014) get flagged everywhere with no exceptions.
- **CC hook input format:** `PostToolUse` hooks receive JSON on stdin. The shape is `{"tool_input": {"file_path": "...", ...}, ...}`. Extract via `jq -r '.tool_input.file_path'`.
- **Exit codes for hooks:** exit 2 sends the stderr output back to Claude as a blocking error. Exit 0 is silent success. Exit 1 is non-blocking error (shows but doesn't block).
- **Frequent commits:** one commit per task. Each task is its own logical unit.

---

## Task 1: Scaffold `.claude/` directory

**Files:**
- Create: `.claude/settings.json` (empty JSON skeleton)
- Create: `.claude/hooks/` (directory)
- Create: `.claude/agents/` (directory)
- Create: `.claude/skills/` (directory)

**Step 1: Create the directory structure**

```bash
mkdir -p .claude/hooks .claude/agents .claude/skills
```

**Step 2: Create the empty settings file**

Write `.claude/settings.json`:

```json
{
  "hooks": {}
}
```

**Step 3: Verify structure**

Run: `find .claude -type f -o -type d | sort`
Expected: prints `.claude`, `.claude/agents`, `.claude/hooks`, `.claude/settings.json`, `.claude/skills`

**Step 4: Commit**

```bash
git add .claude/
git commit -m "Scaffold .claude/ directory for hooks, agents, and skills"
```

---

## Task 2: Write the principles-lint hook script

**Files:**
- Create: `.claude/hooks/principles-lint.sh`
- Create: `tests/hooks/fixtures/clean.md` (no violations)
- Create: `tests/hooks/fixtures/em-dash.md` (em dash present)
- Create: `tests/hooks/fixtures/jargon.md` (uses "MCP server" outside a "Don't say" line)
- Create: `tests/hooks/fixtures/jargon-allowed.md` (uses "MCP server" only inside a "Don't say" line — must NOT trigger)
- Create: `tests/hooks/test_principles_lint.sh`

**Step 1: Write the failing tests first**

Write `tests/hooks/fixtures/clean.md`:

```markdown
# Clean fixture

This file has no em dashes and no jargon. It just talks about how to manage people and write notes that are easy to capture.
```

Write `tests/hooks/fixtures/em-dash.md`:

```markdown
# Em dash fixture

This file uses an em dash — like that one — which violates principle 8.
```

Write `tests/hooks/fixtures/jargon.md`:

```markdown
# Jargon fixture

You will need to set up an MCP server to integrate Linear with the agent loop.
```

Write `tests/hooks/fixtures/jargon-allowed.md`:

```markdown
# Jargon-allowed fixture

When talking to the user, follow principle 7. Don't say "MCP server" or "agent loop". Use plain English instead.
```

Write `tests/hooks/test_principles_lint.sh`:

```bash
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

run_case "clean.md exits 0"            "$FIXTURES/clean.md"          0
run_case "em-dash.md exits 2"          "$FIXTURES/em-dash.md"        2
run_case "jargon.md exits 2"           "$FIXTURES/jargon.md"         2
run_case "jargon-allowed.md exits 0"   "$FIXTURES/jargon-allowed.md" 0
run_case "non-markdown skipped"        "/tmp/not-a-real-file.txt"    0

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
```

Make it executable:

```bash
chmod +x tests/hooks/test_principles_lint.sh
```

**Step 2: Run tests to verify they fail**

Run: `bash tests/hooks/test_principles_lint.sh`
Expected: FAIL on every case (script doesn't exist yet).

**Step 3: Write the minimal hook implementation**

Write `.claude/hooks/principles-lint.sh`:

```bash
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
  violations+=$'Principle 8 violation (em dashes — use period, comma, or rewrite):\n'
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
```

Make it executable:

```bash
chmod +x .claude/hooks/principles-lint.sh
```

**Step 4: Run tests to verify they pass**

Run: `bash tests/hooks/test_principles_lint.sh`
Expected: all 5 cases PASS.

**Step 5: Commit**

```bash
git add .claude/hooks/principles-lint.sh tests/hooks/
git commit -m "Add principles-lint hook script for em dashes and jargon"
```

---

## Task 3: Wire principles-lint into settings.json

**Files:**
- Modify: `.claude/settings.json`

**Step 1: Update settings to register the hook**

Replace `.claude/settings.json` contents with:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/principles-lint.sh"
          }
        ]
      }
    ]
  }
}
```

**Step 2: Verify JSON is valid**

Run: `jq . .claude/settings.json`
Expected: pretty-prints the JSON without errors.

**Step 3: Live-fire test the hook end-to-end**

Create a known-bad markdown file in /tmp and simulate the JSON Claude Code would send:

```bash
echo "Test em — dash" > /tmp/hook-live-test.md
echo '{"tool_input":{"file_path":"/tmp/hook-live-test.md"}}' | bash .claude/hooks/principles-lint.sh
echo "exit code: $?"
```

Expected: prints "PAPERWORK PRINCIPLES VIOLATION in /tmp/hook-live-test.md" with line 1 highlighted, exit code 2.

Cleanup: `rm /tmp/hook-live-test.md`

**Step 4: Commit**

```bash
git add .claude/settings.json
git commit -m "Wire principles-lint hook into PostToolUse on Edit/Write/MultiEdit"
```

---

## Task 4: Write the markdown-hygiene hook script

**Files:**
- Create: `.claude/hooks/markdown-hygiene.sh`
- Create: `tests/hooks/test_markdown_hygiene.sh`

**Step 1: Write the failing test**

Write `tests/hooks/test_markdown_hygiene.sh`:

```bash
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
last_byte=$(tail -c 1 "$TMP")
if [ "$last_byte" = $'\n' ]; then
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
```

Make executable: `chmod +x tests/hooks/test_markdown_hygiene.sh`

**Step 2: Run tests to verify they fail**

Run: `bash tests/hooks/test_markdown_hygiene.sh`
Expected: FAIL on all cases (script doesn't exist yet).

**Step 3: Write the hook**

Write `.claude/hooks/markdown-hygiene.sh`:

```bash
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
```

Make executable: `chmod +x .claude/hooks/markdown-hygiene.sh`

**Step 4: Run tests to verify they pass**

Run: `bash tests/hooks/test_markdown_hygiene.sh`
Expected: all 3 cases PASS.

**Step 5: Wire into settings.json**

Update `.claude/settings.json` to add the second hook:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/principles-lint.sh"
          },
          {
            "type": "command",
            "command": "bash .claude/hooks/markdown-hygiene.sh"
          }
        ]
      }
    ]
  }
}
```

Verify: `jq . .claude/settings.json`

**Step 6: Commit**

```bash
git add .claude/hooks/markdown-hygiene.sh .claude/settings.json tests/hooks/test_markdown_hygiene.sh
git commit -m "Add markdown-hygiene hook for trailing whitespace and final newline"
```

---

## Task 5: Create paperwork-principles-reviewer subagent

**Files:**
- Create: `.claude/agents/paperwork-principles-reviewer.md`

**Step 1: Write the subagent definition**

Write `.claude/agents/paperwork-principles-reviewer.md`:

```markdown
---
name: paperwork-principles-reviewer
description: Reviews proposed changes to PAPERWORK.md (or related repo files) against the 9 numbered Principles. Use proactively before commits and PRs that touch PAPERWORK.md, README.md, or any generation step. Input: a git diff or a description of intended changes. Output: a per-principle verdict citing the principle number, with a concrete violation or "no violations found".
tools: Read, Grep, Bash
---

You are the paperwork-setup principles reviewer. Your only job is to evaluate proposed changes against the 9 Principles in `PAPERWORK.md` (the section starting at line 904, headed `## Principles`).

## Process

1. Read `PAPERWORK.md` lines 900–925 to load the current Principles. They are the source of truth — never rely on a memorized version.
2. Read or accept the diff being reviewed.
3. For each of the 9 principles, evaluate the diff in turn. Output one block per principle:

   ```
   Principle N: <short title>
   Verdict: PASS | VIOLATION | N/A
   Evidence: <quote the offending line(s) from the diff, or "no relevant changes">
   ```

4. If you give a VIOLATION verdict, propose the smallest possible change that would fix it.
5. End with a one-line summary: `<X> violations found` or `No violations found.`

## Rules

- Cite the principle by number every time. Vague approval is not allowed.
- Quote the actual line from the diff when calling out a violation. Don't paraphrase.
- N/A is fine when the diff doesn't touch the principle's domain (e.g., a typo fix doesn't engage Principle 9).
- Don't expand scope. Only review against the 9 principles. Don't comment on style, structure, or anything else unless it maps to a principle.
- Principle 8 (no em dashes) is mechanically enforced by the principles-lint hook. Still verify it — defense in depth.
- Principle 7 (no jargon) requires judgment: the forbidden terms can legitimately appear in meta-instructions (e.g., "Don't say 'MCP server'"). Only flag occurrences in *user-facing copy* — text the AI agent will say to the user or write into a generated file.
- Principle 9 (one source of truth per concept) is the most subtle. Watch for two commands that compute the same content, or a new command that duplicates dashboard logic.
```

**Step 2: Verify frontmatter is well-formed**

Run: `head -5 .claude/agents/paperwork-principles-reviewer.md`
Expected: shows the YAML frontmatter with `name`, `description`, `tools`.

**Step 3: Smoke-test the subagent loads**

Note: live invocation requires Claude Code to actually dispatch the agent. We verify the file is structurally valid by checking frontmatter + ensuring no parse errors:

```bash
awk '/^---$/{c++; next} c==1{print}' .claude/agents/paperwork-principles-reviewer.md | head -20
```

Expected: prints the frontmatter block cleanly.

**Step 4: Commit**

```bash
git add .claude/agents/paperwork-principles-reviewer.md
git commit -m "Add paperwork-principles-reviewer subagent"
```

---

## Task 6: Create command-consistency-reviewer subagent

**Files:**
- Create: `.claude/agents/command-consistency-reviewer.md`

**Step 1: Write the subagent definition**

Write `.claude/agents/command-consistency-reviewer.md`:

```markdown
---
name: command-consistency-reviewer
description: Reviews changes to slash command definitions in PAPERWORK.md (Step 3, lines ~289–585) for responsibility overlap, contract drift, and source-of-truth violations. Use when adding, removing, or modifying any /sod, /eod, /sync, /weekly, /think, /prep, /new, /health, /review, /prune, or other generated command. Output: a per-command map of responsibilities plus a list of overlaps or contradictions.
tools: Read, Grep, Bash
---

You are the slash-command consistency reviewer for paperwork-setup. Your job is to make sure the commands defined in `PAPERWORK.md` Step 3 stay coherent: no two commands own the same responsibility, no command silently re-implements logic that lives in another, and every command's input/output contract is internally consistent.

## Process

1. Read `PAPERWORK.md` Step 3 in full (the section headed `### Step 3: Generate Slash Commands`, currently around lines 289–585).
2. For each command defined there, extract:
   - Name (e.g., `/prep`)
   - One-line purpose
   - Inputs it reads (files, tools, prior command outputs)
   - Outputs it produces (files written, content displayed)
3. Build a responsibility table. Flag any cell where two commands claim ownership of the same output or content type.
4. Cross-reference against Principle 9 ("one source of truth per concept"). Cite the principle when calling out a violation.
5. Output:
   - A markdown table: `| Command | Purpose | Reads | Writes |`
   - A list of overlaps, each with the offending command pair and the shared responsibility
   - A list of contract drifts (e.g., `/prep` is documented as the source of truth for prep content but `/dashboard` recomputes it)
   - A one-line verdict: `<N> overlaps, <M> contract drifts` or `Commands are consistent.`

## Rules

- Quote the relevant lines from PAPERWORK.md when flagging an issue. Don't paraphrase.
- The recent commit `a882260 /prep is sole source of truth; dashboard becomes thin presentation layer` is the canonical example of a fix you're trying to prevent. Use that pattern when proposing fixes.
- Don't comment on principles other than 9 — the principles-reviewer subagent owns those.
- Don't propose new commands. You're a reviewer, not a designer.
```

**Step 2: Verify frontmatter**

Run: `head -5 .claude/agents/command-consistency-reviewer.md`
Expected: clean YAML frontmatter.

**Step 3: Commit**

```bash
git add .claude/agents/command-consistency-reviewer.md
git commit -m "Add command-consistency-reviewer subagent"
```

---

## Task 7: Create `/paperwork-lint` skill

**Files:**
- Create: `.claude/skills/paperwork-lint/SKILL.md`

**Step 1: Write the skill**

Write `.claude/skills/paperwork-lint/SKILL.md`:

```markdown
---
name: paperwork-lint
description: Audit PAPERWORK.md (and any other markdown in the repo) against the 9 Principles. Runs the principles-lint hook against every tracked markdown file, then dispatches the paperwork-principles-reviewer subagent for the judgment-based principles. Use before opening a PR or after a large rewrite.
disable-model-invocation: true
---

# /paperwork-lint

Run a full principles audit on this repo. Two-pass:

## Pass 1: Mechanical (regex)

Run the principles-lint hook against every tracked markdown file:

```bash
for f in $(git ls-files '*.md'); do
  printf '{"tool_input":{"file_path":"%s"}}\n' "$f" | bash .claude/hooks/principles-lint.sh
done
```

Capture stderr per file. If exit code is 2, record the violations.

## Pass 2: Judgment (subagent)

If any markdown file has uncommitted changes, gather the diff:

```bash
git diff HEAD -- '*.md' > /tmp/paperwork-lint-diff.patch
```

Then invoke the `paperwork-principles-reviewer` subagent with that diff as input.

If the working tree is clean, run the subagent against the most recent commit instead:

```bash
git show HEAD -- '*.md' > /tmp/paperwork-lint-diff.patch
```

## Output

Produce a single report:

```
## Paperwork Lint Report

### Mechanical violations (Pass 1)
<file>:<line>: <violation>
...
or "No mechanical violations."

### Judgment review (Pass 2, from paperwork-principles-reviewer)
<full subagent output>

### Summary
<N> mechanical violations, <M> judgment violations.
```

## Notes

- This skill is user-only (`disable-model-invocation: true`). The model should not run it autonomously — it's an explicit pre-flight check the maintainer triggers.
- If `git ls-files` returns nothing (e.g., run outside the repo), exit with a clear error.
```

**Step 2: Verify**

Run: `head -10 .claude/skills/paperwork-lint/SKILL.md`
Expected: clean frontmatter with `disable-model-invocation: true`.

**Step 3: Commit**

```bash
git add .claude/skills/paperwork-lint/
git commit -m "Add /paperwork-lint skill for full principles audit"
```

---

## Task 8: Create `/dry-run-generation` skill with mock interview fixture

**Files:**
- Create: `.claude/skills/dry-run-generation/SKILL.md`
- Create: `.claude/skills/dry-run-generation/fixtures/mock-interview.md`

**Step 1: Write the mock interview fixture**

Write `.claude/skills/dry-run-generation/fixtures/mock-interview.md`:

```markdown
# Mock Interview Answers

A canned set of interview answers covering all 5 parts of the PAPERWORK.md interview. Used by /dry-run-generation to smoke-test the generation steps without a real human conversation.

## Part 1: Your World
- Role: Engineering Director
- Function: Engineering
- Direct reports: 6 (4 ICs, 2 managers)
- Manages other managers: yes (2)
- Cross-functional partners: 1 PM lead (weekly), 1 Design lead (biweekly)
- Skip-level: VP Engineering, monthly
- Company: 200-person Series B
- Time in role: 18 months
- Company-wide processes: quarterly perf review, OKR cadence, biannual calibration

## Part 2: Your Rhythm
- 1-on-1s: weekly with ICs, biweekly with managers, 30 minutes
- Agenda: shared (Notion doc per person)
- Team rituals: weekly standup, monthly retro, weekly team broadcast
- Weekly update: yes, written, sent to VP and team
- Performance reviews: quarterly informal, annual formal
- Planning cadence: 6-week cycles
- Daily bookends: yes, both /sod and /eod

## Part 3: Your Tools
- Calendar: Google
- Notes: Notion (no Claude integration yet)
- Personal tasks: Things
- Team work tracking: Linear (Claude integration installed)
- Code: GitHub (Claude integration installed)
- Meeting recording: Granola
- Team communication: Slack (Claude integration installed)
- Performance/HR: Lattice (manual reference)

## Part 4: Your Philosophy
- Most important: clear feedback, frequent
- Role identity: coach + shield
- Best self: people leave 1-on-1s knowing exactly what to do next
- Struggling signals: missed commitments, withdrawal in standups, vague status updates
- Thriving signals: proactive scope expansion, mentoring others, shipping ahead
- Feedback: in the moment when small, in 1-on-1s when bigger; verbal + written followup
- Mentorship vs autonomy: depends on level, default to autonomy after 6 months
- Performance issues: address fast, document everything, partner with HR early
- Communication style: direct
- Measuring success: career levels (written ladder) + quarterly OKRs + qualitative read on collaboration
- Dashboard: yes, want today's schedule + team pulse (red/yellow/green) + open promises
- Modes wanted: sparring partner, ghostwriter, prep buddy

## Part 5: Your Pain
- Top pain: forgetting what was discussed in 1-on-1s 3 weeks ago
- Second pain: writing perf reviews from cold memory
- Third pain: feeling reactive instead of proactive on team health
```

**Step 2: Write the skill**

Write `.claude/skills/dry-run-generation/SKILL.md`:

```markdown
---
name: dry-run-generation
description: Smoke-test PAPERWORK.md's generation steps end-to-end by running them against a fixed mock interview transcript. Catches "Step 3 references a command that Step 9's dashboard never uses" and similar contract-drift bugs before they ship. Use after edits to any Generation Step (Steps 1–11).
disable-model-invocation: true
---

# /dry-run-generation

Walk PAPERWORK.md's 11 Generation Steps against a canned interview, without writing files anywhere. Output a structured report of what *would* be generated and any contract drift or contradictions found.

## Process

1. Read `PAPERWORK.md` in full.
2. Read the mock interview at `.claude/skills/dry-run-generation/fixtures/mock-interview.md`.
3. For each Generation Step (1 through 11):
   - State the step title.
   - List the files/content the step would produce given the mock answers.
   - Note any inputs the step depends on (prior step outputs, interview answers, tools).
   - Flag contradictions: the step references something a prior step didn't produce, two steps produce conflicting content, or the step's behavior depends on an interview answer the mock doesn't cover.
4. After Step 11, dispatch the `command-consistency-reviewer` subagent on the *would-be-generated* slash commands from Step 3.
5. Produce a final report:

   ```
   ## Dry-Run Generation Report

   ### Step-by-step trace
   Step 1: <title> → <produced>
   Step 2: <title> → <produced>
   ...

   ### Contract drift / contradictions
   - <issue 1>
   - <issue 2>
   or "No issues found."

   ### Command consistency review (from subagent)
   <subagent output>

   ### Verdict
   <PASS | <N> issues found>
   ```

## Notes

- DO NOT actually write any generated files anywhere. This is a dry run. The output goes only to the chat.
- If the mock interview doesn't cover an answer a step needs, log that as a coverage gap, not a step failure.
- This skill is user-only (`disable-model-invocation: true`). It's a maintainer pre-flight check, not a routine action.
```

**Step 3: Verify structure**

Run: `find .claude/skills/dry-run-generation -type f | sort`
Expected: prints `.claude/skills/dry-run-generation/SKILL.md` and `.claude/skills/dry-run-generation/fixtures/mock-interview.md`.

**Step 4: Commit**

```bash
git add .claude/skills/dry-run-generation/
git commit -m "Add /dry-run-generation skill with mock interview fixture"
```

---

## Task 9: Final verification

**Files:** none (verification only)

**Step 1: Run all hook tests**

Run:

```bash
bash tests/hooks/test_principles_lint.sh
bash tests/hooks/test_markdown_hygiene.sh
```

Expected: both report all cases PASS.

**Step 2: Spot-check PAPERWORK.md against the principles hook**

The principles hook should pass cleanly on the current `PAPERWORK.md`:

```bash
echo '{"tool_input":{"file_path":"PAPERWORK.md"}}' | bash .claude/hooks/principles-lint.sh
echo "exit code: $?"
```

Expected: exit code 0. If non-zero, the hook is flagging legitimate uses — record them and refine the false-positive filter (see Task 2 step 3 commentary).

**Step 3: Verify all `.claude/` files are committed**

Run: `git status .claude/ tests/`
Expected: "nothing to commit, working tree clean".

**Step 4: Inventory check**

Run:

```bash
find .claude -type f | sort
find tests -type f | sort
```

Expected output:

```
.claude/agents/command-consistency-reviewer.md
.claude/agents/paperwork-principles-reviewer.md
.claude/hooks/markdown-hygiene.sh
.claude/hooks/principles-lint.sh
.claude/settings.json
.claude/skills/dry-run-generation/SKILL.md
.claude/skills/dry-run-generation/fixtures/mock-interview.md
.claude/skills/paperwork-lint/SKILL.md
tests/hooks/fixtures/clean.md
tests/hooks/fixtures/em-dash.md
tests/hooks/fixtures/jargon-allowed.md
tests/hooks/fixtures/jargon.md
tests/hooks/test_markdown_hygiene.sh
tests/hooks/test_principles_lint.sh
```

**Step 5: Review the branch log**

Run: `git log --oneline main..HEAD`

Expected: roughly 8 commits (one per task, plus the initial .gitignore commit).

---

## Done Criteria

- [ ] `.claude/hooks/principles-lint.sh` exists, tests pass, wired in settings.json
- [ ] `.claude/hooks/markdown-hygiene.sh` exists, tests pass, wired in settings.json
- [ ] `.claude/agents/paperwork-principles-reviewer.md` exists with valid frontmatter
- [ ] `.claude/agents/command-consistency-reviewer.md` exists with valid frontmatter
- [ ] `.claude/skills/paperwork-lint/SKILL.md` exists with `disable-model-invocation: true`
- [ ] `.claude/skills/dry-run-generation/SKILL.md` + fixtures exist
- [ ] All hook tests pass
- [ ] PAPERWORK.md passes the principles hook cleanly (exit 0)
- [ ] Branch is clean and ready for PR

---

## After Implementation

When this plan is fully executed:

1. Use `superpowers:finishing-a-development-branch` to decide between merge-to-main vs PR.
2. The hooks only fire for *this* repo's edits — they ship in `.claude/settings.json` so any clone gets them automatically.
3. The two subagents and two skills are immediately available via the Agent and Skill tools after merge.
