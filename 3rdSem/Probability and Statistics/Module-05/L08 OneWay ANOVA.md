# OneWay ANOVA

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 8  
**Date:** 29-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.6.5-18.6.7

## Notes

---

### Introduction to ANOVA

**ANOVA** stands for **Analysis of Variance**. It is a statistical method used to compare the means of three or more groups to determine if at least one group mean is significantly different from the others.

**Why not use multiple t-tests?**
- If we have `k` groups, we would need `C(k,2)` pairwise t-tests.
- Each test has a Type I error rate of `alpha`. The overall Type I error rate inflates dramatically.
- Example: For `k = 5` groups, we would need `10` t-tests. The overall chance of at least one false positive is `1 - (0.95)^10 = 0.401` (about 40%).
- ANOVA tests **all means simultaneously** while controlling the overall Type I error rate at `alpha`.

---

### One-Way ANOVA: Comparing k Population Means

One-way ANOVA compares means across groups defined by a single factor (categorical variable).

**Example:** Compare the average test scores of students taught using three different teaching methods.

**Hypotheses:**

`H_0: mu_1 = mu_2 = ... = mu_k` (all group means are equal)
`H_1:` At least one `mu_i` is different from the others.

---

### Assumptions of One-Way ANOVA

1. **Normality:** The populations (residuals) are normally distributed. This is especially important for small samples.
2. **Independence:** Observations are independent within and between groups.
3. **Equal variances (Homoscedasticity):** All populations have the same variance `sigma^2`. This is also called the **homogeneity of variance** assumption.
4. **Random sampling:** Data are from random samples.

---

### Partitioning Total Variation

The key idea of ANOVA is to split the total variability in the data into two parts:

1. **Between-group variation:** Variability due to differences between the group means.
2. **Within-group variation:** Variability due to differences within each group (random error).

#### Sum of Squares

**Total Sum of Squares (SST):** Measures total variability in all observations combined.

`SST = sum_{i=1}^{k} sum_{j=1}^{n_i} (x_{ij} - bar{x}_{..})^2`

where `x_{ij}` is the `j`th observation in the `i`th group and `bar{x}_{..}` is the overall (grand) mean.

**Sum of Squares Between Groups (SSB):** Measures variability between group means.

`SSB = sum_{i=1}^{k} n_i (bar{x}_{i.} - bar{x}_{..})^2`

where `bar{x}_{i.}` is the mean of group `i` and `n_i` is the size of group `i`.

**Sum of Squares Within Groups (SSE):** Measures variability within groups (error).

`SSE = sum_{i=1}^{k} sum_{j=1}^{n_i} (x_{ij} - bar{x}_{i.})^2`

**Partitioning Identity:**

`SST = SSB + SSE`

---

### Degrees of Freedom

| Source | df |
|---|---|
| Between groups | `k - 1` |
| Within groups (error) | `N - k` |
| Total | `N - 1` |

where `N = n_1 + n_2 + ... + n_k` (total number of observations).

---

### Mean Squares

**Mean Square Between (MSB):**

`MSB = SSB / (k - 1)`

**Mean Square Within (MSE):**

`MSE = SSE / (N - k)`

MSE is an estimate of the common population variance `sigma^2`.

---

### F-Statistic

The test statistic for ANOVA is:

`F = MSB / MSE`

Under `H_0` (all means equal), `F` follows an F-distribution with `df_1 = k - 1` and `df_2 = N - k`.

- If `H_0` is true, `MSB` and `MSE` both estimate `sigma^2`, so `F` is approximately 1.
- If `H_0` is false, `MSB` tends to be larger than `MSE`, so `F > 1`.
- Reject `H_0` if `F > F_{alpha, k-1, N-k}`.

---

### ANOVA Table

The ANOVA table summarizes all calculations:

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between groups | SSB | `k - 1` | `MSB = SSB / (k-1)` | `F = MSB / MSE` |
| Within groups (Error) | SSE | `N - k` | `MSE = SSE / (N-k)` | |
| **Total** | SST | `N - 1` | | |

---

### Worked Example: One-Way ANOVA (Step-by-Step)

**Problem:** A researcher wants to compare the effectiveness of three different fertilizers (A, B, C) on plant growth. The growth (in cm) after 4 weeks for 5 plants per fertilizer is:

| Fertilizer A | Fertilizer B | Fertilizer C |
|---|---|---|
| 12 | 15 | 10 |
| 14 | 16 | 11 |
| 13 | 14 | 12 |
| 15 | 18 | 9 |
| 11 | 17 | 13 |

Test at `alpha = 0.05` whether there is a difference in mean growth among the three fertilizers.

**Solution:**

#### Step 1: State hypotheses

`H_0: mu_A = mu_B = mu_C` (all fertilizers have the same mean growth)
`H_1:` At least one mean is different.

#### Step 2: Compute group means and overall mean

Group A: `bar{x}_A = (12 + 14 + 13 + 15 + 11) / 5 = 65 / 5 = 13.0`
Group B: `bar{x}_B = (15 + 16 + 14 + 18 + 17) / 5 = 80 / 5 = 16.0`
Group C: `bar{x}_C = (10 + 11 + 12 + 9 + 13) / 5 = 55 / 5 = 11.0`

Overall mean: `bar{x}_{..} = (65 + 80 + 55) / 15 = 200 / 15 = 13.333`

#### Step 3: Compute sum of squares

**SSB:**

`SSB = sum n_i (bar{x}_i - bar{x}_{..})^2`

