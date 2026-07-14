# Testing a Hypothesis and significance

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 2  
**Date:** 08-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Interactive Learning  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18..1

## Notes

---

### Steps in Hypothesis Testing

Hypothesis testing is a systematic procedure for deciding whether the sample evidence supports rejecting the null hypothesis. The steps are:

#### Step 1: State the hypotheses
- Formulate `H_0` and `H_1` clearly.
- `H_0` contains equality; `H_1` contains `!=`, `<`, or `>`.

#### Step 2: Choose the significance level `alpha`
- `alpha` is the probability of rejecting `H_0` when it is actually true.
- Common choices: `alpha = 0.05`, `0.01`, `0.10`.

#### Step 3: Determine the test statistic
- Choose the appropriate test statistic based on the data type and assumptions.
- The test statistic follows a known sampling distribution (e.g., `z`, `t`, `chi^2`, `F`).

#### Step 4: Determine the decision rule
- Two approaches: **critical value approach** or **p-value approach**.
- Define the rejection (critical) region.

#### Step 5: Compute the test statistic from sample data
- Plug sample statistics into the test statistic formula.

#### Step 6: Make a decision
- If test statistic falls in the rejection region (or `p-value < alpha`), reject `H_0`.
- Otherwise, fail to reject `H_0`.

#### Step 7: State the conclusion
- Write the conclusion in the context of the problem.

---

### Type I Error (alpha)

A **Type I error** occurs when we reject a true null hypothesis.

- Probability of Type I error = `alpha` (the significance level).
- It is a "false positive" -- we conclude there is an effect when there is none.

| Decision | `H_0` True | `H_0` False |
|---|---|---|
| Reject `H_0` | **Type I Error** (probability = `alpha`) | Correct decision (power) |
| Fail to reject `H_0` | Correct decision | **Type II Error** (probability = `beta`) |

---

### Type II Error (beta)

A **Type II error** occurs when we fail to reject a false null hypothesis.

- Probability of Type II error = `beta`.
- It is a "false negative" -- we conclude there is no effect when there actually is one.
- `beta` depends on:
  - The true value of the parameter
  - The sample size `n`
  - The significance level `alpha`
  - The variability of the data

---

### Significance Level (`alpha`)

The **significance level** `alpha` is the maximum probability of committing a Type I error that we are willing to accept.

| `alpha` | Interpretation |
|---|---|
| `0.10` | 10% risk of Type I error; used in exploratory research |
| `0.05` | 5% risk; most common in scientific research |
| `0.01` | 1% risk; used when consequences of Type I error are severe |
| `0.001` | 0.1% risk; used in high-stakes medical trials |

---

### Power of a Test

The **power** of a hypothesis test is the probability of correctly rejecting a false null hypothesis.

- `Power = 1 - beta`
- A test with high power is more likely to detect a true effect.

**Factors affecting power:**

| Factor | Effect on Power |
|---|---|
| Increase sample size `n` | Increases power |
| Increase `alpha` | Increases power (but also increases Type I error) |
| Larger true effect size | Increases power |
| Lower variability | Increases power |

---

### Test Statistic

A **test statistic** is a numerical value computed from sample data that is used to decide whether to reject `H_0`. It measures how far the sample statistic deviates from the hypothesized parameter value.

General form:

`text(test statistic) = (text(sample statistic) - text(hypothesized parameter)) / (text(standard error))`

Examples:
- For mean (`sigma` known): `z = (bar{x} - mu_0) / (sigma / sqrt{n})`
- For mean (`sigma` unknown): `t = (bar{x} - mu_0) / (s / sqrt{n})`
- For proportion: `z = (hat{p} - p_0) / sqrt{p_0 (1 - p_0) / n}`

---

### Critical Value Approach

**Critical values** are the boundary values of the rejection region, determined by `alpha` and the sampling distribution.

**Procedure:**
1. Choose `alpha` and determine whether the test is one-tailed or two-tailed.
2. Find the critical value(s) from the appropriate distribution table (z-table, t-table, etc.).
3. Define the rejection region: reject `H_0` if the test statistic falls in this region.

