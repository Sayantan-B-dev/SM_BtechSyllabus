# Analysis of ANOVA

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 9  
**Date:** 30-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.6.8

## Notes

---

### Interpreting ANOVA Results

A significant F-test (rejecting `H_0`) tells us that **at least one** group mean is different from the others, but it does NOT tell us **which** groups are different.

To identify which specific groups differ, we need **post-hoc tests** (also called multiple comparison procedures).

---

### Post-Hoc Tests

After a significant ANOVA F-test, post-hoc tests are used to make pairwise comparisons between group means while controlling the overall Type I error rate.

#### Tukey's Honestly Significant Difference (HSD) Test

Tukey's HSD is the most commonly used post-hoc test when all groups have the **same sample size**.

**Formula:**

`HSD = q_{alpha, k, N-k} * sqrt{MSE / n}`

where:
- `q_{alpha, k, N-k}` = the **studentized range statistic** from the q-table (depends on `alpha`, number of groups `k`, and error df `N - k`)
- `MSE` = mean square error from the ANOVA table
- `n` = number of observations per group (assuming equal group sizes)

**Procedure:**

1. Compute `HSD`.
2. For any pair of groups `i` and `j`, compute the absolute difference in sample means: `|bar{x}_i - bar{x}_j|`.
3. If `|bar{x}_i - bar{x}_j| > HSD`, the difference is statistically significant at level `alpha`.

**If group sizes are unequal** (called the Tukey-Kramer method):

`HSD = q_{alpha, k, N-k} * sqrt{MSE / 2 * (1/n_i + 1/n_j)}`

The critical value `HSD` is different for each pair when sample sizes differ.

---

#### Worked Example 1: Tukey's HSD (Continuing from L08)

**Problem:** Recall the fertilizer example from L08. We had:
- Group A: `bar{x}_A = 13.0`, `n = 5`
- Group B: `bar{x}_B = 16.0`, `n = 5`
- Group C: `bar{x}_C = 11.0`, `n = 5`
- `MSE = 2.5`, `N = 15`, `k = 3`, error df = 12
- ANOVA was significant (`F = 12.666`)

Use Tukey's HSD at `alpha = 0.05` to determine which fertilizers differ.

**Solution:**

Step 1: Find `q` from the studentized range table.
`q_{0.05, k=3, df=12} = 3.77` (from standard q-table)

Step 2: Compute HSD.
`HSD = q * sqrt{MSE / n} = 3.77 * sqrt{2.5 / 5} = 3.77 * sqrt{0.5} = 3.77 * 0.707 = 2.666`

Step 3: Compare all pairs.

| Pair | `|bar{x}_i - bar{x}_j|` | `> HSD?` | Significant? |
|---|---|---|---|
| A vs B | `16.0 - 13.0 = 3.0` | `3.0 > 2.666` | Yes |
| A vs C | `13.0 - 11.0 = 2.0` | `2.0 < 2.666` | No |
| B vs C | `16.0 - 11.0 = 5.0` | `5.0 > 2.666` | Yes |

**Conclusion:** Fertilizer B produces significantly higher growth than both A and C. Fertilizer A and C are not significantly different from each other.

---

### Two-Way ANOVA (Brief Introduction)

**Two-way ANOVA** extends one-way ANOVA to study the effects of **two factors** simultaneously. It can also detect **interaction effects** between the factors.

**Example:** Study the effect of both fertilizer type (A, B, C) AND watering frequency (daily, weekly) on plant growth.

#### Hypotheses in Two-Way ANOVA

For Factor A (e.g., fertilizer):
- `H_0`: No difference in means across levels of Factor A.
- `H_1`: At least one level of Factor A has a different mean.

For Factor B (e.g., watering):
- `H_0`: No difference in means across levels of Factor B.
- `H_1`: At least one level of Factor B has a different mean.

For Interaction (A x B):
- `H_0`: No interaction between factors (they act independently).
- `H_1`: There is an interaction effect.

#### Partitioning Variation in Two-Way ANOVA

`SST = SSA + SSB + SSAB + SSE`

where:
- `SSA` = variation due to Factor A
- `SSB` = variation due to Factor B
- `SSAB` = variation due to interaction between A and B
- `SSE` = variation within cells (error)

#### Two-Way ANOVA Table

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Factor A | SSA | `a - 1` | `SSA / (a-1)` | `MSA / MSE` |
| Factor B | SSB | `b - 1` | `SSB / (b-1)` | `MSB / MSE` |
| Interaction | SSAB | `(a-1)(b-1)` | `SSAB / (a-1)(b-1)` | `MSAB / MSE` |
| Error | SSE | `ab(r-1)` | `SSE / ab(r-1)` | |
| **Total** | SST | `abr - 1` | | |

where `a` = levels of Factor A, `b` = levels of Factor B, `r` = number of replications per cell.

---

