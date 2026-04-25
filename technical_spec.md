# Lifetime Gains Framework: Technical Specification

**Version:** 0.3 (Draft)
**Date:** April 24, 2026
**Status:** Working document

This document is the canonical source of truth for the framework's mechanics. Related documents are derived from this spec. If a conflict exists, this document governs.

---

## 0. Scope

This specification addresses the treatment of capital gains in taxable brokerage accounts and other non-retirement investment vehicles. The integration of retirement accounts (traditional and Roth 401(k)s, IRAs, 529s, HSAs, and other tax-advantaged vehicles) with the Lifetime Gains Framework is addressed in a separate proposal, "One Account to Rule Them All." Until that proposal is enacted, existing retirement account rules apply without modification.

The framework is federal. State capital gains taxes (which vary widely) and state estate taxes are unaffected by this specification.

---

## 1. Parameters

The framework has two adjustable parameters. All other values are derived or inherited from existing law.

| Parameter | Symbol | Individual | Married Filing Jointly | Indexed |
|---|---|---|---|---|
| Lifetime Exemption | E | $2,000,000 | $4,000,000 | CPI, annually |
| Phase-Out Ceiling | C | $6,000,000 | $12,000,000 | CPI, annually |

The top rate (T) is inherited from the income tax code: currently 37%. It is not a framework parameter.

**Breakeven against current law (informational):** at these parameters, a single filer with cumulative lifetime gains of approximately $11.2M pays the same tax under the framework as under current law's 23.8% top combined LTCG + NIIT rate. Below that cumulative gain, the taxpayer pays less under the framework; above, they pay more.

---

## 2. The Five Rules

### Rule 1: Lifetime Exemption

Every individual receives a lifetime capital gains exemption of E. Gains within the exemption are taxed at 0%.

- Per individual, from enactment (only post-enactment gains count against the counter)
- Cumulative across all asset types: equities, real estate, business interests, collectibles, crypto, etc.
- No asset-type restrictions, no qualification tests, no entity-type requirements
- Long-term gains only (holding period > 1 year); short-term gains taxed as ordinary income (unchanged from current law)
- E is indexed to CPI annually; increases apply prospectively to all taxpayers; decreases apply only to gains realized after the adjustment

### Rule 2: Sliding Scale

Above E, the capital gains rate phases linearly from 0% to T over the range [E, C].

**Rate at any counter position P (where P > E):**

```text
rate(P) = min(T, T × (P - E) / (C - E))
```

**Tax on a tranche of gains from counter position P₁ to P₂ (where E ≤ P₁ < P₂):**

```text
tax = ((rate(P₁) + rate(P₂)) / 2) × (P₂ - P₁)
```

This endpoint averaging is exact for a linear scale (equivalent to integrating the area under the curve).

**Above C:** All gains taxed at T. No further calculation needed.

**Critical design choice:** T is always the top marginal income tax rate (currently 37%), regardless of the taxpayer's other income. A retiree with $0 W-2 income and $15M in lifetime gains pays 37% on gains above C, identical to a W-2 earner at $500K. Capital gains under this framework are taxed on a separate schedule that converges to the same top rate as ordinary income but does not stack within ordinary income brackets.

### Rule 3: Expanded Realization Events

Realization happens whenever appreciated wealth changes hands in a way that preserves or transfers its availability for private consumption. Under this principle, four events trigger realization: sale, death, gift to another individual, and borrowing against appreciated assets.

**Exception: transfers to qualified charities are not realization events.** The appreciation exits the private economy. See the Charitable Donation Treatment subsection below for mechanics.

1. **Sale.** (Unchanged from current law.)
2. **Death.** All unrealized gains are deemed realized on the decedent's final return. Heirs receive basis at date-of-death fair market value. Follows the Canadian model (in use since 1972).
3. **Gift.** The donor is taxed on unrealized gains at the time of transfer, using the donor's lifetime counter. Recipient receives basis at gift-date fair market value. Annual gift exclusion ($19K/person/year) retained for administrative simplicity.

   **Gift valuation:** For publicly traded securities, FMV is market price. For illiquid assets, existing IRS qualified appraisal requirements and valuation enforcement (Revenue Ruling 59-60) apply. Critically, the elimination of stepped-up basis creates a natural tension between donor and recipient that discourages undervaluation: if the donor lowballs the gift's FMV, they pay less tax now — but the recipient inherits a lower basis and pays correspondingly more tax upon eventual sale or death. The total tax collected is approximately the same regardless of the stated gift value. Under current law, this tension does not exist because stepped-up basis at death eliminates the deferred tax entirely, making donor and recipient cooperative parties in undervaluation.
