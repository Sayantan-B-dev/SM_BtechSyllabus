# Testing of hypothesis for Means

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 3  
**Date:** 09-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.2

## Notes

---

### Overview

When testing hypotheses about a population mean `mu`, the choice of test statistic depends on:
1. Whether the population standard deviation `sigma` is known.
2. The sample size `n`.
3. Whether the population is normally distributed.

If `sigma` is known: use the **z-test**.
If `sigma` is unknown: use the **t-test** (provided the population is approximately normal or `n` is large).

---

### One-Sample z-Test for Mean (sigma known)

**When to use:**
- Population standard deviation `sigma` is known.
- Either the population is normally distributed OR `n >= 30` (Central Limit Theorem applies).

**Test statistic:**

`z = (bar{x} - mu_0) / (sigma / sqrt{n})`

where:
- `bar{x}` = sample mean
- `mu_0` = hypothesized population mean under `H_0`
- `sigma` = population standard deviation
- `n` = sample size

**Procedure:**

1. **State hypotheses:** `H_0: mu = mu_0` vs `H_1: mu != mu_0` (or `<` or `>`).
2. **Choose `alpha`:** e.g., `0.05`.
3. **Find critical value(s):**
   - Two-tailed: `z_{alpha/2}` from z-table
   - Right-tailed: `z_alpha` from z-table
   - Left-tailed: `-z_alpha` from z-table
4. **Compute test statistic:** `z = (bar{x} - mu_0) / (sigma / sqrt{n})`.
5. **Decision:**
   - Two-tailed: Reject `H_0` if `|z| > z_{alpha/2}`
   - Right-tailed: Reject `H_0` if `z > z_alpha`
   - Left-tailed: Reject `H_0` if `z < -z_alpha`
6. **Conclusion:** State the result in context.

---

#### Worked Example 1: z-test for mean

**Problem:** A cereal manufacturer claims that the average weight of a cereal box is 500 grams. A sample of 40 boxes has a mean weight of 495 grams. The population standard deviation is known to be 15 grams. Test the claim at `alpha = 0.05`.

**Solution:**

Step 1: `H_0: mu = 500`, `H_1: mu != 500` (two-tailed)

Step 2: `alpha = 0.05`

Step 3: Critical values: `z_{0.025} = pm 1.96`

Step 4: Compute test statistic:
`z = (495 - 500) / (15 / sqrt{40}) = (-5) / (15 / 6.3249) = (-5) / 2.3717 = -2.108`

Step 5: `|z| = 2.108 > 1.96`. Reject `H_0`.

Step 6: There is sufficient evidence at the 0.05 level to conclude that the average box weight is different from 500 grams.

---

### One-Sample t-Test for Mean (sigma unknown)

**When to use:**
- Population standard deviation `sigma` is unknown.
- Either the population is normally distributed OR `n >= 30`.
- The sample standard deviation `s` is used as an estimate.

**Test statistic:**

`t = (bar{x} - mu_0) / (s / sqrt{n})`

where:
- `s` = sample standard deviation
- Degrees of freedom `df = n - 1`

**Procedure:**

1. **State hypotheses.**
2. **Choose `alpha`.**
3. **Find critical value(s):** Use the t-distribution table with `df = n - 1`.
   - Two-tailed: `t_{alpha/2, n-1}`
   - Right-tailed: `t_{alpha, n-1}`
   - Left-tailed: `-t_{alpha, n-1}`
4. **Compute test statistic:** `t = (bar{x} - mu_0) / (s / sqrt{n})`.
5. **Decision:** Compare `t` with critical value(s).
6. **Conclusion.**

---

#### Worked Example 2: t-test for mean

**Problem:** A fitness trainer claims that the average resting heart rate of adults is 70 bpm. A sample of 16 adults has a mean of 73 bpm with a standard deviation of 6 bpm. Test the claim at `alpha = 0.01`. Assume the population is normally distributed.

**Solution:**

Step 1: `H_0: mu = 70`, `H_1: mu != 70` (two-tailed)

Step 2: `alpha = 0.01`

Step 3: `df = 16 - 1 = 15`. From t-table, `t_{0.005, 15} = 2.947`. Critical values: `pm 2.947`.

