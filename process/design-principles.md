---
title: Design Principles & Ways of Working
description: Durable heuristics for designing The Tax Refactor and for collaborating on it. Folded in from the Oct 2026 Claude project merge (see internal/archive/claude-project-handoff-2026-10.md). Tenets live in tenets.md; this file is the "how we decide" layer underneath them.
---

# Design Principles & Ways of Working

The four tenets (`tenets.md`) say *what* the system optimizes for. These are the
heuristics we've learned for *how* to design toward them, and how we work.

## Design principles

- **Architecture is the argument; calibration is the negotiation.** Fix the structure publicly; leave the numbers (exemption, rates, thresholds) as stakes in the ground. This keeps the legislative debate surface small.
- **Ride existing rails.** Extend mechanisms the code already has rather than inventing new ones. Precedents: §877A exit tax (death-as-realization), §1259 constructive sale (borrowing as realization), §1.937-2(f) pro-rata allocation (state-level sourcing), Canada's 1972 deemed disposition at death.
- **Surface area, not just simplicity.** The real danger is new machinery that needs new measurement, valuation, or administrative infrastructure. Count the new forms, appraisals, and agencies a proposal requires.
- **Political reversal pattern.** Tax provisions often produce the opposite long-run political effect from what was intended (employer-based health insurance is the canonical case). Ask what coalition a provision creates in 20 years.
- **Fewer programs, fatter checks.** When cutting provisions, overcompensate with simple, generous, universal benefits.
- **Cash over bureaucracy.** Moynihan / Friedman / Lenkowsky lineage.
- **Documents can be more complex if the resulting policy is simpler.** This is the test for combining vs. sequencing essays.
- **Lobbying pressure moves upstream.** If implementation is automated, tenet-setting becomes the battleground. Vague tenets are easier to game, so write them precisely.
- **Two-dial income framework.** Characterize income by basis and timing of receipt, not by source (labor vs. capital).
- **Lock-in effects apply to voluntary realization.** LGF's mandatory death trigger mostly sidesteps the lock-in debate.
- **Recipient-side fragmentation is self-limiting.** Under any recipient-side inheritance tax, splitting bequests among many heirs is self-limiting at large fortunes and can't be designed away under any progressive system.
- **"Redundant windfall"** is the strongest argument against QSBS (and similar carve-outs) under LGF: the lifetime exemption already delivers the benefit.
- **Prefer the stronger structural answer ("Option A").** When choosing between a patch and the structurally cleaner answer, commit to the structural one and defend it.

## Ways of working

- **Source of truth is this repo.** Published essays win on numbers and design choices; `decisions-log.md` / `open-questions.md` / `backlog.md` / `pending.md` govern everything else (rules in `../README.md` and the Claude Project instructions, whose canonical copy is `claude-project-instructions.md`). Claude Project knowledge and memory are views, never a second copy.
- **Show the math.** Every number in an essay should be reproducible from stated inputs. Matt has caught real errors this way (buy-borrow-die estate tax caveat, the AMT-to-estate-tax causal chain, a CPI adjustment, the "deduction worth nothing" accounting artifact).
- **Verify citations before publishing.** Flag unverified cites inline ("*verify before publishing*").
- **Flag scope creep.** Recurring pattern: new essay ideas outpace execution. Park new ideas in `backlog.md` (Idea backlog) rather than starting them; the capital-stack scope decision (2026-07-23) governs what's active.
- **Publishing pipeline.** Markdown in repo → `make substack` / `make substack-copy` → paste to Substack; bump `substack_synced` frontmatter after each sync; `make substack-status` shows drift. For Substack→Git syncs, use a verbatim paste, not WebFetch (cached renders are stale).
- **Second opinions.** Gemini is used occasionally for alternative framings and sensitivity analysis (`internal/analysis/`).

## Key references

Madoff, *The Second Estate* · Reid, *A Fine Mess* · Lindert (*Growing Public*) · Kleven · Batchelder (Hamilton Project inheritance tax) · Starr, *The Social Transformation of American Medicine* · Saez & Zucman, *The Triumph of Injustice* · Klein & Thompson, *Abundance* · Bradford X-tax (Viard & Carroll) · Haltiwanger / Jarmin / Miranda (firm age vs. size) · Hendren & Sprung-Keyser (MVPF) · Fox & Liscow (2024) · Becko & Sztutman (AER, elasticity) · Pluchino / Biondo / Rapisarda (2018, luck vs. talent)
