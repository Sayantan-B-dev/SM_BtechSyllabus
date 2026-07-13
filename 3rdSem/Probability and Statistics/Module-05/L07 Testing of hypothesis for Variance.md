# Testing of hypothesis for Variance

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 7  
**Date:** 27-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.6.5-18.6.7

## Notes

---

### Overview

Hypothesis tests for variances are important when:
- We need to assess the consistency or precision of a process.
- We want to compare the variability of two populations.
- The assumption of equal variances is needed for other tests (like ANOVA, two-sample t-tests).

Two common tests:
1. **Chi-square test** for a single variance.
2. **F-test** for equality of two variances.

---

### Part 1: Chi-Square Test for a Single Variance

#### When to Use

- We want to test a claim about the population variance `sigma^2` (or standard deviation `sigma`).
- The population is **normally distributed** (this assumption is critical).
- The sample is random and independent.

#### Test Statistic

`chi^2 = (n - 1) s^2 / sigma_0^2`

where:
- `n` = sample size
- `s^2` = sample variance
- `sigma_0^2` = hypothesized population variance under `H_0`
- Degrees of freedom `df = n - 1`

The test statistic follows a **chi-square distribution** with `n - 1` degrees of freedom.

#### Procedure

1. **State hypotheses:**
   - Two-tailed: `H_0: sigma^2 = sigma_0^2` vs `H_1: sigma^2 != sigma_0^2`
   - Right-tailed: `H_0: sigma^2 <= sigma_0^2` vs `H_1: sigma^2 > sigma_0^2`
   - Left-tailed: `H_0: sigma^2 >= sigma_0^2` vs `H_1: sigma^2 < sigma_0^2`

2. **Choose `alpha`.**

3. **Find critical values** from the chi-square table (`df = n - 1`):
   - Two-tailed: `chi^2_{alpha/2, n-1}` (right) and `chi^2_{1 - alpha/2, n-1}` (left)
   - Right-tailed: `chi^2_{alpha, n-1}`
   - Left-tailed: `chi^2_{1 - alpha, n-1}`

4. **Compute test statistic:** `chi^2 = (n - 1) s^2 / sigma_0^2`.

5. **Decision:**
   - Two-tailed: Reject if `chi^2 > chi^2_{alpha/2}` or `chi^2 < chi^2_{1 - alpha/2}`
   - Right-tailed: Reject if `chi^2 > chi^2_{alpha}`
   - Left-tailed: Reject if `chi^2 < chi^2_{1 - alpha}`

6. **Conclusion.**

---

#### Worked Example 1: Chi-Square Test for Variance

**Problem:** A machine produces bolts with a specified variance of `sigma^2 = 0.01` mm^2 (so `sigma = 0.1` mm). A sample of 20 bolts has a sample variance of `s^2 = 0.016` mm^2. Test whether the variance has increased at `alpha = 0.05`. Assume the population is normally distributed.

**Solution:**

Step 1: `H_0: sigma^2 <= 0.01` (variance is within specification) vs `H_1: sigma^2 > 0.01` (variance has increased). Right-tailed test.

Step 2: `alpha = 0.05`.

Step 3: `df = 20 - 1 = 19`. From chi-square table: `chi^2_{0.05, 19} = 30.144`. Critical region: `chi^2 > 30.144`.

Step 4: Compute test statistic:
`chi^2 = (n - 1) s^2 / sigma_0^2 = (19 * 0.016) / 0.01 = 0.304 / 0.01 = 30.4`

Step 5: `chi^2 = 30.4 > 30.144`. Reject `H_0`.

Step 6: There is sufficient evidence at the 0.05 level that the variance has increased. The machine needs adjustment.

---

#### Worked Example 2: Testing a Standard Deviation

**Problem:** A manufacturer claims that the standard deviation of the weight of their product is at most 2 grams. A sample of 15 packages has a standard deviation of 2.8 grams. Test the claim at `alpha = 0.10`. Assume normality.

**Solution:**

Step 1: `H_0: sigma <= 2` vs `H_1: sigma > 2` (right-tailed). Using `sigma_0 = 2`, so `sigma_0^2 = 4`.

Step 2: `alpha = 0.10`.

Step 3: `df = 14`. `chi^2_{0.10, 14} = 21.064`. Critical region: `chi^2 > 21.064`.

Step 4: `s^2 = (2.8)^2 = 7.84`.
`chi^2 = (14 * 7.84) / 4 = 109.76 / 4 = 27.44`

Step 5: `chi^2 = 27.44 > 21.064`. Reject `H_0`.

Step 6: There is sufficient evidence at the 0.10 level that the standard deviation exceeds 2 grams. The claim is not supported.

---

### Part 2: F-Test for Equality of Two Variances

#### When to Use

- We want to test whether two populations have equal variances.
- Both populations are **normally distributed**.
- Samples are random and independent.

#### Test Statistic

`F = s_1^2 / s_2^2`

where `s_1^2` and `s_2^2` are the sample variances from populations 1 and 2.

