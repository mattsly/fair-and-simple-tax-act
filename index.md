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

I have spent twenty years building software. A key tenet of good software design is to resist complexity: make the user interface as simple as possible, so that it's easy for the customer to learn and make the codebase as simple as possible, so engineering teams can effectively maintain it, both now and well into the future.

How is it that all of the incredible capabilities of the iPhone or Google or ChatGPT are so easy to use and yet doing one's taxes is so hard? Some of us spend hours wading back and forth between screens in TurboTax, watching numbers flip red to green like a slot machine. Some of us just pay someone a lot of money to...basically do an esoteric form of data entry. And after all that, we still aren't sure if it's right.

What a terrible "product" experience, attached to what, for most of us, is the single largest expense of our lives.

I've surprised myself this past year with just how fascinated I've become with tax policy. That is not a typo! Our tax system *should* encode our fundamental values as a society into a clean specification. So thinking about what those values are, and then how best to build a simple and durable system around them, tickles both the philosophical and the analytical sides of my brain. 

At this point in my life, I've paid taxes from many different angles: low paid W2, high paid W2, consultant, startup employee with options, large tech company employee with options, angel investor, founder with an exit... I have seen he good, the bad, the ugly...and the uglier.

And, at the risk of just a wee bit of hyperbole, I've come to believe that the United States' tax code is the most consequential piece of technical debt in the country.

**The Tax Refactor** is a project to propose a simple, fair, and fiscally durable overhaul of our tax code, built upon four key tenets: simplicity, fiscal durability, economic mobility and innovation (detailed below). This approach is radical, but also pragmatic. There are aspects of what I propose that the political right and left will each like (and not like). I've gotten promising early feedback from policy researchers and several politicians. I think it's pretty elegant, if I do say so myself.

## **Why is a Software Guy Writing about Taxes?**

I don't have the usual bonafides to propose detailed tax policies. I'm not an economist, a tax lawyer, a CPA, or a politician.

What I have done is ship software successfully for almost twenty years - software that has been used by hundreds of millions of users. And shipping software is, at its core, the craft of taking a pile of vague, conflicting demands from a variety of stakeholders and distilling that into a specification that is rigorous enough to build, test, and maintain. You cut scope ruthlessly. You kill features people love. You design for the person who has to use the thing, not the person who built it. And - this is perhaps most important here - you focus on designing a solution that is as simple as it possibly can be. Because complexity breeds costs - both known and, more likely, unknown. You define clear success metrics. Then you ship, monitor, and iterate.

That's the discipline the tax code has never been subjected to. I'm not bringing new economics, most of the economics here is settled. I'm bringing a different question: not "what else should we add?" but "what's the simplest system that does the job?" (A future essay makes the fuller case that government can, and should, build code the way good product teams do.)

I've shipped software for twenty years, used by tens of millions and generating probably close a billion dollars of enterprise value growth. Eesh that sentence is treading dangerously close to doucheyness - it's the last one like that, I promise. And to be fair - the last thing I want to do is "Tech-Splain" how to do government. The world certainly has plenty of tech bros who think they can solve all of the problems. So my intention is not to wrestle control of tax policy from these other disciplines. But I do think I can bring a novel perspective to a crucial problem space.

