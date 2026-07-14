# Estimation: Method of moment estimators

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 5  
**Date:** 15-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.6.3

## Notes

### 1. Introduction to Method of Moments

The **Method of Moments (MOM)** is one of the oldest and most intuitive methods for estimating parameters. The principle is simple: equate sample moments to population moments and solve for the parameters.

**The basic idea:** If a distribution has `k` unknown parameters, we equate the first `k` sample moments to the corresponding population moments and solve the resulting system of equations.

---

### 2. Definition of Moments

#### 2.1 Population Moments

The `r`-th **population moment** about the origin (raw moment) is:

`mu'_r = E[X^r]`

For example:
- `mu'_1 = E[X]` (the population mean)
- `mu'_2 = E[X^2]`
- `mu'_3 = E[X^3]`

The `r`-th **population central moment** is:

`mu_r = E[(X - mu)^r]`

For example:
- `mu_2 = E[(X - mu)^2] = sigma^2` (the population variance)
- `mu_3 = E[(X - mu)^3]` (skewness)

#### 2.2 Sample Moments

The `r`-th **sample moment** about the origin is:

`m'_r = (1/n) * sum_{i=1}^{n} X_i^r`

For example:
- `m'_1 = bar{X}` (sample mean)
- `m'_2 = (1/n) * sum X_i^2`

#### 2.3 The Method of Moments Principle

Set: `m'_r = mu'_r` for `r = 1, 2, ..., k`

...and solve for the `k` unknown parameters.

---

### 3. MOM for Binomial Parameter `p`

#### 3.1 Setup

`X_1, X_2, ..., X_n` i.i.d. `Bernoulli(p)` (or equivalently, `sum X_i ~ Binomial(n, p)`).

#### 3.2 Population Moment

For Bernoulli distribution:

`mu'_1 = E[X] = p`

#### 3.3 Sample Moment

`m'_1 = (1/n) * sum X_i = bar{X}`

#### 3.4 Equating

Set `bar{X} = p`

**MOM estimator of `p`:** `tilde{p} = bar{X}`

**Note:** For the Bernoulli/Binomial distribution, the MOM estimator is the same as the MLE estimator. This is not always the case.

---

### 4. MOM for Poisson Parameter `lambda`

#### 4.1 Setup

`X_1, X_2, ..., X_n` i.i.d. `Poisson(lambda)`.

#### 4.2 Population Moment

For Poisson distribution:

`mu'_1 = E[X] = lambda`

#### 4.3 Sample Moment

`m'_1 = bar{X}`

#### 4.4 Equating

Set `bar{X} = lambda`

**MOM estimator of `lambda`:** `tilde{lambda} = bar{X}`

Again, this matches the MLE for this distribution.

---

### 5. MOM for Normal Parameters `mu` and `sigma^2`

#### 5.1 Setup

`X_1, X_2, ..., X_n` i.i.d. `N(mu, sigma^2)`.

We need two equations because there are two parameters.

#### 5.2 Population Moments

First population moment: `mu'_1 = E[X] = mu`

Second population moment: `mu'_2 = E[X^2] = Var(X) + [E(X)]^2 = sigma^2 + mu^2`

#### 5.3 Sample Moments

`m'_1 = bar{X}`

`m'_2 = (1/n) * sum X_i^2`

#### 5.4 Equating

Equation 1: `bar{X} = mu`

Equation 2: `(1/n) * sum X_i^2 = sigma^2 + mu^2`

#### 5.5 Solving

From equation 1: `tilde{mu} = bar{X}`

Substitute into equation 2:

`(1/n) * sum X_i^2 = sigma^2 + bar{X}^2`

`tilde{sigma}^2 = (1/n) * sum X_i^2 - bar{X}^2`

Recall that `(1/n) * sum (X_i - bar{X})^2 = (1/n) * sum X_i^2 - bar{X}^2`

Therefore: `tilde{sigma}^2 = (1/n) * sum (X_i - bar{X})^2`

**MOM estimators:** `tilde{mu} = bar{X}` and `tilde{sigma}^2 = (1/n) * sum (X_i - bar{X})^2`

