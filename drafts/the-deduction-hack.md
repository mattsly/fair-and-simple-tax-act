# The 1913 Bug We Never Fixed

*The tax deduction is a bizarre remnant from a different era. We can do better.*

---

Every time I've started a new job, when I get my first paycheck, the take-home amount is basically a surprise. The gross pay matches what I expected (my salary divided by 26). But the net - what ends up in my bank account for actual spending - involves a complex calculation that based on an assortment of federal income tax, Social Security, Medicare, state tax, maybe local tax, maybe 401(k) elections, maybe pre-tax health insurance, maybe an FSA, maybe an HSA.

And then there's tax season. I'll sit down with tax software. I click buttons and enter numbers and the number at the top of the screen flips back and forth between red and green like a slot machine. I will usually end up owing (boo!) and being owed (yeah!) a significant amount. It feels so arbitrary - honestly like gambling. That's a strange relationship to have with our largest household expense and our fundamental connection to our government?

I expect I'm not alone and that you too, brave reader, have yourself meandered down this murky path from known salary to actual spendable dollars. **The complexity has been built up over a century by additions that nobody is willing to subtract, and it serves specific interests at the expense of everyone who has to file a tax return.**

A core thesis of The Tax Refactor is that this even though we've become numb to this complexity, it has real cost (? need to make a stronger case of what that cost is?). And it's time for a refactor.

This essay focuses on one major offender, the deduction architecture, which is a design from over a hundred years ago that should have been refactored decades ago.

The good news: the fix isn't complicated. Replace the standard deduction with a 0% bracket. Replace deductions with credits, which is a more logically coherent design. That's it. Two architectural changes. We'll get to the details. But first, let's look at what we're actually fixing.

## What it takes to compute your tax bill

Let me try to spell out everything you need to know to calculate how much money you ultimately get to keep. I'll be exhaustive on purpose, because the point is exactly that this list is long.

