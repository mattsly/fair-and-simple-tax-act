---
layout: plain
title: "America's Most Expensive Technical Debt"
description: "A software entrepreneur's case for radically simple capital gains tax reform. Five rules that eliminate 10-15% of the tax code, close buy-borrow-die, and cut taxes for 98% of Americans."
image: /fair-and-simple-tax-act/lifetime-gains-framework.png
twitter:
  card: summary_large_image
---

# America's Most Expensive Technical Debt, Part 1: Capital Gains

### A software entrepreneur's case for simple, fair and durable capital gains tax reform

*By Matt Sly*

---

## The Algorithm Nobody Designed and the Product Nobody Wants

A billionaire can live tax-free in America. Not through some exotic offshore scheme, but through an entirely legal sequence called "buy, borrow, die." Buy appreciated assets. Borrow against them to fund your lifestyle (loans aren't income, so no tax). Die. Your heirs inherit those assets with the tax basis reset to market value, erasing a lifetime of gains. The lifetime tax on those gains: zero.

This isn't tax fraud. It's "tax planning." And buy-borrow-die is just one example of the absurdities enabled by our capital gains system. [A hedge fund manager pays a lower rate than the teacher who taught her kids](https://www.propublica.org/article/the-secret-irs-files-trove-of-never-before-seen-records-reveal-how-the-wealthiest-avoid-income-tax). A couple who sells the business they spent 30 years building pays capital gains tax on decades of inflation, not real profit. A restaurateur who takes no salary for a decade to build the best restaurant in her city pays full freight when she finally sells, while a venture-backed founder who drew a market salary the whole time walks away from her exit with up to $10 million tax-free. The cost of this complexity is everywhere: [billions in uncollected tax](https://www.cbpp.org/research/closing-the-tax-gap), billions more in fees to navigate the system, and the quiet understanding that the rules are written for people who can afford to game them.

A tax code is an algorithm. It takes inputs (your income, your assets, your transactions) and produces an output (your tax bill). A well-designed algorithm is legible, predictable, and deterministic. The federal tax code is none of these. Its complexity is a byproduct of a political system that rewards adding new provisions rather than refactoring existing ones. In most cases, each provision was a well-intended solution to a real problem. But in a complex system, "well-intended" often invites unintended consequences. Over a century, these "reasonable solutions" have compounded into a byzantine mess that nobody actually designed.

Consider the estate tax: created to prevent dynastic wealth. But the estate tax provided the moral "double taxation" cover for stepped-up basis (the idea that we shouldn't tax gains at death if we're already taxing the estate). Stepped-up basis birthed buy-borrow-die. Similarly, when a handful of wealthy taxpayers started paying zero income tax, rather than fix the underlying "bug," Congress bolted on the Alternative Minimum Tax as a parallel shadow tax code, which now ensnares millions of upper-middle-class families while the truly wealthy route around it. In software terms, this is spaghetti code: a tangled mess of hotfixes created to manage the side effects of previous hotfixes.

I've spent twenty years in software, and I've seen the tax code from most of the angles available to an American: salaried employee, startup employee with options, big tech employee paid in RSUs, founder with an exit, angel investor. Here is my conclusion as both a software professional and a concerned citizen: American capital gains taxation is the single most consequential piece of technical debt in the United States. 

It can be refactored with five simple rules. Those rules cut capital gains taxes for 98% of Americans, close buy-borrow-die, and generate an estimated $85-200 billion per year in deficit reduction (math below). They also eliminate roughly 10-15% of the Internal Revenue Code (including the AMT, the NIIT, and the estate tax) and render a wealth tax unnecessary in the process.

---

## The Capital Gains Refactor: Five Rules

Here's the proposal. Five rules replace a century of accretion.

> Note: the specific numbers below are "stakes in the ground." They're open for debate and much less important than the general framework.

**Rule 1: Every American gets a lifetime capital gains exemption.** $2.5 million per person; $5 million for a married couple. One bucket replaces a dozen narrow exclusions. Any source, any asset type, no qualification tests, no holding-period games. Losses offset gains within the year, same as current law.

**Rule 2: Above the exemption, the rate slides from 0% up to the top income tax rate.** From $2.5 million to $10 million in cumulative lifetime gains, the rate phases linearly from 0% to the current top marginal rate (currently 37%). Above $10 million, all gains are taxed at that top rate. Two details matter here. First, the top rate is *pegged* to whatever the top marginal income tax rate happens to be. It's not a separate number Congress has to update. Second, the rate applies regardless of the taxpayer's other income. A retiree with $0 W-2 income and $15M in lifetime gains pays the same top rate as a wage earner at $500K. This is what eliminates the preferential rate that lets hedge fund managers pay less than teachers.

**Rule 3: You can't defer gains forever.** Realization happens whenever appreciated wealth changes hands in a way that preserves or transfers its availability for private consumption. Four events trigger realization under this principle: sale, death, gift, and borrowing.

- **Sale.** Unchanged from current law.
- **Death.** Unrealized gains are realized on the decedent's final return. Heirs receive basis at fair market value. This is how [Canada has handled it since 1972](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/report-income/capital-gains.html). This single change ends stepped-up basis, the provision that currently lets heirs inherit appreciated assets with a clean tax slate and erases a lifetime of untaxed gains.
- **Gift to another individual.** The donor pays tax on unrealized gains at the time of transfer. The recipient gets basis at gift-date market value. (The annual $18K gift exclusion is retained.)
- **Borrowing against appreciated assets.** When you pledge appreciated assets as collateral, the unrealized gain is deemed realized. Basis steps up to prevent double taxation on eventual sale. Mechanics informed by [research from the Yale Budget Lab](https://budgetlab.yale.edu/research/buy-borrow-die-options-reforming-tax-treatment-borrowing-against-appreciated-assets). If the collateral has no unrealized gain (a purchase mortgage on a newly-bought home, for example), the deemed realization is $0.

*Transfers to qualified charities are not realization events. The appreciation exits the private economy. See "What About Charitable Giving?" below for mechanics.*

**Rule 4: Basis is indexed to inflation.** Your cost basis is adjusted by CPI, so you're taxed on real economic gains, not phantom ones. A house bought for $200,000 in 1995 has a CPI-adjusted basis of roughly $400,000 in 2026. Indexing applies symmetrically to gains and losses. The government doesn't get to profit from inflation anymore.

**Rule 5: Roth reform.** Four changes to simplify Roth accounts and close the [Peter Thiel loophole](https://www.propublica.org/article/lord-of-the-roths-how-tech-mogul-peter-thiel-turned-a-retirement-account-for-the-middle-class-into-a-5-billion-dollar-tax-free-piggy-bank), where a hedge fund manager turned a middle-class retirement vehicle into a $5 billion tax shelter:

1. Remove the income cap for direct Roth contributions
2. Raise the annual contribution limit to $15,000 (from $7K/$8K)
3. Cap the total Roth balance at $5 million per person (growth above this continues tax-free, but new contributions freeze)
4. Close the "backdoor Roth" conversion entirely

That's it. Five rules. From these, an extraordinary amount of existing tax infrastructure becomes unnecessary.

*The full mechanics — including the lifetime counter algorithm, transition rules, trust treatment, and complete list of provisions eliminated — are in the [technical specification](./technical_spec.html). When mechanics change, the spec governs.*

![The Lifetime Gains Framework — How the tax rate changes with cumulative lifetime capital gains](./lifetime-gains-framework.png)

---

## What Falls Away

The five rules make entire categories of tax law redundant.

**The Alternative Minimum Tax.** Created in 1969 because [155 wealthy Americans paid zero income tax that year](https://taxfoundation.org/taxedu/glossary/alternative-minimum-tax-amt/). When there are no exclusions to exploit, the AMT's purpose evaporates. It's been functionally gutted for high earners anyway since the 2017 tax cuts, but it still ensnares upper-middle-class families in high-tax states. Good riddance.

**The Net Investment Income Tax.** A 3.8% surtax bolted onto the Affordable Care Act in 2010 to fund Medicare. Under this framework, gains above the exemption are taxed at rates far exceeding 3.8%. The NIIT becomes redundant by design.

**The estate tax.** A tax that looks progressive on paper and fails in practice. The statutory rate is 40%. The effective rate on well-planned estates is typically 10-15% because an entire industry exists to help wealthy families avoid it. Under this framework, death is a realization event and all unrealized gains are taxed on the decedent's final return. The replacement mechanism collects more revenue from large estates with fewer loopholes. (Full argument below in [The Estate Tax Question](#the-estate-tax-question).)

**A wealth tax.** Not currently law, but perennially proposed. This framework delivers the same progressivity a wealth tax aims for (taxing accumulated wealth, not just current income) through a simpler, constitutionally safer mechanism. (Addressed below in [The Wealth Tax Question](#the-wealth-tax-question).)

**Twelve special exclusions and preferences are replaced by the universal exemption and the five rules.** Some are replaced by the larger universal exemption; others fall away because Rule 3 ends the deferral games. The most significant:

- **[QSBS / Section 1202](https://www.law.cornell.edu/uscode/text/26/1202)** — the "qualified small business stock" exclusion, which gives founders a break of up to $15M in gains ([raised from $10M by OBBB in 2025](https://www.thetaxadviser.com/issues/2025/nov/qsbs-gets-a-makeover-what-tax-pros-need-to-know-about-sec-1202s-new-look/)). It requires a C-corp structure, a 3-5 year hold, an active business test, and a $75M gross assets test. Most founders don't qualify. Under this framework, every founder gets the $2.5M / $5M universal exemption with none of the qualification tests.

- **[Section 121](https://www.law.cornell.edu/uscode/text/26/121)** — the primary home sale exclusion ($250K single / $500K married). Still helpful, but narrow: it covers your house and nothing else. Under this framework, the universal exemption is 10x larger and covers your home, your stocks, your small business, and your rental properties.

- **[Section 1031](https://www.law.cornell.edu/uscode/text/26/1031) like-kind exchanges** — the real estate deferral mechanism that lets investors roll gains into new properties tax-free, with help from an industry of "qualified intermediaries" who hold money in escrow during the 45-day rollover window. Eliminated by Rule 3 (no more deferral). The money will still flow; investors will just pay tax on real gains when they realize them.

- **Stepped-up basis at death** — the most valuable provision in the entire tax code. Heirs inherit appreciated assets with the basis reset to current market value, erasing a lifetime of unrealized gains. Eliminated by Rule 3 (death is a realization event).

- **GRATs, dynasty trusts, and valuation discounts** — the estate planning toolkit that lets ultra-wealthy families transfer hundreds of millions to heirs with little or no tax. [The Walton family used GRATs to transfer billions with zero gift tax liability.](https://www.bloomberg.com/graphics/infographics/how-to-preserve-a-family-fortune-through-tax-tricks.html) These structures work by exploiting the gap between estate tax and income tax, and by deferring realization indefinitely. Eliminated by Rule 3 (gifts and trust transfers are realization events; no more indefinite deferral).

Plus seven more: carried interest (see [Every Perennial Debate, Resolved](#every-perennial-debate-resolved)), Opportunity Zone deferrals, Section 453 installment sales, the Section 1256 60/40 rule for derivatives, the 28% collectibles rate, the lifetime gift tax exemption, and Section 1244 small business loss treatment. Full list in the [technical specification](https://www.mattsly.com/fair-and-simple-tax-act/technical_spec.html).

In total, these five rules eliminate roughly 10-15% of the Internal Revenue Code by volume, along with the thousands of pages of Treasury regulations, IRS guidance, and Tax Court precedent that interpret them.

Most software engineers will tell you: deleting code *and* improving the product is the most satisfying kind of work. But simplification isn't just aesthetically pleasing. It matters because every eliminated provision is an eliminated edge case, an eliminated loophole, and an eliminated compliance cost. The current system has roughly two dozen independent configuration parameters (the exemption amount for each special provision, the holding period rules, the phase-out thresholds, the asset-type definitions, and so on). The proposed system has two: the exemption level ($2.5M / $5M) and the phase-out ceiling ($10M / $20M). Both are indexed to inflation. Both can be adjusted by Congress without reopening the structural framework. Fewer parameters means fewer interactions, fewer exploits, and a system that's easier to administer, audit, and explain.

That's what radical simplification actually looks like.

---

## What About Charitable Giving?

One exception deserves its own treatment: donations of appreciated assets to qualified charities. This is less radical than it first appears.

Under current law, donating $1M of appreciated stock gets the donor a $1M income tax deduction even though only $100K of that was ever taxed — the other $900K is pure appreciation that has never been realized. The deduction exceeds what the donor actually paid tax on.

Under this framework, the capital gains treatment is identical to current law: the appreciation isn't realized, doesn't eat the lifetime cap, and is never taxed. But the income tax deduction is aligned with the donor's actual basis ($100K in this example, CPI-adjusted per Rule 4). You're deducting what you contributed in after-tax terms, which is how deductions work in every other context. Canada uses a similar structure for decades. 

As an example: a middle-class donor giving $5,000 of stock they bought for $4,500 barely notices. A billionaire donating $1 billion of stock with a $10 million basis sees their deduction drop from $1 billion to $10 million — which is the outcome the framework is designed to produce.

Broader questions about how charitable giving should be incentivized (deduction vs. credit, non-itemizer access, foundation governance) are covered in an upcoming companion proposal.

---

## Running the Numbers

**A homeowner** who sells their primary residence for a $250,000 real gain (after inflation adjustment): $0 tax under current law, $0 under this framework. **No change.** The exemption now covers all asset types, not just housing.

**A retiree** who spent 40 years contributing to a 401(k) and taxable brokerage accounts, and sells $800,000 of appreciated stock over a 20-year retirement: Under current law, about $190,000 in capital gains tax over the retirement period. Under this framework, $0. **$190,000 less.** The entire amount falls within the lifetime exemption. The "lifetime" in "Lifetime Gains Framework" is literal. Gains accumulated over a career of saving are not penalized by being realized all at once.

**A small business owner** who runs a successful auto repair shop for 25 years and sells it for $1.5 million (on a $200K basis): Under current law, about $310,000 in capital gains tax (assuming no QSBS qualification, which auto shops don't get because they're LLCs). Under this framework, $0. **$310,000 less.** This is what "fuel the climb" actually looks like for the 99.9% of small business owners who will never raise venture capital.

**A tech employee** who accumulates $1.2 million in gains from RSU vesting and stock sales over a 15-year career at two companies: Under current law, about $285,000 in capital gains tax. Under this framework, $0. **$285,000 less.** The entire amount falls within the lifetime exemption. No special elections, no holding-period optimization, no tax-lot accounting games.

**An angel investor** who writes ten $25,000 checks into friends' startups over twenty years. Eight go to zero. One returns $100K. One returns $2 million: Under current law, the returns are subject to capital gains tax (roughly $475,000 combined, assuming no QSBS qualification), partially offset by capital losses on the failures. Under this framework, $0. **$475,000 less.** The entire portfolio outcome falls within the lifetime exemption.

**A real estate investor** who owns three rental properties worth $2.5 million combined, with $1 million in real (inflation-adjusted) appreciation, and sells them in retirement: Under current law with 1031 exchanges used throughout the holding period, she could defer indefinitely; without 1031, she would owe about $238,000. Under this framework, $0. **$238,000 less.** She pays no tax for the first time because the exemption is universal, not locked to a primary residence.

**A couple selling a long-held family business** for $6 million (basis $500K, held 30 years, most appreciation is inflation): After CPI adjustment, the real gain is about $3.5 million. Under current law, they pay roughly $833,000 in capital gains tax on nominal appreciation that includes $2 million of pure inflation. Under this framework, the $5M married exemption covers most of it; they pay about $80,000 on the real gain above the exemption. **$753,000 less.** This is the archetype from the opening: the couple who spent 30 years building a business paying tax on decades of inflation. The framework fixes it.

**An early startup employee** (not a founder) who joined a startup at year 2, exercised $15K in options, and walks away after IPO with $3M in gains: Under current law, the employee doesn't qualify for QSBS (stock acquired via options has complex rules) and pays about $714,000. Under this framework, about $30,000. **$684,000 less.** The framework treats early employees the same as founders. The current system doesn't.

**A founder whose exit doesn't make headlines** who builds a company over eight years and exits for $2.8 million in real gains: Under current law, if they don't qualify for QSBS (and most founders don't, because it requires a C-corp structure, a $75 million gross asset test, a 3-5 year tiered holding period, and an active business test), they pay roughly $555,000. Under this framework, approximately $2,200. **$553,000 less.** The exemption covers almost the entire gain.

**A successful founder with a $19 million exit:** Under current law, about $4.5 million in tax. Under this framework, about $4.7 million. **$200,000 more.** Effectively breakeven on the tax bill, with one significant bonus: the founder never checks for AMT, calculates NIIT, or attempts QSBS qualification. No planning fees, no entity restructuring, no five-year holding-period calendar on the wall.

**A billionaire borrowing against appreciated stock** who pledges $10 million of appreciated shares (basis $2M, unrealized gain $8M) as collateral for a $5 million loan to fund her lifestyle: Under current law, loan proceeds aren't income and the unrealized gain is untouched. Tax: $0. This is buy-borrow-die. Under this framework, the $8 million unrealized gain is deemed realized under Rule 3 and taxed at the top ordinary rate: about $2.96 million. **$2.96 million more.** Her cost basis in the pledged stock then steps up to $10 million, preventing double taxation when she eventually sells or dies. If she repeats this pattern annually with different appreciated collateral, she pays roughly this amount every year, which is the point.

**A mega-exit founder with $95 million in gains:** Under current law, about $22.6 million. Under this framework, about $32.8 million. **$10.2 million more.** At this scale, the sliding scale has fully phased to ordinary income rates, and the current system's 23.8% flat rate becomes visibly inadequate.

**An inherited estate with $15 million in unrealized gains:** Under current law, $0. Stepped-up basis wipes the slate clean. Under this framework, about $3.2 million. **$3.2 million more.** Collected on wealth that currently escapes taxation entirely.

**A dynasty estate with $500 million, $400 million in unrealized gains:** Under current law, with competent estate planning, the family pays roughly $30-50 million. Under this framework, approximately $148 million. **$98-118 million more.** The framework collects three to five times what the current system actually collects. This is where the revenue argument lives: in the chasm between what the estate tax theoretically collects and what it actually collects after planning.

The pattern is clear. The framework is designed to fuel the climb: homeowners, retirees, small business owners, tech employees, angel investors, landlords, long-held family businesses, early startup employees, and founders whose exits don't make headlines. All pay the same or less. Tax increases are concentrated exactly where they should be: on very large single-event accumulations (above roughly $17.5 million in cumulative lifetime gains), inherited estates exploiting stepped-up basis, and the borrow-against-assets strategy that allows billionaires to live tax-free. The current system structurally advantages those who've already arrived. This one clears the path for those still building.
**A homeowner** who sells their primary residence for a $250,000 real gain (after inflation adjustment): $0 tax under current law, **$0 under this framework**. No change, except the exemption now covers all asset types, not just housing.

**A retiree** who spent 40 years contributing to a 401(k) and taxable brokerage accounts, and sells $800,000 of appreciated stock over a 20-year retirement: Under current law, about $190,000 in capital gains tax over the retirement period. Under this framework: **$0**. The entire amount falls within the lifetime exemption. The "lifetime" in "Lifetime Gains Framework" is literal. Gains accumulated over a career of saving are not penalized by being realized all at once.

**A small business owner** who runs a successful auto repair shop for 25 years and sells it for $1.5 million (on a $200K basis): Under current law, about $310,000 in capital gains tax (assuming no QSBS qualification, which auto shops don't get because they're LLCs). Under this framework: **$0**. The gain is within the lifetime exemption. This is what "fuel the climb" actually looks like for the 99.9% of small business owners who will never raise venture capital.

**A tech employee** who accumulates $1.2 million in gains from RSU vesting and stock sales over a 15-year career at two companies: Under current law, about $285,000 in capital gains tax. Under this framework: **$0**. The entire amount falls within the lifetime exemption. No special elections, no holding-period optimization, no tax-lot accounting games.

**An angel investor** who writes ten $25,000 checks into friends' startups over twenty years. Eight go to zero. One returns $100K. One returns $2 million: Under current law, the returns are subject to capital gains tax (roughly $475K combined, assuming no QSBS qualification), partially offset by capital losses on the failures. Under this framework: **$0**. The entire portfolio outcome falls within the lifetime exemption.

**A real estate investor** who owns three rental properties worth $2.5 million combined, with $1 million in real (inflation-adjusted) appreciation, and sells them in retirement: Under current law with 1031 exchanges used throughout the holding period, she could defer indefinitely; without 1031, she would owe about $238,000. Under this framework: **$0** (within exemption). She pays no tax for the first time because the exemption is universal, not locked to a primary residence.

**A couple selling a long-held family business** for $6 million (basis $500K, held 30 years, most appreciation is inflation): After CPI adjustment, the real gain is about $3.5 million. Under current law, they pay roughly $833,000 in capital gains tax on nominal appreciation that includes $2 million of pure inflation. Under this framework, the $5M married exemption covers most of it; they pay **about $80,000** on the real gain above the exemption. This is the archetype from the opening: the couple who spent 30 years building a business paying tax on decades of inflation. The framework fixes it.

**An early startup employee** (not a founder) who joined a startup at year 2, exercised $15K in options, and walks away after IPO with $3M in gains: Under current law, the employee doesn't qualify for QSBS (stock acquired via options has complex rules), and pays about $714,000. Under this framework: **about $30,000**. The framework treats early employees the same as founders. The current system doesn't.

**A founder whose exit doesn't make headlines** who builds a company over eight years and exits for $2.8 million in real gains: Under current law, if they don't qualify for QSBS (and most founders don't, because it requires a C-corp structure, a $75 million gross asset test, a 3-5 year tiered holding period, and an active business test), they pay roughly $555,000. Under this framework: **approximately $2,200**. The exemption covers almost the entire gain.

**A successful founder with a $19 million exit:** Under current law, about $4.5 million in tax. Under this framework, **about $4.7 million**. Within $200,000, effectively breakeven on the tax bill, with one significant bonus: the founder never checks for AMT, calculates NIIT, or attempts QSBS qualification. No planning fees, no entity restructuring, no five-year holding-period calendar on the wall.

**A billionaire borrowing against appreciated stock** who pledges $10 million of appreciated shares (basis $2M, unrealized gain $8M) as collateral for a $5 million loan to fund her lifestyle: Under current law, loan proceeds aren't income and the unrealized gain is untouched. Tax: $0. This is buy-borrow-die. Under this framework, the $8 million unrealized gain is deemed realized under Rule 3 and taxed at the top ordinary rate: **about $2.96 million**. Her cost basis in the pledged stock then steps up to $10 million, preventing double taxation when she eventually sells or dies. If she repeats this pattern annually with different appreciated collateral, she pays roughly this amount every year, which is the point.

**A mega-exit founder with $95 million in gains:** Under current law, about $22.6 million. Under this framework, **about $32.8 million**. This founder pays roughly $10 million more. At this scale, the sliding scale has fully phased to ordinary income rates, and the current system's 23.8% flat rate becomes visibly inadequate.

**An inherited estate with $15 million in unrealized gains:** Under current law, $0. Stepped-up basis wipes the slate clean. Under this framework: **about $3.2 million**, collected on wealth that currently escapes taxation entirely.

**A dynasty estate with $500 million, $400 million in unrealized gains:** Under current law, with competent estate planning, the family pays roughly $30-50 million. Under this framework: **approximately $148 million**. The framework collects three to five times what the current system actually collects. This is where the revenue argument lives: in the chasm between what the estate tax theoretically collects and what it actually collects after planning.

The pattern is clear. The framework is designed to fuel the climb: homeowners, retirees, small business owners, tech employees, angel investors, landlords, long-held family businesses, early startup employees, and founders whose exits don't make headlines. All pay the same or less. Tax increases are concentrated exactly where they should be: on very large single-event accumulations (above roughly $17.5 million in cumulative lifetime gains), inherited estates exploiting stepped-up basis, and the borrow-against-assets strategy that allows billionaires to live tax-free. The current system structurally advantages those who've already arrived. This one clears the path for those still building.
**A homeowner** who sells their primary residence for a $250,000 real gain (after inflation adjustment): $0 tax under current law, $0 tax under this framework. No change, except the exemption now covers all asset types, not just housing.

**A retiree** who spent 40 years contributing to a 401(k) and taxable brokerage accounts, and sells $800,000 of appreciated stock over a 20-year retirement: Under current law, about $190,000 in capital gains tax over the retirement period. Under this framework: $0. The entire amount falls within the lifetime exemption. The "lifetime" in "Lifetime Gains Framework" is literal — gains accumulated over a career of saving are not penalized by being realized all at once.

**A small business owner** who runs a successful auto repair shop for 25 years and sells it for $1.5 million (on a $200K basis): Under current law, about $310,000 in capital gains tax (assuming no QSBS qualification, which auto shops don't get because they're LLCs). Under this framework: $0. The gain is within the lifetime exemption. This is what "fuel the climb" actually looks like for the 99.9% of small business owners who will never raise venture capital.

**A tech employee** who accumulates $1.2 million in gains from RSU vesting and stock sales over a 15-year career at two companies: Under current law, about $285,000 in capital gains tax. Under this framework: $0. The entire amount falls within the lifetime exemption. No special elections, no holding-period optimization, no tax-lot accounting games.

**An angel investor** who writes ten $25,000 checks into friends' startups over twenty years. Eight go to zero. One returns $100K. One returns $2 million: Under current law, the returns are subject to capital gains tax (roughly $475K combined, assuming no QSBS qualification), partially offset by capital losses on the failures. Under this framework: $0. The entire portfolio outcome falls within the lifetime exemption.

**A real estate investor** who owns three rental properties worth $2.5 million combined, with $1 million in real (inflation-adjusted) appreciation, and sells them in retirement: Under current law with 1031 exchanges used throughout the holding period, she could defer indefinitely; without 1031, she would owe about $238,000. Under this framework: $0 (within exemption). She pays no tax for the first time because the exemption is universal, not locked to a primary residence.

**A couple selling a long-held family business** for $6 million (basis $500K, held 30 years, most appreciation is inflation): After CPI adjustment, the real gain is about $3.5 million. Under current law, they pay roughly $833,000 in capital gains tax on nominal appreciation that includes $2 million of pure inflation. Under this framework, the $5M married exemption covers most of it; they pay about $80,000 on the real gain above the exemption. This is the archetype from the opening — the couple who spent 30 years building a business paying tax on decades of inflation. The framework fixes it.

**An early startup employee** (not a founder) who joined a startup at year 2, exercised $15K in options, and walks away after IPO with $3M in gains: Under current law, the employee doesn't qualify for QSBS (stock acquired via options has complex rules), and pays about $714,000. Under this framework: about $30,000. The framework treats early employees the same as founders. The current system doesn't.

**A founder whose exit doesn't make headlines** who builds a company over eight years and exits for $2.8 million in real gains: Under current law, if they don't qualify for QSBS (and most founders don't, because it requires a C-corp structure, a $75 million gross asset test, a 3-5 year tiered holding period, and an active business test), they pay roughly $555,000. Under this framework: approximately $2,200. The exemption covers almost the entire gain.

**A successful founder with a $19 million exit:** Under current law, about $4.5 million in tax. Under this framework, about $4.7 million. Within $200,000 — effectively breakeven on the tax bill, with one significant bonus: the founder never checks for AMT, calculates NIIT, or attempts QSBS qualification. No planning fees, no entity restructuring, no five-year holding-period calendar on the wall.

**A mega-exit founder with $95 million in gains:** Under current law, about $22.6 million. Under this framework, about $32.8 million. This founder pays more, about $10 million more. At this scale, the sliding scale has fully phased to ordinary income rates, and the current system's 23.8% flat rate becomes visibly inadequate.

**An inherited estate with $15 million in unrealized gains:** Under current law, $0. Stepped-up basis wipes the slate clean. Under this framework, about $3.2 million, collected on wealth that currently escapes taxation entirely.

**A billionaire borrowing $5 million per year against appreciated stock:** Under current law, $0. This is buy-borrow-die. Under this framework, $1.85 million per year.

**A dynasty estate with $500 million, $400 million in unrealized gains:** Under current law, with competent estate planning, the family pays roughly $30-50 million. Under this framework, approximately $148 million. The framework collects three to five times what the current system actually collects. This is where the revenue argument lives: in the chasm between what the estate tax theoretically collects and what it actually collects after planning.

The pattern is clear. The framework is designed to fuel the climb: homeowners, retirees, small business owners, tech employees, angel investors, landlords, long-held family businesses, early startup employees, and founders whose exits don't make headlines — all pay the same or less. Tax increases are concentrated exactly where they should be: on very large single-event accumulations (above roughly $17.5 million in cumulative lifetime gains), inherited estates exploiting stepped-up basis, and the borrow-against-assets strategy that allows billionaires to live tax-free. The current system structurally advantages those who've already arrived. This one clears the path for those still building.

---

*What follows is a deeper dive into the most common questions and objections. If you're already sold on the architecture, skip to [The Coalition](#the-coalition). If you want to stress-test the idea, read on, but fair warning that it will get a little wonky.*

---

## The Estate Tax Question

Abolishing the estate tax sounds like a conservative fever dream. But the estate tax is a policy that looks progressive on paper and fails in practice. It theoretically imposes a 40% rate above a large threshold. In reality, well-advised estates routinely pay 10-15% or less, and the wealthiest pay the least, because they can afford the planners who make it disappear. As Professor Ray Madoff documents in [*The Second Estate*](https://press.uchicago.edu/ucp/books/book/chicago/S/bo256019296.html), the estate tax has become political cover: it *looks* like a tax on dynastic wealth, while its hollowed-out structure ensures the wealthiest families pay the least.

This framework replaces it with a mechanism that actually collects. Death as a realization event is not a radical experiment. It has been the [functional model in Canada since 1972](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/report-income/capital-gains.html), where it successfully replaced their version of the estate tax.

When death is a realization event and all gains are taxed on the decedent's final return, there is no stepped-up basis, no GRAT loophole, no valuation discount game. Even the incentive to lowball gift valuations is structurally defanged: because there is no stepped-up basis, an undervalued gift simply shifts a lower basis to the recipient, who pays a correspondingly larger tax bill later. The total tax collected is roughly the same, so the donor and recipient are no longer on the same team. Dynasty trusts lose their power too: trust-held assets are deemed realized at each generational transfer, so wealth can no longer skip across generations untaxed. A $100 million estate with $80 million in unrealized gains pays approximately $29 million with no planning tricks available. A $500 million dynasty estate pays roughly $148 million, compared to the $30-50 million the current estate tax actually collects after planning.

Critics will inevitably point to the liquidity challenge: if death is a realization event, how do heirs pay the tax on an illiquid family business or farm without being forced to sell it? The solution is straightforward: a 15-year IRS lien option, conceptually similar to existing estate tax installment plans. The IRS places a lien on the asset; the heir pays the tax over fifteen years out of operating cash flow. No fire sale required. And if a family business genuinely cannot service its tax obligation over fifteen years, that is a valuation signal, not a liquidity crisis.

The trade is simple: abolish a tax that collects [$20-25 billion per year](https://taxpolicycenter.org/briefing-book/how-many-people-pay-estate-tax) badly, and replace it with a mechanism that collects three to five times more from the estates that matter most. Progressives get more revenue and no escape routes. Conservatives get the estate tax repeal they've wanted for a generation.

---

## The Wealth Tax Question

A wealth tax polls well. It feels fair: if you have a billion dollars, pay a percentage every year. But [every European country that tried one repealed it](https://taxfoundation.org/research/all/eu/wealth-tax-impact/). France's wealth tax drove an estimated 42,000 millionaires out of the country before it was repealed in 2017. Sweden and Austria reached the same conclusion. The problems are structural: annual valuation of illiquid assets (private businesses, real estate, art) is expensive, subjective, and gameable. And a wealth tax is yet another layer bolted onto an already brittle system. This is the same unwieldy design pattern that gave us the AMT and the NIIT. More tax types means more interactions, more edge cases, and more loopholes. Enforcement costs eat the revenue. And capital flight risk is real as wealthy individuals move to jurisdictions that don't impose the tax, shrinking the base faster than the tax can collect from it.

This framework achieves what a wealth tax promises without these failures. By expanding realization events to include death, gifts, and borrowing, and by taxing gains above the generous phase-out target as ordinary income, it captures wealth accumulation at the moments when assets are easiest to value (transaction prices, not annual appraisals) and hardest to hide (documented transactions with third-party reporting). It uses existing IRS infrastructure rather than requiring a new valuation bureaucracy. Same progressive outcome, half the enforcement cost, none of the constitutional risk.

---

## Why Not Just Tax All Gains as Income?

This is the first objection from the left, and it deserves a direct answer. If the goal is to treat investment income like wages, why bother with an exemption and a sliding scale? Why not just eliminate the preferential rate and be done with it?

First, we have the **bunching problem**: Imagine a founder who builds a company over ten years. For a decade, they may take a below-market salary (or $0) while pouring their labor into equity. When they finally exit for $2.8 million, taxing that as "income" in a single year is a mathematical penalty. It treats them as if they earned $2.8 million every year, pushing them into the highest possible tax bracket instantly.

Investments, with both time and money, also involve **failure risk**. Many founders work for years only to see their equity go to zero. The exemption is a structural buffer that accounts for the fact that capital gains are often the lumpy, high-risk harvest of a decade of work.

But the most salient reason to protect the "climb" is that entrepreneurial risk is a public good. When someone bets their career or their savings on a new idea, the successful outcome benefits everyone, not just the investor. A tax code that punishes that risk from dollar one is a tax code that inadvertently subsidizes stagnation.

The natural follow-up: "OK, founders take risks, but what about someone just buying Apple stock? Why does that deserve preferential treatment?" Two reasons. First, even passive investors provide liquidity and price discovery that make capital markets function. When a dentist in Omaha buys shares on Robinhood, she is providing the capital that lets the next founder go public. Second, and more practically: every attempt to distinguish "deserving" investment from "undeserving" investment creates exactly the kind of complexity this framework eliminates. The QSBS rules, the material participation tests, the qualified real estate professional carve-outs are all attempts to draw that line. Each one spawned an industry of lawyers structuring around it. A universal exemption sidesteps this entirely. The juice is not worth the squeeze.

We want every American to build wealth, but the current system only provides meaningful tax breaks to those who are already wealthy and can navigate complex entity structures like QSBS or own homes. By creating a $2.5 million universal exemption, we provide a powerful, simple incentive for *every* citizen to invest and save.

To be clear: above $10 million in cumulative lifetime gains, gains *are* taxed as ordinary income under this framework. The disagreement isn't about whether gains should be treated as income. It's about where the exemption sits and how fast the rate phases in. Those are exactly the two parameters ($2.5M / $5M exemption, $10M / $20M ceiling) that this framework makes easy to debate and adjust.

---

## Won't Higher Rates Kill Innovation?

Critics may argue that raising the top capital gains rate to 37% and eliminating the QSBS exclusion ([Section 1202](https://www.law.cornell.edu/uscode/text/26/1202)) will stifle startups and scare away angel investors. History says otherwise: Google (IPO [2004](https://www.britannica.com/money/Google-Inc)), the iPhone (launched 2007), and NVIDIA (founded [1993](https://www.britannica.com/money/NVIDIA-Corporation)) were all launched before the [100% QSBS exclusion even existed](https://home.treasury.gov/system/files/131/WP-127.pdf). The tax rate has never been the binding constraint on transformative innovation. Access to talent, infrastructure, and markets has.

The deeper point is that the current system's flat preferential rate is poorly targeted. If you have $50,000 to your name and you bet $25,000 on a startup, you are taking a life-altering risk. If you have $50 million and you bet $500,000, you are "playing with house money." The tax structure should reflect the [inverse relationship of risk to wealth](https://en.wikipedia.org/wiki/Risk_aversion#Absolute_risk_aversion).

For the rising entrepreneur, this framework is *more* encouraging than the current system. The first $2.5M in gains is tax-free for everyone, with no C-corp requirements or five-year hold rules or active business tests that disqualify most founders from QSBS today. A dentist in Omaha writing a $50K angel check into a friend's startup faces 23.8% from dollar one under current law; under this framework, that gain is fully exempt. The current system of specialized carve-outs excludes exactly the investor class that should be encouraged: diverse, geographically distributed, willing to take small risks on people they know.

And here's the most important part of the innovation argument: **this framework makes "doing nothing" more expensive.** Today, the ultimate safe bet is holding a stagnant legacy asset until death to receive a 0% rate via stepped-up basis. The current system literally rewards sitting on capital. By closing those escape hatches, Rule 3 pushes capital back into productive use. That's pro-innovation policy, not anti-innovation.

---

## What About My House?

This is the question every homeowner will ask, and the answer is: you're almost certainly better off.

Under current law, the primary residence exclusion lets you sell your home tax-free up to $250K in gains ($500K married). That sounds generous, but it only covers your house. Not your stock portfolio, not your small business, not your rental property. Under this framework, the $2.5M lifetime exemption ($5M married) covers *all* of it. A couple who sells their home for a $400K gain, later sells stock for $200K, and eventually sells a small business for $800K pays $0 on all of it. The exemption is ten times larger and infinitely more flexible than the provision it replaces.

One group deserves an honest acknowledgment: homeowners in expensive coastal markets with large nominal gains on a primary residence they bought in a hot market. A couple who bought a house in Boston or San Francisco in 2005 for $800K and sells in 2026 for $2.2M has a nominal gain of $1.4M. Under Rule 4's CPI adjustment, their real gain drops to roughly $1M. That's still above the current $500K married exclusion, and it eats into their $5M lifetime exemption more than a similar homeowner in Ohio would experience. These households are rare in absolute terms (primary residences with $1M+ real gains are a small slice of American homeowners), but they are concentrated in politically vocal places. They are still better off than under current law in nearly all cases, because the lifetime exemption covers all future capital gains from any source, not just housing. But the home sale transaction itself will feel different, and that's worth naming honestly.

The more interesting question is what happens to real estate *markets*. Currently, two provisions (like-kind exchange deferrals and stepped-up basis at death) combine to create "capital paralysis" in investment real estate. Investors hold aging properties for decades, not because they're the best investment, but because selling triggers a tax bill that dying doesn't. This locks up inventory, inflates prices, and rewards inertia over efficiency. Eliminating both provisions simultaneously forces investment-grade real estate back into the market. This increased supply puts downward pressure on prices for rentals and commercial space, improving affordability.

The tax intermediary industry that exists to facilitate these deferrals (a multi-billion-dollar ecosystem of qualified intermediaries, accommodators, and specialist attorneys) will shrink. That is a feature, not a bug. The fees they collect are a deadweight cost of navigating complexity that this framework eliminates.

---

## A Meaningful Dent in the Federal Deficit

> Note: These are preliminary estimates based on IRS SOI data, standard elasticity models, and AI-assisted modeling (thanks Claude!) — this is not an official CBO score!

This framework nets an **estimated annual federal revenue increase of $85-200 billion per year.**

The net is real money. At the midpoint, it's roughly $140 billion per year, enough to meaningfully dent annual deficits that currently exceed $2 trillion. And the estimate is likely conservative: traditional capital gains elasticity estimates assume taxpayers can permanently defer or avoid gains, which this framework's expanded realization events largely prevent.

The framework loses roughly $50-65 billion per year from repealing the estate tax, AMT, and NIIT. It gains substantially more from deemed realization at death ($75-100 billion), the sliding scale on large gains, closure of buy-borrow-die ($25-50 billion), elimination of QSBS ($10-20 billion), elimination of 1031 exchanges ($10-15 billion), other preference elimination ($10-20 billion), and Roth reform ($10-23 billion).

The net position depends on the sliding scale calibration: how quickly the rate phases up and where it breaks even against current law's 23.8% rate. Under the moderate calibration I'm proposing ($2.5 million exemption, $10 million ceiling), the breakeven is around $17.5 million in cumulative lifetime gains. Below that, you pay less than current law. Above it, you pay more.

To be clear: this does not solve the deficit. There is no silver bullet that does. The federal deficit exceeds $2 trillion annually; closing that gap requires a combination of tax reform, entitlement reform, and spending discipline. Most economists agree that [stabilizing the debt-to-GDP ratio requires deficit reduction on the order of $800 billion to $1 trillion per year](https://www.americanprogress.org/article/what-would-it-take-to-stabilize-the-debt-to-gdp-ratio/). This framework gets roughly 15-20% of the way there, from a single reform to a single part of the tax code. Paired with broader income tax reform, Social Security modernization, and credible spending restraint, there is a pragmatic path to fiscal sustainability. This is one of the most important arrows in that quiver.

One important implementation detail: on the day of enactment, everyone's lifetime counter starts at $0. Pre-enactment gains are not retroactively counted. This means investors who anticipate the change will harvest gains before enactment to lock in current rates, which is fine. That pre-enactment selling generates immediate tax revenue on gains that might otherwise have been deferred via stepped-up basis indefinitely. The Treasury benefits either way: from the rush of pre-enactment realizations, or from the new framework's broader base going forward.

---

## Every Perennial Debate, Resolved

One way to test whether a reform is structural or cosmetic is to ask: how many ongoing political fights does it settle?

The billionaire tax debate (whether to tax unrealized gains annually) is resolved by expanding realization events to death, gifts, and borrowing. You don't need mark-to-market accounting. You need to close the exits. Carried interest (the provision that lets hedge fund managers pay capital gains rates on what is essentially labor income) is rendered moot without a targeted ban — when gains above the exemption are ordinary income, there is no preferential rate to exploit. The wealth tax debate is settled by offering the same outcome through constitutionally sound and more politically palatable means.

These are not separate reforms requiring separate political coalitions. They are natural consequences of five rules.

---

## Why This Hasn't Happened

If the math works and the politics are tractable, why hasn't someone done this already?

Three reasons.

First, the complexity-industrial complex. The current system supports an ecosystem of estate planners, 1031 exchange intermediaries, QSBS specialists, Opportunity Zone fund managers, and tax attorneys, collectively a multi-billion-dollar industry. Together, this industry generates billions in fees, not for producing anything, but for navigating a system that shouldn't require navigation. And every simplification is an existential threat to someone's livelihood. These constituencies are small but organized and well-funded. The people who benefit from simplification (essentially all taxpayers) are diffuse and unorganized.

Second, partisan framing. Tax reform has been captured by a false binary: raise rates (left) or cut rates (right). This framework does neither. It broadens the base, eliminates preferences, and lets the rate structure do its job. That makes it harder to explain in a sound bite, but it also means it can get a meeting with both the Senate Finance Committee chair and the ranking member, which no other progressive capital gains proposal can claim.

Third, the estate tax trap. For decades, progressive reformers have defended the estate tax as the last line of defense against dynastic wealth. Defending it has become an article of progressive faith — one that prevents progressives from considering the possibility that abolishing it, in exchange for something that actually works, is the better deal. [The Walton family transferred billions using GRATs](https://www.bloomberg.com/graphics/infographics/how-to-preserve-a-family-fortune-through-tax-tricks.html) structured to generate zero gift tax liability. The 40% rate on paper means nothing when the effective rate is 10-15%.

---

## The Coalition

**From the right:** Estate tax repeal. AMT repeal. Radical simplification. A universal exemption that rewards entrepreneurship without government picking winners.

**From the left:** Billionaires paying ordinary income rates. Buy-borrow-die closure. Stepped-up basis elimination. Real revenue for deficit reduction. The end of the Peter Thiel Roth loophole.

**From the middle:** A system you can explain to your neighbor in two sentences. A system where the first $5 million is yours and the government takes its share above that, honestly and without games.

No other capital gains proposal can get a meeting with both the Senate Finance Committee chair and the ranking member. This one can, because it gives each side wins they've wanted for a generation.

---

## The Invitation

This is a working proposal, not a finished bill. The architecture is a structural claim. The calibration (should the exemption be $2.5 million or $3 million? the ceiling $10 million or $8 million?) is deliberately open, and I am asking for input. These are consequential choices that deserve public debate and rigorous scoring, not unilateral declaration.

What I am confident about is the structural claim: that a system built on five rules can replace a system built on four thousand pages, can collect more revenue with fewer escape routes, and can do so in a way that makes 98% of American households unambiguously better off.

The tax code is America's most expensive, most consequential piece of technical debt. Every year we don't refactor it, the complexity compounds, the loopholes widen, and the distance between those who can afford to navigate the system and those who cannot gets larger. That distance is not a bug. In the current system, it is the central feature.

---

*Matt Sly is a software entrepreneur with twenty years of experience building products used by millions. The Lifetime Gains Framework and supporting analysis are available at [mattsly.com](https://www.mattsly.com). This essay is adapted from a longer policy document developed as part of the Fair and Simple Tax Project.*

*Revenue estimates, sensitivity analysis, and editorial assistance provided by Claude AI. All policy positions and framework design are the author's own.*