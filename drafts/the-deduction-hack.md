# The Deduction Hack

*Computing your tax bill takes about a dozen inputs. It should take one. We've been maintaining the bug since 1913.*

---

Every time I start a new job, the take-home amount in my first paycheck - the amount of money that actually makes it to my bank account after withholdings - is basically a surprise. The gross pay matches what I expected (the salary I agreed to divided by 26). But the take-home is that gross pay minus a tangle of withholdings: federal income tax, Social Security, Medicare, state tax, maybe local tax, maybe 401(k) elections, maybe pre-tax health insurance, maybe an FSA, maybe an HSA, etc.

I'm sure I'm not alone. And while we've all gotten a bit numb to this, when you step back for a bit, it's actually pretty crazy that the money we have available to spend for the labor we deliver to the world feels...kinda random?

And then there's tax season. I'll sit down with tax software and click buttons and enter numbers and the value at the top of screen flips back and forth between red (owed - boo!) and green (refund - yeah!). It reminds me of a slot machine. In other words, gambling. That's a strange relationship to have with what is,for many, our largest household expense and the mechanism by which we fund our government.

A core thesis of The Tax Refactor is that this complexity isn't free, it carries a real cost. This essay focuses on one major offender: the deduction architecture of the tax code. The idea of taking deductions - subtracting values from gross income and then using that difference to calculate your tax liability - is a remnant from over a hundred years ago. And when you start to pull at the thread of various deductions (starting with the standard deduction) you find that the idea of deductions is both unnecessarily complex and illogical.

The good news: the fix is two changes:

1. **The UI update:** turn the standard deduction into a 0% tax bracket. That's already what it is, mathematically. It's just cloaked in unnecessary complexity.
2. **The architectural refactor:** get rid of deductions, all of them (above-the-line and itemized), and replace the handful worth keeping with credits, which, as we'll get to, makes much more sense.

We'll get to the details. But first, let's look at what we're actually fixing.

## What it takes to compute your tax bill

Now, it is true that with patience and a calculator (or ideally a spreadsheet), one *could* calculate take-home. Here's "all" it takes:

```
Tax = f(
  income,
  filing_status,
  above_the_line_adjustments (Schedule 1: student loan interest, HSA, educator expenses, etc.),
  schedule_1A_deductions (new in 2025: tips, overtime, car loan, senior),
  standard_deduction_amount,
  itemized_total (only if it exceeds standard),
    └─ mortgage_interest (up to $750K of debt),
    └─ SALT (capped at $40K, phasing out above $500K AGI),
    └─ charitable_giving (above 0.5% AGI floor, below 60% AGI ceiling),
    └─ medical_expenses (above 7.5% AGI),
    └─ casualty_losses (federally declared disasters only),
  QBI_deduction (if you have pass-through income),
  credits,
  bracket_table
)
```
That's roughly twelve inputs, depending on your situation. Some are universal. Some are conditional. Some have thresholds inside them. Some have phaseouts that depend on other inputs.

Here's what the function could and should look like:

```
Tax = f(income)
```
One input. The "function" is simply taking the value of your income, and looking it up in the tax bracket and then calculating the weighted average which determines your total tax liability. Everything else in that monstrous list above is a design choice, not a necessity.

## A grocery store, but for taxes

Does the murkiness (? right word?) of one's take-home pay really matter? I think it does. For most households, taxes are one of the biggest expenses of the year, right up there with housing. (? do we have an aggregate stat on this? % of households for which this is true?) Try running a budget when your single largest line item stays a mystery until the following April. (? it's not just April but every two weeks when you get paid...)

Let's imagine if you needed to endure similar complexity for spending. Imagine you walk into a grocery store. Your total at checkout is $200. Before the cashier swipes your card, she asks:

- Did you donate to charity this year? How much?
- Do you have a mortgage? How much interest did you pay?
- Are your medical expenses more than 7.5% of your annual income?
- How much did you pay in state and local taxes?

If your answers add up to more than $15,750, you get a discount scaled to your income. If they don't, you get a flat $15,750 discount applied automatically.

So picture two shoppers in line with identical $200 carts. The first has a big mortgage, a generous year of giving, and a stack of state tax payments. She walks out paying $137. The second, a renter who gave to his church but didn't clear the threshold, takes the automatic discount and pays $163. Same groceries. Different price. The only variable was their answers to a quiz about their personal lives.

You'd think the cashier had lost her mind. None of these questions have anything to do with the groceries. 
what groceries to buy if you didn't really know how much they would cost after check out. That's kind of uncertainty is basically what we've imposed on ourselves, just on the income side of our family ledgers.

We compute our take-home pay via a series of questions about behaviors that have nothing to do with how much you earned and make it unnecessarily confusing to know how much you will have on-hand to spend.

## Sure it's confusing, but is this really that bad?

Yes, and the specific harm goes deeper than lost weekends meandering through TurboTax. The deduction architecture makes your tax rate enigmatic at best. And when you can't see a price, you make worse decisions about it.

