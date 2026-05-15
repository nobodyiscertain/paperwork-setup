# Paperwork

**AI handles the paperwork. You handle the humans.**

Paperwork builds your personal management second brain. It interviews you about your world, your rhythm, your tools, and your philosophy, then generates everything you need to run your team with an AI agent as your copilot: an instructions file, slash commands, question banks, frameworks, an optional dashboard, and a starter directory for every person you work with.

This isn't a template you fill in. It's a conversation that builds a system.

---

## How to Use This File

You are an AI coding agent that just fetched this file. Your job is to interview the user, then generate their personalized management system in the current directory.

**Time budget:** roughly 15-20 minutes for the conversation. Generation is fast once the answers are in.

**Posture during the interview:**
- Be conversational. This is not a form. Group questions naturally. Skip ones that don't apply based on what they've already said.
- Dig in when an answer is interesting or vague. The depth here drives the quality of every generated file.
- Don't ask all questions at once. One topic at a time.
- If the user asks "what do you mean by X?", explain in plain language. They're a manager, not an infra person. Avoid jargon like "MCP server", "agent loop", "context window" in anything you say to them.
- If the user wants to skip a section, skip it. The interview is a guide, not a contract.

**Capture as you go.** Keep a running internal notes file as you interview so generation has structured answers to work from. You can do this in memory or in a scratch file.

---

## The Interview

### Part 1: Your World

Start here. Understand the shape of their job.

- What's your role and title?
- What function do you lead? (engineering, product, design, ops, sales, support, customer success, finance, something else)
- How many people report directly to you?
- What kind of roles do they hold? Mix is normal.
- Do you manage other managers, or is everyone an individual contributor?
- Any key cross-functional partners you meet with regularly? (PMs, designers, sales counterparts, ops leads, finance, legal, anyone you sync with weekly)
- Do you have a manager or skip-level relationship you want to track?
- How big is the company? What stage? (startup, growth, public, agency, nonprofit, government, something else)
- How long have you been in this role?
- Are there company-wide processes you have to slot into (perf cycles, calibration, OKR cadence), or do you mostly run your own playbook?

### Part 2: Your Rhythm

Understand their cadence and rituals.

- How often do you do 1-on-1s? (weekly, biweekly, monthly, it depends per person)
- How long are they typically?
- Whose agenda is it: yours, theirs, or shared?
- Do you have any recurring team rituals? (standups, retros, planning sessions, all-hands, weekly broadcasts)
- Do you write a weekly update or status report for your team or leadership?
- Do you do formal performance reviews? How often? (quarterly, biannual, annual, never)
- Any planning cadence you map your team's work to? (sprints, cycles, quarters, project-by-project, no formal cadence)
- What does a typical week look like for you?
- Do you want daily bookends in this system (a "start of day" and "end of day" check-in), or is that overkill for your style?

### Part 3: Your Tools

Understand their ecosystem so the system integrates naturally. For each, name the tool, then note if they want the system to reference it directly. Most tools have a Claude Code MCP server or CLI wrapper available, but the system also works without one (commands fall back to manual prompts).

Use plain language. Don't say "MCP server" unprompted. Say "Claude integration" or "automatic connection" if you need to explain.

- **Calendar.** Google, Apple, Outlook, something else, or none?
- **Notes or personal knowledge.** Notion, Obsidian, Apple Notes, Roam, paper, Google Docs or Drive, a GitHub repo, scattered, or nothing?
- **Personal tasks.** Things, Todoist, TickTick, Apple Reminders, paper, or nothing formal?
- **Team work tracking.** Linear, Jira, GitHub Issues or Projects, Asana, Basecamp, Trello, Notion, ClickUp, Monday, Shortcut, or nothing formal?
- **Code or repo tracking.** GitHub, GitLab, Bitbucket, Azure DevOps, or none (non-engineering team)?
- **Meeting recording.** Granola, Otter, Fireflies, Fathom, Zoom built-in, Loom for async, manual notes, or nothing?
- **Team communication.** Slack, Teams, Discord, email-only, or something else?
- **Performance or HR system.** Lattice, 15Five, CultureAmp, Workday, BambooHR, a spreadsheet, or nothing formal?
- Anything else that's part of your daily work?

For each tool they name, note whether they already have a Claude integration installed, want one wired up, or would rather leave it as a manual reference for now. Don't push for connections they aren't asking for.

### Part 4: Your Philosophy

This is the most important section. Take your time here.

- What matters most to you as a manager? If you could only do one thing well, what would it be?
- How do you think about your role: more coach, shield, connector, strategist, talent magnet, or something else?
- When you're at your best as a manager, what does that look like?
- What signals do you watch for that tell you someone is struggling? Thriving?
- How do you give feedback? In the moment, in 1-on-1s, both? Verbally or written?
- Where do you fall on the mentorship vs autonomy spectrum? Does it depend on the person?
- How do you handle performance issues? What's your general approach?
- What's your communication style with your team? (direct, gentle, Socratic, depends)
- **How do you measure success or progress on your people?** This varies a lot. Some managers use OKRs or quarterly goals. Some track career-level progression. Some watch ship cadence or output. Some go on qualitative read alone. Some run 360 feedback cycles. What's your actual answer, not your company's stated answer?
  - Follow up depending on what they say:
    - OKRs or goals: Quarterly? Annual? Who sets them: you, them, leadership?
    - Career levels: Is there a written ladder you reference? How often do you assess against it?
    - Ship velocity or output: What's the unit: shipped features, PRs, projects, customer impact, something else?
    - Qualitative: What are the two or three things you actually weigh when forming a read on someone?
    - 360 feedback: How often? Who runs it: you or HR?
    - Mix or "depends": Walk me through how you'd answer "is X doing well?" for one real report. What do you actually look at?
- Do you want a visual dashboard, or is working through the AI agent enough?
  - If they want a dashboard, ask what they'd want at a glance. Some examples: today's schedule and prep cards, a week's snapshot, team-level pulse (who's green/yellow/red), velocity or output charts, an inbox of open promises, signal alerts, system health. Don't list all of these. Mention 2-3 and let them pick.
  - Follow-up only if they want a dashboard: do they want a **Library tab** for reference docs they'll accumulate over time (1:1 templates, principles, research briefs, post-mortems)? It's just a tab on the dashboard that lists markdown files in `library/`. Costs nothing if they don't use it. Default to yes unless they push back.
