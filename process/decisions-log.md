# Decisions Log

Key decisions made while developing The Tax Refactor project, with the reasoning behind each. The goal is to capture the *why* so future-us (or a new collaborator) doesn't relitigate settled ground.

## Process Rules

### Published doc closure rule
Any document linked from a published document must itself be published. The set of "published" files is the transitive closure of links starting from `index.md`, not just the essays we happen to be talking about at any given moment. Reason: broken links or 404s in a published doc are worse than having an unfinished stub live. If a stub is linked from `index.md`, the stub is published — even if it's still rough. How to apply: before moving any file out of the Jekyll deploy root, grep for inbound links from published docs. If any exist, either the file stays, or the link gets removed first.

## Framing & Architecture

### Lifetime Gains is "first and most fully developed," not "the centerpiece"
Calling it the centerpiece undermined the modular intent of the project. The framework is a system of independently shippable components; elevating one piece rhetorically makes the others look like afterthoughts. "First and most fully developed proposal" preserves the ordering without implying subordination.

### "Simple system architecture," not "microservices"
We briefly framed the project as a microservices architecture for the citizen-government fiscal relationship. "Microservices" is trendy tech jargon that dates quickly and alienates non-technical readers. "Simple system architecture" captures the same idea (clean interfaces, independent components, monolith-to-modules) in plain language.

### Tenet 3 avoids "99%" language
Early drafts leaned on "the 99%" framing. Too overtly political; it codes the whole project as partisan and narrows the audience. Final wording: "Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility." Keeps the moral claim, drops the political tribal signal.

## Scope

### Corporate taxation is out of scope
Including corporate reform would triple the surface area of the project and entangle it in debates (pass-through treatment, international rules, book vs. tax income) that are orthogonal to the core thesis. Scoped out explicitly in index.md. The Phase 2 PRFAQ handles S-corp pass-through recharacterization via Market Compensation Requirement (MCR) as a targeted exception.

### Healthcare tax treatment is out of scope
The employer health insurance exclusion is ~$300B/yr — the largest tax expenditure in the code — but touching it conflates tax reform with healthcare policy, which is a third rail and a separate debate. Scoped out explicitly. We retain a medical cost credit to protect against catastrophic out-of-pocket costs, but we do not restructure employer-provided coverage.

### Pre-enactment gains are not retroactively counted
On day one of enactment, everyone's lifetime counter starts at $0. Retroactive counting would be politically impossible, administratively nightmarish (basis reconstruction for decades-old assets), and legally vulnerable. Clean slate is the only workable design.

## Capital Gains Framework

### Loan as a realization event
Loans, like sales, are "natural" arm's-length transactions with observable valuations. That makes them a clean realization trigger. Gifts and death are messier (no arm's-length counterparty), but donor/recipient basis tension partially mitigates gift valuation, and existing IRS qualified appraisal infrastructure handles death valuation. Not perfect, but adequate — no structural change warranted now.

### Zero-gain collateral edge case: do nothing
Added to the technical spec. Three reasons to leave it alone: (1) opportunity cost of chasing edge cases, (2) the framework itself eliminates the motivation for the edge case (no buy-borrow-die benefit if death triggers realization), (3) systemic design beats point fixes. Fox & Liscow (2024) cited.

### $500B compliance stat gets a qualifier
Using the whole-code compliance figure to motivate a capital-gains-only proposal is disingenuous. Added language acknowledging capital gains is one piece of the burden but generates disproportionate complexity.

### NIIT is not part of the AMT lineage
Initial draft implied a causal chain from AMT to NIIT. NIIT was ACA funding, not a response to buy-borrow-die. Corrected in lifetime-gains-essay.md.

### Gift de minimis (rejected)
All appreciated-asset gifts trigger cap-gains realization with no carve-out. Considered a $25-50K/yr de minimis threshold to spare small intra-family transfers (e.g., shares gifted to a grandkid) from triggering realization tax on small embedded gains. Rejected on architectural-simplicity grounds: the "no special carve-outs" pattern is the framework's core appeal, and adding even small thresholds opens a defense surface (where does the threshold sit? does it index? does it stack with other exclusions?). The sympathetic-grandparent case is real but bounded; the realization tax is on the embedded gain only, and small share gifts to grandkids typically have small embedded gains anyway.

## Income Tax Essay

