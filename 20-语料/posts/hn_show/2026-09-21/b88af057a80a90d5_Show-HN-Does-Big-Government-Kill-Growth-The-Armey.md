---
type: "corpus"
item_id: "b88af057a80a90d5"
title: "Show HN: Does Big Government Kill Growth? The Armey Curve Tested (151 Countries)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47961656"
project_url: "https://julienreszka.github.io/economic-simulator/armey-curve.html"
author: "julienreszka"
published_at: "2026-04-30T12:52:49Z"
captured_at: "2026-09-21T02:52:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_julienreszka
  - story_47961656
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Does Big Government Kill Growth? The Armey Curve Tested (151 Countries)

> [!info] 一句话导读
> ← Back to All Curves

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47961656>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：julienreszka　|　发布：2026-04-30T12:52:49Z
> 项目链接：<https://julienreszka.github.io/economic-simulator/armey-curve.html>
> 采集：2026-09-21T02:52:27+08:00　|　id：`b88af057a80a90d5`

## 正文

← Back to All Curves
English
 Français
Does Big Government Kill Growth? The Armey Curve Tested on 151 Countries
📖 ~28 min read
 ·
 Julien Reszka · Last updated 2026-04-30
 ·
 Jump to the criterion →
What you get from this page: a straight answer to whether your
 tax money is buying growth or quietly slowing it down, an
 interactive simulator
 that estimates how much extra growth a 5-point spending cut could deliver in
 your country, and a clear rule for when government should actually
 intervene — without an econ degree.
The short version: the Armey Curve — the textbook claim that there's a
 "sweet spot" for government spending around 15–25% of GDP — does
 not hold up. World Bank data across 113 countries shows a
 Power Law fit with R² = 0.4219
 (approx. 95% CI: 0.28–0.56 ) , while the
 traditional Quadratic Armey Curve achieves only
 R² = 0.3856 — less explanatory power, and no evidence of the
 predicted upturn at low spending levels . The relationship is
 monotonically negative across the entire observed range — every additional
 point of spending, on average, costs growth.
THE ARGUMENT IN THREE MOVES
Government slows aggregate economic activity. The
 simulator shows the relationship is monotonically
 negative — no Armey-curve sweet spot at 15–25% of GDP.
So the policy question isn't "how much?" — it's "on what?"
 If government is structurally a brake, you don't minimise it, you
 aim it . Brakes are useful precisely because they slow things down.
Aim it by an objective rule, not by taste. The
 Inclusive Wealth Criterion : brake an activity only if it
 imposes a net wealth loss on external parties AND the brake is cost-effective.
 Three of four cells tell government to do nothing.
Shortcuts:
 Growth gain from a 5-point spending cut ·
 Spending cut needed to reach a target growth rate ·
 Freeze scenario: outgrow the spending
Interactive Armey Curve Simulator
Curve Model Type:
Power Law (β₀ × s⁻ᵅ)
 Log-Linear (β₀ − α × ln(s+1))
 Quadratic (Traditional Armey)
 Free Quadratic (Unconstrained)
 Linear Decline
 Inverse (1/x decline)
 Exponential Decay
Power Law: steep initial drop, flattens gradually (α controls
 steepness); Log-Linear: diminishing marginal harm, derived from
 Cobb-Douglas production theory; Quadratic: inverted-U with optimal
 peak; Linear: constant decline; Inverse: steep initial harm that
 levels off; Exponential: accelerating damage
Intercept (β₀, base growth, e.g., 2):
Natural growth rate without government intervention
Linear coefficient (β₁, positive, e.g., 0.5):
Initial positive effect of government spending
Quadratic coefficient (β₂, negative, e.g., -0.01):
Diminishing returns effect (must be negative)
Linear slope (e.g., -0.3):
Rate of change in growth per percentage point of government
 spending (can be positive or negative)
Vertical offset a (e.g., 0):
Vertical offset in the 2-parameter inverse model: growth =
 b/spending + a
Linear coeff β₁ (auto-fitted):
Linear coefficient in y = β₀ + β₁·s + β₂·s² — auto-fitted, can be any sign
Quadratic coeff β₂ (auto-fitted):
Quadratic coefficient — positive = U-shape, negative = inverted-U
Decay rate (e.g., 0.3):
Exponential decay rate: growth = intercept * e^(-decay *
 spending)
Exponent (α, e.g., 1.5):
Power law exponent: growth = β₀ × spending^(-α). α=1 approximates
 inverse; higher α steepens the drop.
Log slope (α, e.g., 2.5):
Log-linear slope: growth = β₀ − α × ln(spending+1). Steep initial
 drop that flattens, never goes sharply negative in realistic
 range.
⚙ Auto-fit parameters
Finds β₀ and the secondary parameter that minimize AIC for the
 selected model and current data.
Show Real Country Data:
All Countries
 Developed Countries
 Developing Countries
 Hide Country Data
Exclude resource-dependent ◆
Exclude externally funded ▲
Exclude conflict/fragile states ✕
Exclude GDP-distorted ★
Also exclude ±1 SE model-residual outliers (exploratory) ■
Real-world data from
 World Bank API
 ( Government expenditure
 &
 GDP growth )
Time Period for Averaging:
Recent (2018-2023) - Post-crisis stability
Decade (2014-2023) - Full business cycle
Long-term (2010-2023) - Including financial crisis
Structural (2005-2023) - Long-term trends
Extended (1995-2023) - Maximum coverage
Longer periods smooth volatility but may include outdated
 regimes
Loading...
Minimum Years of Data per Country:
1 year (maximum coverage)
 3 years (default)
 5 years
 7 years
Countries with fewer years of available data are excluded. Higher thresholds improve reliability but reduce coverage.
Highlight Specific Country:
No country highlighted
Select a country to highlight with a red dot
Chart displaying the Armey Curve with government spending on x-axis
 and GDP growth rate on y-axis
Model Fit Ranking
#
 Model
 R²
 95% CI (R²)
 AIC (lower = better)
 p-value
 N
 Coverage (±1 SE)
