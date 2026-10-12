---
layout: plain
title: Introducing "The Tax Refactor"
description: A software entrepreneur's case for simple, fair, and durable tax reform of America's "Most Expensive Technical Debt."
image: /assets/lifetime-gains-framework.png
twitter:
  card: summary_large_image
redirect_from:
  - /matt-sly-introducing-the-tax-refactor.html
  - /matt-sly-introducing-the-tax-refactor/
substack_slug: introducing-the-tax-refactor
substack_synced: 2026-07-16
---

# Introducing "The Tax Refactor"

**The U.S. tax code is an algorithm. And it is badly broken.**

I have spent twenty years building software. A guiding principle of elegant software design is to resist complexity. Keep the codebase simple, to enable maintainability, reduce regression risk, and mitigate security vulnerabilities. Keep the user interface simple, so customers can learn on their own and reduce training and support costs.

A tax *code* is a form of technology - basically a collection of algorithms. And yet, how is it that the far more sophisticated capabilities of other technologies in our life (iPhone, Google, AI etc) are so easy to use but understanding and completing one's taxes - what could and should be way simpler - is so hard? Some of us spend hours wading back and forth between screens in TurboTax: uploading PDFs, typing in numbers from a stack of papers on your desk...and watching your total flip from red (owed!) to green (refund!) like a slot machine. Some of us just pay someone a lot of money to...basically do an esoteric form of data entry. And after all that, we still aren't sure if it's right.

What a terrible "customer" experience, attached to what, for most of us, is the single largest expense of our lives and the most important "product" that we use: our citizenship. Americans spend [6.5 billion hours and over $500 billion annually](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/) just complying with the tax code, or 1.9% of GDP in pure deadweight loss. Not building products, not funding factories, not making anyone healthier. Just navigating the system. If I were in charge of a software product with metrics like that, let's just say I would not be looking forward to my next performance review.

I've surprised myself this past year with just how fascinated I've become with tax policy. That is not a typo! Our tax system *should* encode our fundamental values as a society into a clean specification and ultimately a simple user interface. This kind of thinking echoes what I've done my whole career building products: starting by asking 'what problems are we solving?' followed by 'what system most efficiently solves them?' And I can't think of a more important 'product' problem to focus on right now.

And, at the risk of a wee bit of hyperbole: the U.S. tax code is the most consequential piece of 'technical debt' in the country.

**The Tax Refactor** is a proposal to overhaul our tax code, built upon four key tenets: simplicity, fiscal durability, economic mobility and innovation (all detailed below). The approach I outline is radical in its means, but pragmatic in its result. There are aspects of what I propose that the political right and left will each like (and not like). I've gotten promising early feedback from policy researchers and several politicians.

## **Why is a Software Guy Writing about Taxes?**

I don't have the usual bonafides to propose detailed tax policies. I'm not an economist, a tax lawyer, a CPA, or a politician. But at this point in my life, I've paid taxes from many different angles: low-paid W-2 teacher, high-paid W-2 software executive, independent consultant, startup employee with options, large tech company employee with options, angel investor, founder with an exit, single filer, married-filing-jointly with dependents...I have seen the good, the bad, the ugly...and the uglier.