### Charitable and medical credits live inside the income tax essay
Originally carved out as standalone stubs. Realized they can't be teased apart from deduction elimination — if you kill all deductions, you have to say what replaces the two that matter most (charitable, medical) in the same breath. Folded back in. The charitable-giving-essay.md file was repurposed as a deeper-dive companion covering DAF tension and appreciated-asset realization.

### Charitable credit: 25% of donation, capped at 3% of tax liability
**(Recalibrated from prior 50%/5% stake in the ground.)** Voluntary incentive, sized to align with international norms (UK Gift Aid ~25%, OECD ~25-30%) and to symmetrize with the SALT credit rate. The 50% rate was generous by historical standards — under current law, the max value of the charitable deduction equals the taxpayer's top bracket (37%). A 25% credit lands closer to that ceiling rather than above it, and a 3% liability cap keeps the zero-out-your-taxes abuse pattern off the table (97% of liability remains untouchable). Cost falls from ~$25-45B (50%/5%) to ~$15-25B/yr.

### Medical credit: 30% refundable, $5K threshold
Involuntary catastrophe protection. Refundability is essential because the people most exposed to catastrophic medical costs are often those with little or no tax liability. The threshold prevents it from becoming a routine subsidy for minor expenses.

### The two credits have parallel framing but different mechanics
User asked whether they should have identical structure. Pushed back: they serve different purposes (voluntary giving vs. involuntary catastrophe), so % of liability cap works for charitable but refundability is structurally required for medical. Parallel in spirit, different in mechanism.

### Filing status: five to two
Collapses Single, MFJ, MFS, HoH, QW into just Single and Joint. Simplification for its own sake — the current five-status system creates edge cases and marriage penalties with no corresponding benefit.

### SALT: kept as a credit, not eliminated
**(Reverses the earlier "eliminate entirely" position from index.md and income-tax-essay.md.)** State and local taxes are recognized via a federal credit at the rate of 25% of estimated state+local taxes paid (stake in the ground; calibration to be finalized when income-tax-essay is written for real), capped at ~15% of federal tax liability (stake; range 10-20% defensible). Mechanism: a Treasury-maintained presumptive lookup table by income decile by state of residence, so the federal return depends on `f(income, state of residence)` rather than `f(income, actual state return)`. No state return required for federal calculation. The lookup approach extends a benefit that under current law is itemizer-only (~10% of filers) to all filers, in proportion to state taxes paid.

Rationale: federalism / Brandeis "labs of democracy" — the federal government affirmatively endorses state-level service delivery and policy experimentation, partially crediting taxes states collect to enable that. The published lifetime-gains-essay's stance on "the framework taxes the use of wealth, not its existence" pairs naturally here with "the federal income tax recognizes the state taxation you've already shouldered." Considered and rejected: full elimination (the deduction-hack essay's published position, but that argument was about the regressive deduction *mechanism*, not the underlying federalism case — moot once we move to a credit); a token flat per-filer credit ($500-1,000, no state variation — defensible but loses the federalism signal); a tighter 5% liability cap (washes out state variation entirely, becoming essentially a flat federal benefit).

To preserve the framework's Fiscal Durability footing, the SALT credit is paired with a more aggressive top bracket: 43% → ~47% on income above $750K MFJ (stake; calibration TBD — Matt has flagged $1.5M MFJ as a possible kick-up threshold for 48%). The bracket hike + LGF pin boost roughly offset the SALT credit cost within the income tax phase.

Presentation device: published bracket rates are uniform (5 brackets, equal treatment under law); the after-SALT-credit effective rate varies by state of residence and is what taxpayers experience. Both can be shown in the essay — "headline rate" vs. "your effective rate" — to make federalism visible without complicating the bracket structure.

### Phase 2 bracket structure stays at 5 brackets
Even after adding SALT credit and raising the top rate, the structure remains 0% / 12% / 22% / 35% / X% MFJ at the published thresholds, where X is currently 43% (Phase 2 published) and likely moves to ~47% to fund the credit. Adding additional brackets (e.g., a separate millionaires-surcharge tier) was considered and rejected: the radical-simplicity claim weighs heavily, and a single steeper top rate accomplishes the same revenue work as a stepped tier above it without expanding the bracket count.

## Modular Components