1
 Power Law ✓
 0.4219
 [0.28, 0.55]
 53.29
 <0.001
 113
 69%
2
 Inverse
 0.4192
 [0.28, 0.55]
 53.82
 <0.001
 113
 70%
3
 Log-Linear
 0.4167
 [0.27, 0.55]
 54.31
 <0.001
 113
 69%
4
 Exponential
 0.4106
 [0.27, 0.54]
 55.48
 <0.001
 113
 68%
5
 Free Quadratic
 0.4083
 [0.27, 0.54]
 57.92
 <0.001
 113
 70%
6
 Linear
 0.3892
 [0.25, 0.53]
 59.51
 <0.001
 113
 68%
7
 Quadratic
 0.3856
 [0.24, 0.52]
 62.17
 <0.001
 113
 67%
Each model is auto-fitted to find its best-case parameters before
 computing AIC/R² — a fair competition at peak performance. Bold row
 = currently selected model. 95% CI computed via Fisher’s
 Z transformation on the sample correlation (N = 113,
 standard exclusions applied).
R² (R-squared)
Measures how well the curve explains the variation in growth rates
 across countries. A perfect fit = 1.0. A score of 0 means the
 model is no better than just predicting the average growth rate
 for every country.
 Negative values mean the model is worse than that
 baseline.
 When models are auto-fitted across 113 countries (resource-dependent, externally-funded, conflict/fragile, and GDP-distorted countries excluded), the top models reach R² ≈ 0.42 —
 meaning government spending % explains roughly 42% of the
 variation in growth. Note that
 Power Law and Inverse are tied on combined R² (0.4913); Power Law edges ahead on AIC (53.29 vs 53.82)
 — it fits the spending–growth relationship well across diverse economies. Each exclusion category has a specific theoretical justification: resource-dependent economies grow via commodity windfalls unrelated to government size; externally-funded states have aid-distorted budgets; conflict/fragile states have suppressed growth from instability; GDP-distorted economies have artificially inflated or deflated GDP figures.
AIC (Akaike Information Criterion)
Ranks competing models by balancing how well they fit the data
 against how many parameters they use (simpler models are
 rewarded). Lower AIC = better model. Unlike R²,
 AIC is useful for comparing models even when none of them fits
 well — it tells you which is the least bad option. With
 113 countries (standard exclusions), Power Law (AIC 53.29) and Inverse (AIC 53.82) are
 effectively tied, with Log-Linear (54.31) close behind. Exponential
 (AIC 55.48) and Quadratic (85.30) trail — the constrained Armey Curve
 shape finds no empirical support in this dataset.
p-value
The probability of observing a fit this strong (or stronger) by
 chance alone, assuming government spending has no real effect on
 growth. Lower p-value = stronger evidence against the
 null hypothesis. A threshold of 0.05 is conventional; all
 models except Quadratic show p < 0.001, meaning there
 is less than a 1-in-1000 chance the observed relationship is a
 statistical accident. The p-value is derived from an F-test on the
 regression: F = (R² / k) / ((1 − R²) / (N − k − 1)), where k is
 the number of fitted parameters.
N (Sample size)
The number of countries included in the regression for the current
 filter and time-period settings. Larger N increases statistical
 power and makes both R² and p-value estimates more reliable.
 Excluding resource-dependent or externally-funded countries reduces
 N and may change all fit metrics — a drop in R² after exclusion
 means those countries were pulling the curve in a predictable
 direction.
What else explains growth beyond government spending?
Greedy stepwise regression across 27 candidate variables (macro, governance, human capital, finance, structural) added one at a time to the power-law spending baseline.
 Each row shows the single best remaining variable at that step. The ceiling — stacking all 17 variables that clear the contribution threshold — is R² ≈ 0.680 .
 The remaining ~32% is not recoverable from standard World Bank data.
 Notably, all 6 WGI governance indicators dropped out again — no marginal gain after income, investment, education and population are controlled.
 Military spending, R&D, and remittances all entered — for structural reasons explained in the interpretation column.
#
 Variable
 Marginal R²
 Cumul. R²
 N
 Slope
 Interpretation
—
 Gov. spending (power law)
 —
 0.4219
 113
 —
 Baseline
1
 R&D spending % GDP
 +0.0728
 0.4947
 95
 −0.435
 Negative slope: high-R&D countries are mature economies growing slowly — captures a development-stage effect not fully absorbed by initial income
2
 Military expenditure % GDP
 +0.0522
 0.5468
 98
 +0.393
 Positive slope: may reflect defense-led investment or reverse causality (richer/faster countries can afford more military)
3
 Capital formation % GDP
 +0.0272
 0.5740
 105
 +0.049
 Investment rate — countries that invest more grow faster
4
 Population growth %
 +0.0192
 0.5933
 113
 +0.186
 More people = more total output (note: total GDP growth, not per-capita)
5
 ToT volatility (SD of annual % changes)
 +0.0175
 0.6107
 113
 −0.028
 Terms-of-trade volatility (SD of annual % changes) — exogenous external shock exposure; uncorrelated with development cluster, captures commodity-price risk channel
6
 Domestic credit (private) % GDP
 +0.0138
 0.6245
 113
 −0.004
 Financial depth — but negative slope suggests over-financialisation drag at high levels
7
 Tertiary enrollment %
 +0.0117
 0.6363
 110
 +0.006
 Human capital stock — higher education feeds productivity growth
8
 ln(GDP/cap) — convergence
 +0.0077
 0.6439
 113
 −0.097
 Beta-convergence: poorer countries grow faster conditional on spending
9
 Remittances received % GDP
 +0.0095
 0.6534
 112
 −0.023
 Negative slope: remittances flow to slow-growing economies as a safety valve, not a growth engine
10
 Tax revenue % GDP
 +0.0066
 0.6601
 111
 +0.024
 Fiscal capacity signal; positive slope may capture institutional quality
11
 FDI inflows % GDP
 +0.0041
 0.6642
 113
 +0.010
 Foreign investment brings capital and technology transfer
