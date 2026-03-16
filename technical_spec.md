# Lifetime Gains Framework: Technical Specification

**Version:** 0.2 (Draft)
**Date:** March 16, 2026
**Status:** Working document — not for public distribution

This document is the canonical source of truth for the framework's mechanics. The essay and PR-FAQ are derived from this spec. If a conflict exists, this document governs.

---

## 1. Parameters

The framework has two adjustable parameters. All other values are derived or inherited from existing law.

| Parameter | Symbol | Individual | Married Filing Jointly | Indexed |
|---|---|---|---|---|
| Lifetime Exemption | E | $2,500,000 | $5,000,000 | CPI, annually |
| Phase-Out Ceiling | C | $10,000,000 | $20,000,000 | CPI, annually |

The top rate (T) is inherited from the income tax code: currently 37%. It is not a framework parameter.

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

Four events trigger realization of capital gains:

1. **Sale.** (Unchanged from current law.)
2. **Death.** All unrealized gains are deemed realized on the decedent's final return. Heirs receive basis at date-of-death fair market value. Follows the Canadian model (in use since 1972).
3. **Gift.** The donor is taxed on unrealized gains at the time of transfer, using the donor's lifetime counter. Recipient receives basis at gift-date fair market value. Annual gift exclusion ($18K/person/year) retained for administrative simplicity.
4. **Borrowing against appreciated assets.** When a loan is secured by appreciated assets, the unrealized gain on the collateral is deemed realized at the time of borrowing, regardless of loan purpose. Basis steps up by the deemed amount to prevent double taxation on eventual sale. If the collateral has no unrealized gain (e.g., a purchase mortgage on a newly acquired home, or collateral that is underwater), the deemed realization is $0. This rule applies universally — no distinction between personal, business, or investment purpose — eliminating the classification disputes that would otherwise become the primary enforcement challenge.

**Trust treatment:** Transfers of appreciated assets into irrevocable trusts are realization events (treated as gifts). For grantor trusts (where the grantor remains the tax owner), realization is deferred until the earlier of: (a) the trust becoming irrevocable with respect to the grantor, or (b) the grantor's death. Trust-held assets are deemed realized upon the death of each generation's primary beneficiary, preventing dynasty trusts from deferring gains across generations indefinitely. This eliminates GRATs, dynasty trusts, and similar structures as tax avoidance vehicles — the appreciated assets are taxed on the way in, and again at each generational transfer to the extent of new appreciation.

In all cases, gains within remaining exemption headroom are tax-free; gains above are taxed on the sliding scale.

### Rule 4: CPI-Indexed Basis

Cost basis is fully adjusted for inflation using the Consumer Price Index:

```text
adjusted_basis = original_basis × (CPI_sale / CPI_purchase)
```

**Symmetry by design:** CPI adjustment applies universally to all transactions, whether sold at a gain or a loss. Because terminal realization (Rule 3) ensures deferred gains are eventually taxed, asymmetric rules to handicap tax-loss harvesting are unnecessary. The framework taxes only real economic gains and recognizes only real economic losses.

For assets acquired by gift or deemed realization at death, the basis date resets to the transfer date.

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
| Negative floor | -E (-$2.5M individual, -$5M MFJ) |
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

---

## 4. What Is Eliminated

The following provisions are rendered redundant and repealed:

| Provision | Reason |
|---|---|
| Estate tax | Replaced by deemed realization at death |
| Alternative Minimum Tax (capital gains component) | No preferential rate to exploit |
| Net Investment Income Tax (3.8% surtax) | Gains above E are ordinary income at rates >> 3.8% |
| Stepped-up basis at death | Death is a realization event; heir gets clean basis at FMV |
| Section 121 (primary residence exclusion) | Replaced by universal lifetime exemption |
| Section 1202 / QSBS (qualified small business stock) | Replaced by universal lifetime exemption |
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

1. **Illiquid asset valuation at death/gift.** Private businesses, art, and real estate require appraisal. Existing IRS infrastructure (Revenue Ruling 59-60, Valuation Office) handles this but disagreements will arise.
2. **Payment flexibility.** The main doc proposes 15-year lien options for illiquid estates. Specific terms (interest rate, collateral rules) are not specified here.
3. **Backdoor Roth closure mechanics.** The spec says "Traditional-to-Roth conversions are closed." This is a significant change that needs precise statutory language. Does it apply to all conversions, or only above certain thresholds?
4. **Qualified dividends.** Counted against the lifetime counter — but what about dividends received within the exemption? Presumably tax-free, same as capital gains within the exemption. Confirm.
5. **State interaction.** The framework is federal. State capital gains taxes (which vary widely) are unaffected. State estate taxes may need separate treatment.

---

*This spec is version-controlled alongside the PR-FAQ and essay. When mechanics change, update this document first, then propagate to derived documents.*