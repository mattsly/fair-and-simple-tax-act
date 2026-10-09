# Backlog: Tax Provisions Need Success Criteria (and a Kill Switch)

**Status:** Idea / pre-draft
**Merge candidate:** "Tax Code Needs Product Management" (Part 1 backlog). Likely the same essay; this is its sharpest angle.
**Tenets:** 1 (Radical simplicity), 2 (Fiscal durability)

## Core thesis

Software products ship with success criteria, get measured against them, and get deprecated when they don't move the needle. Tax provisions ship with none of the three. The result is a code full of "stuff" whose purpose nobody can state with precision. Best practice for tax code product design: every provision ships with a stated objective, metrics, an owner, and a sunset that defaults to *off*.

## Lead examples

| Provision | Failure mode | Detail |
|---|---|---|
| QSBS (Sec. 1202) | No clear purpose | Born in 1993 as a political sweetener in a tax-hike bill. Stated goal (capital for small businesses that can't raise equity) no longer matches reality (record VC dry powder). Worthless 2003–2009. 58% of the 2010–2015 enhancement was granted retroactively, so it couldn't have incentivized anything. |
| AMT | Clear purpose, no monitoring | Had a measurable target (155 high-income filers paying zero in 1969). Failed because it wasn't indexed and nobody owned the dashboard; it drifted into the upper middle class. |

Takeaway: criteria are necessary but not sufficient. You also need telemetry and an owner.

## Proof it's feasible: Washington State

- Since 2013, bills creating or expanding a tax preference must include a **Tax Preference Performance Statement**: public policy objective plus "clear, relevant, and ascertainable" metrics (RCW 82.32.808).
- The Joint Legislative Audit and Review Committee (JLARC) evaluates preferences on a 10-year schedule set by a citizen commission.
- New preferences **auto-expire after 10 years** unless another date is set.
- Great anecdote: three preferences to attract a silicon smelter went unclaimed after the company built in Tennessee instead. They expire in 2027.
- 2026 cycle: 7 preferences reviewed, auditor recommended continuing 5 and letting 2 expire.
- Caveat: Washington still carries 650+ preferences. Even a disciplined system accumulates debt.

Federal contrast: the tax expenditure budget (required since 1974) estimates what provisions *cost*, not whether they *work*.

## The hard part: deprecation, not criteria

- Federal sunsets already exist. They became "extenders," renewed on autopilot. QSBS is the case study: temporary 100% exclusion extended five times (2010–2015), then made permanent.
- Software has the same disease (Hyrum's Law: any behavior someone depends on becomes a constituency), but software has one owner who can say no. The tax code has 535 owners, and every deprecation is a tax increase on someone organized.
- **The essay's real contribution must be the kill mechanism:** default-off at sunset, renewal only if the metrics moved. Burden of proof on the feature, not the deleter.

## Dog food: LGF's own performance statement

The essay only works if the Lifetime Gains Framework ships with one. Draft candidates:

| Tenet | Metric | Revisit trigger |
|---|---|---|
| Simplicity | Capital gains provisions/pages in the code; compliance hours | No meaningful reduction after 5 years |
| Durability | Net revenue vs. scored range ($45–170B) | Below range 3 straight years |
| Climb | Share of small business sales under $2M owing zero | Below target |
| Buy-borrow-die | Share of top-0.1% gains escaping tax at death or via borrowing | Not near zero |
| Innovation | Seed and early-stage VC deal counts vs. pre-enactment trend | Sustained drop beyond X% |

The innovation row turns the conceded NBER risk (LGF likely reduces fund-manager incentives; Campello & Junqueira 2026) into a monitored guardrail. Stronger than any argument against the megafund objection.

## Open questions / to verify

- [ ] JLARC's track record: how often do reviewed preferences actually expire vs. get renewed? If rarely, the lesson flips from "copy Washington" to "metrics alone don't kill anything."
- [ ] Other states with evaluation laws (Pew has tracked this) and any with real repeal outcomes.
- [ ] Federal attempts to require evaluation of tax expenditures (GAO recommendations, GPRA) and why they didn't stick.
- [ ] Set actual targets and thresholds for the LGF table (the "X%" and "target" placeholders).
- [ ] Confirm the AMT "155 filers" origin story and indexing history before publishing.

## Sources

- RCW 82.32.808 (performance statement requirement): https://app.leg.wa.gov/rcw/default.aspx?cite=82.32.808
- JLARC 2026 Tax Preference Reviews: https://leg.wa.gov/studies-audits-and-reports/performance-audits/published-audits/2026troverview/
- JLARC 2025 reviews (silicon smelter): https://leg.wa.gov/jlarc/taxReports/2025/overview.html
- Polsky & Yale, "A Critical Evaluation of the QSBS Exclusion," 42 Va. Tax Rev. 353 (2023): https://digitalcommons.law.uga.edu/fac_artchop/1605
- Campello & Junqueira, NBER Working Paper w35418 (July 2026)