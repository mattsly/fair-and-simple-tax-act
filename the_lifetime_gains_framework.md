# The Lifetime Gains Framework

### A Proposal to Radically Simplify Capital Gains Taxation and Reduce Wealth Inequality in a Fiscally Durable Manner

*By Matt Sly — software entrepreneur, former teacher, and reluctant tax policy enthusiast*

---

> **How to Read the Numbers in This Proposal**
>
> This document is about structural reform, not final rates. The brackets and thresholds shown are initial calibrations meant to prove the system works and to anchor fiscal targets. Reasonable people can disagree on exact numbers; any revisions must still meet the revenue and durability goals in Tenet 2. The intent is to make the levers transparent and modelable, so debate stays focused on outcomes rather than defending a system that cannot be clearly understood, modeled, or tuned.

---

## The Problem in Three Sentences

The U.S. capital gains tax system is not one system — it is dozens of overlapping systems accumulated over a century, each with its own rates, exemptions, phase-outs, and avoidance strategies. The result is a code that theoretically taxes wealth but practically doesn't: the top 0.01% pay lower effective rates than their employees, not because the rates are low, but because the escape routes are numerous and well-mapped. Meanwhile, the political debate focuses on rate levels when the real issue is structural — a system with too many doors left open.

---

## Four Governing Tenets

Every design decision in this framework is evaluated against four tenets. When tenets conflict, the tensions are acknowledged explicitly rather than papered over.

**1. Radical Simplicity**
Fewer rules beat better rules. Every exception is an attack surface for gaming, a source of compliance cost, and a barrier to public understanding. A tax system that cannot be explained clearly cannot be governed honestly.

**2. Fiscal Durability**
The reform must be revenue-positive and survive political cycles. Revenue estimates must account for behavioral responses. Provisions should not rely on temporary sunsets or future legislative action to remain solvent.

**3. Fuel the Climb**
Most Americans should be unambiguously better off under this framework than under current law. The system should reward work, saving, and wealth-building — and should not create structural advantages that entrench dynastic wealth at the expense of economic mobility.

**4. Reward Innovation**
Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively — particularly at the early stage where risk is highest and social returns are greatest.

---

## The Framework

The core idea is simple: replace the current patchwork of capital gains taxes, exemptions, and avoidance strategies with a single progressive tax based on **lifetime cumulative capital gains**. Every American gets a generous tax-free allowance. Above that, rates rise gradually and converge with ordinary income at the top. Three expanded realization events — death, gifts, and borrowing — ensure gains cannot be deferred indefinitely. Basis is indexed to inflation so the system taxes real wealth, not measurement error.

That's it. The entire framework is defined by three global configuration inputs: an income tax table, a lifetime capital gains table, and the Consumer Price Index. Everything else follows.

### The Rate Table

| Cumulative Lifetime Capital Gains (Single) | Cumulative Lifetime Capital Gains (Joint) | Marginal Rate |
|---|---|---|
| $0 – $2M | $0 – $4M | **0%** |
| $2M – $5M | $4M – $10M | **15%** |
| $5M – $10M | $10M – $20M | **20%** |
| $10M – $25M | $20M – $50M | **30%** |
| $25M+ | $50M+ | **37%** |

**Core principle:** Capital gains rates converge with ordinary income at the top. The top rate (37%) matches the top ordinary income rate. No taxpayer ever pays more on investment income than on wages.

**The 0% bracket is the political and policy anchor.** A married couple can accumulate $4M in lifetime capital gains — across home sales, stock sales, business exits, and every other form of appreciation — and pay zero federal capital gains tax. This is more generous than current law for over 99% of American households. It is the "price of passage" that makes the entire framework politically viable.

### Inflation-Indexed Basis

All cost basis is adjusted for inflation using the Consumer Price Index. When an asset is sold, the basis is adjusted from the purchase date to the sale date: `adjusted_basis = original_basis × (CPI_sale / CPI_purchase)`.

This ensures the framework taxes real gains, not phantom gains from purchasing power erosion. A family that bought a home for $200K in 1995 and sells for $600K in 2026 has a nominal gain of $400K — but a real gain of roughly $240K after CPI adjustment. The inflation component was never wealth; taxing it is taxing a measurement error.

Implementation is straightforward: brokerages already track purchase dates and cost basis; the BLS publishes monthly CPI. The calculation is a lookup table multiplication that any brokerage system can automate. For assets acquired by gift or deemed realization at death, the basis date resets to the transfer date.

### Three Structural Rules

**1. Death is a realization event.**
All unrealized gains are taxed on the decedent's final return using the lifetime capital gains table. The remaining 0% bracket shields gains first; amounts above are taxed at progressive rates. Heirs receive a clean basis at the date-of-death value. This follows the Canadian model and eliminates stepped-up basis entirely.

**Example (typical estate):** $300K in unrealized gains (after CPI adjustment), unused $2M allowance → **$0 tax**. Heir inherits at current market value with a clean basis.

