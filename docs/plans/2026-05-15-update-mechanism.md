# Update mechanism for installed users

**Date:** 2026-05-15
**Status:** Plan only. No code changes in this PR.

## TL;DR

- Track the upstream SHA the user installed from in a marker file inside their instance.
- `/paperwork-update` fetches the latest upstream SHA, diffs the two, walks the user through each user-facing change in a yes/skip wizard, applies opt-ins with a three-way merge, and writes the new SHA.
- Idempotent by construction: running it twice in a row finds nothing the second time. No version pinning, no rollback feature, no curated changelog requirement.

## The three commands

**Install command (already exists, unchanged by this plan).** When the user first runs the Paperwork Setup flow, it records the upstream SHA that produced their instance. That SHA is the baseline for every future update.

**`/paperwork-update` (new).** Reads the marker SHA. Fetches the current upstream SHA from `nobodyiscertain/paperwork-setup` master. Lists the user-facing changes between the two. Walks the user through one change at a time with [Yes / Skip / Quit] options. Applies opt-ins with a three-way merge so the user's edits are preserved where possible. On clean exit, writes the new SHA into the marker.

**`/paperwork-setup` (optional re-run of the install wizard).** Re-runs the original install questions, but with the user's current state loaded. Surfaces diffs as proposals: "You have 3 reports configured — add another, edit one, or change a global setting?" Answering "no change" to every prompt is a clean no-op. This is the path for restructuring the install after the fact. Note: this is distinct from `/new`, which lives inside the user's installed instance and adds a single new person/report on demand. `/new` has nothing to do with upstream updates.

## Marker shape and location

**File:** `.claude/paperwork-version` inside the user's instance directory.

**Contents:** one line, two whitespace-separated fields.

```
<install-sha> <iso-8601-utc-timestamp>
```

Example:

```
3c4be7bf9a2e1d4567890abcdef0123456789abc 2026-05-15T14:32:00Z
```

**Why this shape:**

- Plain text. The user can `cat` it and understand what it means.
- Single line, no parsing fragility. Splitting on whitespace is enough.
- Separate file from `CLAUDE.md` so the user editing their instructions can't accidentally clobber the marker.
- Lives under `.claude/` because that directory already exists in every install and is conceptually agent-state.
- The timestamp is informational only. The SHA is the source of truth.

If the marker is missing or unreadable, `/paperwork-update` falls back to asking the user when they installed (rough estimate is fine) and uses the closest upstream commit by date as a baseline.

## The update wizard

The user sees something like this on screen, one card at a time:

```
Change 1 of 3 — Added a new skill: weekly retro

Adds a `/weekly-retro` command that walks you through a Friday
retrospective and writes the output to journal/[year]/[YYYY-WXX].md.
New file. No conflict with your existing setup.

  [Yes — install it]   [Skip]   [Quit and apply what I've said yes to]
```

```
Change 2 of 3 — Updated the 1-on-1 template

The "Notes for next time" section now defaults to a checklist
instead of a free-form bullet list. Your existing one-on-ones.md
files are untouched; this only affects the template used for new
entries.

  [Yes]   [Skip]   [Quit]
```

```
Change 3 of 3 — Edit conflict on PAPERWORK.md

Upstream changed lines 220-240 of PAPERWORK.md. You've also edited
that range locally. I can:
  - apply upstream and lose your local edits there
  - keep your local edits and skip the upstream change
  - show the diff and let you merge by hand

  [Apply upstream]   [Keep mine]   [Show diff]   [Skip]   [Quit]
```

Once the wizard exits cleanly, the new upstream SHA is written into `.claude/paperwork-version`. Running `/paperwork-update` again immediately finds no further changes and exits in one line: "You're already on the latest version."

**Idempotency property:** the marker SHA is only written on clean exit of a successful wizard pass. Partial application (user quit halfway) leaves the marker unchanged, so re-running picks up exactly where they left off without double-applying anything.

## Edit preservation (three-way merge)

For any file that exists in both the user's instance and upstream, and that the user has modified since install, the update applies a three-way merge:

- **Base:** the file's contents at the marker SHA (fetched from upstream history).
- **Ours:** the user's current file.
- **Theirs:** the file at the new upstream SHA.

If the merge succeeds without conflict, apply it silently as part of the opt-in.

If the merge produces conflict markers, surface the conflict inline (the "Edit conflict" card above) and let the user choose: apply upstream, keep theirs, hand-merge, or skip.

For files that only exist upstream (new) or only exist in the user's instance (locally added), there is no merge — just a file-add or a do-nothing.

## Smoke test before broader rollout

Before pointing any beta tester at `/paperwork-update`, the maintainer runs the loop end-to-end in a scratch directory:

1. The owner installs paperwork-setup into `/tmp/scratch-install`. Confirms `.claude/paperwork-version` exists and contains the expected SHA.
2. The owner pushes a no-op user-facing commit to upstream master — for example, adding a line to a template's example output.
3. Runs `/paperwork-update` against the scratch install. Confirms: the wizard presents the change, the opt-in applies cleanly, the marker SHA updates to the new HEAD, a second immediate run reports "already on latest."
4. The owner pushes a second commit that intentionally collides with an edit made locally in the scratch install (modify the same template line on both sides).
5. Runs `/paperwork-update` again. Confirms: the conflict card appears, each resolution option works as advertised, and the marker SHA still ends up at the new HEAD when the wizard exits cleanly.

That's the gate. The mechanism is proven once those five steps pass on the owner's scratch install.

## Non-goals

- **No version pinning.** The user is always at one SHA. They don't pin to "v1.4.2"; there are no version numbers.
- **No rollback mode.** Git history in upstream is the rollback record. If the user wants to revert, they revert the files themselves; the tooling won't ship a `--rollback` flag.
- **No curated changelog requirement.** The wizard derives change descriptions from commit messages and the file-diff itself. The maintainer is not on the hook to maintain a separate `CHANGELOG.md` to make updates work. If a particular commit deserves a longer explanation, the commit message can carry it.
- **No background auto-update.** `/paperwork-update` only runs when the user invokes it. There is no daemon, no notification, no "update available" banner.
- **No telemetry.** The updater does not phone home about what was accepted or skipped.
