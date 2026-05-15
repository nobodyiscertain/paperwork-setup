# Paperwork Setup

**AI handles the paperwork. You handle the humans.**

Paperwork Setup is a one-shot wizard that builds your personal management system into the current directory. It interviews you about how you actually manage, then generates an instructions file your AI agent reads, slash commands wired to your tools, question banks tuned to your team, a signal framework, an optional dashboard, a starter directory for every report and partner, and a human-readable README so you can hand the repo to a future you (or a teammate) without explaining it.

It is not a template you fill in. It is a conversation that builds a system.

## Why this exists

Managers do a surprising amount of paperwork: 1-on-1 prep, reviews, weekly updates, signal-watching, status digests. AI agents are good at most of it, but only if they know how *you* manage. Paperwork Setup encodes that once, into files you own, so the agent has context the moment you ask for help.

## Install

Open your AI coding agent in an empty directory where you want the system to live. Paste this prompt:

```
Set up my personal management system using Paperwork Setup. Begin by fetching
this URL and reading it completely:

https://raw.githubusercontent.com/nobodyiscertain/paperwork-setup/main/PAPERWORK.md

Then follow the instructions inside, starting with the interview. Build the
system in the current directory.
```

The wizard asks you about your team shape (reports, partners, leadership), your tools (calendar, docs, notes), your meeting cadence, whether you want a dashboard, whether to initialize git, and a few questions about how you actually manage. It is one question at a time, with an upfront count, so you know how long it will run. Expect 15-20 minutes.

Works with any agent that can fetch a URL and write files: Claude Code, Codex, Cursor, OpenClaw, and most others. Chat UIs without filesystem access (ChatGPT, Claude.ai) cannot generate the system locally.

## What you get

After the conversation, you have a working repo:

| Path | What it is |
| --- | --- |
| `README.md` | Your instance's human-readable orientation doc. Customized from your interview answers. |
| `CLAUDE.md` | The agent's instructions. Your philosophy, your success framework, your tool map. |
| `people/[name]/` | Profile, 1-on-1 log, and feedback log per direct report and partner. |
| `references/` | Question banks, signal framework, success criteria, feedback templates. |
| `dashboard/` | Optional. Single HTML file you open in your browser. |
| `meetings/`, `weeklies/` | Optional. Routed by `/sync` and `/weekly`. |
| `.claude/commands/` | Slash command definitions. |
| `.claude/paperwork-version` | Install marker. Used by `/paperwork-update` to know what is new upstream. |

Slash commands available in your instance:

- `/new`: adds a direct report or partner and scaffolds their directory
- `/sod` and `/eod`: start and end of day routines
- `/sync`: routes meeting notes to the right place
- `/weekly`: drafts a weekly update from the week's activity
- `/think`: open-ended thinking partner mode
- `/prep`: prep for an upcoming 1-on-1 or meeting
- `/paperwork-update`: pull opt-in updates from upstream Paperwork Setup
- `/paperwork-setup`: re-run the configuration wizard against an existing install

Optional commands appear only if your interview answers warrant them.

## How to update

Paperwork Setup ships changes upstream over time: new commands, better question banks, refined references. Your instance is yours to edit, so updates are opt-in, never forced.

Run `/paperwork-update` inside your instance. It will:

1. Read the SHA in `.claude/paperwork-version` to know what version you are on.
2. Fetch the latest upstream SHA from `nobodyiscertain/paperwork-setup`.
3. Diff the two and group changes into cards: one card per user-facing file or coherent feature.
4. Walk the cards interactively, one at a time. For each, you get a short summary and a Y / Skip / Quit prompt. Default is Skip.
5. Three-way merge any change you accept against your edits, so your customizations survive.
6. Write the new SHA to the install marker when the wizard finishes cleanly.

`/paperwork-update` is idempotent. Re-running picks up where you left off. It never touches your `README.md`, `CLAUDE.md`, or anything under `people/` or `meetings/`. Those are yours.

To reconfigure an existing install (turn the dashboard on, add new commands, change your manager profile), run `/paperwork-setup`. It runs the wizard again against your current files instead of starting from scratch.

## How it actually works

Paperwork Setup is a Claude Code skill that lives as a single prompt (`PAPERWORK.md`) plus an MIT license. Your agent fetches that prompt, runs the interview, and generates files into the current directory. Everything after install is regular files. No background process, no SaaS, no telemetry.

The install marker at `.claude/paperwork-version` records the upstream SHA your instance was generated from. `/paperwork-update` reads that marker to compute the upgrade path the next time you run it.

## Who it is for

Managers of any function. Engineering, product, design, ops, sales, support, customer success. The interview adapts to your stack.

You probably want this if you have direct reports, you already use AI coding agents, and you want a file-based system you own rather than a SaaS dashboard.

You probably do not want this if you have no direct reports yet, or if you want someone else to manage your people for you.

## Coaching

The wizard gets you most of the way. If you want hands-on help getting it set up, debugging your first week, or dialing it in after a month of real use, [book a coaching session](https://everyexpert.com/nobodyiscertain).

## Built by

[Jamie Wagner](https://nobodyiscertain.com), figuring out how to manage a 30-person org with AI in real time and sharing what works.

## License

MIT