## **The Algorithm Nobody Designed and the Product Nobody Wants**
(? do we defintiely need this section here in this intro essay? could it be pushed out to the "poorly designed phone" essay? I feel like it's an aside that stops the momentum that was building...)

A tax code is an algorithm (?is it an algorithm or specification?). It takes inputs (your income, your assets, your transactions) and produces an output (your tax bill). A well-designed algorithm is legible, predictable, and deterministic. The federal tax code is none of these.

This complexity is a byproduct of a political system that rewards adding new provisions rather than refactoring existing ones. In most cases, each provision was a well-intended solution to a real problem. But in a complex system, "well-intended" often invites unintended consequences. Over a century, these "reasonable solutions" have compounded into a byzantine mess that nobody actually designed.

The cost of this complexity is staggering: Americans spend [6.5 billion hours and over $500 billion annually](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/) just complying with the tax code. That is 1.9% of GDP in pure deadweight loss. Not building products, not funding factories, not making anyone healthier. Just navigating the system. Meanwhile, [hundreds of billions of dollars in taxes owed go uncollected every year](https://www.irs.gov/statistics/irs-the-tax-gap), enabled in large part by the very complexity that makes enforcement impossible.

Consider the estate tax. It was meant to curb dynastic wealth, but it became the moral cover for stepped-up basis: the notion that we shouldn't tax gains at death if the estate is already taxed. That, in turn, birthed buy-borrow-die, where billionaires borrow against untaxed appreciation to fund their lives and let death erase the bill. When that pushed effective rates for the ultra-wealthy into the single digits, Congress didn't refactor; it bolted on more layers, the AMT to catch wealthy non-payers, then the NIIT, a surtax on investment income to fund the ACA. In software terms: spaghetti code, hotfixes patching the side effects of earlier hotfixes.

The tax code takes the hardest problem in government (allocating the cost of civilization) and makes the implementation details every individual taxpayer's problem to solve. We've confused a complex economy with a requirement for a complex interface. The tax code is now inundated with brittle dependencies and edge cases that the 'product' has become a nightmare for everyone except the high-priced specialists paid to navigate it.
## **Why Now**

Three converging dynamics make the current approach to federal taxation unsustainable.

**A dire fiscal trajectory.** (? can you add references and links to the data claims in this section?) Servicing the national debt is now the federal government's third-largest line item, behind only Social Security and Medicare. It consumes 19 cents of every dollar of federal tax revenue and is the fastest-growing category in the budget. The deficit is roughly 6% of GDP; most economists across the political spectrum target 3% as a threshold for long-term stability. We are nowhere close. If that trajectory doesn't change, we eventually hit what economists call a debt death spiral: a country borrowing to pay interest on what it already owes, with each rollover demanding higher rates and weaker demand.

**conomic mobility problem.** The current code is a machine for entrenching the people who already made it. Stepped-up basis lets inherited wealth pass through generations untouched. Buy-borrow-die lets large fortunes avoid realization indefinitely. Meanwhile, the people earning their way up navigate phase-outs and cliffs in EITC, CTC, ACA subsidies, and education credits that produce some of the highest marginal tax rates in the system. (? Can we add some data about how wealth concentration now compares to pre French revolution France or something similar? Try to diffuse the "yeah but rising tides lift all boats" rebuttal? Something about how parents don't believe their kids will do better than they will for the first time ever?)

**The AI transition.** Over the next decade, new developments in Artificial Intelligence will produce structural economic shifts at a pace the tax code is not built to handle. New categories of income, work, and value creation are already emerging that don't map cleanly to W-2, 1099, or Schedule D. (? edit thids one?) Service economy job categories will change profoundly, causing disruption, unemployment, new job categories, etc... The tax code needs the dexterity to respond to those shifts to help us leverage the power of AI without further excascerbating previous two challenges.

No amount of incremental tinkering (aka "hotfixes") will address these challenges. We need a bold approach. A refactor.

One more conjecture, more speculative than the others: this complexity is also a quiet driver of our toxic political culture. When citizens can't follow the math, they can't meaningfully debate the trade-offs. The tax code becomes a Rorschach test where everyone projects their priors and nobody can be definitively wrong. "Tax the rich" and "tax cuts pay for themselves" are both slogans that survive precisely because the system is so opaque that neither can be cleanly refuted. We end up with decades of bad-faith argument about a system almost nobody actually understands. The first step toward better debate is a tax code we can actually see.

## **The Design Tenets**

The four tenets below split cleanly into two pairs. The first two (Radical Simplicity, Fiscal Durability) are design constraints, the engineering requirements for a system that works. The last two (Fuel the Climb, Reward Innovation) are commitments to what the system should be optimizing for, and they reflect a healthy tension that I think is fundamental to America.

#### **1. Radical Simplicity.**

The tax code should be broadly understood and almost entirely automated. Simplicity reduces compliance costs, economic deadweight loss, and evasion vectors. It also enables more meaningful public debate about national priorities. If citizens can't understand the system, they can't govern it.

#### **2. Fiscal Durability.**

Reform must measurably reduce the structural deficit, not just hold it steady. Servicing the debt is now the third-largest line item in the federal budget and the fastest-growing. Revenue-neutral reform is no longer enough.

#### **3. Fuel the Climb.**

Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility.

#### **4. Reward Innovation.**

Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively, particularly where individual risk is highest and social returns are greatest.

#### **A note on Tenets 3 and 4.**

These two tenets are in productive tension, a quintessentially American one. Anti-dynastic policy, pushed too far, becomes punitive to creative enterprise (protecting what people have built). Pro-innovation policy, pushed too far, becomes a shelter for inherited wealth, undermining the chance for the next generation to build something of their own (see: QSBS expansions, carried interest). The framework holds these in balance rather than picking one. Where they conflict, the conflict is named.

## **The Components (WIP)**

1. **Lifetime Gains Framework (capital gains reform):** [Read the essay →](./lifetime-gains-essay.html). Replaces the estate tax, AMT, NIIT, and twelve special preferences (QSBS, 1031 exchanges, stepped-up basis, carried interest, etc.) with four simple rules. Revenue-positive.

**Essays 2 - 5 are coming soon, fleshed out more fully with details, and linked here once they are released:**

  1. **Income Tax Reform**: Eliminate all deductions (including the mortgage interest deduction and SALT), replace the standard deduction with a 0% bracket. Filing statuses drop from five to two. Nobody earning under $250K sees a tax increase.

  2. **Child benefits consolidation:** Consolidate the CTC, EITC, and education tax credits into a single universal monthly payment per child.

  3. **Universal Savings Account (USA):** Replace 15+ tax-advantaged account types (401(k), IRA, Roth, SEP, SIMPLE, 529, HSA, FSA, and more) with a single universal account.

  4. **FICA reform:** Ensure long-term solvency

## **How It Fits Together**

The intention here is to design a simple system architecture for the fiscal relationship between citizens and their government. I will lean on system design metaphors that will sound familiar to product developers, although I will try to avoid jargon that is too arcane for a non-technical reader.

Each component has a clean interface and no shared state. Translated out of engineer-speak: no deduction depends on another deduction. No phase-out references another phase-out. Each piece can be debated, scored, and changed without breaking the others. (? wait is still really true?)

On the outbound side, citizens pay taxes through two simple mechanisms: a progressive rate table (income) and a sliding scale (capital gains). No deductions, no itemization, no parallel systems (AMT, NIIT, etc...). The government already has the data (W-2s, 1099s, transaction records) so ultimately tax payments should be fully automated for all but the most extreme edge cases. The algorithm should run automatically; the citizen confirms and clicks "submit."

On the inbound side, citizens receive money through equally simple channels: (? we've also talked about partial credits for charity etc - prob need to mentkion that here?) a monthly child payment, Social Security, and whatever direct transfers come later. The rails for government-to-citizen payments already exist, proven by the 2021 expanded CTC and the pandemic stimulus checks. The same rails could one day carry a universal basic income, an AI productivity dividend, or anything else the political process decides to fund. The architecture doesn't presume what those payments should be; it just makes them trivial to build.

Today, the tax code is a monolith: 4,000+ pages of interdependent rules where changing one provision breaks three others. This project proposes replacing that monolith with a small set of independent components. Each one is simple enough to explain in a sentence, score independently, and debate on its own merits. I think we can cut upwards of 80% of the current tax code (? too bold to make this claim?)

None of this is utopian. A free country ought to be able to read the system that taxes it. Let's build one we can.

## **About This Project**

By [Matt Sly](https://www.mattsly.com/). I'm a software entrepreneur with twenty years of experience building products used by millions of people.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and honest tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

## **A few disclaimers**

  * This is a **structural proposal**, not a fully calibrated legislative bill.

  * **Primarily a revenue-side project**, with some modest adjacent cost-cutting (most notably in Social Security). It targets reforms that raise roughly one-third of the annual deficit, on the assumption that spending discipline and economic growth do the rest.

  * All figures are directional ranges developed with Claude AI, not point estimates. Formal scoring by JCT/CBO would be needed for legislative purposes.

  * **Corporate taxation** (corporate income tax, international tax, transfer pricing) is out of scope. Corporate tax reform is deeply intertwined with global competitiveness, trade policy, and entity structure decisions that deserve their own treatment.

  * **Healthcare tax treatment** (including the employer health insurance exclusion, the largest single tax expenditure at ~$300B/yr) is out of scope. Reforming how we tax health benefits is inseparable from healthcare delivery policy, and this project stays focused on the tax system's structural architecture.

  * Feedback, critique, and collaboration are welcome: **me@mattsly.com**