12
 Renewable energy share %
 +0.0042
 0.6684
 113
 +0.004
 Renewable energy share — positive slope reflects energy diversification and long-run efficiency gains
13
 Current account balance % GDP
 +0.0029
 0.6713
 113
 +0.014
 Surplus countries save and invest more domestically
14
 WGI Voice & Accountability
 +0.0017
 0.6729
 113
 −0.077
 Accountability and freedom of expression correlate with durable institutions
15
 WGI Regulatory Quality
 +0.0033
 0.6763
 113
 +0.109
 Business-friendly regulation supports productive entry and exit
16
 WGI Control of Corruption
 +0.0020
 0.6782
 113
 −0.075
 Clean institutions lower transaction costs and attract capital
17
 Life expectancy
 +0.0017
 0.6799
 113
 +0.009
 Healthy workers are more productive
—
 Trade openness % GDP, Inflation %, WGI Rule of Law, WGI Govt Effectiveness, WGI Political Stability, Secondary school enrollment %, Urban population growth %, Electricity access % population, Energy use per capita (kg oil eq.), Electric power consumption (kWh/cap)
 <0.003 each
 —
 —
 —
 Dropped — no marginal gain after the above variables are controlled
113 countries, 2005–2023, power-law baseline, standard exclusions. Greedy stepwise over 27 candidate World Bank indicators. Threshold: marginal R² > 0.003. Source: scripts/ceiling-r2.mjs . Updated by scripts/update-static-tables.mjs .
Stage 2: Spending + R&D + Military + Capital Formation + Population Growth + Domestic Credit + Tertiary Enrollment + Initial Income
 — combined-R² ranked model comparison
The spending curve above predicts a growth rate for each country. The residual is how far off that prediction is (actual − fitted).
 These charts ask: do R&D, military expenditure, capital formation, population growth, domestic credit, tertiary enrollment, initial income, and terms-of-trade volatility systematically predict the errors?
 All eight are controlled jointly via eight-variable OLS. Each chart shows the partial slope — the effect of one variable holding the other seven at their means.
 A positive capital formation slope reflects the investment-growth channel.
 A positive domestic credit slope would indicate financial depth matters beyond the spending level.
 A negative income slope (poorer countries grow faster conditional on spending) is expected textbook beta-convergence.
 Note: military expenditure, R&D, and tertiary enrollment are all components of total government spending (the Stage 1 x-axis). Their Stage 2 coefficients should be read as composition effects — among countries with the same total spending share, how does allocating more of it toward military (vs. other uses) correlate with growth? This is a guns-vs-butter trade-off coefficient, not an additive one.
 The table below ranks all models by combined R² on the joint subset.
Scatter plot of Armey model residuals against R&D spending % GDP
Scatter plot of Armey model residuals against military expenditure % GDP
Scatter plot of Armey model residuals against gross capital formation % GDP
Scatter plot of Armey model residuals against population growth %
Scatter plot of Armey model residuals against terms-of-trade volatility (SD of annual % changes)
Scatter plot of Armey model residuals against domestic credit to private sector % GDP
Scatter plot of Armey model residuals against tertiary enrollment rate %
Scatter plot of Armey model residuals against log GDP per capita
Stage 2 — Best combined fit (spending + R&D + military + income)
#
 Model
 R²(spending)
 Combined R²
1 Inverse ✓ 0.419 0.625
2 Power Law 0.422 0.623
3 Log-Linear 0.417 0.611
4 Free Quadratic 0.408 0.605
5 Exponential 0.411 0.594
6 Linear 0.389 0.590
7 Quadratic 0.386 0.567
Combined R² = R²(spending+R&D+military+income+capital formation+population growth) evaluated on the joint subset with all five controls. Bold row = current model. 2005–2023, standard exclusions.
⬇ Download data as CSV
Downloads the currently visible country data as a CSV file.
⬇ Download fallback-data.json
Exports all 4 time periods as a drop-in replacement for fallback-data.json . Requires data to be loaded from the live API.
The Armey Curve Theory vs. Reality
The theory seemed reasonable: The Armey Curve
 suggested an inverted U-shaped relationship between government
 spending and economic growth. Named after economist Richard Armey,
 this curve claimed there exists an optimal level of government
 spending that maximizes economic growth.
But here's the problem: When you actually look at
 real-world data from dozens of countries over multiple decades, the
 theory doesn't hold up. Countries with lower government spending
 consistently achieve higher growth rates, while high-spending
 countries cluster in the low-growth zone.
What the data actually shows: Instead of a neat
 U-shaped curve with an "optimal" government size around 20-30% of
 GDP, we see patterns that better fit power law (s⁻ᵅ) or inverse
 (1/x) models - suggesting that any government spending
 beyond the absolute minimum reduces economic growth.
What the Traditional Theory Claimed
The Armey Curve theory proposed three distinct phases:
Rising Phase (0-20%): Government spending
 supposedly provides essential infrastructure, legal framework, and
 public goods that enhance productivity and growth
Peak (20-30%): The mythical "optimal" government
 size where growth is supposedly maximized
Declining Phase (30%+): Excessive spending
 creates inefficiencies, crowds out private investment, and reduces
 growth through higher taxes and regulatory burden
What the Data Actually Shows
There is no "rising phase." Countries with minimal
 government spending (Singapore ~17%, historically Hong Kong ~15%)
 consistently achieve solid growth. Meanwhile, countries that spend
 30-45% of GDP (most of Europe) cluster in the low-growth zone
 (0.5-1.5%).
There is no clear "optimal" zone. The data doesn't
 show clustering around 20-30% spending. Instead, we see a consistent
 negative relationship: lower spending = higher growth.
The relationship is better described by power law or inverse
 decline,
 not a quadratic curve. The data shows government spending is
 harmful to GDP growth from the first dollar — but that's precisely
 the point. The defensible use of government is as a deliberate
 brake on economic activity we don't want: pollution, overfishing,
 systemic financial risk. Slowing the economy is the feature, not
 the bug, in those applications.