4. **Borrowing against appreciated assets.** When a loan is secured by appreciated assets, the unrealized gain on the collateral is deemed realized at the time of borrowing, regardless of loan purpose. Basis steps up by the deemed amount to prevent double taxation on eventual sale. If the collateral has no unrealized gain (e.g., a purchase mortgage on a newly acquired home, or collateral that is underwater), the deemed realization is $0. This rule applies universally — no distinction between personal, business, or investment purpose — eliminating the classification disputes that would otherwise become the primary enforcement challenge.

   **Collateral valuation:** For publicly traded securities, FMV is market price — no ambiguity. For illiquid collateral (private company stock, art, real estate portfolios), the deemed FMV is no less than the value implied by the loan terms (loan amount ÷ lender's LTV ratio). The lender's own risk assessment, documented in loan files and subject to bank regulatory examination, serves as a third-party-verified floor.

   **Edge case — borrowing against zero-gain assets:** A taxpayer could theoretically maintain a pool of zero-gain assets (e.g., CDs, Treasury bills) specifically to borrow against, keeping appreciated assets untouched while accessing liquidity with $0 deemed realization. This is not a material concern for three reasons:

   1. *Opportunity cost makes the exploit economically irrational.* Parking $100M in low-yield instruments to maintain a zero-gain borrowing base costs roughly $5-7M/year in foregone returns versus equities. At some point, it is cheaper to simply sell appreciated assets and pay the tax.

   2. *The framework eliminates the primary motivation.* Under current law, borrowing against appreciated assets is valuable because stepped-up basis at death erases the deferred tax permanently. Under this framework, death triggers realization (Rule 3), so the tax is merely deferred, not eliminated. The economic incentive to borrow instead of sell is dramatically reduced when the end state is taxation either way.

   3. *Systemic design vs. point fix.* Proposals that close only the borrowing loophole — e.g., Fox & Liscow (2024), ["No More Tax-Free Lunch for Billionaires"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4735564) — require complex definitional rules about secured vs. unsecured lending, collateral pools, and asset-level vs. portfolio-level gain calculations. Their deemed realization mechanism is consistent with Rule 3, but their additional definitional complexity is unnecessary under a systemic framework that closes all exit routes simultaneously (sale, death, gift, borrowing). When every exit is taxed, engineering around any single one becomes economically irrational. The residual use case — borrowing against zero-gain assets for short-term liquidity timing — is legitimate financial planning, not tax avoidance.

   **Trust treatment:** The governing principle is: if a transfer changes the tax owner of an asset, it is a realization event; if it does not, it is not. Transferring appreciated assets into an irrevocable trust changes the tax owner and is therefore a realization event (treated as a gift). Transferring assets into a revocable living trust — where the grantor remains the tax owner — is not a realization event; realization occurs when the trust becomes irrevocable or the grantor dies, whichever comes first. Trust-held assets are deemed realized upon the death of each generation's primary beneficiary, preventing dynasty trusts from deferring gains indefinitely. This structurally eliminates GRATs, dynasty trusts, and similar vehicles: appreciated assets are taxed on the way in, and again at each generational transfer to the extent of new appreciation.

   *Design note:* In a cleaner world, revocable living trusts would be unnecessary — they exist primarily because state probate systems are slow, expensive, and public. The framework accommodates them not as a policy choice but because the "change of tax owner" principle naturally exempts them, and penalizing ~25 million households for working around broken state courts is not this proposal's fight. A companion recommendation for federal probate reform or uniform state probate standards would reduce the need for these structures over time.

In all cases, gains within remaining exemption headroom are tax-free; gains above are taxed on the sliding scale.

#### Charitable Donation Treatment

Donations of appreciated assets to qualified 501(c)(3) charities are not realization events. Three mechanical consequences follow:

1. **No capital gains tax is owed** on the appreciation at the time of donation.
2. **The donor's lifetime capital gains counter is not affected.** The donated amount does not consume exemption headroom.
3. **The income tax deduction is limited to the donor's CPI-adjusted basis**, not the asset's fair market value.

**Worked example:** Donor contributes $1,000,000 of appreciated stock with a CPI-adjusted basis of $100,000. Capital gains tax owed: $0. Lifetime counter impact: $0. Charitable income tax deduction: $100,000.

This differs sharply from current law, under which the donor would receive a $1,000,000 FMV deduction and owe no capital gains tax on the $900,000 of appreciation — a double benefit that the framework eliminates. The asset leaves the private economy; the subsidy the donor receives is tied to the real dollars they originally committed, not the unrealized appreciation.

**Scope.** This treatment applies to direct contributions to public charities. Private foundations and donor-advised funds receive the same treatment at the donation stage (no gain recognized, basis-only deduction). Governance issues specific to those vehicles (DAF minimum payout requirements, foundation self-dealing rules, etc.) are addressed in a separate proposal on charitable giving reform and are out of scope for this specification.

### Rule 4: CPI-Indexed Basis

Cost basis is fully adjusted for inflation using the Consumer Price Index:

```text
adjusted_basis = original_basis × (CPI_sale / CPI_purchase)
```

**Symmetry by design:** CPI adjustment applies universally to all transactions, whether sold at a gain or a loss. Because terminal realization (Rule 3) ensures deferred gains are eventually taxed, asymmetric rules to handicap tax-loss harvesting are unnecessary. The framework taxes only real economic gains and recognizes only real economic losses.

For assets acquired by gift or deemed realization at death, the basis date resets to the transfer date.

**CPI mechanics:**

- **Index.** The all-urban consumer CPI-U published by the Bureau of Labor Statistics is the reference series. For months pre-dating CPI-U coverage, Treasury specifies the analogous historical series (same approach as existing indexed provisions such as Social Security).
- **Computation timing.** CPI adjustment is computed at the time of realization (sale, death, gift, or borrowing), using the CPI value for the realization month and the CPI value for the purchase month. No annual mark-to-inflation is required on unsold positions.
- **Lot-level indexing.** Each tax lot is indexed independently based on its own purchase date. Standard broker lot-tracking infrastructure (already used for specific-identification sales) accommodates this without material change.
- **Lump-sum acquisitions.** For assets acquired in multiple installments (dollar-cost averaging, reinvested dividends, stock grants over a vesting schedule), each installment is a separate lot indexed from its own acquisition date.
- **Fractional shares.** Indexed consistently with the full lot; no special rounding rules beyond existing broker conventions.
- **Broker reporting.** Brokers already report cost basis to the IRS under Section 6045(g). The framework extends this obligation to include the purchase-month CPI value, enabling brokers to compute the CPI-adjusted basis and real gain automatically. Legacy lots acquired before reporting requirements (pre-2011 for equities) retain the existing taxpayer-reported basis approach, with CPI adjustment applied against the stated purchase date.
- **Parameter indexing (separate from basis).** The exemption (E) and ceiling (C) are also CPI-indexed, but on an annual basis using the prior calendar year's year-end CPI. This parallels existing treatment of tax brackets and standard deduction.

### Rule 5: Roth Reform

Four changes to Roth IRAs:

1. **Remove income limits** for direct Roth contributions (currently $161K single / $240K married)
2. **Raise annual contribution cap** to $15,000 (indexed to CPI), up from $7K/$8K
3. **$5M balance cap** per person across all Roth-type accounts (IRA + Roth 401(k)). Once combined balance reaches $5M, new contributions are frozen. Investment growth above $5M continues tax-free.
4. **Backdoor conversions prohibited.** Traditional-to-Roth conversions are closed. Direct contributions only. (Existing mega-Roths grandfathered: no forced distributions, no retroactive taxation, contributions frozen immediately.)

At death: Roth accounts pass tax-free to beneficiaries under the existing 10-year distribution rule. No change.

No changes to Traditional 401(k), Traditional IRA, SEP IRA, SIMPLE IRA, HSA, or 529 accounts. These are deferred to a companion proposal.

---

## 3. The Lifetime Counter

The lifetime counter is the core tracking mechanism that determines exemption usage and sliding scale position.

**Properties:**

| Property | Rule |
|---|---|
| Scope | Per individual |
| Starting value | $0 at enactment (for existing taxpayers) or $0 at birth (for post-enactment taxpayers) |
| Increments | Net realized gains (after CPI adjustment) within each calendar year |
| Decrements | Net realized losses (after CPI adjustment) within each calendar year |
| Negative floor | -E (-$2M individual, -$4M MFJ) |
| Annual netting | Losses offset gains without limit within each year (same as current law) |
| Ordinary income offset | Up to $3,000/year of net capital losses can offset ordinary income (same as current law) |
| Loss carryforward | None needed — the counter itself is the carryforward |
| CPI treatment | Both gains and losses enter at real (CPI-adjusted) value |

**Marriage:**

- Filing jointly: combined exemption threshold = sum of both individual counters' remaining headroom
- Gains during marriage allocated 50/50 to each counter by default (overridable by prenup or joint election)
- Spousal transfers during marriage are not realization events

**Divorce:**

- Each spouse retains their individual counter
- Negative counters floor at $0 upon divorce

**Qualified dividends:** Count against the lifetime counter and are taxed on the same sliding scale. Ordinary dividends taxed as ordinary income (unchanged).

**Open design decision — MFJ counter architecture:** Two viable designs exist for married filers, each with tradeoffs:

1. *Two per-spouse counters (current spec).* Each spouse has a personal counter tracked from birth/enactment. Joint filing aggregates remaining headroom ($2M + $2M = $4M) and allocates gains 50/50 by default. This preserves individual entitlements across marriage, divorce, and remarriage cleanly, but requires brokerage accounts to track which spouse owns (or is deemed to own) each lot.
2. *Single combined MFJ counter.* Married couples filing jointly share one $4M counter with no per-spouse allocation. Simpler administratively, but creates asymmetry at divorce (how is a shared counter divided?) and at the death of one spouse (does the surviving spouse inherit the joint counter's remaining headroom, or only their half?).

The spec currently adopts approach #1. A fuller treatment of marriage mechanics — including titling conventions for joint brokerage accounts, community property state interactions, and prenup overrides — is deferred to a companion marriage-tax proposal.

---

## 4. What Is Eliminated

The following provisions are rendered redundant and repealed:

| Provision | Reason |
|---|---|
| Estate tax | Replaced by deemed realization at death |
| Alternative Minimum Tax (capital gains component) | No preferential rate to exploit |
| Net Investment Income Tax (3.8% surtax) | Gains above E are ordinary income at rates >> 3.8% |
| Stepped-up basis at death | Death is a realization event; heir gets clean basis at FMV |
| Section 121 (primary residence exclusion) | Replaced by universal lifetime exemption (see callout below) |
| Section 1202 / QSBS (qualified small business stock) | Replaced by universal lifetime exemption (see callout below) |
| Section 1031 (like-kind exchanges) | Deferral mechanism; incompatible with expanded realization |
| Section 1045 (QSBS rollover) | Same as above |
| Section 453 (installment sale deferral) | Same as above |
| Section 1244 (small business stock loss) | Systems converge; separate treatment unnecessary |
| Opportunity Zone deferrals | Deferral mechanism eliminated |
| Carried interest preference | No preferential rate above E |
| 60/40 rule for derivatives | No preferential rate above E |
| Collectibles rate (28%) | Single rate structure replaces all special rates |
| GRATs, dynasty trusts, valuation discounts | Gifts are realization events; stepped-up basis eliminated |
| Lifetime gift tax exemption ($13.6M) | Purpose (preventing double taxation with estate tax) no longer applies |
| Separate capital loss carryforward tracking | Counter is the carryforward |

**Retained:** Annual gift tax exclusion ($18K/person/year). Existing exit tax on expatriation (IRC §877A), strengthened by alignment with framework's realization events.

---

## 5. Transition Rules

### Counter Initialization
All counters start at $0 on the date of enactment. Pre-enactment gains are not retroactively counted.

### Cost Basis for Pre-Enactment Assets
Original purchase price is retained (not enactment-date value). Pre-enactment unrealized appreciation is taxed when eventually realized under the new system, but the counter starts at $0, giving every taxpayer a fresh exemption.

### Pre-Enactment Gain Harvesting
Expected and acceptable. Investors may sell before enactment to realize gains at current preferential rates (15-23.8%) and reset basis. This generates immediate revenue on gains that might otherwise escape taxation via stepped-up basis. Recommended transition window: 9-12 months.

### Roth Grandfathering
Existing Roth accounts above $5M: contributions frozen immediately, no forced distributions, no retroactive taxation. Growth continues tax-free.

---

## 6. Tax Calculation: Complete Algorithm

For a given taxpayer in a given tax year:

```text
INPUTS:
  counter_start    = lifetime counter at start of year
  transactions[]   = array of realized events (each with purchase_date, purchase_price, sale_price, sale_date)
  E                = current exemption (CPI-adjusted)
  C                = current ceiling (CPI-adjusted)
  T                = top marginal income tax rate

STEP 1: Compute net real gain/loss
  net = 0
  For each transaction:
    cpi_adjusted_basis = purchase_price × (CPI[sale_date] / CPI[purchase_date])
    real_result = sale_price - cpi_adjusted_basis
    net = net + real_result

STEP 2: Update counter
  counter_end = max(-E, counter_start + net)

STEP 3: Compute tax
  If net <= 0:
    tax = 0  (losses may offset up to $3K ordinary income per existing rules)
  If net > 0:
    taxable_start = max(counter_start, E)   // only gains above E are taxed
    taxable_end = counter_end
    If taxable_end <= E:
      tax = 0  (all gains within exemption)
    Else:
      // Gains in the phase-up band [E, C]
      band_start = max(taxable_start, E)
      band_end = min(taxable_end, C)
      If band_start < band_end:
        rate_start = T × (band_start - E) / (C - E)
        rate_end = T × (band_end - E) / (C - E)
        tax_band = ((rate_start + rate_end) / 2) × (band_end - band_start)
      Else:
        tax_band = 0
      // Gains above C
      If taxable_end > C:
        above_C = taxable_end - max(taxable_start, C)
        tax_above = T × above_C
      Else:
        tax_above = 0
      tax = tax_band + tax_above

OUTPUT:
  tax_owed = tax
  counter_end = counter_end  (carried to next year)
```

**Short-term gains** (holding period ≤ 1 year) are excluded from this algorithm entirely and taxed as ordinary income on Schedule D (unchanged from current law).

---

## 7. Open Design Questions

These are acknowledged areas where the spec is incomplete or where reasonable people may disagree:

1. **Illiquid asset valuation at death.** Private businesses, art, and real estate require appraisal. Existing IRS infrastructure (Revenue Ruling 59-60, Valuation Office) handles this but disagreements will arise. (Note: gift valuation is structurally mitigated by donor/recipient basis tension — see Rule 3. Borrowing valuation is addressed by the LTV floor — see Rule 3.)
2. **Payment flexibility.** The main doc proposes 15-year lien options for illiquid estates. Specific terms (interest rate, collateral rules) are not specified here.
3. **Backdoor Roth closure mechanics.** The spec says "Traditional-to-Roth conversions are closed." This is a significant change that needs precise statutory language. Does it apply to all conversions, or only above certain thresholds?
4. **Qualified dividends.** Counted against the lifetime counter — but what about dividends received within the exemption? Presumably tax-free, same as capital gains within the exemption. Confirm.
5. **State interaction.** The framework is federal. State capital gains taxes (which vary widely) are unaffected. State estate taxes may need separate treatment.
6. **Charitable contributions of appreciated assets.** Under current law, donating appreciated assets to charity (including Donor Advised Funds) avoids capital gains entirely and provides a fair-market-value deduction — a double benefit. The framework's "change of tax owner" principle would logically make such donations realization events, significantly reducing the charitable giving incentive. But exempting them creates an obvious new shelter, particularly via DAFs (which have no payout requirement). This tension is intentionally deferred to a companion proposal on charitable giving reform rather than resolved within the capital gains framework.

---

*This spec is version-controlled alongside the PR-FAQ and essay. When mechanics change, update this document first, then propagate to derived documents.*