# Estimation: Unbiasedness

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 6  
**Date:** 17-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Interactive Learning  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.2.1

## Notes

### 1. Definition of Unbiasedness

An estimator `hat{theta}` is said to be an **unbiased estimator** of a parameter `theta` if:

`E[hat{theta}] = theta`

for all possible values of `theta` in the parameter space.

**In words:** The expected value of the estimator equals the true parameter value. Over many repeated samples, the estimator neither systematically overestimates nor underestimates the parameter.

---

### 2. Bias of an Estimator

The **bias** of an estimator `hat{theta}` for `theta` is defined as:

`Bias(hat{theta}) = E[hat{theta}] - theta`

- If `Bias = 0`, the estimator is unbiased.
- If `Bias > 0`, the estimator systematically **overestimates** the parameter.
- If `Bias < 0`, the estimator systematically **underestimates** the parameter.

#### Types of Estimators Based on Bias

| Type | Definition | Example |
|------|------------|---------|
| **Unbiased** | `E[hat{theta}] = theta` | `bar{X}` for `mu` |
| **Positively biased** | `E[hat{theta}] > theta` | Some estimators of `sigma^2` |
| **Negatively biased** | `E[hat{theta}] < theta` | MLE of `sigma^2` (with denominator `n`) |
| **Asymptotically unbiased** | `lim_{n->inf} E[hat{theta}_n] = theta` | Many consistent estimators |

---

### 3. Showing that Sample Mean is Unbiased for Population Mean

Let `X_1, X_2, ..., X_n` be a random sample from a population with mean `mu` (and any finite variance). The sample mean is:

`bar{X} = (1/n) * sum_{i=1}^{n} X_i`

**Proof of unbiasedness:**

`E[bar{X}] = E[(1/n) * sum_{i=1}^{n} X_i]`

By linearity of expectation:

`E[bar{X}] = (1/n) * sum_{i=1}^{n} E[X_i]`

Since each `X_i` is drawn from the same population, `E[X_i] = mu` for all `i`:

`E[bar{X}] = (1/n) * (n * mu) = mu`

Therefore, `E[bar{X}] = mu`, so `bar{X}` is an **unbiased estimator** of `mu`.

**Key insight:** This holds regardless of the population distribution (normal, skewed, discrete, continuous) and regardless of sample size. It only requires that `E[X_i] = mu`.

---

### 4. Sample Variance: Biased vs Unbiased

There are two commonly used formulas for sample variance:

**Version 1 (MLE, denominator n):**

`s_n^2 = (1/n) * sum_{i=1}^{n} (X_i - bar{X})^2`

**Version 2 (Unbiased, denominator n-1):**

`s^2 = (1/(n-1)) * sum_{i=1}^{n} (X_i - bar{X})^2`

#### 4.1 Proving `s_n^2` is Biased

We need to find `E[s_n^2]`.

First, note that:

`sum (X_i - bar{X})^2 = sum X_i^2 - n * bar{X}^2`

So:

`s_n^2 = (1/n) * sum X_i^2 - bar{X}^2`

Taking expectation:

`E[s_n^2] = (1/n) * sum E[X_i^2] - E[bar{X}^2]`

We know:

`E[X_i^2] = Var(X_i) + [E(X_i)]^2 = sigma^2 + mu^2`

`E[bar{X}^2] = Var(bar{X}) + [E(bar{X})]^2 = sigma^2/n + mu^2`

Therefore:

`E[s_n^2] = (1/n) * n * (sigma^2 + mu^2) - (sigma^2/n + mu^2)`

`E[s_n^2] = sigma^2 + mu^2 - sigma^2/n - mu^2`

`E[s_n^2] = sigma^2 - sigma^2/n = sigma^2 * (n-1)/n`

**Bias of `s_n^2`:** `E[s_n^2] - sigma^2 = sigma^2 * (n-1)/n - sigma^2 = -sigma^2/n`

Since `-sigma^2/n < 0`, `s_n^2` is a **negatively biased estimator** of `sigma^2` (it systematically underestimates the population variance).

