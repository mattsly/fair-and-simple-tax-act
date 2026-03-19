---
layout: plain
---

# America's Most Expensive Technical Debt

### A software entrepreneur's case for simple, fair and durable tax reform

*By Matt Sly*

---

I have spent twenty years building software. I've been a salaried employee, a startup employee with stock options, a big tech employee paid in RSUs, a founder with an exit, and an angel investor. I've been on every side of the capital gains equation. As both a software professional and a taxpayer, I think the American tax code (and capital gains taxation in particular) is the most consequential piece of technical debt in the United States.

The tax code is a direct cause of wealth and opportunity inequality in America, epitomized by [billionaires paying taxes at a lower rate than teachers](https://www.propublica.org/article/the-secret-irs-files-trove-of-never-before-seen-records-reveal-how-the-wealthiest-avoid-income-tax). And it can be dramatically improved with a radically simple "refactor" of capital gains taxation specified with five rules that I outline below. These five rules would eliminate roughly 10-15% of the Internal Revenue Code (including the AMT, the NIIT and even the estate tax), preclude the need for a wealth tax, close the "buy, borrow, die" loophole, cut taxes for 98% of Americans, and generate an estimated [$85-200 billion in annual deficit reduction](https://www.cbo.gov/publication/60870) — enough to get us 15-20% of the way to a sustainable federal budget from a single policy change.

## The Algorithm Nobody Designed and the Product Nobody Wants

A tax code is an algorithm. It takes inputs (your income, your assets, your transactions) and produces an output (your tax bill). A well-designed algorithm is legible, predictable, and deterministic. The federal tax code is none of these.

This complexity is a byproduct of a political system that rewards adding new provisions rather than refactoring existing ones. In most cases, each provision was a well-intended solution to a real problem. But in a complex system, "well-intended" often invites unintended consequences. Over a century, these "reasonable solutions" have compounded into a byzantine mess that nobody actually designed.

The cost of this complexity is staggering: Americans spend [6.5 billion hours and over $500 billion annually](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/) just complying with the tax code. That is 1.9% of GDP in pure deadweight loss. Not building products, not funding factories, not making anyone healthier — just navigating the system. Meanwhile, [hundreds of billions of dollars in taxes owed go uncollected every year](https://www.irs.gov/statistics/irs-the-tax-gap), enabled in large part by the very complexity that makes enforcement impossible.

Consider the estate tax: it was created to prevent dynastic wealth, but it provided the moral ‘double taxation’ cover for stepped-up basis (the idea that we shouldn’t tax gains at death if we’re already taxing the estate). That loophole, in turn, birthed ‘Buy, Borrow, Die’—the ultimate bypass where billionaires borrow against untaxed appreciation to fund their lives, then let death erase the tax bill entirely. When this drove effective rates for the ultra-wealthy into the single digits, Congress didn’t refactor the system; they just bolted on more layers.

They added the Alternative Minimum Tax (AMT) as a "shadow" tax code, and later the Net Investment Income Tax (NIIT) as a conditional surtax to scrape back revenue. In software, we call this 'spaghetti code'—a tangled mess of logic where you stop fixing the core engine and start writing 'hotfixes' just to manage the side effects of previous 'hotfixes.' The tax code is now inundated with so many brittle dependencies and edge cases that the 'product' has become a nightmare for everyone except the high-priced specialists paid to navigate it.

This is a design failure. In any other industry, the best products hide complexity from the user. Google search is one of the most sophisticated pieces of software ever built, yet you interact with it through a single text box. An iPhone requires millions of lines of code and a global supply chain, but a child can learn the interface in minutes.

The tax code does the opposite. It takes the hardest problem in government (allocating the cost of civilization) and makes the implementation details every individual taxpayer's problem to solve. We’ve confused a complex economy with a requirement for a complex interface.

---

## The Refactor: Five Rules

Here is my proposal for how to fix the capital gains tax system in five rules:

> Note - the specific numbers here are "stakes in the ground" - they are open for debate and much less important than the general framework

**Rule 1: Every American gets a *lifetime* capital gains exemption.** $2.5 million per person; $5 million for a married couple. Any source, any asset type, no qualification tests. One bucket replaces a dozen narrow exclusions.

**Rule 2: Above the exemption, the tax rate phases up to the top marginal income tax rate.** From $2.5 million to $10 million in cumulative lifetime gains, the rate increases smoothly from 0% to 37% (the current top marginal rate). Above $10 million, all gains are taxed at 37% regardless of other income. Crucially, the rate is not a fixed number — it is pegged to whatever the top marginal income tax rate happens to be. This eliminates the preferential rate that allows hedge fund managers to pay a lower percentage than teachers.

**Rule 3: You can't defer gains forever.** We close the "Buy, Borrow, Die" loophole by triggering realization at four specific events: sale, death, gift, or borrowing. Realization at death eliminates stepped-up basis — the provision that currently lets heirs inherit appreciated assets with a clean tax slate, erasing a lifetime of untaxed gains. Borrowing mechanics are informed by [research from the Yale Budget Lab](https://budgetlab.yale.edu/research/buy-borrow-die-options-reforming-tax-treatment-borrowing-against-appreciated-assets): when you pledge appreciated assets as collateral, the unrealized gain on those assets is deemed realized. Basis steps up to prevent double taxation on eventual sale. If the collateral has no unrealized gain (a purchase mortgage on a home you just bought, for example) the deemed realization is $0.

**Rule 4: Basis is fully indexed to inflation.** Your cost basis is [adjusted by CPI](https://budgetlab.yale.edu/research/indexing-capital-gains-inflation), so you are taxed on real economic gains. A house you bought for $200,000 in 1995 has a CPI-adjusted basis of roughly $400,000 in 2026. This indexing applies symmetrically to both gains and losses. By adjusting for the erosion of purchasing power, we ensure the government does not profit from phantom gains caused by inflation.

**Rule 5: Roth Reforms.**  We simplify the Roth IRA by removing the income cap for participation, raising the annual limit, but imposing a hard $5 million balance cap. This trade eliminates the [Thiel Loophole](https://www.propublica.org/article/lord-of-the-roths-how-tech-mogul-peter-thiel-turned-a-retirement-account-for-the-middle-class-into-a-5-billion-dollar-tax-free-piggy-bank) while expanding access for high-earning professionals.

That's it. Five rules. From these five rules, an extraordinary amount of existing tax infrastructure becomes unnecessary.

*For readers who want the precise mechanics — including the complete tax calculation algorithm and full list of eliminated provisions — the [technical specification](./technical_spec.md) is available alongside this essay.*

---

## What Falls Away

The five rules don't just simplify capital gains. They make entire categories of tax law redundant.

**The Alternative Minimum Tax.** The AMT is a parallel tax system [created in 1969 because 155 wealthy Americans paid zero income tax](https://taxfoundation.org/taxedu/glossary/alternative-minimum-tax-amt/). It now ensnares millions of upper-middle-class households in high-tax states, while the truly wealthy route around it through the same planning strategies they use for everything else. When there are no exclusions to exploit, the AMT's purpose evaporates.

**The Net Investment Income Tax.** A 3.8% surtax bolted onto the Affordable Care Act to fund Medicare. Under this framework, gains above the exemption are ordinary income taxed at rates far exceeding 3.8%. The NIIT becomes redundant by design.

**The estate tax.** If death is a realization event and all gains are taxed on the decedent's final return, the estate tax becomes redundant — and replaceable with something that actually collects. (See *The Estate Tax Question* below.)

**A wealth tax.** This framework precludes the need for a wealth tax by achieving the same progressivity through better means. (See *The Wealth Tax Question* below.)

**Twelve special exclusions and preferences.** QSBS (the startup stock exclusion). Section 121 (the home sale exclusion). 1031 exchanges (the real estate deferral). Opportunity Zone deferrals. The 60/40 rule for derivatives. The collectibles rate. Installment sale deferrals. GRATs and dynasty trusts. Stepped-up basis. The lifetime gift tax exemption. Carried interest. Each one replaced by the universal exemption and the five rules.

In total, these five rules eliminate roughly 10-15% of the Internal Revenue Code by volume, along with the thousands of pages of Treasury regulations, IRS guidance, and Tax Court precedent that interpret them. 

Most software engineers will tell you: deleting code *and* improving the product is the most satisfying kind of work. But simplification isn't just aesthetically pleasing. It is structurally important. Every eliminated provision is an eliminated edge case, an eliminated loophole, an eliminated compliance cost. The current system has at least twenty-five independent configuration parameters. The proposed system has two: the exemption level and the phase-out ceiling. Both are indexed to inflation. Both can be adjusted by Congress without reopening the structural framework. Fewer parameters means fewer interactions, fewer exploits, and a system that is dramatically easier to administer, audit, and explain. That is what radical simplification actually looks like.

---

## Stop Making Users Compile and Run the Code

Imagine if Google shipped you the source code for their search engine and said "compile it yourself, and if it crashes, that’s your problem." That is the U.S. tax system. 160 million Americans download the algorithm every year and run it on their own machines (sometimes with the help of high-priced consultants who charge by the hour to debug it for them). And if you get it wrong, it's your fault. Donald Rumsfeld, a man who ran the Department of Defense, [sent the IRS a letter every year](https://taxfoundation.org/blog/what-does-donald-rumsfeld-have-common-franklin-roosevelt/) saying he had "absolutely no idea" whether his tax returns were accurate, despite hiring a professional accounting firm. If a former Secretary of Defense can't figure it out, the interface is broken.

This is not an unsolvable problem. In the Netherlands, the government pre-fills your return. The algorithm has already run. You review the output and click "confirm." In Estonia, the entire process takes about five minutes. The IRS already has your W-2s, your 1099s, your mortgage interest statements. The data exists. What’s missing is a codebase simple enough to automate.

The tax-prep industry (an [$11 billion market](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/)) has lobbied for decades to keep the interface manual, because their entire business model depends on the complexity that makes self-filing painful. Five deterministic rules don’t eliminate the need for tax software. But they make the software trivial to write, trivial to audit, and trivial to run on your behalf. That is the difference between spaghetti code and a clean API.

## Who Wins, Who Loses

**A homeowner** who sells their primary residence for a $250,000 real gain (after inflation adjustment): $0 tax under current law, $0 tax under this framework. No change, except the exemption now covers all asset types, not just housing.

**A first-time founder** who builds a company over eight years and exits for $2.8 million in real gains: Under current law, if they don't qualify for QSBS (and most founders don't, because it requires a C-corp structure, a $50 million gross asset test, a five-year hold, and an active business test), they pay roughly $555,000. Under this framework: approximately $2,200. The exemption covers almost the entire gain.

**A tech employee** who accumulates $1.2 million in gains from RSU vesting and stock sales over a 15-year career at two companies: Under current law, about $285,000 in capital gains tax. Under this framework: $0. The entire amount falls within the lifetime exemption. No special elections, no holding-period optimization, no tax-lot accounting games.

**A successful founder with a $19 million exit:** Under current law, about $4.5 million in tax. Under this framework, about $4.7 million. Roughly breakeven, within $200,000. The founder also never needs to check for AMT, calculate NIIT, or attempt QSBS qualification.

**A mega-exit founder with $95 million in gains:** Under current law, about $22.6 million. Under this framework, about $32.8 million. This founder pays more, about $10 million more. At this scale, the sliding scale has fully phased to ordinary income rates, and the current system's 23.8% flat rate becomes visibly inadequate.

**An inherited estate with $15 million in unrealized gains:** Under current law, $0. Stepped-up basis wipes the slate clean. Under this framework, about $3.2 million, collected on wealth that currently escapes taxation entirely.

**A billionaire borrowing $5 million per year against appreciated stock:** Under current law, $0. This is buy-borrow-die. Under this framework, $1.85 million per year.

**A dynasty estate with $500 million, $400 million in unrealized gains:** Under current law, with competent estate planning, the family pays roughly $30-50 million. Under this framework, approximately $148 million. The framework collects three to five times what the current system actually collects. This is where the revenue argument lives: in the chasm between what the estate tax theoretically collects and what it actually collects after planning.

The pattern is clear. The framework is designed to fuel the climb: the homeowner, the first-time founder, the tech employee building a career, the saver building a retirement portfolio — all pay the same or less. Tax increases are concentrated exactly where they should be: on very large accumulations, inherited estates exploiting stepped-up basis, and the borrow-against-assets strategy that allows billionaires to live tax-free. The current system structurally advantages those who've already arrived. This one clears the path for those still building.

---

*What follows is a deeper dive into the most common questions and objections. If you're already sold on the architecture, skip to [The Coalition](#the-coalition). If you want to stress-test the idea, read on, but fair warning that it will get a little wonky.*

---

## The Estate Tax Question

Abolishing the estate tax sounds like a conservative fever dream. But the estate tax is a policy that looks progressive on paper and fails in practice. It theoretically imposes a 40% rate above a large threshold. In reality, well-advised estates routinely pay 10-15% or less — and the wealthiest pay the least, because they can afford the planners who make it disappear. As Professor Ray Madoff documents in [*The Second Estate*](https://press.uchicago.edu/ucp/books/book/chicago/S/bo256019296.html), the estate tax has become political cover: it *looks* like a tax on dynastic wealth, while its hollowed-out structure ensures the wealthiest families pay the least.

This framework replaces it with a mechanism that actually collects. Death as a realization event is not a radical experiment. It has been the [functional model in Canada since 1972](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/report-income/capital-gains.html), where it successfully replaced their version of the estate tax.

When death is a realization event and all gains are taxed on the decedent's final return, there is no stepped-up basis, no GRAT loophole, no valuation discount game. Even the incentive to lowball gift valuations is structurally defanged: because there is no stepped-up basis, an undervalued gift simply shifts a lower basis to the recipient, who pays a correspondingly larger tax bill later. The total tax collected is roughly the same — the donor and recipient are no longer on the same team. Dynasty trusts lose their power too: trust-held assets are deemed realized at each generational transfer, so wealth can no longer skip across generations untaxed. A $100 million estate with $80 million in unrealized gains pays approximately $29 million — automatically, with no planning tricks available. A $500 million dynasty estate pays roughly $148 million, compared to the $30-50 million the current estate tax actually collects after planning.

Critics will inevitably point to the liquidity challenge: if death is a realization event, how do heirs pay the tax on an illiquid family business or farm without being forced to sell it? The solution is straightforward: a 15-year IRS lien option, conceptually similar to existing estate tax installment plans. The IRS places a lien on the asset; the heir pays the tax over fifteen years out of operating cash flow. No fire sale required. And if a family business genuinely cannot service its tax obligation over fifteen years, that is a valuation signal, not a liquidity crisis.

The trade is simple: abolish a tax that collects [$20-25 billion per year](https://taxpolicycenter.org/briefing-book/how-many-people-pay-estate-tax) badly, and replace it with a mechanism that collects two to six times more from the estates that matter most. Progressives get more revenue and no escape routes. Conservatives get the estate tax repeal they've wanted for a generation.

---

## The Wealth Tax Question

A wealth tax polls well. It feels fair: if you have a billion dollars, pay a percentage every year. But [every European country that tried one repealed it](https://taxfoundation.org/research/all/eu/wealth-tax-impact/). France's wealth tax drove an estimated 42,000 millionaires out of the country before it was repealed in 2017. Sweden and Austria reached the same conclusion. The problems are structural: annual valuation of illiquid assets (private businesses, real estate, art) is expensive, subjective, and gameable. And a wealth tax is yet another layer bolted onto an already brittle system — the same pattern that gave us the AMT and the NIIT. More tax types means more interactions, more edge cases, and more loopholes. Enforcement costs eat the revenue. And capital flight is real — wealthy individuals move to jurisdictions that don't impose the tax, shrinking the base faster than the tax can collect from it.

This framework achieves what a wealth tax promises without these failures. By expanding realization events (sales, death, gifts, borrowing) and taxing gains as ordinary income, it captures wealth accumulation at the moments when assets are easiest to value — transaction prices, not annual appraisals — and hardest to hide — documented transactions with third-party reporting. It uses existing IRS infrastructure rather than requiring a new valuation bureaucracy. The result is the same progressivity that wealth tax advocates want, delivered through mechanisms that actually work.

---

## Why Not Just Tax All Gains as Income?

This is the first objection from the left, and it deserves a direct answer. If the goal is to treat investment income like wages, why bother with an exemption and a sliding scale? Why not just eliminate the preferential rate and be done with it?

First, we have the **bunching problem**: Imagine a founder who builds a company over ten years. For a decade, they may take a below-market salary—or $0—while pouring their labor into equity. When they finally exit for $2.8 million, taxing that as "income" in a single year is a mathematical penalty. It treats them as if they earned $2.8 million every year, pushing them into the highest possible tax bracket instantly.

Investments, with both time and money, also involve **failure risk**. Many founders work for years only to see their equity go to zero. The exemption is a structural buffer that accounts for the fact that capital gains are often the lumpy, high-risk harvest of a decade of work.

But the most salient reason to protect the "climb" is that entrepreneurial risk is a public good. We want to facilitate risk-taking because that is how the economy grows, how new products are built, and how jobs are created. When someone bets their career or their savings on a new idea, the successful outcome benefits everyone, not just the investor. A tax code that punishes that risk from dollar one is a tax code that inadvertently subsidizes stagnation.

We want every American to build wealth, but the current system only provides meaningful tax breaks to those who are already wealthy and can navigate complex entity structures like QSBS or own homes. By creating a $2.5 million universal exemption, we provide a powerful, simple incentive for *every* citizen to invest and save.

To be clear: above $10 million, gains *are* taxed as ordinary income under this framework. The disagreement isn't about whether gains should be treated as income. It's about where the exemption sits and how fast the rate phases in — and those are exactly the two parameters ($2.5M exemption, $10M ceiling) that this framework makes easy to debate and adjust.

---

## Won't Higher Rates Kill Innovation?

Critics may argue that raising the top capital gains rate to 37% and ending the QSBS exclusion ([Section 1202](https://www.law.cornell.edu/uscode/text/26/1202)) will stifle startups and scare away angel investors. History says otherwise: Google (IPO [2004](https://www.britannica.com/money/Google-Inc)), the iPhone (launched 2007), and NVIDIA (founded [1993](https://www.britannica.com/money/NVIDIA-Corporation)) were all launched before the [100% QSBS exclusion even existed](https://home.treasury.gov/system/files/131/WP-127.pdf). The tax rate has never been the binding constraint on transformative innovation — access to talent, infrastructure, and markets has.

The deeper point is that the current system's flat preferential rate is poorly targeted. If you have $50,000 to your name and you bet $25,000 on a startup, you are taking a life-altering risk. If you have $50 million and you bet $500,000, you are "playing with house money." The tax structure should reflect the [inverse relationship of risk to wealth](https://en.wikipedia.org/wiki/Risk_aversion#Absolute_risk_aversion).
 
For the rising entrepreneur, this framework is *more* encouraging than the current system. The first $2.5M in gains is tax-free for everyone, with no "C-Corp" or "five-year hold" traps that disqualify most founders from QSBS today. A dentist in Omaha writing a $50K angel check into a friend's startup faces 23.8% from dollar one under current law; under this framework, that gain is fully exempt. By democratizing the tax incentive we attract more investors from more backgrounds, producing a more diverse and market-driven capital allocation than today's system of specialized carve-outs.

Finally, this framework makes "doing nothing" more expensive. Today, the ultimate safe bet is holding a stagnant legacy asset until death to receive a 0% rate via stepped-up basis. By closing the escape hatches (Rule 3), we encourage putting investment capital to work.

---

## What About My House?

This is the question every homeowner will ask, and the answer is: you're almost certainly better off.

Under current law, the primary residence exclusion lets you sell your home tax-free up to $250K in gains ($500K married). That sounds generous, but it only covers your house — not your stock portfolio, not your small business, not your rental property. Under this framework, the $2.5M lifetime exemption ($5M married) covers *all* of it. A couple who sells their home for a $400K gain, later sells stock for $200K, and eventually sells a small business for $800K pays $0 on all of it. The exemption is ten times larger and infinitely more flexible than the provision it replaces.

The more interesting question is what happens to real estate *markets*. Currently, two provisions — like-kind exchange deferrals and stepped-up basis at death — combine to create "capital paralysis" in investment real estate. Investors hold aging properties for decades, not because they're the best investment, but because selling triggers a tax bill that dying doesn't. This locks up inventory, inflates prices, and rewards inertia over efficiency. Eliminating both provisions simultaneously forces investment-grade real estate back into the market. This increased supply puts downward pressure on prices for rentals and commercial space, improving affordability. Lobbyists will call it a crash. Renters will call it a correction.

The tax intermediary industry that exists to facilitate these deferrals — a multi-billion-dollar ecosystem of qualified intermediaries, accommodators, and specialist attorneys — will shrink. That is a feature, not a bug. The fees they collect are a deadweight cost of navigating complexity that this framework eliminates.

---

## A Meaningful Dent in the Federal Deficit

> Note: These are preliminary estimates based on IRS SOI data, standard elasticity models, and AI-assisted modeling — not an official CBO score

This framework nets an **estimated annual federal revenue increase of $85-203 billion per year.**

The net is real money. At the midpoint, it's roughly $140 billion per year, enough to meaningfully dent annual deficits that currently exceed $2 trillion. And the estimate is likely conservative: traditional capital gains elasticity estimates assume taxpayers can permanently defer or avoid gains, which this framework's expanded realization events largely prevent.

The framework loses roughly $50-65 billion per year from repealing the estate tax, AMT, and NIIT. It gains substantially more from deemed realization at death ($75-100 billion), the sliding scale on large gains, closure of buy-borrow-die ($25-50 billion), elimination of QSBS ($10-20 billion), elimination of 1031 exchanges ($10-15 billion), other preference elimination ($10-20 billion), and Roth reform ($10-23 billion).

The net position depends on the sliding scale calibration: how quickly the rate phases up and where it breaks even against current law's 23.8% rate. Under the moderate calibration I'm proposing ($2.5 million exemption, $10 million ceiling), the breakeven is around $17.5 million in cumulative lifetime gains. Below that, you pay less than current law. Above it, you pay more.

To be clear: this does not solve the deficit. There is no silver bullet that does. The federal deficit exceeds $2 trillion annually; closing that gap requires a combination of tax reform, entitlement reform, and spending discipline. Most economists agree that [stabilizing the debt-to-GDP ratio requires deficit reduction on the order of $800 billion to $1 trillion per year](https://www.americanprogress.org/article/what-would-it-take-to-stabilize-the-debt-to-gdp-ratio/). This framework gets roughly 15-20% of the way there, from a single reform to a single part of the tax code. Paired with broader income tax reform, Social Security modernization, and credible spending restraint, there is a pragmatic path to fiscal sustainability. This is one of the most important arrows in that quiver.

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