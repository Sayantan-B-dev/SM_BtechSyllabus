# Estimation: Maximum Likelihood estimators

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 4  
**Date:** 11-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.6.1

## Notes

### 1. Introduction to Maximum Likelihood Estimation

Maximum Likelihood Estimation (MLE) is one of the most widely used methods for estimating parameters. The core idea is simple: **choose the parameter value that makes the observed data most probable** (i.e., maximizes the likelihood of obtaining the data we actually observed).

---

### 2. Likelihood Function

Let `X_1, X_2, ..., X_n` be a random sample from a distribution with probability function `f(x; theta)`, where `theta` is the unknown parameter.

The **likelihood function** is the joint probability of the observed data, viewed as a function of the parameter:

`L(theta; x_1, x_2, ..., x_n) = prod_{i=1}^{n} f(x_i; theta)`

For discrete distributions, this is the probability of observing the exact data.
For continuous distributions, this is the joint density evaluated at the observed data.

**Important:** The likelihood function treats the data as fixed (observed) and `theta` as variable. We want to find `theta` that maximizes `L(theta)`.

---

### 3. Log-Likelihood Function

It is often mathematically easier to work with the **log-likelihood function**:

`l(theta) = ln[L(theta)] = sum_{i=1}^{n} ln[f(x_i; theta)]`

**Why use log-likelihood?**
- The natural logarithm is a monotonic increasing function. So maximizing `L(theta)` is equivalent to maximizing `l(theta)`.
- The log transforms products into sums, which are much easier to differentiate.
- The sum of logs is numerically more stable to compute.

**Procedure to find MLE:**

1. Write the likelihood function `L(theta)`.
2. Take the natural log: `l(theta) = ln L(theta)`.
3. Differentiate `l(theta)` with respect to `theta`.
4. Set the derivative equal to 0 and solve for `theta` (this gives the MLE `hat{theta}`).
5. (Optional) Take the second derivative to confirm it is a maximum (negative second derivative).

---

### 4. MLE for Binomial Parameter `p`

#### 4.1 Setup

Suppose `X ~ Binomial(n, p)`. We observe `X = x` successes in `n` trials.

**Probability mass function:**

`P(X = x; p) = C(n, x) * p^x * (1-p)^{n-x}`

where `C(n, x) = n! / (x! * (n-x)!)`.

#### 4.2 Likelihood Function

`L(p) = C(n, x) * p^x * (1-p)^{n-x}`

#### 4.3 Log-Likelihood

`l(p) = ln[C(n, x)] + x * ln(p) + (n-x) * ln(1-p)`

#### 4.4 Derivative and Maximization

`d/dp l(p) = x/p - (n-x)/(1-p)`

Set equal to 0:

`x/p - (n-x)/(1-p) = 0`

`x/p = (n-x)/(1-p)`

`x * (1-p) = (n-x) * p`

`x - xp = np - xp`

`x = np`

`hat{p} = x / n`

#### 4.5 Second Derivative Check

`d^2/dp^2 l(p) = -x/p^2 - (n-x)/(1-p)^2 < 0`

Since the second derivative is negative, this is a maximum.

**MLE of `p`:** `hat{p} = X / n` (sample proportion)

---

### 5. MLE for Poisson Parameter `lambda`

#### 5.1 Setup

Suppose `X_1, X_2, ..., X_n` is a random sample from `Poisson(lambda)`.

**Probability mass function:**

`f(x_i; lambda) = (e^{-lambda} * lambda^{x_i}) / (x_i!)` for `x_i = 0, 1, 2, ...`

#### 5.2 Likelihood Function

`L(lambda) = prod_{i=1}^{n} (e^{-lambda} * lambda^{x_i}) / (x_i!)`

`= e^{-n*lambda} * lambda^{sum x_i} / (prod_{i=1}^{n} x_i!)`

#### 5.3 Log-Likelihood

`l(lambda) = -n*lambda + (sum x_i) * ln(lambda) - sum ln(x_i!)`

#### 5.4 Derivative and Maximization

`d/dlambda l(lambda) = -n + (sum x_i) / lambda`

Set equal to 0:

`-n + (sum x_i) / lambda = 0`

