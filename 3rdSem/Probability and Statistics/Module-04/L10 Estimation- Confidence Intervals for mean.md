# Estimation: Confidence Intervals for mean

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 10  
**Date:** 29-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.7

## Notes

### 1. Concept of Confidence Interval

A point estimate gives a single "best guess" for a parameter, but it does not convey the precision or reliability of that estimate. A **confidence interval (CI)** provides a range of plausible values for the parameter, along with a **confidence level** that quantifies how confident we are that the interval contains the true parameter.

#### 1.1 Definition

A `(1 - alpha) * 100%` confidence interval for a parameter `theta` is an interval `(L, U)` such that:

`P(L <= theta <= U) = 1 - alpha`

where:
- `(1 - alpha)` is the **confidence level** (e.g., 0.95 for 95% confidence).
- `alpha` is the **significance level** (e.g., 0.05 for 95% confidence).
- `L` and `U` are the **lower** and **upper confidence limits**, respectively.

#### 1.2 Interpretation

**Correct interpretation:** If we were to take many random samples and compute a 95% confidence interval from each, approximately 95% of those intervals would contain the true population parameter.

**Incorrect interpretation:** "There is a 95% probability that the true parameter lies in this interval." (The parameter is fixed, not random. The interval is random.)

#### 1.3 General Form

`point estimate +/- margin of error`

`margin of error = critical value * standard error`

---

### 2. Confidence Interval for Mean When `sigma` is Known (z-Interval)

#### 2.1 Assumptions

1. The sample is a random sample from the population.
2. The population standard deviation `sigma` is **known**.
3. Either:
   - The population is normally distributed, OR
   - The sample size is large (`n >= 30`) so the CLT applies.

#### 2.2 Formula

A `(1 - alpha) * 100%` confidence interval for the population mean `mu` is:

`bar{x} +/- z_{alpha/2} * (sigma / sqrt{n})`

where:
- `bar{x}` is the sample mean.
- `z_{alpha/2}` is the critical value from the standard normal distribution such that `P(Z > z_{alpha/2}) = alpha/2`.
- `sigma / sqrt{n}` is the standard error of the mean.

#### 2.3 Common z Critical Values

| Confidence Level | `alpha` | `alpha/2` | `z_{alpha/2}` |
|-----------------|---------|-----------|---------------|
| 90% | 0.10 | 0.05 | 1.645 |
| 95% | 0.05 | 0.025 | 1.960 |
| 99% | 0.01 | 0.005 | 2.576 |

#### 2.4 Step-by-Step Procedure

1. Check assumptions (random sample, known `sigma`, normal population or large `n`).
2. Determine the confidence level `(1 - alpha)`.
3. Find the critical value `z_{alpha/2}` from the standard normal table.
4. Compute the margin of error: `ME = z_{alpha/2} * sigma / sqrt{n}`.
5. Compute the confidence interval: `bar{x} +/- ME`.
6. Interpret the interval in the context of the problem.

---

### 3. Confidence Interval for Mean When `sigma` is Unknown (t-Interval)

#### 3.1 The t-Distribution

When `sigma` is unknown, we estimate it using the sample standard deviation `s`. The standardized statistic follows a **t-distribution** with `n-1` degrees of freedom:

`t = (bar{x} - mu) / (s / sqrt{n}) ~ t_{n-1}`

The t-distribution is similar to the standard normal but has heavier tails (more variability) to account for the uncertainty in estimating `sigma`. As `n -> infinity`, the t-distribution approaches the normal distribution.

#### 3.2 Assumptions

1. The sample is a random sample.
2. The population standard deviation `sigma` is **unknown** (estimated by `s`).
3. Either:
   - The population is normally distributed, OR
   - The sample size is large (`n >= 30`).

#### 3.3 Formula

A `(1 - alpha) * 100%` confidence interval for the population mean `mu` is:

`bar{x} +/- t_{alpha/2, n-1} * (s / sqrt{n})`

where:
- `s` is the sample standard deviation.
- `t_{alpha/2, n-1}` is the critical value from the t-distribution with `n-1` degrees of freedom.

