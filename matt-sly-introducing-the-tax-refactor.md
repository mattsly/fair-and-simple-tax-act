---
title: Introducing "The Tax Refactor"
subtitle: A software entrepreneur's case for simple, fair and durable tax reform of America's "Most Expensive Technical Debt"
author: Matt Sly
publication: The Tax Refactor
date: April 08, 2026
---

# Introducing "The Tax Refactor"
**The U.S. tax code is an algorithm. And it is badly broken.**

I have spent twenty years building software. A key tenet of good software design is to resist complexity: make the user interface as simple as possible, so that it's easy for the customer to learn; make the codebase as simple as possible, so engineering teams can effectively maintain it, both now and well into the future.

How is it that all of the incredible capabilities of the iPhone or Google or ChatGPT are so easy to use and yet doing one's taxes is so hard? Some of us spend hours wading back and forth between screens in TurboTax, watching numbers flip red to green like a slot machine. Some of us just pay someone a lot of money to...basically do an esoteric form of data entry. And after all that, we still aren't sure if it's right.

What a terrible "product" experience with what, for most of us, is our single largest household expense.

TurboTax and CPAs aren't the problem. The problem is what they're both trying to interpret: the underlying tax code itself.

I've surprised myself in the last year with just how fascinated I have become with tax policy. That is not a typo! I enjoy thinking about system design and I've seen the tax code from a variety of perspectives having paid taxes in many forms (W2, startup employee, RSUs, founder w/ an exit...).

Indeed the United States' tax code, I've come to believe, is the most consequential piece of technical debt in the country.

**The Tax Refactor** is a project to propose a simple, fair, and fiscally durable alternative, built for economic mobility and innovation. It's radical, but also pragmatic. There are aspects of what I propose that the political right and left will each like (and not like). I've gotten promising early feedback from policy researchers and several politicians. I think it's pretty elegant, if I do say so myself.