The Historical Arc Confirms the Pattern
The simulator window (2005–2023) captures only a narrow slice of
 history in which all major economies already operate above 25% of
 GDP. But the pre-WWII record is instructive: in 1913, government
 spending averaged roughly 10–15% of GDP across
 Western Europe, and annual per-capita growth ran at
 ~2–3% — consistent with where the power law curve
 projects at those spending levels. The post-war expansion of the
 state shifted every major Western economy rightward along the curve
 into the low-growth zone. Where high-spending economies have
 sustained rapid growth, compositional factors — high investment
 shares, catch-up convergence, or off-budget financing — tend to
 account for the exception.
Traditional Theory vs. Empirical Reality
The traditional quadratic theory claimed:
Growth Rate = β₀ + β₁ × Government Spending + β₂ × (Government
 Spending)²
Where β₀ represents baseline growth, β₁ captures supposed initial
 positive effects, and β₂ (negative) represents diminishing returns.
But the data actually fits these patterns much better:
Power Law: Growth Rate = β₀ × (Government
 Spending)⁻ᵅ
Inverse Model: Growth Rate = β₀ / (Government
 Spending + 1)
Exponential Decay: Growth Rate = β₀ × e^(-decay ×
 Government Spending)
The power law model achieves the highest R² of any model tested,
 explaining ~42% of the variation in growth rates among the 113
 countries that pass the standard quality filters (excluding
 resource-dependent, externally-funded, conflict-fragile, and
 GDP-distorted economies). Without those filters the figure is ~24%,
 because the excluded groups add noise without adding signal. In
 cross-country macroeconomics, 42% is an exceptionally strong result
 for a single explanatory variable. For comparison, Robert Barro's
 landmark 1991 growth study — one of the
 most cited papers in economics — achieved R² ≈ 0.35–0.50 using
 ten or more variables simultaneously. Most single-variable
 growth regressions explain only 5–15% of variation. Government
 spending alone explaining 42% (or even 24% on the full unfiltered
 sample) means it is, by a wide margin, the single most important
 measurable determinant of cross-country growth differences.
The power law generalizes the inverse model (which is just power law
 with α=1) and captures the steep initial harm of government spending
 that gradually flattens at higher levels. These models all suggest
 there's no "beneficial phase" of government spending - it crowds out
 private investment from day one.
Understanding the Intercept (β₀)
The intercept represents the natural economic growth rate in the
 absence of government intervention. This baseline reflects:
Entrepreneurial Innovation: Natural human
 creativity and problem-solving driving new products and services
Voluntary Exchange: Wealth creation through
 mutually beneficial trade
Capital Accumulation: Private savings and
 investment in productive assets
Knowledge Spillovers: Information sharing and
 learning between economic actors
Competition: Market pressure driving efficiency
 improvements
Specialization: Gains from division of labor and
 comparative advantage
Historical evidence suggests this baseline ranges from 2-4% annually
 in developed economies, representing the economy's natural tendency
 toward improvement when people are free to innovate, trade, and
 invest.
Real-World Policy Implications
If the data is right and the traditional theory is wrong, the policy
 implications are dramatic:
No "Optimal Size" to Target: There's no sweet
 spot to fine-tune toward - just minimize government and maximize
 growth
Every Program Has a Cost: Each government
 program, no matter how well-intentioned, reduces overall economic
 growth
Composition Matters, But Level Dominates: This
 data treats all spending identically — it cannot distinguish
 productive from wasteful programs. But the cross-country pattern
 holds at the aggregate level: countries with smaller governments
 consistently outgrow those with larger ones, suggesting the total
 level is the primary driver
The Public Goods Question: Standard economic
 theory identifies a narrow category of goods (defense, basic rule
 of law, core infrastructure) where market provision may be
 insufficient. This data cannot resolve those debates — it only
 shows that countries with very low aggregate spending still
 achieve strong growth, suggesting private and market alternatives
 can substitute for more services than conventional theory predicts
Government as a Selective Brake: If government
 spending reliably slows economic activity, the implication is not
 only to minimize it — but to aim it deliberately at the parts of
 the economy we want to slow down. River pollution, overfishing,
 antibiotic overuse, and systemic financial risk are all cases
 where unchecked private activity grows at society's expense. A
 government that acts as a targeted brake on these harms can
 improve welfare while keeping aggregate spending — and its drag on
 growth — small
Maximum Reduction Strategy: The best policy is to
 cut government to the absolute minimum needed for basic rule of
 law
