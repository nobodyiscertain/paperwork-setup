# Paperwork

**AI handles the paperwork. You handle the humans.**

Paperwork is a one-shot setup prompt that builds your personal management system. It interviews you about how you actually manage, then generates a complete working setup in your current directory: an instructions file your AI agent reads, slash commands wired to your tools, question banks tuned to your team, a signal framework, optional dashboard, and a starter directory for every person and partner you work with.

It isn't a template you fill in. It's a conversation that builds a system.

## Quick Start

Open your AI coding agent in an empty directory where you want your management system to live. Paste this prompt:

```
Set up my personal management system using Paperwork. Begin by fetching this
URL and reading it completely:

https://raw.githubusercontent.com/nobodyiscertain/paperwork-setup/main/PAPERWORK.md

Then follow the instructions inside, starting with the interview. Build the
system in the current directory.
```

Works with any agent that can fetch a URL and write files: Claude Code, Codex, Cursor, OpenClaw, and most others. Chat UIs (ChatGPT, Claude.ai) without filesystem access won't be able to generate the system locally.

**Time:** 15-20 minutes for the conversation. Generation is instant.

## What You Get

After a focused conversation, Paperwork generates:

- **CLAUDE.md** that teaches your AI agent how *you* manage. Your philosophy, your success framework, your tool map. The brain of the system.
- **Slash commands** tuned to your tools and rhythm. Core set is light. /sod, /eod, /sync, /weekly, /think, /prep, /new. More if your interview answers warrant it.
- **People directories** for direct reports, cross-functional partners, and upward relationships. Each report gets a profile, 1-on-1 log, and feedback log.
- **Question banks** weighted toward your stated pain points and team type.
- **Signal framework** for catching problems early, derived from what you said you actually watch for.
- **Optional dashboard**: a single HTML file you open in your browser, showing your day, your team's pulse, and whatever else you said you'd want at a glance. Refreshes when you tell it to.
- **A starter git repo** if you want one. Keeps your notes versioned and your changes traceable.

## Who It's For

Managers of any function. Engineering, product, design, ops, sales, support, customer success. The interview adapts to your stack.

You probably want this if:
- You have direct reports and feel like things fall through the cracks
- You can't remember what you talked about in last month's 1-on-1
- Performance review season is a slog
- You already use AI coding agents but haven't set them up for management
- You want a real system, not a Notion template

You probably don't want this if:
- You don't have direct reports yet
- You're looking for a SaaS dashboard, not a file-based system
- You want someone else to manage your people for you

## What It Isn't

- Not a SaaS. Files on your machine. You own them.
- Not opinionated about how you should manage. It encodes how you *do* manage.
- Not a one-size template. The interview drives generation.
- Not a replacement for being present with your people. It handles the paperwork so you have time for the humans.

## Coaching

The system gets you most of the way. If you want hands-on help getting it set up, debugging your first week, or dialing it in after a month of real use, [book a coaching session](https://everyexpert.com/nobodyiscertain).

## Built By

[Jamie Wagner](https://nobodyiscertain.com), figuring out how to manage a 30-person org with AI in real time and sharing what works.

## License

MIT
