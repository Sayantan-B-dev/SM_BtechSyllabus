# Sampling distributions

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 2  
**Date:** 08-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 15

## Notes

### 1. Introduction to Sampling Distributions

When we take a sample from a population and compute a statistic (like the sample mean `bar{x}` or sample proportion `hat{p}`), that statistic is a random variable. This is because different samples from the same population will yield different values of the statistic. The **sampling distribution** of a statistic is the probability distribution of that statistic over all possible samples of a given size drawn from the population.

**Key insight:** The sampling distribution is the bridge between the sample statistic and the population parameter. It tells us how much the statistic is likely to vary from sample to sample.

---

### 2. Sampling Distribution of the Sample Mean

#### 2.1 Setting Up

Let `X_1, X_2, ..., X_n` be a random sample of size `n` drawn from a population with mean `mu` and variance `sigma^2`.

The sample mean is:

`bar{X} = (1/n) * (X_1 + X_2 + ... + X_n) = (1/n) * sum_{i=1}^{n} X_i`

#### 2.2 Mean and Variance of the Sample Mean

**Mean of bar{X}:**

`E[bar{X}] = E[(1/n) sum X_i] = (1/n) * sum E[X_i] = (1/n) * (n * mu) = mu`

The expected value of the sample mean equals the population mean. This property is called **unbiasedness**.

**Variance of bar{X}:**

`Var(bar{X}) = Var((1/n) sum X_i) = (1/n^2) * sum Var(X_i) = (1/n^2) * (n * sigma^2) = sigma^2 / n`

The variance of the sample mean is the population variance divided by the sample size.

**Standard Error of the Mean (SEM):**

`SE(bar{X}) = sigma / sqrt(n)`

The standard error is the standard deviation of the sampling distribution of the sample mean. It quantifies how much the sample mean is expected to vary from sample to sample.

**Key observations:**
- As `n` increases, `SE(bar{X})` decreases. Larger samples give more precise estimates.
- If `sigma` is unknown, we estimate the standard error using `s / sqrt(n)`, where `s` is the sample standard deviation.

---

### 3. Central Limit Theorem (CLT)

The Central Limit Theorem is one of the most important theorems in statistics.

#### 3.1 Statement of the CLT

Let `X_1, X_2, ..., X_n` be a random sample of size `n` drawn from any population with mean `mu` and finite variance `sigma^2`. Then, for sufficiently large `n`, the sampling distribution of the sample mean `bar{X}` is approximately **normal** with mean `mu` and variance `sigma^2 / n`.

In mathematical notation:

`bar{X} ~ approx N(mu, sigma^2 / n)` for large `n`

Equivalently, the standardized version follows a standard normal distribution:

`Z = (bar{X} - mu) / (sigma / sqrt(n)) ~ approx N(0, 1)` for large `n`

#### 3.2 Implications of the CLT

| Implication | Explanation |
|-------------|-------------|
| Normality | Regardless of the shape of the population distribution, the sampling distribution of `bar{X}` becomes approximately normal as `n` increases. |
| Sample size requirement | The CLT works well even for `n >= 30` for most populations. For highly skewed distributions, larger `n` may be needed. For normal populations, the sampling distribution is exactly normal for any `n`. |
| Statistical inference | The CLT justifies the use of normal distribution theory for confidence intervals and hypothesis tests about the mean. |
| Practical importance | Most real-world statistical procedures rely on the CLT. |

#### 3.3 Visual Intuition

- If the population is normally distributed: `bar{X}` is exactly normally distributed for any `n`.
- If the population is symmetric and unimodal: `bar{X}` is approximately normal even for small `n` (e.g., `n = 5` or `10`).
- If the population is highly skewed: `bar{X}` becomes approximately normal for `n >= 30` (sometimes larger).

---

### 4. Sampling Distribution of the Sample Proportion

#### 4.1 Setting Up