Why High-Spending Countries Struggle to Cut
If smaller government means faster growth, why don't high-spending countries simply cut their way to prosperity? The power law curve itself supplies the most under-appreciated answer: the marginal gain from cutting is tiny when you are already on the flat part of the curve.
The mathematics are exact. For the power law model $g = \beta_0 \cdot s^{-\alpha}$ (growth = scale × spending −exponent ) , the marginal growth gain from cutting spending by a small amount $\Delta s$ (a tiny change in spending) at level $s$ is:
$\Delta g \approx \alpha \cdot \beta_0 \cdot s^{-(\alpha+1)} \cdot \Delta s$
In plain English: the growth boost from cutting spending equals the exponent ($\alpha$) times the baseline scale ($\beta_0$) times how flat the curve is at that spending level ($s^{-(\alpha+1)}$) times the size of the cut ($\Delta s$). At high spending the $s^{-(\alpha+1)}$ term is tiny, so the boost is tiny.
The ratio of that gain at a low-spending country ($s_1 = 20\%$) versus a high-spending one ($s_2 = 50\%$) is:
$\frac{\Delta g(s_1)}{\Delta g(s_2)} = \left(\frac{s_2}{s_1}\right)^{\alpha+1} = \left(\frac{50}{20}\right)^{\alpha+1}$
In plain English: the ratio of how much a cut helps at 20% spending versus 50% spending equals $(50/20)$ raised to the power of $(\alpha+1)$. With $\alpha \approx 0.45$, that is $2.5^{1.45} \approx 3.5$ — meaning the same cut is about 3.5× more valuable if you start from a lean government.
At 20% of GDP, the curve is steep. Cutting from 20% to 15% produces a meaningful jump in predicted growth. At 50% of GDP, the curve has flattened dramatically. Cutting from 50% to 45% produces a barely perceptible improvement. With the empirically fitted exponent α ≈ 0.447, the same five-percentage-point reduction delivers roughly 3.5× less growth dividend when you start from 50% versus 20% — and the ratio grows with the spending gap. If α were closer to 1.5 (the simulator default), that multiplier would reach ~10×. Either way, the directional logic is the same: the flatter the curve, the harder it is to make reform politically legible.
This asymmetry creates a political trap. The costs of cutting are immediate and concentrated — public sector jobs lost, entitlement recipients mobilized, contractors lobbying for reinstatement. The growth benefits are diffuse, delayed, and, crucially, small enough to be statistically invisible in the first few years of data. A government that cuts 5 points of GDP from a 50% baseline cannot credibly promise its population a visible boom; the power law says it will get perhaps 0.2–0.3 additional percentage points of annual growth. That is real wealth compounded over decades, but it is not a headline.
Contrast that with the experience of Ireland in the 1980s–90s or Sweden in the early 1990s: both cut from high bases, but their recoveries were amplified by other tailwinds (EU single market access, currency devaluation, rapid catch-up from deep recessions) that made the growth payoff visible and large. The power law contribution was real, but it was packaged with other forces. Without those tailwinds, a country cutting from 55% to 50% in a stable mature economy will see a reform dividend the curve predicts to be almost invisible over a parliamentary term.
There is also a ratchet effect : spending programmes create constituencies. Each percentage point of GDP spent builds a group of beneficiaries who will resist reversal more fiercely than the diffuse taxpayer will reward it. The political equilibrium drifts rightward along the curve — toward higher spending, lower growth, and ever-smaller marginal returns to cutting — until a fiscal crisis forces discontinuous adjustment. The power law explains not only the economic cost of big government, but the political economy of why large states tend to stay large.
Predicted growth gain from a 5-point spending cut — current model & data
Period:
2018–2023
 2014–2023
 2010–2023
 2005–2023
 1995–2023
Uses current model parameters and the currently displayed country data. Gain = predicted growth at (spending − 5 pp) minus predicted growth at current spending . Load country data and press ⚙ Auto-fit to update.
Country
 Avg. spending %
 2005–2023
 Avg. growth %
 2005–2023
 Predicted gain from −5 pp cut
Greece
 50.6%
 -0.30%
 +0.14 pp
France
 47.9%
 1.20%
 +0.15 pp
Palau
 47.3%
 -0.60%
 +0.15 pp
Austria
 46.4%
 1.40%
 +0.16 pp
Slovenia
 45.1%
 2.20%
 +0.17 pp
Italy
 43.6%
 0.30%
 +0.18 pp
Hungary
 43.2%
 2.00%
 +0.18 pp
Belgium
 42.3%
 1.60%
 +0.19 pp
Portugal
 42.0%
 0.90%
 +0.19 pp
Cyprus
 41.0%
 2.90%
 +0.20 pp
Lesotho
 40.7%
 1.80%
 +0.20 pp
San Marino
 40.6%
 0.20%
 +0.20 pp
United Kingdom
 40.3%
 1.40%
 +0.20 pp
Netherlands
 40.2%
 1.60%
 +0.20 pp
Croatia
 39.7%
 1.90%
 +0.21 pp
Slovak Republic
 39.0%
 3.30%
 +0.21 pp
Ukraine
 39.0%
 -0.90%
 +0.21 pp
Finland
 38.3%
 0.90%
 +0.22 pp
Luxembourg
 38.2%
 2.30%
 +0.22 pp
Malta
 37.6%
 5.20%
 +0.23 pp
Denmark
 37.3%
 1.30%
 +0.23 pp
Israel
 36.7%
 4.00%
 +0.24 pp
Serbia
 36.7%
 2.60%
 +0.24 pp
Bosnia and Herzegovina
 36.3%
 2.60%
 +0.24 pp
Poland
 35.9%
 3.80%
 +0.25 pp
Estonia
 35.2%
 2.40%
 +0.26 pp
Iceland
 34.9%
 2.80%
 +0.26 pp
Lithuania
 34.2%
 3.30%
 +0.27 pp
Czechia
 33.9%
 2.30%
 +0.28 pp
Bulgaria
 33.5%
 2.80%
 +0.28 pp
Romania
 33.5%
 3.30%
 +0.28 pp
New Zealand
 32.9%
 2.40%
 +0.29 pp
Namibia
 32.8%
 2.90%
 +0.29 pp
Latvia
 32.7%
 2.40%
 +0.29 pp
Spain
 32.7%
 1.20%
 +0.29 pp
Sweden
 32.7%
 1.80%
 +0.29 pp
Ireland
 32.3%
 5.20%
 +0.30 pp
Tonga
 32.3%
 0.90%
 +0.30 pp
Turkiye
 31.3%
 5.30%
 +0.32 pp
South Africa
 31.2%
 1.90%
 +0.32 pp
Brazil
 31.0%
 2.10%
 +0.32 pp
West Bank and Gaza
 30.5%
 3.60%
 +0.33 pp
Uruguay
 30.3%
 3.30%
 +0.34 pp
Egypt, Arab Rep.
 30.2%
 4.50%
 +0.34 pp
Moldova
 30.2%
 3.30%
 +0.34 pp
North Macedonia
 30.0%
 2.80%
 +0.34 pp
Belarus
 29.5%
 3.10%
 +0.36 pp
Colombia
 29.3%
 3.80%
 +0.36 pp
Solomon Islands
 29.1%
 3.20%
 +0.36 pp
Barbados
 28.9%
 0.30%
 +0.37 pp
Germany
 28.9%
 1.20%
 +0.37 pp
Seychelles
 28.9%
 4.60%
 +0.37 pp
Samoa
 28.8%
 2.40%
 +0.37 pp