(? not sure this paragraph works per inline comments)
Start with the most basic number in the system: your marginal rate, what the next dollar you earn actually costs you. In [a 2021 survey of 1,000 American adults](https://www.aei.org/economics/survey-confirms-that-many-americans-misunderstand-income-tax-brackets/), 51% thought that moving into a higher bracket means paying the higher rate on ALL their income. (? is this study a red herring to deductions tho? presumably even if deductions go away, the "weighted average" calculation would still be confusing to many...)) A majority of us misunderstand the single most basic feature of the tax we pay, and it isn't harmless trivia: a [review of 128 studies](https://www.tandfonline.com/doi/full/10.1080/09638180.2020.1852095) found the confusion distorts real choices about whether to take a raise, pick up a side gig, or work the extra shift. The deductions make it worse, because they don't sit still, they phase in and out. SALT phases out above $500K, the QBI deduction phases out, the new senior deduction phases out. (? also reference the "no tax on tips" thing, which is an abomination and deserves its own essay!) Each deduction secretly adds points to your marginal rate inside some band of income, so your true rate isn't a clean staircase, it's a jagged line with spikes nobody can see. Even someone who understands brackets can't tell you what their next $5,000 nets. So how do they decide whether the raise is worth it?

You can watch the confusion in the data. Last filing season, 64% of filers got a refund, averaging [$3,167](https://www.irs.gov/newsroom/filing-season-statistics-by-year) (104 million refunds out of 163.5 million returns). People over-withhold on purpose, lending the government money interest-free all year, because they'd rather get a check back than risk owing. That's 100 million Americans who can't predict their single largest annual expense within a few thousand dollars. We've decided that's normal.

And when the architecture does send a clear signal, it often points the wrong way. The mortgage interest deduction is sold as a way to help people buy homes. It has a [precisely estimated zero effect on homeownership](https://www.aei.org/economics/study-tax-subsidies-like-the-mortgage-interest-deduction-have-zero-effect-on-homeownership/); what it actually does is nudge the people who'd buy anyway to buy bigger and borrow more (? does this then artificially drive up home values ... contributing to our current affordability crisis for young people?). The itemize-or-not threshold works the same way: people bunch two years of charity into one, time medical procedures, prepay property taxes, all to clear the line. Donor-advised funds, now holding more than [$300 billion](https://www.dafresearchcollaborative.org/annual-daf-report/2025), exist in large part to game that timing. None of it produces anything.

In fairness, if you have simple W-2 income and take the standard deduction (which about 90% of filers do), the deductions don't distort much for you, and your problem is mostly the bracket confusion, which isn't really their fault. (? but even in this case, the need to take the standard deduction at all is an unnecessary layer of abstraction. Just add a 0% bracket until the amount of the standard deduction and then shift all of the brackets up by that amount, so we have a single place to look to calculate tax rateS) The sharp distortions land on the people near the thresholds and phaseouts. But the not-knowing is close to universal, and that's the tell. The system is so complex that the people paying it can't reason about it correctly. That's not a quirk. It's a design failure. And it's one we can fix.

*(One quick note before going further: there's another federal tax called FICA, the payroll tax, that takes 7.65% off the top of every paycheck. FICA is its own architectural issue and deserves its own write up, which is coming. This piece focuses on the income tax.)* (? this should maybe go earlier?)

## How we ended up here

None of this was designed. It accumulated.

The [1913 income tax](https://legalclarity.org/the-structure-of-the-revenue-act-of-1913/) was never meant for regular people. It exempted the first $3,000 of income (about $95,000 in today's dollars), so only the richest 2% of households owed anything: just 358,000 returns. And the people who did owe were mostly business owners, big farmers, and investors. (? I think we have a stat we can leverage here? Most americans owned and operated businesses back then / wage income was not common?) For them, "income" naturally meant *net* income, revenue minus the cost of earning it. Taxing a household like a small business made sense, because the households being taxed basically were small businesses.

Then the system swallowed everyone. In 1943, withholding arrived (your employer started sending the government a cut of every paycheck). Returns exploded from fewer than 4 million in 1939, about 3% of the population, to roughly 50 million by 1945, more than a third of it. The IRS suddenly had no way to audit fifty million Schedule A forms stuffed with shoebox receipts. So Congress invented the [standard deduction](https://www.thefiscaltimes.com/Columns/2019/07/11/Surprising-History-Standard-Deduction): take this flat number, skip the receipts. It wasn't a theory of fairness. It was administrative duct tape. But it quietly changed what we tax, from *net* household income to something much closer to *gross*.

That duct tape is still there. Eighty years later. Layered with new deductions Congress has added every decade since: mortgage interest, medical expenses, SALT, sales tax, educator expenses, student loan interest, and as of last year, four new deductions on a brand new schedule (Schedule 1-A) for tips, overtime, US-assembled car loans, and seniors.

The architecture is a sedimentary record. Each layer is a political moment, frozen in code. Things get added; nothing ever gets removed. (Why this keeps happening is the subject of a future essay.) We're maintaining a 1944 workaround for a problem that no longer exists, while continuing to bolt on new exceptions every time Congress wants to encourage something.

## The fix: a UI update and an architectural refactor

Two changes clean this up. One of them nobody will feel. The other is the whole ballgame.

**Change 1 (the UI update): turn the standard deduction into a 0% bracket.**

The standard deduction is just a 0% tax bracket wearing a disguise. If it's $15,750, that's identical to a bracket table where the first $15,750 of income is taxed at 0%. Try it: subtract $15,750 from $50,000, apply the 12% bracket, you get $4,110. Now tax the first $15,750 at 0% and the next $34,250 at 12%: $4,110. Same number.

So why keep the awkward "subtract this first" version instead of putting a 0% row at the top of the table? No good reason, except that's how it got jury-rigged in 1944. This change moves nobody's bill by a penny. It just deletes a confusing concept. (And once Change 2 kills itemizing, the entire "should I itemize?" decision goes away with it.)

**Change 2 (the architectural refactor): get rid of deductions, all of them, and replace the worthwhile ones with credits.**

Both kinds go: the above-the-line adjustments on Schedule 1 and the itemized deductions on Schedule A. Here's why deductions are the wrong tool in the first place.

A deduction says: this dollar wasn't income. That makes sense for the actual cost of producing income (business expenses, capital losses), which belongs inside the definition of business income. It does not make sense for charity, mortgage interest, or state taxes. Those are uses of post-tax money, not adjustments to what counts as income.

When you step back, deductions are apples to income's oranges. You earned $100,000. You gave $5,000 to your church. Your income is still $100,000. The $5,000 is what you *did* with $5,000 of your income. It's not negative income, so it really doesn't make sense to "deduct" it from income at all. It's a use of post-tax money, the same way groceries are. We've decided to subsidize one and not the other, and we deliver the subsidy by pretending the donation didn't count as income in the first place. That's a category error. We're using the income-definition mechanism to deliver a behavioral subsidy.

If we want to subsidize charitable giving (and I think we should), there's a cleaner way to do it: use credits instead.

A credit is honest. It says: the government will pay a percentage of your gift as a public match. Whether to offer the match at all, and at what rate, are political questions worth debating. But the architecture is principled either way. A flat-rate credit treats every citizen's contribution to the public good the same. A deduction treats the wealthy person's charitable preferences as worth more than the teacher's.

Consider the math. Under current law, a teacher in the 12% bracket giving $1,000 to her church gets nothing back (because she takes the standard deduction, like [about 90% of filers now do](https://taxpolicycenter.org/briefing-book/what-are-itemized-deductions-and-who-claims-them)). A hedge fund manager in the 37% bracket giving $1,000 to his alma mater gets $370 back. The federal government values the hedge fund manager's preferences at $370 per gift and the teacher's at $0. That's not a policy anyone would design from scratch. It's just what we ended up with.

I'm not going to get into which deductions should 
To keep this essay about architecture and not politics, here's the move I'm proposing: take every subsidy we currently deliver through a deduction (mortgage interest, charity, SALT, all of them) and re-express it as a credit. Keep the list exactly as it is for now. Even that straight swap isn't neutral, it shifts value away from high-bracket itemizers and toward everyone else, but that's the point: the current distribution is the accident we're fixing. Which of these subsidies actually deserve to survive, at what rate, and whether they're refundable, is a separate essay. The architectural claim here is narrow: whatever we choose to subsidize, a credit is the honest way to do it. Deductions were the wrong tool in 1913 and they're the wrong tool now.

Half the developed world has already cleaned this up. Estonia, Sweden, the Netherlands, the UK, Canada — none of them run a "standard vs. itemized" decision tree for their citizens. They apply the bracket table to income. Subsidies for behaviors they care about live elsewhere, as credits or direct payments. These are not radical countries. They've just made different design choices.

How we'd actually rebuild this for the United States (new brackets, new credit rates, transition mechanics for things like the mortgage interest deduction without crashing the housing market) is the subject of the income tax reform proposal coming later in this series.

## The easy button

Picture next April. You sit down with your phone. An app shows you: "Your income for 2026 was $X. Your tax is $Y. Tap to confirm." You tap. You're done. No TurboTax. No slot machine. No bunching strategies. No "do I itemize?" No wondering if you should call your accountant.

That's not utopian. That's the system Estonia has had for fifteen years. That's the system Sweden has. That's the system the UK has for most filers. The technical infrastructure already exists. The IRS could build a version of this with the data they already have.

And the handful of credits we keep don't break this. Your mortgage interest already lands at the IRS on a Form 1098; your charitable gifts could arrive the same way. So even for the minority who use them, the credits show up pre-filled, you confirm a number instead of assembling one. The roughly 90% who take the standard deduction today get the bare "tap to confirm." Everyone else gets the same screen with a few extra lines already filled in.

The only thing standing between us and that experience is a hundred and ten years of sedimentary deduction layers that nobody has been willing to refactor. They were each added for a reason that made sense at the time. They've been kept because no one wants to be the politician who took something away. But the cost is real, and it falls on every American who tries to plan a financial decision and can't get a straight answer about what it will cost them.

For most of us, tax should be `f(income)`. The other eleven inputs are a mistake we've been making since 1913. We can stop.