#### 4.2 Proving `s^2` is Unbiased

`s^2 = (1/(n-1)) * sum (X_i - bar{X})^2 = (n/(n-1)) * s_n^2`

Taking expectation:

`E[s^2] = (n/(n-1)) * E[s_n^2] = (n/(n-1)) * sigma^2 * (n-1)/n = sigma^2`

Thus, `E[s^2] = sigma^2`, so `s^2` is an **unbiased estimator** of `sigma^2`.

**Why `n-1`?** When we compute deviations from `bar{X}` (not from `mu`), we lose one degree of freedom because `sum (X_i - bar{X}) = 0`. This imposes a linear constraint on the deviations. Hence we divide by `n-1`.

---

### 5. Biased vs Unbiased Estimators: Comparison

| Aspect | Biased Estimator | Unbiased Estimator |
|--------|-----------------|-------------------|
| **Expected value** | `E[hat{theta}] != theta` | `E[hat{theta}] = theta` |
| **Example** | `s_n^2` for `sigma^2` | `s^2` for `sigma^2` |
| **Systematic error** | Yes (over or under) | No (centered at truth) |
| **May have lower MSE** | Yes (if bias reduces variance) | Not guaranteed to have low MSE |
| **Large sample behavior** | May be asymptotically unbiased | Already unbiased |

**Important nuance:** Unbiasedness alone is not sufficient to declare an estimator "good." An unbiased estimator with very large variance may be worse than a slightly biased estimator with very small variance.

---

### 6. Mean Squared Error (MSE)

The **mean squared error** of an estimator measures the average squared distance from the true parameter:

`MSE(hat{theta}) = E[(hat{theta} - theta)^2]`

It can be decomposed into:

`MSE(hat{theta}) = Var(hat{theta}) + [Bias(hat{theta})]^2`

| If... | Then MSE is due to... |
|-------|----------------------|
| Estimator is unbiased | `MSE = Var(hat{theta})` |
| Estimator is biased | `MSE = Var(hat{theta}) + Bias^2` |

**Example:** For the normal variance estimators:

For `s_n^2`: `E[s_n^2] = sigma^2 * (n-1)/n`, `Bias(s_n^2) = -sigma^2/n`

For `s^2`: `E[s^2] = sigma^2`, `Bias(s^2) = 0`

---

### 7. Worked Examples

#### Example 1: Determining if an Estimator is Unbiased

Suppose we estimate the population mean `mu` using a single observation: `hat{mu} = X_1`. Is this unbiased?

**Solution:**

`E[hat{mu}] = E[X_1] = mu`

Yes, `hat{mu} = X_1` is unbiased. However, it has high variance (`Var(X_1) = sigma^2`), so it is not a good estimator despite being unbiased.

---

#### Example 2: A Biased Estimator

Consider the estimator `hat{mu} = (X_1 + X_2) / 2` where `X_1, X_2` are from a population with mean `mu`. Is this unbiased? What about `hat{mu} = (X_1 + X_2 + X_3) / 4`?

**Solution:**

For `hat{mu} = (X_1 + X_2) / 2`:
`E[hat{mu}] = (E[X_1] + E[X_2]) / 2 = (mu + mu) / 2 = mu`. Unbiased.

For `hat{mu} = (X_1 + X_2 + X_3) / 4`:
`E[hat{mu}] = (E[X_1] + E[X_2] + E[X_3]) / 4 = 3*mu / 4 = 0.75*mu`

Since `0.75*mu != mu` (unless `mu = 0`), this estimator is **biased**. It systematically underestimates `mu` by 25%.

---

#### Example 3: Checking Unbiasedness of a Proportion Estimator

A survey of 50 people finds that 30 support a policy. Is `hat{p} = X/n` an unbiased estimator of the true proportion `p`?

**Solution:**

For Bernoulli trials: `E[X] = n * p`

`E[hat{p}] = E[X/n] = (1/n) * E[X] = (1/n) * n * p = p`

Yes, `hat{p}` is unbiased.

---

#### Example 4: Bias of the MLE for Normal Variance