### Assumptions Checking

ANOVA results are valid only if the assumptions are reasonably satisfied. We should check:

#### 1. Normality Assumption

**How to check:**
- **Histogram of residuals:** Should be approximately bell-shaped.
- **Normal probability plot (Q-Q plot):** Points should fall approximately along a straight line.
- **Shapiro-Wilk test** or **Kolmogorov-Smirnov test** for formal testing.

**Residuals are computed as:**

`e_{ij} = x_{ij} - bar{x}_{i.}` (for one-way ANOVA)

#### 2. Equal Variance Assumption (Homoscedasticity)

**How to check:**
- **Side-by-side boxplots:** The spread of each group should be roughly similar.
- **Rule of thumb:** The largest sample standard deviation should be no more than twice the smallest.
- **Levene's test:** A formal test for equality of variances across groups.
- **Bartlett's test:** More sensitive to normality violations than Levene's test.

#### 3. Independence Assumption

- Check the study design: Were data collected randomly? Are observations independent?
- This is typically ensured by proper randomization in the experimental design.

#### What if assumptions are violated?

| Violation | Possible Remedy |
|---|---|
| Non-normality | Transform data (log, square root), or use non-parametric alternative (Kruskal-Wallis test) |
| Unequal variances | Use Welch's ANOVA (does not assume equal variances), or transform |
| Non-independence | Use more advanced methods (random effects models, repeated measures ANOVA) |

---

### Worked Example 2: Interpreting ANOVA Output

**Problem:** A researcher compares the effect of three study methods (S1, S2, S3) on exam scores. Twenty students are assigned to each method. The ANOVA output is:

| Source | SS | df | MS | F | p-value |
|---|---|---|---|---|---|
| Method | 1240 | 2 | 620 | 8.27 | 0.0006 |
| Error | 4275 | 57 | 75 | | |
| **Total** | 5515 | 59 | | | |

**Interpretation:**

1. **F-statistic:** `F(2, 57) = 8.27`
2. **p-value:** `0.0006`
3. **Decision:** Since `p = 0.0006 < 0.05`, reject `H_0`. There is a statistically significant difference in mean exam scores among the three study methods.

4. **Effect size (Eta-squared):**
`eta^2 = SSB / SST = 1240 / 5515 = 0.225`
Interpretation: 22.5% of the total variation in exam scores is explained by the study method.

5. **Post-hoc comparison needed:** Since the F-test is significant, we would follow up with Tukey's HSD to determine which methods differ.

---

### Effect Size in ANOVA

**Eta-squared (`eta^2`)** measures the proportion of total variance explained by the group differences.

`eta^2 = SSB / SST`

| `eta^2` | Interpretation |
|---|---|
| `0.01` | Small effect |
| `0.06` | Medium effect |
| `0.14` | Large effect |

**Omega-squared (`omega^2`)** is a less biased alternative:

`omega^2 = (SSB - (k-1) MSE) / (SST + MSE)`

---

### Summary: Complete Workflow for One-Way ANOVA

1. **Check assumptions** (normality, equal variances, independence).
2. **State hypotheses** and choose `alpha`.
3. **Compute the ANOVA table** (SST, SSB, SSE, df, MS, F).
4. **Compare F-statistic with critical value** or use p-value.
5. **If significant, perform post-hoc tests** (Tukey's HSD).
6. **Report results:** Include F-statistic, df, p-value, effect size.

---

## Practice Problems

1. A one-way ANOVA comparing 4 groups (n=10 each) yields F = 4.50 with p-value = 0.008. At `alpha = 0.05`, what is the conclusion? Should post-hoc tests be done?
   - **Answer:** Since `p = 0.008 < 0.05`, reject `H_0`. Significant ANOVA. Yes, perform post-hoc tests to find which groups differ.

2. In Tukey's HSD, what does it mean if `|bar{x}_A - bar{x}_B| > HSD`?
   - **Answer:** The difference between means of groups A and B is statistically significant at the chosen `alpha` level.

3. Three groups with means 20, 24, and 28. MSE = 10, n = 8 per group, k = 3, error df = 21, `q_{0.05,3,21} = 3.57`. Compute HSD and determine which pairs are significantly different.
   - **Answer:** `HSD = 3.57 * sqrt{10/8} = 3.57 * 1.118 = 3.992`. Differences: A-B: 4 (significant), A-C: 8 (significant), B-C: 4 (significant). All pairs differ.

4. SST = 500, SSB = 150, k = 5, N = 40. Compute `eta^2` and interpret.
   - **Answer:** `eta^2 = 150/500 = 0.30`. This is a large effect size: 30% of the total variability is explained by group differences.

5. What is the difference between one-way and two-way ANOVA?
   - **Answer:** One-way ANOVA compares groups based on one factor. Two-way ANOVA analyzes two factors simultaneously and can detect interaction effects between them.