`(sum x_i) / lambda = n`

`lambda = (sum x_i) / n = bar{x}`

#### 5.5 Second Derivative Check

`d^2/dlambda^2 l(lambda) = - (sum x_i) / lambda^2 < 0` (for `sum x_i > 0`)

**MLE of `lambda`:** `hat{lambda} = bar{X}` (sample mean)

---

### 6. MLE for Normal Parameters `mu` and `sigma^2`

#### 6.1 Setup

Suppose `X_1, X_2, ..., X_n` is a random sample from `N(mu, sigma^2)`.

**Probability density function:**

`f(x_i; mu, sigma^2) = (1 / sqrt(2*pi*sigma^2)) * exp(-(x_i - mu)^2 / (2*sigma^2))`

#### 6.2 Likelihood Function

`L(mu, sigma^2) = prod_{i=1}^{n} (1 / sqrt(2*pi*sigma^2)) * exp(-(x_i - mu)^2 / (2*sigma^2))`

`= (1 / (2*pi*sigma^2))^{n/2} * exp(-sum (x_i - mu)^2 / (2*sigma^2))`

#### 6.3 Log-Likelihood

`l(mu, sigma^2) = -(n/2) * ln(2*pi) - (n/2) * ln(sigma^2) - (1/(2*sigma^2)) * sum (x_i - mu)^2`

#### 6.4 MLE for `mu`

Take partial derivative with respect to `mu`:

`partial / partial mu l(mu, sigma^2) = (1/sigma^2) * sum (x_i - mu)`

Set to 0:

`(1/sigma^2) * sum (x_i - mu) = 0`

`sum (x_i - mu) = 0`

`sum x_i - n*mu = 0`

`hat{mu} = (1/n) * sum x_i = bar{x}`

#### 6.5 MLE for `sigma^2`

Take partial derivative with respect to `sigma^2`:

`partial / partial sigma^2 l(mu, sigma^2) = -n/(2*sigma^2) + (1/(2*sigma^4)) * sum (x_i - mu)^2`

Set to 0:

`-n/(2*sigma^2) + (1/(2*sigma^4)) * sum (x_i - mu)^2 = 0`

Multiply both sides by `2*sigma^4`:

`-n*sigma^2 + sum (x_i - mu)^2 = 0`

`hat{sigma}^2 = (1/n) * sum (x_i - bar{x})^2`

#### 6.6 Results

**MLE of `mu`:** `hat{mu} = bar{X}` (sample mean)

**MLE of `sigma^2`:** `hat{sigma}^2 = (1/n) * sum (X_i - bar{X})^2` (sample variance with denominator `n`)

**Note:** The MLE for `sigma^2` is biased (it underestimates the population variance on average). The unbiased estimator uses denominator `n-1`.

---

### 7. Invariance Property of MLE

One of the most useful properties of MLEs is the **invariance property**:

**Statement:** If `hat{theta}` is the MLE of `theta`, then for any function `g(theta)`, the MLE of `g(theta)` is `g(hat{theta})`.

**Example:** If `hat{sigma}^2` is the MLE of the normal variance `sigma^2`, then:
- MLE of `sigma` (standard deviation) is `hat{sigma} = sqrt(hat{sigma}^2)`.
- MLE of precision `1/sigma^2` is `1/hat{sigma}^2`.

**Caution:** The invariance property holds for any function `g`, even non-linear functions. This is a powerful feature unique to MLE.

---

### 8. Worked Examples

#### Example 1: MLE for Binomial

A coin is tossed 100 times and lands heads 62 times. Find the MLE of the probability of heads `p`.

**Solution:**

`n = 100`, `x = 62`

`hat{p} = x / n = 62 / 100 = 0.62`

The MLE of `p` is 0.62.

---

#### Example 2: MLE for Poisson

The number of emails received per hour at a customer service desk is recorded for 10 hours: 3, 5, 2, 7, 4, 3, 6, 5, 4, 1. Find the MLE of `lambda`.

**Solution:**

`hat{lambda} = bar{x} = (3 + 5 + 2 + 7 + 4 + 3 + 6 + 5 + 4 + 1) / 10 = 40 / 10 = 4`

