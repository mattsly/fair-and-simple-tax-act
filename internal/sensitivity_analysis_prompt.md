# Sensitivity Analysis: Lifetime Gains Framework Calibration

## Instructions for the Analyst (LLM or Human)

You are being asked to perform a sensitivity analysis on two variables in a proposed U.S. capital gains tax reform called the **Lifetime Gains Framework**. The framework replaces the current capital gains system (preferential rates, stepped-up basis, estate tax, AMT, NIIT, QSBS, 1031 exchanges, and dozens of other provisions) with five rules. Two of those rules contain the only adjustable parameters in the entire system:

**Variable 1: Lifetime Exemption (E)**
- Every individual gets a lifetime capital gains exemption of $E (2× for married couples filing jointly).
- All gains below this threshold are tax-free, regardless of asset type.
- Range to analyze: $1M to $5M (individual), in $500K increments.

**Variable 2: Phase-Out Ceiling (C)**
- Above the exemption, the capital gains rate phases linearly from 0% to the taxpayer's ordinary income marginal rate.
- The phase-up is complete at $C in cumulative lifetime gains. Above $C, all gains are taxed as ordinary income.
- Range to analyze: $5M to $15M (individual), in $1M increments.

Both variables are CPI-indexed annually (like income tax brackets), so treat them as real 2026 dollars.

## What the Framework Eliminates (Revenue Offsets)

The framework eliminates the following, which currently reduce federal revenue:

| Provision | Estimated Annual Tax Expenditure |
|---|---|
| Stepped-up basis at death | $45-75B (JCT/Treasury estimates vary) |
| Preferential capital gains rate (vs. ordinary income) | $120-180B |
| Estate tax (repealed, but replaced by deemed realization at death) | Net effect depends on calibration |
| QSBS (Section 1202) | $4-5B (JCT) |
| 1031 like-kind exchanges | $4-10B (JCT) |
| Opportunity Zone deferrals | $2-5B |
| Carried interest preferential rate | $1-3B |
| Various other preferences (installment sales, collectibles rate, 60/40 rule) | $3-8B |

The framework also adds new realization events:

| New Realization Event | Estimated Annual Revenue |
|---|---|
| Deemed realization at death (all unrealized gains taxed on final return) | $75-100B |
| Deemed realization on gifts | $5-10B |
| Deemed realization on borrowing against appreciated assets (closes buy-borrow-die) | $25-50B |
| Roth reform ($5M balance cap, backdoor closure) | $10-23B |

## What the Framework Eliminates (Revenue Losses)

| Repealed Tax | Current Annual Revenue |
|---|---|
| Estate tax | $20-25B |
| Alternative Minimum Tax (capital gains component) | $5-10B |
| Net Investment Income Tax (3.8% surtax) | $30-40B |

## What You Should Analyze

For each (E, C) pair in the grid:

### 1. Net Annual Revenue Impact
Estimate the net change in federal revenue compared to current law. Key dynamics:

- **Below E:** All gains are tax-free. This is a revenue *loss* relative to current law's 15%/20%/23.8% rates for taxpayers whose lifetime gains would have been taxable. However, most households with gains below $1.5M already face effective rates well below statutory due to existing preferences (Section 121, QSBS, 0% bracket, etc.).
- **E to C:** The sliding scale generates revenue at rates between 0% and ~37%. Compare to current law's flat 23.8% (20% + 3.8% NIIT). The crossover point where the framework rate exceeds 23.8% is roughly at 60-65% of the way through the phase-up band.
- **Above C:** All gains taxed at ordinary income rates (~37% top rate vs. current 23.8%). This is the primary revenue engine.
- **New realization events:** Deemed realization at death, gifts, and borrowing generate revenue that current law entirely forgoes. This is independent of E and C and should be treated as a constant offset (~$100-160B/yr).

### 2. Distributional Impact
For each (E, C) pair, estimate the percentage of U.S. households that are:
- **Unambiguously better off** (lifetime gains below E, so they pay $0 vs. some positive amount under current law)
- **Roughly breakeven** (lifetime gains in the lower portion of the E-to-C band)
- **Paying more** (lifetime gains in the upper portion of the E-to-C band and above C)

Use the following approximate distribution of lifetime capital gains (based on SCF, IRS SOI, and Federal Reserve data):
- ~80% of households: < $500K lifetime gains
- ~90% of households: < $1M
- ~95% of households: < $2M
- ~98% of households: < $5M
- ~99.5% of households: < $10M
- ~99.9% of households: < $50M

### 3. Behavioral Response (Elasticity)
Capital gains revenue is highly elastic. The standard elasticity estimate is 0.5-0.7 (a 10% increase in the rate reduces realizations by 5-7%). However, this framework changes the elasticity calculus because:
- Death as a realization event eliminates the option to defer indefinitely (reduces elasticity)
- Borrowing as a realization event closes the primary avoidance strategy (reduces elasticity)
- The lifetime counter means timing shifts don't avoid tax, they just defer it (reduces elasticity)
- The exemption eliminates lock-in for most households (reduces elasticity for the middle class)

Estimate an adjusted elasticity for this framework (likely 0.2-0.5, lower than conventional estimates) and apply it to your revenue projections.

### 4. Political Viability Score (Subjective)
Rate each (E, C) pair on a 1-10 scale for political viability, considering:
- Higher E is more attractive to the right (larger tax-free zone, easier to sell as pro-entrepreneur)
- Lower E and C generate more revenue, which is more attractive to deficit hawks and the left
- The estate tax repeal is a major sweetener for the right; it becomes less compelling if the framework's effective rate on estates exceeds current law's effective rate (after planning) by too much
- The "98% of households are better off" claim requires E to be high enough that the exemption covers the vast majority

### 5. Recommended Calibration
Based on your analysis, recommend an (E, C) pair that optimizes for:
1. Revenue positive with high confidence (>95% probability of net positive in year 1)
2. At least 95% of households unambiguously better off
3. Political viability (bipartisan coalition possible)
4. Simplicity of explanation ("your first $X is tax-free")

## Key Assumptions to State Explicitly

Please state your assumptions on:
- Total annual U.S. capital gains realizations (recent years: $1-2T, but this framework would increase realizations due to expanded events)
- Distribution of gains by size (use IRS SOI data if available)
- Effective current-law rate after all preferences and planning (likely 10-15% for large estates, vs. statutory 23.8%)
- Behavioral response to the new realization events (how much new revenue vs. how much avoidance)
- Transition effects (pre-enactment harvesting, grandfathering)

## Output Format

Please provide:
1. A summary table: rows = E values, columns = C values, cells = estimated net annual revenue
2. A second table with the same structure showing % of households better off
3. Your recommended (E, C) pair with a 2-3 paragraph justification
4. The three biggest risks to your revenue estimate (what could make it wrong in either direction)
5. Any structural concerns with the framework itself that the calibration cannot fix

## Reference

The full framework document is available at mattsly.com. The core architecture is:
1. Lifetime exemption of $E per individual
2. Sliding scale from 0% to ordinary income rates, completing at $C
3. Realization events: sale, death, gift, borrowing against appreciated assets
4. CPI-indexed basis (gains only; losses measured at nominal basis)
5. Roth reform: no income limit, $5M balance cap, backdoor closure