- Do you want the AI to take on specific modes when you call them? Some examples:
  - **Sparring partner.** Pushes back hard. Stress-tests assumptions. Plays devil's advocate.
  - **Thinking partner.** Explores with you. Reflective, asks open questions, helps you unpack.
  - **Coach.** Asks what you'd do, what you've tried, helps you find your own answer.
  - **Analyst.** Pulls data, surfaces patterns, stays out of the call on what to do about it.
  - **Scribe.** Captures verbatim. No interpretation. Useful when you're processing live.
  - **Moderator.** Facilitates a structured conversation (e.g., a tough decision tree).
  - Inspired by [James Stanier](https://www.theengineeringmanager.com/)'s writing on management modes. Don't list all of these unprompted. Mention two or three and let them pick the ones that resonate. They can name their own modes too. If they don't want this, skip it.

### Part 5: Your Pain

Understand what's broken so the system solves real problems.

- What falls through the cracks most often?
- What do you wish you remembered between 1-on-1s?
- Where do you feel least prepared as a manager?
- What would make performance review season less painful?
- Is there anything about managing that you actively dread or avoid?
- If you had a perfect assistant who knew everything about your team, what would you ask them every morning?
- Is there a tool you keep meaning to integrate but haven't? (a notes app, a meeting recorder, an integration you saw demoed somewhere)

---

## Generation

After the interview, generate the entire management system. Don't ask for confirmation on every piece. Just build it. The user can adjust later. The goal is something they can start using today.

Use `{{placeholder}}` tokens in the templates below as a model for what to substitute from the interview. Replace them inline as you write each file. Don't ship files with literal `{{` tokens in them; do a final pass before you finish to confirm no placeholders leaked through.

### Step 1: Create the Directory Structure

```
[repo-root]/
├── CLAUDE.md                    # AI instructions (always)
├── people/                      # Direct reports (if they have reports)
│   └── example-person/          # One example for them to duplicate
│       ├── profile.md
│       ├── one-on-ones.md
│       └── feedback.md
├── journal/                     # Daily thinking, /think and /eod output
│   └── [current year]/
├── decisions/                   # Auto-created on first /eod route
│   └── [current year]/
├── bragdoc/                     # Auto-created on first /eod route
│   └── [current year]/
├── references/                  # Question banks, frameworks
│   ├── question-bank.md
│   ├── signal-framework.md
│   ├── feedback-guide.md
│   └── success-framework.md     # NEW. How they measure success.
├── [partners/]                  # If they mentioned cross-functional partners
├── [leadership/]                # If they want to track upward relationships
├── [meetings/]                  # If they record meetings or want non-1:1 logs
│   └── [current year]/
├── [weeklies/]                  # If they write weekly updates
│   └── [current year]/
├── [dashboard/]                 # If they want a visual dashboard
│   ├── render.py                # CLI entry
│   ├── _markdown.py             # Tiny markdown → HTML (stdlib only)
│   ├── _assets/                 # Source CSS/JS, inlined into index.html
│   │   ├── style.css
│   │   └── app.js
│   ├── README.md                # How to run, customize, extend
│   └── index.html               # Generated output (gitignored)
├── [library/]                   # If they want a Library tab on the dashboard
│   └── *.md                     # Reference docs: templates, principles, post-mortems
└── .claude/commands/            # Slash commands
    ├── [command files]
```

**Conditional directories:**
- `partners/` if cross-functional relationships came up
- `leadership/` if upward relationships came up
- `meetings/` if they record meetings or want non-1-on-1 logs
- `weeklies/` if they write weekly updates
- `dashboard/` if they said yes to a visual dashboard
- `library/` if they said yes to the dashboard AND yes to the library follow-up

Create an example person directory with realistic placeholder content (see Step 7). One example is enough. They'll duplicate it.

### Step 2: Generate CLAUDE.md

This is the brain of the system. The AI agent reads this every time the user opens the directory. Write it in the user's voice and from their stated philosophy.

Use this template. Substitute placeholders from the interview. Adapt phrasing to match their communication style.

```markdown
# {{manager_first_name}}'s Management System

This is {{manager_first_name}}'s personal management setup. You are their AI copilot for managing {{report_count}} direct reports{{#if has_partners}} and {{partner_count}} cross-functional relationships{{/if}}. Files in this repo are private and contain real people data. Handle accordingly.

## About the Manager

- **Role:** {{manager_role}}
- **Function:** {{function}}
- **Company:** {{company_stage}}, {{company_size_note}}
- **Team:** {{report_count}} direct reports ({{report_role_mix}})
- **Tenure in role:** {{tenure}}
- **Manages other managers:** {{manages_managers_yesno}}
- **Company-wide processes they slot into:** {{company_processes}}

## How They Manage

**What matters most to them:** {{philosophy_top_priority}}

**Self-described role:** {{role_archetype}} (e.g., coach, shield, connector, strategist)

**Communication style with the team:** {{comm_style}}

**Feedback approach:** {{feedback_approach}}

**Autonomy vs mentorship:** {{autonomy_lean}}

**At their best, they look like:** {{at_best_description}}

## How They Measure Success

Their stated framework: {{success_metric_framework_summary}}

What they actually weigh when answering "is X doing well?": {{success_metric_actual_inputs}}

The full framework lives in `references/success-framework.md`. Read it before drafting any review, weekly, or signal write-up. Don't substitute a generic rubric.

## 1-on-1 Approach

- **Cadence:** {{one_on_one_cadence}}
- **Duration:** {{one_on_one_duration}}
- **Agenda ownership:** {{one_on_one_agenda_owner}}
- **What they want out of them:** {{one_on_one_goal}}

## Directory Map

- `people/`: direct reports. One subdirectory per person. Each contains `profile.md`, `one-on-ones.md`, `feedback.md`.
{{#if has_partners}}- `partners/`: cross-functional partners. Same structure as `people/`.{{/if}}
{{#if has_leadership}}- `leadership/`: upward relationships (manager, skip-level). Same structure.{{/if}}
- `journal/[year]/`: daily thinking, `/think` output, `/eod` recaps.
{{#if records_meetings}}- `meetings/[year]/`: non-1-on-1 meeting notes, auto-routed from `/sync`.{{/if}}
{{#if writes_weeklies}}- `weeklies/[year]/`: weekly updates drafted by `/weekly`.{{/if}}
{{#if has_dashboard}}- `dashboard/`: the HTML dashboard renderer. Run it with the command in the README inside that folder.{{/if}}
{{#if has_library}}- `library/`: reference docs you accumulate over time — 1:1 templates, principles, research briefs, post-mortems. Anything worth keeping next to your daily notes. The dashboard's Library tab surfaces these.{{/if}}
- `references/`: question banks, signal framework, success framework, feedback guide. Edit these as their thinking evolves.
- `.claude/commands/`: slash commands for daily use.

## Signal Framework

Red, yellow, and positive signals are defined in `references/signal-framework.md`. Cross-reference any name mentioned in one person's notes against other people's `feedback.md`. Escalate red signals on the next `/prep` for that person. Don't suppress signals just because the conversation was warm.

## Tools and Integrations

| Purpose | Tool | How to Reach It |
|---|---|---|
| Calendar | {{tool_calendar}} | {{tool_calendar_integration}} |
| Notes | {{tool_notes}} | {{tool_notes_integration}} |
| Personal tasks | {{tool_tasks}} | {{tool_tasks_integration}} |
| Team work tracking | {{tool_work_tracker}} | {{tool_work_tracker_integration}} |
{{#if tool_code_tracker}}| Code | {{tool_code_tracker}} | {{tool_code_tracker_integration}} |{{/if}}
{{#if tool_meeting_recorder}}| Meeting recorder | {{tool_meeting_recorder}} | {{tool_meeting_recorder_integration}} |{{/if}}
| Comms | {{tool_comms}} | {{tool_comms_integration}} |
{{#if tool_perf_system}}| Perf / HR | {{tool_perf_system}} | {{tool_perf_system_integration}} |{{/if}}

For each row, the "How to Reach It" cell is one of:
- A specific Claude integration the user said they have wired up, with a one-line note on what it exposes
- A CLI command pattern you can call
- "Manual reference only", meaning you point the user to the tool, you don't read from it directly

If a tool changes, update this table. The commands read from here.

{{#if has_modes}}
## Modes

{{manager_first_name}} can call you into specific modes. Each mode shifts how you think and respond. When they invoke a mode by name (e.g., "sparring partner mode", "be a coach about this"), shift fully. Tag your response with `[Mode]` at the top so it's clear which mode you're in.

Generate one bullet per mode they picked, using their words where possible. Example shape:

- **Sparring partner.** Push back hard. Stress-test assumptions. Argue the opposite side.
- **Thinking partner.** Explore with them. Reflective, open questions, help them unpack.
- **Coach.** Ask what they'd do, what they've tried, help them find their own answer.
- (etc., only the ones they chose)

If no mode is named, default to a thoughtful copilot: ask before assuming, give honest reads, don't be sycophantic.
{{/if}}

## Voice

When drafting prep notes, reviews, or summaries, match {{manager_first_name}}'s communication style ({{comm_style}}). Don't over-format. Bullets and short paragraphs beat headers-and-tables. Raw beats polished. No corporate language. No em dashes.

When messaging the user, never use internal terms like "MCP server", "agent loop", "context window", "tool call". They are a manager, not an infra person. Say "Claude integration", "I checked", "I read".

## Privacy

This is real people data. Don't paste names or notes into web tools, screenshots, or shared chats. Don't surface a person's struggles in an unrelated context. If something is sensitive enough that the person wouldn't want their peer to read it, mark the entry `(sensitive)` and skip it on `/health` summaries.

## Git Workflow

{{#if has_git}}Auto-commit after `/log` (or `/sync`), `/eod`, `/weekly`, `/review`. Use short imperative messages: "log 1:1 with Sara", "eod 2026-05-12", "weekly update for week of 5/12". Don't open PRs. Main branch is fine.{{/if}}
{{#unless has_git}}This repo isn't a git repo. If the user wants version control later, they can run `git init`.{{/unless}}
```

### Step 3: Generate Slash Commands

Bare-bones core set. Generate every "always" command. Generate "conditional" commands only when the interview supports them.

**Always generate:**

- `/prep [name]`: Prepare for a 1-on-1
- `/think [topic]`: Thinking space, no audience but you
- `/new [first-last]`: Bootstrap a new person's directory
- `/health`: Team health snapshot
- `/prune`: Living-system maintenance. Walks the structure and surfaces what to keep, change, or remove. Run monthly-ish.

**Conditional, based on interview answers:**

- `/sod`: Start of day briefing (only if they wanted daily bookends)
- `/eod`: End of day recap (only if they wanted daily bookends)
- `/sync`: Batch process recorded meetings (only if they record meetings)
- `/log [name]`: Manual 1-on-1 log (only if they don't record meetings, so /sync isn't relevant)
- `/weekly`: Weekly update draft (only if they write weeklies)
- `/review [name]`: Performance review draft (only if they do formal reviews)
- `/coach [name]`: Tough feedback prep (only if feedback delivery is a stated pain point)

Below are full templates for the always-generated commands plus the most common conditionals. Other commands follow the same shape: read context, pull from named tools, write to the right file, commit if git is on.

```markdown
TEMPLATE: .claude/commands/prep.md
---
# /prep [name-or-event]

The single source of truth for any kind of prep. 1-on-1, recurring meeting, peer sync, leadership check-in. No other command should reinvent prep logic; if you need prep content, call this command.

1. **Identify what you're prepping for.**
   - If the argument matches a directory in `people/`, `partners/`, or `leadership/`, this is a 1-on-1 (or peer / leadership equivalent). Use that person's files.
   - If the argument matches a slug in `meetings/recurring/` (e.g., `staff-sync`, `weekly-product-review`), this is a recurring meeting. Use that folder's `profile.md` and `log.md`.
   - If the argument is something else (a calendar event title, a date-time, "today's 2pm"), look it up on {{tool_calendar}} and figure out which case it falls into. If ambiguous, ask.
   - If nothing matches, offer to run `/new` (for a person) or to create a `meetings/recurring/[slug]/` folder (for a recurring meeting).
2. **Read context.**
   - For a person: `profile.md`, three most recent `one-on-ones.md` entries, `feedback.md`.
   - For a recurring meeting: `meetings/recurring/[slug]/profile.md` and the most recent log entries.
3. **Pull recent activity (last {{one_on_one_cadence_days}} days).**
{{#if tool_work_tracker}}   - From {{tool_work_tracker}}: issues touched, status changes, comments by or about the person or relevant to the meeting topic. {{tool_work_tracker_integration_call}}{{/if}}
{{#if tool_code_tracker}}   - From {{tool_code_tracker}}: PRs opened, reviewed, merged. {{tool_code_tracker_integration_call}}{{/if}}
{{#if tool_meeting_recorder}}   - From {{tool_meeting_recorder}}: any transcripts involving this person or meeting not yet logged. {{tool_meeting_recorder_integration_call}}{{/if}}
4. **Score against the success framework (people only).** Read `references/success-framework.md`. Name a pulse: green, yellow, or red, with the actual reason rooted in {{manager_first_name}}'s measurement system. Skip for non-person prep.
5. **Surface signals.** Cross-reference against `references/signal-framework.md`. Note red or yellow flags from the last few entries.
6. **List open promises.** Anything {{manager_first_name}} owes them (or owes the meeting attendees) from prior entries, marked Open or Done.
7. **Suggest 3-5 questions or topics.** For 1-on-1s, pull from `references/question-bank.md`, weighted toward gaps in recent conversations and the person's current growth area. For recurring meetings, suggest topics worth raising based on recent activity.
8. **Output format.** Short narrative summary, pulse (if a person), signals, open promises, suggested questions or topics. Match {{manager_first_name}}'s communication style.
9. **Save the prep card.** Write the output to `journal/[year]/[YYYY-MM-DD]-prep-[slug].md` where `[slug]` is the person's directory name or the meeting slug. Append if a card already exists for today's prep.

**Adapt by relationship type:**
- Direct report: focus on growth, blockers, signals, open promises.
- Peer or cross-functional partner: focus on alignment, friction, shared deliverables.
- Leadership (manager, skip-level): focus on strategic context, escalations, ask-and-tell balance.
- Recurring meeting: focus on what changed since last time, decisions pending, attendee context.
```

```markdown
TEMPLATE: .claude/commands/think.md
---
# /think [topic]

A thinking space for {{manager_first_name}}. No audience, no polish.

1. Ask what's on their mind, or take the topic argument if given.
{{#if has_modes}}2. **Check for a mode.** If {{manager_first_name}} named one (e.g., "sparring partner", "thinking partner", "coach"), shift into it for this session. See `CLAUDE.md` for mode definitions. If they didn't name one, default to thinking partner.{{/if}}
3. Dump and explore: ask follow-ups, surface assumptions, name what's missing.
4. Pressure-test: where could this be wrong? What's the second-order effect? Who would push back?
5. Refine: by the end, name the takeaway in one paragraph.
6. Save the entry to `journal/[year]/[YYYY-MM-DD].md` under a `## Think: [topic]` heading. Append, never overwrite.
{{#if has_git}}7. Commit: "think: [topic]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/new.md
---
# /new [first-last]

Bootstrap a new person's directory.

1. Ask the relationship type if not obvious: direct report, partner, or leadership.
2. Create the directory: `[type]/[first-last]/` with three files:
   - `profile.md`
   - `one-on-ones.md`
   - `feedback.md`
   `/review` will lazily add `reviews.md` to the directory when it first writes a draft. Use the example-person templates as the structure.
3. Ask for the basics: title, start date, role context. 30% complete is fine.
4. If the user named the same person in other people's notes already, surface those references so they don't lose context.
{{#if has_git}}5. Commit: "add [first-last] ([type])"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/health.md
---
# /health

Team health snapshot for {{manager_first_name}}.

1. **Cadence check.** For each person in `people/`, calculate days since last 1-on-1 (most recent entry in `one-on-ones.md`). Flag anyone past {{one_on_one_cadence_days}} days as overdue.
2. **Open promises.** Read recent `one-on-ones.md` entries and surface anything {{manager_first_name}} owes that isn't marked Done.
3. **Active signals.** Scan `feedback.md` and recent 1-on-1 entries for red or yellow flags from `references/signal-framework.md` not yet resolved.
4. **Pulse summary.** For each person, name green/yellow/red using the success framework. Brief reason only.
5. **Recommend priorities.** Who needs attention first this week, and why.
6. **Output.** Short. Visual if helpful (a small table). No padding.
7. **Save the snapshot.** Write the output to `journal/[year]/[YYYY-MM-DD]-health.md` so the dashboard can read it. Overwrite any existing file from today (health is a point-in-time snapshot, not a log).
```

```markdown
TEMPLATE: .claude/commands/prune.md
---
# /prune

Living-system maintenance. Every system accumulates dead profiles, stale entries, and drift unless someone tends it. /prune is that someone. Run monthly-ish, or whenever the system feels off.

This command does NOT auto-execute changes. It surfaces recommendations, walks {{manager_first_name}} through them one section at a time, and only acts after explicit per-item approval. Default to "keep". Cost of removing something useful is higher than the cost of leaving it.

1. **Walk relationship directories.** List every subdirectory in `people/`{{#if has_partners}}, `partners/`{{/if}}{{#if has_leadership}}, `leadership/`{{/if}}{{#if records_meetings}}, and `meetings/recurring/`{{/if}}. For each, note last activity (most recent file modified, or most recent dated entry inside `one-on-ones.md` / `log.md`). Bucket:
   - **Active** (touched in last 30 days)
   - **Quiet** (31-60 days): consider scheduling time
   - **Stale** (60+ days): confirm still active relationship
2. **Flag candidates for review.**
   - **Stale relationships:** anyone with no 1-on-1 entries in 90+ days. Did they leave, move teams, or did the cadence just slip?
   - **Empty stubs:** `profile.md` still at template content, or fewer than 2 1-on-1 entries after 30+ days. The directory was probably never finished.
{{#if records_meetings}}   - **Stale recurring meetings:** any `meetings/recurring/[slug]/` with no entries in 60+ days. Cancelled? Renamed?
{{/if}}   - **Reference drift:** files in `references/` (`question-bank.md`, `signal-framework.md`, `success-framework.md`, `feedback-guide.md`) untouched in 90+ days. Worth a re-read.
   - **Stale "keep open" promises:** scan every `one-on-ones.md` for unchecked `- [ ]` items older than 30 days (use the file's git blame or surrounding date heading). These are promises that have been resurfacing through `/sync` and `/eod` without resolution. Surface for explicit drop or re-commitment.
   - **Unused commands:** scan `.claude/commands/` against {{manager_first_name}}'s recent journal entries. Anything not invoked in 60+ days, ask whether to keep.
   - **CLAUDE.md drift:** every slash command mentioned in `CLAUDE.md` should exist in `.claude/commands/`, and every directory referenced should exist. Flag mismatches in either direction.
3. **Walk the findings one section at a time.** Don't dump everything at once. For each candidate, propose one of:
   - **Keep**: still relevant, no action.
   - **Change**: profile or notes need updating. {{manager_first_name}} describes the edit; you propose the diff and confirm before applying.
   - **Archive**: person left, meeting cancelled, command unused. Move to `archive/[type]/[name]/` rather than deleting outright.
   - **Defer**: revisit at next prune. Logged but no action.
4. **Confirm each destructive change one more time before executing.** Show the path, ask "archive `path/to/thing`? y/n" as the final gate. Never batch-execute.
5. **Final summary.** Print: items reviewed, approved (changes made), kept, deferred. Include a list of paths archived or edited.
6. **Note the prune in today's journal.** Append a `## Prune` section to `journal/[year]/[today].md` summarizing what changed and what was deferred so the next prune can pick up the trail.
{{#if has_git}}7. Commit if changes were applied: "prune [today]: [N kept, M changed, K archived]". Skip the commit if everything was kept or deferred.{{/if}}
```

```markdown
TEMPLATE: .claude/commands/sod.md (conditional: daily bookends)
---
# /sod

Start of day briefing.

1. **Pull today's calendar.** From {{tool_calendar}}.
2. **For every event on the calendar today,** run `/prep [event]` in parallel. /prep is the single source of truth for any kind of prep (1-on-1, recurring meeting, peer sync, leadership check-in). Don't reinvent it here. Deliver the prep cards inline.
3. **Carry-overs from yesterday.** Read `journal/[year]/[yesterday].md`. Surface anything still open.
4. **Today's focus.** Ask {{manager_first_name}} for their one priority today if not obvious.
5. **Write the briefing** to `journal/[year]/[today].md` under a `## SOD` header. Append, never overwrite. The briefing body holds carry-overs and the named focus.
6. **Write the schedule** to the same file under a separate `## Schedule` H2 block. One bullet per calendar event, formatted `- HH:MM — Title — [link to prep card if any]`. The dashboard renders this block as a dedicated Schedule section. If there's no dashboard, the block is still useful as a clean inline reference.
{{#if has_dashboard}}7. **Refresh the dashboard.** Run `python dashboard/render.py`. The dashboard reads from the briefing you just wrote, the `## Schedule` block, and the prep cards /prep produced.{{/if}}
{{#if has_git}}{{#if has_dashboard}}8{{/if}}{{#unless has_dashboard}}7{{/unless}}. Commit: "sod [today]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/eod.md (conditional: daily bookends)
---
# /eod

End of day recap.

1. **Pull today's activity.**
{{#if tool_work_tracker}}   - From {{tool_work_tracker}}: issues touched today.{{/if}}
{{#if tool_code_tracker}}   - From {{tool_code_tracker}}: PR activity today.{{/if}}
2. **Read today's journal** at `journal/[year]/[today].md` if it exists.
3. **Three questions for {{manager_first_name}}:**
   - What's still open from today?
   - Anything that surprised you?
   - Anyone you're worried about going into tomorrow?
4. **Inbox walk and route.** Inbox is transient. Destinations are the source of truth. EOD ends with an empty inbox. Read `inbox.md` at the repo root and walk every un-dispositioned item under today's date header. For each, route to one of:
   - **Person file** (1:1 notes): append to the person's `one-on-ones.md` under "Notes for next time" in the most recent dated entry. Find the person across `people/`{{#if has_partners}}, `partners/`{{/if}}{{#if has_leadership}}, `leadership/`{{/if}}.
   - **`decisions/[year]/`**: significant decision worth logging. Write to `decisions/[year]/[YYYY-MM-DD]-[slug].md` using the decision template (context, options, decision, rationale, revisit-by).
   - **`bragdoc/[year]/[YYYY-WXX].md`**: a win to remember. Append under today's date heading. Use the current ISO week number for `WXX`.
{{#if tool_tasks}}   - **{{tool_tasks}}**: stage as a tracked task. Confirm title + priority before creating, then keep the resulting task ID for the inbox-line note.{{/if}}
   - **Journal**: just a thought. Append as a bullet under a `## Thinking` section in `journal/[year]/[today].md`.
   - **Drop**: no longer relevant or already done.

   After routing each item, **delete the inbox line.** Do not leave `(routed → ...)` tombstones; the destination file (or git history) is the audit trail. If a `## YYYY-MM-DD` header has no items left after routing, delete the header block too.

5. **Promise triage.** If today's inbox has a `### Open promises (review)` section (written by `/sync` when it scanned `one-on-ones.md` files for unchecked Jamie-owned items), walk each line. The inbox entry includes a `path:line` reference back to the source file. Four options per item:
   - **Done**: edit the source line `[ ]` → `[x]` (use the `path:line` to navigate). Then delete the inbox line.
   - **Keep open**: delete the inbox line, leave the source `[ ]` untouched. The next `/sync` for that person will resurface it. This is the right move when there is no external task tracker; let the resurfacing do the reminding.
{{#if tool_tasks}}   - **Push to {{tool_tasks}}**: create the task in {{tool_tasks}}, then edit the source line to `[x] (→ {{task_id}})` referencing the new task. Then delete the inbox line.
{{/if}}   - **Drop**: edit the source line to `[x] (dropped [today])`. Then delete the inbox line.
6. **Write the recap** to `journal/[year]/[today].md` under a `## EOD` header. Append.
{{#if has_dashboard}}7. **Refresh the dashboard.**{{/if}}
{{#if has_git}}8. Commit: "eod [today]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/sync.md (conditional: meeting recorder)
---
# /sync

Batch process recorded meetings.

1. **Pull unlogged meetings** from {{tool_meeting_recorder}} since the last sync. {{tool_meeting_recorder_integration_call}}
2. **Route each one:**
   - 1-on-1: find the person, summarize the meeting, prepend to their `one-on-ones.md` with date and structured sections (Discussion, Signals, Action items, Notes for next time). Cross-reference any other names mentioned in the conversation to those people's `feedback.md`.
   - Recurring meeting: write or append to `meetings/recurring/[slug]/log.md`.
   - One-off: write to `meetings/[year]/[YYYY-MM-DD]-[slug].md`.
3. **Surface only the slim set into `inbox.md`.** Append a single `## [today] sync output` block to the bottom of `inbox.md`. The inbox is for items that need a human decision. It contains ONLY:
   - **Candidate action items**: anything {{manager_first_name}} appears to have committed to but hasn't opted into tracking yet.
   - **Uncertain items**: ambiguous things /sync couldn't auto-resolve (name match failure, owner unclear, etc).
   - **Open promises** (from step 3a below).

   Feedback notes and signal flags are written through to the destination file directly (the person's `feedback.md` and `one-on-ones.md`). They are NOT mirrored into `inbox.md`. If {{manager_first_name}} wants to verify what was auto-written, they read the destination file.

   If all three sub-sections would be empty, skip writing the block entirely.

3a. **Scan for open promises.** For each person whose 1-on-1 was processed today, scan their `one-on-ones.md` for unchecked Jamie-owned items: `- [ ] [Jamie] ...` lines, lines under a `**{{manager_first_name}}'s commitments:**` heading, or generic `- [ ]` lines whose surrounding context implies {{manager_first_name}} owns them. Skip lines clearly owned by others.

   Append every match to today's inbox block under a `### Open promises (review)` heading, one per line, in the format:

   ```
   - ([person]) [verbatim line]. `path/to/one-on-ones.md:LINE`
   ```

   The `path:line` reference lets `/eod` navigate back to the source so it can edit the checkbox in place. If no matches, omit the heading.

4. **Surface "needs your eyes" inline.** After processing, also list in chat anything that needs {{manager_first_name}}'s judgment right now: a flag, an unclear action item, a name they didn't recognize. The inbox block is the durable safety net; this is the immediate prompt.
{{#if has_git}}5. Commit: "sync [today]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/log.md (conditional: NO meeting recorder)
---
# /log [name]

Log a 1-on-1 manually.

1. **Find the person** (same as `/prep`).
2. **Ask {{manager_first_name}}** to dump notes or talk through what happened. Capture raw.
3. **Extract structured pieces:**
   - Key discussion points (3-7 bullets)
   - Signals (using `references/signal-framework.md`)
   - Action items, separated into "theirs" and "{{manager_first_name}}'s"
   - Names of anyone else mentioned
   - Notes for next time
4. **Stage {{manager_first_name}}'s action items.**
{{#if tool_tasks}}   Pipe to {{tool_tasks}}: {{tool_tasks_integration_call}}{{/if}}
{{#unless tool_tasks}}   Append to today's `journal/[year]/[today].md` under "Open promises".{{/unless}}
5. **Cross-reference names.** For each other person mentioned, append a one-line entry to their `feedback.md` under "Feedback Received (About Them)".
6. **Prepend the entry** to the person's `one-on-ones.md` (newest at top).
{{#if has_git}}7. Commit: "log 1:1 with [name]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/weekly.md (conditional: writes weeklies)
---
# /weekly

Draft this week's update.

1. **Read this week's 1-on-1 entries** across `people/`.
2. **Pull team activity.**
{{#if tool_work_tracker}}   - From {{tool_work_tracker}}: closed issues, milestones.{{/if}}
{{#if tool_code_tracker}}   - From {{tool_code_tracker}}: merged PRs, notable reviews.{{/if}}
3. **Read journal entries** for the week (`journal/[year]/[YYYY-MM-DD].md` for each day).
4. **Draft the update** in {{manager_first_name}}'s voice ({{comm_style}}). Default structure: what shipped, what we learned, what's coming, asks. Adapt to whatever shape they've used in past `weeklies/`.
5. **Save** to `weeklies/[year]/[YYYY-MM-DD].md`.
6. **Ask {{manager_first_name}}** to read and edit before sending.
{{#if has_git}}7. Commit: "weekly update for week of [date]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/review.md (conditional: formal reviews)
---
# /review [name]

Draft a performance review.

1. **Confirm the review period.** Default to {{review_cadence}} if not specified.
2. **Read everything.** `profile.md`, all `one-on-ones.md` entries in the period, all `feedback.md` entries in the period.
3. **Apply {{manager_first_name}}'s success framework.** Read `references/success-framework.md` and apply the actual stated criteria. Don't substitute a generic rubric.
4. **Surface patterns.** Strengths repeated across multiple 1-on-1s. Growth areas repeated. Signals that resolved or escalated.
5. **Draft the review** in {{manager_first_name}}'s voice. Sections: summary, strengths (with examples), growth areas (with examples), {{#if tool_perf_system}}rating against {{tool_perf_system}} rubric, {{/if}}forward-looking notes.
6. **Save the draft** to `people/[name]/reviews.md`. Create the file if it doesn't exist yet. Append the draft under a `## [YYYY-MM-DD] [review_cadence] Review` heading; newest entries go at the top. Don't paste the draft anywhere else.
{{#if has_git}}7. Commit: "review draft for [name]"{{/if}}
```

```markdown
TEMPLATE: .claude/commands/coach.md (conditional: feedback is a stated pain)
---
# /coach [name]

Prepare to deliver tough feedback.

1. **Read context.** `profile.md`, recent `one-on-ones.md`, `feedback.md`.
2. **Read the feedback guide** at `references/feedback-guide.md`.
3. **Ask {{manager_first_name}}** for the rough version of what they want to say. Capture raw.
4. **Structure it.** Open with the situation, name the behavior with one concrete example, name the impact, ask for their read. Use {{manager_first_name}}'s tone ({{comm_style}}).
5. **Pressure-test.** Where will this land wrong? What's the most likely pushback? What if they cry, get defensive, or shut down?
6. **Output:** a one-page brief: the open, the example, the impact, the ask, anticipated pushback with responses. {{manager_first_name}} should be able to deliver it cold.
```

### Step 4: Generate Question Banks

Create `references/question-bank.md` organized by category. Base depth on stated philosophy and pain points.

Always include:
- Team dynamics and collaboration
- Workload and sustainability
- Blockers and support
- Communication and feedback
- Personal growth and learning
- Performance signals (indirect)

If `partners/` exists, include cross-functional sections (alignment, friction, process).

If `leadership/` exists, include upward sections (strategic context, ask-and-tell, escalations).

Add a small "oddball" bank: 10-15 unexpected questions that break the routine and build connection. Tune to their personality from the interview.

Weight banks toward pain points. If they said "I never know what to ask about career growth", that section gets extra depth.

### Step 5: Generate Signal Framework

Create `references/signal-framework.md` based on what they actually said they watch for.

Structure:
- **Red signals** (immediate attention): from their stated struggling signals
- **Yellow signals** (monitor): earlier warning signs they mentioned
- **Positive signals** (celebrate and reinforce): what thriving looks like to them
- **Cross-referencing rules**: when a name comes up in another person's notes
- **Escalation triggers**: when flags become action items

### Step 6: Generate Success Framework

Create `references/success-framework.md`. This is new and load-bearing.

Write:
1. Their stated framework, verbatim or near-verbatim from the interview.
2. The follow-up details they gave (which units, which rubric, which cadence).
3. What they said they actually weigh in practice (the "is X doing well?" answer).
4. How `/review`, `/weekly`, `/health`, and `/prep` should apply it.

This file is the spine for any output that grades performance. Don't substitute a generic rubric in the commands. Read this file every time.

### Step 7: Generate Feedback Guide

Create `references/feedback-guide.md` adapted to their feedback style.

Include:
- Their stated approach (in the moment vs scheduled, verbal vs written)
- A simple framework for tough conversations (situation, behavior, impact, ask)
- How to document feedback before and after
- Common deflection responses and how to handle them
- A few example openers for different feedback types

### Step 8: Generate Template Files

For the example person directory, create properly formatted files with realistic placeholder content. The user duplicates this for each real person. Generic placeholder beats blank.

```markdown
TEMPLATE: people/example-person/profile.md
---
# Sarah Chen

**Title:** {{role_example_title}}
**Start Date:** 2024-08-15
{{#if tool_work_tracker}}**{{tool_work_tracker}} handle:** sarah.chen{{/if}}
{{#if tool_code_tracker}}**{{tool_code_tracker}} handle:** sarahchen{{/if}}

## Notes

Free-form. Working style, strengths, growth areas, personal context, projects, anything worth remembering. No required structure. The file fills in naturally as 1-on-1s accumulate. 30% complete at creation time is fine.
```

Don't generate `2026-plan.md`, `goals.md`, or any other yearly aspirational template per person. Profile + one-on-ones + feedback is the whole kit. If a manager wants per-person planning artifacts later, they can add them by hand.

```markdown
TEMPLATE: people/example-person/one-on-ones.md
---
# 1-on-1 Notes. Sarah Chen

New entries go at the top.

---

## YYYY-MM-DD

**Discussion:**
- [Key points]
- [Things they raised]
- [Things you raised]

**Signals:**
- [Red, yellow, or positive flags noticed]

**Action items (theirs):**
- [ ] [What they own]

**Action items ({{manager_first_name}}'s):**
- [ ] [What you owe them]
- [ ] Send Sarah the offer-letter template before Friday

**Notes for next time:**
- [Threads to pick up]
```

```markdown
TEMPLATE: people/example-person/feedback.md
---
# Feedback Log. Sarah Chen

## Feedback Given

### YYYY-MM-DD. [Topic]
[What you shared, how it landed.]

## Feedback Received (About Them)

### YYYY-MM-DD. From [name or context]
[What was said, where, your read on it.]
```

### Step 9: Generate the Dashboard (Conditional)

Only if they said they want a visual dashboard.

**Architecture.** The dashboard is a thin presentation layer. It does not compute prep, pulse, or signals on its own. Those are jobs for `/prep`, `/health`, `/sod`, `/eod`. The dashboard reads the markdown files those commands wrote and renders them as HTML.

This keeps each command as the single source of truth. If the prep logic changes, only `/prep` changes. The dashboard automatically reflects it.

**Generated layout:**
```
dashboard/
├── render.py            # CLI entry, orchestration, HTML composition
├── _markdown.py         # tiny stdlib-only markdown → HTML
├── _assets/
│   ├── style.css        # source CSS (read at gen-time, inlined into index.html)
│   └── app.js           # source JS  (same)
├── README.md            # how to run / customize / extend / agent-state boundary
└── index.html           # generated output (gitignored — fully self-contained)
```

**Why split sources but unified output?** Generated `index.html` is one file users can mail, drop on a USB stick, or share without breaking. But the *source* CSS and JS live as real `.css` and `.js` files so a future "ask Claude to restyle" lands in proper files with editor highlighting — not multi-line string constants inside Python.

**Workflow:**
1. Manager runs `/sod`. /sod writes `## SOD` and `## Schedule` blocks to today's journal and runs /prep for each calendar event.
{{#if has_daily_bookends}}2. End of day: manager runs `/eod`. Recap written under `## EOD`.{{/if}}
{{#if has_daily_bookends}}3{{/if}}{{#unless has_daily_bookends}}2{{/unless}}. Manager runs `python dashboard/render.py`. Reads files, inlines CSS+JS, writes `dashboard/index.html`.
{{#if has_daily_bookends}}4{{/if}}{{#unless has_daily_bookends}}3{{/unless}}. Manager opens `dashboard/index.html` in any browser.

**Daily tab sections** (chronological — Start of Day → Schedule → Meeting Prep → End of Day). Only the sections matching the manager's interview answers ship. `has_daily_bookends=false` strips the Start-of-Day and End-of-Day sections. Empty states for present-but-not-yet-populated sections point at the right slash command.

{{#if has_library}}**Library tab.** Card grid, one card per `library/**/*.md` (recursive). Frontmatter (flat `key: value` only) supplies title/summary/captured/tags; sensible fallbacks fill missing fields. Click a card to expand the rendered markdown inline.{{/if}}

**Security model.** The generated file is opened via `file://`, which has unusual same-origin semantics. Mitigations baked in:
- Inline `<meta http-equiv="Content-Security-Policy">` blocks all network requests and external scripts.
- `[text](url)` link rendering passes URLs through a scheme allowlist (`http`, `https`, `mailto`, relative). `javascript:`, `data:`, `vbscript:` become `href="#"`.
- All user content HTML-escaped before any markdown rule fires.
- Fenced code blocks extracted with `\x00FENCED{i}\x00` placeholders before any other pass.
- Filenames allowlist-validated before reading.

Now generate the five files. Substitute `{{manager_first_name}}` once at the top of `render.py`. Don't paraphrase the code — copy it verbatim.

```python
TEMPLATE: dashboard/render.py
---
"""Dashboard renderer for {{manager_first_name}}'s management system.

Reads markdown files that /sod{{#if has_daily_bookends}}, /eod{{/if}}, and /prep wrote.
Inlines CSS+JS from _assets/ and writes a self-contained index.html.
Stdlib only. Python 3.9+.

Run:  python dashboard/render.py
Open: dashboard/index.html
"""
from __future__ import annotations

import html
import re
import sys
from datetime import date, datetime
from pathlib import Path

# `_markdown` lives next to this file. Add the dashboard directory to the
# path so `python dashboard/render.py` works regardless of CWD.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _markdown import render_markdown, split_into_h2_blocks  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = Path(__file__).resolve().parent
ASSETS = DASHBOARD / "_assets"
OUT = DASHBOARD / "index.html"

# Single source of truth for journal H2 heading names. Slash command
# templates that write to journal/*.md MUST use these exact strings.
JOURNAL_HEADINGS = {"sod": "SOD", "schedule": "Schedule", "eod": "EOD"}

FILENAME_OK = re.compile(r"^[A-Za-z0-9._-]+\.md$")
MAX_FILE_BYTES = 1_000_000  # regex-DoS defense


# ============================================================
# File helpers
# ============================================================

def safe_read(path: Path) -> str:
    """Read a file if it exists, is under the size cap, and has a clean
    filename. Returns '' otherwise. Logs to stderr on rejection."""
    if not path.exists():
        return ""
    if not FILENAME_OK.match(path.name):
        print(f"skip (bad filename): {path.name}", file=sys.stderr)
        return ""
    if path.stat().st_size > MAX_FILE_BYTES:
        print(f"skip (too large): {path.name}", file=sys.stderr)
        return ""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"skip (not utf-8): {path.name}", file=sys.stderr)
        return ""
    # Reject NUL bytes — they're our placeholder sentinel.
    return text.replace("\x00", "")


def journal_path(target: date) -> Path:
    return ROOT / "journal" / str(target.year) / f"{target.isoformat()}.md"


def prep_card_paths(target: date) -> list[Path]:
    year_dir = ROOT / "journal" / str(target.year)
    if not year_dir.exists():
        return []
    return sorted(year_dir.glob(f"{target.isoformat()}-prep-*.md"))


# ============================================================
# Section renderers — each takes a target date and returns HTML
# ============================================================

def _panel(title: str, body: str, meta: str = "") -> str:
    meta_html = f'<span class="panel-meta">{html.escape(meta)}</span>' if meta else ""
    return (
        f'<section class="panel">'
        f'<div class="panel-head"><h2>{html.escape(title)}</h2>{meta_html}</div>'
        f'<div class="panel-body">{body}</div>'
        f'</section>'
    )


def _empty(title: str, command: str) -> str:
    return (
        f'<div class="empty">'
        f'<span class="empty-glyph" aria-hidden="true">&#9676;</span>'
        f'<p class="empty-title">{html.escape(title)}</p>'
        f'<p class="empty-hint">Run <code class="cmd">{html.escape(command)}</code> in your terminal, '
        f'then re-run <code>python dashboard/render.py</code>.</p>'
        f'</div>'
    )


def sod_section(target: date) -> str:
    text = safe_read(journal_path(target))
    blocks = split_into_h2_blocks(text)
    body = blocks.get(JOURNAL_HEADINGS["sod"], "").strip()
    if not body:
        return _panel("Start of day", _empty("Nothing here yet.", "/sod"))
    return _panel("Start of day", render_markdown(body))


def schedule_section(target: date) -> str:
    text = safe_read(journal_path(target))
    blocks = split_into_h2_blocks(text)
    body = blocks.get(JOURNAL_HEADINGS["schedule"], "").strip()
    if not body:
        # Fallback for journals written before the /sod template change.
        sod = blocks.get(JOURNAL_HEADINGS["sod"], "").strip()
        if sod:
            return _panel("Schedule", '<p class="hint">Schedule lives inside today\'s start-of-day briefing.</p>')
        return _panel("Schedule", _empty("No schedule captured yet.", "/sod"))
    # Count bullets for a small meta affordance.
    count = sum(1 for ln in body.splitlines() if ln.strip().startswith("-"))
    meta = f"{count} {'event' if count == 1 else 'events'}" if count else ""
    return _panel("Schedule", render_markdown(body), meta=meta)


def prep_cards_section(target: date) -> str:
    cards = prep_card_paths(target)
    if not cards:
        return _panel("Meeting prep", _empty("No prep cards for today.", "/sod"))
    parts = []
    today_prefix = f"{target.isoformat()}-prep-"
    for card in cards:
        slug = card.stem.removeprefix(today_prefix) if card.stem.startswith(today_prefix) else card.stem
        body = safe_read(card)
        parts.append(
            f'<details>'
            f'<summary><span class="prep-slug">{html.escape(slug)}</span></summary>'
            f'<div class="prep-body">{render_markdown(body)}</div>'
            f'</details>'
        )
    meta = f"{len(cards)} {'card' if len(cards) == 1 else 'cards'}"
    return _panel("Meeting prep", "".join(parts), meta=meta)


def eod_section(target: date) -> str:
    text = safe_read(journal_path(target))
    blocks = split_into_h2_blocks(text)
    body = blocks.get(JOURNAL_HEADINGS["eod"], "").strip()
    if not body:
        return _panel("End of day", _empty("Not captured yet.", "/eod"))
    return _panel("End of day", f'<details open><summary>Day\'s recap</summary><div>{render_markdown(body)}</div></details>')


# ============================================================
# Library
# ============================================================

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
KV_RE = re.compile(r"^([a-zA-Z_][\w-]{0,40}):\s*(.{0,500})$")
SLUG_OK = re.compile(r"^[a-z0-9-]{1,80}$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines()[:50]:
        kv = KV_RE.match(line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return meta, text[m.end():]


def humanize(stem: str) -> str:
    return stem.replace("-", " ").replace("_", " ").strip().capitalize()


def first_paragraph(body: str, limit: int = 140) -> str:
    for para in body.split("\n\n"):
        clean = para.strip()
        if clean and not clean.startswith("#"):
            return clean[:limit] + ("..." if len(clean) > limit else "")
    return ""


def library_cards() -> list[dict]:
    lib = ROOT / "library"
    if not lib.exists():
        return []
    docs: list[dict] = []
    for path in sorted(lib.rglob("*.md")):
        if not FILENAME_OK.match(path.name):
            print(f"skip library (bad filename): {path.name}", file=sys.stderr)
            continue
        # Path safety: must stay under library/.
        try:
            path.resolve().relative_to(lib.resolve())
        except ValueError:
            print(f"skip library (path escape): {path.name}", file=sys.stderr)
            continue
        raw = safe_read(path)
        meta, body = parse_frontmatter(raw)
        slug = path.stem
        if not SLUG_OK.match(slug):
            slug = f"doc-{abs(hash(slug)) % (10**8):08d}"
        title = meta.get("title") or humanize(path.stem)
        summary = meta.get("summary") or first_paragraph(body)
        captured = meta.get("captured") or datetime.fromtimestamp(path.stat().st_mtime).date().isoformat()
        tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
        docs.append({
            "slug": slug,
            "title": title,
            "summary": summary,
            "captured": captured,
            "tags": tags,
            "body_html": render_markdown(body),
        })
    docs.sort(key=lambda d: d["title"].lower())
    return docs


def render_library_panel() -> str:
    docs = library_cards()
    if not docs:
        return _panel("Library", _empty("Empty library.", "drop a markdown file in library/"))
    cards = []
    bodies = []
    for d in docs:
        tag_html = "".join(
            f'<span class="tag">{html.escape(t)}</span>' for t in d["tags"][:4]
        )
        cards.append(
            f'<button class="library-card" type="button" '
            f'aria-expanded="false" aria-controls="doc-{html.escape(d["slug"], quote=True)}" '
            f'data-doc-slug="{html.escape(d["slug"], quote=True)}" '
            f'data-tags="{html.escape(",".join(d["tags"]), quote=True)}">'
            f'<h3>{html.escape(d["title"])}</h3>'
            f'<p class="card-summary">{html.escape(d["summary"])}</p>'
            f'<div class="card-meta"><time>{html.escape(d["captured"])}</time>{tag_html}</div>'
            f'</button>'
        )
        bodies.append(
            f'<section class="doc-body" id="doc-{html.escape(d["slug"], quote=True)}" hidden>'
            f'<button class="doc-close" type="button">Close</button>'
            f'<article>{d["body_html"]}</article>'
            f'</section>'
        )
    return (
        f'<header class="hero hero-library">'
        f'<p class="eyebrow">LIBRARY &middot; {len(docs)} {"DOC" if len(docs) == 1 else "DOCS"}</p>'
        f'<h1>Reference shelf</h1>'
        f'</header>'
        f'<div class="library-grid">{"".join(cards)}</div>'
        f'{"".join(bodies)}'
    )


# ============================================================
# Tab + section registry
# ============================================================

DAILY_SECTIONS = [
    {{#if has_daily_bookends}}sod_section,
    {{/if}}schedule_section,
    prep_cards_section,
    {{#if has_daily_bookends}}eod_section,
    {{/if}}
]

TABS = [
    {"id": "daily", "label": "Daily"},
    {{#if has_library}}{"id": "library", "label": "Library"},{{/if}}
]


# ============================================================
# Page composition
# ============================================================

CSP = (
    "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; "
    "img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'"
)


def render_hero(target: date) -> str:
    eyebrow = "TODAY &middot; " + target.strftime("%A, %B %-d").upper()
    headline = "Your day at a glance"
    return (
        f'<header class="hero">'
        f'<p class="eyebrow">{eyebrow}</p>'
        f'<h1>{headline}</h1>'
        f'</header>'
    )


def render_tabs() -> str:
    if len(TABS) == 1:
        return ""  # no tab nav if only one tab
    items = []
    for i, tab in enumerate(TABS):
        selected = "true" if i == 0 else "false"
        tabindex = "0" if i == 0 else "-1"
        items.append(
            f'<button role="tab" id="tab-{tab["id"]}" '
            f'aria-controls="panel-{tab["id"]}" aria-selected="{selected}" '
            f'tabindex="{tabindex}">{html.escape(tab["label"])}</button>'
        )
    return f'<div role="tablist" aria-label="Sections">{"".join(items)}</div>'


def render_daily_panel(target: date) -> str:
    sections = "".join(fn(target) for fn in DAILY_SECTIONS)
    hidden = "" if TABS[0]["id"] == "daily" else " hidden"
    return (
        f'<section role="tabpanel" id="panel-daily" aria-labelledby="tab-daily" tabindex="0"{hidden}>'
        f'{render_hero(target)}'
        f'{sections}'
        f'</section>'
    )


def render_library_tabpanel() -> str:
    return (
        f'<section role="tabpanel" id="panel-library" aria-labelledby="tab-library" tabindex="0" hidden>'
        f'{render_library_panel()}'
        f'</section>'
    )


def render_theme_toggle() -> str:
    return (
        '<fieldset class="theme-toggle" role="radiogroup" aria-label="Color theme">'
        '<button role="radio" aria-checked="true"  data-theme-choice="system">System</button>'
        '<button role="radio" aria-checked="false" data-theme-choice="light">Light</button>'
        '<button role="radio" aria-checked="false" data-theme-choice="dark">Dark</button>'
        '</fieldset>'
    )


# Inlined synchronously in <head> BEFORE the stylesheet to prevent FOUC.
PRE_PAINT_SCRIPT = """(function(){
  var stored = localStorage.getItem('theme');
  if (stored === 'light' || stored === 'dark') {
    document.documentElement.dataset.theme = stored;
  }
  document.documentElement.style.colorScheme =
    stored || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
})();"""


def render_page(target: date) -> str:
    css = (ASSETS / "style.css").read_text(encoding="utf-8")
    js = (ASSETS / "app.js").read_text(encoding="utf-8")
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    favicon = (
        "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
        "<rect width='32' height='32' rx='6' fill='%231f3a5f'/>"
        "<rect x='8' y='10' width='16' height='2' fill='%23fbfaf7'/>"
        "<rect x='8' y='15' width='16' height='2' fill='%23fbfaf7'/>"
        "<rect x='8' y='20' width='10' height='2' fill='%23fbfaf7'/>"
        "</svg>"
    )

    library_panel_html = render_library_tabpanel() if any(t["id"] == "library" for t in TABS) else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<title>Paperwork &mdash; {target.strftime('%B %-d')}</title>
<link rel="icon" type="image/svg+xml" href="{favicon}">
<script>{PRE_PAINT_SCRIPT}</script>
<style>{css}</style>
</head>
<body>
<div class="wrap">
  <header class="top-bar">
    <div class="brand">Paperwork</div>
    {render_theme_toggle()}
  </header>
  {render_tabs()}
  {render_daily_panel(target)}
  {library_panel_html}
  <footer class="footer">
    <small>Generated <time>{generated}</time> &middot; Contains internal management notes &mdash; handle accordingly.</small>
  </footer>
</div>
<script>{js}</script>
</body>
</html>
"""


def main() -> int:
    target = date.today()
    OUT.write_text(render_page(target), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

```python
TEMPLATE: dashboard/_markdown.py
---
"""Tiny markdown → HTML for the dashboard. Stdlib only.

Supports: ATX headings (H1-H4), paragraphs, bulleted/numbered lists (one
level of nesting), bold, italic, inline code, fenced code blocks,
blockquotes, links, horizontal rules. Unknown markdown degrades to literal
escaped text.

Security invariants:
1. Escape BEFORE applying markdown rules.
2. Fenced code blocks extracted to \\x00FENCED{i}\\x00 placeholders first.
3. Link URLs pass through a scheme allowlist.

Run tests with:  python -m doctest dashboard/_markdown.py -v
"""
from __future__ import annotations

import html
import re
from urllib.parse import urlparse

SAFE_SCHEMES = {"http", "https", "mailto", ""}
FENCE_RE = re.compile(r"```(?P<info>[\w-]{0,30})?\n(?P<body>.*?)\n```", re.DOTALL)
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
CONTROL_CHARS = "\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f"


def _safe_href(url: str) -> str:
    """Allowlist URL schemes. Return '#' for unsafe URLs.

    >>> _safe_href("https://example.com")
    'https://example.com'
    >>> _safe_href("javascript:alert(1)")
    '#'
    >>> _safe_href("data:text/html,<script>alert(1)</script>")
    '#'
    >>> _safe_href("/relative/path")
    '/relative/path'
    """
    url = url.strip()
    if any(c in url for c in CONTROL_CHARS):
        return "#"
    scheme = urlparse(url).scheme.lower()
    return url if scheme in SAFE_SCHEMES else "#"


def _mask_fenced(text: str) -> tuple[str, list[str]]:
    """Replace fenced code blocks with placeholders. Returns (masked, blocks)."""
    blocks: list[str] = []
    def stash(m: "re.Match[str]") -> str:
        info = (m.group("info") or "").strip()
        info = info if re.match(r"^[A-Za-z0-9_-]{0,30}$", info) else ""
        body = html.escape(m.group("body"), quote=False)
        cls = f' class="lang-{info}"' if info else ""
        blocks.append(f"<pre><code{cls}>{body}</code></pre>")
        return f"\x00FENCED{len(blocks) - 1}\x00"
    return FENCE_RE.sub(stash, text), blocks


def _inline(line: str) -> str:
    """Apply inline markdown rules to an already-escaped line."""
    line = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", line)
    line = re.sub(r"\*\*([^*\n]+)\*\*", r"<strong>\1</strong>", line)
    line = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", line)
    line = re.sub(
        r"\[([^\]\n]{1,200})\]\(([^)\n\s]{1,500})\)",
        lambda m: f'<a href="{html.escape(_safe_href(m.group(2)), quote=True)}">{m.group(1)}</a>',
        line,
    )
    return line


def _block_render(text: str) -> str:
    """Block-level state machine. Handles headings, lists (1-level nesting),
    blockquotes, horizontal rules, and paragraphs."""
    out: list[str] = []
    stack: list[str] = []  # open block elements: 'ul', 'ol', 'blockquote', 'p'

    def close_to(target: list[str]) -> None:
        while stack and (not target or stack[-1] != target[-1]):
            out.append(f"</{stack.pop()}>")
            if target and stack and stack[-1] == target[-1]:
                break

    def close_all() -> None:
        while stack:
            out.append(f"</{stack.pop()}>")

    lines = text.split("\n")
    for raw_line in lines:
        line = raw_line.rstrip()

        if not line.strip():
            close_all()
            continue

        # Headings
        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if m:
            close_all()
            level = len(m.group(1))
            out.append(f"<h{level}>{_inline(m.group(2))}</h{level}>")
            continue

        # Horizontal rule
        if re.match(r"^[-*_]{3,}$", line.strip()):
            close_all()
            out.append("<hr>")
            continue

        # Blockquote
        if line.lstrip().startswith(">"):
            if not stack or stack[-1] != "blockquote":
                close_all()
                out.append("<blockquote>")
                stack.append("blockquote")
            body = line.lstrip()[1:].lstrip()
            out.append(f"<p>{_inline(body)}</p>")
            continue

        # Unordered list
        ul_match = re.match(r"^(\s{0,4})[-*+]\s+(.+)$", line)
        if ul_match:
            indent = len(ul_match.group(1))
            if indent >= 2:
                # Nested ul
                if not stack or stack[-1] != "ul-nested":
                    out.append("<ul>")
                    stack.append("ul-nested")
            else:
                # Top-level ul
                while stack and stack[-1] == "ul-nested":
                    out.append("</ul>")
                    stack.pop()
                if not stack or stack[-1] != "ul":
                    close_all()
                    out.append("<ul>")
                    stack.append("ul")
            out.append(f"<li>{_inline(ul_match.group(2))}</li>")
            continue

        # Ordered list
        ol_match = re.match(r"^(\s{0,4})\d+\.\s+(.+)$", line)
        if ol_match:
            indent = len(ol_match.group(1))
            if indent >= 2:
                if not stack or stack[-1] != "ol-nested":
                    out.append("<ol>")
                    stack.append("ol-nested")
            else:
                while stack and stack[-1] == "ol-nested":
                    out.append("</ol>")
                    stack.pop()
                if not stack or stack[-1] != "ol":
                    close_all()
                    out.append("<ol>")
                    stack.append("ol")
            out.append(f"<li>{_inline(ol_match.group(2))}</li>")
            continue

        # Paragraph
        if not stack or stack[-1] != "p":
            close_all()
            out.append("<p>")
            stack.append("p")
            out.append(_inline(line))
        else:
            out.append("<br>" + _inline(line))

    close_all()
    # Map our internal tags to real ones.
    return "".join(out).replace("ul-nested", "ul").replace("ol-nested", "ol")


def render_markdown(text: str) -> str:
    """Render a markdown string to safe HTML.

    >>> render_markdown("**bold**")
    '<p><strong>bold</strong></p>'
    >>> render_markdown("[ok](https://example.com)")
    '<p><a href="https://example.com">ok</a></p>'
    >>> render_markdown("[bad](javascript:alert)")
    '<p><a href="#">bad</a></p>'
    >>> render_markdown("`<script>`")
    '<p><code>&lt;script&gt;</code></p>'
    >>> render_markdown("# Heading")
    '<h1>Heading</h1>'
    """
    if not text:
        return ""
    text, fenced = _mask_fenced(text)
    text = html.escape(text, quote=False)
    text = _block_render(text)
    for i, block in enumerate(fenced):
        text = text.replace(f"\x00FENCED{i}\x00", block)
    return text


def split_into_h2_blocks(text: str) -> "dict[str, str]":
    """Split a markdown document into {h2-heading: body} pairs.

    Fenced code blocks are masked first so '## not a heading' inside ```...```
    doesn't split a block. Content before the first H2 is dropped.

    >>> split_into_h2_blocks("## A\\nbody a\\n## B\\nbody b")
    {'A': 'body a', 'B': 'body b'}
    >>> split_into_h2_blocks("preamble\\n## Only\\nbody")
    {'Only': 'body'}
    """
    if not text:
        return {}
    masked, blocks_list = _mask_fenced(text)
    blocks: dict[str, str] = {}
    matches = list(H2_RE.finditer(masked))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(masked)
        body = masked[m.end():end].strip()
        # Restore fenced code placeholders inside the body.
        for j, block in enumerate(blocks_list):
            body = body.replace(f"\x00FENCED{j}\x00", "```\n" + re.sub(r"<[^>]+>", "", block) + "\n```")
        blocks[heading] = body
    return blocks
```

```css
TEMPLATE: dashboard/_assets/style.css
---
/* Paperwork lightweight dashboard — warm-neutral + ink accent */

:root {
  color-scheme: light dark;
  --bg: #fbfaf7;
  --surface: #ffffff;
  --border: #e8e4dc;
  --text: #1a1a1a;
  --text-muted: #6b6258;
  --accent: #1f3a5f;
  --accent-soft: #eef1f6;
  --shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  --font-mono: "SF Mono", ui-monospace, Menlo, Consolas, monospace;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #14130f;
    --surface: #1c1b17;
    --border: #2a2823;
    --text: #f5f3ee;
    --text-muted: #a59f93;
    --accent: #c9d6e8;
    --accent-soft: rgba(201, 214, 232, 0.10);
    --shadow: none;
  }
}
:root[data-theme="dark"] {
  --bg: #14130f;
  --surface: #1c1b17;
  --border: #2a2823;
  --text: #f5f3ee;
  --text-muted: #a59f93;
  --accent: #c9d6e8;
  --accent-soft: rgba(201, 214, 232, 0.10);
  --shadow: none;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font);
  font-size: 15px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.wrap {
  max-width: 1100px;
  margin: 0 auto;
  padding: 32px 24px 96px;
}

/* === Top bar === */
.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 48px;
  gap: 16px;
}
.brand {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--text);
}

/* === Theme toggle === */
.theme-toggle {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 2px;
  display: inline-flex;
  background: var(--surface);
  margin: 0;
}
.theme-toggle button {
  background: transparent;
  border: 0;
  padding: 4px 12px;
  font: inherit;
  font-size: 12px;
  color: var(--text-muted);
  border-radius: 6px;
  cursor: pointer;
  transition: background 120ms ease, color 120ms ease;
}
.theme-toggle button[aria-checked="true"] {
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: 600;
}
.theme-toggle button:hover:not([aria-checked="true"]) {
  color: var(--text);
}

/* === Tabs === */
[role="tablist"] {
  display: flex;
  gap: 4px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 48px;
}
[role="tab"] {
  background: transparent;
  border: 0;
  padding: 12px 16px;
  font: inherit;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  margin-bottom: -1px;
  transition: color 120ms ease, border-color 120ms ease;
}
[role="tab"]:hover { color: var(--text); }
[role="tab"][aria-selected="true"] {
  color: var(--text);
  border-bottom-color: var(--accent);
}
[role="tab"]:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* === Hero === */
.hero {
  margin-bottom: 64px;
  padding-bottom: 32px;
  border-bottom: 1px solid var(--border);
}
.eyebrow {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin: 0 0 16px;
}
.hero h1 {
  font-size: 36px;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
  margin: 0;
  color: var(--text);
}

/* === Panels === */
.panel {
  margin-bottom: 96px;
}
.panel-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 24px;
  gap: 16px;
}
.panel-head h2 {
  font-size: 22px;
  font-weight: 600;
  letter-spacing: -0.01em;
  margin: 0;
  color: var(--text);
}
.panel-meta {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-muted);
  letter-spacing: 0.02em;
}
.panel-body {
  font-size: 15px;
  line-height: 1.65;
  color: var(--text);
}
.panel-body p, .panel-body li { color: var(--text); }
.panel-body h1, .panel-body h2, .panel-body h3, .panel-body h4 {
  margin: 24px 0 8px;
}
.panel-body h3 { font-size: 17px; font-weight: 600; }
.panel-body h4 { font-size: 14px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.04em; }
.panel-body ul, .panel-body ol { padding-left: 22px; }
.panel-body code {
  font-family: var(--font-mono);
  font-size: 13px;
  background: var(--accent-soft);
  color: var(--accent);
  padding: 1px 6px;
  border-radius: 3px;
}
.panel-body pre {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 14px 16px;
  border-radius: 8px;
  overflow-x: auto;
  font-family: var(--font-mono);
  font-size: 13px;
}
.panel-body pre code { background: transparent; padding: 0; color: var(--text); }
.panel-body a {
  color: var(--accent);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 2px;
}
.panel-body blockquote {
  margin: 12px 0;
  padding-left: 16px;
  border-left: 3px solid var(--accent);
  color: var(--text-muted);
  font-style: italic;
}
.panel-body details {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 12px;
  background: var(--surface);
}
.panel-body details > summary {
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  list-style: none;
  color: var(--text);
}
.panel-body details > summary::-webkit-details-marker { display: none; }
.panel-body details > summary::before {
  content: "+";
  display: inline-block;
  margin-right: 8px;
  color: var(--accent);
  font-family: var(--font-mono);
  font-weight: 500;
}
.panel-body details[open] > summary::before { content: "−"; }
.panel-body details .prep-body, .panel-body details > div {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
}
.panel-body .hint {
  color: var(--text-muted);
  font-size: 13px;
  font-style: italic;
  margin: 0;
}

/* === Empty states === */
.empty {
  padding: 32px 24px;
  text-align: center;
  background: var(--surface);
  border: 1px dashed var(--border);
  border-radius: 12px;
}
.empty-glyph {
  display: block;
  font-size: 28px;
  color: var(--text-muted);
  margin-bottom: 12px;
}
.empty-title {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  margin: 0 0 6px;
}
.empty-hint {
  font-size: 13px;
  color: var(--text-muted);
  margin: 0;
}
.empty-hint code {
  font-family: var(--font-mono);
  background: var(--accent-soft);
  color: var(--accent);
  padding: 1px 6px;
  border-radius: 3px;
  font-size: 12px;
}
.empty-hint code.cmd { font-weight: 600; }

/* === Library === */
.hero-library h1 { font-size: 32px; }
.library-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
  margin-bottom: 32px;
}
.library-card {
  display: block;
  width: 100%;
  text-align: left;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  cursor: pointer;
  font: inherit;
  color: var(--text);
  transition: border-color 120ms ease, transform 120ms ease;
  box-shadow: var(--shadow);
}
.library-card:hover {
  border-color: var(--accent);
  transform: translateY(-1px);
}
.library-card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.library-card[aria-expanded="true"] {
  border-color: var(--accent);
  background: var(--accent-soft);
}
.library-card h3 {
  font-size: 16px;
  font-weight: 600;
  margin: 0 0 8px;
  color: var(--text);
}
.card-summary {
  font-size: 13px;
  color: var(--text-muted);
  margin: 0 0 12px;
  line-height: 1.5;
}
.card-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
}
.tag {
  background: var(--accent-soft);
  color: var(--accent);
  padding: 2px 8px;
  border-radius: 999px;
  font-family: var(--font);
  font-size: 11px;
  font-weight: 500;
}

/* === Doc body (expanded library entry) === */
.doc-body {
  margin-top: 32px;
  padding: 32px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  position: relative;
}
.doc-body article h1 { font-size: 28px; }
.doc-close {
  position: absolute;
  top: 16px;
  right: 16px;
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 4px 12px;
  font: inherit;
  font-size: 12px;
  color: var(--text-muted);
  cursor: pointer;
}
.doc-close:hover { color: var(--text); border-color: var(--accent); }

/* === Prep cards === */
.prep-slug {
  font-family: var(--font-mono);
  font-size: 13px;
}

/* === Footer === */
.footer {
  margin-top: 96px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 12px;
  text-align: center;
}

/* === Mobile === */
@media (max-width: 640px) {
  .wrap { padding: 24px 16px 64px; }
  .top-bar { flex-direction: column; align-items: stretch; gap: 12px; }
  [role="tablist"] { width: 100%; }
  [role="tab"] { flex: 1; text-align: center; }
  .hero h1 { font-size: 24px; }
  .panel { margin-bottom: 64px; }
  .panel-head { flex-direction: column; align-items: flex-start; gap: 4px; }
  .doc-body { padding: 20px; }
}
```

```javascript
TEMPLATE: dashboard/_assets/app.js
---
// Paperwork dashboard — tabs, theme toggle, library card expansion.
// No frameworks, no build step. All state local to the browser.

(function () {
  'use strict';

  // ============================================================
  // Tabs (WAI-ARIA Tabs Pattern)
  // ============================================================
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  var validTabs = new Set(tabs.map(function (t) { return t.id.replace('tab-', ''); }));

  function showTab(name) {
    if (!validTabs.has(name)) name = tabs[0] && tabs[0].id.replace('tab-', '');
    if (!name) return;
    tabs.forEach(function (tab) {
      var isActive = tab.id === 'tab-' + name;
      tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
      tab.tabIndex = isActive ? 0 : -1;
    });
    document.querySelectorAll('[role="tabpanel"]').forEach(function (panel) {
      panel.hidden = panel.id !== 'panel-' + name;
    });
    var current = '#' + name;
    if (location.hash !== current) history.replaceState(null, '', current);
  }

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      showTab(tab.id.replace('tab-', ''));
    });
    tab.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(tab);
      var next;
      if (e.key === 'ArrowLeft')  next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      if (e.key === 'Home')       next = tabs[0];
      if (e.key === 'End')        next = tabs[tabs.length - 1];
      if (next) {
        next.focus();
        showTab(next.id.replace('tab-', ''));
        e.preventDefault();
      }
    });
  });

  window.addEventListener('hashchange', function () {
    showTab(location.hash.slice(1));
  });

  // Initial tab from hash or default to first.
  if (tabs.length > 0) {
    showTab(location.hash.slice(1) || tabs[0].id.replace('tab-', ''));
  }

  // ============================================================
  // Theme toggle (System / Light / Dark)
  // ============================================================
  var themeButtons = Array.prototype.slice.call(
    document.querySelectorAll('.theme-toggle [data-theme-choice]')
  );

  function applyThemeChoice(choice) {
    if (choice === 'light' || choice === 'dark') {
      document.documentElement.dataset.theme = choice;
      document.documentElement.style.colorScheme = choice;
      localStorage.setItem('theme', choice);
    } else {
      delete document.documentElement.dataset.theme;
      document.documentElement.style.colorScheme =
        matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      localStorage.removeItem('theme');
    }
    themeButtons.forEach(function (b) {
      b.setAttribute('aria-checked',
        b.dataset.themeChoice === (choice || 'system') ? 'true' : 'false');
    });
  }

  themeButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      applyThemeChoice(btn.dataset.themeChoice);
    });
  });

  // Initialize toggle state from current storage.
  applyThemeChoice(localStorage.getItem('theme') || 'system');

  // React live to OS theme changes when System is active.
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    if (!localStorage.getItem('theme')) applyThemeChoice('system');
  });

  // ============================================================
  // Library card expansion
  // ============================================================
  document.querySelectorAll('.library-card').forEach(function (card) {
    card.addEventListener('click', function () {
      var slug = card.dataset.docSlug;
      var body = document.getElementById('doc-' + slug);
      if (!body) return;
      var nowOpen = body.hidden;
      // Close any other open docs.
      document.querySelectorAll('.doc-body').forEach(function (d) {
        if (d !== body) d.hidden = true;
      });
      document.querySelectorAll('.library-card').forEach(function (c) {
        if (c !== card) c.setAttribute('aria-expanded', 'false');
      });
      body.hidden = !nowOpen;
      card.setAttribute('aria-expanded', nowOpen ? 'true' : 'false');
      if (nowOpen) body.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  document.querySelectorAll('.doc-close').forEach(function (closeBtn) {
    closeBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var body = closeBtn.closest('.doc-body');
      if (!body) return;
      body.hidden = true;
      var slug = body.id.replace('doc-', '');
      var card = document.querySelector('.library-card[data-doc-slug="' + slug + '"]');
      if (card) {
        card.setAttribute('aria-expanded', 'false');
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });
})();
```

```markdown
TEMPLATE: dashboard/README.md
---
# Dashboard

`python render.py` writes `index.html`. Open that file in any modern browser.

The dashboard is a thin presentation layer. It reads what slash commands (`/sod`{{#if has_daily_bookends}}, `/eod`{{/if}}, `/prep`) wrote to disk and surfaces it in one view. It does not compute anything on its own.

## Layout

- `render.py` — CLI entry. Orchestrates section rendering and HTML composition.
- `_markdown.py` — Tiny stdlib-only markdown → HTML. Doctested.
- `_assets/style.css` — Source CSS. Inlined into `index.html` at gen-time.
- `_assets/app.js` — Source JS. Inlined into `index.html` at gen-time.
- `index.html` — Generated output. Fully self-contained: no external CSS, no external JS, no font CDN, no internet required to open.

## Refresh cycle

The dashboard is a snapshot of what's on disk. Run the commands first, then re-render:

1. Morning: run `/sod`. (This also runs `/prep` for each calendar event.)
{{#if has_daily_bookends}}2. Evening: run `/eod`.
3{{/if}}{{#unless has_daily_bookends}}2{{/unless}}. Run `python dashboard/render.py`.
{{#if has_daily_bookends}}4{{/if}}{{#unless has_daily_bookends}}3{{/unless}}. Refresh the browser.

The footer shows when the file was generated. If it looks stale, re-run.

## Customization

The default styling is restrained on purpose so your data leads. To change it:
- Edit `_assets/style.css` directly. Re-run `render.py` and refresh.
- Or ask Claude to restyle it. ("Match this screenshot." "Make it more Notion-like." "Restyle in a Verge aesthetic.") Claude edits the real CSS file, not a Python string.

The toggle in the top-right cycles theme: System / Light / Dark. Choice persists in `localStorage`.

## Adding a section

The 3-step recipe — works for adding a Health section, a Weekly section, a Customer Delight section, anything new:

1. **Write a section function** in `render.py`:
   ```python
   def health_section(target):
       text = safe_read(ROOT / "journal" / str(target.year) / f"{target.isoformat()}-health.md")
       if not text:
           return _panel("Team health", _empty("No snapshot yet.", "/health"))
       return _panel("Team health", render_markdown(text))
   ```

2. **Add it to `DAILY_SECTIONS`** (or create a new tab in `TABS`):
   ```python
   DAILY_SECTIONS = [sod_section, schedule_section, prep_cards_section, health_section, eod_section]
   ```

3. **Done.** The existing `_panel` and `_empty` helpers give you the empty state, the header, and styling for free.

Don't compute new things in the renderer. Compute them in a slash command, save the result to a file, then add a section here that reads it. This keeps one source of truth per concept.

## What lives only in the browser

Theme choice (`localStorage.theme`), tab state (URL hash), library card expansion state are **browser-local** and intentionally invisible to Claude. Never store decisions or task state there. If a future feature ties behavior to one of these, move that state to a file in the repo so the agent can read it back.

## Security notes

The generated `index.html` opens via `file://`, which has unusual same-origin semantics in some browsers. The renderer ships with:
- A strict Content-Security-Policy meta tag (no network, no external scripts).
- URL-scheme allowlist on markdown links (`javascript:` / `data:` become `#`).
- Filename and size validation on every file read.

This file contains internal management notes. Don't post it publicly. Treat it as you would any document you authored.

## Sample journal shape

`/sod` writes today's journal under H2 blocks. Roughly:

```markdown
## SOD

Today's focus: ship the GEO rollout doc. Carry-overs from yesterday: review Sara's PR.

## Schedule

- 09:30 — 1:1 with Sara — [link](journal/2026/2026-05-15-prep-sara.md)
- 11:00 — Eng leads sync
- 14:00 — Focus block

## EOD

Shipped GEO doc. Sara's PR reviewed and merged. Tomorrow: write the Q3 brief.
```

The dashboard extracts each H2 block and renders it under the matching section.
```

Sections list is wired automatically from the interview answers via the conditional blocks in the `TABS` and `DAILY_SECTIONS` lists above. Keep the dashboard small at handoff. The manager can ask Claude to extend it later.

### Step 10: Initialize Git (Optional)

Ask: "Want me to initialize this as a git repo? Version control is useful for tracking changes over time. Not required."

If yes:
- `git init`
- Create a `.gitignore` (OS files, editor files, dashboard/index.html if they want renders untracked)
- Initial commit: "initialize management system with Paperwork"
- Ask if they want to push to GitHub or GitLab. If yes and they have `gh` or `glab` installed, create a private repo and push.

### Step 11: The Handoff

Tell them what was built, what's auto-populated, and what they need to fill in.

Use this template, adapted to what was actually generated:

```
Your management system is ready. Here's where things stand.

**Auto-populated, ready to use:**
- CLAUDE.md with your philosophy, success framework, and tool map
- Slash commands wired to {{tool_list}}
- Question banks weighted toward {{top_pain_points}}
- Signal framework derived from what you said you watch for
- Success framework with your stated criteria
- Example person directory ({{example_person_path}})
{{#if has_dashboard}}- Dashboard renderer at dashboard/render.py — single self-contained HTML file, light/dark theme toggle{{#if has_library}}, Daily + Library tabs{{/if}}{{/if}}
{{#if has_git}}- Git repo initialized{{/if}}

**On you, in order:**
1. **Now (5 min).** Open CLAUDE.md and read it. If anything misrepresents how you actually manage, edit it. The system reads from this file every session.
2. **Before your next 1-on-1 (10 min).** Duplicate {{example_person_path}} to people/[first-last]/ for your top three reports. Fill in profile.md with whatever you know. 30% complete is fine.
3. **Tool wiring (optional, 10 min).** Open the Tools table in CLAUDE.md. For any tool where you have a Claude integration installed, the commands will use it automatically. For anything else, the system falls back to manual prompts. You can wire integrations later.
4. **First week.** After each 1-on-1, run /{{primary_log_command}} [name]. Don't worry about format. Raw notes compound.
5. **End of first week.** Run /health and see if it surfaces anything useful. If not, edit references/signal-framework.md and try again.
{{#if has_dashboard}}6. **Dashboard (optional).** Run `python dashboard/render.py` and open `dashboard/index.html`. The toggle in the top-right cycles theme (System / Light / Dark). {{#if has_library}}Drop reference docs in `library/` to populate the Library tab. {{/if}}Bookmark the file. Re-render after each /sod{{#if has_daily_bookends}} or /eod{{/if}}.{{/if}}

**What to expect:**
- Week 1: feels like extra typing. It is.
- Week 2: /prep starts pulling useful context.
- Month 1: /review and /weekly become a real time-saver.

If something's off, run Paperwork again and tell it what to change. The system is meant to evolve.

If you want hands-on help getting it dialed in, there's a coaching option in the README.
```

---

## Principles

These guide every generation decision:

1. **Their system, not yours.** Every output reflects how *they* manage. Don't impose a philosophy.
2. **Start useful, grow over time.** Generate enough to be immediately usable. Don't over-engineer.
3. **Tools they have, not tools they should get.** If they don't use a meeting recorder, don't generate /sync. Meet them where they are.
4. **Raw over polished.** Notes and logs should be fast to capture, not pretty to read. Speed of capture beats formatting.
5. **Humans over process.** The system exists to free up time for the hard, human parts of management. If a feature adds process without saving time, skip it.
6. **Private by default.** This is sensitive people data. Generate appropriate privacy guidelines and remind them.
7. **No jargon in user-facing text.** They are a manager, not an infra person. Don't say "MCP server", "agent loop", "context window", "tool call" to them. Say "Claude integration", "I checked", "I read".
8. **No em dashes anywhere.** Period or comma or rewrite. House style.
9. **One source of truth per concept.** `/prep` owns prep content. `/health` owns the team snapshot. The dashboard and other commands read those outputs, they don't recompute. If two pieces of code generate the same kind of content, one of them is wrong.

---

## After Setup

Paperwork is done once the system is generated. The user works with it directly using their AI agent and the generated commands.

If they want to evolve the system later, they can run Paperwork again to add commands, adjust question banks, or restructure as their role changes.

---

*Built by [Jamie Wagner](https://www.linkedin.com/in/nobodyiscertain/). Figuring out how to manage 30 people with AI in real time and sharing what works.*

*Want help getting this dialed in? [Book a coaching session.](https://everyexpert.com/nobodyiscertain)*
