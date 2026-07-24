# Backlog

Single source of truth for what's done, in-flight, planned, and parked. Merged from the old `TODO.md`, `process-notes/future-essays.md`, and `process-notes/scratch-future.md`.

## Done (published)

Essays at the repo root, served from mattsly.com and re-posted to [taxrefactor.substack.com](https://taxrefactor.substack.com).

- **index.md** — Intro essay ("Introducing The Tax Refactor"). Lives at the site root. Establishes the project, names the four tenets (canonical prose copied from `process/tenets.md`), and frames the components.
- **lifetime-gains-essay.md** — Flagship. Lifetime capital gains framework with $2M exemption ($4M MFJ), phase-up, four realization events (sale, loan, gift, death).
- **technical_spec.md** — Implementation details for Lifetime Gains, including zero-gain collateral edge case.
- **warren-wealth-tax-oped-v7.md** — Op-ed positioning the framework against Warren's wealth tax. Submitted to Boston Globe - March 2026
- **gemstone-essay.md** — "If you designed it from scratch" framing piece.
- **dear-tech-bros.md** — Direct address to Silicon Valley on QSBS, carried interest, and the framework's actual impact on founders.
- **the-deduction-hack.md** — "Retire the Personal Tax Deduction." Personal W-4 hook → complexity-is-the-point thesis → deduction architecture as one major case → two fixes (0% bracket + credits) → easy button close.
- **trump-accounts-essay.md** — "Trump Accounts: Great Idea, Bad Product." Case study in legislative product malpractice; sets up the USA argument by walking through why a new account type was the wrong answer to a real problem.

## In progress

Active drafts in `drafts/` that are close to publishable.

- **drafts/income-tax-essay.md** — "The Index Card Tax Return." Rate table, deduction elimination, charitable + medical credits, filing status simplification. Substantively complete; not yet announced/distributed. **Parked per 2026-07-23 scope decision** (the top-bracket piece it contained is fenced into "The Pin" instead).
- **drafts/universal-savings-account-essay.md** — see stub entry below. **Ship-vs-park is Matt's call on return from vacation (~7/29):** ship if the polish pass is under a week, otherwise park cleanly.

## Stubs awaiting expansion

Files exist in `drafts/`, content is sketched but not finished.

- **drafts/charitable-giving-essay.md** — **Re-scoped 2026-07-23: "The Charity Exit," a capital-stack essay** (was: income-tax companion). The published LGF essay promises this companion and names charity "the last large door left open." Scope: DAF payout rules (no requirement today), foundation 5% payout, FMV-vs-basis credit base (see open-questions), warehousing/control-vs-consumption problem, appreciated-asset realization treatment, Madoff's DAF critiques (contact; collaboration candidate). Takes the logged 25%/3% charitable credit as a given parameter. Sequence after Madoff book review + engagement (Q4).
- **drafts/child-payment-essay.md** — Consolidates CTC, ACTC, EITC, AOTC, LLC, and education credits into a single monthly payment. Needs: payment amounts, phase-out thresholds, age cutoffs, interaction with other benefits, 2021 expanded CTC precedent (~30% child-poverty reduction).
- **drafts/fica-reform-essay.md** — Promote from reference-heavy stub to a full standalone essay: case for eliminating employee-side FICA, why employer side is retained and uncapped at 8% as ESNC, revenue neutrality, Social Security solvency implications.
- **drafts/universal-savings-account-essay.md** — Full treatment of the $1K birth seed, $30K annual cap, $5M balance cap, contribution/withdrawal rules, the 15+ accounts it replaces, qualified medical withdrawals, account transition (deprecation-first + optional PV-neutral conversion; old flat-12%/$1.2-1.3T framing retired June 2026), death/inheritance rules, indexing debate. Substantially built out June 2026 (open questions resolved, FAQ cluster, Politics + What Now sections); needs a voice/polish pass and Trump Accounts handoff.
- **drafts/linkedin-post-draft.md** — LinkedIn distribution-format draft.

## Planned essays (not yet drafted)

> **Scope note (2026-07-23, see decisions-log):** active development is the
> **capital stack**. The ranked slate below is the active pipeline; planned
> essays further down that aren't capital-stack are parked as roadmap items —
> kept, not killed.

### ACTIVE SLATE (ranked)

**1. Buy, Save, Die (August flagship).** Counter-punch to the WaPo "myth" piece and the Fox & Liscow discourse: concede the borrowing point (top-0.1% new borrowing ≈ 1% of economic income), expose that the critique amputates its own source (F&L call step-up "indefensible"), name the death exit as the main event ($13.7T top-0.1% unrealized reservoir vs. $62B/yr borrowing flow), present LGF as the framework that answers the critics. Key stats + sources in `research.md` (2026-07-23 sections). Bonus argument: closing death is what makes rate-raising (their own prescription) collectible — deferral elasticity is an artifact of the escape hatch.

**2. The Two Kinds of Rich (September flagship).** W2 rich vs. capital rich — the starkest codified disconnect isn't rich vs. working class. Personal frame: doctor wife's marginal wage dollar (35% + 2.35% Medicare) vs. Matt's marginal qualified-dividend dollar (15% + 3.8% NIIT); ~27-30% vs. ~14% effective on the same $500K, ~6.5% if selling at 50% basis. Use per-stream marginal rates on the joint return (survives the CPA pedant). Chart: Fox & Liscow's rate curve — average rates climb to 15.8% (99-99.9th) then fall to 9.6% for the Forbes 400 ≈ the 8.6% paid by the 50-90th percentiles. **Prerequisite: wife's genuine sign-off.** Recruits the $400K-$1M professional class. Title candidate: "The Two Kinds of Rich."

**3. Field Guide to Taxing Billionaires (Sep/Oct).** The comparison piece (promoted from "Deeper dives" below): LGF vs. ROBINHOOD (Gallego + Goldman versions) vs. Wyden mark-to-market vs. Warren wealth tax vs. Batchelder inheritance tax — scored on revenue, complexity, liquidity, constitutional risk, admin burden. Pre-publication hole-poking ask to Riedl. ROBINHOOD analysis done in `research.md`.

**4. Prop 40 piece (October, calendar-locked).** "Right villain, wrong weapon" timed to California's November billionaire-tax vote — guaranteed national news cycle. Warren op-ed argument transfers directly.

**5. Madoff "The Second Estate" review (October swing).** Low-lift; rides the Ezra Klein moment; warmest re-engagement with the key contact before The Charity Exit.

**6. The Pin (Q4).** The one income-tax change the capital stack needs: new top bracket (45-47% at $750K or $1.5M MFJ), LGF peg convergence mechanics, package math toward a ~$250B/yr headline. Explicitly fences off all other income-tax reform. Feeds on the calibration task: run `internal/analysis/calibration_comparison.xlsx` on (a) 2/6 + 45%@$750K, (b) 2/6 + 45%@$1.5M MFJ, (c) 1/4 anchors as negotiation fallback (+~$27B but taxes into the 90-99th pctile, avg ~$1.8M unrealized/household). Current lean: keep 2/6, fight the bracket fight. Expands the LGF essay's published "if a new top bracket were added" line.

**7. The Charity Exit (Q4, after Madoff engagement).** Re-scoped `drafts/charitable-giving-essay.md` — see stub entry above. The published LGF essay's IOU ("the last large door left open" + promised companion).

**8. The Billionaire and the Senator Agree (conditional).** Short Ackman/Gallego convergence piece — Ackman's Aug 2024 borrow-above-basis proposal vs. S.4662. Trigger: a news moment (e.g., Ackman on Prop 40). Note his version is borrow-above-basis, not gain-equal-to-loan.

### Roadmap (parked unless capital-stack)

### Fiscal Infrastructure First
**Thesis:** Progressives keep proposing ambitious new programs on a foundation that can't support them. Before Medicare for All, before a Green New Deal, we need a tax system that's simple enough to actually work. That's not austerity. That's infrastructure. **Connection to Abundance** thinking. Could serve as the broader frame that makes the Warren op-ed a case study rather than a one-off.

### Vibe Journalism
**Thesis:** Everyone is vibe coding. I'm trying vibe journalism. AI democratized production but not distribution. Meta-frame for the whole project. Personal/accessible tone, early-Substack candidate for audience building. Outline lives in `process/vibe-journalism-outline.md`.

### The Bribery Machine
**Thesis:** Both parties have turned the tax code into a constituency rewards system, just for different demographics. The only structural fix is a code simple enough that there's nothing to corrupt. Examples: Warren's wealth tax (left), "No tax on tips" + Mace's boat deduction (right), Opportunity Zones, MID, pass-through deduction, carried interest survival.

### Who Really Owns "Free Markets"?
**Thesis:** Republicans have abandoned free-market principles; Democrats failed to claim the actual Adam Smith tradition (externalities, anti-monopoly, labor mobility). Two angles in tension — the "rebrand" angle and the "hypocrisy" angle. Probably one essay focused on hypocrisy, with the rebrand argument as a footnote.

### How Are We Keeping Score?
**Thesis:** What metrics is the tax code actually optimizing for, and what *should* it be optimizing for? Inequality data (Realtime Inequality, WID) is contested precisely because we haven't agreed on which numbers matter — wealth share, mobility, middle-class growth rate, generational outcomes. A simple-enough tax code paired with clear scoring metrics could create a self-correcting system: define the optimization function, measure against it, adjust. Connects to the "tax code as algorithm" framing and the AI-era dexterity argument from the intro essay.

### Inheritance as income (the Madoff/Batchelder layer)
**Thesis:** LGF taxes the decedent's *gains* at death but is silent on the *transfer*: $50M of post-tax cash passes to an heir at 0%, forever, while wages are taxed at 37%. "Form of income shouldn't determine rate" demands closing the income-tax exemption on the largest untaxed income category. Proposal sketch: heirs include inherited receipts above a high lifetime threshold (~$10M stake in the ground) in ordinary income. NOT an estate tax revival — it taxes living recipients, not estates, so the estate-repeal positioning survives (but the "death-as-realization makes the estate tax redundant" line in the published LGF essay needs careful handling: redundant for appreciation, silent on transfer). Academic anchor: Batchelder's Hamilton Project proposal (repeal estate/gift taxes; tax inheritances above a lifetime exemption as income + payroll; TPC scored $340B/decade at a $2.5M exemption, $1.4T at $500K — a $10M threshold lands well below, order of $10-20B/yr). Relationship anchor: Ray Madoff (already engaged; her inheritance/philanthropy work makes this the natural collaboration essay). Interacts with the USA death design: the taxable "flush" above the heir's room capacity is a day-one observable receipt, trivially includable. Motivated by Tenets 2 (revenue) + 3 (perpetual dynasties). Raised July 2026.

### Estate tax sunset
The Lifetime Gains framework makes the estate tax redundant (death is a realization event). Needs explicit piece: transition mechanics, treatment of mid-probate estates, interaction with GST tax, trust unwinding.

### AMT elimination
AMT becomes vestigial once deductions are eliminated. Short piece explaining the elimination and the simplification dividend. Could also direct this to Scott Galloway, who's often argued for using the AMT (vs fixing root causes)

### Phase 5: "The Great Conversion" standalone
Currently lives inside `universal-savings-account-essay.md`. **Note (June 2026):** the conversion was redesigned to deprecation-first + an optional PV-neutral conversion, so the original "big revenue generator" rationale for a standalone is weaker. If it still warrants its own piece, the hook is the *design problem* (the migration trilemma, why a discount is a hidden deficit, PV-neutral pricing) rather than a headline revenue number. Revisit the "Great Conversion" name too.

### Corporate tax companion (deferred, explicitly out-of-scope)
A short piece explaining *why* corporate reform is out of scope (and what a separate effort might look like) would preempt the obvious critique.

### Healthcare tax treatment companion (deferred, explicitly out-of-scope)
Same pattern: scoped out, but a short piece explaining why (notes the ~$300B/yr employer exclusion) defends the scope boundary.

## Idea backlog (not yet promoted to a planned essay)

Raw ideas from the old TODO. Not blocked, just not picked up yet.

- **What if Complexity is the Point?** Political-economy umbrella. Tax resistance isn't burden size — it's felt arbitrariness. Stats anchors: Credello 51% bracket survey, Blaufus 128-study review, EITC participation, IRS Taxpayer Advocate filing burden data.
- **Government Can Build Beautiful Products.** Libertarian-trap antidote. NPS, military, GPS, SS, NIH, FAA, FDIC. Image-rich format. Strong viral candidate.
- **The Insane Phone that would be designed if it looked like the tax code.**
- **Tax Code Needs Product Management.** What is product management? We've collapsed objectives into implementation. Student loans as example. Start with the problem, agnostic to solution. Opportunity for AI usage angle.
- **Simplicity should not be political.** Historically "simple taxes" codes conservative (flat tax, free markets). Shouldn't be that way.
- **Charity vs redistribution.** Why the same dollar gets celebrated as charity and attacked as redistribution. Asymmetry: charity preserves donor agency, hierarchy, naming rights, opt-in status; redistribution is mandatory, anonymous, rights-based. 530A as case study — federal seed + tax-advantaged corporate contributions, where political reception tracks framing not mechanism. Possible kicker: "charity in legislative drag."
- **Productizing the Tax Code / Paying taxes should be delightful.**
- **An argument against corporate taxation from the left.** Don't endow corporations with this kind of agency.
- **Are loopholes (i.e. tax credits) effective to modify behavior?** Are they a good way to direct capital toward desirable outcomes — green energy etc.?
- **Importance of dexterity in a dynamic world.** AI is going to change things; we need a few levers, not a tangled mess.
- **What if we let AI design and run our tax code?** Dynamic Mobility + Resource Velocity as system-level goals (replacing Meritocracy and Capital Velocity).
- **The Philosophy of Luck & Mobility.** Money = Talent + Effort + Luck. Insurance model framing for progressive taxation.
- **"No Tax on Tips" case study.** Violates horizontal equity. Form-of-income shouldn't determine rate.
- **Student Loan Interest Deduction case study.** Behavioral subsidy via definitional mechanism. One of five overlapping higher-ed subsidies with zero coordination.
- **The Withholding Architecture.** Withholding as prediction system structurally guaranteed to be wrong. Connects to USA / post-tax architecture.
- **Deconstruct the employer-benefits infrastructure.** Why is so much of American financial life (retirement saving, health insurance, FSAs/HSAs, life insurance, the match) routed through the employer at all? It's a WWII wage-control accident that became load-bearing. The USA essay already chips at one piece (eliminating the employer match as a construct) and now states the project-level position explicitly: employers should pay cash and equity, and the rest unwinds. This would be the umbrella argument: employment-tethered benefits are regressive (you only get them with the right job), create job lock, and hide compensation. Must include the anti-stiffing half: when unwinding saves employers money (match dollars, plan admin, later FICA/ESNC changes), that money passes through to wages, via a one-time mandatory conversion at each transition plus the transparency of cash comp. Connects to FICA reform (ESNC) and the "fewer programs, fatter checks" architecture. Raised by Matt June 2026; pass-through requirement added July 2026.
- **Studies I'd like to see run:** Can people predict their taxes? Do they remember what they paid? Do they feel they're paying the right amount?
- **The rails essay: one deposit address per citizen.** Trump Accounts proved it within months: build a universal account and philanthropy shows up ($6.25B Dell, ~$325M Shotwell SpaceX pledge) because there's finally somewhere to send money. Generalize: the USA as national deposit infrastructure for seeds, child payments, disaster relief, tax refunds, state baby bonds, and private gifts. Includes the door rule (cash only, public securities liquidated at the door, no private assets). Connects to "Government Can Build Beautiful Products" and the child payment essay. Short version now lives in the USA essay's "Anyone Can Fund Anyone" section. Raised July 2026.
- **The Confession (series conclusion candidate).** After N essays of architecture, turn to reader: "yeah, I know how hard this is." Entrenchment IS the argument for refactoring vs. patching.

## Deeper dives / research needed

Referenced but not yet engaged with in depth.

- **Madoff book engagement.** Read Ray Madoff's book, then discuss. Likely relevant to charitable-giving deeper dive (DAFs) and possibly estate tax sunset.
- **Fox & Liscow (2024) "No More Tax-Free Lunch for Billionaires."** Already cited in `technical_spec.md`. Their borrowing-loophole proposal overlaps with our loan-as-realization design. A comparison piece would strengthen both.
- **Field-guide comparison piece.** *Promoted to Active Slate #3 (2026-07-23).* Lifetime Gains vs. Wyden's mark-to-market, Biden-era minimum billionaire tax, Warren's wealth tax, plus the ROBINHOOD Acts. Compare on revenue, complexity, constitutional risk, compliance burden.

## Architectural open questions (summaries — full notes in `open-questions.md`)

- **SALT:** Decided (June 2026): kept as a 25% credit via Treasury-maintained presumptive lookup table, capped at ~15% of federal liability. Calibration of rate, cap, and paired top-bracket hike to be finalized when income-tax-essay is written for real. See `decisions-log.md`. Published `index.md` and `drafts/income-tax-essay.md` need updating to reflect this.
- **Post-tax vs. pre-tax retirement contributions.** ~~All-post-tax is consistent with the broader principle, but optionality has real value for declining-bracket workers.~~ **Resolved June 2026: post-tax only.** Written into the USA essay with the declining-bracket tradeoff addressed head-on. See `decisions-log.md`.
- **Phase 2 scope:** Single comprehensive essay (5-6K words) or three separate pieces (complexity → deductions → Phase 2 proposal)? Currently planning the three-essay approach.

## Meta / infrastructure

- **~~Substack sync pass for the LGF flagship~~ DONE 2026-07-16.** Full-body repaste via `make substack` + md-to-substack. Fixed: superseded charitable section (now status-quo FMV), incorrect Canada citation, July 7 estate-tax restructure, Batchelder scope note, $108B figure, leaked md-to-substack.netlify.app anchor links. Remaining known drift: the other six published essays (see `make substack-status`) — verify each and bump its synced date as they're re-pasted.
- **Standing rule: after any Substack sync, bump that essay's `substack_synced` frontmatter date; run `make substack-status` to see what's drifted.** Slugs/sync dates live in essay frontmatter (fallback map in internal/scripts/substack_export.py covers the four essays that predate frontmatter — migrate them after verifying `make serve` renders them unchanged). The three surfaces drift silently otherwise — the charitable-section divergence went unnoticed for a month.
- **USA publication-day checklist:** add Rule 5 supersession note to the LGF essay (both surfaces), matching the note already in technical_spec.md; swap the Trump Accounts postscript's "coming soon in this series" line for a real link; re-add USA links where the Relationship section was cut if the linked essays are published by then; add the USA post's slug to `SUBSTACK_SLUGS` in internal/scripts/substack_export.py.
- **"What's Next" refresh on index.md.** Update as stubs get promoted to full essays.
- **index.md bundled edit pass (when Matt returns, ~7/29):** one pass, one Substack re-sync — (a) dated "note on scope" block per 2026-07-23 decision (draft language in that session), (b) June SALT-credit drift fix, (c) What's-Next refresh pointing at Buy Save Die. Bump `substack_synced` after.
- **Regenerate `assets/lifetime-gains-framework.png`.** The image live in the published LGF essay still shows the old $2.5M/$10M calibration; spec at `internal/image-specs/lifetime-gains-infographic-spec.md` is current ($2M/$6M, $4M/$12M MFJ). Published-surface error — regenerate from the spec prompt, replace on both surfaces.
- **Project rename.** Public brand is "The Tax Refactor" everywhere. As of June 2026, all human-readable "Fair and Simple Tax Act"/"Fair and Simple Tax Project" references in essays and process docs were replaced with "The Tax Refactor." Repo name, site slug, and URLs remain `fair-and-simple-tax-act` for SEO continuity (URL migration still deferred). Archive files under `internal/archive/` left as historical record.