### Child payment consolidates CTC/ACTC/EITC/AOTC/LLC/education credits
One monthly payment replaces six overlapping programs. 2021 expanded CTC cut child poverty ~30%; the precedent exists.

### FICA reform: kill employee side, keep employer side as 8% uncapped ESNC
Employee-side FICA is regressive and visible on every paycheck. Eliminating it is a large tax cut for working people. Employer-side retained (and uncapped) as Employer Social Net Contribution. Details in social-security-prfaq.md.

### Universal Savings Account (USA) replaces 15+ account types
401(k), IRA, Roth, SEP, SIMPLE, 529, Coverdell, ABLE, HSA, FSA, HRA, 457(b), etc. Single account, $1K seed at birth, $30K annual cap, tax-free growth, $5M balance cap, contributions withdrawable anytime, qualified medical withdrawals tax-free. Legacy accounts deprecated on enactment with an optional PV-neutral conversion (redesigned June 2026 — see entry below; the old flat-12%/$1.2-1.3T framing is retired).

### USA balance cap is CPI-indexed
The $5M cap inflation-adjusts in parallel with the LGF exemption and the income tax brackets. Reason: without indexing, the cap loses ~50% of real value over 25 years and the account stops serving middle-class savers exactly when their balances would otherwise mature. The anti-dynastic purpose is preserved by the existence of any cap, not by its erosion. The counter-argument (deliberately non-indexed to force periodic political maintenance) was considered and rejected as inconsistent with Radical Simplicity.

### USA eliminates the employer match as a construct (June 2026)
No special employer-match mechanism. The USA has a single $30K annual cap that counts every dollar regardless of source (employee, employer, relative). Reasoning: today the match only adds tax-advantaged room because it lives in the gap between the employee elective limit ($23,500 in 2025) and the combined §415(c) limit ($70,000). Under one cap, an employer dollar just displaces an employee dollar for anyone saving near the cap, so the match collapses into compensation — pay it as wages and let the worker decide. This deletes ERISA nondiscrimination testing, top-heavy rules, safe harbor formulas, true-ups, and vesting (no employer-owned money to vest). Also resolves the regressivity tension: a match is a subsidy you only collect with the right employer and spare cash, re-creating the access gap the USA exists to close. Behavioral defense of the match is weak — Chetty et al. (2014, Denmark, 41M people): ~85% of savers are "passive" and barely respond to subsidies; each $1 of subsidy raises total saving ~1 cent; the responders skew wealthy. Vesting question (originally open) is dissolved by this, not answered.

### USA participation engine is auto-enrollment, not the match (June 2026)
Replaces the match's behavioral role with a payroll-level auto-enrollment default (3% escalating 1%/yr to ~10%, opt-out anytime), ported from SECURE 2.0 (2022). Because there's no employer "plan" to sponsor, auto-enrollment rides payroll instead — more universal than current law, which only fires if the employer sets up a plan. Default rate is a stake in the ground pending calibration.

### USA is post-tax only — no pre-tax option (June 2026)
Roth-style only; no Traditional/pre-tax election. Cost: workers expecting a lower retirement bracket lose the defer-high/withdraw-low arbitrage. Accepted on purpose — the Traditional-vs-Roth fork is the financial-literacy tax the essay attacks; you don't simplify it by keeping both options and a calculator. Post-tax is the honest one (no embedded IOU at withdrawal; government collects now, not on a bet about future brackets). Marginal losers are a narrow band; the lower income-tax rates + employee-side FICA elimination give most workers more to contribute. Resolves the backlog's "post-tax vs pre-tax" open question.

### USA: 529 / Coverdell / ABLE roll in tax-free (June 2026)
Already after-tax, tax-free-growth, purpose-specific accounts; the USA subsumes the purpose with fewer strings, so no conversion tax. Rolled-in balances count against the $5M balance cap (it's a balance) but not the $30K annual contribution cap (a transfer isn't a new contribution). Same treatment as Roth conversions.

### USA medical: port §213(d); no double-dip with the Phase 2 medical credit (June 2026)
Qualified medical withdrawals use the existing IRS §213(d) expense definition (the HSA list), ported wholesale rather than reinvented. The USA's tax-free medical withdrawal and the Phase 2 medical credit (30% refundable above $5K) target the same expenses, so they can't stack: a dollar covered tax-free from the USA doesn't count toward the credit base, and vice versa. Mirrors current law (can't deduct expenses paid from an HSA). Enforcement piggybacks on the same insurer/provider reporting the credit relies on. Resolves the open-questions.md double-dip item.