| Test Type | Critical Region | Decision Rule |
|---|---|---|
| Two-tailed | `|z| > z_{alpha/2}` | Reject `H_0` if `|text(test stat)| > text(critical value)` |
| Right-tailed | `z > z_alpha` | Reject `H_0` if `text(test stat) > text(critical value)` |
| Left-tailed | `z < -z_alpha` | Reject `H_0` if `text(test stat) < text(critical value)` |

---

### P-value Approach

The **p-value** (or probability value) is the probability, assuming `H_0` is true, of obtaining a test statistic as extreme as or more extreme than the one observed.

**Procedure:**
1. Compute the test statistic from the sample.
2. Find the p-value using the sampling distribution:
   - For `z`-test: use the standard normal table.
   - For `t`-test: use the t-distribution table.
3. Compare p-value with `alpha`:
   - If `p-value <= alpha`: reject `H_0`
   - If `p-value > alpha`: fail to reject `H_0`

| p-value | Evidence against `H_0` |
|---|---|
| `p < 0.01` | Very strong evidence |
| `0.01 <= p < 0.05` | Strong evidence |
| `0.05 <= p < 0.10` | Weak evidence |
| `p >= 0.10` | Little to no evidence |

---

### Worked Example: Comparing Both Approaches

**Problem:** A manufacturer claims that the average lifetime of their light bulbs is 1200 hours. A sample of 36 bulbs has a mean of 1170 hours with a known population standard deviation of 90 hours. Test the claim at `alpha = 0.05`.

#### Step 1: State hypotheses
`H_0: mu = 1200`  
`H_1: mu != 1200` (two-tailed)

#### Step 2: Significance level
`alpha = 0.05`

#### Step 3: Test statistic
`z = (bar{x} - mu_0) / (sigma / sqrt{n}) = (1170 - 1200) / (90 / sqrt{36}) = (-30) / (90 / 6) = (-30) / 15 = -2.00`

#### Step 4a: Critical value approach
For `alpha = 0.05` (two-tailed), critical values: `z_{alpha/2} = z_{0.025} = pm 1.96`

Decision rule: Reject `H_0` if `|z| > 1.96`.

Since `|z| = 2.00 > 1.96`, we **reject `H_0`**.

#### Step 4b: P-value approach
For `z = -2.00`, the left-tail probability from the z-table is `0.0228`.

Since two-tailed: `p-value = 2 times 0.0228 = 0.0456`

Compare with `alpha = 0.05`: `0.0456 < 0.05`, so we **reject `H_0`**.

#### Step 5: Conclusion
There is sufficient evidence at the 0.05 significance level to conclude that the average lifetime of the bulbs is different from 1200 hours.

---

### Important Relationship

The critical value approach and p-value approach always yield the same decision. They are just two different ways of looking at the same test:
- Critical value: compares test statistic to a fixed threshold.
- P-value: computes the probability and compares it to `alpha`.

---

## Practice Problems

1. In hypothesis testing, what is the relationship between Type I error and the significance level?
   <details>
   <summary>Show Answer</summary>
   The significance level `alpha` is exactly the probability of making a Type I error.
   </details>

2. A test has `alpha = 0.01` and `p-value = 0.03`. Should you reject `H_0`?
   <details>
   <summary>Show Answer</summary>
   No, because `0.03 > 0.01`, so we fail to reject `H_0`.
   </details>

3. A researcher obtains `z = 1.75` in a right-tailed test at `alpha = 0.05` (critical value `z_{0.05} = 1.645`). What is the decision?
   <details>
   <summary>Show Answer</summary>
   Reject `H_0` because `1.75 > 1.645`.
   </details>

4. Explain what it means to have a test with 80% power.
   <details>
   <summary>Show Answer</summary>
   If `H_0` is false, there is an 80% probability that the test will correctly reject it.
   </details>

5. A two-tailed test yields a test statistic `z = 2.33`. Find the p-value and state the decision at `alpha = 0.05`.
   <details>
   <summary>Show Answer</summary>
   p-value = `2 times P(Z > 2.33) = 2 times 0.0099 = 0.0198`. Since `0.0198 < 0.05`, reject `H_0`.
   </details>
