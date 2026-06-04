# Proposal TLDR

> **Internal working document.** Master cross-phase reference for The Tax Refactor. Captures the current state of decisions across all six phases plus the project's quick-reference answers and out-of-scope items. Decisions and their rationale live in `decisions-log.md`; unresolved questions live in `open-questions.md`; this doc integrates and serves as the project's single-page state-of-play.
>
> **Not public.** Polish pass required before any external release. Today's character is "working notes," not "polished spec." Several Phase 2 numbers are explicit stakes-in-the-ground pending final calibration during essay drafting.

---

## What the project is

The Tax Refactor is a structural overhaul of U.S. federal personal taxation, built across six modular phases that can each be enacted independently but are designed to interoperate. Architectural pattern: "fewer programs, fatter checks" — the tax code collects taxes; subsidies and benefits flow through direct programs run by domain-expert agencies. Design tenets in `tenets.md`: **Radical Simplicity**, **Fiscal Durability**, **Fuel the Climb**, **Reward Innovation**.

Public-facing brand: **The Tax Refactor** (Substack). Repo and URL slug remain `fair-and-simple-tax-act` for SEO continuity.

Audience: deliberately cross-partisan. The published essays use a "From the right / From the left / From the middle" framing rather than tribal positioning.

---

## The Six Phases

### Phase 1 — Lifetime Gains Framework (LGF). **PUBLISHED.**

**Summary.** Every American gets a universal lifetime capital gains exemption ($2M single / $4M MFJ). Above the exemption, rate slides from 0% up to the top ordinary income tax rate, fully phased in at $6M single / $12M MFJ. Four realization events: sale, death, gift, borrowing. Eliminates roughly 10–15% of the IRC.

**Key mechanics.**
- Universal exemption: **$2M single / $4M MFJ**, CPI-indexed
- Phase-in zone: $2M–$6M single ($4M–$12M MFJ), rate slides 0% → top ordinary
- Top rate is **pegged** to the top ordinary income rate (modeled as 37% in the published essay; moves to whatever Phase 2 lands on, roughly 43–47%)
- Realization events: sale (unchanged), death (Canada-style), gift (donor pays at transfer; $19K annual cash exclusion retained), borrowing against appreciated assets (deemed realization with basis step-up)
- CPI-indexed basis (Rule 4) — eliminates phantom inflation gains
- Roth Rule 5 in published essay is **superseded** by Phase 5 USA design
- Implementation: lifetime counter starts at $0 on enactment; no retroactive counting
- Charitable transfers: appreciation not realized; deduction (now: credit under Phase 2) aligned with cost basis (UK Gift Aid model)

**Eliminates.** AMT, NIIT, estate tax, QSBS / Section 1202, Section 121 (home sale exclusion), Section 1031 (like-kind exchanges), stepped-up basis, lifetime gift tax exemption (~$13.6M), carried-interest preference, GRATs and dynasty trusts, Opportunity Zone deferrals, Section 453 installment sales, Section 1256 60/40, the 28% collectibles rate, Section 1244 small business loss treatment.

**Revenue.** $45–170B/yr, midpoint **~$108B**. Phase 2 pin boost adds **~$13–15B** once the top rate moves from 37% baseline to ~43–47%.

**Status.** Published. See `lifetime-gains-essay.md` and `technical_spec.md`.

---

### Phase 2 — Income Tax Reform. **DRAFT; calibration TBD.**

**Summary.** Eliminate all deductions, replace with a 0% bracket and three capped credits. Five brackets, more progressive than current law. Filing status collapses from five to two. Published headline rates are uniform; after-SALT effective rates vary by state of residence (federalism made visible without expanding the bracket count).

**Key mechanics.**
- **Five brackets (MFJ):** 0% / 12% / 22% / 35% / **43%** at $0–30K / $30–130K / $130–300K / $300–750K / $750K+
  - *Stake in the ground.* Top rate may rise to ~47% on $750K+ to fund the SALT credit; possibly with the higher tier kicking in at $1.5M MFJ instead of $750K. Calibration finalized at essay drafting.
- Single-filer thresholds = half of MFJ
- 0% bracket replaces the standard deduction
- **Filing status: 5 → 2** (Individual, Joint). HoH, MFS-as-separate-structure, QSS all collapse.
- All deductions eliminated (mortgage interest, SALT-as-deduction, medical-as-deduction, charitable-as-deduction, etc.)
- Pass-through deduction (Section 199A / QBI) not renewed

