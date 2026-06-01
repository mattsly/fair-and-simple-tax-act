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
---

# Introducing "The Tax Refactor"

**The U.S. tax code is an algorithm. And it is badly broken.**

I have spent twenty years building software. A guiding principle of great software design is to resist complexity. Keep the user interface simple, so customers can learn on their own. Keep the codebase, to enable maintainability, reduce regression risk, and mitigate security vulnerabilities.

A tax *code* is a form of technology. It's a series of algorithms. It could be simple. And yet, how is it that all of far more sophisicated capabilities of our technologies (iPhone, Google, Claude etc) are so easy to use and yet doing one's taxes - what could and should be way simpler - is so hard? Consider the "user experience" of doing one's taxes. Some of us spend hours wading back and forth between screens in TurboTax, watching numbers flip red to green like a slot machine. Some of us just pay someone a lot of money to...basically do an esoteric form of data entry. And after all that, we still aren't sure if it's right.

What a terrible "customer" experience, attached to what, for most of us, is the single largest expense of our lives and the most important "product" that we use: our citizenship. Americans spend [6.5 billion hours and over $500 billion annually](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/) just complying with the tax code, or 1.9% of GDP in pure deadweight loss. Not building products, not funding factories, not making anyone healthier. Just navigating the system. If I shipped a product with metrics like that, I'd get fired.

I've surprised myself this past year with just how fascinated I've become with tax policy. That is not a typo! Our tax system *should* encode our fundamental values as a society into a clean specification and ultimately a simple user interface. Thinking about what those values are, and then how best to build durable system to support them tickles both sides of my brain. That's is a really interesting challenge.

And, at the risk of just a wee bit of hyperbole, I've come to believe that the United States' tax code is the most consequential piece of "technical debt" in the country.

**The Tax Refactor** is a proposal to overhaul our tax code, built upon four key tenets: simplicity, fiscal durability, economic mobility and innovation (all detailed below). This approach is radical, but also pragmatic. There are aspects of what I propose that the political right and left will each like (and not like). I've gotten promising early feedback from policy researchers and several politicians.

## **Why is a Software Guy Writing about Taxes?**

I don't have the usual bonafides to propose detailed tax policies. I'm not an economist, a tax lawyer, a CPA, or a politician. But at this point in my life, I've paid taxes from many different angles: low-paid W-2, high-paid W-2, consultant, startup employee with options, large tech company employee with options, angel investor, founder with an exit... I have seen the good, the bad, the ugly...and the uglier.

And I have shipped high impact software for almost twenty years - software used by tens of millions and generating something around a billion dollars of enterprise value. Eesh that sentence is treading dangerously close to doucheyness - I'm sorry - it's the last one like that, I promise. And to be clear, the last thing I want to do is "Tech-Splain" how to do government. But I do contend that there are principles of good software design that can be applied to tax policy. Product thinkers should be in the room when we're designing 21st-century tax infrastructure.

