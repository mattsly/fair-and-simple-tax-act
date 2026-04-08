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