```
Tax = f(
  income,
  filing_status,
  above_the_line_adjustments (Schedule 1),
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

One input. The bracket table is published infrastructure, the same for everyone (like the speed of light, or a tide chart). Everything else in that monstrous list above is design choice, not necessity.

This isn't just my opinion. In [a 2021 survey of 1,000 American adults](https://www.aei.org/economics/survey-confirms-that-many-americans-misunderstand-income-tax-brackets/), 51% incorrectly believed that moving into a higher tax bracket means paying the higher rate on ALL your income. A majority of us don't understand the most basic structural feature of our own income tax. A [literature review of 128 studies on tax misperception](https://www.tandfonline.com/doi/full/10.1080/09638180.2020.1852095) found that this kind of misperception isn't just annoying — it distorts real economic decisions about whether to take a raise, whether to take a side gig, how much to save.

The system is so complex that the people it taxes can't reason about it correctly. That's not a quirk. That's a design failure. And it's one we can fix.

*(One quick note before going further: there's another federal tax called FICA, the payroll tax, that takes 7.65% off the top of every paycheck. FICA is its own architectural issue and deserves its own write up, which is coming. This piece focuses on the income tax.)*

## A grocery store, but for taxes

Does this really matter? I think so. We should know how much money we have to spend so that we can make good decisions (?? let's make this stronger!)

Let's imagine if you needed to endure similar complexity for spending. Imagine you walk into a grocery store. Your total at checkout is $200. Before the cashier swipes your card, she asks:

- Did you donate to charity this year? How much?
- Do you have a mortgage? How much interest did you pay?
- Are your medical expenses more than 7.5% of your annual income?
- How much did you pay in state and local taxes?

If your answers add up to more than $15,750, you get a discount based on your income bracket. If they don't, you get a flat $15,750 discount applied automatically. (? let's be more specific - you're grocery bill is $137 or maybe it's $114 or possible $163)

You'd think the cashier had lost her mind. None of these questions have anything to do with the groceries. But this is essentially what the federal government does every April. We compute your tax bill by asking a series of questions about behaviors that have nothing to do with how much you earned.

## How we ended up here

None of this was designed. It accumulated.

The [1913 income tax](https://legalclarity.org/the-structure-of-the-revenue-act-of-1913/) was built for about 1% of households, mostly people who ran their own businesses. Treating a household like a small business made sense, because it usually was one. You computed net income after the costs of producing income. Interest paid? Deductible. State taxes paid? Deductible. Charitable giving was added in 1917, because back then it was hard to tell where the proprietor ended and the business began.

Then in 1943, withholding was introduced. In 1944, the income tax became a mass tax (4 million filers in 1939, 50 million by the mid-1940s). The IRS had no way to audit fifty million Schedule A forms full of shoebox receipts. So Congress invented the [standard deduction](https://www.thefiscaltimes.com/Columns/2019/07/11/Surprising-History-Standard-Deduction). It was a peace treaty: take this flat number, skip the audit. It wasn't a theory of fairness. It was administrative duct tape.

That duct tape is still there. Eighty years later. Layered with new deductions Congress has added every decade since: mortgage interest, medical expenses, SALT, sales tax, educator expenses, student loan interest, and as of last year, four new deductions on a brand new schedule (Schedule 1-A) for tips, overtime, US-assembled car loans, and seniors.

The architecture is a sedimentary record. Each layer is a political moment, frozen in code. Things get added; nothing ever gets removed. (Why this keeps happening is the subject of a future essay.) We're maintaining a 1944 workaround for a problem that no longer exists, while continuing to bolt on new exceptions every time Congress wants to encourage something.

## The fix is two changes

Two architectural moves clean this up. Neither is complicated.

**Change 1:** Replace the standard deduction with a 0% bracket.

The standard deduction is just a 0% tax bracket dressed up as something else. (? should this be the subtitle? feel like we should get to this earlier...) If the standard deduction is $15,750, that's mathematically identical to having a bracket structure where the first $15,750 of income is taxed at 0%. The math is the same. Try it: subtract $15,750 from $50,000, apply the 12% bracket to the result, you get $4,110 in tax. Now apply 0% to the first $15,750 and 12% to the next $34,250: $4,110. Identical.

So why do we have the awkward "subtract this number first" version instead of just putting a 0% row at the top of the bracket table? No good reason. The standard deduction was invented in 1944 as a workaround and never got refactored.

**Change 2:** Replace deductions with credits, which is more logically coherent.

A deduction says: this dollar wasn't income. That makes sense for actual costs of producing income (business expenses, capital losses). It does not make sense for charity, mortgage interest, or state taxes. Those are uses of post-tax money, not adjustments to what counts as income.

When you step back, deductions are apples and income's oranges. You earned $100,000. You gave $5,000 to your church. Your income is still $100,000. The $5,000 is what you *did* with $5,000 of your income. It's not negative income. It's a use of post-tax money, the same way groceries are. We've decided to subsidize one and not the other, and we deliver the subsidy by pretending the donation didn't count as income in the first place. That's a category error. We're using the income-definition mechanism to deliver a behavioral subsidy.

If we want to subsidize charitable giving (and I think we should), there's a cleaner way to do it. More on that in a minute.

A credit is honest. It says: the government will pay a percentage of your gift as a public match. Whether to offer the match at all, and at what rate, are political questions worth debating. But the architecture is principled either way. A flat-rate credit treats every citizen's contribution to the public good the same. A deduction treats the wealthy person's charitable preferences as worth more than the teacher's.

Consider the math. Under current law, a teacher in the 12% bracket giving $1,000 to her church gets nothing back (because she takes the standard deduction, like 86% of filers do). A hedge fund manager in the 37% bracket giving $1,000 to his alma mater gets $370 back. The federal government values the hedge fund manager's preferences at $370 per gift and the teacher's at $0. That's not a policy anyone would design from scratch. It's just what we ended up with.

How the credits should actually work (what rate, which behaviors qualify, whether they're refundable) is a separate design question. The architectural point stands either way: deductions are the wrong tool for delivering behavioral subsidies. They were the wrong tool in 1913 and they're the wrong tool now.

Half the developed world has already cleaned this up. Estonia, Sweden, the Netherlands, the UK, Canada — none of them run a "standard vs. itemized" decision tree for their citizens. They apply the bracket table to income. Subsidies for behaviors they care about live elsewhere, as credits or direct payments. These are not radical countries. They've just made different design choices.

How we'd actually rebuild this for the United States (new brackets, new credit rates, transition mechanics for things like the mortgage interest deduction without crashing the housing market) is the subject of the income tax reform proposal coming later in this series.

## The easy button

Picture next April. You sit down with your phone. An app shows you: "Your income for 2026 was $X. Your tax is $Y. Tap to confirm." You tap. You're done. No TurboTax. No slot machine. No bunching strategies. No "do I itemize?" No wondering if you should call your accountant.

That's not utopian. That's the system Estonia has had for fifteen years. That's the system Sweden has. That's the system the UK has for most filers. The technical infrastructure already exists. The IRS could build a version of this with the data they already have.

The only thing standing between us and that experience is a hundred and ten years of sedimentary deduction layers that nobody has been willing to refactor. They were each added for a reason that made sense at the time. They've been kept because no one wants to be the politician who took something away. But the cost is real, and it falls on every American who tries to plan a financial decision and can't get a straight answer about what it will cost them.

For most of us, tax should be `f(income)`. The other eleven inputs are a mistake we've been making since 1913. We can stop.