Jordan
 28.6%
 3.60%
 +0.38 pp
Tunisia
 28.3%
 2.10%
 +0.38 pp
Russian Federation
 27.4%
 2.50%
 +0.41 pp
Jamaica
 27.4%
 0.90%
 +0.41 pp
Australia
 26.6%
 2.70%
 +0.43 pp
Maldives
 26.5%
 5.80%
 +0.43 pp
Costa Rica
 26.4%
 3.90%
 +0.44 pp
Fiji
 26.2%
 2.10%
 +0.44 pp
Georgia
 26.0%
 5.60%
 +0.45 pp
Vanuatu
 26.0%
 2.80%
 +0.45 pp
Lebanon
 25.6%
 0.80%
 +0.46 pp
Kyrgyz Republic
 25.2%
 4.20%
 +0.48 pp
Eswatini
 25.0%
 2.90%
 +0.48 pp
Morocco
 24.9%
 3.40%
 +0.49 pp
El Salvador
 24.7%
 2.30%
 +0.49 pp
St. Kitts and Nevis
 24.2%
 2.30%
 +0.51 pp
United States
 24.1%
 2.10%
 +0.52 pp
Albania
 24.1%
 3.50%
 +0.52 pp
Argentina
 23.6%
 2.20%
 +0.54 pp
St. Vincent and the Grenadines
 23.3%
 1.60%
 +0.55 pp
Kenya
 22.7%
 4.80%
 +0.58 pp
Honduras
 22.6%
 3.60%
 +0.58 pp
Korea, Rep.
 22.4%
 3.30%
 +0.59 pp
Armenia
 22.2%
 5.10%
 +0.60 pp
Mauritius
 22.2%
 3.20%
 +0.60 pp
Chile
 21.4%
 3.20%
 +0.65 pp
Mozambique
 21.1%
 5.50%
 +0.67 pp
Cabo Verde
 20.9%
 3.70%
 +0.68 pp
Mexico
 20.8%
 1.70%
 +0.68 pp
Senegal
 20.5%
 4.20%
 +0.70 pp
Belize
 19.6%
 2.20%
 +0.77 pp
Ghana
 19.6%
 5.80%
 +0.77 pp
Peru
 19.6%
 4.30%
 +0.77 pp
Bhutan
 19.2%
 5.50%
 +0.80 pp
Thailand
 19.2%
 2.70%
 +0.80 pp
Rwanda
 18.9%
 7.30%
 +0.83 pp
Canada
 18.5%
 1.90%
 +0.86 pp
Malaysia
 18.4%
 4.40%
 +0.87 pp
Macao SAR, China
 18.1%
 6.40%
 +0.90 pp
Japan
 17.5%
 0.60%
 +0.96 pp
Burundi
 17.3%
 3.50%
 +0.98 pp
Sri Lanka
 17.2%
 3.90%
 +0.99 pp
St. Lucia
 17.2%
 1.70%
 +0.99 pp
Bahamas, The
 17.1%
 1.20%
 +1.01 pp
Switzerland
 17.1%
 2.00%
 +1.01 pp
Zimbabwe
 16.6%
 2.90%
 +1.07 pp
Nepal
 16.4%
 4.30%
 +1.09 pp
Dominican Republic
 16.0%
 5.30%
 +1.15 pp
Nicaragua
 15.7%
 3.40%
 +1.20 pp
India
 15.6%
 6.40%
 +1.21 pp
Tanzania
 15.0%
 5.80%
 +1.31 pp
Panama
 14.9%
 6.40%
 +1.33 pp
Philippines
 14.9%
 5.00%
 +1.33 pp
Paraguay
 14.8%
 3.70%
 +1.35 pp
Singapore
 14.6%
 4.70%
 +1.39 pp
Burkina Faso
 14.6%
 5.30%
 +1.39 pp
Malawi
 14.4%
 4.50%
 +1.43 pp
Guinea-Bissau
 14.0%
 4.20%
 +1.52 pp
Uganda
 13.5%
 5.80%
 +1.64 pp
Guatemala
 13.1%
 3.60%
 +1.75 pp
Cote d'Ivoire
 12.7%
 5.10%
 +1.87 pp
Myanmar
 12.6%
 6.00%
 +1.91 pp
Lao PDR
 12.4%
 6.40%
 +1.97 pp
Togo
 12.4%
 4.20%
 +1.97 pp
Cameroon
 12.2%
 3.60%
 +2.05 pp
Sudan
 12.1%
 -1.30%
 +2.08 pp
Tajikistan
 11.4%
 7.00%
 +2.39 pp
Central African Republic
 11.2%
 1.20%
 +2.49 pp
Congo, Dem. Rep.
 10.9%
 5.90%
 +2.65 pp
Mali
 10.7%
 3.80%
 +2.77 pp
Ethiopia
 10.0%
 9.20%
 +3.26 pp
Cambodia
 9.7%
 6.90%
 +3.51 pp
Madagascar
 9.7%
 2.80%
 +3.51 pp
Bangladesh
 8.8%
 6.40%
 +4.53 pp
With α = 0.666: ratio of marginal gains at 20% vs 50% = (50/20) 1.666 ≈ 4.6×
Spending cut needed to reach a target growth rate — current model
Target:
2% growth
 3% growth
 4% growth
 5% growth
 6% growth
 7% growth
Adjust for country baseline
Inverts the current model: finds the spending level predicted to reach the target growth rate, then computes the required cut per country. Countries already below that spending level are shown as "already there".
Baseline-adjusted: each country's residual (actual − predicted at current spending) is added to the model. The inversion then accounts for structural over/underperformance.
Country
 Avg. spending %
 2005–2023
 Avg. growth %
 2005–2023
 Required cut to reach 3%
 Adj. target spending %
Greece
 50.6%
 -0.30%
 −39.5 pp
 11.1%
France
 47.9%
 1.20%
 −29.9 pp
 18.0%
Palau
 47.3%
 -0.60%
 −37.4 pp
 9.9%
