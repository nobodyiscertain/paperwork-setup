---
name: dry-run-generation
description: Smoke-test PAPERWORK.md's generation steps end-to-end by running them against a fixed mock interview transcript. Catches "Step 3 references a command that Step 9's dashboard never uses" and similar contract-drift bugs before they ship. Use after edits to any Generation Step (Steps 1-11).
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
   Step 1: <title> -> <produced>
   Step 2: <title> -> <produced>
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
