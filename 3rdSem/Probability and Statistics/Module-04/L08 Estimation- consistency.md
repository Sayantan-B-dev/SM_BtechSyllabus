# Estimation: consistency

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 8  
**Date:** 24-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.2.2

## Notes

### 1. Introduction to Consistency

Consistency is a **large-sample** property of estimators. While unbiasedness tells us about the average behavior for a fixed sample size, consistency tells us what happens as the sample size grows without bound.

**Intuition:** A consistent estimator gets better (more accurate) as we collect more data. Eventually, with enough data, the estimator will be arbitrarily close to the true parameter value.

---

### 2. Definition of Consistency

An estimator `hat{theta}_n` (where the subscript `n` emphasizes dependence on sample size) is said to be a **consistent estimator** of `theta` if it converges **in probability** to `theta` as `n -> infinity`.

Mathematically:

`hat{theta}_n -> theta` in probability as `n -> infinity`

This means: for any `epsilon > 0`,

`lim_{n -> infinity} P(|hat{theta}_n - theta| < epsilon) = 1`

Equivalently:

`lim_{n -> infinity} P(|hat{theta}_n - theta| >= epsilon) = 0`

**In words:** As the sample size increases, the probability that the estimator deviates from the true parameter by more than any small amount `epsilon` approaches zero.

---

### 3. Weak Law of Large Numbers (WLLN)

The Law of Large Numbers provides the theoretical foundation for consistency of the sample mean.

#### 3.1 Statement of WLLN

Let `X_1, X_2, ..., X_n` be i.i.d. random variables with mean `mu` and finite variance. Then the sample mean `bar{X}_n` converges in probability to `mu`:

`bar{X}_n -> mu` in probability as `n -> infinity`

#### 3.2 Proof Sketch (using Chebyshev's inequality)

Chebyshev's inequality: For any random variable `Y` with mean `mu_Y` and variance `sigma_Y^2`:

`P(|Y - mu_Y| >= epsilon) <= sigma_Y^2 / epsilon^2`

Apply this to `Y = bar{X}_n`:

`E[bar{X}_n] = mu`, `Var(bar{X}_n) = sigma^2 / n`

`P(|bar{X}_n - mu| >= epsilon) <= (sigma^2 / n) / epsilon^2 = sigma^2 / (n * epsilon^2)`

As `n -> infinity`, the right-hand side approaches 0. Therefore:

`lim_{n -> infinity} P(|bar{X}_n - mu| >= epsilon) = 0`

So `bar{X}_n` is consistent for `mu`.

---

### 4. Checking Consistency

There are several ways to verify that an estimator is consistent.

#### 4.1 Method 1: Using Bias and Variance

A sufficient condition for consistency is:

1. The bias tends to 0 as `n -> infinity` (asymptotically unbiased).
2. The variance tends to 0 as `n -> infinity`.

**Why this works:** Using the mean squared error decomposition:

`MSE(hat{theta}_n) = Var(hat{theta}_n) + [Bias(hat{theta}_n)]^2`

If both `Var -> 0` and `Bias -> 0`, then `MSE -> 0`. By Chebyshev's inequality, this implies consistency.

**Formal result:** If `lim_{n -> infinity} MSE(hat{theta}_n) = 0`, then `hat{theta}_n` is consistent for `theta`.

#### 4.2 Method 2: Direct Probability Argument

Show directly that `P(|hat{theta}_n - theta| > epsilon) -> 0` as `n -> infinity`.

#### 4.3 Method 3: Using Convergence in Distribution

If `hat{theta}_n -> theta` in distribution (to a degenerate distribution at `theta`), then it converges in probability as well.

---

### 5. Examples of Consistent Estimators

#### 5.1 Sample Mean

`bar{X}_n` is consistent for `mu` (proved above via WLLN).

#### 5.2 Sample Proportion

`hat{p}_n = X/n` is consistent for `p`.

**Proof:** `E[hat{p}_n] = p`, `Var(hat{p}_n) = p(1-p)/n -> 0` as `n -> infinity`. Both bias (0) and variance (->0) tend to 0, so `hat{p}_n` is consistent.

