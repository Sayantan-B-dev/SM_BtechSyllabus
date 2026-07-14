# Testing of hypothesis for Proportion

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 6  
**Date:** 16-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.6.2-18.6.4

## Notes

---

### Overview

Hypothesis testing for a population proportion `p` is used when the data is categorical (success/failure, yes/no, defective/non-defective). We test a claim about the proportion of successes in the population.

---

### Conditions for One-Sample z-Test for Proportion

Before conducting a z-test for proportion, the following conditions MUST be satisfied:

1. **Random sample:** The sample must be a simple random sample from the population.
2. **Independence:** Sample size `n` must be less than 10% of the population if sampling without replacement.
3. **Large sample (normality condition):** Both `n p_0` and `n (1 - p_0)` must be at least 10 (or sometimes 5), where `p_0` is the hypothesized proportion under `H_0`.
   - `n p_0 >= 10`
   - `n (1 - p_0) >= 10`

If these conditions are met, the sampling distribution of `hat{p}` is approximately normal.

---

### Formula for Test Statistic

The test statistic for a one-sample z-test for proportion is:

`z = (hat{p} - p_0) / sqrt{p_0 (1 - p_0) / n}`

where:
- `hat{p} = x / n` = sample proportion (x = number of successes in the sample)
- `p_0` = hypothesized population proportion under `H_0`
- `n` = sample size

The denominator `sqrt{p_0 (1 - p_0) / n}` is the **standard error** of `hat{p}` under `H_0`.

---

### Step-by-Step Procedure

1. **State hypotheses:**
   - Two-tailed: `H_0: p = p_0` vs `H_1: p != p_0`
   - Right-tailed: `H_0: p <= p_0` vs `H_1: p > p_0`
   - Left-tailed: `H_0: p >= p_0` vs `H_1: p < p_0`

2. **Choose significance level `alpha`.**

3. **Check conditions:**
   - Random sample?
   - `n p_0 >= 10` and `n (1 - p_0) >= 10`?

4. **Find critical value(s):** From z-table (z-test for proportion always uses z).

5. **Compute test statistic:**
   `z = (hat{p} - p_0) / sqrt{p_0 (1 - p_0) / n}`

6. **Decision:**
   - Two-tailed: reject `H_0` if `|z| > z_{alpha/2}`
   - Right-tailed: reject `H_0` if `z > z_alpha`
   - Left-tailed: reject `H_0` if `z < -z_alpha`

7. **Conclusion:** Interpret in the context of the problem.

---

### Worked Example 1: Testing a Claim About a Population Proportion

**Problem:** A company claims that at least 90% of its customers are satisfied with its service. A survey of 200 randomly selected customers found that 172 are satisfied. Test the company's claim at `alpha = 0.05`.

**Solution:**

Step 1: State hypotheses.
- `H_0: p >= 0.90` (the claim -- at least 90% satisfied)
- `H_1: p < 0.90` (left-tailed test)

Step 2: `alpha = 0.05`.

Step 3: Check conditions.
- Random sample: Yes.
- `n p_0 = 200 * 0.90 = 180 >= 10` (ok)
- `n (1 - p_0) = 200 * 0.10 = 20 >= 10` (ok)

Step 4: Critical value. Left-tailed, `alpha = 0.05`: `z_{0.05} = 1.645`. Critical region: `z < -1.645`.

Step 5: Compute test statistic.
`hat{p} = 172 / 200 = 0.86`

`z = (0.86 - 0.90) / sqrt{0.90 * 0.10 / 200} = (-0.04) / sqrt{0.09 / 200} = (-0.04) / sqrt{0.00045} = (-0.04) / 0.02121 = -1.886`

Step 6: Decision.
`z = -1.886 < -1.645`. Reject `H_0`.

Step 7: Conclusion.
There is sufficient evidence at the 0.05 significance level to conclude that the proportion of satisfied customers is less than 90%. The company's claim is not supported.

**Alternative using p-value:**
`p-value = P(Z < -1.886) = 0.0297`
Since `0.0297 < 0.05`, we reject `H_0`.

---

### Worked Example 2: Two-Tailed Proportion Test

**Problem:** A coin is flipped 100 times and lands heads 61 times. Is the coin fair? Test at `alpha = 0.01`.

**Solution:**

Step 1: `H_0: p = 0.50` (fair coin) vs `H_1: p != 0.50` (biased coin)

Step 2: `alpha = 0.01`

Step 3: Conditions check.
- `n p_0 = 100 * 0.5 = 50 >= 10` (ok)
- `n (1 - p_0) = 100 * 0.5 = 50 >= 10` (ok)

Step 4: Critical values. Two-tailed, `alpha = 0.01`: `z_{0.005} = 2.576`. Reject if `|z| > 2.576`.

Step 5: Compute test statistic.
`hat{p} = 61 / 100 = 0.61`