**Example (large estate):** $80M in unrealized gains (after CPI adjustment), allowance fully used → approximately $29.6M in tax at the 37% rate. Under current law with estate planning, this estate likely pays $5-15M. Under current law without planning, approximately $34.8M. This framework collects more than practice, slightly less than theory — but with no escape routes.

**2. Gifts are realization events.**
The donor pays capital gains tax at the time of transfer, using their own lifetime counter. This neutralizes GRATs, dynasty trusts, and every other technique that relies on transferring appreciation without triggering tax. The recipient receives a clean basis at the gift-date value.

**3. Borrowing against appreciated assets is a realization event.**
If a loan is secured by appreciated assets and the loan exceeds the remaining lifetime 0% bracket, the excess triggers taxable gain. Basis steps up by the taxed amount to prevent double taxation on eventual sale. This closes buy-borrow-die: you can still borrow, but you cannot live tax-free on appreciation indefinitely.

**What is not affected:** Ordinary business loans, mortgages for purchase, and borrowing for reinvestment or expansion. The rule targets personal-consumption borrowing against appreciated collateral, using lender-reported loan purpose and existing enforcement doctrines.

### Payment Flexibility for Illiquid Assets

For all three realization events (death, gift, borrowing), a universal lien at market-rate interest is available for illiquid assets — farms, closely-held businesses, real estate. Heirs or donors can defer payment over 15 years without forced liquidation.

The lien rate is the market rate. This is not a subsidy. A business that cannot service market-rate cost of capital has a problem predating this framework. Every LBO and PE deal finances at market rates. GRATs work precisely because they arbitrage the artificial Section 7520 rate against actual returns. This framework replaces artificial government rates with real ones.

### The Lifetime Counter

The lifetime counter is the core tracking mechanism. It is:

- **Per individual.** Each person has their own counter from birth (or from enactment, for existing taxpayers — only post-enactment gains count).
- **Cumulative.** Every realized capital gain (sale, deemed realization at death/gift/borrowing) adds to the counter.
- **Irreversible.** Capital losses offset gains in the year incurred (and carry forward per current rules) but do not reduce the lifetime counter. The counter only goes up.
- **Inflation-adjusted.** Gains entering the counter are real gains after CPI basis adjustment.
- **Survives marriage and divorce.** The counter belongs to the individual. Marriage doubles the bracket thresholds for joint filing; divorce returns each spouse to their individual counter. No pooling, no splitting, no planning incentive. (See FAQ for details.)

### System Configuration Summary

The entire framework is defined by three global configuration inputs:

| Input | Source | Changeability |
|---|---|---|
| Income tax bracket table | Legislative | Rates and thresholds adjustable; structure fixed |
| Lifetime capital gains bracket table | Legislative | Rates and thresholds adjustable; structure fixed |
| Consumer Price Index (CPI) | Bureau of Labor Statistics | Published monthly; not a policy variable |

Compare this to the current system's 25+ independent parameters — each a knob that lobbyists can turn, each creating edge cases requiring IRS guidance, and each interacting with others in ways that are difficult to model or predict.

---

## What the Framework Makes Possible

Because the lifetime gains system is universal, progressive, and closes all deferral escape routes, an extraordinary amount of existing tax infrastructure becomes redundant. The framework doesn't just reform capital gains — it renders entire categories of tax law unnecessary.

### Three Shadow Tax Codes Eliminated

| Tax | Current Revenue | Why It's Now Redundant |
|---|---|---|
| Estate Tax | ~$20-25B/yr | A Potemkin tax: theoretically 40%, actually ~10% on large estates after planning. Its existence justifies stepped-up basis, which costs $75-100B/yr. The lifetime gains framework with deemed realization at death collects multiples more — with no avoidance path. (See "The Insight" below for the full argument.) |
| Alternative Minimum Tax (AMT) | ~$5-7B/yr | A parallel tax system created in 1969 to catch 155 wealthy non-payers. It now affects millions of upper-middle-class households while the truly wealthy route around it. Progressive lifetime rates with no exclusions make AMT's purpose obsolete. |
| Net Investment Income Tax (NIIT) | ~$25-33B/yr | A 3.8% surtax bolted onto capital gains to fund Medicare — a patch on a patch. The framework's broader base and higher top-end rates generate far more revenue for general funds, which is where Medicare funding actually comes from. (See FAQ.) |

### Ten Shadow Exclusions and Preferences Eliminated