Austria
 46.4%
 1.40%
 −27.2 pp
 19.2%
Slovenia
 45.1%
 2.20%
 −17.7 pp
 27.4%
Italy
 43.6%
 0.30%
 −31.1 pp
 12.5%
Hungary
 43.2%
 2.00%
 −19.2 pp
 24.0%
Belgium
 42.3%
 1.60%
 −22.5 pp
 19.8%
Portugal
 42.0%
 0.90%
 −27.0 pp
 15.0%
Cyprus
 41.0%
 2.90%
 −2.7 pp
 38.3%
Lesotho
 40.7%
 1.80%
 −19.6 pp
 21.1%
San Marino
 40.6%
 0.20%
 −28.8 pp
 11.8%
United Kingdom
 40.3%
 1.40%
 −22.6 pp
 17.7%
Netherlands
 40.2%
 1.60%
 −21.0 pp
 19.2%
Croatia
 39.7%
 1.90%
 −18.0 pp
 21.7%
Slovak Republic
 39.0%
 3.30%
 no cut needed
 —
Ukraine
 39.0%
 -0.90%
 −30.4 pp
 8.6%
Finland
 38.3%
 0.90%
 −24.0 pp
 14.3%
Luxembourg
 38.2%
 2.30%
 −12.7 pp
 25.5%
Malta
 37.6%
 5.20%
 no cut needed
 —
Denmark
 37.3%
 1.30%
 −21.0 pp
 16.3%
Israel
 36.7%
 4.00%
 no cut needed
 —
Serbia
 36.7%
 2.60%
 −7.8 pp
 28.9%
Bosnia and Herzegovina
 36.3%
 2.60%
 −7.6 pp
 28.7%
Poland
 35.9%
 3.80%
 no cut needed
 —
Estonia
 35.2%
 2.40%
 −10.0 pp
 25.2%
Iceland
 34.9%
 2.80%
 −3.9 pp
 31.0%
Lithuania
 34.2%
 3.30%
 no cut needed
 —
Czechia
 33.9%
 2.30%
 −10.6 pp
 23.3%
Bulgaria
 33.5%
 2.80%
 −3.7 pp
 29.8%
Romania
 33.5%
 3.30%
 no cut needed
 —
New Zealand
 32.9%
 2.40%
 −9.0 pp
 23.9%
Namibia
 32.8%
 2.90%
 −1.9 pp
 30.9%
Latvia
 32.7%
 2.40%
 −9.0 pp
 23.7%
Spain
 32.7%
 1.20%
 −18.1 pp
 14.6%
Sweden
 32.7%
 1.80%
 −14.5 pp
 18.2%
Ireland
 32.3%
 5.20%
 no cut needed
 —
Tonga
 32.3%
 0.90%
 −19.2 pp
 13.1%
Turkiye
 31.3%
 5.30%
 no cut needed
 —
South Africa
 31.2%
 1.90%
 −12.8 pp
 18.4%
Brazil
 31.0%
 2.10%
 −11.1 pp
 19.9%
West Bank and Gaza
 30.5%
 3.60%
 no cut needed
 —
Uruguay
 30.3%
 3.30%
 no cut needed
 —
Egypt, Arab Rep.
 30.2%
 4.50%
 no cut needed
 —
Moldova
 30.2%
 3.30%
 no cut needed
 —
North Macedonia
 30.0%
 2.80%
 −3.1 pp
 26.9%
Belarus
 29.5%
 3.10%
 no cut needed
 —
Colombia
 29.3%
 3.80%
 no cut needed
 —
Solomon Islands
 29.1%
 3.20%
 no cut needed
 —
Barbados
 28.9%
 0.30%
 −18.6 pp
 10.3%
Germany
 28.9%
 1.20%
 −15.4 pp
 13.5%
Seychelles
 28.9%
 4.60%
 no cut needed
 —
Samoa
 28.8%
 2.40%
 −7.4 pp
 21.4%
Jordan
 28.6%
 3.60%
 no cut needed
 —
Tunisia
 28.3%
 2.10%
 −9.7 pp
 18.6%
Russian Federation
 27.4%
 2.50%
 −5.9 pp
 21.5%
Jamaica
 27.4%
 0.90%
 −15.5 pp
 11.9%
Australia
 26.6%
 2.70%
 −3.7 pp
 22.9%
Maldives
 26.5%
 5.80%
 no cut needed
 —
Costa Rica
 26.4%
 3.90%
 no cut needed
 —
Fiji
 26.2%
 2.10%
 −8.7 pp
 17.5%
Georgia
 26.0%
 5.60%
 no cut needed
 —
Vanuatu
 26.0%
 2.80%
 −2.4 pp
 23.6%
Lebanon
 25.6%
 0.80%
 −14.5 pp
 11.1%
Kyrgyz Republic
 25.2%
 4.20%
 no cut needed
 —
Eswatini
 25.0%
 2.90%
 −1.2 pp
 23.8%
Morocco
 24.9%
 3.40%
 no cut needed
 —
El Salvador
 24.7%
 2.30%
 −6.6 pp
 18.1%
St. Kitts and Nevis
 24.2%
 2.30%
 −6.4 pp
 17.8%
United States
 24.1%
 2.10%
 −7.7 pp
 16.4%
Albania
 24.1%
 3.50%
 no cut needed
 —
Argentina
 23.6%
 2.20%
 −6.8 pp
 16.8%
St. Vincent and the Grenadines
 23.3%
 1.60%
 −9.9 pp
 13.4%
Kenya
 22.7%
 4.80%
 no cut needed
 —
Honduras
 22.6%
 3.60%
 no cut needed
 —
Korea, Rep.
 22.4%
 3.30%
 no cut needed
 —
Armenia
 22.2%
 5.10%
 no cut needed
 —
Mauritius
 22.2%
 3.20%
 no cut needed
 —
Chile
 21.4%
 3.20%
 no cut needed
 —
Mozambique
 21.1%
 5.50%
 no cut needed
 —
Cabo Verde
 20.9%
 3.70%
 no cut needed
 —