Building software products entails asking "what are the problems we are trying to solve" and then "what's the simplest system that does the job?" You take a pile of vague, conflicting demands from a variety of stakeholders and distill those into a specification that is rigorous enough to build, test, and maintain. Good software has a product experience that is easy to learn and even delightful to use. You cut scope ruthlessly and kill features people love. You design for the person who has to use the product, not the person who built it or gets to announce it. You define clear success metrics. You ship, monitor, and iterate. And - this is perhaps most important here - you focus on designing a solution that is as simple as it possibly can be. Because complexity breeds costs - both known and, more likely, unknown. (? is this redundant with some of the intro above? can/should we trim this paragraph a bit? is the second person awkward?

## **Why Now**

Three converging dynamics make the current approach to federal taxation unsustainable.

**A dire fiscal trajectory.** Servicing the national debt is [now the federal government's third-largest line item](https://www.cbo.gov/publication/61172) consumes roughly 19 cents of every dollar of federal tax revenue, up from about 8 cents a decade ago, and is the fastest-growing category in the budget. The annual deficit is roughly 6% of GDP, well above the [3% threshold commonly cited as a target](https://www.crfb.org/papers/case-3-gdp-deficit-target). Meanwhile, [hundreds of billions in taxes owed go uncollected every year](https://www.irs.gov/statistics/irs-the-tax-gap), enabled in large part by the very complexity that makes enforcement impossible. If the trajectory doesn't change, we eventually hit what economists call a debt death spiral: a country borrowing to pay interest on what it already owes, with each rollover demanding higher rates and weaker demand. (For the range of calamitous scenarios, see [CBO's long-term budget projections](https://www.cbo.gov/publication/62044).)

**An economic mobility problem.** The potential for each generation to have more economic opportunity the previous is a defining features of the "American Dream." [Yet, only about 50% of Americans born in 1984 earn more than their parents did at the same age, down from 92% for those born in 1940](https://opportunityinsights.org/paper/the-fading-american-dream/). There are many specific culprits (stepped-up basis, a feckless estate tax, infinitely preferential capital gains rates, to name a few), but the deeper problem is structural: a tax code designed around constituencies rather than citizens. (More on that in a future essay.) (? we need more data here that also shows the increase in the concentration of wealth over the last 50 years as well...? and we should concede it's not only the tax code, but that's the engine that helps perpetuate and grow it...)

**The AI transition.** Over the next decade, AI will drive structural economic shifts at a pace the tax code was not built to handle. Whole job categories will compress: customer service, paralegal work, basic radiology, parts of accounting. New ones (AI operators, alignment researchers, agentic workflow designers) will appear faster than the tax code can categorize them. The system needs the dexterity to respond to those shifts and harness AI's productivity without further exacerbating the previous two challenges.

One more conjecture, more speculative than the others: this complexity is also a quiet driver of our toxic political culture. When citizens [can't follow the math](https://www.credello.com/news/most-americans-dont-know-their-tax-bracket/), they can't meaningfully debate the trade-offs. The tax code becomes a Rorschach test where everyone projects their priors and nobody can be definitively wrong. "Tax the rich" and "tax cuts pay for themselves" are both slogans that survive precisely because the system is so opaque that neither can be cleanly refuted. We end up with decades of bad-faith argument about a system almost nobody actually understands. The first step toward better debate is a tax code we can actually see.

No amount of incremental tinkering (aka "hotfixes") will address these challenges. We need a bold approach. A refactor.

## **The Design Tenets**
#### **1. Radical Simplicity.**

The tax code should be broadly understood and almost entirely automated. Simplicity reduces compliance costs, economic deadweight loss, and evasion vectors. It also enables more meaningful public debate about national priorities. If citizens can't understand the system, they can't govern it.

#### **2. Fiscal Durability.**

Reform must measurably reduce the structural deficit, not just hold it steady. Servicing the debt is now the third-largest line item in the federal budget and the fastest-growing. Revenue-neutral reform is no longer enough.

#### **3. Fuel the Climb.**

Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility.

#### **4. Reward Innovation.**

Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively, particularly where individual risk is highest and social returns are greatest.

#### **A note on Tenets 3 and 4.**

The first two tenets (Radical Simplicity, Fiscal Durability) are design constraints for a system that works and can scale. 

The last two (Fuel the Climb, Reward Innovation) are in productive tension, a quintessentially American one. Anti-dynastic policy, pushed too far, becomes punitive to creative enterprise. Pro-innovation policy, pushed too far, becomes a shelter for inherited wealth, undermining the chance for the next generation to build something of their own. The framework holds this tension in balance.

## **The Components (WIP)**

1. **Lifetime Gains Framework (capital gains reform):** [Read the essay →](./lifetime-gains-essay.html). Replaces the estate tax, AMT, NIIT, and twelve special preferences (QSBS, 1031 exchanges, stepped-up basis, carried interest, etc.) with four simple rules. Revenue-positive.

**Essays 2 - 5 are coming soon, fleshed out more fully with details, and linked here once they are released:**

  1. **Income Tax Reform**: Eliminate all deductions (including the mortgage interest deduction and SALT), replace the standard deduction with a 0% bracket. Filing statuses drop from five to two. Nobody earning under $250K sees a tax increase.

  2. **Child benefits consolidation:** Consolidate the CTC, EITC, and education tax credits into a single universal monthly payment per child.

  3. **Universal Savings Account (USA):** Replace 15+ tax-advantaged account types (401(k), IRA, Roth, SEP, SIMPLE, 529, HSA, FSA, and more) with a single universal account.

  4. **FICA reform:** Ensure long-term solvency

## **How It Fits Together**

Each component has a clean interface and minimal shared state, meaning each piece can be debated, scored, and changed largely independent of the others. Some interactions remain (the charitable credit touches the capital gains framework when appreciated assets are donated, for example), but the dense web of phase-outs and parallel systems that defines today's code is gone.

**Outbound:** citizens pay through two simple mechanisms (a progressive income rate table and a sliding capital gains scale), with a small set of targeted credits where social value is clear (charitable giving, catastrophic medical). No itemized deductions, no parallel systems (AMT, NIIT, etc.). The government already has the data (W-2s, 1099s, transaction records), so for most filers, the system runs automatically and the citizen confirms and clicks "submit."

**Inbound:** monthly child payments, Social Security, the targeted credits above, and whatever direct transfers come later. The rails already exist, proven by the 2021 expanded CTC and pandemic stimulus checks. Whether the political process decides to fund a universal basic income, an AI productivity dividend, or something else, the architecture makes those payments trivial to build.

Today's tax code is a 4,000-page monolith where changing one provision breaks three others. This project replaces it with a small set of independent components. The proposed system eliminates the estate tax, the AMT, the NIIT, roughly a dozen capital gains preferences (QSBS, 1031 exchanges, stepped-up basis, carried interest, and more), three of the five filing statuses, the entire itemized deductions stack, the fifteen-plus tax-advantaged account types, and the alphabet soup of child and education credits. Back-of-envelope, that's about 80% of what an individual filer ever has to deal with.

None of this is utopian. A free country ought to be able to read the system that taxes it. Let's build one we can.

## **About This Project**

By [Matt Sly](https://www.mattsly.com/). I'm a software entrepreneur with twenty years of experience building products used by millions of people.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and honest tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

## **A few disclaimers**

  * This is a meant to be *work-in-progress* to invite collaboration and critique. Similar to an open source software project.  

  * This is a **structural proposal**, not a fully calibrated legislative bill.

  * **Primarily a revenue-side project**, with some modest adjacent cost-cutting (most notably in Social Security). It targets reforms that raise roughly one-third of the annual deficit, on the assumption that spending discipline and economic growth do the rest.

  * All figures are directional ranges developed with Claude AI, not point estimates. Formal scoring by JCT/CBO would be needed for legislative purposes.

  * **Corporate taxation** (corporate income tax, international tax, transfer pricing) is out of scope. Corporate tax reform is deeply intertwined with global competitiveness, trade policy, and entity structure decisions that deserve their own treatment.

  * **Healthcare tax treatment** (including the employer health insurance exclusion, the largest single tax expenditure at ~$300B/yr) is out of scope. Reforming how we tax health benefits is inseparable from healthcare delivery policy, and this project stays focused on the tax system's structural architecture.

  * Feedback, critique, and collaboration are welcome: **me@mattsly.com**