And I have shipped high impact software for almost twenty years: software used by tens of millions and generating something around a billion dollars of enterprise value. Eesh that sentence is treading dangerously close to doucheyness (I'm sorry). It's the last one like that, I promise. And to be clear, the last thing I want to do is "Tech-Splain" how to do government. But I do contend that there are principles of good software design and product management that can be applied to tax policy. Experienced product thinkers (like me!) should be in the room when we're designing 21st-century tax infrastructure. Shipping quality software involves the discipline to ask "what's the *simplest* system that does the job?" and to ruthlessly cut everything else. The tax code should be subjected to that discipline.

## **Why Now**

Three converging dynamics make the current approach to federal taxation unsustainable.

**A dire fiscal trajectory.** Servicing the national debt [now exceeds the federal defense budget](https://www.cbo.gov/publication/61172) and is the fastest-growing major category of federal spending. It consumes roughly 18 cents of every dollar of federal tax revenue, up from about 8 cents a decade ago. The annual deficit is roughly 6% of GDP, well above the [3% threshold commonly cited as a target](https://www.crfb.org/papers/case-3-gdp-deficit-target). Meanwhile, [hundreds of billions in taxes owed go uncollected every year](https://www.irs.gov/statistics/irs-the-tax-gap), enabled in large part by the very complexity that makes enforcement impossible. If the trajectory doesn't change, we eventually hit what economists call a debt death spiral: a country borrowing to pay interest on what it already owes, with each rollover demanding higher rates and weaker demand. (For the range of calamitous scenarios, see [CBO's long-term budget projections](https://www.cbo.gov/publication/62044).)

**An economic mobility problem.** [Only 50% of Americans born in 1984 earn more than their parents did at the same age, down from 92% for those born in 1940](https://opportunityinsights.org/paper/the-fading-american-dream/). The tax code isn't the sole cause of this slide (technology, globalization, education gaps all matter), but it's a major engine that perpetuates it: stepped-up basis, a feckless estate tax, infinitely preferential capital gains rates, to name a few.

**The AI transition.** Over the next decade, AI will drive structural economic shifts at a pace the tax code was not built to handle. AI is already doing work once reserved for stable, well-paid professionals, and the pace of layoffs, skill shifts, and retraining may well outrun the policy that exists for the labor market we used to have. Worse: AI's owners are overwhelmingly already-wealthy, so the productivity gains risk pooling exactly where concentration is worst. The system needs the dexterity to respond to those shifts and harness AI's productivity without further exacerbating the previous two challenges.

One more conjecture, more speculative than the others: the complexity of our tax code is also a quiet driver of our toxic political culture. Most of us have just written off the capacity to really understand how our take-home pay is calculated and what our tax bill will be. When citizens [can't follow the math](https://taxfoundation.org/blog/national-tax-poll-understanding-taxes/), they can't meaningfully debate the trade-offs. So "debate" about the tax code becomes a Rorschach test where everyone retreats to partisan clichés. The first step toward better debate is a tax code we can actually understand and meaningfully debate.

No amount of incremental tinkering (aka "hotfixes") will address these challenges. We need a bold approach. A refactor.

## **What Do You Mean by "Refactor"?**

A refactor is necessary because software accrues what engineers call "technical debt": teams under deadline keep shipping quick fixes and new features and never go back to clean up, until the accumulated shortcuts make the whole system brittle. After accruing years of technical debt, the software is "spaghetti code" -- it is messy that every change is risky and every new contributor needs a month just to untangle how a specific component works. 

The tax code has accrued technical debt at national scale for decades. For example, the Alternative Minimum Tax was a sensible fix in 1969 to stop [155 wealthy households from paying zero](https://taxfoundation.org/taxedu/glossary/alternative-minimum-tax-amt/); decades later it had curdled into a trap for millions of upper-middle-class families it was never meant to catch.

A refactor does not change what the system is fundamentally *for*: in this case, collecting revenue and encoding a few shared priorities. The focus of refactoring is to collapse the duplication, delete the dead code, simplify the logic, so the system still works, just on clean foundations that more people can read and maintain. 

Often, executives aren't all that excited about devoting resources to a refactor because it requires resources, and there aren't any new shiny features to announce. And that same dynamic exists with politics. We are far better at adding well-meaning fixes than at removing the ones that are no longer necessary. But once a refactor is complete, you can a) move faster, because the code is easier to work with, and b) sleep better, because fewer code paths mean fewer potential exploits.


## **The Design Tenets**

This is probably the most important section of this project and, word-for-word, the part I've spent the most time writing. All of the implementation details derive from alignment around these tenets.

#### **1. Radical Simplicity.**

Every citizen should be able to understand how they're taxed. The system itself should be as automated as possible. Simplicity reduces the economic deadweight loss of compliance and evasion, and enables more focused and meaningful debate about national priorities.

#### **2. Fiscal Durability.**

Reform must measurably reduce the structural federal deficit. Closing today's ~6% of GDP gap toward a sustainable 3% will require revenue, spending discipline, and economic growth. This project will make a meaningful contribution toward this goal, primarily on the revenue side.

#### **3. Fuel the Climb.**

Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility.

#### **4. Reward Innovation.**

Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively, particularly where individual risk is highest and social returns are greatest.

#### **A note on Tenets 3 and 4.**

The last two tenets (Fuel the Climb, Reward Innovation) are meant to coexist in productive tension, and a quintessentially American one. Anti-dynastic policy, pushed too far, becomes punitive to creative enterprise. Pro-innovation policy, pushed too far, becomes a shelter for inherited wealth, undermining the chance for the next generation to build something of their own. The framework holds this tension in balance.

## **Where the Refactor Starts: Capital Gains**

Anyone who has led a big refactor will tell you the same thing: don't rewrite everything at once. Pick the module that's most broken, fix it, ship it, and let it prove the approach.

For the tax code, that module is capital gains. It's where the code is most tangled: stepped-up basis, QSBS, 1031 exchanges, carried interest, the estate tax, the AMT, the NIIT, each one a patch on a patch. It's where the gap between what the law says and what people actually pay is widest. And it's where Tenets 3 and 4 collide hardest: can new wealth still be built, and can old wealth keep compounding untaxed forever?

**Lifetime Gains Framework:** [Read the essay →](./lifetime-gains-essay.html). Replaces today's patchwork of overlapping capital gains preferences, raises significant revenue, and mitigates the "root cause" of accelerating wealth disparity. A universal exemption on capital gains, with rates that scale up based on cumulative lifetime gains.


## **About This Project**

By [Matt Sly](https://www.mattsly.com/). I'm a software entrepreneur with twenty years of experience building products used by millions of people.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and honest tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

## **A few disclaimers**

  * This is meant to be *work-in-progress* to invite collaboration and critique, similar to an open source software project.  

  * This is a **structural proposal**, not a fully calibrated legislative bill.

  * **Primarily a revenue-side project.** The capital gains module alone raises more than $100 billion a year in net new revenue (details in the [Lifetime Gains essay](./lifetime-gains-essay.html)). Spending and entitlement reform are outside the current scope; closing the rest of the deficit gap takes spending discipline and growth too.

  * All figures are directional ranges developed with Claude AI, not point estimates. Formal scoring by JCT/CBO would be needed for legislative purposes.

  * **Corporate taxation** (corporate income tax, international tax, transfer pricing) is out of scope. Corporate tax reform is deeply intertwined with global competitiveness, trade policy, and entity structure decisions that deserve their own treatment.

  * **Healthcare tax treatment** (including the employer health insurance exclusion, the largest single tax expenditure at ~$300B/yr) is out of scope. Reforming how we tax health benefits is inseparable from healthcare delivery policy, and this project stays focused on the tax system's structural architecture.

  * Feedback, critique, and collaboration are welcome: **me@mattsly.com**