| Provision | Why It's Now Redundant |
|---|---|
| QSBS (Section 1202) | Replaced by the universal 0% bracket. All founders benefit, not just those who meet arbitrary entity and industry tests. |
| Primary Residence Exclusion (Section 121) | Redundant. The $2M/$4M 0% bracket covers typical home-sale gains without privileging housing over other savings. |
| Like-Kind Exchanges (Section 1031) | Indefinite deferral vehicle. All gains flow through the lifetime counter; no asset class gets special treatment. |
| Opportunity Zone Deferrals (Section 1400Z-2) | Deferral + basis step-up mechanism. Both features are irrelevant under this framework. |
| Section 1256 Contracts (60/40 Rule) | Holding period is irrelevant under a lifetime cumulative system. No reason for a special derivatives rate. |
| Collectibles Rate (28%) | No principled basis for a separate asset-class rate. Everything flows through the same lifetime counter. |
| Installment Sale Deferral (Section 453) | Creates multi-decade deferral that contradicts the framework's realization principles. |
| QSBS Rollover (Section 1045) | Another deferral mechanism. Redundant when the 0% bracket already protects early-stage gains. |
| Section 1244 (Small Business Stock Loss) | Ordinary-loss treatment for small business stock losses becomes unnecessary as the systems converge. |
| GRATs, Dynasty Trusts, Valuation Discounts | Structurally eliminated. These tools exploit indefinite deferral, stepped-up basis, and high estate exemptions — all of which no longer exist. |

### Carried Interest: Rendered Moot

Not banned — rendered moot. A fund manager with $50M+ in lifetime gains pays 37%, the same as if it were wages. Rate convergence eliminates the preference at scale without requiring the IRS to draw lines between "real" capital gains and labor income dressed up as capital gains. Below the 0% bracket, emerging fund managers are actually better off than under current law. No new rules needed.

---

## The Insight

Professor Ray Madoff's *The Second Estate* (2025) identifies the foundational design flaw that makes this simplification possible: the estate tax functions as political cover. Its existence justifies excluding inheritances from income tax, while its hollowed-out structure — GRATs, dynasty trusts, valuation discounts, stepped-up basis — ensures the wealthy pay neither. The estate tax theoretically collects 40% but actually collects closer to 10% on large estates. It has become a Potemkin tax: visible enough to deflect criticism, porous enough to be irrelevant.

But the estate tax is only the most visible example. The entire capital gains landscape is a series of narrow fixes layered on top of each other — AMT to catch what income tax missed, NIIT to catch what AMT missed, QSBS to incentivize what the rates discouraged, Section 121 to protect what QSBS didn't cover. Each provision has a constituency and a rationale. Collectively they produce a system with **25+ independent configuration parameters** that interact in ways no single person fully understands — including the people who wrote them.

The lifetime gains framework resolves this by eliminating the structural conditions that made every one of these provisions necessary. When gains are tracked cumulatively, taxed progressively, and realized at death, gift, and borrowing — the rationale for parallel tax codes, narrow exclusions, and estate planning loopholes simply disappears.

---

## The Political Landscape

### Why This Gets a Meeting

The three-tax repeal is the framework's key political asset:

- **Estate tax repeal** has been the GOP donor class's top priority for 30 years. This delivers it.
- **AMT repeal** appeals to suburban swing voters who have been caught in its creep for decades.
- **NIIT repeal** lets Republicans claim they repealed a piece of the Affordable Care Act.

No other progressive capital gains proposal can get a meeting with every Republican on the Senate Finance Committee. This one can — because it gives them three wins they've wanted for a generation, in exchange for a system that actually collects more revenue with no escape routes.

### The Opposition Map

**More pushback from the right.** Five constituencies:

1. **Investment class ($10M+ in gains):** Loudest and most funded. Effective rate jumps from ~23.8% to 30-37%. But the 0% bracket and three-tax repeal provide cover.
2. **Estate planning industry:** Existential threat to a $5B+ industry. GRATs, dynasty trusts, and valuation discount work disappear. This constituency will fight hard but has limited public sympathy.
3. **Real estate industry:** 1031 elimination. The most organized lobby; killed reform in 2017 and 2021. The 0% bracket softens the blow for smaller investors; the large commercial operators are the real opposition.
4. **Anti-tax ideologues:** This is a net tax increase regardless of simplification framing. Some will oppose on principle.
5. **Farm lobby:** Neutralized by the 0% bracket ($4M for a couple covers most farm-sale gains) plus the 15-year lien for illiquid assets. But they will find edge cases and organize around them.

**The left is mostly on board.** This framework addresses billionaire effective rates, stepped-up basis, estate tax holes, and carried interest. Warren/Sanders would prefer a wealth tax and higher rates, but would likely take this deal. The residual objection — 37% isn't enough — is philosophical, not a dealbreaker. (See FAQ: "Why not higher rates?")

### The Wealth Tax Comparison

This framework collects more than a wealth tax with fewer constitutional risks, lower administrative costs, and proven international precedent:

- **No annual valuation nightmare.** Gains are taxed at realization events with transaction prices, not annual appraisals of illiquid assets.
- **No constitutional question.** Deemed realization at death is low risk post-*Moore v. United States*; a wealth tax faces serious Article I challenges.
- **No European failure mode.** France, Sweden, Austria, and others repealed their wealth taxes after capital flight exceeded collections. Realization-based taxation has a proven track record (Canada, Australia, UK).
- **Larger effective base.** By expanding realization events to include death, gifts, and borrowing, the base captures wealth accumulation that a rate-based-only approach never reaches.

### Debates This Framework Renders Moot

