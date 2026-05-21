# The Deduction Hack

*Computing your tax bill takes about a dozen inputs. It should take one. We've been maintaining the bug since 1913.*

---

Every time I start a new job, my first paycheck's take-home is a surprise. The gross matches what I expected (salary divided by 26). The take-home is that gross minus a tangle of withholdings: federal income tax, Social Security, Medicare, state tax, maybe local tax, a 401(k), pre-tax health insurance, an FSA, an HSA.

We've all gotten numb to this, but step back and it's a little crazy: the money we actually keep for our labor feels...kinda random.

Then there's tax season. I sit down with tax software, click buttons, type in numbers, and the total at the top flips between red (owe) and green (refund) like a slot machine. It's a strange way to relate to what is, for many, our largest annual expense and our main connection to the government.

A core thesis of The Tax Refactor is that this complexity carries a real cost. This essay focuses on one major offender: the deduction architecture of the tax code. The idea of taking deductions - subtracting values from gross income and then using that difference to calculate your tax liability - is a remnant from over a hundred years ago. And when you start to pull at the thread of various deductions (starting with the standard deduction) you find that the idea of deductions in a personal tax return is unnecessarily complex, illogical, and quietly regressive.

*(Two quick boundaries. This post is about the federal income tax, not FICA, the payroll tax that skims another 7.65% off every paycheck (its own mess, its own essay). And I'm writing for the typical W-2 wage earner, the vast majority of filers, whose tax is auto-withheld and whose salary is a clean, knowable number. The self-employed are a different animal, with real business costs to net out, and get their own treatment elsewhere.)*

The good news: the fix is two "code" changes:

1. **The UI update:** turn the standard deduction into a 0% tax bracket. That's already what it is, mathematically. It's just cloaked in unnecessary complexity.
2. **The architectural refactor:** stop using deductions to hand out subsidies, and deliver those as credits instead, which, as we'll get to, makes much more sense.

We'll get to the details. But first, let's look at what we're actually fixing.

## What it takes to compute your tax bill

It's true that with patience and a spreadsheet, you *could* compute it yourself. Here's "all" it takes:

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
One input. You look your income up in the bracket table, and that's your tax. Everything else in that monstrous list above is a design choice, not a necessity.

## A grocery store, but for taxes

Does it matter that you can't pin down your own take-home pay? I think it does. The average household [spends more on taxes than on food and clothing combined](https://reason.com/2022/09/12/americans-spent-more-on-taxes-last-year-than-on-food-health-care-education-and-clothing-combined/), it's about the biggest line item there is. Try budgeting when your largest expense stays a mystery, not just until next April, but in every paycheck along the way.

Imagine groceries worked this way. You fill a cart, and at checkout, before she swipes your card, the cashier asks:

- Did you donate to charity this year? How much?
- Do you have a mortgage? How much interest did you pay?
- Are your medical expenses more than 7.5% of your annual income?
- How much did you pay in state and local taxes?

Your answers set your discount. So picture two shoppers with identical $200 carts. The first has a big mortgage, a generous year of giving, and a stack of state tax payments; she walks out paying $137. The second, a renter who gave to his church but didn't clear the threshold, takes the automatic discount and pays $163. Same groceries, different price, the only variable being their answers to a quiz about their personal lives.

You'd think the cashier had lost her mind, none of these questions have anything to do with groceries. But that's exactly what we've done to ourselves on the income side of the ledger: we work out our take-home by answering a quiz about behaviors that have nothing to do with what we earned. Apples, meet oranges. 😒

## Sure it's confusing, but is this really that bad?

**Problem 1: it's worth more to you the richer you are.** A deduction shrinks your taxable income, so what it's worth depends on your top tax rate. Take the same $1,000 gift to charity. A teacher in the 12% bracket gets nothing back, because she takes the standard deduction, like [about 90% of filers do](https://taxpolicycenter.org/briefing-book/what-are-itemized-deductions-and-who-claims-them). A hedge-fund manager in the 37% bracket gets $370. Same gift, same public good, but the federal government values his generosity at $370 and hers at $0. A deduction quietly says a rich person's charitable impulse is worth more than a teacher's, which is a frankly aristocratic thing for a tax code to say. A flat credit fixes it in one move: every $1,000 gift earns the same match, itemizer or not.

**Problem 2: you can't tell whether your own choices "count."** Now decide whether to give that $1,000. Does the government chip in? You can't know, it depends on whether your itemized deductions will top the standard deduction ($15,750 single, $31,500 married) after a year of expenses you haven't had yet. The simplest question, "what will this gift cost me?", has no answer when you'd want it. And the fog reaches past the ~10% who itemize, since nobody knows in advance which side they'll land on. A credit erases it: the match is the same either way.

**Problem 3: it pays people to rearrange their lives for zero value.** The only way to beat the standard deduction is to pile enough itemizable spending into one year, so people do, bunching two years of charitable gifts together, timing medical procedures, prepaying property taxes before December 31. Donor-advised funds, now holding over [$300 billion](https://www.dafresearchcollaborative.org/annual-daf-report/2025), exist largely to game this: park a lump sum for the deduction now, dole it out to charities later. None of it produces an extra dollar of giving. It's pure effort to outwit a threshold, and a credit (claimable whether or not you itemize) makes the whole game pointless.

**The best case for keeping it this way.** Deductions have a serious defender, and it isn't "the rich deserve more." It's that the deducted dollar was never really income. The tax scholar William Andrews [argued in 1972](https://www.jstor.org/stable/1339894) that income should count only what you consume or save for yourself, and a dollar you give away is neither, so excluding it isn't a favor, it's correct measurement. And if the dollar shouldn't be taxed at all, returning it at your own marginal rate is the only coherent answer; a flat credit would over-credit the teacher and under-credit the manager relative to what each would otherwise owe. By that logic the regressivity isn't favoritism, just a progressive rate schedule on a correctly-measured base.

It's a real argument, and it wins for the deductions that genuinely aren't discretionary, a catastrophic medical bill, or state taxes you were forced to pay. But charity is contestable (most economists treat giving as a chosen preference), and the mortgage on your own home isn't income measurement by any theory, it's consumption. And here's the tell: if measurement were the point, the teacher's gift would cut *her* income too, she'd get her 12%. She gets zero. Today's rule gives itemizers their full marginal-rate benefit and everyone else nothing, satisfying neither theory. It's the worst of both.

The fog and the bunching land hardest on people near the itemize threshold; the regressivity lands on everyone who gives a dollar. Put them together and this isn't a quirky inconvenience. It's a design failure. And it's one we can fix.

## How we ended up here

None of this was designed. It accumulated.

The [1913 income tax](https://legalclarity.org/the-structure-of-the-revenue-act-of-1913/) was never meant for regular people. It exempted the first $3,000 of income (about $95,000 in today's dollars), so only the richest 2% of households owed anything: just 358,000 returns. And those people mostly didn't live on a wage. They lived off *ownership*: business profits, farm income, dividends, interest, rents. For income that comes from owning things, "income" naturally means *net* income, what's left after the cost of earning it. So building the tax around net income made sense, because the few people who paid it genuinely had costs to subtract. A wage earner doesn't. A salary is already a clean number.

Then the system swallowed everyone, to pay for World War II. In 1943, withholding arrived (your employer started sending the government a cut of every paycheck). Returns exploded from fewer than 4 million in 1939, about 3% of the population, to roughly 50 million by 1945, more than a third of it. The IRS suddenly had no way to audit fifty million Schedule A forms stuffed with shoebox receipts. So Congress invented the [standard deduction](https://www.thefiscaltimes.com/Columns/2019/07/11/Surprising-History-Standard-Deduction): take this flat number, skip the receipts. It wasn't a theory of fairness. It was administrative duct tape. But it quietly changed what we tax, from *net* household income to something much closer to *gross*.

That duct tape is still there. Eighty years later. Layered with new deductions Congress has added every decade since: mortgage interest, medical expenses, SALT, sales tax, educator expenses, student loan interest, and as of last year, four new deductions on a brand new schedule (Schedule 1-A) for tips, overtime, US-assembled car loans, and seniors.

The architecture is a sedimentary record. Each layer is a political moment, frozen in code. Things get added; nothing ever gets removed. (Why this keeps happening is the subject of a future essay.) We're maintaining a 1944 workaround for a problem that no longer exists, while continuing to bolt on new exceptions every time Congress wants to encourage something.

## The fix: a UI update and an architectural refactor

Two changes clean this up. One of them nobody will feel. The other, people will definitely feel, because making the swap means giving up the ability to itemize. That one's the whole ballgame.

**Change 1 (the UI update): turn the standard deduction into a 0% bracket.**

The standard deduction is just a 0% tax bracket wearing a disguise. If it's $15,750, that's identical to a bracket table where the first $15,750 of income is taxed at 0%. Try it: subtract $15,750 from $50,000, apply the 12% bracket, you get $4,110. Now tax the first $15,750 at 0% and the next $34,250 at 12%: $4,110. Same number.

So why keep the awkward "subtract this first" version instead of putting a 0% row at the top of the table? No good reason, except that's how it got jury-rigged in 1944. This change moves nobody's bill by a penny; it just deletes a step. Today you subtract the standard deduction to reach your "adjusted gross income" before you can even read the bracket table. A 0% bracket means one table, one lookup. (And once Change 2 kills itemizing, the whole "should I itemize?" question goes away too.)

**Change 2 (the architectural refactor): stop using deductions to hand out subsidies, and deliver them as credits instead.**

Not every deduction is the same animal, and the difference is the whole game. Sort them into three piles:

- **Deductions that *define* income** (business expenses, capital losses, and for the self-employed, things like half of the self-employment tax). These aren't favors; they're how you measure income correctly in the first place. They stay. For a typical wage earner this pile is empty anyway, your salary is already a clean number, which is why we set the self-employed aside earlier.
- **Deductions that *subsidize* a behavior** (mortgage interest, charity, SALT, student loan interest, last year's new tips/overtime/car-loan/senior breaks). These are the problem. These become credits.
- **Tax-deferred saving** (traditional IRAs and the like). Not really a subsidy, it shifts *when* income is taxed, not whether, you pay on the way out instead of the way in. Leave it for now, though a future essay argues the whole retirement-savings tangle, IRAs, 401(k)s, HSAs, should collapse into a single Universal Savings Account.

The middle pile is where the design goes wrong. A deduction says: this dollar wasn't income. That's true for the cost of earning income, but it's a fiction for charity, mortgage interest, or state taxes. If you earn $100,000 and give $5,000 to your church, your income is still $100,000, the gift is something you *did* with your money, not a cut in what you made. Treating it as negative income is a category error: we're using the income-definition mechanism to hand out a behavioral subsidy.

If we want to subsidize charitable giving (and I think we should), a credit is the honest way to do it. It says: the government matches a set percentage of your gift, the same percentage for everyone. That also erases the regressivity from Problem 1, the teacher and the hedge-fund manager finally get the same deal.

Which subsidies deserve to exist is a separate fight, and a separate essay. (The swap I'm describing *is* redistributive, unapologetically, I'm just not relitigating each line item here.) The architectural claim is narrow: whatever we subsidize, a credit is the honest way to deliver it. So: take every subsidy we now route through a deduction (mortgage interest, charity, SALT, all of them) and re-express it as a credit, same list for now. Yes, that shifts value from high-bracket itemizers toward everyone else, that's the point, not a side effect to apologize for. Which subsidies ultimately survive, and at what rate, is for the reform proposal later in this series.

Half the developed world has already cleaned this up. Estonia, Sweden, the Netherlands, the UK, Canada don't make citizens run a "standard vs. itemized" gauntlet at all; they apply the brackets to income and put subsidies elsewhere, as credits or direct payments. Australia draws the line even more pointedly, almost a mirror image of ours: Australians deduct the real costs of earning income (work tools, work travel, a uniform, interest on a loan that produces taxable rent) but get nothing for the mortgage on the home they live in. We do it backwards, deducting the interest on the home you live in (not a cost of earning a dime) but not, under current law, the tools your job demands (a real one). They deduct the costs of earning; we deduct a grab bag. (Australia still deducts charitable gifts, so it's not pure, but the housing contrast is stark.) None of these are radical countries, they've just made better design choices.

How we'd actually rebuild this for the United States (new brackets, new credit rates, transition mechanics for things like the mortgage interest deduction without crashing the housing market) is the subject of the income tax reform proposal coming later in this series.

## The easy button

Picture next April. You sit down with your phone. An app shows you: "Your income for 2026 was $X. Your tax is $Y. Tap to confirm." You tap. You're done. No TurboTax. No slot machine. No bunching strategies. No "do I itemize?" No wondering if you should call your accountant.

That's not utopian, it's roughly what Estonia, Sweden, and the UK already do. The technical infrastructure exists; the IRS could build it with the data it already has.

And the handful of credits we keep don't break this. Your mortgage interest already lands at the IRS on a Form 1098; your charitable gifts could arrive the same way. So even for the minority who use them, the credits show up pre-filled, you confirm a number instead of assembling one. The roughly 90% who take the standard deduction today get the bare "tap to confirm." Everyone else gets the same screen with a few extra lines already filled in.

What stands in the way is a hundred and ten years of deduction layers nobody's been willing to refactor, each added for a reason that made sense at the time, each kept because no politician wants to be the one who took something away. But the cost is real, and it lands on everyone trying to make a financial decision who can't get a straight answer about what it'll cost.

For most of us, tax should be `f(income)`. The other eleven inputs are a mistake we've been making since 1913. We can stop.