#### 5.3 Sample Variance (with n-1 denominator)

`s_n^2 = (1/(n-1)) * sum (X_i - bar{X})^2` is consistent for `sigma^2`.

**Proof:** We know `E[s_n^2] = sigma^2`. It can also be shown that `Var(s_n^2) -> 0` as `n -> infinity`. Therefore `s_n^2` is consistent.

#### 5.4 MLE of Normal Variance (with n denominator)

`hat{sigma}_n^2 = (1/n) * sum (X_i - bar{X})^2`

**Proof:** `E[hat{sigma}_n^2] = (n-1)/n * sigma^2`. Bias `= -sigma^2/n -> 0`. `Var(hat{sigma}_n^2) = (2*sigma^4*(n-1))/n^3 -> 0`. Both tend to 0, so `hat{sigma}_n^2` is consistent (even though it is biased for finite samples).

---

### 6. Consistent vs Inconsistent Estimators

| Estimator | Target | Consistent? | Reason |
|-----------|--------|-------------|--------|
| `bar{X}` | `mu` | Yes | WLLN |
| `hat{p} = X/n` | `p` | Yes | Variance -> 0, unbiased |
| `s^2` (n-1 denom) | `sigma^2` | Yes | Variance -> 0, unbiased |
| `hat{sigma}^2` (n denom) | `sigma^2` | Yes | Bias -> 0, variance -> 0 |
| `X_1` (single obs) | `mu` | No | Variance = `sigma^2` (constant, does not -> 0) |
| `(X_1 + X_n)/2` | `mu` | No | Variance does not -> 0 |

---

### 7. Worked Examples

#### Example 1: Checking Consistency of Sample Mean

Let `X_1, X_2, ..., X_n` be i.i.d. with mean `mu = 5` and variance `sigma^2 = 4`. Show that `bar{X}_n` is consistent for `mu` using Chebyshev's inequality.

**Solution:**

`P(|bar{X}_n - mu| >= epsilon) <= Var(bar{X}_n) / epsilon^2 = (sigma^2/n) / epsilon^2 = 4/(n * epsilon^2)`

For `epsilon = 0.1`:

`P(|bar{X}_n - 5| >= 0.1) <= 4 / (n * 0.01) = 400 / n`

When `n = 1000`: `P(|bar{X}_n - 5| >= 0.1) <= 0.4`

When `n = 4000`: `P(|bar{X}_n - 5| >= 0.1) <= 0.1`

When `n = 40000`: `P(|bar{X}_n - 5| >= 0.1) <= 0.01`

As `n -> infinity`, this probability approaches 0. Hence, `bar{X}_n` is consistent.

---

#### Example 2: Inconsistent Estimator

Consider the estimator `T_n = X_n` (the last observation in the sample) for `mu`. Is it consistent?

**Solution:**

`E[T_n] = mu` (unbiased).
`Var(T_n) = sigma^2` (constant, does not depend on `n`).

The variance does not tend to 0 as `n -> infinity`. Using Chebyshev:

`P(|T_n - mu| >= epsilon) <= sigma^2 / epsilon^2`

This bound does not approach 0 as `n -> infinity`. Therefore, `T_n` is **not** consistent. Adding more observations does not improve the estimator because we always use just the last observation.

---

#### Example 3: Showing Consistency of `s_n^2`

Let `X_1, ..., X_n` be i.i.d. `N(mu, sigma^2)`. Show that the MLE `hat{sigma}_n^2 = (1/n) * sum (X_i - bar{X})^2` is consistent for `sigma^2`.

**Solution:**

We know that for normal data:

`(n-1) * s^2 / sigma^2 ~ Chi-square(n-1)`

where `s^2` is the unbiased estimator.

Then: `hat{sigma}_n^2 = (n-1)/n * s^2`

`E[hat{sigma}_n^2] = (n-1)/n * sigma^2 -> sigma^2` as `n -> infinity`

`Var(hat{sigma}_n^2) = ((n-1)/n)^2 * Var(s^2)`

For normal data, `Var(s^2) = 2*sigma^4/(n-1)`, so:

