# Pending — staging area for proposed commits

Proposed decisions, backlog entries, and open questions captured mid-week
(usually by Claude, JIT). The Monday weekly briefing presents every item here
for forced disposition: **decide / drop / punt**. Nothing lives here longer
than one week.

*Emptied 2026-07-23 in pre-vacation triage (Matt away until ~7/29). All items
dispositioned: scope decision → `decisions-log.md`; two Rule 3 questions →
`open-questions.md`; build slate → `backlog.md` Active Slate; sell actions →
outreach-log pipeline; hygiene items (index.md bundled edit, PNG regen) →
backlog Meta section.*

## Charitable giving: charity becomes a Rule 3 realization event (2026-08-27 — Matt leaning DECIDE)

Matt's call: any donation of an appreciated asset is a realization event. Remove the Rule 3 charity carve-out (`lifetime-gains-essay.md:45`) and the "What About Charitable Giving?" section (`:100-108`). Matt is doing the essay edit; this entry logs the analysis + blast radius.

### The spec already contradicts the published essay (fix required regardless)

`technical_spec.md:101-113` currently specifies **no realization + basis-only deduction** (worked example at :109 — $1M stock, $100K basis, deduction $100K). `lifetime-gains-essay.md:104` says **no realization + full FMV deduction, "exactly as today."** These are different policies and the essay's own note says the spec governs. Whatever happens with the new rule, one of these has to move.

### Matt's route is not the same as the spec's route — and is better

Let V=FMV, B=basis, G=V-B, t_oi = ordinary rate, t_cg = the LGF sliding-scale rate at the donor's counter position.
- Spec route (no realization, deduct B): net tax change = -t_oi x B.
- Matt's route (realize G, deduct V): net tax change = t_cg(G) - t_oi x V.
These coincide **only when t_cg = t_oi** — i.e. above the $6M ceiling where LGF pegs to the top rate. Below the exemption t_cg = 0, so Matt's route yields -t_oi x V: **full FMV deduction, zero gains tax — today's treatment, preserved intact.** So Matt's version is a *progressive phase-in of the basis haircut*, automatic and free, rather than the spec's flat haircut on everyone. It's strictly better on both the "fuel the climb" and radical-simplicity tenets than what the spec says today. Matt's earlier "unless I've used my exemption this is moot" instinct was right on the current-year number (the earlier pending entry over-corrected on this; the exemption-consumption point below is the only thing that survives).

### The characterization to own: same subsidy as cash — ending the DOUBLE subsidy, not the subsidy

(Corrects an earlier framing in this entry that said the deduction becomes "worth nothing" for zero-basis assets. That was an accounting artifact — the deduction and the realization tax cancel to zero *net cash at the moment of donation* — read wrongly as an economic conclusion. Matt caught it. The correct baseline is after-tax wealth foregone, not pre-tax FMV.)

Top bracket, $10M zero-basis stock. Counterfactual is sell-and-keep (under LGF the gain is taxed on every path — sale, death, gift, borrowing — so "never pay" no longer exists):

| | You give up | Charity gets | Gov't share of gift | Leverage |
|---|---|---|---|---|
| Today (no realization, FMV deduction) | $2.6M | $10M | **74%** | 3.85x |
| Proposed (realization + FMV deduction) | $6.3M | $10M | **37%** | 1.59x |
| Phase 2 (realization + 25%/3%-cap credit) | ~$5.7M | $10M | **~6%** | ~1.05x |

37% is *exactly* the government share of a **cash** gift from a top-bracket donor today. So the honest headline is: **the rule makes appreciated-stock giving as subsidized as cash giving, instead of twice as subsidized.** Not "we ended the charitable deduction" — "we ended the double deduction." Much stronger ground for the nonprofit fight than the earlier framing implied.

Matt's redirection point is right and should be in the essay: a donor still moves $1.59 to charity per $1 of foregone family wealth. Sharpen it though — today philanthropy of appreciated stock is *mostly the government's money* (74%), privately directed; under this rule it's mostly the donor's (63%). **That is Madoff's core critique, arrived at from the capital-gains side** — direct hook for the Q4 Madoff engagement and The Charity Exit.

### The unresolved problem: the rule means something different in Phase 2

