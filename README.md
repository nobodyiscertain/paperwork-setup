# Paperwork Setup

**AI handles the paperwork. You handle the humans.**

Paperwork Setup is a one-shot wizard that builds your personal management system into the current directory. It interviews you for fifteen or twenty minutes about how you actually manage your team, then generates an instructions file your AI agent reads, slash commands wired to your tools, question banks tuned to your people, a signal framework, an integrations doc, an optional dashboard, and a human-readable README so the repo makes sense when you come back to it months later.

It is not a template you fill in. It is a conversation that builds a system.

## Who this is for

Managers of any function. Engineering, product, design, ops, sales, support, customer success, finance. If you have direct reports, you already use an AI coding agent, and you want a file-based system you own rather than a SaaS dashboard, this is for you.

If you have no direct reports yet, or you want a tool that manages your people for you, you probably want something else.

## Install

Open your AI coding agent in an empty directory where you want the system to live. Paste this prompt:

```
Set up Paperwork for me. Read https://raw.githubusercontent.com/nobodyiscertain/paperwork-setup/main/PAPERWORK.md and follow the instructions there.
```

Run the wizard. It interviews you. Fifteen to twenty minutes. Done.

The agent asks one question at a time about your team shape, your rhythm, your tools, your philosophy, and what falls through the cracks. When the conversation is over it generates everything in place. Nothing for you to copy or move.

At the end you can paste a list of names and roles to scaffold your team folders in one pass, or skip and use `/new` one report at a time as the week unfolds.

If you already have Paperwork installed in this directory, the wizard will detect it and point you at `/paperwork-update` or `/paperwork-setup` instead of overwriting anything.

Works with any agent that can fetch a URL and write files: Claude Code, Codex, Cursor, OpenClaw, and most others. Chat UIs without filesystem access (ChatGPT, Claude.ai) cannot generate the system locally.

## Your first week

The wizard hands you a working repo. Here is what the first week looks like in practice. Skip any command you don't see in `.claude/commands/`; the wizard only installs the ones your interview answers asked for.

**Monday morning.** Open the directory and run `/sod`. The agent pulls today's calendar, prepares a prep card for every 1-on-1 and recurring meeting, surfaces what carried over from Friday, and asks you what your one priority is today. You read the briefing, push the priority back if it is wrong, then start your day.

**Midweek, right after a 1-on-1.** Run `/sync`. The agent pulls the transcript from your meeting recorder, summarizes the conversation into the right person's file, cross-references any other names that came up, and surfaces only the items that need your judgment. If the meeting was a recurring one the agent has not seen before, it sets up the folder for that meeting on the fly. Same for any new name that comes up in the transcript. You do not move files around.

**Friday afternoon.** Run `/weekly`. The agent reads every 1-on-1 entry from the week, pulls activity from your work tracker and code host, and drafts your week-in-review for your manager in your voice. You edit, you send.

**End of the day, any day.** Run `/eod`. The agent walks your inbox, asks where each item belongs, routes decisions into a decision log, wins into a brag doc, action items into your task tool. The inbox ends empty.

## What you get

After the conversation, you have a working repo:

| Path | What it is |
| --- | --- |
| `README.md` | Your instance's human-readable orientation doc, customized from your interview. |
| `CLAUDE.md` | The agent's instructions. Your philosophy, your success framework, your tool map. |
| `people/[name]/` | Profile, 1-on-1 log, and feedback log per direct report, partner, or leadership relationship. Created by `/new`. |
| `context/` | Question banks, signal framework, success framework, feedback guide, integrations doc. Edit as your thinking evolves. |
| `library/` | Markdown docs you want to come back to: research, frameworks, redlines. Surfaced as cards on the dashboard. |
| `dashboard/` | Optional. Single HTML page with your day, your team snapshot, and your library. Opens in your browser when the wizard finishes. |
| `meetings/`, `weeklies/` | Optional. Lazy-created by `/sync` and `/weekly` the first time you need them. |
| `.claude/commands/` | Slash command definitions. |
| `.claude/paperwork-version` | Install marker. Used by `/paperwork-update` to know what is new upstream. |

