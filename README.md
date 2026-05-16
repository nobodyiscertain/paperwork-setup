# Paperwork Setup

**AI handles the paperwork. You handle the humans.**

Paperwork Setup is a one-shot wizard that builds your personal management system into the current directory. It interviews you for about 20 minutes, then generates an instructions file your AI agent reads, slash commands wired to your tools, question banks tuned to your team, a signal framework, an integrations guide for any tool you have not wired yet, an optional dashboard that opens on its own, and a human-readable README so future you (or a teammate) can pick up the repo without an explanation.

It is not a template you fill in. It is a conversation that builds a system. The system does the file work. You do the people work.

## Install

Open your AI coding agent in an empty directory where you want the system to live. Paste this prompt:

```
Set up my personal management system using Paperwork Setup. Begin by fetching
this URL and reading it completely:

https://raw.githubusercontent.com/nobodyiscertain/paperwork-setup/main/PAPERWORK.md

Then follow the instructions inside, starting with the interview. Build the
system in the current directory.
```

The wizard asks you about your team shape, your tools, your cadence, your philosophy, and your pain points. One question at a time, with an upfront count, so you know how long it will run. Expect 15 to 20 minutes.

When the interview ends, the system writes itself. The dashboard (if you said yes to one) opens in your browser. You get three things to do next, not five.

Works with any agent that can fetch a URL and write files: Claude Code, Codex, Cursor, OpenClaw, and most others. Chat UIs without filesystem access (ChatGPT, Claude.ai) cannot generate the system locally.

## Your first week

You do not duplicate folders. You do not copy templates. The commands handle file work.

**Monday morning. `/sod`.**
You open Claude and run `/sod`. It reads your calendar, runs `/prep` for every meeting on the day, writes a briefing, and refreshes the dashboard tab. By week two, the prep cards pull useful context from your earlier 1-on-1 notes.

**Midweek. `/sync` or `/log` after a 1-on-1.**
If you record meetings, `/sync` routes the transcript into the right person's `one-on-ones.md` and asks you once if a new name should get a folder. If you do not record meetings, `/log [name]` lets you dump notes and Claude structures them. Either way, the file work happens for you.

**Friday. `/weekly` or `/health`.**
`/weekly` reads the week's 1-on-1 notes and team activity and drafts an update in your voice. `/health` gives you a team snapshot: who is green, yellow, red, whose cadence has slipped, open promises you owe. Pick whichever your job actually calls for.

That is the loop. `/think`, `/prep`, `/new`, `/review`, `/coach`, and `/prune` round out the toolkit; you reach for them when you need them.

## What you get

After the conversation, your repo looks like this:

| Path | What it is |
| --- | --- |
| `README.md` | Your instance's orientation doc. Customized from your interview answers. |
| `CLAUDE.md` | The agent's instructions. Your philosophy, your success framework, your tool map. |
| `people/[first-last]/` | Created lazily by `/new` or the optional bulk bootstrap. Profile, 1-on-1 log, feedback log. |
| `references/` | Question banks, signal framework, success framework, feedback guide, integrations guide. |
| `dashboard/` | Optional. Single HTML file that auto-opens after install. |
| `meetings/`, `weeklies/` | Optional. Routed by `/sync` and `/weekly`. |
| `.claude/commands/` | Slash command definitions. |
| `.claude/paperwork-version` | Install marker. Used by `/paperwork-update`. |

Slash commands available in your instance:

- `/sod` and `/eod`: start and end of day routines
- `/sync`: routes meeting notes to the right place, scaffolds new people as they come up
- `/prep`: prep for a 1-on-1 or recurring meeting
- `/weekly`: drafts a weekly update from the week's activity
- `/think`: open-ended thinking partner mode
- `/new`: adds a direct report or partner and scaffolds their directory
- `/health`: team health snapshot
- `/prune`: living-system maintenance
- `/paperwork-update`: pull opt-in updates from upstream Paperwork Setup
- `/paperwork-setup`: re-run the configuration wizard against an existing install

Optional commands (`/log`, `/review`, `/coach`) appear only if your interview answers warrant them.

## Tools and integrations

The wizard asks you what tools you use. For each one, you tell it whether you already have a Claude integration installed, want one wired now, or want to leave it as manual reference. After install, `references/integrations.md` lists every tool you named with copy-pasteable setup steps and a one-liner of what you get when the wiring lands. When `/prep` or `/sync` hits a tool that is still manual, it points you at that file instead of silently degrading.

## How to update

Paperwork Setup ships changes upstream over time: new commands, better question banks, refined references. Your instance is yours to edit, so updates are opt-in, never forced.

Run `/paperwork-update` inside your instance. It walks each change as a yes / skip card, applies opt-ins via a three-way merge so your local edits survive, and updates the install marker on clean exit. Re-running picks up where you left off. It never touches your `README.md`, `CLAUDE.md`, or anything under `people/` or `meetings/`.

To reconfigure an existing install (turn the dashboard on, add new commands, change your manager profile), run `/paperwork-setup`. It runs the wizard against your current files instead of starting from scratch.

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