**Three credits.**
- **Charitable: 25% credit on donations, capped at 3% of federal liability.** (Recalibrated from prior 50%/5%.) Aligns with international norms (UK Gift Aid ~25%), prevents zero-out abuse via cap.
- **Medical: 30% refundable credit on expenses above $5,000.** Universal, no itemization. Refundability is essential for catastrophe protection.
- **SALT: 25% credit on estimated state+local taxes paid, capped at ~15% of federal liability.** *Stake in the ground.* Mechanism: Treasury-maintained presumptive lookup table by income decile × state of residence. Federal return computes as `f(income, state of residence)` — no actual state return needed. Extends what is currently an itemizer-only benefit (~10% of filers under TCJA/OBBBA) to all filers.
- **Subsidies leave the tax code.** CTC, EITC, AOTC, LLC, student loan interest deduction, education credits all relocated to Phase 3's direct payment program.

**Federalism / Brandeis framing.** The federal income tax recognizes that states are sovereign laboratories of policy. A 25% credit on state taxes is the federal government's affirmative acknowledgment of state-level service delivery — not a defensive "no double taxation" claim but an offensive "we want states to vary" claim.

**Presentation: "after-SALT effective rates."** Publish headline brackets uniform; show readers their actual effective rate based on state of residence. This makes federalism visible in every taxpayer's actual bill without expanding the bracket structure.

**Revenue.** Designed roughly revenue-neutral within the income tax phase once the top-rate hike + LGF pin boost are paired with the credit costs. The published essay's "designed as a simplification and fairness play, not a major revenue raiser" framing holds.

**Status.** Draft (`drafts/income-tax-essay.md`). SALT, charitable calibration, top bracket, and the after-SALT presentation device all need to be written into the essay before publication.

---

### Phase 3 — Child Benefits. **DRAFT STUB.**

**Summary.** Replace nine overlapping programs with one universal monthly per-child payment. Income-phased. Delivered monthly (not annual). Take-up rates on simple universal payments approach 100%, vs. ~78% for EITC.

**Key mechanics.**
- Single per-child monthly payment
- Income-phased (calibration open)
- Universal — no work requirement, no childcare-expense requirement
- Tentative amount baseline: 2021 expanded CTC ($300/mo under 6, $250/mo ages 6–17) — payment amount and phase-out structure both open
- Replaces: **CTC, ACTC, EITC, AOTC, LLC, student loan interest deduction, educator expense deduction, Coverdell ESA, employer educational assistance exclusion** (nine programs)

**Open.** Payment amount; phase-out thresholds; age cutoffs; childless low-income workers gap (0% bracket + FICA elimination partially fill); adult learner absorption (no longer in tax code, no replacement designed).

**Revenue.** Net depends on calibration. Consolidated budgets of eliminated programs ≈ $220–225B/yr (EITC ~$70B, CTC ~$120B, education credits ~$30–35B) get redirected into the per-child payment. Administrative savings from program consolidation are real but harder to quantify.

**Status.** Draft stub (`drafts/child-payment-essay.md`).

---

### Phase 4 — FICA Reform. **DRAFT STUB.**

**Summary.** Eliminate employee-side FICA entirely (~8% immediate raise for every worker). Retain employer side as an **Employer Safety Net Contribution (ESNC)** at 8%, uncapped. Self-employed pay 8% flat (down from 15.3%). Social Security and Medicare funded through ESNC plus general revenue.

**Key mechanics.**
- Employee-side FICA: eliminated
- Employer-side: 8% uncapped ESNC (vs. current 7.65% capped at ~$176K wage)
- Self-employed: 8% (vs. current 15.3%)
- SS + Medicare funded via ESNC + general revenue blend

**Open.** Social Security benefit formula impact (current AIME/PIA ties benefits to contributions; uncapping contributions without uncapping benefits changes the social contract). Transition mechanics for workers near retirement. General revenue dependency (changes the political dynamics of SS funding).

**Revenue.** Eliminating employee-side ≈ –$600–700B/yr. Uncapping employer-side raises significant revenue but depends on wage distribution modeling. Net position requires detailed scoring; framing is "consolidation, not rate increase" (Wyden-Coats 2011 precedent for the gross-up mechanic).

**Status.** Draft stub (`drafts/fica-reform-essay.md`). Detailed PRFAQ in `internal/archive/social-security-prfaq.md`.

---

### Phase 5 — Universal Savings Account (USA). **DRAFT.**

**Summary.** Replace 15+ tax-advantaged account types with one universal post-tax savings vehicle. $1K government seed at birth. Roth-style: contributions withdrawable anytime; gains tax-free after age 60 up to $2.5M of withdrawals; qualified medical withdrawals tax-free at any age. Inheritance mirrors current Roth IRA rules.

