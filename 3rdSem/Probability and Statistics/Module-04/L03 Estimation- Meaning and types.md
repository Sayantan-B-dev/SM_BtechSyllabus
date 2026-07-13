# Estimation: Meaning and types

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 3  
**Date:** 10-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17

## Notes

### 1. Introduction to Estimation

In the previous lectures, we learned about sampling and sampling distributions. Now we use that knowledge to make educated guesses about population parameters based on sample data. This process is called **estimation**.

**Estimation** is the process of using sample data to estimate (or approximate) the value of an unknown population parameter.

**Why is estimation needed?**
- Population parameters (like `mu`, `p`, `sigma^2`) are usually unknown.
- It is impractical or impossible to measure the entire population.
- We use sample statistics to estimate these parameters.

---

### 2. Point Estimation vs Interval Estimation

There are two fundamentally different approaches to estimation.

#### 2.1 Point Estimation

A **point estimate** is a single numerical value that serves as a "best guess" for an unknown population parameter.

| Parameter | Point Estimator | Formula |
|-----------|----------------|---------|
| Population mean `mu` | Sample mean `bar{x}` | `bar{x} = (1/n) sum x_i` |
| Population variance `sigma^2` | Sample variance `s^2` | `s^2 = (1/(n-1)) sum (x_i - bar{x})^2` |
| Population proportion `p` | Sample proportion `hat{p}` | `hat{p} = x / n` |
| Population standard deviation `sigma` | Sample standard deviation `s` | `s = sqrt(s^2)` |

**Example:** If we want to estimate the average height of all students in a university, we might take a sample of 100 students and find their average height is 168 cm. Then `bar{x} = 168` cm is a point estimate of `mu`.

**Limitation of point estimation:** A single number gives no indication of how close the estimate is likely to be to the true parameter value. The probability that `bar{x}` exactly equals `mu` is essentially zero.

#### 2.2 Interval Estimation

An **interval estimate** provides a range of plausible values for the unknown parameter, along with a confidence level that indicates how plausible it is that the interval contains the true parameter.

**General form:**

`point estimate +/- margin of error`

**Example:** "We are 95% confident that the average height of all students is between 165.5 cm and 170.5 cm."

#### 2.3 Comparison: Point vs Interval Estimation

| Aspect | Point Estimation | Interval Estimation |
|--------|------------------|---------------------|
| Output | A single number | A range of numbers |
| Precision | Precise but uncertain | Less precise but more informative |
| Confidence | No measure of confidence | Includes confidence level |
| Margin of error | Not provided | Explicitly provided |
| Use when | A rough estimate is sufficient | A reliable estimate with known precision is needed |

---

### 3. Estimator vs Estimate

These two terms are closely related but distinct.

| Term | Definition | Notation | Example |
|------|------------|----------|---------|
| **Estimator** | A rule or formula for estimating a parameter; a random variable. | `hat{theta}` (as a function of `X_1,...,X_n`) | `bar{X} = (1/n) sum X_i` (before data is collected) |
| **Estimate** | The specific numerical value obtained from the data. | `hat{theta}` (the computed value) | `bar{x} = 168` cm (after collecting and computing) |

**Think of it this way:**
- The **estimator** is the formula or recipe.
- The **estimate** is what you get when you apply the recipe to actual data.

---

### 4. Desirable Properties of a Good Estimator

Not all estimators are created equal. We evaluate estimators based on several criteria.

#### 4.1 Unbiasedness

An estimator `hat{theta}` is **unbiased** if its expected value equals the true parameter value:

`E[hat{theta}] = theta`

**Intuition:** On average, over many samples, the estimator hits the true value. It does not systematically overestimate or underestimate.

**Examples:**
- `bar{X}` is an unbiased estimator of `mu` because `E[bar{X}] = mu`.
- `s^2 = (1/(n-1)) sum (X_i - bar{X})^2` is an unbiased estimator of `sigma^2`.
- `s^2_n = (1/n) sum (X_i - bar{X})^2` is a **biased** estimator of `sigma^2` (it systematically underestimates the variance).

#### 4.2 Consistency

An estimator `hat{theta}_n` (where `n` is the sample size) is **consistent** if it converges in probability to the true parameter as `n` approaches infinity:

`hat{theta}_n -> theta` in probability as `n -> infinity`

**Intuition:** As we collect more data, the estimator gets better and better, eventually converging to the true value.

**Check:** An estimator is consistent if:
- Its bias goes to 0 as `n -> infinity` (asymptotically unbiased).
- Its variance goes to 0 as `n -> infinity`.

**Examples:**
- `bar{X}` is a consistent estimator of `mu` because `Var(bar{X}) = sigma^2 / n -> 0` as `n -> infinity`, and it is unbiased.
- Sample median is also a consistent estimator of the population median.

#### 4.3 Efficiency

If two estimators `hat{theta}_1` and `hat{theta}_2` are both unbiased, we prefer the one with smaller variance. The estimator with smaller variance is said to be **more efficient**.

**Definition:** The **relative efficiency** of `hat{theta}_2` compared to `hat{theta}_1` is:

`Eff(hat{theta}_1, hat{theta}_2) = Var(hat{theta}_2) / Var(hat{theta}_1)`

If `Eff > 1`, then `hat{theta}_1` is more efficient.

**Most efficient estimator:** Among all unbiased estimators, the one with the smallest possible variance is called the **minimum variance unbiased estimator (MVUE)**.

**Example:** For normally distributed data, `bar{X}` is more efficient than the sample median for estimating `mu`. The variance of `bar{X}` is `sigma^2/n`, while the variance of the sample median is approximately `(pi/2) * (sigma^2/n) = 1.57 * sigma^2/n`. So `bar{X}` is about 1.57 times more efficient than the median.