`z = (0.61 - 0.50) / sqrt{0.50 * 0.50 / 100} = 0.11 / sqrt{0.25 / 100} = 0.11 / 0.05 = 2.20`

Step 6: Decision.
`|z| = 2.20 < 2.576`. Fail to reject `H_0`.

Step 7: Conclusion.
There is insufficient evidence at the 0.01 significance level to conclude that the coin is biased. The result is not statistically significant.

**Using p-value:** `P(Z > 2.20) = 0.0139`. Two-tailed: `p = 2 * 0.0139 = 0.0278`. Since `0.0278 > 0.01`, fail to reject `H_0`.

---

### Worked Example 3: Right-Tailed Proportion Test

**Problem:** A candidate claims that more than 50% of voters support her. A poll of 400 voters finds 215 supporters. Test at `alpha = 0.05`.

**Solution:**

Step 1: `H_0: p <= 0.50`, `H_1: p > 0.50` (right-tailed)

Step 2: `alpha = 0.05`

Step 3: `n p_0 = 200`, `n (1 - p_0) = 200`. Conditions satisfied.

Step 4: Critical value: `z_{0.05} = 1.645`. Reject if `z > 1.645`.

Step 5: `hat{p} = 215 / 400 = 0.5375`

`z = (0.5375 - 0.50) / sqrt{0.50 * 0.50 / 400} = 0.0375 / sqrt{0.25 / 400} = 0.0375 / 0.025 = 1.50`

Step 6: `z = 1.50 < 1.645`. Fail to reject `H_0`.

Step 7: There is insufficient evidence at the 0.05 level to conclude that more than 50% of voters support the candidate.

---

### Confidence Interval Approach

The z-test for proportion is equivalent to checking whether the hypothesized proportion `p_0` falls inside a `(1 - alpha)%` confidence interval for `p`.

**Confidence interval for `p`:**

`hat{p} pm z_{alpha/2} * sqrt{hat{p} (1 - hat{p}) / n}`

**Decision:** If `p_0` falls inside the confidence interval, fail to reject `H_0`. If `p_0` falls outside, reject `H_0`.

---

### Summary of One-Sample z-Test for Proportion

| Element | Value |
|---|---|
| Test statistic | `z = (hat{p} - p_0) / sqrt{p_0 (1 - p_0) / n}` |
| Distribution | Standard normal (z) |
| Conditions | Random sample, `n p_0 >= 10`, `n (1 - p_0) >= 10` |
| Data type | Categorical (binary) |

---

## Practice Problems

1. A drug company claims that 95% of patients recover using their medication. In a trial of 300 patients, 276 recover. Test the claim at `alpha = 0.05`.
   <details>
   <summary>Show Answer</summary>
   `H_0: p = 0.95`, `H_1: p != 0.95`. `hat{p} = 0.92`. `z = (0.92 - 0.95) / sqrt{0.95*0.05/300} = -2.38`. `z_{0.025} = 1.96`. `|z| = 2.38 > 1.96`, reject `H_0`. The claim is not supported.
   </details>

2. A school claims that at least 80% of its students pass a proficiency test. A sample of 50 students shows 37 passing. Test at `alpha = 0.10`.
   <details>
   <summary>Show Answer</summary>
   `H_0: p >= 0.80`, `H_1: p < 0.80`. `hat{p} = 0.74`. `z = (0.74 - 0.80) / sqrt{0.80*0.20/50} = -1.061`. `z_{0.10} = 1.282`. Since `-1.061 > -1.282`, fail to reject `H_0`. Claim is supported.
   </details>

3. A survey finds that 45 out of 200 people prefer a new brand. Test whether the preference rate differs from 25% at `alpha = 0.05`.
   <details>
   <summary>Show Answer</summary>
   `H_0: p = 0.25`, `H_1: p != 0.25`. `hat{p} = 0.225`. `z = (0.225 - 0.25) / sqrt{0.25*0.75/200} = -0.816`. `z_{0.025} = 1.96`. `|z| = 0.816 < 1.96`, fail to reject `H_0`.
   </details>

4. What are the necessary conditions for using a one-sample z-test for proportion?
   <details>
   <summary>Show Answer</summary>
   Random sample, `n p_0 >= 10`, and `n (1 - p_0) >= 10`.
   </details>

5. A researcher wants to test if a new teaching method improves the pass rate above the current 60%. She gets a sample of 80 students with 54 passing. Test at `alpha = 0.01`.
   <details>
   <summary>Show Answer</summary>
   `H_0: p <= 0.60`, `H_1: p > 0.60`. `hat{p} = 0.675`. `z = (0.675 - 0.60) / sqrt{0.60*0.40/80} = 1.369`. `z_{0.01} = 2.326`. Since `1.369 < 2.326`, fail to reject `H_0`.
   </details>