**Key mechanics.**
- **$1,000 government seed at birth** (annual cost ~$3.6B for 3.6M births/yr)
- **$30,000 annual contribution cap** (after-tax, CPI-indexed) — single cap, counts every dollar regardless of source (no separate employer limit)
- **$5,000,000 balance cap (CPI-indexed)** — contributions stop at cap, growth continues tax-free. System's only balance cap; absorbs LGF Rule 5's $5M Roth cap (Rule 5 retires)
- **Post-tax only** — no pre-tax/Traditional option (kills the Traditional-vs-Roth decision)
- **No employer match construct** — match collapses into salary under the single cap; deletes ERISA testing, safe harbor, true-ups, vesting
- **Auto-enrollment as payroll default** — 3% → ~10% (SECURE 2.0 port); the participation engine in place of the match
- Contributions withdrawable anytime, no penalty
- Qualified medical withdrawals tax-free at any age (§213(d) definition; no double-dip with Phase 2 medical credit)
- **529 / Coverdell / ABLE roll in tax-free** (count to $5M cap, not the $30K annual cap)
- **Pre-age-60 gains:** taxed under LGF (USA gains use LGF exemption and sliding scale)
- **Post-age-60:** tax-free up to $2.5M total withdrawals (indexed); above $2.5M, LGF rates
- **No required minimum distributions**

**Inheritance (Roth IRA port; SECURE Act 2019).**
- **Spouse:** treat-as-own rollover; lifetime continuation; no drain
- **Non-spouse:** separate Inherited USA; full drain within 10 years; tax-free during the window; no annual RMDs; drained balance exits to taxable brokerage at FMV basis
- **Eligible Designated Beneficiaries** (minor child of decedent, disabled, chronically ill, beneficiary not more than 10 years younger): lifetime stretch instead of 10-year drain

**Replaces (15 account types).** Traditional 401(k), Roth 401(k), Traditional IRA, Roth IRA, SEP IRA, SIMPLE IRA, 529, Coverdell ESA, ABLE, HSA, FSA, HRA, 457(b), TSP, employer-sponsored pensions.

**Transitioning the old accounts (redesigned June 2026).** Two mechanisms. (1) **Deprecation is the baseline:** on enactment, legacy account types close to new accounts and new contributions; all new saving flows to the USA; existing balances run off under old rules. Zero cost, near-zero risk, delivers the forward-looking simplification by itself. (2) **Optional conversion, priced PV-neutral:** after-tax accounts (Roth, 529, Coverdell, ABLE) roll in tax-free; pre-tax accounts pay a conversion rate set to be roughly present-value-neutral to Treasury (no discount carrot → no giveaway, no regressive windfall). It pulls revenue *forward* (near-term debt paydown at no net long-run cost) and migrates the willing. No deadline/cliff. **Retired:** the flat-12%/10-year-window/$1.2–1.3T-windfall framing — gross cash that ignored the future revenue it spends. Rationale: a carrot deep enough to convert everyone fast necessarily deepens the long-run deficit (the trilemma between fast migration, debt paydown, and not deepening the deficit). See `decisions-log.md`.

**Revenue.** Ongoing: roughly revenue-neutral (Roth-style timing shift; $5M cap prevents unlimited accumulation). Conversion: PV-neutral by design (timing shift, not a net raiser). $1K seed cost: ~$3.6B/yr from general revenue.

**Open (remaining after June 2026 passes).** Conversion rate: solve via simulation for the PV-neutral point (or a deliberately budgeted cost), modeling uptake by age/balance/horizon. Auto-enrollment default-rate calibration. Medical receipt substantiation mechanism. *Resolved: post-tax-only, no-employer-match/single-cap, auto-enrollment, 529/Coverdell/ABLE rollover, §213(d) port, medical double-dip rule, seed funding (general revenue), $5M-cap/Rule-5 reconciliation, conversion redesign (deprecation + PV-neutral optional conversion). See `decisions-log.md`.*

**Status.** Draft (`drafts/universal-savings-account-essay.md`).

---

### Phase 6 — Social Security Modernization. **NOT YET DRAFTED.**

**Summary.** Largest fiscal impact and hardest political lift. Deferred. Transition mechanism contemplated: "higher of" frozen-floor structure (UK 2016 State Pension and Sweden 1990s precedents). Not yet in essay form.

**Key tensions.**
- **Double progressivity:** progressive payout formula (bend points) + (proposed) uncapped progressive contributions = simplicity violation worth resolving
- Five levers identified (in archived PRFAQ)
- Contributory insurance framing (FDR design) is durable political design; preserved in transition narrative
- The "future me" framing is emotionally useful even if technically imprecise

**Status.** Not drafted. PRFAQ in `internal/archive/social-security-prfaq.md`.

---

## 30-Second Answers (Quick Reference)

**What is the Tax Refactor?**
A structural refactor of U.S. federal personal taxation across six modular phases, built on four design tenets and a "fewer programs, fatter checks" architecture.