Phase 1 (today's income tax, FMV deduction exists): rule = progressive basis haircut, as above.
Phase 2 (`income-tax-essay.md` — all deductions eliminated, charitable becomes a **25% credit capped at 3% of liability**): there is no FMV deduction to offset the realization. $10M zero-basis gift -> $3.7M gains tax, credit capped around $450-600K for a donor with $15-20M liability. Government share of the gift collapses to roughly **6%** (see table above) — near-total withdrawal of federal support for large charitable gifts. That is not "consistent with the framework," it's punitive, and it's the *stated* Phase 2 design. **The flagship cannot assert the realization rule without saying which phase's deduction/credit regime it assumes.** This is the real open question, not FMV-vs-basis.

### Rule 3's own stated principle cuts against it

Rule 3 (`:36`): realization happens when wealth "changes hands in a way that **alters its availability for private consumption**." A charitable gift is the one transfer that removes wealth from private consumption entirely. Adding charity requires restating the principle — the bridge already exists in the text being deleted (`:108`, control-vs-consumption: the donor surrenders *spending* but not *control*, influence or prestige). Keep that argument; it becomes load-bearing. Also `:37` bullet reads "Gift to another individual" and needs broadening.

### Don't delete the DAF/warehousing paragraph

Realization is orthogonal to warehousing — DAFs still carry no payout requirement, foundations still 5%. That paragraph is the published IOU for "The Charity Exit" (backlog #7, Q4) and the warm-up for the Madoff engagement (backlog #5). Replace it with the new rule + a narrowed IOU (payout/control, not realization); don't remove it.

### Revenue is modest — worth naming the trade

Rough: non-cash appreciated-securities giving on the order of $30-40B/yr, embedded gain maybe 60-70%, and only the slice above donors' exemptions is taxed -> plausibly **$4-8B/yr**, shrinking further with behavioral response. Numbers need checking. The case for the change is architectural coherence and shelter closure, not revenue — the nonprofit-sector fight is being picked for single-digit billions.

### Sequencing risk

The flagship is published; `decisions-log.md:150` notes the Substack sync is **already pending and already stale** on the charitable section. Shipping the new rule now asserts it publicly for 2-4 months with no companion essay to defend it, reversing the current honest punt-plus-IOU posture. Recommended: log the decision, fix the spec/essay contradiction, write The Charity Exit, amend the flagship when the companion lands.

### Blast radius (all need edits, not just the two essay sections)

- `lifetime-gains-essay.md`: :37 (gift bullet scope), :45 (carve-out note), :100-108 (section)
- `technical_spec.md`: :72 (exception), :101-113 (Charitable Donation Treatment + worked example), :363 (resolved-issues line)
- `process/proposal-tldr.md`: :33 (deduction aligned with basis)
- `process/open-questions.md`: :10-11 (FMV-vs-basis question — superseded or reframed)
- `drafts/charitable-giving-essay.md`: Option 1/2/3 list — Option 2 now adopted; re-scope the draft
- `drafts/income-tax-essay.md`: :114 Phase 2 interaction (the open problem above)

### Rule 3's principle needs restating (Matt, 2026-08-27) — separate but blocking

"Changes hands in a way that alters its availability for private consumption" isn't precise enough, and it's worse than imprecise: **it fails on Rule 3's own first bullet.** A *sale* converts illiquid appreciated wealth into spendable cash — it *increases* availability for private consumption. And "alters" is loose enough that charity already satisfies it (alters availability to zero), so the current text doesn't even exclude the thing line :45 carves out. Matt's instinct that it'd be clean as "any time an asset changes hands" is right; borrowing is the exception that breaks it, since a lien isn't a transfer.

**Proposed replacement — a two-prong test:**

> A gain is realized when either (a) the asset passes to a **different taxpayer**, or (b) the owner converts the gain into spendable cash while keeping the asset.

Test: sale (a) / gift (a) / death (a) / **charity (a) — no special pleading needed, which is the argument for the change** / borrowing (b) / perpetual hoarder: neither, correctly excluded / transfer to revocable or grantor trust: same taxpayer, correctly excluded / non-grantor trust and generational transfers: different taxpayer, caught — matches the dynasty-trust treatment at essay :162 / DAF contribution: different taxpayer, caught / pledge of unappreciated asset: (b) with $0 gain, matches existing text.

"Different taxpayer" (not "changes hands") is what makes it work — it handles same-owner moves between accounts and grantor trusts without a carve-out. Flag: **spousal transfers** need an explicit exception or MFJ-as-one-unit treatment; not currently addressed anywhere.

**Rhetorical version for the essay** — one principle plus one backstop, rather than two co-equal prongs: *gains are taxed when the asset moves to someone else; and because that moment can be deferred indefinitely while the owner still enjoys the gain, borrowing against appreciated assets triggers it too.* Prong (b) is subordinate, an anti-deferral rule, which is honest about what it is.

**Anchor for prong (b): constructive sale doctrine, IRC Sec. 1259** (enacted 1997, killed short-against-the-box). The code already has a doctrine for "you captured the economics of a sale without a sale." In a pledge the borrower hands the *downside* to the lender and takes cash out today while keeping the upside — partial sale in substance. Matt's own text already gives borrowing a **basis step-up**, i.e. sale treatment, so this is naming what's already built rather than inventing. *Verify the Sec. 1259 citation and enactment date before it goes in an essay.*

---

## Estate tax: keep it rather than repeal? (2026-08-27 — Matt raising, NOT decided)

Matt's proposal: reverse the published repeal, keep the estate tax alongside LGF, argue the two serve distinct purposes (LGF = government captures a share of appreciation; estate tax = estates aren't handed down perpetually), lean on LGF having closed the avoidance channels, and hint at a future rethink. Notes Madoff/Batchelder inheritance-as-income is the elegant answer but out of scope here.

### Two real holes in LGF-only (concede — one is sharper than the argument Matt made)

1. **LGF slows dynasties, it doesn't break them.** $100M all-gain estate: pay $28M, heirs hold $72M with fresh basis. At 4% real over 30 yrs -> $233M, gain $161M, tax $59.6M, next generation receives ~$173M. Real wealth grew 73% across a generation. Matt's "two distinct purposes" claim survives this test.
2. **The bigger hole Matt didn't name: LGF taxes appreciation, so an estate that is mostly principal pays nothing.** A family that sold the business a generation ago and holds $500M in Treasuries has ~zero unrealized gain and owes ~$0 at death under LGF-only. That is *precisely* the perpetual-transmission case, and it is invisible to every mechanism in the framework. **This is the strongest argument for retaining something at death, and it should be the argument if we keep one.**

### But stacking produces a headline rate that eats the essay

Assuming the LGF liability is deductible from the estate tax base (Sec. 2053 claims-against-estate treatment — **not yet decided anywhere, and it swings the answer 11 points**):

| Estate | LGF | Estate tax | Combined | Effective | Today (post-planning) |
|---|---|---|---|---|---|
| $100M / $80M gain | $28M | $22.8M | $50.8M | **50.8%** | ~10-15% |
| $500M / $400M gain | $147M | $135.2M | $282.2M | **56.4%** | 6-9% ($30-50M) |
| $100M, LGF non-deductible | $28M | $34M | $62M | **62%** | — |

The "double taxation" broadside is spurious in theory and lethal in practice at 56%. The combined rate is the political object, not the conceptual separation.

### Other objections

- **Loses the centrist keystone.** "Progressives get more revenue and no escape routes. Conservatives get the repeal they've wanted for a generation" (essay :164) is the most quotable line in the piece and the thing that makes the framework read as centrist rather than as a large progressive tax increase. Remove it and the package is: new tax on borrowing + death + gifts + charity, *and* we keep the estate tax. There is no remaining offer to the right.
- **Largest single hit to Tenet 1 (radical simplicity).** Retains Form 706, the unified credit, portability/DSUE elections, the GST tax, valuation-discount litigation, and the entire estate planning bar. Nothing else in the framework retains this much machinery.
- **Canada cuts against it.** The essay cites Canada (:160) as proof deemed-disposition-at-death works. Canada adopted it in 1972 *instead of* an estate tax — abolished the estate tax in the same reform. Not aware of an OECD country that stacks both. Citing Canada for the mechanism while doing the opposite with it is a visible seam. *Verify the both-taxes claim before relying on it.*
- **Matt's reason #2 argues the other way.** LGF collects $75-100B at death; the estate tax collects $20-25B today and its base *shrinks* once LGF liabilities reduce the estate — so retention is worth maybe $15-20B/yr, ~10% of the package for what will be ~50% of the political fight.
- **The loophole-closure claim is half right.** LGF's dual-purpose valuation (:162) genuinely undercuts discounts — the largest avoidance channel. It does not touch ILITs (life insurance outside the estate), charitable lead annuity trusts, or freeze techniques. Effective rate improves; it does not reach 40%.
- **It forecloses the Madoff answer Matt says he prefers.** The published scope note (:166) already leaves inheritance-as-income deliberately open — repeal + death-as-realization + explicit IOU is a coherent three-move posture. Keep the estate tax and a future inheritance-as-income essay is proposing a *third* tax at death. The repeal is what clears the ground for the preferred answer.

### Recommended alternative: estate tax as a MINIMUM tax at death, not a stacked one

Credit the LGF liability against the estate tax so the combined take is capped at the estate tax rate rather than summed. $100M / $80M gain: estate tax $34M, LGF $28M credited, total **$34M (34%)**.

Why this is the better shape: it targets hole #2 exactly (a high-basis or all-cash estate pays the 40% floor where LGF alone collects ~$0), it kills the double-taxation broadside *literally* rather than by argument, it preserves the dynasty floor, and it is a far smaller edit to a published flagship than reversing the repeal outright. Framing: **"LGF collects on appreciation; the estate tax remains only as a floor, ensuring the largest estates cannot pass untouched merely because their wealth isn't in the form of unrealized gain."**

If the repeal is kept instead: strengthen and date the inheritance-as-income IOU, and add hole #2 explicitly as the acknowledged gap — that is a strengthening of the current text rather than a reversal.

### Editorial reality

"Leave it alone" is a reversal of a published position, not inaction. Repeal is woven through :72 (list of eliminated taxes), the whole Estate Tax Question section (:155-166), the revenue table's "$20-25B estate tax repeal" reduction line, and the political framing at :164. Substack sync is already stale (decisions-log :150). Reversing here plus the charitable change makes this a substantial flagship revision, not a patch.

### Floor design worked out (2026-08-27) — and a correction to the suggestion above

**The max()-at-40% version I proposed above does not work.** Ignoring the $2M personal exemption (negligible at these sizes), T_LGF ~= 0.37G, and the floor is r(E-X). The floor binds whenever gain share G/(E-X) < r/0.37. At r = 40% that threshold is **108%** — and gain share can never exceed 100%. So at the current statutory rate the floor binds for *every* estate: death-as-realization becomes a pure prepayment of the estate tax with zero independent revenue effect, and the essay's central mechanism is decorative. The $34M figure quoted above was arithmetically right and architecturally wrong. **The floor rate must be well below 37% or the floor becomes the tax.**

**Rule text (drop-in):**

> At death, federal tax is the greater of (a) the Lifetime Gains liability on deemed realization of all unrealized gains, or (b) a floor of **20%** of the gross estate above the $15M / $30M exemption. Mechanically the estate tax survives at 20% with a dollar-for-dollar credit for LGF tax paid on the final return. Estates that are mostly unrealized appreciation pay (a) and never see the floor; estates that are mostly principal pay (b).

`Tax_death = max(T_LGF, r x max(0, E - X))`

| Floor rate r | Binds when gain share below | Character |
|---|---|---|
| 40% | 108% | always — LGF redundant. Fails. |
| 30% | 81% | almost always |
| 25% | 68% | most estates |
| **20%** | **54%** | roughly half — genuine backstop |
| 15% | 41% | minority — narrow backstop |

Recommend **r = 20%**, sellable as "the estate tax survives at half its old rate, purely as a minimum tax, and only reaches estates the framework doesn't otherwise touch."

**Revenue (rough, order-of-magnitude — needs real modeling):**

Build: ~3,000 estates/yr above a $15M exemption; back into aggregate gross estate from current receipts ($20-25B at ~15-17% effective on the taxable base -> base ~$130-165B, plus ~$45B of aggregate exemption) -> gross estate **$150-250B/yr**, taxable-above-exemption **$105-205B**. Floor gross at 20% = **$21-41B**. LGF at death on those same estates (gain share ~45-55%, ~35% effective) = **$25-40B**. Incremental revenue is the estate-by-estate `sum of max(0, F_i - T_i)`, not the difference of aggregates — positive because gain share is widely dispersed; roughly 20-35% of floor gross.

**Incremental: ~$5-12B/yr at r = 20%** (~$3-7B at 15%, ~$8-18B at 25%). Effect on the essay's table: the "Estate tax repeal: -$20-25B" reduction line becomes roughly **-$10-18B**, moving net framework revenue from $45-170B (mid $108B) to about $50-182B (mid ~$116B).

**Conclusion: the floor is not a revenue play** — under 10% of the package midpoint. Its value is closing the all-principal hole and defusing the double-taxation attack. If revenue is the goal, inheritance-as-income is where it lives.

**Data caveat that matters beyond this question:** Form 706 does not collect basis (there's no need under step-up), so unrealized-gain share by estate size is **not directly observable** — every figure here and every published estimate is modeled. That softness applies equally to the essay's existing "$75-100B death as realization" line. IRS SOI estate studies give asset *composition* by estate size, which is the best available proxy and the right input if this gets modeled properly in `internal/analysis/calibration_comparison.xlsx`.

### Attribution fix + the Walton test (2026-08-27)

**Inheritance-as-income is Lily Batchelder's proposal, not Ray Madoff's.** Batchelder (NYU), "Leveling the Playing Field between Inherited Income and Income from Work through an Inheritance Tax," Hamilton Project — **already cited correctly in the essay at :166.** Madoff (BC Law) works on charitable structures and perpetual dynasty wealth (*The Second Estate*, DAF payout reform, Initiative to Accelerate Charitable Giving) — she is the right cite for the *charitable* exit, and she is a live outreach target (backlog #5, Q4). Attributing a colleague's signature proposal to her in a published essay, three lines from a correct Batchelder footnote, would be a bad way to open that conversation. *Verify before publishing.* Madoff can be cited alongside on the dynasty-perpetuation framing, not for the mechanism.

**Walton test — does LGF let them off easy? Partly yes, and the floor is useless here.**

Generational math, zero-basis stock, no consumption. Start W (basis 0), death-as-realization at 37%, heirs take fresh basis, grow at g for T years:

`heirs receive = 0.63W x [0.63e^(gT) + 0.37]`

At g = 3% real, T = 30 yrs: e^0.9 = 2.46 -> **$100B becomes $121B per generation.** LGF slows the compounding from 2.46x to 1.21x — it does not shrink the fortune. Each death collects ~$37B (vs ~nothing today after planning), so LGF is enormously more effective than current law, but perpetual transmission survives.

**The 20% floor does nothing for the Waltons.** Their gain share is ~100%, so `max(0.37G, 0.20(E-X))` always resolves to LGF. The floor catches the *cash-rich* dynasty (sold the business a generation ago, holds Treasuries), never the *appreciation-rich* one. Worth stating plainly: the floor and the Waltons are disjoint problems.

**Inheritance-as-income is the only tool that reverses it.** Same model with a 37% recipient-side tax stacked on: per-generation multiple falls to ~0.76 — the fortune **shrinks ~24% per generation**. That is the quantified case for the IOU, and it is honest: the framework taxes appreciation well and does not break dynasties.

**Editorial note:** essay :166 already does 80% of what Matt wants — it names Batchelder, links the Hamilton Project paper, and says "nothing here forecloses it, and nothing here requires it." The ask is only a valence shift from *deliberately silent* to *out of scope here, but worth pursuing*, plus the honest admission that LGF alone leaves dynastic compounding intact. Don't rewrite the paragraph; edit its last two sentences.

### Floor rate: 25% works; the risk-taking worry is real but misnamed (2026-08-27)

**1. No perverse incentive toward safe assets — LGF tilts *toward* risk.** Treasuries throw off interest taxed annually at ordinary rates; equities defer all tax to death. $100M over 30 yrs: Treasuries at 4% nominal taxed annually at 37% -> 2.52% after-tax -> **$211M**, and ~$0 owed at death (reinvested after-tax interest raises basis, so gain ~= 0). Equities at 7% -> $761M, gain $661M, tax $245M -> **$516M to heirs.** Deferral means LGF's effective annual rate on appreciation is *below* the ordinary rate on interest. This is a feature and it serves Tenet 4.

**2. But Matt's instinct is right with the wrong instrument: it's municipal bonds, not Treasuries.** Munis are federally tax-exempt, produce no appreciation, and therefore generate **zero** LGF liability at death. With the estate tax repealed, a $500M muni portfolio is a **perpetual, entirely tax-free dynasty vehicle** — no annual tax, no realization, no transfer tax, forever. $500M at 3.5% -> $281M real... more importantly, lifetime federal tax = $0. A wealth-maximizer still prefers equities ($516M vs $281M), so this is **not a perverse incentive — it is a zero-tax hole**, and risk-averse old money is exactly the profile that takes it. This is the strongest argument for a floor and it's better than the cash/Treasuries version. Floor at 25% collects $121M from that estate instead of nothing.

**3. 25% is fine — and it breaks none of the published examples.** Crossover: floor binds when gain share < r/0.37, so 25% -> **68%**. Checked against every death example in the essay: $100M/$80M gain (94% share) -> LGF $28M binds, floor $21.25M. $500M/$400M (82%) -> LGF $147M binds, floor $121M. $15M estate -> E-X = 0, floor = 0, LGF binds. **All published numbers survive unchanged at 25%.** Effective rates stay progressive ($50M/40%-share estate: floor 17.5%; $500M dynasty: 29.4%). Revenue ~$8-18B vs ~$5-12B at 20%. Recommend **25%** over 20% — same architecture, more revenue, no rewrite of published figures, and "we cut the estate tax rate from 40% to 25% and made it a backstop" is a clean line.

**4. But the "less avoidable" claim is half wrong, and this is the real weakness.** Realization-at-death makes the *income tax* side unavoidable — the gain follows the asset regardless of what trust holds it. The **floor does not inherit that protection**, because it is computed on the **gross estate**, which is precisely the number GRATs, ILITs, FLP/LLC discounts and charitable lead trusts are engineered to shrink. A GRAT remainder sits outside the gross estate -> outside the floor base. Life insurance in an ILIT -> outside. So the floor inherits the same avoidance machinery that makes today's estate tax collect 10-15% instead of 40%, which means the $8-18B estimate is optimistic.

Partial mitigation, fairly stated: the *prize* is much smaller than today (a 25% floor on top of LGF already collecting 37% of appreciation, vs. a 40% tax avoided outright), and LGF's dual-purpose valuation (:162) does police discounts, so the planning response should be materially muted relative to current behavior. But it is not zero, and the floor should not be sold as un-gameable.

**Implication:** the floor is a partial backstop that closes the muni/cash hole for families that don't aggressively plan. It is not a dynasty-breaker and it is not un-avoidable. Both of those still point at inheritance-as-income (recipient-side base is much harder to shrink), reinforcing the strengthened Batchelder IOU rather than substituting for it.

### Inheritance-as-income: the fork Matt hasn't resolved (2026-08-27)

**Gift for the essay — the framing is already law for found money.** Treasure trove is gross income under Treas. Reg. Sec. 1.61-14; *Cesarini v. United States* (N.D. Ohio 1969, aff'd 6th Cir. 1970) held $4,467 found in a used piano taxable in the year of discovery. So: *find $4,467 in a piano, that's income; inherit $50 million, that's not.* Matt's paid/found/inherited framing isn't an analogy — the code already does two of the three. *Verify citation before publishing.*

**The fork: donor-side vs recipient-side.** Rule 3 currently taxes the **donor** on lifetime gifts ("the donor pays tax on unrealized gains at the time of transfer"). Inheritance-as-income taxes the **recipient**. A lifetime gift and a bequest are the same economic event at different times — taxing one at the donor and the other at the recipient is exactly the kind of asymmetry the project exists to delete. Matt has to pick a side; "hint and punt" doesn't survive contact with this.

**Recipient-side for both would SIMPLIFY the framework, not complicate it:**
- Rule 3 realization events drop from four to **two** (sale, borrowing).
- Gift and death both become: *receiving wealth from another person, above a lifetime exemption, is ordinary income to the recipient at FMV.*
- Runs entirely on existing income tax machinery — no Form 706, no unified credit, no GST, no valuation-discount regime, no estate tax at all.
- Step-up dies cleanly: the heir is taxed on the **full value**, not the gain, so basis-at-FMV is not a loophole — it's the normal rule for anything received as income. **Best analogy: inherited assets get treated exactly like vested RSUs** (taxed on FMV at receipt, basis = FMV). That sentence lets Matt give heirs FMV basis without ever saying "we kept step-up."

**Do not stack it on death-as-realization — it substitutes for it, and collects more.** $100M estate, $80M gain, $2M exemption, 37%:

| Design | Collected | Effective |
|---|---|---|
| LGF death-realization only (published) | $28.1M | 28% |
| Inheritance-as-income only | **$36.3M** | 36% |
| Both stacked | $54.0M | 54% |

Taxing the whole receipt beats taxing only the gain. Stacking reproduces the estate tax problem with a worse optic, because now the same dollars are literally in the *income tax* base twice.

**It also makes the 25% floor unnecessary.** The muni-dynasty hole exists only because LGF taxes appreciation. A $500M all-muni estate under inheritance-as-income: heir owes 0.37 x $498M = **$184M**, versus $121M from the floor and $0 from LGF. The recipient-side base needs no backstop because it doesn't care what form the wealth took.

**Design items to settle if pursued:** lifetime exemption (symmetry argument for the framework's existing **$2M / $4M** — possibly a single combined lifetime exemption across gains and inherited income); bunching relief for a one-time large receipt (same logic as the retiree example that motivated the lifetime gains counter); the 15-year lien ports over for illiquid inheritances; spousal transfers; trust distributions with no identifiable recipient.

**Honest scoping warning:** this is not a hint-and-punt. Resolving the fork toward recipient-side rewrites Rule 3, removes death and gift from the realization list, retires the estate tax question entirely, and moots the floor. That is **v2 of the framework**, not a companion essay. Decide deliberately whether the IOU reads as "a tax we might add later" (safe, current posture) or "the architecture may get rebuilt around this" (true, but a very different promise to have made in a published flagship).

### Matt is right to stack — and the substitution argument above was wrong (2026-08-27)

**Retracting the "inheritance-as-income substitutes for death-as-realization" recommendation.** It breaks earned-vs-appreciated neutrality, which is the whole point of the framework. Test with a $2M exemption at 37%:

| | Parent's tax | Heir's tax | Total |
|---|---|---|---|
| **A. Parent earns $100M in wages**, dies with $63M cash (no gain, LGF = $0) | $37M | $22.6M | **$59.6M** |
| **B. Parent's stock appreciates $0 -> $100M**, dies | $35.5M | $23.1M | **$58.6M** |
| B under *inheritance-only* (no death realization) | $0 | $36.3M | **$36.3M** |

Stacking produces parity between wealth that was earned and wealth that merely appreciated (~$59M either way). Dropping the realization leg undertaxes appreciated wealth by ~$23M — **that is stepped-up basis returning through the back door.** Both legs are load-bearing. Matt's "orthogonal" read is correct: it is not one dollar taxed twice, it is two taxpayers' income taxed once each.

**But fix the analogy — as stated it describes something that doesn't happen.** Wages are *deductible* to the corporation; a company pays no entity-level tax on money it pays out as wages. The only true corporate double tax is on **dividends**, and that is the single most criticized feature of the corporate tax — the thing Australia and NZ fixed with imputation credits and the US mitigates with preferential qualified-dividend rates. Citing it as precedent invites "you're defending your design with the one thing everyone agrees is broken."

**Much better analogy, exactly parallel and unimpeachable:** *You sell appreciated stock and pay capital gains tax. You use the proceeds to pay your contractor. The contractor pays income tax on the payment.* Two taxes, two people, one transaction chain — and nobody calls it double taxation. Realization tax on the owner, income tax on the recipient. Use this instead.

**The family farm — the actual math.** $10M farm, $8M gain, single decedent, $2M exemptions on both legs:
- LGF at death: ~$1.48M (18.5% effective on the gain, thanks to exemption + phase-in)
- Estate net $8.52M -> inheritance-as-income: 0.37 x $6.52M = **$2.41M**
- **Combined $3.89M on a $10M farm = 39%.** Farm income at 3-5% of asset value = $300-500K/yr; the 15-year lien costs $259K/yr — most of the farm's cash flow. Survivable on paper, brutal in a bad year, and *fatal in an ad.*

This is where "orthogonal" is weakest: an illiquid asset is hit on both legs with no cash available at either. Design fix if pursued is **coordination, not two independent exemptions** — a combined lifetime exemption, a Sec. 2032A-style special-use valuation port, or family-rollover deferral until the asset leaves the family. Worth noting for the eventual essay: **the family farm is already largely a rhetorical device** — a very small share of farm estates owe estate tax under current exemptions (USDA ERS has the figure; verify before citing).

**Conclusion: punt is right, but for a better reason than "the politics are hard."** The framework at LGF-only puts the farm at ~15% effective, which is defensible on its own. Adding the second leg without first calibrating a coordinated exemption takes it to 39% and hands opponents the Death Tax ad with a real example behind it. Sequence: ship LGF, calibrate the combined exemption, then make the inheritance case on its own terms.

---

## Substack -> Git sync of the flagship, 2026-08-27 (DONE)

First attempt used a WebFetch of the live URL which returned a **stale cached render** (showed the pre-June charitable section, no Batchelder scope note, no revenue tables). Those edits were reverted. Sync redone from Matt's verbatim paste. **Lesson: do not trust WebFetch on Substack for sync work — ask for a paste.**

**Applied to `lifetime-gains-essay.md`:**
- **Rule 3 restructured** — principle is now "Gains are realized when the asset ownership changes"; bullets reordered to Sale / Gifts / Death; **borrowing broken out of the list into a following paragraph** ("In addition, leveraging an appreciated asset as collateral also triggers realization. The owner is choosing to defer liquidation while still enjoying the benefit of appreciation."). This is the one-principle-plus-one-backstop structure proposed earlier in this file.
- **"What About Charitable Giving?" section deleted entirely**, and the Rule 3 charity carve-out line deleted. Charity is now covered *implicitly* by the ownership-change principle.
- **"What This Settles" section deleted**; carried interest promoted to a bullet in What Falls Away; "Plus seven more" delinked.
- **What Falls Away restructured** — software-engineer paragraph moved to the top and merged with the 10-15% claim; wealth-tax bullet removed and replaced by a closing paragraph ("I believe this proposal obviates the need for a wealth tax"); Stepped-up basis moved to first bullet.
- Intro rewritten (Tax Refactor framing first, "systems thinking", "So let's refactor it!"); Rule 1 stakes-in-the-ground note; Rule 2 condensed; Rule 5 parenthetical; Wealth Tax Question paragraphs reordered; estate-tax "which is a feature" added.

**Typos fixed rather than copied down (Substack still has these — fix there):**
1. "generate an hundreds of billions per year" -> "generate hundreds of billions"
2. "avoid ever paying taxes on a lifetime gains" -> "on a lifetime of gains"
3. "borrowing leveraging an appreciated asset as collateral" -> "leveraging an appreciated asset as collateral"
4. "so when the heir will now realize a bigger gain" — Substack broke this sentence; Git keeps "so when the heir eventually sells, they realize a bigger gain"
5. "it lookslike a tax on dynastic wealth" -> "it *looks* like"

**Substantive issues introduced by the Substack edits (need Matt's call):**
- **Revenue claim contradiction.** Intro now says "hundreds of billions per year in net new revenue"; the revenue section still says **$45B-$170B, midpoint ~$108B**, and the anchors table tops out at $195B. "Hundreds of billions" is not supported by the essay's own numbers.
- **Charity is now unstated, and the spec contradicts it.** With the section gone, charitable donation of appreciated assets is a realization event only *by implication* of "asset ownership changes." Meanwhile `technical_spec.md:72,101-113,363` still explicitly says charitable transfers are **not** realization events with a **basis-only deduction** — and the essay says the spec governs. Spec must be updated or the essay is self-contradicting on the most contested point in the framework.
- **The Batchelder scope note survived** in the estate tax section, so the inheritance-as-income IOU is intact (it is absent from the Substack version — reverse-sync candidate).
- **Buy-borrow-die / "billionaires pay a lower rate than teachers"** framing was dropped from the intro along with the old opening paragraph. Deliberate? It was the essay's strongest hook.

Git-only content preserved (absent from Substack, do NOT let a future sync delete): Batchelder scope note, full revenue tables, relative Jekyll links, the framework PNG, `substack_slug`/`substack_synced` frontmatter.

**Frontmatter `substack_synced` left at 2026-07-20** — the two are still not identical (typo fixes + Git-only content), so it is not a clean sync date.
