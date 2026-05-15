---
name: paperwork-lint
description: Audit PAPERWORK.md (and any other markdown in the repo) against the 9 Principles. Runs the principles-lint hook against every tracked markdown file, then dispatches the paperwork-principles-reviewer subagent for the judgment-based principles. Use before opening a PR or after a large rewrite.
disable-model-invocation: true
---

# /paperwork-lint

Run a full principles audit on this repo. Two-pass.

## Pass 1: Mechanical (regex)

The principles-lint hook only enforces Principle 8 (no em dashes). Principle 7 (no jargon) requires meta-instruction judgment and is deferred to Pass 2.

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

- This skill is user-only (`disable-model-invocation: true`). The model should not run it autonomously. It's an explicit pre-flight check the maintainer triggers.
- If `git ls-files` returns nothing (e.g., run outside the repo), exit with a clear error.
