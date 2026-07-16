# Open Questions

Unresolved questions surfaced during development but not yet settled. These are the things worth revisiting when the project gets its next round of attention.

## Credit Mechanics

### Charitable credit calibration (50% credit, 5% liability cap)
Numbers are decided as the stake in the ground (per `decisions-log.md`). Calibration validation still open: no donor-behavior modeling has been done to test whether the 50%/5% pair optimally balances incentive strength against the zero-out-your-taxes abuse pattern. The numbers may need to move once empirical modeling exists.

### Charitable credit base for appreciated assets: FMV or basis? (deferred from LGF flagship, June 2026)
The LGF essay punts on this (see `decisions-log.md`): it keeps the status quo FMV deduction for gifts of appreciated assets and hands the reform to the charitable-giving companion proposal. The open question for that proposal: when the charitable deduction becomes a credit (income-tax essay: 25% credit, 3% liability cap), should the credit base for appreciated assets equal **fair market value** or the donor's **basis**? Current lean: **FMV** — it matches the donor's actual sacrifice and the charity's actual benefit, and aligns with current law plus Canada/UK norms. Flagged to reconsider: the basis version is the progressive / Madoff-aligned alternative that stops donors from getting credit on never-taxed appreciation. Entangled with the DAF/foundation warehousing problem (no-payout DAFs, 5% foundation payout) the companion proposal must also resolve.

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

## USA Room Accrual

### Room accrual start: birth or age 18?
Room banking is decided (see decisions-log, July 2026); the accrual start date is not. From birth is consistent with the $1K seed and gifts-to-kids fundability, but lets well-off parents shelter $540K per child by 18 (partially blunted by the fact that capacity is equal for all kids and unused room banks for the poor kid's later use). Age 18 is Canada's rule and kills the optics problem, but then kid-directed gifts (Dell, Shotwell) need their own room source — a carve-out, which is its own smell. Related: new citizens/residents should accrue from arrival, not birth; define "arrival" (residency? citizenship? visa class?).

## Social Security Interaction (for the FICA/SS essay)

### USA withdrawals are invisible to SS benefit taxation
Because USA withdrawals are tax-free, they don't enter provisional income, so USA retirees escape the existing income-based taxation of SS benefits that Traditional-401(k) retirees face today (mirrors current Roth treatment, but at much larger scale once the USA is the only account). Is that a feature (consistent post-tax design) or a quiet base erosion the FICA/SS essay must address? Note: means-testing SS against USA *balances* is decided-rejected (see decisions-log July 2026); this item is only about the income-side interaction.

## Employer Transition

### Match pass-through: how hard can the conversion rule be?
The USA essay commits to a one-time rule: employers offering a match at enactment must fold its dollar value into base pay. Open design work: what's the base ("dollar value" = trailing-year actual match paid? the formula's expected value?), how it applies to non-matched employees at matching firms, whether small employers get a glide path, and what enforcement looks like (payroll audit? attestation?). Beyond the one-time conversion, pass-through relies on wage visibility and labor-market competition; is that enough, or does the umbrella employer-benefits essay need a stronger mechanism for the later FICA/ESNC transition?

### Interim payroll-tax treatment if USA ships before FICA reform
Converted match dollars paid as wages bear ~15.3% combined FICA that match dollars escape today (~$490/yr on a typical $3,200 match; roughly $9-10B/yr economy-wide). Current lean (July 2026): accept it and say so in the essay — it's small, honest, and Social Security-solvency-positive, and the match's FICA exemption was a loophole. Rejected for now: a sunsetting FICA exclusion for payroll-routed USA deposits (invites relabeling wages as "contributions" — an 8% ESNC dodge worth ~$2,400/employee/yr at the $30K cap once ESNC exists); making FICA reform a prerequisite (breaks modularity). Revisit if employer-side politics demand a sweetener.

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
