# Document Sync Checklist

**Source of Truth:** [The Fair & Simple Tax Act - PR_FAQ.md](The%20Fair%20%26%20Simple%20Tax%20Act%20-%20PR_FAQ.md) - Q1

When updating policy details, ensure these locations stay in sync:

## Core Policy Elements

### Child Benefit
- [ ] README.md - Family Benefits section
- [ ] PR_FAQ.md - Q1 Family Benefits
- [ ] PR_FAQ.md - Q10 (detailed explanation + phase-out formula)
- [ ] PR_FAQ.md - Q10 Examples 1-3 (household benefit calculations)
- [ ] PR_FAQ.md - Appendix B case studies (Sofia, Garcias)
- [ ] PR_FAQ.md - Budget tables (costs section)

### Income Tax Brackets
- [ ] README.md - Income Taxes section
- [ ] PR_FAQ.md - Q1 Income Taxes (table)
- [ ] PR_FAQ.md - Q10 Examples (income tax calculations)
- [ ] PR_FAQ.md - Appendix B case studies (all examples)

### Deductions & Credits
- [ ] README.md - Itemized Deductions & Universal Credits section
- [ ] PR_FAQ.md - Q1 Deductions and Credits
- [ ] PR_FAQ.md - Q15 (philosophy of deductions/credits)
- [ ] PR_FAQ.md - Q15a (medical cost credit details)
- [ ] PR_FAQ.md - Budget tables (mortgage/SALT/charitable/medical revenue)

### Capital Gains
- [ ] README.md - Capital Gains & Investment Income section
- [ ] PR_FAQ.md - Q1 Capital Gains section
- [ ] PR_FAQ.md - Q7 (detailed capital gains explanation)
- [ ] PR_FAQ.md - Budget tables (loophole closures)

### Payroll Taxes
- [ ] README.md - Payroll Taxes section
- [ ] PR_FAQ.md - Q1 Payroll Taxes
- [ ] PR_FAQ.md - Q10 Examples (payroll tax elimination)
- [ ] PR_FAQ.md - Appendix B case studies (FICA calculations)

### Budget Impact
- [ ] README.md - Overall net position
- [ ] PR_FAQ.md - Quick summary table (costs/revenue)
- [ ] PR_FAQ.md - Detailed revenue tables (Appendix)
- [ ] PR_FAQ.md - Headline Budget Impact section

## Update Workflow

1. **Make changes in PR_FAQ.md Q1 first** (source of truth)
2. **Update README.md table** to match (keep concise)
3. **Update examples/case studies** if numbers change
4. **Update budget tables** if revenue/cost estimates change
5. **Run consistency check** (see below)

## Quick Consistency Check Commands

```bash
# Check for old child benefit amounts
grep -r "\$3,000.*child" *.md
grep -r "\$3K.*child" *.md

# Check for budget inconsistencies
grep -r "Net.*\$54B.*savings" *.md

# Check for old bracket rates
grep -r "5%.*bracket\|10%.*bracket" *.md
```

## Known Duplications (By Design)

These serve different purposes and should stay duplicated:
- **README.md table** = Executive summary (scannable)
- **Q1 in PR_FAQ** = Detailed narrative (comprehensive)

When updating policy, update both but tailor the level of detail appropriately.
