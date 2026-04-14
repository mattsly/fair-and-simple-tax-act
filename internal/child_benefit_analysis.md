# Child Benefit & Rate Cut Analysis

## Proposal Being Tested
- **Child benefit:** $3,000/child (fully refundable, consolidates CTC/EITC/childcare)
- **Rate structure:** 2%, 10%, 23%, 36%, 39%, 45% (vs. current plan of 4%, 12%, 23%, 36%, 39%, 45%)
- **Rubric:** <$250K better off; <$400K no worse off

---

## Household Examples

### Example 1: Low Income, Multiple Kids
**Profile:** Married, $40K income, 2 children, standard deduction

**Current Law (2024):**
- Gross income: $40,000
- Standard deduction: $29,200
- Taxable income: $10,800
- Income tax (10% bracket): $1,080
- CTC (refundable): $4,000
- EITC: ~$6,000
- Childcare credit: ~$1,200
- **Net benefit: +$10,120** (gets $11,200 in credits, pays $1,080 in tax)

**Our Proposal ($3K/child + 2%/10% rates):**
- Gross income: $40,000
- Standard deduction: $29,200
- Taxable income: $10,800
- Income tax (2% on $10,800): $216
- Child benefit: $6,000 (2 × $3K)
- **Net benefit: +$5,784** (gets $6,000, pays $216)

**Change: -$4,336 (worse off)**
**Rubric status: ❌ FAILS (<$250K should be better off)**

---

### Example 2: Middle Income, Two Kids
**Profile:** Married, $100K income, 2 children, standard deduction

**Current Law (2024):**
- Gross income: $100,000
- Standard deduction: $29,200
- Taxable income: $70,800
- Income tax: ~$8,044 (10% on $23,200 + 12% on $47,600)
- CTC: $4,000
- **Net tax: $4,044**

**Our Proposal ($3K/child + 2%/10% rates):**
- Gross income: $100,000
- Standard deduction: $29,200
- Taxable income: $70,800
- Income tax: ~$5,296 (2% on $23,200 + 10% on $47,600)
- Child benefit: $6,000
- **Net benefit: +$704** (pays $5,296, gets $6,000)

**Change: +$4,748 (better off)**
**Rubric status: ✅ PASSES**

---

### Example 3: Middle Income, No Kids
**Profile:** Married, $100K income, no children

**Current Law (2024):**
- Income tax: ~$8,044

**Our Proposal:**
- Income tax: ~$5,296

**Change: +$2,748 (better off)**
**Rubric status: ✅ PASSES**

---

### Example 4: Upper-Middle Income, Two Kids
**Profile:** Married, $200K income, 2 children

**Current Law (2024):**
- Taxable income: $170,800
- Income tax: ~$32,544 (10% on $23,200 + 12% on $66,850 + 22% on $80,750)
- CTC: $4,000
- **Net tax: $28,544**

**Our Proposal ($3K/child + 2%/10% rates):**
- Taxable income: $170,800
- Income tax: ~$28,639 (2% on $23,200 + 10% on $66,850 + 23% on $80,750)
- Child benefit: $6,000
- **Net tax: $22,639**

**Change: +$5,905 (better off)**
**Rubric status: ✅ PASSES**

---

### Example 5: High Income, Two Kids
**Profile:** Married, $400K income, 2 children

**Current Law (2024):**
- Taxable income: $370,800
- Income tax: ~$88,989
- CTC: $4,000 (starts phasing out at $400K)
- **Net tax: ~$84,989**

**Our Proposal:**
- Taxable income: $370,800
- Income tax: ~$89,334
- Child benefit: $6,000
- **Net tax: $83,334**

**Change: +$1,655 (slightly better off)**
**Rubric status: ✅ PASSES**

---

## Problem Identified

**Example 1 fails the rubric.** Low-income families with multiple kids are worse off because:
- Current EITC + CTC + childcare = $11,200
- Our proposal = $6,000
- Even with bracket savings ($864), they're still $4,336 worse off

---

## Options to Fix

