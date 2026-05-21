# Backlog

Single source of truth for what's done, in-flight, planned, and parked. Merged from the old `TODO.md`, `process-notes/future-essays.md`, and `process-notes/scratch-future.md`.

## Done (published)

Essays at the repo root, served from mattsly.com and re-posted to [taxrefactor.substack.com](https://taxrefactor.substack.com).

- **index.md** — Intro essay ("Introducing The Tax Refactor"). Lives at the site root. Establishes the project, names the four tenets (canonical prose copied from `process/tenets.md`), and frames the components.
- **lifetime-gains-essay.md** — Flagship. Lifetime capital gains framework with $2.5M exemption, phase-up, four realization events (sale, loan, gift, death).
- **technical_spec.md** — Implementation details for Lifetime Gains, including zero-gain collateral edge case.
- **warren-wealth-tax-oped-v7.md** — Op-ed positioning the framework against Warren's wealth tax. Submitted to Boston Globe (pending as of March 2026).
- **gemstone-essay.md** — "If you designed it from scratch" framing piece.
- **dear-tech-bros.md** — Direct address to Silicon Valley on QSBS, carried interest, and the framework's actual impact on founders.
- **drafts/the-deduction-hack.md** — The 1913 Bug We Never Fixed. Personal W-4 hook → complexity-is-the-point thesis → deduction architecture as one major case → two fixes (0% bracket + credits) → easy button close. Draft complete, in review.

## In progress

Active drafts in `drafts/` that are close to publishable.

- **drafts/income-tax-essay.md** — "The Index Card Tax Return." Rate table, deduction elimination, charitable + medical credits, filing status simplification. Substantively complete; not yet announced/distributed.

## Stubs awaiting expansion

Files exist in `drafts/`, content is sketched but not finished.

- **drafts/charitable-giving-essay.md** — Repurposed as a deeper-dive companion to the income-tax essay. Needs: DAF (Donor-Advised Fund) tension analysis, appreciated-asset realization treatment on charitable transfers, discussion of "change of tax owner" principle, Ray Madoff's critiques of DAF abuse (she's a contact).
- **drafts/child-payment-essay.md** — Consolidates CTC, ACTC, EITC, AOTC, LLC, and education credits into a single monthly payment. Needs: payment amounts, phase-out thresholds, age cutoffs, interaction with other benefits, 2021 expanded CTC precedent (~30% child-poverty reduction).
- **drafts/fica-reform-essay.md** — Promote from reference-heavy stub to a full standalone essay: case for eliminating employee-side FICA, why employer side is retained and uncapped at 8% as ESNC, revenue neutrality, Social Security solvency implications.
- **drafts/universal-savings-account-essay.md** — Full treatment of the $1K birth seed, $30K annual cap, $5M balance cap, contribution/withdrawal rules, the 15+ accounts it replaces, qualified medical withdrawals, The Great Conversion at 12% flat over 10 years (~$1.2-1.3T revenue), death/inheritance rules, indexing debate.
- **drafts/linkedin-post-draft.md** — LinkedIn distribution-format draft.

## Planned essays (not yet drafted)

Ranked roughly by likely impact / readiness.

### Fiscal Infrastructure First
**Thesis:** Progressives keep proposing ambitious new programs on a foundation that can't support them. Before Medicare for All, before a Green New Deal, we need a tax system that's simple enough to actually work. That's not austerity. That's infrastructure. **Connection to Abundance** thinking. Could serve as the broader frame that makes the Warren op-ed a case study rather than a one-off.

### Vibe Journalism
**Thesis:** Everyone is vibe coding. I'm trying vibe journalism. AI democratized production but not distribution. Meta-frame for the whole project. Personal/accessible tone, early-Substack candidate for audience building. Outline lives in `process/vibe-journalism-outline.md`.

### The Bribery Machine
**Thesis:** Both parties have turned the tax code into a constituency rewards system, just for different demographics. The only structural fix is a code simple enough that there's nothing to corrupt. Examples: Warren's wealth tax (left), "No tax on tips" + Mace's boat deduction (right), Opportunity Zones, MID, pass-through deduction, carried interest survival.

### Who Really Owns "Free Markets"?
**Thesis:** Republicans have abandoned free-market principles; Democrats failed to claim the actual Adam Smith tradition (externalities, anti-monopoly, labor mobility). Two angles in tension — the "rebrand" angle and the "hypocrisy" angle. Probably one essay focused on hypocrisy, with the rebrand argument as a footnote.

### Estate tax sunset
The Lifetime Gains framework makes the estate tax redundant (death is a realization event). Needs explicit piece: transition mechanics, treatment of mid-probate estates, interaction with GST tax, trust unwinding.

### AMT elimination
AMT becomes vestigial once deductions are eliminated. Short piece explaining the elimination and the simplification dividend.

### "The Great Conversion" standalone
Currently lives inside `universal-savings-account-essay.md`. The 12% flat conversion rate over a 10-year window to migrate legacy retirement accounts into USAs is a big enough idea (and a big enough revenue generator) to warrant its own treatment.