| Perennial Debate | How the Framework Resolves It |
|---|---|
| Billionaire tax / unrealized gains | Expanded realization events (death, gift, borrowing), not annual mark-to-market |
| Rate wars (15% vs. 60%) | Base broadening matters more than rates; 37% with no escape > 60% with loopholes |
| Stepped-up basis | No estate tax = no "double taxation" argument = no justification for step-up |
| Inflation indexing | Built in. CPI-adjusted basis is automatic for all assets. |
| Carried interest | Rate convergence makes it irrelevant at scale; no definitional boundary needed |
| Wealth tax | Same outcome, constitutionally sound, proven internationally |
| SALT (partially) | $2M/$4M 0% bracket provides significant new benefit that partially offsets SALT pain for wealth-builders in high-tax states |

---

## Frequently Asked Questions

### FAQ Quick Links

**Framework Design**
- [Q1: Why abolish the estate tax?](#q1-why-abolish-the-estate-tax-instead-of-fixing-it)
- [Q2: Dynasty wealth](#q2-what-about-dynasty-wealth-wont-large-fortunes-persist-forever)
- [Q3: Why not higher rates?](#q3-why-not-higher-rates-why-not-50-or-60-above-25m)
- [Q4: Why not tax gains as ordinary income?](#q4-why-not-just-tax-capital-gains-as-ordinary-income-from-dollar-one)
- [Q5: Inflation indexing complexity](#q5-what-about-inflation-indexing--isnt-that-complex)

**Specific Situations**
- [Q6: Marriage and divorce](#q6-what-happens-to-marriage-and-divorce)
- [Q7: Primary residence](#q7-doesnt-eliminating-the-primary-residence-exclusion-hurt-homeowners)
- [Q8: Entrepreneurs and innovators](#q8-will-this-punish-entrepreneurs-and-innovators)
- [Q9: Expatriation and capital flight](#q9-what-about-expatriation-and-capital-flight)
- [Q10: Medicare funding without NIIT](#q10-how-is-medicare-funded-without-the-niit)
- [Q11: Trusts](#q11-what-about-trusts)
- [Q12: Remaining avoidance vectors](#q12-what-are-the-remaining-avoidance-vectors)

**Scope**
- [Q13: Income tax brackets](#q13-what-about-income-tax-brackets)
- [Q14: Child tax credit](#q14-what-about-the-child-tax-credit)
- [Q15: Retirement accounts](#q15-what-about-retirement-accounts)
- [Q16: Charitable giving](#q16-what-about-charitable-giving)

---

### On the Framework Design

#### Q1: Why abolish the estate tax instead of fixing it?

This is the core insight from Madoff's *The Second Estate*: the estate tax's existence justifies excluding inheritances from income tax, while its hollowed-out structure ensures the wealthy pay neither.

The numbers tell the story. The estate tax theoretically imposes a 40% rate but actually collects ~$20-25B/year — a fraction of what it should. Well-advised estates use GRATs, dynasty trusts, valuation discounts, and charitable vehicles to reduce effective rates to 10-15% or less. The Walton family famously transferred billions using a GRAT that generated $1.54 in gift tax.

This framework replaces the estate tax with deemed realization at death — a mechanism with no avoidance path. A $100M estate with $80M in unrealized gains pays approximately $29.6M under this framework. Under current law with competent planning, the same estate pays $5-15M. The framework collects 2-6x more from the estates that matter most.

Yes, a small number of families who were honestly paying the full estate tax without avoidance will pay slightly less. That is the explicit trade: a tax that theoretically collects 40% but actually collects 10% is replaced by a tax that reliably collects 37% with no escape. The government collects more in aggregate.

#### Q2: What about dynasty wealth? Won't large fortunes persist forever?

This is a legitimate concern and the framework is honest about it. If a family has $500M in basis (all gains taxed at the prior generation's death), the principal itself is not taxed again until new gains arise. In theory, a dynasty could persist on the stock of existing wealth.

In practice, three forces erode dynastic fortunes under this framework:

1. **Realization at every generation.** New appreciation is taxed at up to 37% at each death, gift, or borrowing event. A $500M fortune that grows to $900M over 25 years loses ~$148M to capital gains tax at the next generational transfer.

2. **Multi-child dilution.** Ultra-high-net-worth families average 2-3 children. $500M split three ways is $167M each. Three generations out, even with growth, each heir holds ~$60M — still wealthy, but not "owning democracy" wealthy.

3. **Inflation erosion on basis.** At 2.5% annual inflation, $500M in real purchasing power becomes ~$310M over 20 years if the assets merely keep pace with inflation.

The combined effect: realization-at-death + progressive rates + dilution + inflation does substantial erosion work without a separate tax on the stock of wealth.

The framework acknowledges that taxing the *stock* of existing wealth (as opposed to the *flow* of new gains) is a legitimate policy question — but entangling it with capital gains reform has historically killed both. This proposal addresses capital gains comprehensively and leaves the stock-of-wealth question as a separable debate.

#### Q3: Why not higher rates? Why not 50% or 60% above $25M?

The framework's power is that capital gains converge with ordinary income at 37%. That is a clean, defensible principle: no one pays more on investment income than on wages.

Adding a super-bracket breaks convergence, creates a new incentive for avoidance, and gives opponents a number to attack. Japan's 55% combined rate shows declining collections and capital emigration.

More importantly: the 0% bracket is what makes this politically viable. A super-bracket is what kills it. The deal is "simpler AND fairer." Adding a punitive top rate makes it look like the real goal was redistribution dressed up as simplification — which is exactly what opponents will claim.

The honest answer for progressives: if the base-broadened system with deemed realization collects less than projected, the rate table is the obvious adjustment lever. But start with convergence at 37% and measure actual collections before concluding the rates are wrong. Zidar et al. (Princeton) find the revenue-maximizing capital gains rate under base-broadening is 40-47% — well above 37%. There is headroom if needed, but leading with a moderate rate that matches the ordinary income ceiling is the strongest opening position.

#### Q4: Why not just tax capital gains as ordinary income from dollar one?

Six reasons this fails:

1. **Bunching.** A founder who builds for 10 years and sells in one year would face the top marginal rate on a decade of work. Lifetime accounting solves this; annual ordinary income treatment doesn't.
2. **Inflation.** Without basis indexing, taxing nominal gains at ordinary rates taxes purchasing power erosion at up to 37%. The 0% bracket absorbs most inflation effects, but eliminating it removes that cushion.
3. **Capital formation has genuine social value** that diminishes as wealth accumulates — the declining marginal social value of capital justifies lower rates at the bottom and convergence at the top, not flat equalization.
4. **Lock-in.** At 37% from dollar one, the incentive to never sell becomes overwhelming, reducing market liquidity and capital reallocation.
5. **International precedent.** Every country that tried full equalization retreated. It is not a stable equilibrium.
6. **Political viability.** Full equalization gets zero votes in the current Congress. The 0% bracket is the coalition-builder.

#### Q5: What about inflation indexing — isn't that complex?

No. This is a 1986 objection, not a 2026 objection. The IRS already indexes brackets, standard deductions, and dozens of thresholds annually using CPI. Brokerages already track cost basis with purchase dates. The calculation is: `adjusted_basis = original_basis × (CPI_sale / CPI_purchase)`. Any brokerage API can compute this in milliseconds.

Inflation indexing under this framework is actually progressive in effect. It matters most near the 0% bracket boundary: a family with $2.8M in nominal lifetime gains might have only $1.9M in real gains and stay entirely in the 0% bracket. For someone with $50M in gains, CPI adjustment might knock it to $42M — still deep in the 37% bracket.

Taxing inflation isn't taxing wealth — it's taxing a measurement error. The framework corrects for it automatically.

### On Specific Situations

#### Q6: What happens to marriage and divorce?

The lifetime counter is per individual, always. Marriage and divorce do not change your personal counter.

**Marriage:** Filing jointly doubles the bracket thresholds ($2M becomes $4M, etc.). Each spouse's pre-marriage counter carries forward unchanged. Gains realized during marriage are allocated to the individual whose assets generated them.

**Divorce:** Each spouse retains their individual lifetime counter. No splitting, no pooling, no reallocation. The bracket thresholds return to single-filer levels.

**Why this design?** It eliminates "capital gains divorce planning" entirely. There is no advantage to timing a divorce around asset sales, and no complexity in unwinding a shared counter. The counter belongs to the person, not the marriage.

**Spousal transfer exception:** Transfers between spouses (during marriage) are not realization events. This preserves current law's treatment and avoids taxing routine household financial management.

#### Q7: Doesn't eliminating the primary residence exclusion hurt homeowners?

No. The $2M/$4M 0% bracket covers typical home-sale gains and treats housing the same as every other form of long-term saving.

**Example:** Buy at $250K in 2000, sell at $700K in 2026. Nominal gain: $450K. After CPI adjustment (roughly 1.8x over 26 years): adjusted basis ~$450K, real gain ~$250K. **$0 tax**, with $1.75M of lifetime allowance remaining.

The current Section 121 exclusion ($250K/$500K) requires ownership and use tests, creates tax-driven housing decisions, and privileges homeownership over all other forms of saving. A universal lifetime allowance is simpler and neutral across asset types.

#### Q8: Will this punish entrepreneurs and innovators?

No. The 0% bracket is the innovation incentive. A founder who builds a company over 8 years and exits for $3M (with $2.8M in gains) pays **$0** in capital gains tax — better than current law unless they qualified for QSBS, which most founders don't.

The framework replaces QSBS's narrow, entity-specific test with a universal benefit. Every founder gets the same treatment regardless of whether they incorporated as a C-corp, LLC, or S-corp, and regardless of industry. This is both simpler and more equitable.

For large exits: a founder with a $50M exit is in the 30% bracket on gains above $10M. This is higher than current law's 23.8% — but the founder also had $2M at 0%, which current law doesn't offer. The effective rate on the full $50M is approximately 22%, comparable to current law but without the QSBS lottery or the need for expensive legal structuring.

#### Q9: What about expatriation and capital flight?

Renouncing citizenship triggers the same rule as death: deemed realization of all gains, with the lifetime allowance and progressive rates. Payment flexibility for illiquid assets.

Enforcement uses existing FATCA/FBAR reporting, beneficial ownership rules, and bank reporting on large transfers. Departure bonds and treaty information-sharing can be required for high-net-worth departures.

The fiscal risk is limited. A few thousand people renounce annually; a minority are tax-motivated. Even with some evasion, the leakage is small relative to the revenue recovered from closing domestic loopholes. International precedent (Canada, Australia) shows that realization-at-death systems do not trigger meaningful capital flight.

#### Q10: How is Medicare funded without the NIIT?

The NIIT generates ~$30-40B/year from a 3.8% surtax on net investment income. But Medicare is already primarily funded from general revenue — Parts B and D draw ~75% from general funds, and Medicaid is 100% general revenue. The NIIT's "earmarking" for the Hospital Insurance Trust Fund is largely an accounting convention, not a lockbox.

This framework eliminates a $30-40B surtax levied against a narrow, avoidable base and replaces it with a system that raises $180-285B from a broad, unavoidable base — all flowing to general revenue, which is where Medicare funding actually comes from. The net effect is substantially more federal revenue available for Medicare, not less.

The attack ad writes itself: *"They repealed the Medicare tax!"* The rebuttal: we repealed a $30-40B surtax and replaced it with a system that raises 5-8x more total revenue. Medicare's actual funding increases. The existing income-based Medicare taxes (the 0.9% Additional Medicare Tax on high earners) are unchanged.

A companion proposal on payroll tax reform will address the broader question of whether Medicare and Medicaid funding should be formally consolidated into general revenue rather than maintained as separate accounting buckets.

#### Q11: What about trusts?

Trusts remain useful for governance, creditor protection, and controlled distributions. They cannot be used for permanent tax deferral.

- **Trust-held gains:** Taxed to the trust at the top rate (37%) in the year realized.
- **Distributions to beneficiaries:** Taxed using the beneficiary's lifetime counter.
- **No allowance stacking:** Trusts do not receive their own 0% bracket and cannot multiply the allowance across generations.
- **Gift of assets to a trust:** A realization event for the grantor (gifts are realization events under this framework).

This eliminates dynasty trusts as a tax avoidance vehicle while preserving their legitimate non-tax functions.

#### Q12: What are the remaining avoidance vectors?

Honest answer: the attack surface is dramatically smaller, but not zero. Remaining vectors include:

1. **Valuation gaming on illiquid assets.** Private businesses, art, and real estate require appraisal at death/gift. This is the #1 remaining attack surface. It exists today under the estate tax and doesn't go away.
2. **Jurisdiction arbitrage.** Renouncing citizenship before realization events. Addressed by the exit tax, but enforcement depends on international cooperation.
3. **Entity layering.** Complex partnership structures that obscure ownership and basis tracking. The lifetime counter needs to be robust against this.
4. **Charitable vehicle manipulation.** Charitable transfers are treated as realization events under this framework (donor pays gains tax, retains eligibility for charitable credit under separate reform). This closes the biggest escape route but the details of charitable reform are addressed in a companion proposal.

The critical difference: current avoidance is *structural* — it exploits gaps between parallel tax systems. Remaining avoidance under this framework is *administrative* — it exploits measurement difficulty. That is a much easier problem. The IRS can improve appraisal enforcement and entity reporting; it cannot fix the fundamental architecture of having two tax systems that don't talk to each other.

### On Scope

#### Q13: What about income tax brackets?

Income tax bracket reform (including the possibility of adding a top bracket above 37%) is addressed in a companion proposal. This document focuses exclusively on capital gains.

The one structural dependency: the top capital gains rate (37%) converges with the top ordinary income rate (37%). If income tax reform changes the top rate, the capital gains ceiling should move with it to maintain convergence.

#### Q14: What about the child tax credit?

A unified child benefit ($4,000/child, fully refundable, consolidating CTC/EITC/CDCC) is addressed in a companion proposal. It is scoped out of this document to keep the capital gains framework laser-focused.

#### Q15: What about retirement accounts?

Retirement accounts (401k, IRA, Roth, 529) are explicitly excluded from the lifetime counter. Gains within these accounts do not consume the 0% bracket.

A separate companion proposal addresses retirement account consolidation and simplification. For purposes of this framework, the current retirement account structure is unchanged.

#### Q16: What about charitable giving?

Charitable giving reform (including a proposed universal credit) is addressed in a companion proposal. Within this framework, charitable transfers of appreciated assets are treated as realization events: the donor pays capital gains tax on the appreciation and retains eligibility for the charitable deduction/credit. This prevents the largest remaining escape route — donating appreciated stock to avoid gains tax entirely — while preserving the incentive for charitable giving.

---

## Revenue Assessment

### What We Lose

| Repeal | Annual Revenue Lost | Notes |
|---|---|---|
| Estate Tax | ~$20-25B | Replaced by deemed realization at death (collects multiples more) |
| AMT | ~$5-7B | Complexity savings offset some revenue loss |
| NIIT | ~$25-33B | Replaced by broader capital gains base flowing to general revenue |
| **Total** | **~$50-65B** | |

### What We Gain

| Change | Annual Revenue Gained | Notes |
|---|---|---|
| Deemed realization at death (stepped-up basis eliminated) | +$75-100B | Every estate realizes; no basis step-up; allowance protects ordinary families |
| Progressive lifetime capital gains rates above $2M/$4M | +$50-80B | 5-tier lifetime system; protects small gains, taxes large accumulations |
| Buy-borrow-die closure (borrowing as realization) | +$25-50B | Deemed sale when appreciated assets secure loans for consumption |
| QSBS elimination (replaced by universal 0% bracket) | +$10-20B | All founders/investors get same allowance; no more $10M+ exclusions |
| 1031 exchange elimination | +$10-15B | Real estate gains flow through same lifetime counter as all other assets |
| Other preference elimination (OZ, 1256, collectibles, 453, 1045) | +$10-20B | Collectively meaningful; individually small |
| **Total** | **+$180-285B** | Interaction-adjusted (overlapping provisions netted) |

### Net Position

| Scenario | Annual Cost | Annual Gain | Net Revenue |
|---|---|---|---|
| Conservative | -$65B | +$180B | **+$115B** |
| Mid | -$57B | +$230B | **+$173B** |
| Optimistic | -$50B | +$285B | **+$235B** |

*Note: These estimates are directional. Line items overlap (e.g., death as realization and progressive rates interact). Totals are interaction-adjusted ranges that include conservative offsets for behavioral response. Formal scoring by JCT/CBO would be needed for legislative purposes.*

**Key behavioral assumption:** Traditional capital gains elasticity estimates (-0.7) assume permanent deferral escape. This framework removes that escape. Under base-broadening, Zidar et al. (Princeton) find revenue-maximizing rates of 40-47%, well above our 37% top rate, implying our revenue estimates are conservative.

---

## Case Studies

These case studies show simplified before/after calculations for representative taxpayers. All gains are shown after CPI basis adjustment.

### Summary

| Case Study | Income/Gain | Current Law | This Framework | Change |
|---|---|---|---|---|
| Homeowner — sells primary residence, $300K real gain | $300K gain | $0 (Section 121) | $0 (0% bracket) | **No change** |
| Small Founder — $3M exit after 8 years | $2.8M gain | $555K (no QSBS) | $120K | **-$435K** |
| Successful Founder — $20M exit | $19M gain | $4.52M | $4.15M | **-$370K** |
| Mega Founder — $100M exit | $95M gain | $22.6M | $31.85M | **+$9.25M** |
| Inherited Estate — $20M, $15M unrealized gain | $15M gain | ~$0 (step-up + planning) | $3.1M | **+$3.1M** |
| Billionaire Borrower — $100M stock, $5M/yr loan | $5M/yr deemed | $0 | $1.85M/yr | **+$1.85M/yr** |
| Dynasty Estate — $500M, $400M unrealized | $400M gain | ~$30-50M (with planning) | $145M | **+$95-115M** |

**Pattern:** The bottom 99%+ of households pay the same or less. Small founders and homeowners benefit from the universal 0% bracket. The increases are concentrated on very large accumulations, inherited estates that currently exploit stepped-up basis, and asset-backed borrowing strategies.

---

### 1. Homeowner — Linda, Sells Primary Residence

Bought in 2000 for $250K. Sells in 2026 for $700K. CPI-adjusted basis: ~$450K. Real gain: ~$250K.

| | Current Law | This Framework |
|---|---|---|
| Real Gain | $250K | $250K |
| Exclusion/Allowance | $250K (Section 121) | $250K (0% bracket) |
| Tax | **$0** | **$0** |

Remaining lifetime allowance: $1.75M. No change for the typical homeowner, but the allowance covers all asset types — not just housing.

---

### 2. Small Founder — Priya, $3M Exit After 8 Years

Does not qualify for QSBS (common — most founders don't). CPI-adjusted gain: $2.8M.

| Bracket | Current Law (no QSBS) | This Framework |
|---|---|---|
| Real Gain | $2.8M | $2.8M |
| $0 – $2M at 0% | N/A | $0 |
| $2M – $2.8M at 15% | N/A | $120K |
| Current law (flat 19.8%) | $555K | N/A |
| **Total Tax** | **$555K** | **$120K** |
| **Effective Rate** | **19.8%** | **4.3%** |

---

### 3. Successful Founder — Marcus, $20M Exit

CPI-adjusted gain: $19M. First-time use of lifetime allowance.

| Bracket | Amount | Rate | Tax |
|---|---|---|---|
| $0 – $2M | $2M | 0% | $0 |
| $2M – $5M | $3M | 15% | $450K |
| $5M – $10M | $5M | 20% | $1M |
| $10M – $19M | $9M | 30% | $2.7M |
| **Total** | **$19M** | | **$4.15M (21.8%)** |

Current law: $19M × 23.8% (including NIIT) = $4.52M. **This framework saves $370K** and is simpler — no NIIT, no AMT check, no QSBS qualification attempt.

---

### 4. Mega Founder — Sarah, $100M Exit

CPI-adjusted gain: $95M. First-time use of lifetime allowance.

| Bracket | Amount | Rate | Tax |
|---|---|---|---|
| $0 – $2M | $2M | 0% | $0 |
| $2M – $5M | $3M | 15% | $450K |
| $5M – $10M | $5M | 20% | $1M |
| $10M – $25M | $15M | 30% | $4.5M |
| $25M+ | $70M | 37% | $25.9M |
| **Total** | **$95M** | | **$31.85M (33.5%)** |

Current law: $95M × 23.8% = $22.6M. **This framework collects $9.25M more.** The effective rate (33.5%) is higher but still below the top ordinary income rate — convergence holds.

---

### 5. Inherited Estate — $20M, $15M in Unrealized Gains

Decedent has used $500K of lifetime allowance previously. CPI-adjusted unrealized gains: $15M.

| | Current Law | This Framework |
|---|---|---|
| Stepped-up basis | Yes — $0 gains tax | No — gains taxed on final return |
| Estate tax (with planning) | Likely ~$0 (exemption + planning) | $0 (estate tax abolished) |
| Remaining allowance | N/A | $1.5M |
| Capital gains tax | $0 | See below |

| Bracket (Decedent's Cumulative Position) | Amount | Rate | Tax |
|---|---|---|---|
| $500K – $2M (remaining 0% bracket) | $1.5M | 0% | $0 |
| $2M – $5M | $3M | 15% | $450K |
| $5M – $10M | $5M | 20% | $1M |
| $10M – $15.5M | $5.5M | 30% | $1.65M |
| **Total Tax** | **$15M** | | **$3.1M** |

Under current law: **$0** (stepped-up basis eliminates gains; estate planning reduces or eliminates estate tax). This framework collects $3.1M that currently escapes entirely.

---

### 6. Billionaire Borrower — $100M Stock, $5M/Year Lifestyle Loan

Lifetime allowance fully used. Borrows $5M/year against appreciated stock for personal consumption.

| | Current Law | This Framework |
|---|---|---|
| Lifestyle Loan | $5M | $5M |
| Taxable Gain Triggered | $0 | $5M (deemed realization) |
| Tax | $0 | $1.85M (at 37%) |
| **Effective Rate on Consumption** | **0%** | **37%** |

Basis steps up by $5M to prevent double taxation on eventual sale.

---

### 7. Dynasty Estate — $500M, $400M in Unrealized Gains

Decedent's lifetime allowance fully used. CPI-adjusted unrealized gains: $400M.

| | Current Law (with planning) | This Framework |
|---|---|---|
| Stepped-up basis | Yes — $0 gains tax | No |
| Estate tax | ~$30-50M (after GRAT/trust planning) | $0 (abolished) |
| Capital gains tax | $0 | $400M at blended rates → ~$145M |
| **Total** | **~$30-50M** | **~$145M** |

The framework collects 3-5x what the current system actually collects on a $500M estate. This is where the revenue argument lives: the gap between what the estate tax theoretically collects and what it actually collects after planning.

---

## What This Document Is Not

This is not a bill. It is not a CBO score. It is a framework — a structural argument that the U.S. capital gains system can be made radically simpler, meaningfully more progressive, and fiscally durable by replacing dozens of overlapping provisions with a single lifetime system.

The specific rates and thresholds are placeholders. The structural principles are not:

1. One lifetime counter replaces all carve-outs.
2. Death, gifts, and borrowing are realization events.
3. Basis is inflation-adjusted.
4. Rates converge with ordinary income at the top.
5. The 0% bracket makes most Americans better off than current law.

If these five principles hold, the rest is calibration.

---

## Intellectual Lineage

This framework builds on work by:

- **Ray Madoff**, *The Second Estate* (2025) — the foundational insight that the estate tax is structural cover for non-taxation of wealth transfers
- **Edward Fox & Zachary Liscow** — borrowing-as-realization design and empirical data
- **Owen Zidar et al. (Princeton)** — revenue-maximizing rates under base-broadening
- **Yale Budget Lab** — scoring data for borrowing-as-realization
- **Saez & Zucman**, *The Triumph of Injustice* — effective tax rate data showing top-end regressivity
- **David Cay Johnston**, *Perfectly Legal* — political economy of avoidance
- **Colin Heath (NYU Law Review)** — constitutional analysis of deemed realization
- **The Canadian model** — deemed disposition at death as international precedent

---

*This document is part of the Fair and Simple Tax Project. Companion proposals address income tax bracket reform, child benefits, retirement account consolidation, and charitable giving reform. Each can be enacted independently; together they form a cohesive fiscal system.*

*Contact: Matt Sly — mattsly@gmail.com*
