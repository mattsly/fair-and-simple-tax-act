## ROBINHOOD Act — loan-as-realization in Congress (added 2026-07-23)

Two bills, same brand, different architecture. Together they show Congress converging on LGF Rule 3's borrowing trigger. Nowhere in the repo until now; this is the strongest external validation of the loan-as-realization design to date.

### Goldman version (House, Dec 2025)
[Press release](https://goldman.house.gov/media/press-releases/rep-dan-goldman-introduces-new-tax-wealthiest-americans-generating-estimated). A 20% **excise tax on the loan itself** — not a realization rule.

- Applies to individuals with income over $400K ($450K joint).
- No basis adjustment → double taxation: 20% on the loan now, full capital gains on the same appreciation at eventual sale.
- Carve-outs gut it: home mortgages, HELOCs, **margin loans** (the closest substitute for the SBLOCs it targets), farmland credit.
- Revenue claim: $276B/10yr, from $138B outstanding securities-backed loans ([Fed estimate, Q1 2024](https://www.federalreserve.gov/econres/notes/feds-notes/estimating-securities-based-loans-outstanding-20240802.html)). Math is mushy — $138B × 20% = $27.6B once.
- Attacked from the right as a wealth tax (S-Corp Assn, "Wealth Tax Mania Spreads East," Dec 2025) despite the $400K threshold and excise design.

### Gallego version (Senate, May 2026)
[Full text (PDF)](https://www.gallego.senate.gov/wp-content/uploads/2026/05/260528-ROBINHOOD-Act_Final-Text.pdf) · [press release](https://www.gallego.senate.gov/news/press-releases/gallego-introduces-legislation-to-crack-down-on-billionaire-tax-loophole/). Fixed the architecture and narrowed the target:

- **Deemed realization, gain-equal-to-loan:** taxpayer *identifies* long-term lots whose combined gain ≥ loan amount; those lots deemed sold at FMV (§1299(a)). Basis steps up to FMV on identified lots (§1299(b)). Elective lot-ID = no collateral disputes, no LTV fights.
- Note it's gain = loan amount, not proceeds = loan — slightly harsher than a real sale ($1M loan on 90%-gain stock recognizes $1M, vs $900K on an actual $1M sale).
- **Applicable taxpayer:** income >$100M OR assets >$1B, met **each of 3 preceding years**; sticky status (exit requires 3 years below *half* thresholds + election). Trusts at $10M/$100M. Entity look-through with §318 constructive ownership. Expat 10-year tail.
- **Existing loans swept in:** outstanding balances deemed a single new loan on Jan 1, 2027 — retroactive teeth for existing buy-borrow-die stacks.
- Leases >5 years treated as loans (anti-avoidance).
- Nontradable valuation floor includes "value used to secure indebtedness" (§1299B(d)(2)(E)) — the same LTV-floor logic as our technical_spec, independently arrived at.
- Warts: no capital-loss offset against deemed gains (punitive, asymmetric); no basis step-up for depreciable property (double-tax landmine for real estate); "any loan issued" appears to re-tax refinancings (no netting / high-water-mark rule).

### Analysis vs. LGF

- **The complexity lives in the cliff:** ~22 of the bill's 29 pages (Secs. 1299A/1299B — lookbacks, sticky status, divorce/expat/trust rules, six-way "greatest of" valuation) exist solely to define *who's covered*. The mechanism fits in ~7. An exemption parameter deletes the 22.
- **Lifetime-counter gate has a circularity problem:** a gate keyed to past *realized* gains never triggers for the disciplined never-seller — the gated activity (borrowing) is what would fill the counter. Fix = count loan-deemed gains for everyone, tax only above the exemption… which is no longer a coverage test, it's the LGF. One-sentence pitch to Gallego/Goldman staff: *don't define who's covered, define what's exempt.*
- **Evolution arc (essay frame):** excise on debt → realization of gain → (next) exemption instead of class test. "This bill is two revisions away from the Lifetime Gains Framework." Generous framing matters if the audience includes their staff.
- **Measurement rule — candidate LGF spec change (needs open-questions.md entry):** gain-equal-to-loan with taxpayer lot-ID may beat our collateral-gain rule. At 30% LTV, $30M loan / $10M-basis $100M pledge: collateral rule taxes $22.5M (75% of proceeds); loan rule taxes $7.5M (25%). Loan rule invariant: tax ≤ rate × proceeds, always payable from the loan. Also kills blanket-lien/margin/substitution ambiguity. Needs: default ordering rule + high-water-mark rule for serial borrowing. Since death is closed under LGF, the collateral rule's extra harshness buys nothing.
- **Second open question (needs open-questions.md entry):** under a universal rule, ordinary transactions burn exemption room (a $200K cash-out refi on an appreciated home = $200K of deemed gain at 0% but −10% of lifetime room). Demagoguable ("government tracks your mortgage"). Need a §121-style answer for primary residences or a principled defense of room-burning.
- **Counter transition:** counter starts at zero at enactment (reconstructing lifetime history is a nonstarter) → everyone's first $2M post-enactment is free, including billionaires'. Say it before critics do.

### Ackman convergence (added 2026-07-23)

Bill Ackman proposed the identical mechanism in [Aug 2024](https://x.com/BillAckman/status/1826361874654658880): loans in excess of basis "taxable as if you sold a like amount of stock" — proceeds-based loan-as-realization, same design as Gallego's bill. He simultaneously [opposes wealth taxes as expropriation](https://x.com/BillAckman/status/2005710812359622840) (Dec 2025, re California Prop 40). Nobody has connected Ackman's proposal to the ROBINHOOD Act. **Essay hook: "the billionaire and the senator agree on how to tax billionaires — they just don't know it yet."** Strongest available proof of the centrist lane: loan-as-realization is the fix both sides reach when they reject the other's frame.

### Why ROBINHOOD got no press (attention-economics note)

0%-odds minority bill = no stakes, no coverage. Too moderate to rally the left (concedes no wealth tax), auto-filed as "wealth tax mania" by the right. Name is SEO-poisoned by the brokerage. Sponsor distracted (DOJ campaign-spending probe, July 2026 NY Post scandal coverage, competitive midterm). Implication: the explainer/reference-piece lane for loan-as-realization is empty — being early beats being loud.

### Pundit/editorial response — the premise fight (added 2026-07-23)

The serious response to ROBINHOOD attacked the *premise*, not the bill:

- **[WaPo opinion, 2026-06-05](https://www.washingtonpost.com/opinions/2026/06/05/ruben-gallego-tax-plan-is-premised-myth-buy-borrow-die/):** "Gallego's tax plan is premised on the myth of 'buy, borrow, die'."
- **[Fox & Liscow at TPC, 2026-06-15](https://taxpolicycenter.org/taxvox/richs-real-tax-trick-isnt-buy-borrow-die):** top-1% borrowing ≈ **1-2% of economic income**; unrealized gains **20-40x larger**. Coinage: **"buy, save, die"** — the dominant shelter is untaxed compounding + step-up, not loans. Only ~60% of top-1% economic income (incl. unrealized gains) is in the current tax base (~71% inflation-adjusted). They say the Gallego/Goldman bill was "informed by our analysis." Their prescription: raise rates on the existing base + reform step-up.
- **[AAF, Dec 2025](https://www.americanactionforum.org/daily-dish/robin-hood-delivers-xmas-coal/):** regulatory boondoggle, behavioral adaptation. Plus S-Corp Assn "wealth tax mania." Punchbowl covered the introduction.

**LGF implication — the counter-punch essay:** the "myth" critique kills a standalone loan bill but argues *for* the systemic framework. If the big money is buy-SAVE-die (compounding + step-up), the fix is death-as-realization — LGF Rule 3, exactly what ROBINHOOD omits. Frame: "The Post is right that buy-borrow-die is a sideshow. The main event is buy-save-die, and only closing the death exit touches it." Agree with critics, out-flank the bill.

**[Yale Budget Lab modeling, Mar 2025](https://budgetlab.yale.edu/research/buy-borrow-die-options-reforming-tax-treatment-borrowing-against-appreciated-assets):** three loan-side options — deemed realization ($102B/10yr), 10% withholding ($147B), 0.5% excise on balances ($130B). Key details: their deemed-realization variant is *universal* (no wealth test) with a $250K/person/yr exemption and **FIFO lot ordering** (vs. Gallego's taxpayer-elective ID — FIFO is the respectable anti-electivity argument for the measurement-rule open question). Their annual-vs-lifetime exemption discussion names the tradeoff: lifetime kills debt-smoothing avoidance but requires cumulative tracking (= the LGF counter). Critically: **all three options leave step-up intact**, so borrowing stays tax-advantaged when returns exceed borrowing costs — loan-side patches can't reach the main shelter. Current-law tax advantage of borrowing vs. selling: ~12pp.

**Outreach implications:**
- **Fox (Michigan) & Liscow (Yale Law)** are the intellectual center of the debate; technical_spec already cites their 2024 paper; backlog already has a comparison piece. High-value academic outreach: LGF is the systemic answer to the limitation they keep flagging.
- **Ray Madoff's book "The Second Estate"** is the cultural engine of buy-borrow-die discourse ([Ezra Klein interview, 2026-04-17](https://www.nytimes.com/2026/04/17/opinion/ezra-klein-podcast-ray-madoff.html)). Existing contact; backlog's "read Madoff book" item now urgent.

### WaPo "myth" piece — full read (added 2026-07-23)

[WaPo Opinions, 2026-06-05](https://www.washingtonpost.com/opinions/2026/06/05/ruben-gallego-tax-plan-is-premised-myth-buy-borrow-die/) (Matt has gift link; byline/board status unverified). Claims and data:

- Cites [Fox & Liscow (Michigan/Yale)](https://repository.law.umich.edu/cgi/viewcontent.cgi?article=1397&context=law_econ_current): top-1% new borrowing ≈ 2% of economic income (incl. unrealized gains); their liquid income exceeds consumption; median top-1% household has 56% of economic income subject to income tax and **median debt/wealth = 0%**.
- Argument: strategy is rare → bill is "policy untethered from reality"; US income tax already very progressive; top-1% revenue share rising.
- Uses home-equity analogy (borrowing doesn't avoid tax for wage earners).

Observed omissions/weaknesses (facts, not framing):

- Never addresses stepped-up basis, though its own ¶2 describes it; Fox & Liscow's [TPC piece (6/15)](https://taxpolicycenter.org/taxvox/richs-real-tax-trick-isnt-buy-borrow-die) calls step-up "indefensible" and recommends reforming it — the op-ed cites the debunking half of its source and omits the prescription half.
- Median statistics can't detect a top-400 tail behavior; aggregate top-1% borrowing >$1T (Yale) and Musk's $94B pledge coexist with median debt/wealth = 0%.
- "56% subject to tax" ⇒ 44% of median top-1% economic income outside the tax base (worse at the tail: ProPublica 3.4% top-25 effective rate).
- Home-equity analogy assumes already-taxed wages — inapplicable to zero-salary low-basis founders.
- Context: post-2025 WaPo opinion-section mandate shift; keep provenance separate from substance in any response.

### Fox & Liscow key fact sheet (added 2026-07-23)

[Yale fact sheet, Jan 2025](https://economics.yale.edu/sites/default/files/publication-documents/2025-01/UnrealizedGainsandTaxesKeyFactSheet.pdf), summarizing ["The Role of Unrealized Gains and Borrowing in the Taxation of the Rich"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5104644):

- **Share of economic income (incl. unrealized gains) captured by current tax base, by wealth percentile: 90-99th = 75%; 99.0-99.9th = 67%; top 0.1% = 50.2%.** Top 1% overall ≈ 60% (70% inflation-adjusted). The leak worsens as wealth rises — the gradient, not the average, is the LGF-relevant fact.
- **Tail outlier stat (their own):** Musk + Bezos + Buffett, 2014-2018: $137B asset growth vs. $5.7B tax-recognized income = **4%**.
- Top-1% borrowing = 1-2% of economic income; 50-90th percentiles borrowed a *higher share* of their unrealized gains (~2x) than the top 1% — borrowing against gains is more middle-class than billionaire behavior.
- Methodology note: they estimate *actual* unrealized gains per group (not assumed standard returns) — the credibility edge over prior economic-income studies.
- Their policy conclusion: raise ordinary + cap-gains rates on the existing base. (Tension to note: higher realization-based rates raise the value of deferral + step-up, strengthening buy-save-die unless the death exit is closed — rates and realization rules are complements.)

Reading path for reactions: Heath, [NYU L. Rev. note](https://www.nyulawreview.org/wp-content/uploads/2024/05/99-NYU-L-Rev-717.pdf) (taxing the borrow leg); Chamberlain, ["Borrowing as Realization,"](https://digitalcommons.law.buffalo.edu/buffalolawreview/vol73/iss2/6/) Buffalo L. Rev. (academic case for the mechanism); plus WaPo 6/5 and TPC 6/15 entries above.

### Fox & Liscow full paper — key stats (added 2026-07-23)

Read from `internal/fox-liscow.pdf` (Michigan Law & Econ WP 286, Jan 2025). Data: SCF 2004-2022 (oversamples rich; 256 households >$62M in 2022 wave) + Forbes 400 bolted on separately. Wealth cutoffs 2022: top 1% = $14M; top 0.1% = $62M.

- **Tax-base capture gradient (share of economic income in AGI, 2004-22 avg):** bottom 50% = 98%; 50-90th = 87%; 90-99th = 75%; 99-99.9th = 67%; top 0.1% ex-Forbes = 50.2%; **Forbes 400 = 48.1%**.
- **Average tax rate on economic income INVERTS at the top:** rises to 15.8% (99-99.9th), then falls — 12.1% (top 0.1%), **9.6% (Forbes 400) vs. 8.6% (50-90th percentiles)**. The 400 richest pay ≈ upper-middle-class average rates. Matches Yagan (2023) independently. [Chart candidate for Two Kinds of Rich / Buy Save Die.]
- **Composition, top 0.1%:** realized + unrealized gains = 73% of economic income; salary only 6%. Only ~27% of top-0.1% income is rate-hike-inelastic AGI types.
- **Borrowing detail:** top-1% debt stock $1.02T (66% is mortgages; 12% margin); new borrowing $62B/yr ≈ 2% of economic income (0.1%: 1.0%; 99-99.9: 2.4%). Forcing all borrowing into sales would raise top average rates only ~0.2pp. Forbes 400 borrowing not in SCF; F&L 2024 estimate ~$100B existing stock, new borrowing <2% of economic income.
- **Bimodal distribution rescues BBD from "myth":** 55% of top 1% borrow <0.1% of wealth, but **~15% borrow >5% of wealth, and that subgroup's borrowing ≈ 68% of its unrealized gains** (Appendix Fig 6 — verify against table before citing). Honest framing: not the dominant class strategy; a meaningful minority runs it hard. LGF loan rule = integrity valve, not revenue engine.
- **Unrealized-gain reservoirs (2022):** 90-99.9th ≈ $35T; top 1% ≈ $23T; top 0.1% ≈ $13.7T. Death exit reaches these; borrowing taxes reach ~$62B/yr of flow.
- Alternative capture measures: inflation-adjusted 71%; step-up/deferral-adjusted 59%; both 70%.

### Stats worth citing

- Next-richest 1% (beyond top 400) borrowed **>$1T in 2022 alone** ([Yale, role of unrealized gains and borrowing](https://economics.yale.edu/research/role-unrealized-gains-and-borrowing-taxation-rich)) — best single number for sizing buy-borrow-die.
- Musk had pledged **$94B** of Tesla shares as loan collateral as of 2022 (Forbes).
- ProPublica 2021: top-25 average effective rate **3.4%** (Musk 3.3%, Bezos 1%, Buffett 0.1%).
- $138B outstanding securities-backed loans (Fed, Q1 2024).

---

A few strong data points to consider adding:

**Tax Compliance Confidence:**
- IRS data shows ~40% of filers use professional tax prep services (H&R Block, tax attorneys, CPAs)
- Survey data: Only ~30% of Americans say they "fully understand" their tax obligations
- Gallup/AARP polls show majority of Americans find tax code "too complicated"

**Time Burden:**
- IRS estimates 7.1 billion hours annually on tax compliance (you cite this)
- That's roughly 21 hours per household per year
- Adds up to ~$213B in economic value lost to compliance alone

**Tax Gap:**
- IRS reports $600B+ annual "tax gap" (taxes owed but uncollected)
- Higher on capital gains and business income due to complexity
- Simplification directly improves collection rates

**Error Rates:**
- IRS audit data shows higher error rates on itemized deductions and complex credits
- EITC error rate ~24% (overpayment or underpayment)
- Simplification reduces these administrative errors

**Key Sources to Cite:**
- IRS Data Book (annual, public)
- Federal Reserve Survey of Consumer Finances
- Brookings Institution reports on tax compliance
- Tax Foundation studies on compliance burden

I'd recommend adding a sentence or two around **line 3-4** of the press release noting: *"[X]% of Americans lack confidence in their tax filing, and the average household spends 21 hours annually on compliance."* This sets emotional stakes before launching into policy.


---

### Q19 passthrough draft (15% annual capital return) — condensed summary

* Proposed a 15% annual capital-return allowance (up to 10 years) on documented owner capital; excess profit taxed as ordinary income; capital-return amounts counted against the $1.5M lifetime exemption; capital gains at exit still available.
* Goal: end S-corp wage/distribution arbitrage, curb carried-interest treatment, and reward documented risk-taking; S-corp vs LLC choice becomes tax-neutral.
* Examples showed ~31% effective rates on $500K profit with $200K invested; modest revenue gain from closing arbitrage (~$15–25B net after allowing the preference).
* Mechanics: salary optimization becomes irrelevant; allowance expires after 10 years; “use it or lose it” each year; lifetime exemption brake limits double-dipping.

### Why we didn’t adopt the 15% capital-return approach

* **Complexity vs. simplicity goal:** Annual capital-base tracking, documentation tests, and 10-year timers add moving parts; harder to message than a salary floor plus a single residual allowance percentage.
* **Audit/gaming risk:** Fair-market-value disputes on contributed property; timing games on capital infusions; pressure to inflate basis to grow the 15% benefit.
* **Uneven by business type:** Capital-heavy firms benefit more than sweat-heavy firms; we want a uniform rule for founders, professionals, and small services.
* **Overlap with lifetime exemption:** Annual capital-return amounts already consume the exemption, but still invite double counting debates and recordkeeping friction.
* **Fiscal uncertainty:** Revenue swing depends on capital-basis assertions; harder to bound than a flat residual percentage with a salary floor.
* **Cleaner alternative chosen:** The $120K compensation floor + 20% residual sweat-equity allowance (counting against the lifetime exemption) gives parity or better outcomes with fewer calculations and clearer guardrails.






Phases:

> **⚠️ SUPERSEDED (noted 2026-07-23).** The numbers in this phases sketch predate
> the published spec and are wrong on several points: exemption is **$2M/$4M MFJ**
> (not $1.5M); the rate **slides 0% → top ordinary rate (pegged, currently 37%),
> fully phased at $6M/$12M MFJ** (not a 0/15/20/27/32 ladder). Published
> `lifetime-gains-essay.md` + `technical_spec.md` are the source of truth.
> Kept for historical reference only.

PHASE 1: "The Billionaire Loophole Closure Act" (2025-2026)
What's in it:

Buy-borrow-die closure (asset-backed borrowing triggers deemed realization)
Simplified income tax brackets (6 brackets: 4%, 12%, 23%, 36%, 39%, 45%)
Stepped-up basis elimination (phased: $50M+ estates first 3 years, $20M+ next 3 years, then universal)
AMT/NIIT elimination + progressive lifetime capital gains rates (0% → 15% → 20% → 27% → 32%)
$1.5M lifetime capital gains exemption (replaces $500K home exclusion with universal exemption)
Pass-through & Carrieed Interest reform: $120K salary minimum + 50% of profits above salary at cap gains (counts toward exemption) + 50% ordinary income with SE tax
Universal $6,000/child benefit (consolidates CTC, EITC, childcare credits)

Revenue: $150-250B annually (when fully phased)
Political sell: "Close loopholes that only benefit ultra-wealthy, simplify taxes for everyone else by eliminating AMT/NIIT, and give every American a $1.5M lifetime exemption for building wealth."
Feasibility: HIGH - Pure loophole closure + simplification sweetener

PHASE 2: "The Social Security Solvency Act" (2027-2028)
What's in it:

Eliminate Social Security wage cap (6.2% on all wages, no ceiling)
Reduce self-employment tax 15.3% → 12%
Minor benefit reforms (means-test top 5%, raise retirement age 2 months for those under 50)

Revenue: $150-200B annually
Political sell: "Social Security trust fund depletes in 2033. This fixes it for 75+ years without cutting benefits for 95% of Americans. High earners finally contribute on all income. Small business owners get a tax cut."
Feasibility: MEDIUM-HIGH - Crisis creates urgency as 2033 approaches

PHASE 3: "The Universal Savings & Family Security Act" (2029-2030)
What's in it:
American Savings Account (ASA) - one account replaces 15+ types
Optional 12% conversion from legacy 401(k)/IRA (10-year window)

Revenue/Cost: Roughly neutral ($50-100B net cost)

USA conversion redesigned (June 2026): deprecation-first + optional PV-neutral conversion; pulls revenue forward (near-term debt paydown) but not a net raiser. Old "$1.2-1.3T one-time windfall" claim retired.

Political sell: "One retirement account instead of 15. One child benefit instead of three. Six simple brackets. Optional conversion at bargain 12% rate. This is what simplification actually looks like."
Feasibility: MEDIUM - Easier after Phases 1-2 build trust

PHASE 4: "The Final Simplification" (2031+)
What's in it:

Eliminate mortgage interest deduction (standard deduction already higher)
SALT → universal 10% credit (automatic, capped at $10K)
Charitable deduction → 30% universal credit (capped at 25% of tax liability)
Student loan interest, energy credits, home office → direct programs (outside tax code)

Revenue: $100-150B annually
Political sell: "No more hidden subsidies. Same treatment for everyone. If government wants to subsidize something, do it openly through direct programs - not buried in tax forms."
Feasibility: LOW-MEDIUM - Hardest phase, only works after 1-3 succeed

Why This Sequencing:

Phase 1 = Easy win (villains are billionaires, benefits are universal)
Phase 2 = Crisis-driven (SS depletion focuses minds)
Phase 3 = Rewards for trust (tangible benefits after proving you can execute)
Phase 4 = Cleanup (final distortions, only possible if 1-3 worked)

Total when fully implemented: $400-600B in annual deficit reduction




### Old Index PAge


The Tax Refactor is a proposal to "refactor" U.S. fiscal policy.

### Why This Matters
The U.S. tax system raises revenue in ways that are opaque, uneven, and increasingly disconnected from how Americans actually earn money and build wealth. It punishes work more reliably than wealth, rewards financial engineering over productive activity, and requires an entire parallel industry just to navigate it. The result is a system that is widely resented, poorly understood, and politically brittle.

At the same time, we are heading into a decade defined by two unavoidable realities:
1. An aging population that will put sustained pressure on Social Security and Medicare
2. A labor market that looks nothing like the one the tax code was designed for

Layering new credits on top of old deductions, or carving out yet another exception, only deepens the problem. Complexity itself has become a form of unfairness.

This proposal starts from a different premise:

If the tax code were simple, durable, and legible to ordinary citizens, many downstream problems would become easier to solve.

The policy design is based on three fundamental tenets (see below). These tenets will be referenced throughout, and are included in each independant proposal.

Phase 1 modernizes how we tax income and capital so that work, saving, and entrepreneurship are treated consistently and transparently.

Phase 2 strengthens Social Security by broadening its funding base in a way that reflects today’s economy, without cutting benefits for typical workers.

The goal is not to “win” a partisan argument or to optimize for a single constituency. It’s to build a tax system that can plausibly last: one that people can understand, comply with, and debate honestly.

A tax system that no one trusts cannot sustain a democratic society for long. This is an attempt to rebuild that trust, starting with the fundamentals.

### Why I'm Doing This

I’ve paid taxes as a student, a teacher, a W-2 employee, a startup employee, a founder, an executive, and an investor. I’ve filed as single and married, with and without kids. I’ve done my taxes by hand, used consumer software, hired professionals, filed extensions, and dealt with edge cases that only show up once you’ve lived in the system for a long time. None of this makes me special, but it does give me a wide, practical view of how the tax code actually behaves in the real world.

What stands out is not that taxes are too high or too low. It’s that the system is far more complex than it needs to be, in ways that actively distort behavior and undermine trust.

I’m a systems thinker by training and by instinct. I’ve spent my career designing and maintaining software systems, and one lesson carries across domains: complexity is not neutral. Every extra rule, exception, and workaround increases failure modes, shifts power to intermediaries, and makes honest reasoning harder. When a system becomes too complex to explain clearly, it stops being governable. The tax code now feels like a software system that has never been refactored, only patched.

I’m also an experienced product leader. Whether we like it or not, we are all customers of our government, and the tax code is how most of us interact with it most directly. For many households, taxes are the single largest “purchase” they make each year. Yet the experience is opaque, stressful, and often dependent on professional help. In any other domain, we would call that a design failure. A well-designed tax system should feel more like a simple checkout flow than a legal obstacle course. That means thinking explicitly about different user personas, defaults, automation, and clarity, not just statutory intent.

I sold a company a few years ago and now have time to work on problems that sit at the intersection of systems, numbers, and fairness. This is exactly that kind of problem. I’m not approaching it as an academic exercise or a campaign platform, but as a design challenge: how do we build a tax system that is simpler, more legible, and more durable over time?

Finally, I’m doing this as an American citizen and a parent. I’m concerned about the long-term fiscal health of the country my kids will inherit, and about a political environment that makes sensible reform feel impossible. I believe we need to find a middle ground that protects and rewards innovation and work, while also acknowledging the systemic risks of extreme and growing wealth inequality.

This proposal is an attempt to bring a fresh perspective, without a political agenda, to a system that desperately needs one.

{% include tenets.md %}

## Proposals

These proposals are intentionally written in an [Amazon-style "Working Backwards" PR-FAQ format](https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes) by [Matt Sly](https://wwww.mattsly.com). I spent much of my career in technology and product development and wrote many such documents. The format is an effective way to present new ideas, establish clear design tenets, and make assumptions and tradeoffs explicit.

As a major caveat - I am not a career policy professional. I’m a quasi-retired software entrepreneur. I am approaching the U.S. tax code as a product that has accumulated complexity over decades without a clear owner and is not serving its customers well. My goal is to help “refactor” the tax code by simplifying where possible, reducing the hidden costs of complexity and edge cases, and making fiscal tradeoffs legible to both policymakers and the public.

Each proposal can be enacted independently, but they are designed together and can be calibrated as part of a single fiscal system.

#### [Phase 1: Income Tax Reform](phase_1_income_tax_reform_pr_faq.md) Eliminate loopholes and complexity, introduce new top bracket, universal child credit, and a **Lifetime Tax-Free Capital Gains Allowance** with a lifetime rate table. 

#### [Phase 2: Social Security Modernization](social-security-prfaq.md): Restore solvency and protect current and future retirees.

#### Phase 3: American Opportunity Accounts (Coming Soon)

## Fiscal Sustainability Summary

This project is designed to be additive across phases, but it does not replace the need for spending reform.

### **Current Fiscal Baseline (Illustrative)**

| Metric | Current | Sustainable Target | Gap to Close |
| :---- | :---- | :---- | :---- |
| **Federal Deficit** | ~\$1.7T (~6% of GDP) | ~\$840B–1.14T (3–4% of GDP) | ~\$600B–1.12T annually |
| **Over 10 Years** | ~\$17T of deficit | ~\$8.4T–11.4T sustainable | Need to reduce by ~$6.0T–11.2T |

### **Project Impact (Illustrative Annual)**

| Component | Annual Impact | Notes |
| :---- | :---- | :---- |
| **Phase 1** | **\$200–310B** | Base‑broadening and loophole closure |
| **Phase 2** | **\$310–350B** | Long‑run Social Security gap reduction (steady‑state, illustrative) |
| **Interest Savings** | **\$20–50B (near‑term)** | Scales over time with debt avoided and rates |

### **What Remains**

On optimistic assumptions, Phase 1 + Phase 2 + interest savings can close most (or even all) of the near‑term deficit gap. On conservative assumptions, a meaningful gap remains, so **targeted spending cuts and modernization** are still likely needed.

*Note:* Interest savings are small in the early years and grow as avoided debt accumulates. A simple rule of thumb is **interest savings ≈ cumulative debt avoided × average interest rate**.
Example (10‑year, 4%): avoiding $6T of cumulative borrowing implies roughly **$240B/year** in interest savings once fully phased in.





- **Radical simplicity**, so the system can be understood, automated, and debated honestly.  
- **Fueling the climb rather than protecting the summit**, rewarding work, saving, and entrepreneurship instead of complexity or dynastic advantage.  
- **Fiscal durability**, so today’s policies do not quietly shift costs onto future generations.