Mexico
 20.8%
 1.70%
 −8.0 pp
 12.8%
Senegal
 20.5%
 4.20%
 no cut needed
 —
Belize
 19.6%
 2.20%
 −5.2 pp
 14.4%
Ghana
 19.6%
 5.80%
 no cut needed
 —
Peru
 19.6%
 4.30%
 no cut needed
 —
Bhutan
 19.2%
 5.50%
 no cut needed
 —
Thailand
 19.2%
 2.70%
 −2.2 pp
 17.0%
Rwanda
 18.9%
 7.30%
 no cut needed
 —
Canada
 18.5%
 1.90%
 −6.0 pp
 12.5%
Malaysia
 18.4%
 4.40%
 no cut needed
 —
Macao SAR, China
 18.1%
 6.40%
 no cut needed
 —
Japan
 17.5%
 0.60%
 −9.1 pp
 8.4%
Burundi
 17.3%
 3.50%
 no cut needed
 —
Sri Lanka
 17.2%
 3.90%
 no cut needed
 —
St. Lucia
 17.2%
 1.70%
 −6.1 pp
 11.1%
Bahamas, The
 17.1%
 1.20%
 −7.4 pp
 9.7%
Switzerland
 17.1%
 2.00%
 −5.0 pp
 12.1%
Zimbabwe
 16.6%
 2.90%
 −0.6 pp
 16.0%
Nepal
 16.4%
 4.30%
 no cut needed
 —
Dominican Republic
 16.0%
 5.30%
 no cut needed
 —
Nicaragua
 15.7%
 3.40%
 no cut needed
 —
India
 15.6%
 6.40%
 no cut needed
 —
Tanzania
 15.0%
 5.80%
 no cut needed
 —
Panama
 14.9%
 6.40%
 no cut needed
 —
Philippines
 14.9%
 5.00%
 no cut needed
 —
Paraguay
 14.8%
 3.70%
 no cut needed
 —
Singapore
 14.6%
 4.70%
 no cut needed
 —
Burkina Faso
 14.6%
 5.30%
 no cut needed
 —
Malawi
 14.4%
 4.50%
 no cut needed
 —
Guinea-Bissau
 14.0%
 4.20%
 no cut needed
 —
Uganda
 13.5%
 5.80%
 no cut needed
 —
Guatemala
 13.1%
 3.60%
 no cut needed
 —
Cote d'Ivoire
 12.7%
 5.10%
 no cut needed
 —
Myanmar
 12.6%
 6.00%
 no cut needed
 —
Lao PDR
 12.4%
 6.40%
 no cut needed
 —
Togo
 12.4%
 4.20%
 no cut needed
 —
Cameroon
 12.2%
 3.60%
 no cut needed
 —
Sudan
 12.1%
 -1.30%
 −7.4 pp
 4.7%
Tajikistan
 11.4%
 7.00%
 no cut needed
 —
Central African Republic
 11.2%
 1.20%
 −4.1 pp
 7.1%
Congo, Dem. Rep.
 10.9%
 5.90%
 no cut needed
 —
Mali
 10.7%
 3.80%
 no cut needed
 —
Ethiopia
 10.0%
 9.20%
 no cut needed
 —
Cambodia
 9.7%
 6.90%
 no cut needed
 —
Madagascar
 9.7%
 2.80%
 −0.5 pp
 9.2%
Bangladesh
 8.8%
 6.40%
 no cut needed
 —
Residual-adjusted: target spending is country-specific, accounting for structural over/underperformance. Global model baseline: 25.2% of GDP (power law, 2005–2023)
Freeze scenario: outgrow the spending instead of cutting it
For countries where a one-shot cut is politically impossible (France, Italy, Belgium…), there is a slower path:
 hold real spending flat while the economy grows. The spending/GDP ratio falls automatically each year by a factor of
 (1 + s) / (1 + g) , where s is real spending growth and g is real GDP growth.
 This is the Canada 1995–2005 and Sweden post-1993 playbook.
Country:
Real GDP growth:
 %
Real spending growth:
 %
Target spending:
 %
France : 57.2% (2024) → 30.0% in 32.6 years .
 After 10 years: 46.9%. After 20 years: 38.5%.
Country
 Avg. spending %
 2024
 Years to 30.0%
 After 10 years
Ukraine
 71.3%
 43.7
 58.5%
Finland
 57.7%
 33.0
 47.3%
France
 57.2%
 32.6
 46.9%
Austria
 56.0%
 31.5
 45.9%
Belgium
 54.5%
 30.1
 44.7%
Lesotho
 53.5%
 29.2
 43.9%
Italy
 50.6%
 26.4
 41.5%
Germany
 49.4%
 25.2
 40.5%
Poland
 49.4%
 25.2
 40.5%
Sweden
 49.3%
 25.1
 40.4%
Croatia
 48.0%
 23.7
 39.4%
Greece
 48.0%
 23.7
 39.4%
Denmark
 47.3%
 23.0
 38.8%
Palau
 47.3%
 23.0
 38.8%
Slovak Republic
 47.1%
 22.8
 38.6%
Hungary
 46.9%
 22.6
 38.5%
Luxembourg
 46.9%
 22.6
 38.5%
Iceland
 46.5%
 22.1
 38.1%
Slovenia
 46.5%
 22.1
 38.1%
Maldives
 46.1%
 21.7
 37.8%
Brazil
 45.7%
 21.3
 37.5%
Spain
 45.3%
 20.8
 37.2%
Canada
 44.7%
 20.1
 36.7%
Latvia
 44.5%
 19.9
 36.5%
Netherlands
 44.4%
 19.8
 36.4%
United Kingdom
 44.0%
 19.3
 36.1%
Israel
 43.8%
 19.1
 35.9%
Estonia
 43.6%
 18.9
 35.8%
Bosnia and Herzegovina
 43.3%
 18.5
 35.5%
Czechia
 42.8%
 17.9
 35.1

## 导航

- 项目页：[[10-项目/julienreszka.github.io_0eb713ab]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
