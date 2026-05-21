# The Deduction Hack

*Computing your tax bill takes about a dozen inputs. It should take one. We've been maintaining the bug since 1913.*

---

Every time I've started a new job, my first paycheck's take-home amount is a surprise. The gross pay matches what I expected (salary divided by 26). But the take-home is that gross minus a tangle of withholdings: federal income tax, Social Security, Medicare, state tax, maybe local tax, a 401(k), pre-tax health insurance, an FSA, an HSA.

We've all gotten numb to this, but step back and it's a little crazy: the money we actually keep for our labor feels...kinda random.

Then there's tax season. Sit down with tax software, click buttons, type in numbers, and the balance flips between red (owe) and green (refund) like a slot machine. It's a strange way to relate to what is, for many, our largest annual expense and the price of the government we share.

A core thesis of [The Tax Refactor](https://taxrefactor.substack.com/) is that this complexity has a real price: wasted hours, distorted decisions, and a thumb on the scale for the wealthy. This essay focuses on one major offender: the deduction architecture of the federal tax code. The idea of taking deductions - subtracting values from gross income and then using that difference to calculate your tax liability - is a remnant from over a hundred years ago. And when you start to pull at the thread of what deductions we take and why, you find that building deductions into the individual tax return is unnecessarily complex, illogical, and quietly regressive.

*(Two quick boundaries. This post is about the federal income tax, not FICA, the payroll tax that skims another 7.65% off every paycheck (its own mess, its own essay). And I'm writing for the typical W-2 wage earner, the vast majority of filers, whose tax is auto-withheld and whose salary is a clean, knowable number. The self-employed are a different animal, with real business costs to net out, and get their own treatment elsewhere.)*

The good news: the fix is two "code" changes:

1. **The architectural refactor:** stop using deductions to hand out subsidies; deliver those as credits instead.
2. **The UI cleanup:** once itemizing is gone, the standard deduction turns out to have been a plain 0% bracket all along.

We'll get to the details. But first, let's look at what we're actually fixing.

## What it takes to compute your tax bill

It's true that with patience and a spreadsheet, you *could* work out the federal income tax behind your take-home yourself. Here's "all" it takes:

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
One input. You look your income up in the bracket table, and that's your tax. Everything else in that massive list above is a design choice, not a necessity.

## A grocery store, but for taxes

Does it matter that you can't pin down your own take-home pay? I think it does. The average household [spends more on taxes than on food and clothing combined](https://reason.com/2022/09/12/americans-spent-more-on-taxes-last-year-than-on-food-health-care-education-and-clothing-combined/), it's about the biggest line item there is. Try budgeting when your largest expense stays a mystery, not just until next April, but in every paycheck along the way.

Imagine groceries worked this way. You fill a cart, and at checkout, before she swipes your card, the cashier asks:

- Did you donate to charity this year? How much?
- Do you have a mortgage? How much interest did you pay?
- Are your medical expenses more than 7.5% of your annual income?
- How much did you pay in state and local taxes?

Your answers set your discount. So picture two shoppers with identical $200 carts. The first has a big mortgage, a generous year of giving, and a stack of state tax payments; she walks out paying $137. The second, a renter who gave to his church but didn't clear the threshold, takes the automatic discount and pays $163. Same groceries, different price, the only variable being their answers to a quiz about their personal lives.

You'd think the cashier had lost her mind -- none of these questions have anything to do with groceries. But that's exactly what we've done to ourselves on the income side of our family ledgers: our take-home is determined based on a quiz about behaviors that have nothing to do with what we earned. Apples, meet oranges. (I'm just going to dwell on the grocery visual just long enough to get that in 😒)

## How we ended up here

None of this was designed, it accumulated. And the accumulation left a root bug: the tax code can't decide whether it taxes your *gross* income or your *net* income. It started as one, drifted toward the other, and never finished the trip.

The [1913 income tax](https://legalclarity.org/the-structure-of-the-revenue-act-of-1913/) exempted the first $3,000 of income (about $95,000 today, which was, ahem, a 0% bracket), so only the richest 2% of households owed anything: 358,000 returns. And those people mostly didn't live on a wage. They lived off *ownership*: business profits, farm income, dividends, interest, rents. For income that comes from owning things, "income" naturally means *net* income, what's left after the cost of earning it, so building the tax around net made sense. The handful who paid it genuinely had costs to subtract. A wage earner doesn't. A salary is already clean.

Then the tax went from a rich-person's levy to nearly everyone's, to pay for World War II, and broadening it was the right call: a country at war needs broad-based revenue. Filers jumped from about 4 million in 1939 to 50 million by 1945. But it created a contradiction. **Withholding, which arrived in 1943, computes your tax on gross pay, because your employer can't possibly know your charitable gifts or medical bills.** The moment we began withholding from tens of millions of paychecks, we were taxing gross income while still pretending, through deductions, to tax net. The honest move was to commit to gross. Instead, with no way to audit fifty million Schedule A forms full of shoebox receipts, Congress reached for the [standard deduction](https://www.thefiscaltimes.com/Columns/2019/07/11/Surprising-History-Standard-Deduction): a flat number, skip the receipts. As wartime triage it was reasonable; the laziness was never finishing the job. We've been stuck in the muddy in-between ever since, taxing gross minus a grab-bag of leftover subtractions.

To be fair, deductions aren't crazy on their own terms. There's a real argument, made by the tax scholar William Andrews [in 1972](https://www.jstor.org/stable/1339894), that a dollar which was never really your income shouldn't be taxed in the first place, which is exactly why a business subtracts its costs before reporting profit. The catch is that almost nothing we now deduct is a cost of *earning* income; it's things we do *with* income. (Whether a gift the government partly funds is even "yours" is a deeper question for another day.) And even where the logic does hold, today's system botches it, handing the benefit only to itemizers when it should apply to everyone.

So we kept the machinery of the old net-income paradigm and stuffed it with subsidies: mortgage interest, medical expenses, SALT, educator expenses, student loan interest, and as of last year, four new ones on a brand-new Schedule 1-A for tips, overtime, US-assembled car loans, and seniors. We're overloading a hack that should have been deprecated in the 1940s.

## It's not just confusing — it's rigged toward the rich

The grocery store already made the confusion vivid. But confusion isn't the real damage. This is:

A deduction shrinks your taxable income, so what it's worth depends on your top tax rate. Take the same $1,000 gift to charity. A teacher in the 12% bracket gets nothing back, because she takes the standard deduction, like [about 90% of filers do](https://taxpolicycenter.org/briefing-book/what-are-itemized-deductions-and-who-claims-them). A hedge-fund manager in the 37% bracket gets $370. Same gift, same public good, but the federal government values his generosity at $370 and hers at $0. A deduction quietly says a rich person's charitable impulse is worth more than a teacher's. A flat credit fixes it in one move: every $1,000 gift earns the same match, itemizer or not.

Not a quirk. A design failure. And one we can fix.

## The fix: an architectural refactor, then a UI cleanup

Two changes. The first does the real work, and people will feel it. The second is a cosmetic payoff that, once the first is done, falls out for free.

**Change 1 (the architectural refactor): scrap deductions as a way to hand out subsidies, and the itemize-or-not decision with them.**

Not every deduction is the same animal, and the difference is the whole game. Sort them into three piles:

- **Deductions that *define* income** (the costs of running a business, netted on Schedule C; capital losses; and for the self-employed, things like half of the self-employment tax). These aren't favors; they're how you measure income correctly in the first place. They stay. For a typical wage earner this pile is empty anyway, your salary is already a clean number, which is why we set the self-employed aside earlier.
- **Deductions that *subsidize* a behavior** (mortgage interest, charity, SALT, student loan interest, last year's new tips/overtime/car-loan/senior breaks). These are the problem. These should become credits.
- **Tax-deferred saving** (traditional IRAs and the like). This is a subsidy too, but a different kind, it rewards the *timing* of saving rather than rebating a purchase, so a credit doesn't map cleanly onto it. Leave it for now; a future essay argues the whole retirement-savings tangle, IRAs, 401(k)s, HSAs, should collapse into a single Universal Savings Account.

The middle pile is where the design goes wrong. A deduction says: this dollar wasn't income. That's true for the cost of earning income, but it's a fiction for charity, mortgage interest, or state taxes. If you earn $100,000 and give $5,000 to your church, your income is still $100,000, the gift is something you *did* with your money, not a cut in what you made. Treating it as negative income is a category error: we're using the income-definition mechanism to hand out a behavioral subsidy.

There's a structural problem too. Deductions are tightly coupled: you can't judge any single one on its own, because you have to add them all up just to know whether to itemize at all. Credits are modular, each stands alone, gets claimed on its own, and can be reported by a third party without reference to any other. The tax code already runs clean microservices like this, your 401(k) is one: handled at the paycheck, reported on your W-2, never part of the itemize calculus. Deductions are the tangled legacy module that never got refactored.

If we want to subsidize charitable giving (and I think we should), a credit is the honest way to do it: the government matches a set percentage of your gift, the same percentage for everyone. That also erases the regressivity from Problem 1, the teacher and the hedge-fund manager finally get the same deal on the same gift (the higher earner can still give more, which is fine).

Which subsidies deserve to exist is a separate fight, and a separate essay. (The swap I'm describing *is* redistributive, unapologetically, I'm just not relitigating each line item here.) The architectural claim is narrow: whatever we subsidize, a credit is the honest way to deliver it. Which subsidies ultimately survive, and at what rate (spoiler: not many), is for the reform proposal later in this series.

Half the developed world has already cleaned this up. The UK, Canada, the Netherlands, Sweden don't make citizens run a "standard vs. itemized" gauntlet at all; they apply the brackets to income and put subsidies elsewhere, as credits or direct payments. In the UK, most people never file a return at all, the system just gets it right. None of these are radical countries, they've just made better design choices.

**Change 2 (the UI cleanup): now look what's left.**

With itemizing gone, there's no "itemize instead" alternative for the standard deduction to anchor, so it isn't really a deduction anymore. It's a 0% bracket. If the figure is $15,750, that's identical to a bracket table where the first $15,750 of income is taxed at 0%. Try it: subtract $15,750 from $50,000, apply the 12% bracket, you get $4,110. Now tax the first $15,750 at 0% and the next $34,250 at 12%: $4,110. Same number.

So drop the awkward "subtract this first" step and put a 0% row at the top of the table. Nobody's bill moves by a penny; you just delete a concept. No "adjusted gross income" to compute before you can read your rate, one table, one lookup. The standard deduction was a 0% bracket the whole time, hiding behind eighty years of paperwork.

How we'd rebuild the rest for the United States (new brackets, new credit rates, transition mechanics for things like the mortgage interest deduction without crashing the housing market) is the subject of the income tax reform proposal coming later in this series.

## The easy button

Picture your next paycheck. You already know the number: salary ÷ 26, minus a rate you can actually see. No surprise. And come April, you open an app: "Your income for 2026 was $X. Your tax is $Y. Tap to confirm." You tap. You're done. No TurboTax, no slot machine, no bunching, no "do I itemize?", no calling your accountant.

That's not utopian, it's roughly what the UK and Canada already do, and the fully-automated version, tap and you're done, has run in even tiny Estonia for fifteen years. The technical infrastructure exists; the IRS could build it with the data it already has.

And the handful of credits we keep don't break this. Your mortgage interest already lands at the IRS on a Form 1098; your charitable gifts could arrive the same way. Each is a self-contained microservice, pre-filled rather than assembled. The ~90% who take the standard deduction get the bare "tap to confirm"; everyone else gets the same screen with a few lines already filled in.

What stands in the way is a hundred and ten years of deduction layers nobody's been willing to refactor, each added for a reason that made sense at the time, each kept because no politician wants to be the one who took something away. But the cost is real, and it lands on everyone trying to make a financial decision who can't get a straight answer about what it'll cost.

For most of us, tax should be `f(income)`. The other eleven inputs are a mistake we've been making since 1913. We can stop.
