# Estimation: Confidence Intervals for Proportion

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 11  
**Date:** 01-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.7

## Notes

### 1. Introduction

In many real-world problems, we are interested in estimating a **proportion** or **percentage** -- the fraction of a population that possesses a certain characteristic. Examples include:

- Proportion of voters who support a candidate.
- Proportion of defective items in a production line.
- Proportion of patients who recover after a treatment.
- Proportion of households that own a car.

---

### 2. Sampling Distribution of the Sample Proportion

Let `X` be the number of "successes" (individuals with the characteristic of interest) in a random sample of size `n`. Then:

`X ~ Binomial(n, p)`

The sample proportion is:

`hat{p} = X / n`

#### Properties:

- `E[hat{p}] = p` (unbiased)
- `Var(hat{p}) = p(1-p) / n`
- `SE(hat{p}) = sqrt(p(1-p) / n)`

#### CLT for Sample Proportion:

For large `n`, by the Central Limit Theorem:

`hat{p} ~ approx N(p, p(1-p)/n)`

The standardized version:

`Z = (hat{p} - p) / sqrt(p(1-p)/n) ~ approx N(0, 1)`

---

### 3. Confidence Interval for Population Proportion `p`

#### 3.1 Conditions

To use the normal approximation, the following conditions must be satisfied:

1. The sample is a simple random sample.
2. The population is at least 20 times the sample size (`N >= 20*n`).
3. **Success-failure condition:** Both the number of successes and failures are at least 5:
   - `n * hat{p} >= 5` and `n * (1 - hat{p}) >= 5`
   - Alternatively (more conservatively): `n * p >= 5` and `n * (1-p) >= 5`

#### 3.2 Formula

A `(1 - alpha) * 100%` confidence interval for the population proportion `p` is:

`hat{p} +/- z_{alpha/2} * sqrt{hat{p} * (1 - hat{p}) / n}`

where:
- `hat{p}` is the sample proportion.
- `z_{alpha/2}` is the critical value from the standard normal distribution.
- `sqrt{hat{p} * (1 - hat{p}) / n}` is the **estimated standard error** (we use `hat{p}` as an estimate of `p` in the standard error formula).

#### 3.3 Step-by-Step Procedure

1. Check the conditions: random sample, `n * hat{p} >= 5`, `n * (1 - hat{p}) >= 5`.
2. Compute `hat{p} = x / n` (sample proportion).
3. Determine the confidence level `(1 - alpha)`.
4. Find `z_{alpha/2}` from the standard normal table.
5. Compute the margin of error: `ME = z_{alpha/2} * sqrt{hat{p} * (1 - hat{p}) / n}`.
6. Compute the confidence interval: `hat{p} +/- ME`.
7. Interpret the interval.

---

### 4. Sample Size Determination

Before conducting a survey, we often need to determine how large a sample is required to achieve a desired margin of error.

#### 4.1 Formula

The margin of error for a proportion is:

`ME = z_{alpha/2} * sqrt{p* * (1 - p*) / n}`

Solving for `n`:

`n = (z_{alpha/2})^2 * p* * (1 - p*) / (ME)^2`

where `p*` is an estimate of the population proportion (from a pilot study, prior research, or using `p* = 0.5` for the maximum sample size).

#### 4.2 Conservative Approach (Worst-Case)

The product `p*(1-p*)` is maximized when `p* = 0.5`, which gives `p*(1-p*) = 0.25`. Using `p* = 0.5` yields the largest (most conservative) sample size:

`n = (z_{alpha/2})^2 * 0.25 / (ME)^2`

This is a safe choice when we have no prior information about `p`.

#### 4.3 When Prior Information is Available

If we have a prior estimate `p*` (e.g., from a previous study), we use it. This often gives a smaller required sample size.

#### 4.4 Rounding

Always **round up** to the next integer when computing sample size, to ensure the margin of error is at most the desired value.

---

### 5. Common z Critical Values for Proportions

| Confidence Level | `z_{alpha/2}` |
|-----------------|---------------|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

