---
title: Introducing "The Tax Refactor"
subtitle: A software entrepreneur’s case for simple, fair and durable tax reform of
  America’s "Most Expensive Technical Debt"
author: Matt Sly
publication: The Tax Refactor
date: April 08, 2026
---

# Introducing "The Tax Refactor"
**The U.S. tax code is an algorithm. And it is badly broken.**

I have spent twenty years building software. Along the way, I’ve seen the tax code from many different angles: as a salaried employee, a startup employee with stock options, a big tech employee paid in RSUs, a founder with an exit, and an angel investor.

And as both a software professional and a concerned citizen, I’ve come to believe the American tax code is the most consequential piece of technical debt in the United States. In its current state, it lacks the policy dexterity required to navigate a mounting fiscal deficit or the profound structural shifts driven by AI.

 **The Tax Refactor** is a project to propose a simple, fair, and fiscally durable alternative, built for economic mobility and innovation.

[![](https://substackcdn.com/image/fetch/$s_!Hk7X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b121f6d-9400-4c68-b094-d2198a12ff95_1024x608.png)](https://substackcdn.com/image/fetch/$s_!Hk7X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b121f6d-9400-4c68-b094-d2198a12ff95_1024x608.png)

It’s radical, but also pragmatic. There are aspects of what I propose that the political right and left will each like (and not like). I’ve gotten promising early feedback from policy researchers and several politicians. I think it’s pretty elegant, if I do say so myself.

##  **The Algorithm Nobody Designed and the Product Nobody Wants**

A tax code is an algorithm. It takes inputs (your income, your assets, your transactions) and produces an output (your tax bill). A well-designed algorithm is legible, predictable, and deterministic. The federal tax code is none of these.

This complexity is a byproduct of a political system that rewards adding new provisions rather than refactoring existing ones. In most cases, each provision was a well-intended solution to a real problem. But in a complex system, “well-intended” often invites unintended consequences. Over a century, these “reasonable solutions” have compounded into a byzantine mess that nobody actually designed.

The cost of this complexity is staggering: Americans spend [6.5 billion hours and over $500 billion annually](https://taxfoundation.org/data/all/federal/irs-tax-compliance-costs/) just complying with the tax code. That is 1.9% of GDP in pure deadweight loss. Not building products, not funding factories, not making anyone healthier. Just navigating the system. Meanwhile, [hundreds of billions of dollars in taxes owed go uncollected every year](https://www.irs.gov/statistics/irs-the-tax-gap), enabled in large part by the very complexity that makes enforcement impossible.

Consider the estate tax: it was created to prevent dynastic wealth, but it provided the moral ‘double taxation’ cover for stepped-up basis (the idea that we shouldn’t tax gains at death if we’re already taxing the estate). That loophole, in turn, birthed ‘Buy, Borrow, Die’—the ultimate bypass where billionaires borrow against untaxed appreciation to fund their lives, then let death erase the tax bill entirely. When this drove effective rates for the ultra-wealthy into the single digits, Congress didn’t refactor the system; they just bolted on more layers. They added the Alternative Minimum Tax (AMT) as a “shadow” tax code to catch wealthy non-payers, and later the Net Investment Income Tax (NIIT) as an unrelated conditional surtax on investment income to fund the ACA. In software speak, this is ‘spaghetti code’ — a tangled mess of ‘hotfixes’ created just to manage the side effects of previous ‘hotfixes.’

This is a design failure. In any other industry, the best products hide complexity from the user. Google search is one of the most sophisticated pieces of software ever built, yet you interact with it through a single text box. An iPhone requires millions of lines of code and a global supply chain, but a child can learn the interface in minutes.

The tax code does the opposite. It takes the hardest problem in government (allocating the cost of civilization) and makes the implementation details every individual taxpayer’s problem to solve. We’ve confused a complex economy with a requirement for a complex interface. The tax code is now inundated with brittle dependencies and edge cases that the ‘product’ has become a nightmare for everyone except the high-priced specialists paid to navigate it.

##  **The Design Tenets**

Every proposal in this project is evaluated against four principles. When they conflict, the tensions are acknowledged explicitly rather than papered over.

####  **1\. Radical Simplicity.**

The tax code should be broadly understood and almost entirely automated. Simplicity reduces compliance costs, economic deadweight loss, and evasion vectors. It also enables more meaningful public debate about national priorities. If citizens can’t understand the system, they can’t govern it.

####  **2\. Fiscal Durability.**

Reform must be meaningfully revenue-positive and resilient to political cycles. The federal deficit exceeds $2 trillion annually; net interest on the debt is now a top-five budget line item. Reforms that are merely “revenue neutral” are no longer sufficient. Revenue estimates must account for behavioral responses.

####  **3\. Fuel the Climb.**

Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility.

####  **4\. Reward Innovation.**

Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively, particularly where individual risk is highest and social returns are greatest.

##  **The Components (WIP)**

 **Parts 2 - 5 are still WIP and will be linked here once they are released:**

  2.  **Income Tax Reform** : Eliminate all deductions (including the mortgage interest deduction and SALT), replace the standard deduction with a 0% bracket, and reduce the rate table from seven brackets to four. The charitable and medical expense deductions are replaced with targeted credits that work for all filers, not just itemizers. Filing statuses drop from five to two. Nobody earning under $250K sees a tax increase. 

  3. **Child benefits consolidation:** Consolidate the CTC, EITC, and education tax credits into a single universal monthly payment per child. The 2021 expanded CTC experiment cut child poverty ~30% in six months. This proposal makes it permanent, funds it by redirecting the budgets of nine overlapping programs, and delivers it monthly instead of annually.

  4.  **FICA reform:** Ensure long-term solvency by eliminating employee-side FICA entirely (an immediate ~8% raise for every worker), replace it with an uncapped 8% employer-side contribution, and broaden Social Security’s funding base without cutting benefits. Self-employed individuals pay 8% flat, down from 15.3%.

  5.  **Universal Savings Account (USA):** Replace 15+ tax-advantaged account types (401(k), IRA, Roth, SEP, SIMPLE, 529, HSA, FSA, and more) with a single universal account. After-tax contributions, tax-free growth, $5M balance cap, $1,000 government seed at birth. A 10-year conversion window at a 12% flat rate generates an estimated $1.2-1.3 trillion in one-time revenue while leaving most savers hundreds of thousands of dollars better off.




##  **Designing a “Civic Architecture”**

The intention here is to design a simple system architecture for the fiscal relationship between citizens and their government. I will lean heavily on system design metaphors, although I will try to avoid veering off into jargon that is too arcane for a non-technical reader. 

Each component of the reform is designed to have a clean interface, with no shared state (no deductions that cross boundaries, no phase-outs that reference other programs), and can be deployed, tested, and modified independently.

On the outbound side, citizens pay taxes through two simple mechanisms: a progressive rate table (income) and a sliding scale (capital gains). No deductions, no itemization, no parallel systems. The government already has the data (W-2s, 1099s, transaction records) so ultimately tax payments should be fully automated for all but the most extreme edge cases. The algorithm should run automatically; the citizen confirms and clicks “submit.”

On the inbound side, citizens receive payments through equally simple mechanisms: a monthly child payment, a Social Security payment, and potentially other direct transfers in the future. The infrastructure for direct government-to-citizen payments (proven by the 2021 expanded CTC and pandemic stimulus checks) is the same infrastructure that could one day deliver a universal basic income, an AI productivity dividend, or any other form of direct transfer that the political process decides to fund. The architecture doesn’t presume what those future payments should be. It just makes them trivial to implement.

Today, the tax code is a monolith: 4,000+ pages of interdependent rules where changing one provision breaks three others. This project proposes replacing that monolith with a small set of independent components. Each one is simple enough to explain in a sentence, score independently, and debate on its own merits.

##  **About This Project**

By [Matt Sly](https://www.mattsly.com/). I’m a software entrepreneur with twenty years of experience building products used by millions of people. I approach the tax code the way I would any complex system that has accumulated decades of technical debt without a clear owner: identify the structural problems, propose a major refactor, and invite scrutiny.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and honest tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

##  **Scope and Status**

  * This is a **structural proposal** , not a fully calibrated legislative bill.

  * All figures are directional ranges, not point estimates. Formal scoring by JCT/CBO would be needed for legislative purposes.

  *  **Corporate taxation** (corporate income tax, international tax, transfer pricing) is out of scope. Corporate tax reform is deeply intertwined with global competitiveness, trade policy, and entity structure decisions that deserve their own treatment.

  *  **Healthcare tax treatment** (including the employer health insurance exclusion, the largest single tax expenditure at ~$300B/yr) is out of scope. Reforming how we tax health benefits is inseparable from healthcare delivery policy, and this project stays focused on the tax system’s structural architecture.

  * Feedback, critique, and collaboration are welcome: **me@mattsly.com**