`SSB = 5(13.0 - 13.333)^2 + 5(16.0 - 13.333)^2 + 5(11.0 - 13.333)^2`

`SSB = 5(-0.333)^2 + 5(2.667)^2 + 5(-2.333)^2`

`SSB = 5(0.111) + 5(7.111) + 5(5.444)`

`SSB = 0.555 + 35.555 + 27.220 = 63.33`

**SSE:**

For Group A: `(12-13)^2 + (14-13)^2 + (13-13)^2 + (15-13)^2 + (11-13)^2`
= `1 + 1 + 0 + 4 + 4 = 10`

For Group B: `(15-16)^2 + (16-16)^2 + (14-16)^2 + (18-16)^2 + (17-16)^2`
= `1 + 0 + 4 + 4 + 1 = 10`

For Group C: `(10-11)^2 + (11-11)^2 + (12-11)^2 + (9-11)^2 + (13-11)^2`
= `1 + 0 + 1 + 4 + 4 = 10`

`SSE = 10 + 10 + 10 = 30`

**SST:**

Method 1: `SST = SSB + SSE = 63.33 + 30 = 93.33`

Method 2 (direct): Compute all deviations from overall mean 13.333:
Group A: `(12-13.333)^2 + (14-13.333)^2 + ...` = `1.777 + 0.444 + 0.111 + 2.777 + 5.444 = 10.553`
Group B: `(15-13.333)^2 + (16-13.333)^2 + ...` = `2.777 + 7.111 + 0.444 + 21.777 + 13.444 = 45.553`
Group C: `(10-13.333)^2 + ...` = `11.111 + 5.444 + 1.777 + 18.777 + 0.111 = 37.220`
SST = `10.553 + 45.553 + 37.220 = 93.33` (matches)

#### Step 4: Compute degrees of freedom

Between groups: `k - 1 = 3 - 1 = 2`
Within groups: `N - k = 15 - 3 = 12`
Total: `N - 1 = 14`

#### Step 5: Compute mean squares

`MSB = SSB / (k - 1) = 63.33 / 2 = 31.665`

`MSE = SSE / (N - k) = 30 / 12 = 2.5`

#### Step 6: Compute F-statistic

`F = MSB / MSE = 31.665 / 2.5 = 12.666`

#### Step 7: Find critical value

From F-table: `F_{0.05, 2, 12} = 3.89` (approximately)
Critical region: `F > 3.89`

#### Step 8: Decision

`F = 12.666 > 3.89`. Reject `H_0`.

#### Step 9: Conclusion

There is sufficient evidence at the 0.05 significance level that at least one fertilizer has a different mean growth.

#### ANOVA Table

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between groups | 63.33 | 2 | 31.665 | 12.666 |
| Within groups (Error) | 30.00 | 12 | 2.500 | |
| **Total** | 93.33 | 14 | | |

---

### Computational Formulas (for manual calculation)

Let `T_i` = sum of all observations in group `i`, `T` = sum of all observations, `N` = total sample size.

`CF` (Correction Factor) `= T^2 / N`

`SST = sum_{ij} x_{ij}^2 - CF`

`SSB = sum_i (T_i^2 / n_i) - CF`

`SSE = SST - SSB`

Using the worked example:
`T = 200`, `N = 15`, `CF = 200^2 / 15 = 40000 / 15 = 2666.667`

`sum x_{ij}^2 = (144+196+169+225+121) + (225+256+196+324+289) + (100+121+144+81+169)`
= `855 + 1290 + 615 = 2760`

`SST = 2760 - 2666.667 = 93.33`

`SSB = (65^2/5 + 80^2/5 + 55^2/5) - 2666.667`
= `(845 + 1280 + 605) - 2666.667`
= `2730 - 2666.667 = 63.33`

`SSE = 93.33 - 63.33 = 30`

Same results, confirming our manual calculations.

---

## Practice Problems

1. An experiment compares the weight gain (in kg) of animals on four different diets. Each diet is given to 6 animals. Complete the partial ANOVA table:

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between | 45 | ? | ? | ? |
| Within | ? | ? | 5 | |
| **Total** | 125 | ? | | |

   <details>
   <summary>Show Answer</summary>
   Between df = 3, MSB = 15. Total df = 23, Within df = 20, SSE = 100. F = 15/5 = 3.00.
   </details>

2. In a one-way ANOVA with 4 groups and 8 observations per group, what are the degrees of freedom for the F-test?
   <details>
   <summary>Show Answer</summary>
   `df1 = k - 1 = 3`, `df2 = N - k = 32 - 4 = 28`.
   </details>

3. If SST = 200, SSB = 80, and N = 25 with k = 5, compute the ANOVA table.
   <details>
   <summary>Show Answer</summary>
   SSE = 120. df(B) = 4, MSB = 20. df(W) = 20, MSE = 6. F = 20/6 = 3.333.
   </details>

4. What is the main advantage of ANOVA over multiple t-tests?
   <details>
   <summary>Show Answer</summary>
   ANOVA controls the overall Type I error rate at `alpha`, while multiple t-tests inflate the error rate.
   </details>

5. A one-way ANOVA yields `F = 4.50` with `df1 = 2` and `df2 = 18`. Using `alpha = 0.05` and `F_{0.05,2,18} = 3.55`, what is the conclusion?
   <details>
   <summary>Show Answer</summary>
   Since `4.50 > 3.55`, reject `H_0`. At least one group mean is significantly different.
   </details>
