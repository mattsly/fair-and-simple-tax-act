# The Lifetime Gains Framework

### A Proposal to Radically Simplify Capital Gains Taxation and Reduce Wealth Inequality in a Fiscally Durable Manner

I’m [Matt Sly](https://www.mattsly.com) - a software entrepreneur, not a policy professional. But the tax code is essentially an algorithm. And, as implemented, it is our country's most profound and expensive technical debt. My perspective is shaped by 20 years managing software products as well as a lifetime of paying taxes in many capacities: a student, a W2 employee, startup employee, founder and investor. 

I’m proposing a "major refactor" based on four design tenets. My solution is centered on the concept of a universal lifetime capital gains framework which renders entire categories of tax law redundant while addressing many of our most pressing social challenges including profound wealth inequality and a cascading federal deficit.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and clear tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

## Press Release

FOR IMMEDIATE RELEASE

**The Lifetime Equity Act Introduced to Refactor the U.S. Tax Code, Close $300B in Loopholes, and Restore Economic Mobility**

WASHINGTON, D.C. — Today, a birpartisan coalition introduced The Lifetime Equity Act (LEA), a structural modernization of the U.S. tax code designed to eliminate systemic complexity that has enabled unprecedented levels of wealth inequality. 

Over decades, the tax code, specifically as it pertains to capital and wealth, has accumulated layer upon layer of special rules, carve-outs, and parallel systems. While many of these provisions were created with good intentions, the result is a system that is difficult for taxpayers to understand, costly to comply with, and increasingly disconnected from its stated goals. Filing taxes has become unpredictable for ordinary households and arbitrage-driven for those with access to sophisticated planning.

Simultaneously, the federal deficit has become a primary national expense, with 2026 net interest outlays projected to exceed $1 trillion, or roughly 14% of the total federal budget.

The LEA introduces a single Lifetime Gains Framework, eliminates dozens of complex carve outs and loopholds, moves the country toward long-term budget sustainability by raising $200–310 billion annually, 

Importantly, the LEA is not a wealth tax. It accomplishes the same objective of reducing wealth inequality with a simpler solution. In addition, the LEA includes the elimination of many of complex (and now redundant) "shadow" components of the tax code, including NIIT, AMT and the Estate Tax. As such, it has achieved broad appeal to a bipartisan congressional coalition.

A primary goal of the LEA is to make the tax code legible, coherent, and enable more honest about tradeoffs. 

By simplifying the system and aligning incentives with productive economic activity, the proposal aims to create a tax code that better serves taxpayers, policymakers, and the long-term health of the country.

## The Design Tenets

Every design decision in this framework is evaluated against four tenets. When tenets conflict, the tensions are acknowledged explicitly rather than papered over.

**1. Radical Simplicity**
The tax code should be broadly understood and almost entirely automated. If a provision cannot be understood without specialists, it does not belong. Simplicity reduces compliance costs, economic deadweight loss, and evasion vectors. Simplicity also enables more meaningful public debate about national priorities.

**2. Fiscal Durability**
The reform must be revenue-positive and survive political cycles. Revenue estimates must account for behavioral responses.

**3. Fuel the Climb**
Americans who are seeking to climb the economic ladder should be unambiguously better off under this framework than under current law. The system should reward work, saving, and wealth-building. It should not create structural advantages that entrench dynastic wealth at the expense of economic ascendency.

**4. Reward Innovation**
Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively — particularly at the early stage where risk is highest and social returns are greatest.


> **How to Read the Numbers in This Proposal**
>
> This document proposes a structure. The brackets and thresholds shown are initial calibrations meant to prove the system works and to anchor fiscal targets. Reasonable people can disagree on exact numbers; any revisions must still meet the revenue and durability goals in Tenet 2. The intent is to make the levers transparent and modelable, so debate stays focused on outcomes rather than defending a system that cannot be clearly understood, modeled, or tuned.

---

## Solution Overview

The core idea is simple: replace the current patchwork of capital gains taxes, exemptions, and avoidance strategies with a single progressive tax based on **lifetime cumulative capital gains**. Every American gets a generous tax-free allowance, recognizing that as a society we want to encourage saving, investment and innovation, especially for those who are working to climb the economic ladder. We recognize that wealth begets wealth, and that investing when you are already rich deserves less preferential treatment than investing while you are climbing the socioeconomic ladder. As such, lifetime capital gains tax rates rise gradually and converge with ordinary income at the top lifetime accumulated bracket. 

Three expanded realization events — death, gifts, and borrowing — ensure gains cannot be deferred indefinitely. Basis is indexed to inflation so the system taxes real wealth, not measurement error.

Because the lifetime gains system is universal, progressive, and closes all deferral escape routes, an extraordinary amount of existing tax infrastructure becomes redundant. The framework doesn't just reform capital gains — it renders entire categories of tax law unnecessary. AMT, NIIT and the Estate Tax all become redundant and can be eliminated. And dozens of specialized and complicated capital gains carve outs are removed in favor of more flexible, durable and less gameable system of unverisal capital gains treatment.

TODO: - let's start the FAQs Here - Call the first section "Implementation Details" and have a FAQ with each of these components

### The Rate Table
*see note above - this rate table is a directional placeholders rather than final proposal*

| Cumulative Lifetime Capital Gains (Single) | Cumulative Lifetime Capital Gains (Joint) | Marginal Rate |
|---|---|---|
| $0 – $2M | $0 – $4M | **0%** |
| $2M – $5M | $4M – $10M | **15%** |
| $5M – $10M | $10M – $20M | **20%** |
| $10M – $25M | $20M – $50M | **30%** |
| $25M+ | $50M+ | **37%** |

**Core principle:** Capital gains rates converge with ordinary income rates at the top brackets. The top rate (37%) matches the top ordinary income rate. No taxpayer ever pays more on investment income than on wages.

**The 0% bracket.** A married couple can accumulate $4M in lifetime capital gains — across home sales, stock sales, business exits, and every other form of appreciation — and pay zero federal capital gains tax. This is more generous than current law for over 99% of American households. (See FAQ: "Why is the 0% bracket so important?")

### The Lifetime Counter

The lifetime counter is the core tracking mechanism. It is:

- **Per individual.** Each person has their own counter from birth (or from enactment, for existing taxpayers — only post-enactment gains count).
- **Cumulative.** Every realized capital gain (sale, deemed realization at death/gift/borrowing) adds to the counter.
- **Annual Netting.** Capital losses offset gains within each calendar year. The net result (gains minus losses) adjusts the counter once per year, on December 31st. Unused losses at year-end do not carry forward. The counter can move up or down year-to-year based on net realized results.
- **Inflation-adjusted.** Gains entering the counter are real gains after CPI basis adjustment.
- **Survives marriage and divorce.** The counter belongs to the individual. Marriage doubles the bracket thresholds for joint filing; divorce returns each spouse to their individual counter. No pooling, no splitting, no planning incentive. (See FAQ for details.)

### System Configuration Summary

The entire framework is defined by three global configuration inputs:

| Input | Source | Changeability |
|---|---|---|
| Income tax bracket table | Legislative | Rates and thresholds adjustable; structure fixed |
| Lifetime capital gains bracket table | Legislative | Rates and thresholds adjustable; structure fixed |
| Consumer Price Index (CPI) | Bureau of Labor Statistics | Published monthly; not a policy variable |

TODO - indicate how we will adjust the table based on inflation every year - it should be recursive and self healing


### Three Realization Events
TODO - let's move this down the FAQ section - it's a detailed How - we already mentioned the events in the Framework section, which we want to keep as tight as possible

**1. Death is a realization event.**
All unrealized gains are taxed on the decedent's final return using the lifetime capital gains table. The remaining 0% bracket shields gains first; amounts above are taxed at progressive rates. Heirs receive a clean basis at the date-of-death value. This follows the Canadian model and eliminates stepped-up basis entirely.

**Example (typical estate):** $300K in unrealized gains (after CPI adjustment), unused $2M allowance → **$0 tax**. Heir inherits at current market value with a clean basis.

**Example (large estate):** $80M in unrealized gains (after CPI adjustment), allowance fully used → approximately $29.6M in tax at the 37% rate. (See Case Studies for detailed comparisons to current law.)

TODO - refernce w/ a link how financing options work for illiquid assets, and link to the details on that

**2. Gifts are realization events.**
The donor pays capital gains tax at the time of transfer, using their own lifetime counter. This neutralizes GRATs, dynasty trusts, and every other technique that relies on transferring appreciation without triggering tax. The recipient receives a clean basis at the gift-date value.

TODO - an open question is whether we continue to allow for Gift Exemptions? I actually think we can completely get rid of them since we reset the basis of a gift?

**3. Borrowing against appreciated assets is a realization event.**
If a loan is secured by appreciated assets and the loan exceeds the remaining lifetime 0% bracket, the excess triggers taxable gain. Basis steps up by the taxed amount to prevent double taxation on eventual sale. This closes buy-borrow-die: you can still borrow, but you cannot live tax-free on appreciation indefinitely.

**What is not affected:** Ordinary business loans, mortgages for purchase, and borrowing for reinvestment or expansion. The rule targets personal-consumption borrowing against appreciated collateral. (See FAQ: "How does borrowing-as-realization work in practice?")

### Payment Flexibility for Illiquid Assets

For all three realization events (death, gift, borrowing), a universal lien at market-rate interest is available for illiquid assets — farms, closely-held businesses, real estate. Heirs or donors can defer payment over 15 years without forced liquidation. The lien rate is the prevailing market rate, not a subsidized government rate. (See FAQ: "Won't this force families to sell farms and businesses?")

### Inflation-Indexed Basis

All cost basis is adjusted for inflation using the Consumer Price Index. When an asset is sold, the basis is adjusted from the purchase date to the sale date: `adjusted_basis = original_basis × (CPI_sale / CPI_purchase)`.

This ensures the framework taxes real gains, not phantom gains from purchasing power erosion. A family that bought a home for $200K in 1995 and sells for $600K in 2026 has a nominal gain of $400K — but a real gain of roughly $240K after CPI adjustment. The inflation component was never wealth; taxing it is taxing a measurement error.

Implementation is straightforward: brokerages already track purchase dates and cost basis; the BLS publishes monthly CPI. The calculation is a lookup table multiplication that any brokerage system can automate. For assets acquired by gift or deemed realization at death, the basis date resets to the transfer date.


---

## What the Framework Makes Possible

TODO: let's move all of this into the FAQ for "What gets eliminated and what are the impacts?"

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

TODO - I think we can cut this section, and marge parts of it into the Estate Tax section - as is, it floats a little randomly

Professor Ray Madoff's *The Second Estate* (2025) identifies the foundational design flaw that makes this simplification possible: the estate tax functions as political cover. Its existence justifies excluding inheritances from income tax, while its hollowed-out structure — GRATs, dynasty trusts, valuation discounts, stepped-up basis — ensures the wealthy pay neither. The estate tax theoretically collects 40% but actually collects closer to 10% on large estates. It has become a Potemkin tax: visible enough to deflect criticism, porous enough to be irrelevant.

But the estate tax is only the most visible example. The entire capital gains landscape is a series of narrow fixes layered on top of each other — AMT to catch what income tax missed, NIIT to catch what AMT missed, QSBS to incentivize what the rates discouraged, Section 121 to protect what QSBS didn't cover. Each provision has a constituency and a rationale. Collectively they produce a system with **25+ independent configuration parameters** that interact in ways no single person fully understands — including the people who wrote them.

The lifetime gains framework resolves this by eliminating the structural conditions that made every one of these provisions necessary. When gains are tracked cumulatively, taxed progressively, and realized at death, gift, and borrowing — the rationale for parallel tax codes, narrow exclusions, and estate planning loopholes simply disappears.

---

## The Political Landscape

TODO - I think we can push this in to an FAQ - it's not a "what" but a "how do we get this passed" - I think a new FAQ section with "Handling Political Objections" (or something)

### Why This Gets a Meeting

The three-tax repeal is the framework's key political asset:

- **Estate tax repeal** has been the GOP donor class's top priority for 30 years. This delivers it.
- **AMT repeal** appeals to suburban swing voters who have been caught in its creep for decades.
- **NIIT repeal** lets Republicans claim they repealed a piece of the Affordable Care Act.

No other progressive capital gains proposal can get a meeting with every Republican on the Senate Finance Committee. This one can — because it gives them three wins they've wanted for a generation, in exchange for a system that actually collects more revenue with no escape routes.

### The Opposition Map

TODO - I think we can push this in to an FAQ - it's not a "what" but a "how"

**More pushback from the right.** Five constituencies:

1. **Investment class ($10M+ in gains):** Loudest and most funded. Effective rate jumps from ~23.8% to 30-37%. But the 0% bracket and three-tax repeal provide cover.
2. **Estate planning industry:** Existential threat to a $5B+ industry. GRATs, dynasty trusts, and valuation discount work disappear. This constituency will fight hard but has limited public sympathy.
3. **Real estate industry:** 1031 elimination. The most organized lobby; killed reform in 2017 and 2021. The 0% bracket softens the blow for smaller investors; the large commercial operators are the real opposition.
4. **Anti-tax ideologues:** This is a net tax increase regardless of simplification framing. Some will oppose on principle.
5. **Farm lobby:** Neutralized by the 0% bracket ($4M for a couple covers most farm-sale gains) plus the 15-year lien for illiquid assets. But they will find edge cases and organize around them.

**The left is mostly on board.** This framework addresses billionaire effective rates, stepped-up basis, estate tax holes, and carried interest. Warren/Sanders would prefer a wealth tax and higher rates, but would likely take this deal. The residual objection — 37% isn't enough — is philosophical, not a dealbreaker. (See FAQ: "Why not higher rates?")

### The Wealth Tax Comparison

TODO - I think we can push this in to an FAQ - it's not a "what" but a "why"

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

**On the Framework Design:** [Q1: Why not ordinary income from dollar one?](#q1) · [Q2: Why progressive lifetime taxation?](#q2) · [Q3: Why not higher rates?](#q3) · [Q4: Inflation indexing complexity?](#q4)

**On Eliminating Provisions:** [Q5: Why abolish the estate tax?](#q5) · [Q6: Dynasty fortunes without estate tax?](#q6) · [Q7: Homeowners hurt by losing Section 121?](#q7) · [Q8: QSBS elimination punishes entrepreneurs?](#q8)

**On Specific Situations:** [Q9: Marriage and divorce?](#q9) · [Q10: Expatriation and capital flight?](#q10) · [Q11: Medicare funding without NIIT?](#q11) · [Q12: Trusts?](#q12) · [Q13: Remaining avoidance vectors?](#q13)

**On Practical Concerns:** [Q14: Will 1031 elimination crash real estate?](#q14) · [Q15: Forced farm/business sales?](#q15) · [Q16: Is this a massive tax increase?](#q16) · [Q17: Radical simplicity with lifetime tracking?](#q17) · [Q18: How borrowing-as-realization works](#q18) · [Q19: Why the 0% bracket matters](#q19) · [Q20: Government as behavioral engineer?](#q20) · [Q21: Canada complexity creep?](#q21)

** Political Landscape**
(TODO - add these - objections from the right, objections from the left)

**On Scope:** [Q22: Income tax brackets?](#q22) · [Q23: Child tax credit?](#q23) · [Q24: Retirement accounts?](#q24) · [Q25: Charitable giving?](#q25)

---

### On the Framework Design

#### Q1: Why not just tax capital gains as ordinary income from dollar one?

Six reasons this fails:

1. **Bunching.** A founder who builds for 10 years and sells in one year would face the top marginal rate on a decade of work. Lifetime accounting solves this; annual ordinary income treatment doesn't.
2. **Inflation.** Without basis indexing, taxing nominal gains at ordinary rates taxes purchasing power erosion at up to 37%. The 0% bracket absorbs most inflation effects, but eliminating it removes that cushion.
3. **Capital formation has genuine social value** that diminishes as wealth accumulates — the declining marginal social value of capital justifies lower rates at the bottom and convergence at the top, not flat equalization.
   
TODO - investing also entails risk which employment income does not

4. **Lock-in.** At 37% from dollar one, the incentive to never sell becomes overwhelming, reducing market liquidity and capital reallocation.
5. **International precedent.** Every country that tried full equalization retreated. It is not a stable equilibrium.
6. **Political viability.** Full equalization gets zero votes in the current Congress. The 0% bracket is the coalition-builder.

#### Q2: Why progressive lifetime taxation? Isn’t a dollar a dollar?

The framework’s core tax base is cumulative lifetime gains, and the rate table is graduated. Some critics ask: "Why should somebody who has already realized tens of millions in gains face a higher rate on the next dollar than someone selling their first $100K?" The answer has both **fairness** and **economic** justifications:

- **Wealth begets wealth.** Once you’ve accumulated a large stock of capital, you can take risks that others cannot: you can finance long-shot ventures out of pocket, you can weather a string of losses, and you have access to cheaper credit. A middle‑class saver selling a small rental property is often taking substantial risk relative to their net worth. The wealthy are effectively getting a backed‑up insurance policy courtesy of their balance sheet; the tax system should reflect that asymmetry by requiring a higher risk/reward premium as lifetime gains grow.

- **Reduced marginal social value.** The first dollar of gain to someone with no savings is often spent or invested in ways that expand productive capacity. The millionth dollar for a billionaire is most likely reinvested in more wealth‑management and tax‑avoidance schemes. Progressive rates allocate the incidence of taxation toward gains with higher social opportunity cost and away from gains that are essential for upward mobility.

- **Consistency with income tax principles.** The ordinary income tax is progressive because a dollar means more to the poor than the rich, both in ability to pay and in marginal utility. Capital gains are not a separate "thing" – they are just another form of income. Tracking them cumulatively simply makes visible the total resources an individual has extracted from the economy over time. Once that total passes generous thresholds, it’s fair to start charging higher rates, just as you would on wages.

TODO - can we cite data that indicates that changes in capital gains rates doesn't impact rates of investment? (i.e. if I'm super rich, I'm not going to not start a company b/c of 20% vs 37% tax rate...?)

This logic also underpins the 0% bracket: giving everyone the same generous tax‑free allowance ensures the system is redistributive at the bottom while still allowing for progressivity at the top.


#### Q3: Why not higher rates? Why not 50% or 60% above $25M?

The framework's power is that capital gains converge with ordinary income at 37%. That is a clean, defensible principle: no one pays more on investment income than on wages.

Adding a super-bracket breaks convergence, creates a new incentive for avoidance, and gives opponents a number to attack. Japan's 55% combined rate shows declining collections and capital emigration.

More importantly: the 0% bracket is what makes this politically viable. A super-bracket is what kills it. The deal is "simpler AND fairer." Adding a punitive top rate makes it look like the real goal was redistribution dressed up as simplification — which is exactly what opponents will claim.

The honest answer for progressives: if the base-broadened system with deemed realization collects less than projected, the rate table is the obvious adjustment lever. But start with convergence at 37% and measure actual collections before concluding the rates are wrong. Zidar et al. (Princeton) find the revenue-maximizing capital gains rate under base-broadening is 40-47% — well above 37%. There is headroom if needed, but leading with a moderate rate that matches the ordinary income ceiling is the strongest opening position.

#### Q4: What about inflation indexing — isn't that complex?

No. This is a 1986 objection, not a 2026 objection. The IRS already indexes brackets, standard deductions, and dozens of thresholds annually using CPI. Brokerages already track cost basis with purchase dates. The calculation is: `adjusted_basis = original_basis × (CPI_sale / CPI_purchase)`. Any brokerage API can compute this in milliseconds.

Inflation indexing under this framework is actually progressive in effect. It matters most near the 0% bracket boundary: a family with $2.8M in nominal lifetime gains might have only $1.9M in real gains and stay entirely in the 0% bracket. For someone with $50M in gains, CPI adjustment might knock it to $42M — still deep in the 37% bracket.

Taxing inflation isn't taxing wealth — it's taxing a measurement error. The framework corrects for it automatically.

### The Impact of Eliminating Various Provisions and Carve Outs

#### Q5: Why abolish the estate tax instead of fixing it?

This is the core insight from Madoff's *The Second Estate*: the estate tax's existence justifies excluding inheritances from income tax, while its hollowed-out structure ensures the wealthy pay neither.

The numbers tell the story. The estate tax theoretically imposes a 40% rate but actually collects ~$20-25B/year — a fraction of what it should. Well-advised estates use GRATs, dynasty trusts, valuation discounts, and charitable vehicles to reduce effective rates to 10-15% or less. The Walton family famously transferred billions using a GRAT that generated $1.54 in gift tax.

This framework replaces the estate tax with deemed realization at death — a mechanism with no avoidance path. A $100M estate with $80M in unrealized gains pays approximately $29.6M under this framework. Under current law with competent planning, the same estate pays $5-15M. The framework collects 2-6x more from the estates that matter most.

Yes, a small number of families who were honestly paying the full estate tax without avoidance will pay slightly less. That is the explicit trade: a tax that theoretically collects 40% but actually collects 10% is replaced by a tax that reliably collects 37% with no escape. The government collects more in aggregate.

#### Q6: Without an estate tax, do we enable perpetual dynastic fortunes?

This is a legitimate concern and the framework is honest about it. If a family has $500M in basis (all gains taxed at the prior generation's death), the principal itself is not taxed again until new gains arise. In theory, a dynasty could persist on the stock of existing wealth.

In practice, three forces erode dynastic fortunes under this framework:

1. **Realization at every generation.** New appreciation is taxed at up to 37% at each death, gift, or borrowing event. A $500M fortune that grows to $900M over 25 years loses ~$148M to capital gains tax at the next generational transfer.

2. **Multi-child dilution.** Ultra-high-net-worth families average 2-3 children. $500M split three ways is $167M each. Three generations out, even with growth, each heir holds ~$60M — still wealthy, but not "owning democracy" wealthy.

3. **Inflation erosion on basis.** At 2.5% annual inflation, $500M in real purchasing power becomes ~$310M over 20 years if the assets merely keep pace with inflation.

The combined effect: realization-at-death + progressive rates + dilution + inflation does substantial erosion work without a separate tax on the stock of wealth.

The framework acknowledges that taxing the *stock* of existing wealth (as opposed to the *flow* of new gains) is a legitimate policy question — but entangling it with capital gains reform has historically killed both. This proposal addresses capital gains comprehensively and leaves the stock-of-wealth question as a separable debate.

#### Q7: Doesn't eliminating the primary residence exclusion hurt homeowners?

No. The $2M/$4M 0% bracket covers typical home-sale gains and treats housing the same as every other form of long-term saving.

**Example:** Buy at $250K in 2000, sell at $700K in 2026. Nominal gain: $450K. After CPI adjustment (roughly 1.8x over 26 years): adjusted basis ~$450K, real gain ~$250K. **$0 tax**, with $1.75M of lifetime allowance remaining.

The current Section 121 exclusion ($250K/$500K) requires ownership and use tests, creates tax-driven housing decisions, and privileges homeownership over all other forms of saving. Why does the tax code treat your house differently from your retirement account, your small business, or your stock portfolio? A universal lifetime allowance is simpler and neutral across asset types — the code stops telling you that owning a home is more virtuous than starting a business or investing in the stock market.

#### Q8: Will getting rid of QSBS punish entrepreneurs and innovators?

No. The 0% bracket is the innovation incentive. A founder who builds a company over 8 years and exits for $3M (with $2.8M in gains) pays **$0** in capital gains tax — better than current law unless they qualified for QSBS, which most founders don't.

**What QSBS actually does in practice:** It provides a tax windfall *after* a startup has already succeeded. By definition, you only claim QSBS when you sell stock at a large gain — meaning the company already worked. QSBS doesn't help you raise your seed round, make payroll, or reduce the risk of starting a company. It's a reward for having already won. No founder in the history of Silicon Valley said "I wasn't going to start this company, but then I heard about Section 1202."

TODO - I actually do think QSBS helps you raise money - because investors also take part and know that the upside is greater than it would be w/out it.

**Who QSBS actually serves:** QSBS requires you to form a C-corp (not an LLC or S-corp — the structures 95% of small businesses actually use), stay under $75M in assets, be in a qualifying industry, and hold for 5+ years. A Treasury analysis found that 70% of excluded QSBS dollars go to taxpayers with average income over $1 million making claims over $1 million. The landscaper who builds a $3M business and sells it gets nothing from QSBS. Under this framework, they get the same 0% bracket as the YC-backed founder.

**What this framework does instead:** It replaces QSBS's narrow, entity-specific test with a universal benefit. Every founder gets the same treatment regardless of whether they incorporated as a C-corp, LLC, or S-corp, and regardless of industry.

For large exits: a founder with a $50M exit is in the 30% bracket on gains above $10M. This is higher than current law's 23.8% — but the founder also had $2M at 0%, which current law doesn't offer. The effective rate on the full $50M is approximately 22%, comparable to current law but without the QSBS lottery or the need for expensive legal structuring.

### On Specific Situations

#### Q9: What happens to marriage and divorce?

The lifetime counter is per individual, always. Marriage and divorce do not change your personal counter.

**Marriage:** Filing jointly doubles the bracket thresholds ($2M becomes $4M, etc.). Each spouse's pre-marriage counter carries forward unchanged. Gains realized during marriage are allocated to the individual whose assets generated them.

TODO - I don't love this - it requires a new form of capital gains tracking as part of a joint return. We just split gains during marriage equally.

**Divorce:** Each spouse retains their individual lifetime counter. No splitting, no pooling, no reallocation. The bracket thresholds return to single-filer levels.

**Why this design?** It eliminates "capital gains divorce planning" entirely. There is no advantage to timing a divorce around asset sales, and no complexity in unwinding a shared counter. The counter belongs to the person, not the marriage.

**Spousal transfer exception:** Transfers between spouses (during marriage) are not realization events. This preserves current law's treatment and avoids taxing routine household financial management.

#### Q10: What about expatriation and capital flight?

Renouncing citizenship triggers the same rule as death: deemed realization of all gains, with the lifetime allowance and progressive rates. Payment flexibility for illiquid assets.

Enforcement uses existing FATCA/FBAR reporting, beneficial ownership rules, and bank reporting on large transfers. Departure bonds and treaty information-sharing can be required for high-net-worth departures.

The fiscal risk is limited. A few thousand people renounce annually; a minority are tax-motivated. Even with some evasion, the leakage is small relative to the revenue recovered from closing domestic loopholes. International precedent (Canada, Australia) shows that realization-at-death systems do not trigger meaningful capital flight.

#### Q11: How is Medicare funded without the NIIT?

The NIIT generates ~$30-40B/year from a 3.8% surtax on net investment income. But Medicare is already primarily funded from general revenue — Parts B and D draw ~75% from general funds, and Medicaid is 100% general revenue. The NIIT's "earmarking" for the Hospital Insurance Trust Fund is largely an accounting convention, not a lockbox.

This framework eliminates a $30-40B surtax levied against a narrow, avoidable base and replaces it with a system that raises $180-285B from a broad, unavoidable base — all flowing to general revenue, which is where Medicare funding actually comes from. The net effect is substantially more federal revenue available for Medicare, not less.

The attack ad writes itself: *"They repealed the Medicare tax!"* The rebuttal: we repealed a $30-40B surtax and replaced it with a system that raises 5-8x more total revenue. Medicare's actual funding increases. The existing income-based Medicare taxes (the 0.9% Additional Medicare Tax on high earners) are unchanged.

A companion proposal on payroll tax reform will address the broader question of whether Medicare and Medicaid funding should be formally consolidated into general revenue rather than maintained as separate accounting buckets.

#### Q12: What about trusts?

Trusts remain useful for governance, creditor protection, and controlled distributions. They cannot be used for permanent tax deferral.

- **Trust-held gains:** Taxed to the trust at the top rate (37%) in the year realized.
- **Distributions to beneficiaries:** Taxed using the beneficiary's lifetime counter.
- **No allowance stacking:** Trusts do not receive their own 0% bracket and cannot multiply the allowance across generations.
- **Gift of assets to a trust:** A realization event for the grantor (gifts are realization events under this framework).

This eliminates dynasty trusts as a tax avoidance vehicle while preserving their legitimate non-tax functions.

#### Q13: What are the remaining avoidance vectors?

Honest answer: the attack surface is dramatically smaller, but not zero. Remaining vectors include:

1. **Valuation gaming on illiquid assets.** Private businesses, art, and real estate require appraisal at death/gift. This is the #1 remaining attack surface. It exists today under the estate tax and doesn't go away.
2. **Jurisdiction arbitrage.** Renouncing citizenship before realization events. Addressed by the exit tax, but enforcement depends on international cooperation.
3. **Entity layering.** Complex partnership structures that obscure ownership and basis tracking. The lifetime counter needs to be robust against this.
4. **Charitable vehicle manipulation.** Charitable transfers are treated as realization events under this framework (donor pays gains tax, retains eligibility for charitable credit under separate reform). This closes the biggest escape route but the details of charitable reform are addressed in a companion proposal.

The critical difference: current avoidance is *structural* — it exploits gaps between parallel tax systems. Remaining avoidance under this framework is *administrative* — it exploits measurement difficulty. That is a much easier problem. The IRS can improve appraisal enforcement and entity reporting; it cannot fix the fundamental architecture of having two tax systems that don't talk to each other.

### On Practical Concerns

#### Q14: Won't eliminating 1031 exchanges crash the real estate market?

No. But the real estate lobby will tell you otherwise, so let's engage seriously.

**The lock-in argument:** Proponents say 1031s keep capital flowing by removing the "friction" of taxation on property sales. Without them, investors will hold properties longer, reducing transaction volume.

**The counter:** The lifetime counter with its generous 0% bracket addresses the legitimate concern behind 1031s for smaller investors. A couple selling a rental property with $800K in gains uses their lifetime allowance and pays nothing. For larger commercial operators, the gains flow through the progressive brackets like any other asset class.

**The dynastic wealth problem:** Combined with stepped-up basis, 1031 exchanges allow real estate portfolios to be passed down for generations with *zero* capital gains ever paid. The gain isn't deferred — it's eliminated. Deemed realization at death closes this loop permanently.

**The scale argument:** The JCT has estimated the tax expenditure for 1031 exchanges at roughly $4-10 billion per year. The real estate market in the United States involves trillions in annual transactions. The idea that a tax provision worth single-digit billions would "crash" a multi-trillion dollar market is not supported by evidence. The 1031 exchange industry — qualified intermediaries, specialist attorneys, dedicated software — exists solely because of this provision. That's not market liquidity. That's an artificial ecosystem created by a tax distortion.

#### Q15: Won't this force families to sell farms and businesses?

No. The payment flexibility lien exists specifically for this case. A family farm or closely-held business can defer tax payment over 15 years at market-rate interest without forced liquidation.

**Why market rate?** The lien rate is not a subsidy. A business that cannot service market-rate cost of capital has a problem predating this framework. Every LBO and PE deal finances at market rates. GRATs work precisely because they arbitrage the artificial Section 7520 rate against actual returns. This framework replaces artificial government rates with real ones.

Moreover, the $4M 0% bracket (for a couple) covers most family farm and small business exits entirely. A farm couple that sells for $3.5M in real gains after CPI adjustment pays **$0**. The 15-year lien is for the edge cases above that threshold — and even then, the annual payment at market rate is typically manageable for a going-concern business.

#### Q16: Isn't this a massive tax increase?

It depends on who you are.

**If you're a middle-class family** with one home sale and a retirement portfolio: You almost certainly pay *less* under this system. The 0% lifetime bracket covers the vast majority of your lifetime capital gains. You no longer need to worry about whether your home sale qualifies for Section 121, or whether you held long enough, or whether you used it as a primary residence for 2 of the last 5 years. You just sell your house.

**If you're a successful entrepreneur** with a $5M exit: You pay a moderate rate on gains above the 0% bracket. You might pay more than you would under current QSBS rules — but you also don't need to spend $20K on tax attorneys making sure your company qualifies. And if your company *didn't* qualify for QSBS (wrong structure, wrong industry, too much in assets), you pay dramatically less.

**If you're a serial real estate investor** rolling gains through 1031 exchanges indefinitely: Yes, you pay more. The code currently lets you defer — and ultimately eliminate — gains forever. That ends.

**If you're an ultra-high-net-worth individual** using buy-borrow-die to avoid ever realizing gains: Yes, you pay significantly more. That's the point.

The question isn't "does anyone pay more?" Of course some people do. The question is: **should the tax code be engineered to help specific groups avoid taxation based on which asset they hold, which structure they chose, or which advisor they hired?** We think the answer is no.

#### Q17: How is this "radical simplicity" if you're adding lifetime tracking?

Fair pushback. Let's do the complexity math.

**What we're eliminating:**

- Section 1202 (QSBS): 8 qualifying tests, multiple holding period rules, industry restrictions, asset thresholds, special basis calculations, 1045 rollover rules
- Section 1031: 45-day identification windows, 180-day completion deadlines, qualified intermediary requirements, boot calculations, related-party rules, Form 8824
- Section 121: Primary residence tests, 2-of-5-year rules, partial exclusion calculations, divorce provisions, military exceptions
- Opportunity Zones: Fund certification, 90% asset tests, substantial improvement tests, 10-year holding requirements, Form 8996
- Carried interest: Complex allocation rules distinguishing investment from service income
- Stepped-up basis: Valuation disputes, date-of-death appraisals, alternate valuation dates
- Estate tax: Entire parallel code — exemptions, portability elections, marital deductions, generation-skipping rules, Form 706
- AMT: Parallel rate structure, preference items, exemption phase-outs, Form 6251
- NIIT: Net investment income calculations, material participation tests, Form 8960

**What we're adding:**

- One lifetime running total, reported by brokerages (who already track cost basis) and maintained by the IRS

Modern brokerage platforms already track cost basis, acquisition dates, and cumulative gains. The infrastructure exists. What doesn't exist — and what we'd eliminate the need for — is the army of tax attorneys, qualified intermediaries, exchange accommodators, and OZ fund administrators whose entire business model depends on the current system's complexity.

The annual netting of gains against losses — which happens within each calendar year — uses infrastructure that already exists. Brokerages already report gains and losses on Form 1099-B. Taxpayers (or their preparers) already do this math on Form 8949/Schedule D. You're not asking the system to do something new; you're actually *removing* complexity by eliminating carryforwards that extend for decades and require perpetual reconciliation. One annual net result feeds the lifetime counter.

#### Q18: How does borrowing-as-realization work in practice?

The rule targets personal-consumption borrowing against appreciated collateral. If a taxpayer pledges appreciated assets as collateral and uses the loan proceeds for personal consumption (not reinvestment or business expansion), the excess over any remaining 0% bracket triggers a deemed realization.

**Enforcement:** Lender-reported loan purpose, existing IRS enforcement doctrines (economic substance, sham transaction), and bank reporting on large transfers. This is the same enforcement infrastructure used for existing margin lending rules, the wash sale rule, and anti-abuse doctrines.

**What is not affected:** Ordinary business loans, mortgages for purchase, borrowing for reinvestment or expansion, and margin loans used to buy additional securities. The rule specifically targets the buy-borrow-die strategy: using appreciated assets as collateral for personal lifestyle while deferring gains indefinitely.

**Basis step-up:** When borrowing triggers a deemed realization, the taxpayer's basis steps up by the taxed amount. This prevents double taxation on eventual sale. The mechanic is identical to what happens when you sell an asset: you pay tax on the gain, and your basis resets.

#### Q19: Why is the 0% bracket so important?

The 0% bracket is simultaneously the framework's policy anchor and its political anchor.

**Policy:** It ensures that over 99% of American households are unambiguously better off under this framework than under current law. A married couple can accumulate $4M in lifetime capital gains — more than most families will ever realize — before paying any federal capital gains tax. This is the most generous universal capital gains allowance ever proposed.

**Politics:** The 0% bracket is what makes the three-tax repeal politically viable. Abolishing the estate tax, AMT, and NIIT without a generous universal benefit would look like a giveaway to the wealthy. The 0% bracket makes it a deal: everyone gets a large tax-free allowance; above that, rates rise progressively. This is a trade every moderate Republican and every pragmatic Democrat can defend.

**The coalition math:** Estate tax repeal gets Republican votes. The 0% bracket protects Democrats' middle-class credibility. Progressive rates above $2M satisfy the fairness argument. All three pieces are load-bearing — remove any one and the coalition collapses.

#### Q20: Should the government use the tax code to encourage specific behaviors?

This is the philosophical heart of the debate.

The tax code's primary job is to **raise revenue fairly and efficiently** — not to be a shadow regulatory system that picks economic winners and losers. When Congress wants to encourage homeownership, clean energy, or small business formation, there are better tools: direct spending, grants, loan guarantees, regulatory reform. These tools are transparent, measurable, and can be adjusted without rewriting the tax code.

Tax preferences are the worst way to deliver subsidies because they're invisible (most taxpayers don't know they exist), regressive (they're worth more to people in higher brackets), and durable (once created, they're nearly impossible to repeal because they create constituencies that lobby for their preservation).

**A principled test:** A tax preference is justified only when (a) the behavior it encourages produces a clear positive externality that the market would not adequately provide, and (b) the preference is the most efficient way to generate that externality. The charitable deduction arguably passes this test. QSBS fails it — starting a C-corp doesn't produce a positive externality that starting an LLC doesn't. 1031 exchanges fail it — swapping one investment property for another doesn't produce a positive externality. Opportunity Zones fail it — place-based investment can produce positive externalities, but OZs are the least efficient way to generate them (63% of OZ census tracts received zero investment; 1% of tracts got 42% of the money).

The principle isn't "no nudges ever." It's: **the default should be neutrality, and any deviation from neutrality should carry a heavy burden of proof.**

Every special rule we keep also brings hidden costs. Added complexity creates enforcement headaches: more loopholes sprout, the IRS spends more on audits and litigation, and revenue leaks out long before Congress even learns about the gap. And the deadweight loss of the "tax optimization" industry — CPAs, law firms, and boutique consultants whose business model is finding new ways for the wealthy to duck their bill — redirects resources from productive output to pure rent-seeking. Simplifying the base shrinks that sector and puts more of the tax burden on actual economic activity rather than on who has the best lawyer.

#### Q21: Canada has a lifetime capital gains system that got more complex over time. What makes this different?

This is the best objection anyone can make, and we take it seriously.

Canada's Lifetime Capital Gains Exemption (LCGE) started relatively clean in 1972 and has accumulated layers of complexity over 50 years — qualifying tests, industry carve-outs, the new Canadian Entrepreneurs' Incentive with its own eligibility criteria and phase-in schedules. CPA Canada itself has questioned whether "creating complex tax benefits to offset other complex tax rules helps or hinders the tax system."

Three design choices in this proposal are specifically intended to resist this trajectory:

1. **Universality.** Canada's LCGE applies only to qualified small business shares and farm/fishing property. That narrow scope *invites* lobbying for expansion to other categories, which creates new boundaries, which creates new complexity. This framework applies to all capital gains from all sources. There are no qualifying tests because there are no categories. The dairy farmer, the app developer, and the day trader all face the same rules.

2. **Structural simplicity.** The mechanism is a single running total with progressive brackets. There's nothing to "carve out" because there are no special provisions to carve out *from*. Canada's complexity grew because each exception created a boundary that needed policing. This framework has no exceptions, so there are no boundaries.

3. **The three-repeal anchor.** By simultaneously abolishing the estate tax, AMT, and NIIT, the framework creates a political constituency (primarily Republican) invested in the new system's *survival*. Rolling back would mean re-imposing three taxes the repeal coalition fought to eliminate. This makes complexity creep harder because any "improvement" that threatens the system's simplicity risks unraveling the entire deal.

Will lobbying pressure exist? Absolutely. Real estate will want its 1031 back. VCs will want their QSBS back. The question is whether the system's architecture makes it harder to grant those requests without breaking the whole structure. We believe it does — a system with zero exceptions is harder to degrade than a system that already has fifty.

But we're not naive. The honest answer is: **every tax system trends toward complexity over time.** The goal isn't perfection — it's raising the cost of complexity so that each new exception has to clear a higher bar.

### On Scope

#### Q22: What about income tax brackets?

Income tax bracket reform (including the possibility of adding a top bracket above 37%) is addressed in a companion proposal. This document focuses exclusively on capital gains.

The one structural dependency: the top capital gains rate (37%) converges with the top ordinary income rate (37%). If income tax reform changes the top rate, the capital gains ceiling should move with it to maintain convergence.

#### Q23: What about the child tax credit?

A unified child benefit ($4,000/child, fully refundable, consolidating CTC/EITC/CDCC) is addressed in a companion proposal. It is scoped out of this document to keep the capital gains framework laser-focused.

#### Q24: What about retirement accounts?

Retirement accounts (401k, IRA, Roth, 529) are explicitly excluded from the lifetime counter. Gains within these accounts do not consume the 0% bracket.

A separate companion proposal addresses retirement account consolidation and simplification. For purposes of this framework, the current retirement account structure is unchanged.

#### Q25: What about charitable giving?

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

TODO - these are all "Left Leaning" - I think we can also reference some "simplify the tax code" thinkers?

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

*Contact: Matt Sly — me@mattsly.com*