**Note:** Again, the MOM estimator matches the MLE for the normal distribution.

---

### 6. MOM for Gamma Distribution

To illustrate a case where MOM differs from MLE, consider the Gamma distribution.

#### 6.1 Setup

`X_1, X_2, ..., X_n` i.i.d. `Gamma(alpha, beta)` where `alpha` is the shape parameter and `beta` is the rate parameter.

**PDF:** `f(x; alpha, beta) = (beta^alpha / Gamma(alpha)) * x^{alpha-1} * e^{-beta*x}` for `x > 0`

**Properties:** `E[X] = alpha / beta`, `Var(X) = alpha / beta^2`

#### 6.2 Population Moments

`mu'_1 = E[X] = alpha / beta`

`mu'_2 = E[X^2] = Var(X) + [E(X)]^2 = alpha/beta^2 + (alpha/beta)^2`

#### 6.3 Sample Moments

`m'_1 = bar{X}`

`m'_2 = (1/n) * sum X_i^2`

#### 6.4 Equating and Solving

Equation 1: `bar{X} = alpha / beta`

Equation 2: `(1/n) * sum X_i^2 = alpha/beta^2 + (alpha/beta)^2 = alpha/beta^2 + bar{X}^2`

From equation 2:

`(1/n) * sum X_i^2 - bar{X}^2 = alpha/beta^2`

The left side is the sample variance (with denominator `n`): `tilde{sigma}^2 = (1/n) * sum (X_i - bar{X})^2`

So: `alpha/beta^2 = tilde{sigma}^2`

From equation 1: `alpha = beta * bar{X}`

Substitute:

`(beta * bar{X}) / beta^2 = bar{X} / beta = tilde{sigma}^2`

`tilde{beta} = bar{X} / tilde{sigma}^2`

And: `tilde{alpha} = tilde{beta} * bar{X} = bar{X}^2 / tilde{sigma}^2`

**MOM estimators:** `tilde{alpha} = bar{X}^2 / tilde{sigma}^2` and `tilde{beta} = bar{X} / tilde{sigma}^2`

**Note:** These MOM estimators are not the same as the MLE (which requires numerical methods for the Gamma distribution).

---

### 7. Comparison: MLE vs MOM

| Aspect | MLE | MOM |
|--------|-----|-----|
| **Principle** | Maximizes the likelihood function | Equates sample and population moments |
| **Ease of computation** | May require numerical optimization | Usually easy to compute (closed form) |
| **Efficiency** | Generally efficient (asymptotically minimum variance) | May be less efficient than MLE |
| **Invariance property** | Yes (MLE of `g(theta) = g(MLE(theta))`) | No |
| **Consistency** | Yes (under regularity conditions) | Yes |
| **Unbiasedness** | Not guaranteed (e.g., MLE of `sigma^2` is biased) | Not guaranteed |
| **Initial estimates** | Can be sensitive to starting values | Often used to get starting values for MLE |
| **Small sample properties** | Often optimal | May be poor |

#### When MLE and MOM agree:
- Bernoulli/Binomial `p`: `bar{X}`
- Poisson `lambda`: `bar{X}`
- Normal `mu`: `bar{X}`
- Normal `sigma^2`: `(1/n) * sum (X_i - bar{X})^2`

#### When they typically differ:
- Gamma distribution
- Weibull distribution
- Beta distribution
- Many other distributions with complex parameter structures

---

### 8. Worked Examples

#### Example 1: MOM for Binomial

A coin is tossed 100 times and lands heads 62 times. Find the MOM estimate of `p`.

**Solution:**

`tilde{p} = bar{X} = 62/100 = 0.62`

---

#### Example 2: MOM for Normal

A random sample of 5 measurements from a normal distribution yields: 10.2, 9.8, 10.5, 10.0, 9.5. Find the MOM estimates of `mu` and `sigma^2`.

**Solution:**

`tilde{mu} = bar{x} = (10.2 + 9.8 + 10.5 + 10.0 + 9.5) / 5 = 50.0 / 5 = 10.0`