`Var(hat{sigma}_n^2) = ((n-1)/n)^2 * 2*sigma^4/(n-1) = 2*sigma^4*(n-1)/n^3 -> 0` as `n -> infinity`.

Since bias -> 0 and variance -> 0, `hat{sigma}_n^2` is consistent.

---

#### Example 4: Showing Consistency of Sample Median

For a symmetric distribution, the sample median is a consistent estimator of the population median (which equals the mean for symmetric distributions).

**Intuition:** As `n` increases, the sample median converges to the population median. This is a general property of sample quantiles.

---

#### Example 5: Practical Implication

A quality control engineer wants to estimate the mean weight of cereal boxes. She can afford to sample either 10 boxes or 100 boxes.

- With `n = 10`: `SE = sigma / sqrt(10)`
- With `n = 100`: `SE = sigma / sqrt(100) = sigma / 10`

The standard error is 3.16 times smaller with `n = 100`. The estimator with `n = 100` is more likely to be close to the true mean, illustrating consistency in practice.

---

### 8. Relationship Between Consistency and Unbiasedness

| Property | Relationship |
|----------|--------------|
| **Unbiased does NOT imply consistent** | Example: `X_1` is unbiased for `mu` but not consistent (variance stays constant). |
| **Consistent does NOT imply unbiased** | Example: `hat{sigma}^2` (MLE with denominator `n`) is consistent but biased for finite `n`. |
| **Unbiased + Variance -> 0 implies consistent** | This is a sufficient condition. |
| **Asymptotically unbiased + Variance -> 0 implies consistent** | More general sufficient condition. |

---

### 9. Summary

- **Consistency**: As `n -> infinity`, `hat{theta}_n -> theta` in probability.
- **Sufficient condition**: `Bias(hat{theta}_n) -> 0` and `Var(hat{theta}_n) -> 0`.
- **WLLN**: `bar{X}_n` is consistent for `mu`.
- **Practical meaning**: Larger samples give more accurate estimates.
- **Key distinction**: Unbiasedness is a fixed-sample property; consistency is a large-sample property.

---

## Practice Problems

**Problem 1:** Let `X_1, X_2, ..., X_n` be i.i.d. with mean `mu` and variance `sigma^2`. Consider the estimator `T_n = (X_1 + X_2 + ... + X_k) / k` where `k` is a fixed number (does not grow with `n`). Is `T_n` consistent? Explain.

**Problem 2:** Let `X_1, X_2, ..., X_n` be i.i.d. `Bernoulli(p)`. Show that `hat{p}_n = bar{X}_n` is consistent for `p` using Chebyshev's inequality.

**Problem 3:** The sample median is a consistent estimator of the population median. True or False? Justify briefly.

**Problem 4:** A statistician proposes the estimator `T_n = bar{X}_n + 1/n` for the population mean `mu`. Is `T_n` consistent? Is it unbiased?

**Problem 5:** Explain the difference between unbiasedness and consistency. Can an estimator be unbiased but not consistent? Give an example.

---

### Answers / Hints

**Problem 1:** No, `T_n` is not consistent. It only uses the first `k` observations regardless of `n`. Its variance is `sigma^2/k`, which does not go to 0 as `n -> infinity`.

**Problem 2:** `E[hat{p}_n] = p`, `Var(hat{p}_n) = p(1-p)/n`. By Chebyshev: `P(|hat{p}_n - p| >= epsilon) <= p(1-p)/(n*epsilon^2) -> 0` as `n -> infinity`.

**Problem 3:** True. Sample quantiles (including the median) are consistent estimators of their population counterparts under mild regularity conditions.

**Problem 4:** `E[T_n] = mu + 1/n`, so bias = `1/n -> 0`. `Var(T_n) = sigma^2/n -> 0`. Since both bias and variance go to 0, `T_n` is consistent. It is biased for finite `n` but asymptotically unbiased.

**Problem 5:** Unbiasedness = `E[hat{theta}_n] = theta` for every `n`. Consistency = `hat{theta}_n -> theta` in probability as `n -> infinity`. Example of unbiased but not consistent: `T_n = X_1` (use only the first observation) is unbiased for `mu` but its variance is constant `sigma^2`, so it does not converge to `mu`.