#### 4.4 Sufficiency

An estimator (or statistic) is **sufficient** if it captures all the information in the sample about the parameter. No other statistic can provide any additional information about the parameter.

**Formal definition:** A statistic `T(X_1, ..., X_n)` is sufficient for `theta` if the conditional distribution of the sample given `T` does not depend on `theta`.

**Neyman-Fisher Factorization Theorem:** `T` is sufficient for `theta` if and only if the joint probability function can be factored as:

`f(x_1, ..., x_n; theta) = g(T(x_1, ..., x_n); theta) * h(x_1, ..., x_n)`

where `g` depends on `theta` and `T`, and `h` does not depend on `theta`.

**Examples:**
- `sum X_i` is sufficient for `p` in Bernoulli/Binomial distribution.
- `sum X_i` is sufficient for `lambda` in Poisson distribution.
- `(sum X_i, sum X_i^2)` is jointly sufficient for `(mu, sigma^2)` in Normal distribution.

---

### 5. Summary Table of Estimator Properties

| Property | Definition | Check | Example |
|----------|------------|-------|---------|
| Unbiasedness | `E[hat{theta}] = theta` | Compute expected value | `bar{X}` for `mu` |
| Consistency | `hat{theta}_n -> theta` in probability | Bias and variance go to 0 | `bar{X}` for `mu` |
| Efficiency | Minimum variance among unbiased estimators | Compare variances | `bar{X}` vs median for normal data |
| Sufficiency | Captures all information about parameter | Factorization theorem | `sum X_i` for Binomial `p` |

---

### 6. Worked Examples

#### Example 1: Identifying Point vs Interval Estimate

Identify each of the following as a point estimate or an interval estimate.

(a) "The average monthly rent for a 1-bedroom apartment in the city is $1,200."
    - **Answer:** Point estimate (single value).

(b) "We are 90% confident that the average monthly rent is between $1,150 and $1,250."
    - **Answer:** Interval estimate (range with confidence level).

(c) "Based on a sample of 500 voters, 54% support the candidate."
    - **Answer:** Point estimate (single proportion).

---

#### Example 2: Estimator vs Estimate

A random sample of 10 students yields the following test scores: 72, 85, 91, 68, 77, 83, 79, 74, 88, 93.

(a) What is the estimator for the population mean?
(b) What is the estimate?

**Solution:**

(a) The estimator is `bar{X} = (1/n) sum_{i=1}^{n} X_i`.

(b) `bar{x} = (72 + 85 + 91 + 68 + 77 + 83 + 79 + 74 + 88 + 93) / 10 = 810 / 10 = 81`.

So the estimate is 81.

---

#### Example 3: Comparing Two Estimators

Suppose we have two estimators for the population mean `mu`:

`hat{theta}_1 = bar{X}` (sample mean)
`hat{theta}_2 = (X_1 + X_n) / 2` (average of first and last observations)

Assume the population is normal with variance `sigma^2 = 25`.

(a) Are both estimators unbiased?
(b) Which is more efficient?

**Solution:**

(a) `E[hat{theta}_1] = E[bar{X}] = mu`. Unbiased.

`E[hat{theta}_2] = E[(X_1 + X_n) / 2] = (E[X_1] + E[X_n]) / 2 = (mu + mu) / 2 = mu`. Unbiased.

Both are unbiased.

(b) `Var(hat{theta}_1) = sigma^2 / n = 25 / n`.

`Var(hat{theta}_2) = Var((X_1 + X_n) / 2) = (Var(X_1) + Var(X_n)) / 4 = (25 + 25) / 4 = 12.5`.

For `n > 2`, `25/n < 12.5`. So `hat{theta}_1` has smaller variance (for `n >= 3`) and is more efficient.

---

## Practice Problems

**Problem 1:** Classify each as point estimate or interval estimate:
(a) "The proportion of defective items is 0.03."
(b) "The average weight of packages is between 495 g and 505 g with 99% confidence."
(c) "The sample mean is 62.4."

**Problem 2:** A statistician proposes using the sample median to estimate the population median. Is the sample median an estimator or an estimate? Explain.

**Problem 3:** For a population with mean `mu` and variance `sigma^2`, consider two estimators: `hat{theta}_1 = bar{X}` and `hat{theta}_2 = (X_1 + X_2 + X_3) / 3`. For a sample of size `n = 5`:
(a) Are both unbiased?
(b) Which has smaller variance?

**Problem 4:** Explain in one sentence each what it means for an estimator to be:
(a) Unbiased
(b) Consistent
(c) Efficient
(d) Sufficient

**Problem 5:** Is `bar{X}` always the best estimator for `mu`? What about when the data come from a distribution with very heavy tails (extreme outliers)?

---

### Answers / Hints

**Problem 1:** (a) Point estimate. (b) Interval estimate. (c) Point estimate.

**Problem 2:** Both. The formula "sample median" is the estimator (a rule). The specific value computed from data is the estimate.

**Problem 3:** (a) Yes, both are unbiased. `E[hat{theta}_1] = mu`, `E[hat{theta}_2] = (mu+mu+mu)/3 = mu`. (b) `Var(hat{theta}_1) = sigma^2/5`, `Var(hat{theta}_2) = sigma^2/3`. So `hat{theta}_1` has smaller variance.

**Problem 4:** (a) On average, the estimator equals the true value. (b) The estimator gets arbitrarily close to the true value as sample size grows. (c) Among unbiased estimators, it has the smallest variance. (d) It captures all information in the sample about the parameter.

**Problem 5:** No. For heavy-tailed distributions (e.g., Cauchy), the sample mean can be severely affected by outliers. The sample median may be a more robust and efficient estimator in such cases.