### Corporate tax companion (deferred, explicitly out-of-scope)
A short piece explaining *why* corporate reform is out of scope (and what a separate effort might look like) would preempt the obvious critique.

### Healthcare tax treatment companion (deferred, explicitly out-of-scope)
Same pattern: scoped out, but a short piece explaining why (notes the ~$300B/yr employer exclusion) defends the scope boundary.

## Idea backlog (not yet promoted to a planned essay)

Raw ideas from the old TODO. Not blocked, just not picked up yet.

- **Tax Deductions are a bizarre construct.** Apples-to-oranges critique. "Net" vs. "Gross" income. What if we could deduct Food, Housing, Transportation?
- **What if Complexity is the Point?** Political-economy umbrella. Tax resistance isn't burden size — it's felt arbitrariness. Stats anchors: Credello 51% bracket survey, Blaufus 128-study review, EITC participation, IRS Taxpayer Advocate filing burden data.
- **Government Can Build Beautiful Products.** Libertarian-trap antidote. NPS, military, GPS, SS, NIH, FAA, FDIC. Image-rich format. Strong viral candidate.
- **The Insane Phone that would be designed if it looked like the tax code.**
- **Tax Code Needs Product Management.** What is product management? We've collapsed objectives into implementation. Student loans as example. Start with the problem, agnostic to solution. Opportunity for AI usage angle.
- **Simplicity should not be political.** Historically "simple taxes" codes conservative (flat tax, free markets). Shouldn't be that way.
- **Productizing the Tax Code / Paying taxes should be delightful.**
- **An argument against corporate taxation from the left.** Don't endow corporations with this kind of agency.
- **Are loopholes (i.e. tax credits) effective to modify behavior?** Are they a good way to direct capital toward desirable outcomes — green energy etc.?
- **Importance of dexterity in a dynamic world.** AI is going to change things; we need a few levers, not a tangled mess.
- **What if we let AI design and run our tax code?** Dynamic Mobility + Resource Velocity as system-level goals (replacing Meritocracy and Capital Velocity).
- **The Philosophy of Luck & Mobility.** Money = Talent + Effort + Luck. Insurance model framing for progressive taxation.
- **"No Tax on Tips" case study.** Violates horizontal equity. Form-of-income shouldn't determine rate.
- **Student Loan Interest Deduction case study.** Behavioral subsidy via definitional mechanism. One of five overlapping higher-ed subsidies with zero coordination.
- **The Withholding Architecture.** Withholding as prediction system structurally guaranteed to be wrong. Connects to USA / post-tax architecture.
- **Studies I'd like to see run:** Can people predict their taxes? Do they remember what they paid? Do they feel they're paying the right amount?
- **The Confession (series conclusion candidate).** After N essays of architecture, turn to reader: "yeah, I know how hard this is." Entrenchment IS the argument for refactoring vs. patching.

## Deeper dives / research needed

Referenced but not yet engaged with in depth.

- **Madoff book engagement.** Read Ray Madoff's book, then discuss. Likely relevant to charitable-giving deeper dive (DAFs) and possibly estate tax sunset.
- **Fox & Liscow (2024) "No More Tax-Free Lunch for Billionaires."** Already cited in `technical_spec.md`. Their borrowing-loophole proposal overlaps with our loan-as-realization design. A comparison piece would strengthen both.
- **Field-guide comparison piece.** Lifetime Gains vs. Wyden's mark-to-market, Biden-era minimum billionaire tax, Warren's wealth tax. Compare on revenue, complexity, constitutional risk, compliance burden.

## Architectural open questions (summaries — full notes in `open-questions.md`)

- **SALT:** Deduction (eliminate per intro essay) or partial credit (federalism)? Intro said "eliminate," but federalism argument deserves real analysis. Deferred to its own essay.
- **Post-tax vs. pre-tax retirement contributions.** All-post-tax is consistent with the broader principle, but optionality has real value for declining-bracket workers; behavioral effects of auto-enrollment could weaken. Belongs in USA essay.
- **Phase 2 scope:** Single comprehensive essay (5-6K words) or three separate pieces (complexity → deductions → Phase 2 proposal)? Currently planning the three-essay approach.

## Pitch list

People worth pitching when the right essay drops. See also `auto-memory/outreach_contacts.md` for current state on individual contacts.

- Gina Raimondo
- Patriotic Millionaires
- Ray Madoff (Boston College Law) — already met in person
- Jess Tarlov
- Scott Galloway
- Mark Cuban
- Sam Harris
- Bill Maher
- Jake Auchincloss (MA-4) — email exchanges in progress
- David Scharfenberg (Globe Ideas) — neighbor, not yet pitched
- T.S. Reid — outreach notes in `internal/outreach/ts-reid-reachout.md`

## Meta / infrastructure

- **"What's Next" refresh on index.md.** Update as stubs get promoted to full essays.
- **Project rename.** Public brand is now "The Tax Refactor" (Substack). Repo and site slug remain "fair-and-simple-tax-act" — URL migration deferred.
