# Tax Refactor: Project Handoff

*Compiled Oct 12, 2026 from the old "Tax Refactor - Chat Version" project. Paste this into the first chat of the new project (or commit it to `/process/handoff.md` in the repo). Facts below were stated by Matt in past chats unless marked as an open question.*

---

## 1. Setup checklist for the new project

- [ ] **Re-add GitHub sync**: `mattsly/fair-and-simple-tax-act`, branch `master`. Old include filters: `/drafts/`, `/process/`, `/internal/`, `/index.md`, `/README.md`, `/technical_spec.md`, `/dear-tech-bros.md`, `/gemstone-essay.md`, `/the-deduction-hack.md`, `/lifetime-gains-essay.md`, `/trump-accounts-essay.md`, `/warren-wealth-tax-oped-v7.md`. Consider just including the whole repo so new essays don't need new filters.
- [ ] **Upload the Writing Style Guide doc** (the single home for the full guide).
- [ ] **Decide on the "Lifetime Gains Framework" doc**: it likely duplicates `lifetime-gains-essay.md` in the repo. Diff them; drop it if there's nothing unique.
- [ ] **Set the project description** (see open question #1).
- [ ] **Paste trimmed instructions** (section 2).
- [ ] **Seed project memory** from section 3 (ask Claude to file it), or keep it in the repo instead.

---

## 2. Proposed project instructions (trimmed)

> Published work: taxrefactor.substack.com — Introducing the Tax Refactor; The Lifetime Gains Framework; The Magic Gemstone; Senator Warren Is Right About the Problem.
>
> Goal: a pragmatic, centrist federal tax policy built on four tenets: Radical Simplicity, Fiscal Durability, Fueling the Climb to the Middle Class, Ensuring Incentive for Innovation.
>
> Moral foundation: modified Rawls. The veil of ignorance applies most strongly to circumstances of birth. Social investment is densest in childhood and adolescence, phases down to a minimum in mid-career as personal responsibility phases up, and thickens again in retirement. Mid-life catastrophic luck gets targeted programs (SSDI, medical expense provisions), not a thick universal adult floor.
>
> How to collaborate: simple, clear, brief. Use data. Question my assumptions, steelman objections, push back. Show arithmetic explicitly. Flag scope creep and park new ideas in the backlog.
>
> Writing in my voice: follow the Writing Style Guide doc. Short version: conversational and irreverent, short sentences, specific numbers, parenthetical asides, self-deprecating humor, no em dashes, no emoji, no bullet points in essays, no corporate language. Open with a concrete scene or fact; end with an image, not a summary.
>
> Source of truth: the GitHub repo (`backlog.md` and essay files). Project knowledge syncs from it.

---

## 3. Durable context (for project memory)

### Proposal core
- Comprehensive federal tax reform proposal (Fair & Simple Tax Act / FAST), published as The Tax Refactor. Structured as an Amazon PR/FAQ.
- Bipartisan appeal through radical simplification and loophole closure (stepped-up basis, buy-borrow-die, carried interest).
- Core mechanics: Lifetime Gains Framework with constructive realization triggers (death as a realization event), lifetime $1.5M exemption, capital gains annualization, simplified savings accounts (ARA, AOA), FICA restructuring.
- Appendices done: taxpayer case studies and borrowing-rule scenarios.
- Prior analysis concluded: Trump Accounts are inferior to existing vehicles for most uses; Michael Green's estate tax proposal is architecturally weaker than LGF.

### Design principles and learnings
- **Architecture is the argument; calibration is the negotiation.** Shrinks the legislative debate surface.
- **Ride existing rails.** Extend existing mechanisms (§877A exit tax as precedent for death-as-realization; §1.937-2(f) pro-rata allocation as precedent for state-level sourcing).
- **Surface area, not just simplicity.** The real danger is new machinery that needs new measurement, valuation, or admin infrastructure.
- **Political reversal pattern.** Tax provisions often produce the opposite long-run political effect (employer-based health care).
- **Fewer programs, fatter checks.** When cutting provisions, overcompensate with generous universal benefits.
- **Documents can be more complex if the resulting policy is simpler.** The test for combining and sequencing essays.
- **Cash over bureaucracy.** Moynihan/Friedman/Lenkowsky lineage.
- **Lobbying pressure moves upstream.** If implementation is automated, tenet-setting becomes the battleground; vague tenets are easier to game.
- **Two-dial income framework:** characterize by basis and timing of receipt, not source (labor vs. capital).
- **Lock-in effects apply to voluntary realization;** LGF's mandatory death trigger mostly sidesteps that debate.
- **Fragmentation under a recipient-side inheritance tax** is self-limiting at large fortunes and can't be designed away under any progressive system.
- **"Redundant windfall"** is the strongest argument against QSBS under LGF.

### Ways of working
- **Two-instance workflow:** chat Claude for strategy, stress-testing, voice, structure. CoWork Claude (file access) for mechanical drafting, find-and-replace, recalculation.
- **Spec-driven handoff:** decide in chat → write a precise CoWork spec with validation checklist → CoWork executes → paste back for review.
- Publishing pipeline: Markdown → StackEdit → Substack. mattsly.com hosts the full proposal.
- Gemini used occasionally for alternative framings.
- Matt has caught Claude's errors before (buy-borrow-die estate tax caveat, AMT-to-estate-tax causal chain, CPI adjustment). Show the math.
- Option A framing preferred: commit to the stronger structural answer.
- Recurring pattern to flag: new essay ideas outpace execution.

### Key references
Madoff, *The Second Estate*; Reid, *A Fine Mess*; Lindert; Kleven; Batchelder; Starr, *Social Transformation of American Medicine*; Saez & Zucman, *Triumph of Injustice*; Klein & Thompson, *Abundance*; Bradford X-tax (Viard & Carroll); Haltiwanger/Jarmin/Miranda (firm age vs. size); Hendren & Sprung-Keyser MVPF; Fox & Liscow (2024); Becko & Sztutman (AER, elasticity); Pluchino/Biondo/Rapisarda (2018, luck vs. talent).

---

## 4. Essay backlog (mirror as of Sept 8; repo `backlog.md` is canonical)

**Done:** Dear Tech Bros · Magic Gemstone · Warren wealth tax response · Retire the Personal Tax Deduction · Dear Congress: Just Launch USAs

**Part 1:** Tax deductions are a bizarre construct · Insane phone designed like the tax code (satire) · Tax Code Needs Product Management · Simplicity should not be political · Productizing the tax code / paying taxes should be delightful

**Part 2:** Argument against corporate taxation from the left · What are we optimizing for? · Do loopholes/credits actually change behavior? · Importance of dexterity in a dynamic world · What if AI designs and runs our tax code?

**Part 3:** Philosophy of Luck & Mobility (Money = Talent + Effort + Luck; progressive tax as insurance) · Series closer candidate: "The Confession"

---

## 5. Open questions and to-dos

### Housekeeping
1. **Tenets don't match.** The old project description says Simplicity / Fiscal Durability / *Equalizing Opportunity* / *Incentivizing Entrepreneurship*. The instructions say *Fueling the Climb to the Middle Class* / *Ensuring Incentive for Innovation*. Pick one set and use it everywhere, including on Substack.
2. **Naming sprawl.** FAST, Fair & Simple Tax Act, The Tax Refactor, LGF. Decide which is the brand and which is the bill name.
3. **Account naming.** Memory says "ARA, AOA"; a published essay title says "USAs." Confirm current names and update the repo spec.
4. **Backlog drift.** The memory mirror is from Sept 8. Reconcile it against repo `backlog.md`, then pick one canonical copy. Recommendation: the repo only, with no mirror in memory.
5. **Style guide duplication.** Keep it in one place (the doc). Keep instructions short.

### Essay decisions
6. **Merge or sequence?** "Dexterity," "AI designs the tax code," and "What are we optimizing for?" are one idea (the tax code as an adaptive system). Merge into one essay or a mini-series.
7. **Merge or sequence?** "Tax Code Needs Product Management" vs. "Productizing the Tax Code" overlap heavily. Merge, or make an explicit order.
8. **"The Confession" closer:** still needs its closing image or scene.
9. **Tax-advantaged accounts thread** ("the left's counteroffer is a 12th account"): is this already covered by "Just Launch USAs," or is it still an unwritten essay or tweet thread?
10. **Next essay to write.** The backlog has 12 items and no stated priority. Pick one.

### Policy questions still open
11. **Lifetime capital gains exemption for small shop/restaurant owners**, alongside killing 1031 and stepped-up basis: in or out? Tension: LGF already has a $1.5M lifetime exemption, and the "redundant windfall" logic used against QSBS cuts against a carve-out here too.
12. **Social Security pairing:** should savings reform be paired with SS restructuring (unbundling disability from retirement)? Still at the research stage.
13. **Health care / ESI / HSA consolidation:** research in progress; no position written.
14. **VAT as a corporate tax replacement:** explored; not decided. Connects to the Part 2 "corporate tax from the left" essay.
15. **Storefront vacancy pricing:** complementary local measure or out of scope? Scope discipline suggests out of scope.

### Outreach
16. **Rep. Auchincloss and online communities:** strategy drafted. Status unknown. Was anything sent?