---

### 6. Worked Examples

#### Example 1: Confidence Interval for a Proportion

A survey of 500 randomly selected voters finds that 280 support a particular candidate. Construct a 95% confidence interval for the true proportion of voters who support the candidate.

**Solution:**

Step 1: Check conditions.
- Random sample: Yes.
- `n * hat{p} = 500 * (280/500) = 280 >= 5`. Good.
- `n * (1 - hat{p}) = 500 * (220/500) = 220 >= 5`. Good.

Step 2: `hat{p} = 280 / 500 = 0.56`

Step 3: 95% confidence => `alpha = 0.05`, `alpha/2 = 0.025`.

Step 4: `z_{0.025} = 1.96`

Step 5: `SE(hat{p}) = sqrt{0.56 * 0.44 / 500} = sqrt{0.2464 / 500} = sqrt{0.0004928} = 0.02220`

`ME = 1.96 * 0.02220 = 0.0435`

Step 6: CI = `0.56 +/- 0.0435` = `(0.5165, 0.6035)`

Step 7: We are 95% confident that the true proportion of voters supporting the candidate is between 51.65% and 60.35%.

---

#### Example 2: Proportion with 99% Confidence

In a quality control check, 15 out of 200 items are found to be defective. Construct a 99% confidence interval for the true proportion of defective items.

**Solution:**

`hat{p} = 15 / 200 = 0.075`

Check conditions: `200 * 0.075 = 15 >= 5`, `200 * 0.925 = 185 >= 5`. Good.

`z_{0.005} = 2.576`

`SE = sqrt{0.075 * 0.925 / 200} = sqrt{0.069375 / 200} = sqrt{0.000346875} = 0.01862`

`ME = 2.576 * 0.01862 = 0.0480`

CI = `0.075 +/- 0.0480` = `(0.0270, 0.1230)`

We are 99% confident that the true proportion of defective items is between 2.70% and 12.30%.

---

#### Example 3: When Conditions Are Not Met

A sample of 20 items contains 2 defective items. Can we construct a valid confidence interval?

**Solution:**

`hat{p} = 2/20 = 0.10`

`n * hat{p} = 20 * 0.10 = 2 < 5`. The success-failure condition is **not** satisfied.

We cannot use the normal approximation. Alternative methods (exact binomial confidence interval using the Clopper-Pearson method) should be used, which is beyond the scope of this lecture.

---

#### Example 4: Sample Size Determination

A political pollster wants to estimate the proportion of voters supporting a candidate with a margin of error of at most 3% (0.03) at 95% confidence.

(a) What sample size is needed assuming no prior information?
(b) What if a previous poll suggested `p* = 0.60`?

**Solution:**

(a) Conservative approach: `p* = 0.5`

`n = (1.96)^2 * 0.5 * 0.5 / (0.03)^2`

`= 3.8416 * 0.25 / 0.0009`

`= 0.9604 / 0.0009`

`= 1067.11`

Round up: `n = 1068`

(b) Using `p* = 0.60`:

`n = (1.96)^2 * 0.60 * 0.40 / (0.03)^2`

`= 3.8416 * 0.24 / 0.0009`

`= 0.921984 / 0.0009`

`= 1024.43`

Round up: `n = 1025`

The sample size needed is smaller when we have prior information.

---

#### Example 5: Effect of Desired Margin of Error

For 95% confidence with `p* = 0.5`, find the sample size needed for:
(a) `ME = 0.05` (5 percentage points)
(b) `ME = 0.03` (3 percentage points)
(c) `ME = 0.01` (1 percentage point)

**Solution:**

(a) `n = 3.8416 * 0.25 / 0.0025 = 0.9604 / 0.0025 = 384.16`. Round up: `n = 385`

(b) `n = 3.8416 * 0.25 / 0.0009 = 0.9604 / 0.0009 = 1067.11`. Round up: `n = 1068`

(c) `n = 3.8416 * 0.25 / 0.0001 = 0.9604 / 0.0001 = 9604`. `n = 9604`