Consider a population where a proportion `p` of individuals have a certain characteristic (e.g., prefer a particular brand, have a disease, etc.). Let `X` be the number of successes (individuals with the characteristic) in a random sample of size `n`.

Then:

`X ~ Binomial(n, p)`

The sample proportion is:

`hat{p} = X / n`

#### 4.2 Mean and Variance of the Sample Proportion

**Mean of hat{p}:**

`E[hat{p}] = E[X/n] = (1/n) * E[X] = (1/n) * (n * p) = p`

**Variance of hat{p}:**

`Var(hat{p}) = Var(X/n) = (1/n^2) * Var(X) = (1/n^2) * (n * p * (1-p)) = p(1-p) / n`

**Standard Error of the Proportion:**

`SE(hat{p}) = sqrt(p(1-p) / n)`

#### 4.3 CLT for the Sample Proportion

By the CLT, for large `n`, the sampling distribution of `hat{p}` is approximately normal:

`hat{p} ~ approx N(p, p(1-p) / n)`

The standardized version:

`Z = (hat{p} - p) / sqrt(p(1-p) / n) ~ approx N(0, 1)`

**Conditions for normality:**
- `n * p >= 5` and `n * (1-p) >= 5`

These conditions ensure that the binomial distribution is sufficiently symmetric for the normal approximation to be valid.

---

### 5. Worked Examples

#### Example 1: Basic CLT Application for Mean

A population has mean `mu = 100` and standard deviation `sigma = 15`. A sample of size `n = 36` is taken.

(a) What is the mean and standard error of `bar{X}`?
(b) What is the probability that the sample mean exceeds 105?

**Solution:**

(a) `E[bar{X}] = mu = 100`
    `SE(bar{X}) = sigma / sqrt(n) = 15 / sqrt(36) = 15 / 6 = 2.5`

(b) We want `P(bar{X} > 105)`.

Standardize: `Z = (bar{X} - mu) / (sigma / sqrt(n)) = (105 - 100) / 2.5 = 5 / 2.5 = 2`

`P(bar{X} > 105) = P(Z > 2) = 1 - P(Z <= 2) = 1 - 0.9772 = 0.0228`

So there is about a 2.28% chance that the sample mean exceeds 105.

---

#### Example 2: CLT for Proportion

According to a report, 60% of adults in a city support a new policy. If we survey 200 randomly selected adults:

(a) What is the mean and standard error of the sample proportion?
(b) What is the probability that more than 65% of the sample support the policy?

**Solution:**

`p = 0.60`, `n = 200`

(a) `E[hat{p}] = p = 0.60`
    `SE(hat{p}) = sqrt(p(1-p) / n) = sqrt(0.60 * 0.40 / 200) = sqrt(0.24 / 200) = sqrt(0.0012) = 0.03464`

(b) Check conditions: `n * p = 200 * 0.60 = 120 >= 5`, `n * (1-p) = 200 * 0.40 = 80 >= 5`. Both satisfied, so normal approximation is valid.

`P(hat{p} > 0.65)`

Standardize: `Z = (0.65 - 0.60) / 0.03464 = 0.05 / 0.03464 = 1.44`

`P(hat{p} > 0.65) = P(Z > 1.44) = 1 - P(Z <= 1.44) = 1 - 0.9251 = 0.0749`

So there is about a 7.49% chance that more than 65% of the sample supports the policy.

---

#### Example 3: Effect of Sample Size on Standard Error

Compare the standard error of the sample mean for `n = 16` vs `n = 100` when `sigma = 20`.

**Solution:**

For `n = 16`: `SE = 20 / sqrt(16) = 20 / 4 = 5`

For `n = 100`: `SE = 20 / sqrt(100) = 20 / 10 = 2`

Increasing the sample size from 16 to 100 (a factor of 6.25) reduces the standard error from 5 to 2 (a factor of 2.5). The standard error decreases by a factor of `sqrt(n)`, so to halve the standard error, we need to quadruple the sample size.