### USA $1K birth seed funded from general revenue (June 2026)
~$3.6B/yr (3.6M births × $1,000) ≈ 0.05% of a ~$7T federal budget. Funded from general revenue; no dedicated funding mechanism needed. Considered and set aside: endowing the seed from one-time conversion cash (rhetorically strong, but the conversion is now priced PV-neutral, so there's no windfall to endow from).

### USA $5M cap is the system's only balance cap; LGF Rule 5 retires (June 2026)
The $5M USA balance cap absorbs the separate $5M Roth balance cap proposed in Rule 5 of the Lifetime Gains Framework. One cap, one place. Rule 5 retires. (Was an explicit-reconciliation open question.)

### USA withdrawal design: qualified-withdrawal superset, not "never tax-free" (June 2026)
Resolves a multi-step design debate about how the USA's tax-free treatment should relate to the Lifetime Gains Framework (LGF). Final design: the USA allows **tax-free gains for qualified withdrawals** — retirement (after 59½), higher education, medical (§213(d)), and first home — porting definitions that 529s, HSAs, and the IRA first-time-homebuyer rule already use. Non-qualified early gains are taxed as capital gains under LGF (no penalty; $0 for most via the $2M exemption).

Paths considered and rejected:
- **"USA gains never tax-free" (all gains run through LGF; USA = pure tax-deferral wrapper; maybe raise LGF exemption).** Elegant and maximally simple, but rejected for two decisive reasons: (1) it screws the long-lived retiree, who would exhaust the $2M lifetime exemption over a multi-decade drawdown and start paying tax on their own retirement savings (a Roth never does this); (2) the converter problem — if the USA is worse than a Roth, no Roth/529/HSA holder ever migrates, and the entire consolidation thesis collapses. You can't build a unifying account that's a downgrade from the things it unifies.
- **Pure-Roth basis rule (pre-59½ tax-free only up to contributions/basis).** Clean, but reintroduces tax drag on college/medical/home gains — a regression from 529s/HSAs — which again blocks conversion.
- **Self-contained USA (no LGF interaction at all).** Would force either taxing college withdrawals or re-adding purpose definitions; no better than the chosen design and less generous.

Why qualified withdrawals win: consolidation only happens if the USA is a true **superset** of the accounts it replaces. The modest cost (porting three battle-tested purpose definitions) is far less than 15 separate account rule-sets, and it's ported, not invented. Deliberately excluded: "business/startup" as a qualified purpose (no clean definition, biggest abuse surface).

Framing point (belongs in essay): the USA doesn't *abolish* the allocation decision, it *relocates* it — from a blind, up-front, hard-to-reverse "how much in each account?" guess at 25, to a single informed "spend now or leave it compounding?" question asked only when money is needed, with a good default (leave it). Late-with-facts beats early-with-guesses.

Also decided: **dropped the $2.5M tax-free-withdrawal sublimit** (the $5M balance cap is the sole anti-shelter limit) for simplicity — flagged for confirmation. **59½** retained as a familiarity port from Roth/IRA (acknowledged-arbitrary; round 60/65 was considered). This resolves the `open-questions.md` "post-tax vs pre-tax / USA-LGF overlap" thread.

**Amendment (June 2026, reader feedback): 10% surcharge restored on non-qualified early gains.** Routing non-qualified early gains through LGF made them $0-tax for most people (the $2M exemption covers them), which inadvertently removed *all* friction — the "you lose the tax-free wrapper" brake is toothless when there's no tax to lose. So a 10% surcharge is restored as the commitment device, applied *only* to gains pulled early for non-qualified reasons (never contributions, never qualified withdrawals). Contributions stay fully liquid, so emergency access is preserved; the surcharge protects only the growth. Ports the established 401(k)/IRA/Roth early-withdrawal penalty. Also confirmed: USA gains get long-term capital-gains treatment regardless of internal holding period (no short-term/long-term lot tracking).

### USA onboarding: private custody behind a neutral default router (June 2026, reader proposal)
Fills a gap the essay had hand-waved ("auto-enrollment as payroll default" never specified who holds the money). Design keeps the government out of asset management (avoids the failed myRA and the "government picks your fund" attack): certified private brokerages offer a fee-capped "baseline tier" with a low-cost index target-date default; a stateless federal clearinghouse (holds no capital) round-robin-assigns silent savers who haven't chosen a provider; one-click portability preserves choice. Key economic insight: the $0 customer-acquisition-cost effect (free automated customer flow) makes small-dollar accounts profitable to serve, turning the industry from obstacle into constituency — reinforces the "Wall Street isn't monolithic" FAQ. Flagged risks: federal account-matching IT is a real dependency (healthcare.gov-class launch risk), KYC/fraud for lottery-created accounts, and the lottery quality floor rests entirely on the baseline-tier specs. Alternative considered: default to the saver's existing bank (better recognition) vs. blind lottery (better neutrality/no favoritism). Full technical detail (exact bps caps, API mechanics) deferred to a possible technical addendum.

### Great Conversion redesigned: deprecation-first + optional PV-neutral conversion (June 2026)
Replaces the original "flat 12% over a 10-year window → ~$1.2–1.3T one-time revenue" design. Two reasons it changed. (1) **The math didn't close and the framing was dishonest.** A conversion rate below the expected withdrawal rate is PV-negative for Treasury: collecting (say) 12% today on a balance that would be taxed at ~30% in 20 years books gross cash now but gives up more in present value. The "$1.2–1.3T windfall" counted the cash and ignored the forgone future stream. (2) **The trilemma.** Fast/universal conversion, near-term debt paydown, and not deepening the long-run deficit can't all hold — a carrot deep enough to convert everyone necessarily deepens the deficit. Matt's binding constraint is "don't deepen the deficit," so that wins.

New design: **(a) Deprecation is the baseline** — on enactment, legacy account types close to new accounts and new contributions; all new saving flows to the USA; existing balances run off under old rules over their holders' lifetimes. Zero cost, near-zero risk, and it delivers the forward-looking simplification on its own (new entrants deal with one account; payroll/contribution rules simplify immediately). The only thing given up is speed (two systems coexist for a generation). **(b) Optional conversion priced PV-neutral** — after-tax accounts (Roth, 529, Coverdell, ABLE) roll in tax-free; pre-tax accounts pay a rate set so Treasury breaks even between collecting now and later. No discount carrot means no giveaway and no regressive windfall to large balances; converters self-select as people who value simplicity/certainty. It still pulls revenue forward (near-term debt paydown at no net long-run cost). No deadline/cliff. Rate is a placeholder; solve via simulation for the PV-neutral point (or a deliberately budgeted cost), modeling uptake by age/balance/horizon. Considered and rejected: revenue-maximizing (out-year hole), deep-discount migration-max (giveaway, deepens deficit). Eligibility cap on the low rate left as an open calibration flag rather than decided. Note: this demotes the standalone "Great Conversion" essay's revenue rationale; revisit that plan and possibly the name.

### USA inheritance follows current Roth IRA rules (SECURE Act 2019)
Spouse: treat-as-own rollover, lifetime continuation, no drain. Non-spouse heirs: separate Inherited USA, full drain within 10 years, tax-free during the window, no annual RMDs, drained balance exits to taxable brokerage at FMV basis. Eligible Designated Beneficiaries (minor child of decedent, disabled, chronically ill, beneficiary not more than 10 years younger) get lifetime stretch. We also considered C-only (immediate exit to brokerage at FMV; cleaner but loses the rhetorical offset to estate tax elimination) and C+A (full rollover into heir's USA up to cap; more generous than current Roth law, opens the trust-fund-kid optic). The Roth port is the middle ground: matches established convention, sidesteps the need to defend new architecture, and bounds intergenerational continuation to 10 years for non-spouse heirs. Defense reduces to "same as Roth, applied to USA."

## Publishing & Infrastructure

### Jekyll site.url for absolute URLs
Rather than hardcoding mattsly.com in every image path for OG/Twitter cards, added `url: "https://www.mattsly.com"` to _config.yml and let jekyll-seo-tag prepend it automatically. Template variable, not hardcoded strings.

### Twitter card: summary_large_image
Frontmatter on lifetime-gains-essay.md specifies the large image card for better social sharing.

### Outgoing links stay same-tab
User preference: ctrl-click is fine, don't force new tabs.
