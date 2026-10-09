# Revising QSBS (working title)

**Status:** Draft v1, not ready to publish. See Open Questions at bottom.
**Suggested location:** `drafts/qsbs-essay.md`
**Tenets:** 1 (Simplicity), 3 (Climb to middle class), 4 (Innovation)
**Alt titles:** "QSBS: Right Idea, Terrible Code" / "Delete the If-Statements" / "Three Exits, Zero QSBS"
**Related:** `lifetime-gains-essay.md` (published), success-criteria backlog item

---

I've been part of three startup exits. I qualified for QSBS zero times.

(If you don't know what QSBS is, congratulations on your life choices. Stay with me anyway.)

The first was FutureMe, my own company. It was an LLC, like most small businesses, and LLCs don't qualify. The other two were companies where I was an employee. I had stock options, and I didn't hold the shares for five years after exercising them. Almost nobody does. You exercise when you're finally allowed to sell, and you sell. [Matt: confirm details.]

Three bets on startups. Three times the tax code's flagship startup incentive said: not you.

And I got off easy. I know founders who had to pause their company and pay lawyers [$X] to convert from an LLC to a C-corp, just to become eligible for a tax break on a sale that might never happen. [Matt: "guy I know" moment here, with specifics.]

## What QSBS is

Qualified Small Business Stock (Section 1202, if you're into that sort of thing) lets founders and early investors exclude up to $15 million of gains from federal tax, per company. Here's the eligibility test, written the way a programmer would write it:

```
if (entity == C_CORP
    && gross_assets_at_issuance <= 75_000_000
    && !excluded_industry(business)
    && acquired_at_original_issue
    && active_business_test(business)
    && holding_years >= 3) {
  exclude(min(gain, max(15_000_000, 10 * basis))
          * tier(holding_years))  // 50%, 75%, or 100%
}
```

Every one of those lines has a history, a lobbyist, and a shelf of case law.

Line three alone excludes health, law, engineering, architecture, accounting, consulting, athletics, financial services, the performing arts, farming, mining, hotels, restaurants, and any business whose main asset is "the reputation or skill of" its employees.*

*Yes, that's in the statute. If your business is good because your people are good, Congress would prefer you build something else.

## Where it came from

QSBS was born in 1993, tucked into Clinton's deficit reduction bill. That bill raised the top income tax rate to 39.6% and passed without a single Republican vote. QSBS reads like the sweetener: we're raising your taxes, but we still love entrepreneurs. The stated goal was getting capital to small businesses that struggled to raise equity.

Then the rest of the tax code ate it. Capital gains rate cuts in 1997 and 2003 shrank the benefit to almost nothing. From 2003 to 2009, a $10 million QSBS gain saved you about $2,000 compared to a regular capital gain. (Less than the lawyer bill to prove you qualified.)

The 2009 recession brought it back. Congress bumped it to 75%, then 100%, then extended it five times through 2015, mostly retroactively. For stock bought during that stretch, investors could only have known they qualified 42% of the time. The rest was a thank-you note for bets already made. You can't incentivize an investment that already happened.

It went permanent in 2015 and got bigger in 2025.

That's not a product. That's a feature that kept getting shipped, killed, and resurrected by accident.

## Here's the thing: it works

I'd love to tell you QSBS is useless. It isn't.

A new NBER paper by Murillo Campello and Gustavo Junqueira (July 2026) is the most careful look yet at what QSBS actually does. When the full exclusion kicked in, venture capitalists got braver. They became 81% more likely to back pre-commercial startups and 60% more likely to write a company's very first check. Those bets failed 71% more often. But the survivors exited at 131% higher valuations and were twice as likely to become unicorns.

That's what a risk subsidy is supposed to do.

So, a confession. In my Lifetime Gains post, I wrote that the tax rate has never been the binding constraint on transformative innovation. That was too glib. Tax incentives move venture capital. I'll own it.

The bill: about $3 billion a year in lost revenue today, projected to hit $7 billion by 2035.

## But look who it works on

Here's the twist. The entire effect runs through venture funds.

Angels investing their own money? No response. Corporate investors? No response. The authors found 1,187 people who invest both ways, as angels and through VC funds. Same people, same brains. They only change behavior when it's the fund's money.

The explanation is carried interest. A fund manager typically gets about 20% of the upside and none of the downside on money that belongs to someone else. That's an option. A tax break on the upside makes the option worth more, so they swing harder. An angel betting her own savings feels every loss, and a tax break on a hypothetical win doesn't change her math.

Now look at who actually qualifies:

| Who | Gets QSBS? |
|---|---|
| Founders | Yes |
| Very early employees with stock | Yes |
| Later employees with options | No |
| Angels (US individuals) | Yes |
| Institutional investors in VC funds | No |
| Foreign investors in VC funds | No |
| US individuals in VC funds | Yes |
| Fund managers | Yes, including on their carry |

Individuals and families supply only about 10% of the money in VC funds. Pension funds, endowments, and foreign investors supply most of the rest, and they never touch QSBS.

Here's my favorite part. Nobody designed QSBS for Silicon Valley. It happened by accident. Main Street businesses pick LLCs, partly because buyers pay more for them. VC-backed startups pick C-corps for unrelated reasons (their foreign and tax-exempt investors need it). So the one line requiring a C-corp quietly turned a small business incentive into a venture capital incentive.

If that isn't technical debt, I don't know what is.

Tenet 3 of this project is fueling the climb to the middle class. QSBS fuels a climb. Just not mine, and probably not yours.

## And then there are the loopholes

The $15 million cap is per company, per taxpayer. And "taxpayer" turns out to be flexible. Give shares to your relatives, or to a stack of trusts, and each one gets its own cap. Silicon Valley calls this "stacking." One founder reportedly spread shares across at least 12 extended family members. Another, through more than seven of his children, as part of maneuvers that avoided tax on over $150 million of gain.

Meanwhile, the company has to prove its gross assets never crossed the threshold, not even for a single day, before the stock was issued. Good luck reconstructing that from quarterly financials.

And the timing games you'd expect: the NBER paper finds a pile-up of sales at exactly the five-year mark. Founders timing their exits to the tax calendar instead of the business.

## The fix: delete the if-statements

The Lifetime Gains Framework gives every American a $2 million lifetime capital gains exemption ($4 million for a couple). Any asset. Any business structure. Any industry. Above $2 million, the rate phases up gently until it hits the top income tax rate at $6 million.

Here's the eligibility test:

```
exempt(min(gain, 2_000_000 - lifetime_used))
```

That's it. That's the whole thing.

Check it. Maria opens a restaurant. Dev starts a software company. Eight years later each sells with a $5 million gain (single filers):

| | Today | Lifetime Gains |
|---|---|---|
| Maria (restaurant) | ~$1.2 million | ~$416,000 |
| Dev (software, QSBS) | $0 | ~$416,000 |

Maria saves about $780,000. Dev pays about $416,000 he doesn't pay today. That's not a bug I'm hiding. That's the trade: fewer jackpots, more people allowed to play.

(Tax nerds will note that Dev probably sold for less, because buyers pay less for C-corp stock than for an LLC. For a lot of businesses, QSBS mostly cancels out that penalty. Which means we're spending billions on one quirk of the code to undo another quirk of the code. Refactor, anyone?) [See Open Question #1.]

## Yeah, but...

**"You're killing the one carve-out with evidence that it works."**

Fair. It's the strongest objection. Three responses.

First, the paper measures behavior and valuations, not social payoff. There's no cost-benefit analysis in it. A unicorn valuation is a price someone paid, not proof the public got its $3 billion back.

Second, almost any $3 to $7 billion subsidy changes behavior. The question isn't "does it do something?" It's "is this the best thing we could buy with the money?"

Third, if Congress wants to subsidize venture risk-taking, it should do it on purpose and in the open. Not dress it up as help for small business and let it flow to fund managers.

**"You'll hurt venture capital."**

Yes. Probably. Let me be clear-eyed about this.

Because QSBS's cap is per company, a fund manager with carry in 20 qualifying exits can exclude on every one. Under Lifetime Gains, the first good exit uses up the exemption and everything after is ordinary income. That doesn't dent the incentive the NBER paper found. It removes it. Expect fewer bets on pre-commercial companies. Expect fewer failures. Maybe fewer unicorns.

Two things to keep in mind. First, most VC money comes from institutions and foreign investors who never got QSBS, so fund sizes shouldn't change much. The fund managers' appetite for risk will. Second, we've run this experiment. From 2003 to 2009 QSBS was worth essentially nothing. That's when Facebook, YouTube, and Tesla raised their early rounds.

And if I'm wrong, we should know fast. Lifetime Gains should ship with a success metric on early-stage deal counts, and a commitment to revisit if they drop. (More on that in a future post.)

So here's the trade, stated plainly: this proposal gives up some measured venture risk-taking in exchange for broader access to ownership. I think that trade is right. You're allowed to disagree. But that's the actual argument.

**"Won't people game a $2 million exemption?"**

Some will. A consultant could underpay herself for a decade, build a firm, and sell it, turning salary into tax-free gain. That's exactly why QSBS excludes lawyers, doctors, and consultants.

The difference is the size of the leak. The most anyone can ever save under Lifetime Gains by converting salary into gains is about $1.5 million, once, in a lifetime. Under QSBS it's about $3.6 million per company, per person, and repeatable through gifts. A small, bounded leak with no guardrails beats an unbounded leak with seven guardrails.

**"Why not just fix QSBS?"**

Try it. Drop the C-corp requirement. Drop the industry list. Drop the asset cap and the holding tiers. Close the stacking loophole. Congratulations, you've built a universal lifetime exemption. The refactor ends exactly where Lifetime Gains begins. We just set the cap somewhere Treasury can afford.

## Closing time

Maria's restaurant closes for good on a Sunday in March. The new owners are keeping the name. She stacks the chairs one last time, shuts off the walk-in, and drives home to figure out what she owes.

Under today's code, the answer depends on what she chose to build eight years ago.

It shouldn't.

[Matt: alternative ending that circles back to your three exits?]

---

## Open Questions

### Substance

1. **Maria vs. Dev math is not apples to apples.** Polsky & Yale (Part IV) show buyers pay less for C-corp stock than for an LLC because they lose a basis step-up. In their stylized example, full QSBS only brings a C-corp stock sale back to parity with an LLC sale. Options: (a) compare after-tax *proceeds* rather than tax bills, (b) keep tax bills and add the parenthetical above, (c) drop Maria/Dev and lead entirely with the three exits. Current draft does (b).
2. **The megafund concession: is it strong enough, or too strong?** Draft says LGF likely removes the fund-manager incentive. Need a crisper counterfactual than "2003-2009 funded Facebook." Check early-stage deal counts 2003-2009 vs. 2015-2024 before relying on it.
3. **Founder vs. investor response.** The NBER paper studies investors. Is there any evidence on how *founders* respond to capital gains exclusions? Chen & Farre-Mensa (2026) find roughly a 10% firm-birth response to QSBS in eligible sectors. That's the best available support for LGF's entry story. Read it.
4. **LGF deletes Section 1244** (ordinary loss treatment on failed small business stock). If the goal is more people starting businesses, the downside is the bigger lever than the upside. Reconsider in `open-questions.md`.
5. **Labor-to-capital conversion under LGF.** Is "bounded leak" a sufficient answer, or does LGF need a reasonable-compensation rule for service businesses? Check the $1.5M figure against the phase-in math.
6. **Values framing.** Draft argues fairness/ownership, not aggregate growth. Confirm that's the intended claim. The "thousand flowers" growth claim was cut deliberately (cross-country self-employment rates correlate negatively with GDP per capita).
7. **Carried interest.** LGF treats carry how? The essay implies carry loses QSBS. Make sure that's consistent with the published LGF essay.

### Consistency with published essays (source-of-truth rules)

8. **LGF post's innovation claim.** The published Lifetime Gains essay says the tax rate "has never been the binding constraint on transformative innovation." This draft concedes that was too glib. Before publishing: add an update note to the LGF post and log the change in `decisions-log.md`.
9. **QSBS parameters.** Draft uses LGF post's figures ($15M cap, $75M assets, 3/4/5-year tiers). Confirm those are current.

### Facts to verify

10. NBER paper: author names, working paper number (w35418), and exact stat wording (81%, 60%, 71%, 131%, 2x, 1,187 dual-role investors, $3B to $7B by 2035).
11. Polsky & Yale figures: 42% prospective, $2,000 benefit 2003-2009, ~10% individual share of VC commitments, stacking examples.
12. Whether dry cleaning is excluded under 1202(e)(3). If not, "a dry cleaner can qualify but the restaurant next door can't" is a great line.
13. Facebook/YouTube/Tesla early-round dates fall in 2003-2009.
14. Whether OBBBA's 2025 expansion changes the $3B/$7B cost projections.
15. Madoff's stated position (inheritance taxed as income). Worth telling her about this piece either way.

### Production

16. Tables and code blocks on Substack: likely need images.
17. Venue: Substack post first, or cut an 800-word op-ed version (The Hill, Reason)?
18. Length: currently ~1,700 words. Trim target?

## Sources

- Campello & Junqueira, NBER Working Paper w35418 (July 2026)
- Polsky & Yale, "A Critical Evaluation of the Qualified Small Business Stock Exclusion," 42 Va. Tax Rev. 353 (2023): https://digitalcommons.law.uga.edu/fac_artchop/1605
- Chen & Farre-Mensa (2026), cited in Campello & Junqueira (firm-birth response)
- The Lifetime Gains Framework: https://taxrefactor.substack.com/p/the-lifetime-gains-framework
- I.R.C. Section 1202, esp. 1202(e)(3) (excluded industries)