Step 4: Compute test statistic:
`t = (73 - 70) / (6 / sqrt{16}) = 3 / (6 / 4) = 3 / 1.5 = 2.00`

Step 5: `|t| = 2.00 < 2.947`. Fail to reject `H_0`.

Step 6: There is insufficient evidence at the 0.01 level to conclude the average resting heart rate differs from 70 bpm.

---

#### Worked Example 3: One-tailed t-test

**Problem:** A company claims that its new training program reduces the average assembly time below the current average of 30 minutes. A sample of 9 employees who completed the new program had an average assembly time of 27 minutes with a standard deviation of 4 minutes. Test at `alpha = 0.05`. Assume normality.

**Solution:**

Step 1: `H_0: mu >= 30`, `H_1: mu < 30` (left-tailed)

Step 2: `alpha = 0.05`

Step 3: `df = 8`. From t-table, `t_{0.05, 8} = 1.860`. Since left-tailed, critical value = `-1.860`.

Step 4: Compute test statistic:
`t = (27 - 30) / (4 / sqrt{9}) = (-3) / (4 / 3) = (-3) / 1.333 = -2.25`

Step 5: `t = -2.25 < -1.860`. Reject `H_0`.

Step 6: There is sufficient evidence at the 0.05 level that the new training program reduces assembly time.

---

### When to Use z vs t

| Condition | Test to Use | Formula |
|---|---|---|
| `sigma` known, normal population or `n >= 30` | z-test | `z = (bar{x} - mu_0) / (sigma / sqrt{n})` |
| `sigma` unknown, normal population or `n >= 30` | t-test | `t = (bar{x} - mu_0) / (s / sqrt{n})` |
| `sigma` unknown, small sample, non-normal | Non-parametric test (beyond scope) | -- |

**Rule of thumb:**
- If `sigma` is known, always use z.
- If `sigma` is unknown and `n` is large (`n >= 30`), the t-test is approximately equivalent to the z-test (t approaches z as `n` increases), but t-test is more accurate.
- If `sigma` is unknown and `n` is small, use the t-test only if the population is approximately normal.

---

### Assumptions for Both Tests

1. **Random sample:** The data must come from a random sample.
2. **Independence:** Observations are independent.
3. **Normality:** The population is normally distributed (for small `n`). For large `n`, the Central Limit Theorem ensures approximate normality of the sampling distribution.
4. **Scale:** The data is measured on an interval or ratio scale.

---

## Practice Problems

1. A sample of 25 students has a mean test score of 78 with a standard deviation of 8. Test whether the population mean is different from 75 at `alpha = 0.05` (use t-test).
   <details>
   <summary>Show Answer</summary>
   `t = (78 - 75) / (8/5) = 1.875`, `df = 24`, critical values `pm 2.064`. Fail to reject `H_0` since `1.875 < 2.064`.
   </details>

2. A factory produces bolts with a known standard deviation of 2 mm. A sample of 36 bolts has a mean diameter of 12.5 mm. Test `H_0: mu = 12` against `H_1: mu > 12` at `alpha = 0.01`.
   <details>
   <summary>Show Answer</summary>
   `z = (12.5 - 12) / (2/6) = 1.5`, `z_{0.01} = 2.326`. Fail to reject `H_0` since `1.5 < 2.326`.
   </details>

3. When would you use a t-test instead of a z-test?
   <details>
   <summary>Show Answer</summary>
   When the population standard deviation `sigma` is unknown and must be estimated using the sample standard deviation `s`.
   </details>

4. A sample of 10 patients has mean cholesterol 190 mg/dL with `s = 20`. Test `H_0: mu = 200` against `H_1: mu < 200` at `alpha = 0.05`.
   <details>
   <summary>Show Answer</summary>
   `t = (190 - 200) / (20 / sqrt{10}) = -1.581`, `df = 9`, `t_{0.05,9} = 1.833`. Since `-1.581 > -1.833`, fail to reject `H_0`.
   </details>

5. For which of the following would you use a z-test? (a) n=15, sigma known; (b) n=40, sigma unknown; (c) n=100, sigma known; (d) n=8, sigma unknown.
   <details>
   <summary>Show Answer</summary>
   (a) and (c) -- z-test is appropriate when sigma is known. For (b), use t-test. For (d), use t-test only if population is normal.
   </details>
