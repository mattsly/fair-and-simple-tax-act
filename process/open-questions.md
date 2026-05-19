# Open Questions

Unresolved questions surfaced during development but not yet settled. These are the things worth revisiting when the project gets its next round of attention.

## Credit Mechanics

### Should the charitable credit cap be 5% of liability, or something else?
Current: 50% of donation, capped at 5% of tax liability. The 5% number is a stake in the ground. Too low and it fails to incentivize giving; too high and it recreates the zero-out-your-taxes abuse pattern. No modeling yet on where real donor behavior sits.

### Is a 30% refundable medical credit with a $5K threshold the right shape?
Current design is a reasonable first cut but untested. Questions: should the threshold scale with income or household size? Should the percentage phase up for very large expenses (e.g., 30% below $50K, 50% above)? How does this interact with ACA subsidies, which remain in place?

### Should medical and charitable credits share exact mechanical structure?
Decided for now that they should *not* — charitable is voluntary incentive (cap on liability), medical is involuntary protection (refundability essential). But the parallel framing might be stronger if we found a way to make the mechanics match. Worth revisiting if someone finds a clean unified form.

## Receipt Tracking & Compliance Burden

### Charitable giving still requires receipt tracking
One of the pitches of the framework is drastic simplification for ordinary filers. But if the charitable credit exists, so does the receipt-tracking apparatus that makes charitable deductions annoying today. We haven't resolved how to keep the credit without recreating the paperwork.

### Medical receipts too
Same problem, larger scale. Medical receipts are messier than charitable (EOBs, HSAs, pharmacy receipts, dental, vision). If we retain a medical credit, we retain the substantiation problem. Is there a way to piggyback on existing insurer/provider reporting (1095 forms, etc.) to avoid pushing the burden onto filers?

## USA / Savings Account Overlap

### USA qualified medical withdrawals overlap with the medical cost credit
USA withdrawals for qualified medical expenses are tax-free. The medical credit provides a 30% refundable credit above a $5K threshold. A filer could conceivably get both benefits on the same dollar of spending. Need to specify the interaction rule: can't double-dip, first-dollar rule, or something cleaner.

### Should the USA balance cap be $5M or indexed?
$5M is the current stake in the ground. Not indexed. Over 40-year working lives with inflation, this cap compresses hard. Do we index, or do we treat the cap as deliberately non-indexed to prevent the account from becoming a dynastic vehicle?

### What happens to USA balances at death?
Not yet specified. Does the balance transfer to heirs' USAs? Get forced out and taxed? Inherited with stepped-up basis (which would contradict the Lifetime Gains death-as-realization principle)?

## Lifetime Gains Framework

### Gift tax interaction with Lifetime Capital Gains framework
The framework states "gifts trigger realization" but doesn't address the existing gift tax structure. Key questions to resolve:

1. **Annual exclusion for cash gifts** — probably keep as-is ($18K/year). Cash is already-taxed dollars, no unrealized gain to realize. Non-issue.

2. **Annual exclusion for appreciated-asset gifts** — need a de minimis threshold so small transfers (e.g., giving a grandkid shares of stock) don't trigger realization. Proposed range: $25K–$50K/year in appreciated assets before realization kicks in. Threshold TBD.

3. **Lifetime gift exemption (~$13.6M)** — likely redundant and can be eliminated. Its purpose (tax-free lifetime wealth transfer) is already handled by the $5M couple lifetime capital gains exemption. Two parallel lifetime exclusion systems is unnecessary complexity.

4. **Gift tax as a separate tax** — if appreciated-asset gifts trigger capital gains realization, the gift tax itself may be eliminable. Gain gets recognized and taxed at transfer. This would be a simplification win — removes another layer of the code.

**Decision needed:** Confirm de minimis threshold for appreciated-asset gifts, and whether gift tax is fully replaced by realization trigger or retained in modified form.

### Gift valuation problem
Donor/recipient basis tension helps police valuation, but not perfectly. Artwork, private company shares, and illiquid real estate can be gifted at aggressive valuations. We decided to leave it alone for now, but this is the most likely attack vector once the framework is in place.