#### 3.4 Step-by-Step Procedure

1. Check assumptions.
2. Compute `bar{x}` and `s` from the sample data.
3. Determine the confidence level `(1 - alpha)`.
4. Find the critical value `t_{alpha/2, n-1}` from the t-table.
5. Compute the margin of error: `ME = t_{alpha/2, n-1} * s / sqrt{n}`.
6. Compute the confidence interval: `bar{x} +/- ME`.
7. Interpret the interval.

---

### 4. Comparison: z-Interval vs t-Interval

| Aspect | z-Interval | t-Interval |
|--------|------------|------------|
| When to use | `sigma` known | `sigma` unknown |
| Critical value | `z_{alpha/2}` | `t_{alpha/2, n-1}` |
| Distribution | Standard normal | t-distribution |
| Degrees of freedom | None | `n-1` |
| Width | Narrower (if `n` same) | Wider (accounts for extra uncertainty) |
| Large `n` behavior | Same | Approaches z-interval |

---

### 5. Worked Examples

#### Example 1: z-Interval (sigma known)

A manufacturer knows that the standard deviation of the lifetime of light bulbs is `sigma = 100` hours. A random sample of 50 bulbs has an average lifetime of `bar{x} = 1200` hours. Construct a 95% confidence interval for the population mean lifetime.

**Solution:**

Step 1: Assumptions met (random sample, `sigma` known, `n = 50 >= 30`).

Step 2: 95% confidence => `alpha = 0.05`, `alpha/2 = 0.025`.

Step 3: `z_{0.025} = 1.96`

Step 4: `ME = 1.96 * 100 / sqrt{50} = 1.96 * 100 / 7.071 = 1.96 * 14.142 = 27.72`

Step 5: CI = `1200 +/- 27.72` = `(1172.28, 1227.72)`

Step 6: We are 95% confident that the true mean lifetime of all light bulbs is between 1172.28 and 1227.72 hours.

---

#### Example 2: t-Interval (sigma unknown)

A sample of 10 students yields the following test scores: 72, 85, 91, 68, 77, 83, 79, 74, 88, 93. Construct a 90% confidence interval for the population mean score.

**Solution:**

Step 1: `n = 10` (small), `sigma` unknown. We assume the population of test scores is approximately normal.

Step 2: Compute `bar{x}` and `s`.

`bar{x} = (72 + 85 + 91 + 68 + 77 + 83 + 79 + 74 + 88 + 93) / 10 = 810 / 10 = 81`

`s^2 = (1/9) * sum (x_i - 81)^2`

Deviations: `-9, 4, 10, -13, -4, 2, -2, -7, 7, 12`

Squared: `81, 16, 100, 169, 16, 4, 4, 49, 49, 144`

Sum of squares = `636`

`s^2 = 636 / 9 = 70.667`

`s = sqrt{70.667} = 8.406`

Step 3: 90% confidence => `alpha = 0.10`, `alpha/2 = 0.05`, `n-1 = 9`.

Step 4: From t-table, `t_{0.05, 9} = 1.833`

Step 5: `ME = 1.833 * 8.406 / sqrt{10} = 1.833 * 8.406 / 3.162 = 1.833 * 2.658 = 4.872`

Step 6: CI = `81 +/- 4.872` = `(76.128, 85.872)`

Step 7: We are 90% confident that the true mean test score is between 76.13 and 85.87.

---

#### Example 3: Effect of Confidence Level

Using the data from Example 1 (`bar{x} = 1200`, `sigma = 100`, `n = 50`), construct 90%, 95%, and 99% confidence intervals.

**Solution:**

| Confidence Level | `z_{alpha/2}` | Margin of Error | Confidence Interval |
|-----------------|---------------|-----------------|---------------------|
| 90% | 1.645 | `1.645 * 14.142 = 23.26` | `(1176.74, 1223.26)` |
| 95% | 1.960 | `1.960 * 14.142 = 27.72` | `(1172.28, 1227.72)` |
| 99% | 2.576 | `2.576 * 14.142 = 36.43` | `(1163.57, 1236.43)` |