The MLE of the average number of emails per hour is 4.

---

#### Example 3: MLE for Normal

A random sample of 5 measurements from a normal distribution yields: 10.2, 9.8, 10.5, 10.0, 9.5. Find the MLEs of `mu` and `sigma^2`.

**Solution:**

`hat{mu} = bar{x} = (10.2 + 9.8 + 10.5 + 10.0 + 9.5) / 5 = 50.0 / 5 = 10.0`

`hat{sigma}^2 = (1/5) * sum (x_i - 10.0)^2`

`= (1/5) * [(0.2)^2 + (-0.2)^2 + (0.5)^2 + (0)^2 + (-0.5)^2]`

`= (1/5) * [0.04 + 0.04 + 0.25 + 0 + 0.25]`

`= (1/5) * 0.58 = 0.116`

Therefore, `hat{mu} = 10.0` and `hat{sigma}^2 = 0.116`.

---

#### Example 4: Using Invariance Property

For the normal data in Example 3, find the MLE of the standard deviation `sigma` and of the probability that a single observation exceeds 11 (i.e., `P(X > 11)`).

**Solution:**

MLE of `sigma`: `hat{sigma} = sqrt(0.116) = 0.3406`

MLE of `P(X > 11)`: Using the invariance property,

`hat{P}(X > 11) = P(Z > (11 - hat{mu}) / hat{sigma}) = P(Z > (11 - 10) / 0.3406) = P(Z > 2.936) = 1 - Phi(2.936)`

From standard normal table, `Phi(2.94) = 0.9984`, so:

`hat{P}(X > 11) approx 1 - 0.9984 = 0.0016`

---

### 9. Summary of MLE Results

| Distribution | Parameter(s) | MLE |
|-------------|--------------|-----|
| Binomial(`n`, `p`) | `p` | `hat{p} = X / n` |
| Poisson(`lambda`) | `lambda` | `hat{lambda} = bar{X}` |
| Normal(`mu`, `sigma^2`) | `mu` | `hat{mu} = bar{X}` |
| Normal(`mu`, `sigma^2`) | `sigma^2` | `hat{sigma}^2 = (1/n) sum (X_i - bar{X})^2` |

---

## Practice Problems

**Problem 1:** In a sample of 200 items from a production line, 15 are defective. Find the MLE of the proportion of defective items.

**Problem 2:** The number of accidents per day at an intersection is recorded for 30 days. The sum of all accidents is 45. Assuming a Poisson distribution, find the MLE of the mean number of accidents per day.

**Problem 3:** A random sample of size `n = 10` from a normal distribution gives `sum x_i = 250` and `sum (x_i - bar{x})^2 = 40`. Find the MLEs of `mu` and `sigma^2`.

**Problem 4:** State the invariance property of MLEs. If `hat{lambda} = bar{X}` is the MLE of the Poisson parameter `lambda`, what is the MLE of `e^{-lambda}` (the probability of zero events)?

**Problem 5:** Derive the MLE of the Bernoulli parameter `p` from first principles (hint: Bernoulli is a special case of Binomial with `n = 1`).

---

### Answers / Hints

**Problem 1:** `hat{p} = 15/200 = 0.075`.

**Problem 2:** `hat{lambda} = bar{x} = 45/30 = 1.5`.

**Problem 3:** `hat{mu} = 250/10 = 25`. `hat{sigma}^2 = 40/10 = 4`.

**Problem 4:** Invariance property: MLE of `g(theta)` is `g(hat{theta})`. MLE of `e^{-lambda}` is `e^{-hat{lambda}} = e^{-bar{X}}`.

**Problem 5:** For Bernoulli, `f(x; p) = p^x (1-p)^{1-x}` for `x = 0, 1`. `L(p) = prod p^{x_i} (1-p)^{1-x_i} = p^{sum x_i} (1-p)^{n - sum x_i}`. `l(p) = (sum x_i) ln p + (n - sum x_i) ln(1-p)`. `dl/dp = (sum x_i)/p - (n - sum x_i)/(1-p) = 0` gives `hat{p} = (sum x_i)/n = bar{x}`.