**What's the public-facing brand?**
The Tax Refactor (taxrefactor.substack.com). Repo and URL slug stay `fair-and-simple-tax-act` for SEO continuity.

**What's the headline LGF exemption?**
**$2M single / $4M MFJ.** Universal, CPI-indexed. Source of truth: published `lifetime-gains-essay.md`.

**What's the headline Phase 2 top rate?**
**43% MFJ on $750K+** (published draft). Working stake-in-the-ground may rise to ~47% to fund the SALT credit; final calibration deferred to essay drafting.

**What gets eliminated in Phase 1?**
AMT, NIIT, estate tax, QSBS, Section 121, 1031, stepped-up basis, lifetime gift exemption, GRATs/dynasty trusts, carried interest, Opportunity Zone deferrals, plus seven more. ~10–15% of the IRC by volume.

**What gets eliminated in Phase 2?**
All itemized deductions (mortgage interest, SALT-as-deduction, etc.), the standard deduction (replaced by 0% bracket), Schedule A, three filing statuses, the pass-through deduction (Section 199A/QBI), CTC/EITC/AOTC/education credits (relocated to Phase 3).

**What replaces deductions in Phase 2?**
A 0% bracket plus three capped credits: charitable (25%, 3% cap), medical (30% refundable, $5K threshold), SALT (25%, ~15% cap via Treasury-maintained presumptive lookup).

**Is the framework revenue-positive?**
Phase 1 generates ~$108B/yr midpoint. Phase 2 designed roughly revenue-neutral within the phase. Phase 4 is net negative without offsets. Framework's Fiscal Durability claim depends on the integrated case plus growth plus spending discipline (both acknowledged out of scope for this project). Phase 5's account transition is designed PV-neutral (pulls revenue forward for near-term debt paydown; not a net raiser).

**What's out of scope?**
Corporate taxation (entirely; triples surface area). Healthcare tax treatment (~$300B employer exclusion is the largest single tax expenditure but conflates with healthcare policy).

**Who's the audience?**
Deliberately cross-partisan. See the "From the right / From the left / From the middle" framing in `lifetime-gains-essay.md`.

**What does this project deliberately *not* do?**
Maximize revenue. Re-engineer the entire welfare system. Solve healthcare. Solve corporate. Re-litigate Social Security from scratch. Be a bill that could pass tomorrow.

---

## Cross-Phase Open Questions (current)

Full state in `open-questions.md`. Headline items:

- **Phase 2 calibration**: SALT credit rate (25% stake), SALT cap (~15% stake), top bracket (43% vs 47%), whether 48% kicks in at $1.5M MFJ instead of $750K. All TBD when essay is written for real.
- **Phase 3**: per-child payment amount and phase-out structure. Childless low-income worker gap.
- **Phase 4**: SS benefit formula impact. Transition for workers near retirement.
- **Phase 5**: USA / medical credit double-dip rule.
- **Phase 6**: most details.
- **Cross-cutting**: charitable-credit receipt tracking, medical credit substantiation, K-1 income treatment, marriage/divorce LGF counter, gift tax as separate type, international tax interaction.
- **Calibration validation**: empirical donor-behavior modeling for charitable credit rate; medical credit calibration against ACA interaction.

---

## Out-of-Scope (with brief why)

- **Corporate taxation.** Triples surface area. Tangled in different debates (pass-through, international, book-vs-tax). Deserves its own treatment.
- **Healthcare tax treatment.** Employer exclusion ~$300B/yr (largest single tax expenditure). Conflates tax reform with healthcare policy.
- **State tax design.** The federal SALT credit recognizes state tax burden but doesn't prescribe state policy.
- **Tax administration UI / IRS modernization.** The framework assumes the IRS can implement a presumptive-lookup mechanism (it can; state-by-bracket data exists), but doesn't redesign the IRS itself.

---

## Sources of Truth

- **Tenets:** `process/tenets.md` (canonical) ↔ `index.md` (synced by hand; one published verbatim copy)
- **Decisions:** `process/decisions-log.md` — captures the *why* so future-us doesn't relitigate settled ground
- **Open questions:** `process/open-questions.md`
- **Backlog (essays / pitch list):** `process/backlog.md`
- **Style:** `process/style-guide.md`
- **Research / stats:** `process/research.md`
- **Published essays are authoritative** for numbers and design choices per README's source-of-truth rule. If a draft or process doc contradicts a published essay, the published essay wins; update the draft.

---

## Maintenance

When a decision changes: update `decisions-log.md`, remove the topic from `open-questions.md`, update the relevant essay (or essays), and reflect it here. Don't leave the file system in an in-between state.

When a number is genuinely up for revision: leave it as an open question, resolve before shipping the next essay that depends on it.

This document is integrative reference, not a published artifact. If anything here diverges from a published essay, the published essay wins.