A sample of size `n = 10` from `N(mu, sigma^2)` gives `sum (x_i - bar{x})^2 = 72`. Compare `s_n^2` and `s^2`.

**Solution:**

`s_n^2 = 72 / 10 = 7.2` (biased, underestimates on average)

`s^2 = 72 / 9 = 8.0` (unbiased)

The bias of `s_n^2` is `-sigma^2 / 10`. Since `sigma^2` is unknown, we estimate the bias as `-7.2 / 10 = -0.72`.

---

#### Example 5: Proving Unbiasedness

Let `X_1, X_2, ..., X_n` be a random sample from a distribution with mean `mu`. Show that the linear combination `T = sum_{i=1}^{n} a_i * X_i` is an unbiased estimator of `mu` if and only if `sum a_i = 1`.

**Solution:**

`E[T] = E[sum a_i X_i] = sum a_i * E[X_i] = sum a_i * mu = mu * sum a_i`

For `E[T] = mu`, we need `mu * sum a_i = mu`, which requires `sum a_i = 1`.

Therefore, any weighted average of the observations with weights summing to 1 is an unbiased estimator of the population mean.

---

### 8. Summary Table

| Estimator | Target | Expected Value | Bias | Unbiased? |
|-----------|--------|---------------|------|-----------|
| `bar{X}` | `mu` | `mu` | 0 | Yes |
| `s_n^2 = (1/n) sum (X_i - bar{X})^2` | `sigma^2` | `(n-1)/n * sigma^2` | `-sigma^2/n` | No (negatively biased) |
| `s^2 = (1/(n-1)) sum (X_i - bar{X})^2` | `sigma^2` | `sigma^2` | 0 | Yes |
| `hat{p} = X/n` | `p` | `p` | 0 | Yes |
| `hat{mu} = X_1` (single obs) | `mu` | `mu` | 0 | Yes (but high variance) |

---

## Practice Problems

**Problem 1:** Let `X_1, X_2, ..., X_n` be a random sample from a population with mean `mu`. Consider the estimator `T = (X_1 + X_n) / 2`. Is `T` unbiased for `mu`?

   <details>
   <summary>Show Answer</summary>
   **Problem 1:** `E[T] = (E[X_1] + E[X_n])/2 = (mu + mu)/2 = mu`. Yes, `T` is unbiased.
   </details>

**Problem 2:** The MLE of `sigma^2` for a normal distribution is `hat{sigma}^2 = (1/n) sum (X_i - bar{X})^2`. What is the bias of this estimator? What happens to the bias as `n -> infinity`?

   <details>
   <summary>Show Answer</summary>
   **Problem 2:** `Bias(hat{sigma}^2) = -sigma^2/n`. As `n -> infinity`, the bias goes to 0, so the estimator is asymptotically unbiased.
   </details>

**Problem 3:** A sample of size `n = 25` from a normal distribution yields `sum (x_i - bar{x})^2 = 240`. Compute both `s_n^2` and `s^2`. Which one is unbiased?

   <details>
   <summary>Show Answer</summary>
   **Problem 3:** `s_n^2 = 240/25 = 9.6`, `s^2 = 240/24 = 10`. `s^2` is unbiased.
   </details>

**Problem 4:** You have two estimators for `mu`: `hat{mu}_1 = bar{X}` and `hat{mu}_2 = (X_1 + X_2 + ... + X_n) / (n+1)`. Which is biased? Compute the bias of the biased estimator.

   <details>
   <summary>Show Answer</summary>
   **Problem 4:** `hat{mu}_2` is biased. `E[hat{mu}_2] = n*mu/(n+1)`. `Bias = n*mu/(n+1) - mu = -mu/(n+1)`.
   </details>

**Problem 5:** Prove that the sample proportion `hat{p} = X/n` from a binomial experiment is an unbiased estimator of `p`.
   <details>
   <summary>Show Answer</summary>
   **Problem 5:** `E[hat{p}] = E[X/n] = (1/n) * E[X] = (1/n) * (n*p) = p`. Therefore `hat{p}` is unbiased.
   </details>
