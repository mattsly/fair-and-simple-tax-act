**A systems-thinking approach to modernizing how America taxes wealth, rewards work, and funds its future.**

The U.S. tax code is an algorithm — and it is badly broken. Not because the rates are wrong, but because 4,000 pages of interacting rules, carve-outs, and parallel systems have made it incomprehensible, unfair, and structurally incapable of collecting what it's owed. Complexity is not a side effect. It is the mechanism through which wealth inequality compounds.

This project proposes a cleaner, more durable alternative — guided by four design tenets and starting with the piece of the code that does the most damage.

---

## The Design Tenets

Every proposal in this project is evaluated against four principles. When they conflict, the tensions are acknowledged explicitly rather than papered over.

**1. Radical Simplicity.** The tax code should be broadly understood and almost entirely automated. Simplicity reduces compliance costs, economic deadweight loss, and evasion vectors. It also enables more meaningful public debate about national priorities. If citizens can't understand the system, they can't govern it.

**2. Fiscal Durability.** Reform must be meaningfully revenue-positive and resilient to political cycles. The federal deficit exceeds $2 trillion annually; net interest on the debt is now a top-five budget line item. Reforms that are merely "revenue neutral" are no longer sufficient. Revenue estimates must account for behavioral responses.

**3. Fuel the Climb.** Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility.

**4. Reward Innovation.** Risk-taking and entrepreneurship have genuine social value. The framework must preserve strong incentives to start companies, build businesses, and allocate capital productively, particularly where individual risk is highest and social returns are greatest.

---

## The Lifetime Gains Framework

The first and most fully developed proposal: a structural redesign of the entire U.S. capital gains tax system, built on five rules.

1. **A $2.5 million lifetime exemption** ($5M married) — covering 98%+ of American households. Home sales, stock sales, business exits, all treated identically.
2. **A sliding scale above the exemption** — phasing smoothly from 0% to ordinary income rates. No cliffs, no brackets, no preferential rate.
3. **Four realization events** — selling, dying, gifting, and borrowing against appreciated assets. No more deferring gains forever.
4. **Inflation-indexed basis** — so you're taxed on real wealth, not measurement error.
5. **Roth reforms** — remove the income cap, raise the annual limit, and impose a hard $5 million balance cap. This eliminates the Thiel Loophole while expanding access for high-earning professionals.

These five rules replace the estate tax, the Alternative Minimum Tax, the Net Investment Income Tax, and twelve special exclusions including QSBS, 1031 exchanges, stepped-up basis, and carried interest — the largest simplification of the capital gains code ever proposed.

The framework is revenue-positive ($85–200B/yr depending on calibration), protects small founders and homeowners, and creates a bipartisan path: estate tax repeal for the right, billionaire effective rate reform for the left, and a system ordinary citizens can actually understand for everyone.

> **[Read my proposal for the Lifetime Gains Framework tax reform →](lifetime-gains-essay.md)**

---

## What's Next

These are additional WIP proposals, each of which is scoped to be independently "shippable" and ultimately to work as part of a cohesive fiscal system:

**[Income tax reform.](income-tax-essay.md)** Eliminate all deductions (including the mortgage interest deduction and SALT), replace the standard deduction with a 0% bracket, and reduce the rate table from seven brackets to five. The charitable and medical expense deductions are replaced with targeted credits that work for all filers, not just itemizers. Filing statuses drop from five to two. Nobody earning under $250K sees a tax increase. A working draft is available.

**[Child payment.](child-payment-essay.md)** Consolidate the CTC, EITC, and education tax credits into a single universal monthly payment per child. The 2021 expanded CTC experiment cut child poverty ~30% in six months. This proposal makes it permanent, funds it by redirecting the budgets of nine overlapping programs, and delivers it monthly instead of annually.

**[FICA reform.](fica-reform-essay.md)** Eliminate employee-side FICA entirely (an immediate ~8% raise for every worker), replace it with an uncapped 8% employer-side contribution, and broaden Social Security's funding base without cutting benefits. Self-employed individuals pay 8% flat, down from 15.3%.

**[Universal Savings Account (USA).](universal-savings-account-essay.md)** Replace 15+ tax-advantaged account types (401(k), IRA, Roth, SEP, SIMPLE, 529, HSA, FSA, and more) with a single universal account. After-tax contributions, tax-free growth, $5M balance cap, $1,000 government seed at birth. A 10-year conversion window at a 12% flat rate generates an estimated $1.2-1.3 trillion in one-time revenue while leaving most savers hundreds of thousands of dollars better off.

Each of these is guided by the same four design tenets above.

---

## The Architecture

What we're building is a simple system architecture for the fiscal relationship between citizens and their government. Each component has a clean interface, no shared state (no deductions that cross boundaries, no phase-outs that reference other programs), and can be deployed, tested, and modified independently.

On the outbound side, citizens pay taxes through two simple mechanisms: a progressive rate table (income) and a sliding scale (capital gains). No deductions, no itemization, no parallel systems. The government already has the data (W-2s, 1099s, transaction records). The algorithm should run automatically; the citizen confirms and clicks "submit."

On the inbound side, citizens receive payments through equally simple mechanisms: a monthly child payment, a Social Security payment, and potentially other direct transfers in the future. The infrastructure for direct government-to-citizen payments (proven by the 2021 expanded CTC and pandemic stimulus checks) is the same infrastructure that could one day deliver a universal basic income, an AI productivity dividend, or any other form of direct transfer that the political process decides to fund. The architecture doesn't presume what those future payments should be. It just makes them trivial to implement.

Today, the tax code is a monolith: 4,000+ pages of interdependent rules where changing one provision breaks three others. This project proposes replacing that monolith with a small set of independent components. Each one is simple enough to explain in a sentence, score independently, and debate on its own merits.

---

## About This Project

By [Matt Sly](https://www.mattsly.com). I'm a software entrepreneur with twenty years of experience building products used by millions of people. I approach the tax code the way I would any complex system that has accumulated decades of technical debt without a clear owner: identify the structural problems, propose a major refactor, and invite scrutiny.

This project is not affiliated with a political party, campaign, or institution. It is an attempt to apply systems thinking, real-world experience, and honest tradeoffs to a problem that sits at the intersection of economics, equity, and long-term national health.

---

## Scope and Status

- This is a **structural proposal**, not a fully calibrated legislative bill.
- All figures are directional ranges, not point estimates. Formal scoring by JCT/CBO would be needed for legislative purposes.
- **Corporate taxation** (corporate income tax, international tax, transfer pricing) is out of scope. Corporate tax reform is deeply intertwined with global competitiveness, trade policy, and entity structure decisions that deserve their own treatment.
- **Healthcare tax treatment** (including the employer health insurance exclusion, the largest single tax expenditure at ~$300B/yr) is out of scope. Reforming how we tax health benefits is inseparable from healthcare delivery policy, and this project stays focused on the tax system's structural architecture.
- Feedback, critique, and collaboration are welcome: **me@mattsly.com**