**Observation:** Higher confidence levels produce wider intervals. There is a trade-off between confidence and precision.

---

#### Example 4: Effect of Sample Size

For `sigma = 15`, `bar{x} = 100`, construct 95% CIs for `n = 25` and `n = 100`.

**Solution:**

For `n = 25`: `ME = 1.96 * 15 / 5 = 5.88`. CI: `(94.12, 105.88)`

For `n = 100`: `ME = 1.96 * 15 / 10 = 2.94`. CI: `(97.06, 102.94)`

**Observation:** Larger sample sizes produce narrower intervals (more precision).

---

#### Example 5: z-Interval with Small Sample from Normal Population

The weights of a certain product are known to be normally distributed with `sigma = 2` grams. A sample of 4 items has mean weight `bar{x} = 50` grams. Construct a 95% CI for the population mean weight.

**Solution:**

`n = 4` is small, but the population is normal and `sigma` is known. The z-interval is valid.

`ME = 1.96 * 2 / sqrt{4} = 1.96 * 1 = 1.96`

CI: `50 +/- 1.96` = `(48.04, 51.96)`

---

### 6. Interpreting Confidence Intervals

**Correct statements:**
- "We are 95% confident that the interval contains the true population mean."
- "If we repeated this sampling procedure many times, 95% of the resulting intervals would contain the true mean."

**Incorrect statements:**
- "There is a 95% probability that the true mean is in this interval." (The true mean is fixed, not random.)
- "95% of the data falls within this interval." (That is a prediction interval, not a confidence interval.)

---

### 7. Summary

| Scenario | Procedure | Formula | Critical Value |
|----------|-----------|---------|---------------|
| `sigma` known, normal population or large `n` | z-interval | `bar{x} +/- z * sigma/sqrt{n}` | `z_{alpha/2}` |
| `sigma` unknown, normal population or large `n` | t-interval | `bar{x} +/- t * s/sqrt{n}` | `t_{alpha/2, n-1}` |

---

## Practice Problems

**Problem 1:** A sample of 36 observations from a population with `sigma = 12` gives `bar{x} = 85`. Construct a 99% confidence interval for the population mean.

**Problem 2:** A random sample of 16 bottles from a filling machine yields an average fill volume of 500 ml with a sample standard deviation of 3 ml. Assuming the fill volumes are normally distributed, construct a 95% confidence interval for the population mean fill volume.

**Problem 3:** For a 90% confidence interval with `n = 20` and `sigma` unknown, what is the critical t-value? What is the z-value for the same confidence level?

**Problem 4:** A researcher wants to estimate the mean height of students at a university. She samples 100 students and finds `bar{x} = 168` cm and `s = 10` cm. Construct a 95% confidence interval.

**Problem 5:** Explain what happens to the width of a confidence interval when:
(a) The confidence level increases from 90% to 99%.
(b) The sample size increases from 25 to 100.
(c) The population standard deviation decreases.

---

### Answers / Hints

**Problem 1:** `z_{0.005} = 2.576`. `ME = 2.576 * 12/6 = 5.152`. CI = `85 +/- 5.152` = `(79.848, 90.152)`.

**Problem 2:** `t_{0.025, 15} = 2.131`. `ME = 2.131 * 3/4 = 1.598`. CI = `500 +/- 1.598` = `(498.402, 501.598)`.

**Problem 3:** `t_{0.05, 19} = 1.729`. `z_{0.05} = 1.645`. The t-value is larger because of the additional uncertainty from estimating `sigma`.

**Problem 4:** `df = 99`, `t_{0.025, 99} approx 1.984` (close to 1.96 for large `n`). `ME = 1.984 * 10/10 = 1.984`. CI = `168 +/- 1.984` = `(166.016, 169.984)`.

**Problem 5:** (a) The interval becomes wider (larger critical value). (b) The interval becomes narrower (standard error decreases by factor of `sqrt{n}`). (c) The interval becomes narrower (smaller standard error).