---

#### Example 4: Non-Normal Population

The time spent by customers in a grocery store follows a right-skewed distribution with mean `mu = 25` minutes and standard deviation `sigma = 12` minutes. If we randomly sample 40 customers:

(a) Can we use the CLT? Why?
(b) What is the approximate distribution of `bar{X}`?
(c) Find the probability that the average shopping time exceeds 28 minutes.

**Solution:**

(a) Yes, because `n = 40 >= 30`. The CLT applies regardless of the population shape for sufficiently large `n`.

(b) `bar{X} ~ approx N(25, 12^2 / 40) = N(25, 3.6)`
    Standard error `= 12 / sqrt(40) = 12 / 6.3249 = 1.897`

(c) `Z = (28 - 25) / 1.897 = 3 / 1.897 = 1.58`

`P(bar{X} > 28) = P(Z > 1.58) = 1 - 0.9429 = 0.0571`

About 5.71% chance.

---

### 6. Summary Table

| Concept | Sample Mean `bar{X}` | Sample Proportion `hat{p}` |
|---------|---------------------|----------------------------|
| Mean of sampling distribution | `mu` | `p` |
| Variance of sampling distribution | `sigma^2 / n` | `p(1-p) / n` |
| Standard error | `sigma / sqrt(n)` | `sqrt(p(1-p) / n)` |
| Distribution (large n) | Approximately Normal | Approximately Normal |
| Condition for CLT | `n >= 30` (or population normal) | `n*p >= 5` and `n*(1-p) >= 5` |

---

## Practice Problems

**Problem 1:** A population has mean 50 and standard deviation 8. A random sample of size 64 is taken. What is the probability that the sample mean is between 48 and 52?

   <details>
   <summary>Show Answer</summary>
   **Problem 1:** `SE = 8/8 = 1`. `Z_1 = (48-50)/1 = -2`, `Z_2 = (52-50)/1 = 2`. `P(-2 < Z < 2) = 0.9772 - 0.0228 = 0.9544`.
   </details>

**Problem 2:** A manufacturer claims that 90% of his products are non-defective. You randomly select 400 products. What is the probability that the sample proportion of non-defective products is less than 87%?

   <details>
   <summary>Show Answer</summary>
   **Problem 2:** `p = 0.90`, `SE = sqrt(0.9*0.1/400) = 0.015`. `Z = (0.87 - 0.90)/0.015 = -2`. `P(hat{p} < 0.87) = P(Z < -2) = 0.0228`.
   </details>

**Problem 3:** The average monthly electricity bill in a city is $120 with a standard deviation of $30. A sample of 36 households is selected. What is the probability that the average bill exceeds $130?

   <details>
   <summary>Show Answer</summary>
   **Problem 3:** `SE = 30/6 = 5`. `Z = (130-120)/5 = 2`. `P(Z > 2) = 0.0228`.
   </details>

**Problem 4:** Explain what happens to the standard error of the sample mean when: (a) the sample size is quadrupled, (b) the population standard deviation is doubled.

   <details>
   <summary>Show Answer</summary>
   **Problem 4:** (a) `SE` becomes half (`SE_new = sigma / sqrt(4n) = sigma / (2*sqrt(n)) = SE_old / 2`). (b) `SE` doubles (`SE_new = (2sigma)/sqrt(n) = 2*(sigma/sqrt(n)) = 2*SE_old`).
   </details>

**Problem 5:** A population is heavily skewed to the right. Can you still use the normal distribution to approximate the sampling distribution of the sample mean? If yes, what is the minimum sample size required?
   <details>
   <summary>Show Answer</summary>
   **Problem 5:** Yes, the CLT applies. For skewed populations, a minimum sample size of `n >= 30` is generally recommended; for heavily skewed populations, `n >= 50` may be safer.
   </details>