- **Convention:** Place the larger sample variance in the numerator to make the F-statistic >= 1 (for a two-tailed test, this simplifies the procedure).
- Degrees of freedom: `df_1 = n_1 - 1` (numerator), `df_2 = n_2 - 1` (denominator).

#### Assumptions

1. Both populations are normally distributed.
2. Samples are independent.
3. Samples are random.

#### Procedure for Two-Tailed F-Test

1. **State hypotheses:** `H_0: sigma_1^2 = sigma_2^2` vs `H_1: sigma_1^2 != sigma_2^2`.

2. **Choose `alpha`.**

3. **Find critical value:** For `F_{alpha/2, df1, df2}` from the F-distribution table.

4. **Compute test statistic:** `F = s_1^2 / s_2^2` (put larger variance in numerator).

5. **Decision:** Reject `H_0` if `F > F_{alpha/2, df1, df2}`.

6. **Conclusion.**

---

#### Worked Example 3: F-Test for Equality of Variances

**Problem:** Two methods of assembly are compared. A sample of 10 items using Method A has variance 16. A sample of 12 items using Method B has variance 9. Test whether the variances are equal at `alpha = 0.10`. Assume normality.

**Solution:**

Step 1: `H_0: sigma_A^2 = sigma_B^2`, `H_1: sigma_A^2 != sigma_B^2` (two-tailed)

Step 2: `alpha = 0.10`. For two-tailed, use `alpha/2 = 0.05`.

Step 3: Since `s_A^2 = 16 > s_B^2 = 9`, put Method A in numerator.
`df_1 = 10 - 1 = 9`, `df_2 = 12 - 1 = 11`
From F-table: `F_{0.05, 9, 11} = 2.90` (approximate value).
Critical region: `F > 2.90`.

Step 4: `F = 16 / 9 = 1.778`.

Step 5: `F = 1.778 < 2.90`. Fail to reject `H_0`.

Step 6: There is insufficient evidence at the 0.10 level that the variances are different. The assumption of equal variances is plausible.

---

#### Worked Example 4: One-Tailed F-Test

**Problem:** A researcher suspects that the variance of test scores for Class A is greater than for Class B. Sample A (n=8) has variance 25. Sample B (n=10) has variance 12. Test at `alpha = 0.05`. Assume normality.

**Solution:**

Step 1: `H_0: sigma_A^2 <= sigma_B^2`, `H_1: sigma_A^2 > sigma_B^2` (right-tailed)

Step 2: `alpha = 0.05`.

Step 3: `s_A^2 = 25` (numerator), `s_B^2 = 12` (denominator).
`df_1 = 7`, `df_2 = 9`
From F-table: `F_{0.05, 7, 9} = 3.29`.
Critical region: `F > 3.29`.

Step 4: `F = 25 / 12 = 2.083`.

Step 5: `F = 2.083 < 3.29`. Fail to reject `H_0`.

Step 6: Insufficient evidence that the variance of Class A is greater.

---

### Summary of Tests for Variance

| Test | Purpose | Test Statistic | Distribution | df |
|---|---|---|---|---|
| Chi-square test | Test a single variance | `(n-1)s^2 / sigma_0^2` | `chi^2` | `n - 1` |
| F-test | Compare two variances | `s_1^2 / s_2^2` | `F` | `n_1-1, n_2-1` |

---

### Important Notes

- Both tests are **highly sensitive to normality**. If the populations are not normally distributed, these tests are unreliable. Use alternative non-parametric tests (like Levene's test) when normality is violated.
- For the F-test, the convention of putting the larger variance in the numerator is for two-tailed tests only. For a right-tailed test, the suspected larger variance goes in the numerator regardless.
- The F-distribution is **not symmetric** (unlike z and t). It is skewed to the right.

---

## Practice Problems

1. A sample of 25 items has variance 8.5. Test `H_0: sigma^2 = 5` against `H_1: sigma^2 > 5` at `alpha = 0.05`.
   - **Answer:** `chi^2 = (24 * 8.5) / 5 = 40.8`. `chi^2_{0.05, 24} = 36.415`. Since `40.8 > 36.415`, reject `H_0`.

2. Two samples: n1=13, s1^2=30; n2=16, s2^2=14. Test equality of variances at `alpha = 0.10`.
   - **Answer:** `F = 30/14 = 2.143`. `df1=12, df2=15`. `F_{0.05,12,15} = 2.48` (approx). Since `2.143 < 2.48`, fail to reject `H_0`.

3. What is the critical assumption for both chi-square and F-tests for variances?
   - **Answer:** The populations must be normally distributed. Both tests are very sensitive to violations of normality.

4. A quality control engineer wants to test if the variance of a process has decreased from `sigma^2 = 0.04`. Sample of 20 items has variance 0.025. Test at `alpha = 0.05`.
   - **Answer:** `H_0: sigma^2 >= 0.04`, `H_1: sigma^2 < 0.04`. `chi^2 = (19*0.025)/0.04 = 11.875`. `chi^2_{0.95,19} = 10.117`. Since `11.875 > 10.117`, fail to reject `H_0`.

5. Which test would you use to compare the consistency (variability) of two production lines?
   - **Answer:** F-test for equality of two variances.