**Observation:** Reducing the margin of error by half requires quadrupling the sample size (since `n` is inversely proportional to `ME^2`).

---

#### Example 6: Interpreting the Result

A newspaper reports: "Based on a survey of 1000 adults, 52% support the new law, with a margin of error of plus or minus 3.1 percentage points at the 95% confidence level."

Interpret this result.

**Solution:**

We are 95% confident that the true proportion of all adults who support the new law is between 48.9% and 55.1% (52% +/- 3.1%).

The reported margin of error is likely computed as:

`ME = 1.96 * sqrt{0.52 * 0.48 / 1000} = 1.96 * sqrt{0.2496 / 1000} = 1.96 * 0.0158 = 0.0310` = 3.1 percentage points.

---

### 7. Summary

| Concept | Formula | Notes |
|---------|---------|-------|
| Point estimate | `hat{p} = x / n` | Sample proportion |
| Standard error | `SE = sqrt(hat{p}(1-hat{p})/n)` | Estimated from data |
| CI for `p` | `hat{p} +/- z * sqrt(hat{p}(1-hat{p})/n)` | Requires `n*hat{p} >= 5`, `n*(1-hat{p}) >= 5` |
| Sample size (general) | `n = z^2 * p*(1-p*) / ME^2` | Use `p* = 0.5` if no prior info |
| Sample size (conservative) | `n = z^2 * 0.25 / ME^2` | Safe overestimate |

---

## Practice Problems

**Problem 1:** In a survey of 900 voters, 495 support a proposed tax reform. Construct a 90% confidence interval for the true proportion of supporters.

**Problem 2:** A manufacturer samples 250 items and finds 10 defective. Construct a 95% confidence interval for the proportion of defective items.

**Problem 3:** How large a sample is needed to estimate the proportion of left-handed people with a margin of error of 0.02 at 99% confidence? Assume no prior information.

**Problem 4:** A previous study found that 30% of patients experience side effects from a certain medication. A new study wants to estimate the current proportion with a margin of error of 0.04 at 95% confidence. What sample size is needed?

**Problem 5:** A candidate's campaign claims that 55% of voters support him. An independent poll of 400 voters finds that 48% support him. Construct a 95% confidence interval for the true proportion. Does the interval contradict the campaign's claim?

---

### Answers / Hints

**Problem 1:** `hat{p} = 495/900 = 0.55`. `z_{0.05} = 1.645`. `SE = sqrt(0.55*0.45/900) = 0.01658`. `ME = 1.645 * 0.01658 = 0.0273`. CI = `0.55 +/- 0.0273` = `(0.5227, 0.5773)`.

**Problem 2:** `hat{p} = 10/250 = 0.04`. Check: `250*0.04 = 10 >= 5`, `250*0.96 = 240 >= 5`. `z = 1.96`. `SE = sqrt(0.04*0.96/250) = 0.01239`. `ME = 1.96 * 0.01239 = 0.0243`. CI = `0.04 +/- 0.0243` = `(0.0157, 0.0643)`.

**Problem 3:** `z_{0.005} = 2.576`. `n = (2.576)^2 * 0.25 / (0.02)^2 = 6.636 * 0.25 / 0.0004 = 1.659 / 0.0004 = 4147.5`. Round up: `n = 4148`.

**Problem 4:** `p* = 0.30` (from previous study). `n = (1.96)^2 * 0.30 * 0.70 / (0.04)^2 = 3.8416 * 0.21 / 0.0016 = 0.8067 / 0.0016 = 504.2`. Round up: `n = 505`.

**Problem 5:** `hat{p} = 0.48`. `SE = sqrt(0.48*0.52/400) = 0.02498`. `ME = 1.96 * 0.02498 = 0.0490`. CI = `0.48 +/- 0.0490` = `(0.431, 0.529)`. The campaign claim of 0.55 is above the upper limit (0.529), so the interval suggests the campaign's claim may be inflated. The data contradicts the claim at the 95% confidence level.