Slash commands available in your instance:

Always installed:

- `/prep [name-or-event]`: prep for an upcoming 1-on-1, peer sync, or recurring meeting.
- `/think [topic]`: open-ended thinking space, no audience but you.
- `/new [first-last]`: add a direct report, partner, or leadership relationship. Conversational; the agent asks the basics and builds the folder.
- `/health`: team health snapshot. Pulls signals across your people and surfaces what to pay attention to.
- `/prune`: living-system maintenance. Walks the structure and surfaces what to keep, change, or remove. Run monthly-ish.
- `/paperwork-update`: pull opt-in updates from upstream Paperwork Setup.
- `/paperwork-setup`: re-run the configuration wizard against an existing install.

Optional, based on your interview answers:

- `/sod` and `/eod`: start and end of day routines (if you wanted daily bookends).
- `/sync`: routes recorded meeting notes to the right place (if you use a meeting recorder).
- `/log [name]`: manual 1-on-1 log (if you don't use a meeting recorder).
- `/weekly`: drafts a weekly update from the week's activity (if you write weeklies).
- `/review [name]`: performance review draft (if you do formal reviews).
- `/coach [name]`: tough feedback prep (if feedback delivery came up as a pain point).

## Integrations

The wizard generates `context/integrations.md` listing every tool you named, with the setup link or install command for each one. When a slash command needs an integration that isn't wired up yet, it points you at that file instead of silently degrading. Wire what you need, when you need it.

## How to update

Paperwork Setup ships changes upstream over time: new commands, better question banks, refined references. Your instance is yours to edit, so updates are opt-in, never forced.

Run `/paperwork-update` inside your instance. It will:

1. Read the SHA in `.claude/paperwork-version` to know what version you are on.
2. Fetch the latest upstream SHA from `nobodyiscertain/paperwork-setup`.
3. Diff the two and group changes into cards: one card per user-facing file or coherent feature.
4. Walk the cards interactively, one at a time. For each, you get a short summary and a Y / Skip / Quit prompt. Default is Skip.
5. Three-way merge any change you accept against your edits, so your customizations survive.
6. Write the new SHA to the install marker when the wizard finishes cleanly.

`/paperwork-update` is idempotent. Re-running picks up where you left off. It never touches your `README.md`, `CLAUDE.md`, or anything you've written under `people/`, `partners/`, `leadership/`, `journal/`, `decisions/`, `bragdoc/`, `meetings/`, `weeklies/`, or `library/`. Those are yours.

To reconfigure an existing install (turn the dashboard on, add new commands, change your manager profile), run `/paperwork-setup`. It runs the wizard again against your current files instead of starting from scratch.

## How it actually works

Paperwork Setup is a single prompt (`PAPERWORK.md`) plus an MIT license. Your agent fetches that prompt, runs the interview, and generates files into the current directory. Everything after install is regular files. No background process, no SaaS, no telemetry.

The install marker at `.claude/paperwork-version` records the upstream SHA your instance was generated from. `/paperwork-update` reads that marker to compute the upgrade path the next time you run it.

## Coaching

The wizard gets you most of the way. If you want hands-on help getting it set up, debugging your first week, or dialing it in after a month of real use, [book a coaching session](https://everyexpert.com/nobodyiscertain).

## Privacy

Your instance lives on your machine. There's no server, no telemetry, nothing sent upstream. The agent reads your files locally and writes back locally.

When you note something a teammate would not want a peer to read, mark the entry `(sensitive)` and the agent skips it on team-wide summaries.

If you push the repo somewhere, push it private. Names and notes belong to you.

## Built by

[Jamie Wagner](https://nobodyiscertain.com), figuring out how to manage a 30-person org with AI in real time and sharing what works.

## License

MIT