`tilde{sigma}^2 = (1/5) * sum (x_i - 10.0)^2 = (1/5) * 0.58 = 0.116`

---

#### Example 3: MOM for Gamma

A sample of size 20 from a Gamma distribution yields `sum x_i = 40` and `sum x_i^2 = 110`. Find the MOM estimates of `alpha` and `beta`.

**Solution:**

`bar{x} = 40 / 20 = 2`

`(1/n) * sum x_i^2 = 110 / 20 = 5.5`

`tilde{sigma}^2 = (1/n) * sum x_i^2 - bar{x}^2 = 5.5 - 4 = 1.5`

`tilde{beta} = bar{x} / tilde{sigma}^2 = 2 / 1.5 = 4/3 = 1.333`

`tilde{alpha} = bar{x}^2 / tilde{sigma}^2 = 4 / 1.5 = 8/3 = 2.667`

So `tilde{alpha} = 2.667` and `tilde{beta} = 1.333`.

---

#### Example 4: MOM Using Higher Moments

Suppose a distribution has only one parameter `theta`, but `E[X] = 0` for all `theta`. The first moment provides no information. Explain how you would use MOM.

**Solution:**

When the first moment does not depend on the parameter, we use the second (or higher) moment.

For example, if `X ~ N(0, sigma^2)`, then `E[X] = 0` gives no information about `sigma^2`. We equate the second moments:

`mu'_2 = E[X^2] = sigma^2`

`m'_2 = (1/n) * sum X_i^2`

So: `tilde{sigma}^2 = (1/n) * sum X_i^2`

---

### 9. Procedure Summary

**Step-by-step MOM method:**

1. Identify the number of parameters `k`.
2. Compute population moments `mu'_r = E[X^r]` for `r = 1, 2, ..., k` in terms of the parameters.
3. Compute sample moments `m'_r = (1/n) sum X_i^r`.
4. Set `mu'_r = m'_r` for each `r = 1, ..., k`.
5. Solve the system of equations for the parameters.

---

## Practice Problems

**Problem 1:** A random sample of 8 observations from a Poisson distribution gives: 2, 4, 1, 3, 5, 2, 3, 4. Find the MOM estimate of `lambda`.

   <details>
   <summary>Show Answer</summary>
   **Problem 1:** `tilde{lambda} = bar{x} = (2+4+1+3+5+2+3+4)/8 = 24/8 = 3`.
   </details>

**Problem 2:** A sample of size `n` from a distribution with mean `mu` and variance `sigma^2` yields `bar{x} = 50` and sample variance (with denominator `n`) `tilde{sigma}^2 = 16`. What are the MOM estimates of `mu` and `sigma^2`?

   <details>
   <summary>Show Answer</summary>
   **Problem 2:** `tilde{mu} = 50`, `tilde{sigma}^2 = 16`.
   </details>

**Problem 3:** For the Uniform distribution `U(0, theta)`, we have `E[X] = theta/2`. Find the MOM estimator of `theta`.

   <details>
   <summary>Show Answer</summary>
   **Problem 3:** Set `bar{X} = theta/2`, so `tilde{theta} = 2 * bar{X}`.
   </details>

**Problem 4:** Compare MLE and MOM. Give one advantage of each method.

   <details>
   <summary>Show Answer</summary>
   **Problem 4:** Advantage of MLE: Asymptotically efficient (smallest possible variance among consistent estimators). Advantage of MOM: Simpler to compute, often gives closed-form solutions.
   </details>

**Problem 5:** A sample from an exponential distribution (`f(x; lambda) = lambda * e^{-lambda*x}` for `x >= 0`) has mean `E[X] = 1/lambda`. A sample of size 10 gives `sum x_i = 25`. Find the MOM estimate of `lambda`.
   <details>
   <summary>Show Answer</summary>
   **Problem 5:** `E[X] = 1/lambda`. Set `bar{x} = 25/10 = 2.5 = 1/lambda`. So `tilde{lambda} = 1/2.5 = 0.4`.
   </details>