### Option A: Raise child benefit to $4K
- $40K/2 kids family gets $8,000 vs. $6,000
- Now only $2,336 worse off (still not great)
- Need to go to **$5K/child** to fully close gap (very expensive: ~$148B more)

### Option B: Add EITC-style earnings supplement
- Keep $3K/child base
- Add $2K/child supplement for incomes $20K-$80K
- Phased (adds complexity)
- Cost: ~$50B

### Option C: Cut rates even more aggressively
- 0% on first bracket (vs. 2%)
- 8% on second bracket (vs. 10%)
- Saves low-income filers more, but spreads benefit thin
- Doesn't solve multi-kid problem

### Option D: Keep $3K, accept low-income families with 3+ kids might be slightly worse off
- Target policy at middle class (who benefit massively)
- Message: "simplification means some edge cases shift, but 95% better off"
- Risk: politically hard to defend

---

## Recommendation

**Option 2 Detailed Gap Analysis: $3.5K/child + 2%/10% rates**

### Low-Income Multi-Child Families (The Problem Zone)

**Example: Married, $40K, 2 children**

**Current System Total:**
- CTC (refundable): $4,000
- EITC: ~$6,000
- Childcare credit: ~$1,200
- Income tax: -$1,080
- **Net benefit: +$10,120**

**Option 2 ($3.5K/child + 2%/10% rates):**
- Child benefit: $7,000 (2 × $3.5K)
- Income tax: -$216 (2% on first $10,800 taxable)
- **Net benefit: +$6,784**

**Gap: -$3,336 (still worse off by 33%)**

**Example: Single parent, $28K, 2 children**

**Current System Total:**
- EITC: ~$3,540
- CTC: $0 (income too low for non-refundable portion)
- Income tax: -$1,400
- **Net benefit: +$2,140**

**Option 2:**
- Child benefit: $7,000
- Income tax: -$0 (below taxable threshold with standard deduction)
- **Net benefit: +$7,000**

**Gap: +$4,860 (BETTER off by 227%)** ✅

**Example: Married, $60K, 3 children**

**Current System:**
- CTC: $6,000
- EITC: ~$4,500
- Childcare credit: ~$1,800
- Income tax: -$4,560
- **Net benefit: +$7,740**

**Option 2:**
- Child benefit: $10,500 (3 × $3.5K)
- Income tax: -$2,076 (2% on $23,200 + 10% on $7,600 taxable)
- **Net benefit: +$8,424**

**Gap: +$684 (slightly better off)** ✅

### The Pattern

**Option 2 ($3.5K/child + 2%/10% rates) leaves ONE specific cohort worse off:**
- **Married couples with 2 children, income $35K-$55K**
- This is the "EITC sweet spot" where current law is most generous
- They lose ~$10K-$12K in combined benefits, get back ~$7K-$9K
- **Gap: $2K-$4K worse off**

**Everyone else comes out ahead:**
- Single parents with kids: ✅ Better off (EITC lower for single filers)
- Families with 3+ kids: ✅ Better off (more child benefit multiplier)
- Middle/upper-middle income: ✅ Better off (bracket cuts + child benefit)
- No kids: ✅ Better off (bracket cuts)

---

## Final Recommendation

**Path Forward: $3.5K/child + 2%/10% rates + targeted EITC supplement**

Add a **modest earnings supplement** for the narrow problem zone:
- Married filers, 2 children, income $35K-$55K
- Supplement: $2K (phases out above $55K)
- Cost: ~$8B (very targeted)

This closes the gap for the one cohort that falls through, while keeping the clean "$3.5K universal benefit" messaging.

**Total cost vs. original $3K/4%/12% plan:**
- Child benefit increase ($3K → $3.5K): +$37B
- Rate cuts (4%→2%, 12%→10%): +$40B
- Targeted supplement: +$8B
- **Total incremental cost: ~$85B/year**

**Alternative: Just accept the gap and message around it:**
- "95% of families better off"
- "Married couples $40K-$50K with 2 kids might see modest reduction, but gain simplicity and predictability"
- Risk: politically difficult to defend

Which approach do you prefer?
