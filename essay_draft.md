# America's Most Expensive Technical Debt

### A software entrepreneur's case for simple, fair and durable tax reform

*By Matt Sly*

---

I have spent twenty years in the software industry working in a variety of environments. I've been a W-2 employee, a startup employee with stock options, a founder with an exit, and an investor writing checks to the next generation of builders. I have filed taxes in every one of these capacities, and I can tell you with confidence: the American capital gains tax system is the most consequential piece of technical debt in the United States.

It is a direct cause of wealth and opportunity inequality in America, epitomized by [billionaires paying taxes at a lower rate than teachers](https://www.propublica.org/article/the-secret-irs-files-trove-of-never-before-seen-records-reveal-how-the-wealthiest-avoid-income-tax). But I believe it can be fixed with a radical but simple "refactor" that can be specified with five rules. Those five rules would eliminate more tax law than any reform in American history and preclude the need for a wealth tax.

## The Algorithm Nobody Wrote

A tax code is an algorithm. It takes inputs (your income, your assets, your transactions) and produces an output (your tax bill). A well-designed algorithm is legible, predictable, and produces the same result regardless of who runs it. The federal capital gains system fails every one of these tests.

This complexity is not a conspiracy. It is an accidental byproduct of a political system that rewards adding new provisions rather than shoring up existing ones. In most cases, each provision was a reasonable solution to a real problem. But reasonable solutions to problems caused by previous reasonable solutions, compounded over a century, have produced a byzantine mess that nobody designed.

Consider that the estate tax was created to prevent dynastic wealth concentration. But it justified stepped-up basis (why tax gains at death if you're already taxing the estate?). Stepped-up basis created buy-borrow-die (why sell if you can borrow against your assets and let death erase the gains?). Buy-borrow-die meant billionaires could pay effective federal tax rates in the single digits, which created political pressure for the Net Investment Income Tax, bolted onto the Affordable Care Act as a 3.8% surtax. The NIIT didn't fix the underlying problem, so we got Opportunity Zones, which were supposed to direct capital to underserved communities but mostly subsidized luxury apartments in already-gentrifying neighborhoods. And on and on. A patient on seventeen medications, where half exist to manage the side effects of the other half.

Each layer has a constituency. Estate planning attorneys. 1031 exchange intermediaries. Opportunity Zone fund managers. QSBS specialists. Together, this industry generates billions in fees, not for producing anything, but for navigating a system that shouldn't require navigation. When a system accumulates this much technical debt, you don't keep patching. You refactor.

---

## The Refactor: Five Rules

The best products hide complexity from the user. Google's search index is one of the most sophisticated pieces of software ever built; you interact with it through a single text box. Apple's iPhone requires millions of lines of code and requires a complex global supply chain, but you can learn how to use the product in 3 minutes. The tax code does the opposite. Yes, the underlying economy is complicated. But the interface (the part citizens and small business owners actually touch) should be simple. The current system takes the hardest problem in government (allocating the cost of civilization fairly) and makes it every individual taxpayer's problem to solve. That's a design failure.

Here is the entire capital gains tax system (or "User Interface") that I'm proposing, in five rules:

> Note - the specific numbers here are stakes in the ground - they are much less important than the general framework and open for debate

**Rule 1: Every American gets a $2.5 million lifetime capital gains exemption.** That's $5 million for a married couple. Your first $2.5 million in investment gains, from any source, over your entire lifetime, is tax-free. Home sales, stock sales, business exits, everything. No forms, no qualification tests, no entity-type restrictions. The government stops telling you which types of investments are virtuous.

**Rule 2: Above the exemption, the tax rate phases up on a sliding scale to the top marginal income tax rate.** From $2.5 million to $10 million in cumulative lifetime gains, the rate increases smoothly from 0% to 37% (the current top marginal rate). Above $10 million, all gains are taxed at 37% regardless of other income. This eliminates the preferential rate that allows hedge fund managers to pay a lower percentage than teachers.

**Rule 3: You can't defer gains forever.** Three events trigger realization: selling, dying, and borrowing against appreciated assets. Death as a realization event follows the Canadian model, in use since 1972 (the sky has not fallen). Gifts also trigger realization. Borrowing closes the "buy, borrow, die" strategy that lets the ultra-wealthy live on loans backed by untaxed appreciation indefinitely.

**Rule 4: Basis is indexed to inflation (for gains only).** Your cost basis is adjusted by CPI, so you're taxed on real gains, not phantom gains from purchasing power erosion. A house you bought for $200,000 in 1995 has a CPI-adjusted basis of roughly $400,000 in 2026. You're taxed on the real wealth you accumulated, not on the fact that the dollar lost value. One asymmetry by design: CPI adjustment applies only to gains. Losses are measured against original purchase price. This prevents inflation indexing from amplifying tax-loss harvesting strategies, where investors sell losing positions to generate inflated deductions. Losses reflect actual dollars lost; gains reflect actual purchasing power gained.

**Rule 5: Roth Reforms.**  Roth IRAs were designed as modest retirement vehicles: you pay tax on the way in, and withdrawals are tax-free. But unlimited "backdoor" conversions have made the Roth an unlimited, unrestricted tax shelter (the most famous example: Peter Thiel grew a Roth to $5 billion, all tax-free.) This framework puts a hard limit on annual contributions (preventing backdoors), but also removes the income cap, making Roths more useful to higher income taxpayers who previously had an incentive to utilize the backdoor strategy. It imposes a $5 million balance cap: once your combined Roth balance hits $5M, new contributions are frozen.

That's it. Five rules. From these five rules, an extraordinary amount of existing tax infrastructure becomes unnecessary.

*For readers who want the precise mechanics — including the complete tax calculation algorithm and full list of eliminated provisions — the [technical specification](./technical_spec.md) is available alongside this essay.*

---

## What Falls Away

This is the part that surprises people. The five rules don't just simplify capital gains. They make entire categories of tax law redundant.

**The estate tax.** If death is a realization event and all gains are taxed on the decedent's final return, why do we need a separate estate tax? The estate tax currently collects about $20-25 billion per year, a fraction of what it should, because the wealthy use GRATs, dynasty trusts, and valuation discounts to reduce their effective rates to 10-15%. Under this framework, a $100 million estate with $80 million in unrealized gains pays approximately $29 million. No planning tricks. No escape routes. The estate tax is replaced by something that actually works.

Eliminating the estate tax is not a concession to conservatives. It is a trade. For thirty years, estate tax repeal has been the Republican donor class's top legislative priority. This framework delivers it, in exchange for a system that collects two to six times more from the estates that matter most. That trade is the political engine that makes this proposal viable across party lines.

**The Alternative Minimum Tax.** The AMT is a parallel tax system created in 1969 because 155 wealthy Americans paid zero income tax. It now ensnares millions of upper-middle-class households in high-tax states, the very people it was never meant to touch, while the truly wealthy route around it through the same planning strategies they use for everything else. When there are no exclusions to exploit, the AMT's purpose evaporates.

**The Net Investment Income Tax.** A 3.8% surtax bolted onto the Affordable Care Act to fund Medicare. Under this framework, gains above the exemption are ordinary income taxed at rates far exceeding 3.8%. Medicare revenue doesn't decrease. It increases. The NIIT becomes redundant by design.

**A Wealth Tax** We don't currenty have a wealth tax, but it has been frequently floated as a solution to inequality, that, in my opinion, is a poor solution to a valid problem. This framework precludes the need for a wealth tax as it achieves the same progressivity through realization events (sales, death, gifts, borrowing), which are easier to value (transaction prices, not annual appraisals), harder to evade (documented transactions with third-party reporting), and more enforceable (uses existing IRS infrastructure). By expanding realization events and taxing gains as ordinary income, the base captures wealth accumulation that a rate-based-only approach never reaches.

**Twelve special exclusions and preferences.** QSBS (the startup stock exclusion). Section 121 (the home sale exclusion). 1031 exchanges (the real estate deferral). Opportunity Zone deferrals. The 60/40 rule for derivatives. The collectibles rate. Installment sale deferrals. GRATs and dynasty trusts. Stepped-up basis. The lifetime gift tax exemption. Carried interest. Each one replaced by the universal exemption and the four rules.

The current system has at least twenty-five independent configuration parameters that interact in ways no single expert fully understands. The proposed system has two: the exemption level and the phase-out ceiling. Both are indexed to inflation. Both can be adjusted by Congress without reopening the structural framework. That is what radical simplification actually looks like.


---

## Why Not Just Tax All Gains as Income?

This is the first objection from the left, and it deserves a direct answer. If the goal is to treat investment income like wages, why bother with an exemption and a sliding scale? Why not just eliminate the preferential rate and be done with it?

The core problem is lock-in. At full income tax rates from dollar one, the incentive to never sell becomes overwhelming. Capital gets trapped in yesterday's investments instead of flowing to tomorrow's. Add the bunching problem (a founder who builds a company over ten years realizes a decade of gains in a single tax year, facing a marginal rate designed for people earning that amount *every* year) and you've created a system that punishes exactly the kind of long-term entrepreneurial risk-taking you want to encourage. The exemption eliminates lock-in for 98%+ of households entirely, and the sliding scale handles bunching structurally.

There's also the capital flight problem. France, Sweden, and Austria all repealed their wealth taxes after discovering that aggressive taxation of capital drove high-net-worth individuals and their assets to friendlier jurisdictions. Full equalization from dollar one creates the same pressure. The exemption and sliding scale keep rates competitive for the vast majority of investors while ensuring that very large accumulations pay their share.

The honest rebuttal to the left: gains above $10 million *are* taxed as ordinary income under this framework. The disagreement isn't about whether gains should be income. It's about whether the transition should be gradual or abrupt, and what happens to capital mobility if it's abrupt.

---

## The 1031 Question and Housing Prices

The real estate lobby will tell you that eliminating 1031 exchanges will crash the property market. The opposite case is at least as strong.

1031 exchanges, combined with stepped-up basis at death, create a structural incentive to hold real estate forever. An investor who bought an apartment building in 1985 has no tax reason to sell, ever. They can 1031 into another property, defer the gain, and let stepped-up basis erase it at death. This isn't capital efficiency. It's capital paralysis. Properties that should trade, get renovated, or change use instead sit in aging portfolios managed for tax optimization rather than productivity.

Eliminating 1031 and stepped-up basis simultaneously increases the supply of investment-grade real estate entering the market. More supply, at the margin, means lower prices, particularly for commercial properties, multi-family housing, and rental units. The effect on single-family homes is modest (most homeowners' gains fall within the $5M married exemption), but for the rental and commercial markets that most affect housing affordability, the directional impact is clear: more transactions, more efficient allocation, and downward pressure on prices.

The JCT estimates the 1031 tax expenditure at roughly $4-10 billion per year. The U.S. real estate market involves trillions in annual transactions. The idea that a tax provision worth single-digit billions would crash a multi-trillion dollar market is not supported by evidence. What it *would* crash is the 1031 exchange industry: qualified intermediaries, specialist attorneys, and dedicated software that exist solely because of this provision. That's not market liquidity. That's an artificial ecosystem built on a tax distortion.

---

## The QSBS Question and Startups

The venture capital community will argue that eliminating QSBS (Section 1202, the qualified small business stock exclusion) will destroy American startup formation. The history doesn't support this. QSBS existed at 50% exclusion from 1993 to 2009, rose to 75%, and only reached 100% exclusion in September 2010. Google went public in 2004. Apple's iPhone launched in 2007. NVIDIA was founded in 1993. The American startup ecosystem was built before QSBS reached its current form. Meanwhile, Israel has the highest startup density in the world with no equivalent provision, and the UK uses targeted EIS/SEIS programs that are narrower and more time-limited. Under this framework, a founder's first $2.5 million in gains ($5M married) is still tax-free, covering the vast majority of startup exits. The founders who lose are the ones with $50 million exits, and they can afford the tax bill.

---

## A Meaningful Dent in the Federal Deficit

> Note: This is an unofficial estimate, generated by Claude, not an official CBO score

This framework nets an **estimated annual federal revenue increase of $85-203 billion per year.**

The net is real money. At the midpoint, it's roughly $140 billion per year, enough to meaningfully dent annual deficits that currently exceed $2 trillion. And the estimate is likely conservative: traditional capital gains elasticity estimates assume taxpayers can permanently defer or avoid gains, which this framework's expanded realization events largely prevent.

The framework loses roughly $50-65 billion per year from repealing the estate tax, AMT, and NIIT. It gains substantially more from deemed realization at death ($75-100 billion), the sliding scale on large gains, closure of buy-borrow-die ($25-50 billion), elimination of QSBS ($10-20 billion), elimination of 1031 exchanges ($10-15 billion), other preference elimination ($10-20 billion), and Roth reform ($10-23 billion).

The net position depends on the sliding scale calibration: how quickly the rate phases up and where it breaks even against current law's 23.8% rate. Under the moderate calibration I'm proposing ($2.5 million exemption, $10 million ceiling), the breakeven is around $17.5 million in cumulative lifetime gains. Below that, you pay less than current law. Above it, you pay more. 

---

## Who Wins, Who Loses

**A homeowner** who sells their primary residence for a $250,000 real gain (after inflation adjustment): $0 tax under current law, $0 tax under this framework. No change, except the exemption now covers all asset types, not just housing.

**A first-time founder** who builds a company over eight years and exits for $2.8 million in real gains: Under current law, if they don't qualify for QSBS (and most founders don't, because it requires a C-corp structure, a $50 million gross asset test, a five-year hold, and an active business test), they pay roughly $555,000. Under this framework: approximately $2,200. The exemption covers almost the entire gain.

**A successful founder with a $19 million exit:** Under current law, about $4.5 million in tax. Under this framework, about $4.7 million. Roughly breakeven, within $200,000. The founder also never needs to check for AMT, calculate NIIT, or attempt QSBS qualification.

**A mega-exit founder with $95 million in gains:** Under current law, about $22.6 million. Under this framework, about $32.8 million. This founder pays more, about $10 million more. At this scale, the sliding scale has fully phased to ordinary income rates, and the current system's 23.8% flat rate becomes visibly inadequate.

**An inherited estate with $15 million in unrealized gains:** Under current law, $0. Stepped-up basis wipes the slate clean. Under this framework, about $3.2 million, collected on wealth that currently escapes taxation entirely.

**A billionaire borrowing $5 million per year against appreciated stock:** Under current law, $0. This is buy-borrow-die. Under this framework, $1.85 million per year.

**A dynasty estate with $500 million, $400 million in unrealized gains:** Under current law, with competent estate planning, the family pays roughly $30-50 million. Under this framework, approximately $148 million. The framework collects three to five times what the current system actually collects. This is where the revenue argument lives: in the chasm between what the estate tax theoretically collects and what it actually collects after planning.

The pattern is clear. The bottom 98% of American households pay the same or less. Tax increases are concentrated exactly where they should be: on very large accumulations, inherited estates exploiting stepped-up basis, and the borrow-against-assets strategy that allows billionaires to live tax-free.

---

## Every Perennial Debate, Resolved

One way to test whether a reform is structural or cosmetic is to ask: how many ongoing political fights does it settle?

The billionaire tax debate (whether to tax unrealized gains annually) is resolved by expanding realization events to death, gifts, and borrowing. You don't need mark-to-market accounting. You need to close the exits. Carried interest (the provision that lets hedge fund managers pay capital gains rates on what is essentially labor income) is rendered moot without a targeted ban — when gains above the exemption are ordinary income, there is no preferential rate to exploit. The wealth tax debate is settled by offering the same outcome through constitutionally sound means; France, Sweden, and Austria all repealed their wealth taxes after discovering that capital flight and enforcement costs made them counterproductive.

These are not separate reforms requiring separate political coalitions. They are natural consequences of five rules.

---

## The Risk Premium Argument

There is an economic theory behind this design. Economists call it "decreasing absolute risk aversion": the risk premium on investment shrinks as wealth increases. If you have $50,000 to your name and you bet $25,000 on a startup, you are taking a life-altering risk. If you have $50 million and you bet $500,000, you are taking a rounding error. The current tax code ignores this entirely. It charges the same preferential rate (23.8%) whether a gain represents a first-time founder's entire net worth or a billionaire's Tuesday. The lifetime exemption corrects this: the tax benefit is concentrated where the risk is highest and the social return on that risk is greatest. At the top, where a portfolio rebalancing is about as risky as choosing which yacht to refuel, the rate converges to ordinary income.

---

## Why This Hasn't Happened

If the math works and the politics are tractable, why hasn't someone done this already?

Three reasons.

First, the complexity-industrial complex. The current system supports an ecosystem of estate planners, 1031 exchange intermediaries, QSBS specialists, Opportunity Zone fund managers, and tax attorneys, collectively a multi-billion-dollar industry. Every simplification is an existential threat to someone's livelihood. These constituencies are small but organized and well-funded. The people who benefit from simplification (essentially all taxpayers) are diffuse and unorganized.

Second, partisan framing. Tax reform has been captured by a false binary: raise rates (left) or cut rates (right). This framework does neither. It broadens the base, eliminates preferences, and lets the rate structure do its job. That makes it harder to explain in a sound bite, but it also means it can get a meeting with both the Senate Finance Committee chair and the ranking member, which no other progressive capital gains proposal can claim.

Third, the estate tax trap. For decades, progressive reformers have defended the estate tax as the last line of defense against dynastic wealth. And in theory, it is. In practice, it is a line of defense made of wet cardboard. The estate tax theoretically imposes a 40% rate. In practice, well-advised estates pay 10-15% or less. The Walton family transferred billions using a GRAT that generated $1.54 in gift tax. Defending the estate tax has become an article of progressive faith that prevents progressives from considering the possibility that abolishing it, in exchange for something that actually works, is the better deal.

Professor Ray Madoff at Boston College School of Law made this argument rigorously in her 2025 book *The Second Estate*: the estate tax functions as political cover. Its existence justifies excluding inheritances from income tax, while its hollowed-out structure ensures the wealthy pay neither. Tearing down the cover and replacing both with deemed realization at death collects more, with no escape routes.

---

## The Coalition

**From the right:** Estate tax repeal. AMT repeal. Radical simplification. A universal exemption that rewards entrepreneurship without government picking winners.

**From the left:** Billionaires paying ordinary income rates. Buy-borrow-die closure. Stepped-up basis elimination. Real revenue for deficit reduction. The end of the Peter Thiel Roth loophole.

**From the middle:** A system you can explain to your neighbor in two sentences. A system where the first $5 million is yours and the government takes its share above that, honestly and without games.

No other capital gains proposal can get a meeting with both the Senate Finance Committee chair and the ranking member. This one can, because it gives each side wins they've wanted for a generation.

---

## The Invitation

This is a working proposal, not a finished bill. The architecture is a structural claim. The calibration (should the exemption be $2.5 million or $3 million? the ceiling $10 million or $25 million?) is deliberately open, and I am asking for input. These are consequential choices that deserve public debate and rigorous scoring, not unilateral declaration.

What I am confident about is the structural claim: that a system built on five rules can replace a system built on four thousand pages, can collect more revenue with fewer escape routes, and can do so in a way that makes 98% of American households unambiguously better off.

The tax code is America's most expensive, most consequential piece of technical debt. Every year we don't refactor it, the complexity compounds, the loopholes widen, and the distance between those who can afford to navigate the system and those who cannot gets larger. That distance is not a bug. In the current system, it is the central feature.

---

*Matt Sly is a software entrepreneur with twenty years of experience building products used by millions. The Lifetime Gains Framework and supporting analysis are available at [mattsly.com]. This essay is adapted from a longer policy document developed as part of the Fair and Simple Tax Project.*