[![](https://substackcdn.com/image/fetch/$s_!Hk7X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b121f6d-9400-4c68-b094-d2198a12ff95_1024x608.png)](https://substackcdn.com/image/fetch/$s_!Hk7X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b121f6d-9400-4c68-b094-d2198a12ff95_1024x608.png)](https://substackcdn.com/image/fetch/$s_!Hk7X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b121f6d-9400-4c68-b094-d2198a12ff95_1024x608.png)

## **The Algorithm Nobody Designed and the Product Nobody Wants**

A tax code is an algorithm. It takes inputs (your income, your assets, your transactions) and produces an output (your tax bill). A well-designed algorithm is legible, predictable, and deterministic. The federal tax code is none of these.

This complexity is a byproduct of a political system that rewards adding new provisions rather than refactoring existing ones. In most cases, each provision was a well-intended solution to a real problem. But in a complex system, "well-intended" often invites unintended consequences. Over a century, these "reasonable solutions" have compounded into a byzantine mess that nobody actually designed.

The cost of this complexity is staggering: Americans spend [6.5 billion hours and over $500 billion annually](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/) just complying with the tax code. That is 1.9% of GDP in pure deadweight loss. Not building products, not funding factories, not making anyone healthier. Just navigating the system. Meanwhile, [hundreds of billions of dollars in taxes owed go uncollected every year](https://www.irs.gov/statistics/irs-the-tax-gap), enabled in large part by the very complexity that makes enforcement impossible.

Consider the estate tax: it was created to prevent dynastic wealth, but it provided the moral 'double taxation' cover for stepped-up basis (the idea that we shouldn't tax gains at death if we're already taxing the estate). That loophole, in turn, birthed 'Buy, Borrow, Die', the ultimate bypass where billionaires borrow against untaxed appreciation to fund their lives, then let death erase the tax bill entirely. When this drove effective rates for the ultra-wealthy into the single digits, Congress didn't refactor the system; they just bolted on more layers. They added the Alternative Minimum Tax (AMT) as a "shadow" tax code to catch wealthy non-payers, and later the Net Investment Income Tax (NIIT) as an unrelated conditional surtax on investment income to fund the ACA. In software speak, this is 'spaghetti code', a tangled mess of 'hotfixes' created just to manage the side effects of previous 'hotfixes.'

The tax code takes the hardest problem in government (allocating the cost of civilization) and makes the implementation details every individual taxpayer's problem to solve. We've confused a complex economy with a requirement for a complex interface. The tax code is now inundated with brittle dependencies and edge cases that the 'product' has become a nightmare for everyone except the high-priced specialists paid to navigate it.

## **Why Now**

This kind of reform has been discussed for decades. So why try now?

Three converging pressures make the current trajectory unsustainable.

**The fiscal trajectory.** Servicing the national debt is now the federal government's third-largest line item, behind only Social Security and Medicare. It consumes 19 cents of every dollar of federal tax revenue and is the fastest-growing category in the budget. The deficit is roughly 6% of GDP; most economists across the political spectrum target 3% as a threshold for long-term stability. We are nowhere close. If that trajectory doesn't change, we eventually hit what economists call a debt death spiral: a country borrowing to pay interest on what it already owes, with each rollover demanding higher rates and weaker demand.

**The mobility problem.** The current code is a machine for entrenching the people who already made it. Stepped-up basis lets inherited wealth pass through generations untouched. Buy-borrow-die lets large fortunes avoid realization indefinitely. Meanwhile, the people earning their way up navigate phase-outs and cliffs in EITC, CTC, ACA subsidies, and education credits that produce some of the highest marginal tax rates in the system.

**The AI transition.** Whatever you think about the timeline, the next decade will produce structural economic shifts at a pace the tax code is not built to handle. New categories of income, work, and value creation are already emerging that don't map cleanly to W-2, 1099, or Schedule D. The system needs the dexterity to respond to those shifts without another century of bolted-on hotfixes. A tax code designed in the era of typewriters cannot govern an economy running on real-time machine intelligence.

Each of these is a system-level failure, not a programmatic one. No amount of incremental tinkering with individual provisions will address them. They are consequences of the architecture itself.

One more conjecture, more speculative than the others: this complexity is also a quiet driver of our toxic political culture. When citizens can't follow the math, they can't meaningfully debate the trade-offs. The tax code becomes a Rorschach test where everyone projects their priors and nobody can be definitively wrong. "Tax the rich" and "tax cuts pay for themselves" are both slogans that survive precisely because the system is so opaque that neither can be cleanly refuted. We end up with decades of bad-faith argument about a system almost nobody actually understands. The first step toward better debate is a tax code we can actually see.

## **The Design Tenets**

Walter Isaacson recently called "Life, Liberty, and the pursuit of Happiness" [the greatest sentence ever written](https://news.harvard.edu/gazette/story/2025/11/our-self-evident-truths/). The second half of that sentence (the *Pursuit* part) is where the philosophical core of this project lives.

The four tenets below split cleanly into two pairs. The first two (Radical Simplicity, Fiscal Durability) are design constraints, the engineering requirements for a system that works. The last two (Fuel the Climb, Reward Innovation) are commitments to what the system should be optimizing for, and they reflect a tension as old as the country. When they conflict, the tensions are acknowledged explicitly rather than papered over.

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

1. **Lifetime Gains Framework (capital gains reform):** [(lifetime-gains-essay.md)]. Replaces the estate tax, AMT, NIIT, and twelve special preferences (QSBS, 1031 exchanges, stepped-up basis, carried interest, etc.) with four simple rules. Revenue-positive.

**Essays 2 - 5 are coming soon and will be linked here once they are released:**

  1. **Income Tax Reform**: Eliminate all deductions (including the mortgage interest deduction and SALT), replace the standard deduction with a 0% bracket, and reduce the rate table from seven brackets to four. The charitable and medical expense deductions are replaced with targeted credits that work for all filers, not just itemizers. Filing statuses drop from five to two. Nobody earning under $250K sees a tax increase.

  2. **Child benefits consolidation:** Consolidate the CTC, EITC, and education tax credits into a single universal monthly payment per child. The 2021 expanded CTC experiment cut child poverty ~30% in six months. This proposal makes it permanent, funds it by redirecting the budgets of nine overlapping programs, and delivers it monthly instead of annually.

  3. **FICA reform:** Ensure long-term solvency by eliminating employee-side FICA entirely (an immediate ~8% raise for every worker), replace it with an uncapped 8% employer-side contribution, and broaden Social Security's funding base without cutting benefits. Self-employed individuals pay 8% flat, down from 15.3%.

  4. **Universal Savings Account (USA):** Replace 15+ tax-advantaged account types (401(k), IRA, Roth, SEP, SIMPLE, 529, HSA, FSA, and more) with a single universal account. After-tax contributions, tax-free growth, $5M balance cap, $1,000 government seed at birth. A 10-year conversion window at a 12% flat rate generates an estimated $1.2-1.3 trillion in one-time revenue while leaving most savers hundreds of thousands of dollars better off.

## **How It Fits Together**

The intention here is to design a simple system architecture for the fiscal relationship between citizens and their government. I will lean on system design metaphors, although I will try to avoid jargon that is too arcane for a non-technical reader.

Each piece has a clean interface and no shared state. Translated out of engineer-speak: no deduction depends on another deduction. No phase-out references another phase-out. Each piece can be debated, scored, and changed without breaking the others.

On the outbound side, citizens pay taxes through two simple mechanisms: a progressive rate table (income) and a sliding scale (capital gains). No deductions, no itemization, no parallel systems. The government already has the data (W-2s, 1099s, transaction records) so ultimately tax payments should be fully automated for all but the most extreme edge cases. The algorithm should run automatically; the citizen confirms and clicks "submit."

On the inbound side, citizens receive payments through equally simple mechanisms: a monthly child payment, a Social Security payment, and potentially other direct transfers in the future. The infrastructure for direct government-to-citizen payments (proven by the 2021 expanded CTC and pandemic stimulus checks) is the same infrastructure that could one day deliver a universal basic income, an AI productivity dividend, or any other form of direct transfer that the political process decides to fund. The architecture doesn't presume what those future payments should be. It just makes them trivial to implement.

Today, the tax code is a monolith: 4,000+ pages of interdependent rules where changing one provision breaks three others. This project proposes replacing that monolith with a small set of independent components. Each one is simple enough to explain in a sentence, score independently, and debate on its own merits.

## **About This Project**

By [Matt Sly](https://www.mattsly.com/). I'm a software entrepreneur with twenty years of experience building products used by millions of people. I approach the tax code the way I would any complex system that has accumulated decades of technical debt without a clear owner: identify the structural problems, propose a major refactor, and invite scrutiny.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and honest tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

## **Scope and Status**

  * This is a **structural proposal**, not a fully calibrated legislative bill.

  * **Primarily a revenue-side project**, with some modest adjacent cost-cutting (most notably in Social Security). It targets reforms that raise roughly one-third of the annual deficit, on the assumption that spending discipline and economic growth do the rest.

  * All figures are directional ranges, not point estimates. Formal scoring by JCT/CBO would be needed for legislative purposes.

  * **Corporate taxation** (corporate income tax, international tax, transfer pricing) is out of scope. Corporate tax reform is deeply intertwined with global competitiveness, trade policy, and entity structure decisions that deserve their own treatment.

  * **Healthcare tax treatment** (including the employer health insurance exclusion, the largest single tax expenditure at ~$300B/yr) is out of scope. Reforming how we tax health benefits is inseparable from healthcare delivery policy, and this project stays focused on the tax system's structural architecture.

  * Feedback, critique, and collaboration are welcome: **me@mattsly.com**