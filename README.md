# The Tax Refactor

A modular proposal to refactor U.S. federal tax policy. Published essays at [mattsly.com/fair-and-simple-tax-act](https://www.mattsly.com/fair-and-simple-tax-act/), with copies on [Substack](https://taxrefactor.substack.com).

This git repo and `mattsly.com` are the source of truth. Substack is a republishing destination; if anything diverges, this repo wins.

## Directory layout

The repo has four working areas, plus the usual Jekyll plumbing.

```
.
├── index.md                          # Landing page (uses canonical tenets — sync by hand)
├── *.md (at root)                    # PUBLISHED essays. Live at /:basename.html on the site.
│
├── assets/                           # Images and other binary assets used by published essays.
│
├── drafts/                           # IN-PROGRESS essays. Not in the Jekyll build.
│
├── process/                          # PROJECT DOCS. Not in the Jekyll build.
│   ├── tenets.md                     #   Canonical design tenets (source of truth)
│   ├── backlog.md                    #   Done · In Progress · Stubs · Planned · Ideas · Pitch list
│   ├── decisions-log.md              #   Why we decided what we decided
│   ├── open-questions.md             #   Unsettled architectural questions
│   ├── proposal-tldr.md              #   Cross-phase integrative reference (state-of-play)
│   ├── style-guide.md                #   Voice and writing rules (Matt's voice)
│   ├── research.md                   #   Compliance stats, sources, raw data
│   └── vibe-journalism-outline.md    #   Working outline for a meta essay
│
└── internal/                         # NOT FOR PUBLISHING. Not in the Jekyll build.
    ├── outreach/                     #   One-pagers, pitch docs, contact-specific drafts
    ├── analysis/                     #   Spreadsheets, sensitivity studies, modeling work
    ├── image-specs/                  #   Specs for hero images and infographics
    └── archive/                      #   Superseded drafts, old PR-FAQs, dead-letter docs
```

Everything that's not a published essay is excluded from the Jekyll build via `_config.yml`. Nothing in `drafts/`, `process/`, or `internal/` is ever served.

## Editing rules

### Published essays live at the root, flat URLs

A published essay's URL is `https://www.mattsly.com/fair-and-simple-tax-act/<basename>.html`. **Do not move published essays into a subfolder** — every inbound link breaks. If you need to organize them, add Jekyll permalinks first.

### Tenets are not auto-included

The canonical tenets live in `process/tenets.md`. One published file includes the prose verbatim: `index.md` (which is also the intro essay, and also the version copied to Substack).

If you change `process/tenets.md`, update `index.md` in the same commit.

### Anything linked from a published doc must itself be published

If you add a link from a published essay to a draft, either promote the draft (move it to root, build it out, accept that it's now live) or remove the link. Broken links on a published site are worse than an unfinished essay.

### Published essays are the source of truth

If a draft, process doc, or internal note contradicts a published essay on a number, design decision, or position, the published essay wins. Update the draft or process doc to match — don't quietly change the published essay to fit internal thinking that hasn't shipped. (Live thinking belongs in drafts; once it ships, it is the spec.) If a published number is genuinely up for revision, flag it as an open question and resolve it before shipping the next essay that depends on it.

### Open questions land in `open-questions.md`; resolutions land in `decisions-log.md`

When a new architectural question surfaces in discussion, capture it in `process/open-questions.md` with enough framing (the tension, candidate answers, what's at stake) that future-us can pick it up cold. When a question gets resolved, transcribe the decision and the *why* into `process/decisions-log.md` and remove the entry from `open-questions.md`. The two files should not overlap: a topic is either decided (in the log) or open, never both. If a decided number is still pending external validation (e.g. behavioral modeling), note that in the log entry; don't relist the topic as open.

Three consequences of this rule:

- **Published essays should not contradict anything in `open-questions.md`.** If it's published, we've decided. The exception is when the essay itself explicitly and publicly lists an open question (the LGF flagship's "$2M or $2.5M?" callout is the model). In that case the publicly flagged question can be mirrored in `open-questions.md`.
- **Drafts can freely overlap with `open-questions.md`.** Drafts are work in progress; that's the whole point.
- **When working on an essay produces a decision, update both files in the same pass.** Move the entry from open-questions to decisions-log, and update the essay (or essays) to reflect the decision. Don't leave the file system in an in-between state.

## Publishing workflow

1. Draft lives in `drafts/`.
2. When ready, move to repo root and add Jekyll frontmatter (`layout: plain`, `title`, `description`, `image`, `twitter`).
3. Build locally: `make serve` (renders at `http://localhost:4000/fair-and-simple-tax-act/`).
4. Update `index.md` "What's Next" → link the new essay.
5. Update `process/backlog.md` → move entry from "In Progress" to "Done."
6. Commit, push to `main`. Pages deploys automatically.
7. Copy markdown into Substack, hand-format the image, schedule the post.

## Contributing

This is a personal project. The proposal is structural and opinionated; I'm not soliciting community contributions. But: factual errors, broken numbers, or unclear arguments are always worth flagging — open an issue or email **me@mattsly.com**.

## Status

Active. See `process/backlog.md` for the current state of what's published, in flight, and planned.