### Death valuation at scale
IRS qualified appraisal infrastructure exists but is thin. If death becomes the dominant realization event, appraisal demand will spike. Is the capacity there? Should the framework fund appraisal infrastructure?

### Does the lifetime counter follow marriage/divorce cleanly?
Each person has their own $2.5M exemption. What happens on marriage — do the counters merge? On divorce — do they split? On remarriage — reset, or cumulative?

## Revenue & Modeling

### $85-200B annual revenue range is too wide
The range reflects genuine uncertainty but is so wide it's easy to attack. Need tighter modeling, probably with explicit scenarios (aggressive avoidance, moderate avoidance, full compliance).

### Interaction effects between components
We've modeled components largely in isolation. When you stack income tax rate table changes with deduction elimination with FICA reform with USA conversion, the interactions are non-trivial. No integrated model yet.

## Political & Strategic

### Who is the audience?
The op-ed pitches the framework as a critique of Warren's wealth tax. That positions it in the progressive policy conversation. But the "kill deductions, flatten the code" language codes libertarian. Is this deliberately cross-partisan, or do we pick a lane?

### Is the renaming from "Fair and Simple Tax Act" to "Simple and Fair Tax Project" final?
Pending URL migration. The word "Act" implies legislation; "Project" is more honest about what this is. But "Act" is catchier.

## Structural

### Should the Lifetime Gains framework eventually replace the AMT explicitly, or just make it vestigial?
Current framing eliminates the AMT. Is that a separate legislative ask, or does it fall out automatically once deductions are gone and the AMT has nothing to claw back?

### Corporate tax scope-out is convenient but unstable
We've scoped out corporate taxation, but the line between personal and corporate income is exactly where the ultra-wealthy play (pass-throughs, closely-held C-corps, holding companies). Is the scope-out defensible long-term, or a known weakness?

## Legacy Open Questions

*Merged from an older `OpenQuestions.md` brainstorm doc. Some of these may have been resolved since; flagged here so they don't get lost.*

### Is CPI fair to "sweat equity" where the cost basis is $0?
Founders and early employees who take equity instead of salary have a $0 cost basis on their shares. Indexing to CPI doesn't help them the way it helps someone who actually paid for their assets. Is that fair, or does it need a carve-out?

### Is the framework meaningfully better than the estate tax once buy-borrow-die is closed?
Once death triggers realization and loans count as realization events, the main dynastic-wealth exits are closed. At that point, what is the Lifetime Gains Framework adding on top of a well-enforced estate tax? This is worth answering cleanly because the honest answer ("a lot simpler, a lot more enforceable, and it also catches in-life wealth transfers") is a feature.

### K-1 income treatment
Pass-through income via K-1s is where a lot of the ultra-wealthy actually get paid. How does the framework handle K-1 distributions vs. the Phase 2 Market Compensation Requirement?

### International tax interaction
US citizens abroad, foreign investors in US assets, treaty implications. Not addressed anywhere in the current framework.

### Philosophy clarity
Is the underlying philosophy (simplicity > targeted fairness, systems > patches, closing exits > raising rates) communicated clearly enough in the current essays, or is it getting lost in the mechanics?

### If death triggers realization, are we effectively keeping the estate tax by another name?
Somewhat yes — but the framing matters. Estate tax is a separate tax type with its own threshold, rules, and workarounds. Death-as-realization is the same rule applied to every life event. Worth making this contrast explicit in the essays.

### VC / Silicon Valley objection: "don't punish repeat success"
The likely pushback from VCs and serial founders is: "why should my prior success raise my rates? You're punishing the people who start multiple companies." Response elements worth developing:
- Existing wealth is a massive de-risker; starting a company when you already have $50M is structurally safer than starting one with $50K in savings.
- Empirical claim worth checking: founders who are already wealthy don't pull back from starting new companies at the margin when tax rates rise.
- Luck is a much bigger factor in outlier success than the VC narrative admits (there's data on this — worth citing).
- Even at phased-up rates, successful entrepreneurs still make a lot of money. The framework caps the rate of compounding advantage, not the upside.

### Payment flexibility for illiquid assets — section placement
Should the "payment flexibility for illiquid assets" FAQ move into the Practical Concerns section, next to the related FAQ? Currently separated.
