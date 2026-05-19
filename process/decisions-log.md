# Decisions Log

Key decisions made while developing the Fair and Simple Tax Act project, with the reasoning behind each. The goal is to capture the *why* so future-us (or a new collaborator) doesn't relitigate settled ground.

## Process Rules

### Published doc closure rule
Any document linked from a published document must itself be published. The set of "published" files is the transitive closure of links starting from `index.md`, not just the essays we happen to be talking about at any given moment. Reason: broken links or 404s in a published doc are worse than having an unfinished stub live. If a stub is linked from `index.md`, the stub is published — even if it's still rough. How to apply: before moving any file out of the Jekyll deploy root, grep for inbound links from published docs. If any exist, either the file stays, or the link gets removed first.

## Framing & Architecture

### Lifetime Gains is "first and most fully developed," not "the centerpiece"
Calling it the centerpiece undermined the modular intent of the project. The framework is a system of independently shippable components; elevating one piece rhetorically makes the others look like afterthoughts. "First and most fully developed proposal" preserves the ordering without implying subordination.

### "Simple system architecture," not "microservices"
We briefly framed the project as a microservices architecture for the citizen-government fiscal relationship. "Microservices" is trendy tech jargon that dates quickly and alienates non-technical readers. "Simple system architecture" captures the same idea (clean interfaces, independent components, monolith-to-modules) in plain language.

### Tenet 3 avoids "99%" language
Early drafts leaned on "the 99%" framing. Too overtly political; it codes the whole project as partisan and narrows the audience. Final wording: "Building new wealth should be easier than compounding dynastic wealth. The system should not create structural advantages that entrench existing fortunes at the expense of economic mobility." Keeps the moral claim, drops the political tribal signal.

## Scope

### Corporate taxation is out of scope
Including corporate reform would triple the surface area of the project and entangle it in debates (pass-through treatment, international rules, book vs. tax income) that are orthogonal to the core thesis. Scoped out explicitly in index.md. The Phase 2 PRFAQ handles S-corp pass-through recharacterization via Market Compensation Requirement (MCR) as a targeted exception.

### Healthcare tax treatment is out of scope
The employer health insurance exclusion is ~$300B/yr — the largest tax expenditure in the code — but touching it conflates tax reform with healthcare policy, which is a third rail and a separate debate. Scoped out explicitly. We retain a medical cost credit to protect against catastrophic out-of-pocket costs, but we do not restructure employer-provided coverage.

### Pre-enactment gains are not retroactively counted
On day one of enactment, everyone's lifetime counter starts at $0. Retroactive counting would be politically impossible, administratively nightmarish (basis reconstruction for decades-old assets), and legally vulnerable. Clean slate is the only workable design.

## Capital Gains Framework

### Loan as a realization event
Loans, like sales, are "natural" arm's-length transactions with observable valuations. That makes them a clean realization trigger. Gifts and death are messier (no arm's-length counterparty), but donor/recipient basis tension partially mitigates gift valuation, and existing IRS qualified appraisal infrastructure handles death valuation. Not perfect, but adequate — no structural change warranted now.

### Zero-gain collateral edge case: do nothing
Added to the technical spec. Three reasons to leave it alone: (1) opportunity cost of chasing edge cases, (2) the framework itself eliminates the motivation for the edge case (no buy-borrow-die benefit if death triggers realization), (3) systemic design beats point fixes. Fox & Liscow (2024) cited.

### $500B compliance stat gets a qualifier
Using the whole-code compliance figure to motivate a capital-gains-only proposal is disingenuous. Added language acknowledging capital gains is one piece of the burden but generates disproportionate complexity.

### NIIT is not part of the AMT lineage
Initial draft implied a causal chain from AMT to NIIT. NIIT was ACA funding, not a response to buy-borrow-die. Corrected in lifetime-gains-essay.md.

## Income Tax Essay

### Charitable and medical credits live inside the income tax essay
Originally carved out as standalone stubs. Realized they can't be teased apart from deduction elimination — if you kill all deductions, you have to say what replaces the two that matter most (charitable, medical) in the same breath. Folded back in. The charitable-giving-essay.md file was repurposed as a deeper-dive companion covering DAF tension and appreciated-asset realization.

### Charitable credit: 50% of donation, capped at 5% of tax liability
Voluntary incentive. The cap prevents the wealthy from using it to zero out their tax bill, which was the old itemized-deduction abuse pattern.

### Medical credit: 30% refundable, $5K threshold
Involuntary catastrophe protection. Refundability is essential because the people most exposed to catastrophic medical costs are often those with little or no tax liability. The threshold prevents it from becoming a routine subsidy for minor expenses.

### The two credits have parallel framing but different mechanics
User asked whether they should have identical structure. Pushed back: they serve different purposes (voluntary giving vs. involuntary catastrophe), so % of liability cap works for charitable but refundability is structurally required for medical. Parallel in spirit, different in mechanism.

### Filing status: five to two
Collapses Single, MFJ, MFS, HoH, QW into just Single and Joint. Simplification for its own sake — the current five-status system creates edge cases and marriage penalties with no corresponding benefit.

## Modular Components

### Child payment consolidates CTC/ACTC/EITC/AOTC/LLC/education credits
One monthly payment replaces six overlapping programs. 2021 expanded CTC cut child poverty ~30%; the precedent exists.

### FICA reform: kill employee side, keep employer side as 8% uncapped ESNC
Employee-side FICA is regressive and visible on every paycheck. Eliminating it is a large tax cut for working people. Employer-side retained (and uncapped) as Employer Social Net Contribution. Details in social-security-prfaq.md.

### Universal Savings Account (USA) replaces 15+ account types
401(k), IRA, Roth, SEP, SIMPLE, 529, Coverdell, ABLE, HSA, FSA, HRA, 457(b), etc. Single account, $1K seed at birth, $30K annual cap, tax-free growth, $5M balance cap, contributions withdrawable anytime, qualified medical withdrawals tax-free. "Great Conversion" at flat 12% over 10-year window yields ~$1.2-1.3T.

## Publishing & Infrastructure

### Jekyll site.url for absolute URLs
Rather than hardcoding mattsly.com in every image path for OG/Twitter cards, added `url: "https://www.mattsly.com"` to _config.yml and let jekyll-seo-tag prepend it automatically. Template variable, not hardcoded strings.

### Twitter card: summary_large_image
Frontmatter on lifetime-gains-essay.md specifies the large image card for better social sharing.

### Outgoing links stay same-tab
User preference: ctrl-click is fine, don't force new tabs.
