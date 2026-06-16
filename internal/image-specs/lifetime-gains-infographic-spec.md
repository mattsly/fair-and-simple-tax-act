# Infographic Prompt for AI Image Generator

> **SPEC IS CURRENT — PUBLISHED PNG STILL NEEDS REGENERATION.** This spec now matches the canonical figures in the published Lifetime Gains essay ("America's Most Expensive Technical Debt, Part 1"): $2M exemption / $6M ceiling per person ($4M / $12M married), both CPI-indexed; rate pegged to the top ordinary rate (currently 37%). The live image at `assets/lifetime-gains-framework.png` was generated from the old $2.5M / $10M spec and must be regenerated from the prompt below.

Create a clean, minimal infographic on a white background. No clip art, no icons, no flags, no illustrations. This should look like a chart from The Economist or a policy brief, not a campaign ad.

**Title** (top left, bold, dark charcoal): "The Lifetime Gains Framework"
**Subtitle** (below title, lighter gray): "How the tax rate changes with cumulative lifetime capital gains"

**The chart** (takes up 70% of the image):

A line chart with clearly labeled axes.

X-axis label: "Cumulative Lifetime Capital Gains"
X-axis tick marks at: $0, $2M, $4M, $6M, $10M, $15M, $20M

Y-axis label: "Marginal Tax Rate"
Y-axis tick marks at: 0%, 10%, 20%, 23.8%, 30%, 37%

**Line 1 (the framework)** — bold, dark blue or teal:
- Flat at 0% from $0 to $2M
- Rises linearly from 0% at $2M to 37% at $6M
- Flat at 37% from $6M onward

**Line 2 (current law)** — dashed, gray or light red:
- Flat at 23.8% across the entire chart
- Labeled "Current Law: up to 23.8% (top earners; most pay 0–15%)"
- Note for the designer: 23.8% is the *top* combined rate (20% LTCG + 3.8% NIIT), reached only above ~$545K income (single) / ~$614K (married) in 2026. It is the high-earner benchmark, not what a typical filer pays today. Most of the households the framework helps are currently in the 0% or 15% bracket, so this line overstates the dollar savings for them while remaining the correct comparison for the high-end / crossover story.

**Shaded zones** (subtle, low opacity):
- $0 to $2M: light green fill, labeled "Tax-Free Zone"
- $2M to $6M: light amber fill, labeled "Sliding Scale"
- $6M+: light coral/red fill, labeled "Full Rate"

**The intersection point** where the framework line crosses the current law line (approximately $4.6M) should be marked with a small dot and labeled "Crossover: ~$4.6M"

Below the crossover label, a small annotation: "Below this point, the framework's marginal rate is lower than current law's top rate; above it, higher. (On total tax paid, the framework stays cheaper well past this point — a $6M filer pays ~$740K vs. ~$1.43M at a flat 23.8%.)"

**Bottom bar** — three compact stats in a horizontal row, small text:

"95%+ of Americans pay the same or less" | "$45–170B in annual deficit reduction" | "Eliminates 10–15% of the Internal Revenue Code"

**Footer** (very small, gray): "mattsly.com/fair-and-simple-tax-act · Thresholds are proposed starting points ($4M / $12M married), indexed to CPI"

**Style requirements:**
- White or off-white background
- Clean sans-serif font (Inter, Helvetica, DM Sans, or similar)
- No gradients, no drop shadows, no 3D effects, no decorative elements
- Color palette limited to: dark charcoal text, teal/blue for the framework line, gray for current law, green/amber/coral for zone fills
- Aspect ratio: 16:9 landscape for social sharing
- Overall feel: data visualization, not marketing material