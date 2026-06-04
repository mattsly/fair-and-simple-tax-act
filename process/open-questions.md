# Open Questions

Unresolved questions surfaced during development but not yet settled. These are the things worth revisiting when the project gets its next round of attention.

## Credit Mechanics

### Charitable credit calibration (50% credit, 5% liability cap)
Numbers are decided as the stake in the ground (per `decisions-log.md`). Calibration validation still open: no donor-behavior modeling has been done to test whether the 50%/5% pair optimally balances incentive strength against the zero-out-your-taxes abuse pattern. The numbers may need to move once empirical modeling exists.

### Medical credit calibration (30% refundable, $5K threshold)
Numbers are decided as the stake in the ground (per `decisions-log.md`). Open work distinct from the structural choice: should the threshold scale with income or household size? Should the percentage phase up for very large expenses (e.g., 30% below $50K, 50% above)? How does the credit interact with ACA subsidies, which remain in place?

## Receipt Tracking & Compliance Burden

### Charitable giving still requires receipt tracking
One of the pitches of the framework is drastic simplification for ordinary filers. But if the charitable credit exists, so does the receipt-tracking apparatus that makes charitable deductions annoying today. We haven't resolved how to keep the credit without recreating the paperwork.

### Medical receipts too
Same problem, larger scale. Medical receipts are messier than charitable (EOBs, HSAs, pharmacy receipts, dental, vision). If we retain a medical credit, we retain the substantiation problem. Is there a way to piggyback on existing insurer/provider reporting (1095 forms, etc.) to avoid pushing the burden onto filers?

## USA / Savings Account Overlap

*Resolved June 2026 — see `decisions-log.md`. The USA medical / Phase 2 medical credit double-dip is settled (no stacking; USA-paid dollars excluded from the credit base, mirroring current HSA rules). Remaining sub-issue — medical receipt substantiation mechanism — folded into the general "Receipt Tracking & Compliance Burden" item above.*

## Lifetime Gains Framework

### Gift tax as a separate tax type: keep or repeal?
The LGF essay treats gifts as cap-gains realization events (donor pays tax on unrealized gains at transfer). It also retains the $19K annual cash gift exclusion and eliminates the $13.6M lifetime gift exemption. What's not yet decided: should the gift tax remain a separate tax type at all, or does it collapse entirely once gifts are realization events? The simplification win is removing another layer of the code. The open question is whether anything in the gift tax (gift-splitting, generation-skipping rules, certain trust structures) does work that cap-gains realization alone doesn't.

### Gift valuation problem
Donor/recipient basis tension helps police valuation, but not perfectly. Artwork, private company shares, and illiquid real estate can be gifted at aggressive valuations. We decided to leave it alone for now, but this is the most likely attack vector once the framework is in place.

### Death valuation at scale
IRS qualified appraisal infrastructure exists but is thin. If death becomes the dominant realization event, appraisal demand will spike. Is the capacity there? Should the framework fund appraisal infrastructure?

### Does the lifetime counter follow marriage/divorce cleanly?
Each person has their own $2M exemption. What happens on marriage — do the counters merge? On divorce — do they split? On remarriage — reset, or cumulative?

## Revenue & Modeling

### Revenue range inconsistency ($45-170B in flagship vs. $85-200B in companion docs)
The published flagship essay states $45-170B/year, midpoint ~$108B. Internal docs and several drafts cite $85-200B. Per the source-of-truth rule, the flagship number wins; companion docs should be aligned. The range is also still too wide — needs tighter modeling with explicit scenarios (aggressive avoidance, moderate avoidance, full compliance).

### Interaction effects between components
We've modeled components largely in isolation. When you stack income tax rate table changes with deduction elimination with FICA reform with USA conversion, the interactions are non-trivial. No integrated model yet.

## Structural

### Corporate tax scope-out is convenient but unstable
We've scoped out corporate taxation, but the line between personal and corporate income is exactly where the ultra-wealthy play (pass-throughs, closely-held C-corps, holding companies). Is the scope-out defensible long-term, or a known weakness?

## Legacy Open Questions

*Merged from an older `OpenQuestions.md` brainstorm doc. Some of these may have been resolved since; flagged here so they don't get lost.*

### Is CPI fair to "sweat equity" where the cost basis is $0?
Founders and early employees who take equity instead of salary have a $0 cost basis on their shares. Indexing to CPI doesn't help them the way it helps someone who actually paid for their assets. Is that fair, or does it need a carve-out?

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
