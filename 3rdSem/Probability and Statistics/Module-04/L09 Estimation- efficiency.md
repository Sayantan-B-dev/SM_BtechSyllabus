# Estimation: efficiency

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 9  
**Date:** 25-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.2.3

## Notes

### 1. Introduction to Efficiency

When we have multiple unbiased estimators for the same parameter, we need a way to choose between them. **Efficiency** provides this criterion: among unbiased estimators, we prefer the one with the **smallest variance**.

**Core idea:** An estimator with smaller variance is more "precise" -- it produces estimates that are closer to the true value on average.

---

### 2. Definition of Efficiency

#### 2.1 Relative Efficiency

Let `hat{theta}_1` and `hat{theta}_2` be two unbiased estimators of `theta`. The **relative efficiency** of `hat{theta}_1` with respect to `hat{theta}_2` is:

`Eff(hat{theta}_1, hat{theta}_2) = Var(hat{theta}_2) / Var(hat{theta}_1)`

- If `Eff > 1`, then `hat{theta}_1` is more efficient (has smaller variance) than `hat{theta}_2`.
- If `Eff < 1`, then `hat{theta}_2` is more efficient.
- If `Eff = 1`, both estimators are equally efficient.

#### 2.2 Most Efficient Estimator (MVUE)

An unbiased estimator is called the **Minimum Variance Unbiased Estimator (MVUE)** if it has the smallest variance among all unbiased estimators of `theta`.

---

### 3. Cramer-Rao Lower Bound (CRLB)

The Cramer-Rao Lower Bound provides a theoretical lower bound on the variance of any unbiased estimator.

#### 3.1 Statement

Under regularity conditions, the variance of any unbiased estimator `hat{theta}` of `theta` satisfies:

`Var(hat{theta}) >= 1 / I_n(theta)`

where `I_n(theta)` is the **Fisher Information** in the sample.

#### 3.2 Fisher Information

The Fisher information for a sample of size `n` is:

`I_n(theta) = n * I_1(theta)`

where `I_1(theta)` is the Fisher information for a single observation:

`I_1(theta) = E[(d/dtheta ln f(X; theta))^2]`

Under regularity, this is also equal to:

`I_1(theta) = -E[d^2/dtheta^2 ln f(X; theta)]`

#### 3.3 CRLB for Common Distributions

| Distribution | Parameter | `f(x; theta)` | `I_1(theta)` | CRLB (for n observations) |
|-------------|-----------|---------------|--------------|---------------------------|
| Bernoulli(`p`) | `p` | `p^x (1-p)^{1-x}` | `1/[p(1-p)]` | `p(1-p)/n` |
| Poisson(`lambda`) | `lambda` | `e^{-lambda} lambda^x / x!` | `1/lambda` | `lambda/n` |
| Normal(`mu`) (known `sigma^2`) | `mu` | `N(mu, sigma^2)` | `1/sigma^2` | `sigma^2/n` |
| Normal(`sigma^2`) (known `mu`) | `sigma^2` | `N(mu, sigma^2)` | `1/(2*sigma^4)` | `2*sigma^4/n` |

---

### 4. Efficiency of an Estimator

The **efficiency** of an unbiased estimator `hat{theta}` is defined as:

`Eff(hat{theta}) = CRLB / Var(hat{theta})`

- `0 <= Eff(hat{theta}) <= 1` for any unbiased estimator.
- If `Eff(hat{theta}) = 1`, the estimator is **efficient** (it attains the CRLB, meaning it has the minimum possible variance).

#### 4.1 Asymptotic Efficiency

For large samples, many estimators (including MLEs) achieve the CRLB. Such estimators are called **asymptotically efficient**.

---

### 5. Efficiency of Common Estimators

#### 5.1 Sample Mean for Normal Distribution

For `X_1, ..., X_n ~ N(mu, sigma^2)`:

`Var(bar{X}) = sigma^2 / n`

CRLB for `mu` = `sigma^2 / n`

`Eff(bar{X}) = (sigma^2/n) / (sigma^2/n) = 1`

The sample mean is **efficient** for `mu` in normal populations.

#### 5.2 Sample Proportion

For `X ~ Binomial(n, p)`:

`Var(hat{p}) = p(1-p)/n`

CRLB for `p` = `p(1-p)/n`

`Eff(hat{p}) = 1`

The sample proportion is **efficient** for `p`.

#### 5.3 Sample Variance (unbiased) vs MLE

For normal data:

`s^2 = (1/(n-1)) * sum (X_i - bar{X})^2` has variance `= 2*sigma^4/(n-1)`.

The MLE `hat{sigma}_n^2 = (1/n) * sum (X_i - bar{X})^2` has MSE:

`MSE(hat{sigma}_n^2) = Var(hat{sigma}_n^2) + Bias^2 = 2*sigma^4*(n-1)/n^2 + (sigma^2/n)^2 = sigma^4*(2n-1)/n^2`

For large `n`, both are close, but for small `n`, the biased MLE may have lower MSE despite being biased.

CRLB for `sigma^2` (with known `mu`): `2*sigma^4/n`. The unbiased `s^2` does **not** achieve the CRLB (because `Var(s^2) = 2*sigma^4/(n-1) > 2*sigma^4/n`), so `s^2` is not fully efficient.

---

### 6. Comparing MLE and MOM Efficiency

| Distribution | Parameter | MLE Variance (asymptotic) | MOM Variance (if different) | More Efficient |
|-------------|-----------|--------------------------|---------------------------|----------------|
| Normal `mu` | `mu` | `sigma^2/n` | Same | Equal |
| Normal `sigma^2` | `sigma^2` | `2*sigma^4/n` (approx) | Same | Equal |
| Poisson `lambda` | `lambda` | `lambda/n` | Same | Equal |
| Bernoulli `p` | `p` | `p(1-p)/n` | Same | Equal |
| Gamma `(alpha, beta)` | `alpha`, `beta` | Achieves CRLB asymptotically | Higher variance | MLE |
| Uniform `(0, theta)` | `theta` | Depends on `theta` | May differ | MLE typically |

**General rule:** MLEs are asymptotically efficient (achieve CRLB as `n -> infinity`). MOM estimators may not be.

---

### 7. Worked Examples

#### Example 1: Computing Relative Efficiency

For a normal population `N(mu, sigma^2)`, compare the efficiency of the sample mean `bar{X}` and the sample median `tilde{X}` as estimators of `mu`.

**Solution:**

`Var(bar{X}) = sigma^2 / n`

For large `n`, `Var(tilde{X}) ~= (pi/2) * (sigma^2 / n) = 1.571 * sigma^2 / n`

`Eff(bar{X}, tilde{X}) = Var(tilde{X}) / Var(bar{X}) = 1.571 * sigma^2/n / (sigma^2/n) = 1.571`

The sample mean is about 1.571 times more efficient than the sample median for normal data.

---

#### Example 2: CRLB for Bernoulli

Derive the CRLB for `p` in a Bernoulli distribution.

**Solution:**

`f(x; p) = p^x (1-p)^{1-x}`

`ln f(x; p) = x * ln p + (1-x) * ln(1-p)`

`d/dp ln f = x/p - (1-x)/(1-p)`

`d^2/dp^2 ln f = -x/p^2 - (1-x)/(1-p)^2`

Fisher Information:

`I_1(p) = -E[d^2/dp^2 ln f] = -E[-X/p^2 - (1-X)/(1-p)^2]`

`= E[X]/p^2 + E[1-X]/(1-p)^2`

`= p/p^2 + (1-p)/(1-p)^2 = 1/p + 1/(1-p) = (1-p+p)/(p(1-p)) = 1/(p(1-p))`

CRLB for `n` observations: `1/(n * I_1(p)) = 1/(n * 1/(p(1-p))) = p(1-p)/n`

---

#### Example 3: Checking Efficiency

Let `X_1, X_2, ..., X_n` be i.i.d. `Poisson(lambda)`. Show that `bar{X}` is an efficient estimator of `lambda`.

**Solution:**

`Var(bar{X}) = lambda / n`

For Poisson, we computed `I_1(lambda) = 1/lambda`.

CRLB = `1/(n * (1/lambda)) = lambda / n`

Since `Var(bar{X}) = lambda/n = CRLB`, the sample mean is efficient for the Poisson parameter `lambda`.

---

#### Example 4: Comparing Two Estimators

Let `X_1, X_2, ..., X_n` be i.i.d. with mean `mu` and variance `sigma^2`. Consider:

`hat{theta}_1 = bar{X}`

`hat{theta}_2 = (X_1 + X_2 + X_3)/3` (using only the first 3 observations regardless of `n`)

Compute the relative efficiency of `hat{theta}_1` with respect to `hat{theta}_2`.

**Solution:**

`Var(hat{theta}_1) = sigma^2 / n`

`Var(hat{theta}_2) = sigma^2 / 3` (since only 3 observations are used)

`Eff(hat{theta}_1, hat{theta}_2) = (sigma^2/3) / (sigma^2/n) = n/3`

For `n > 3`, `hat{theta}_1` is more efficient (ratio > 1). For `n = 30`, `Eff = 10`, meaning `bar{X}` is 10 times more efficient.

---

#### Example 5: MSE Comparison (Biased vs Unbiased)

For normal data with `n = 5`, compare the MSE of:

`hat{sigma}_1^2 = (1/4) * sum (X_i - bar{X})^2` (unbiased `s^2`)

`hat{sigma}_2^2 = (1/5) * sum (X_i - bar{X})^2` (MLE)

**Solution:**

For normal data:

`Var(s^2) = 2*sigma^4/(n-1) = 2*sigma^4/4 = sigma^4/2`

`MSE(hat{sigma}_1^2) = Var(s^2) = 0.5*sigma^4`

`Var(hat{sigma}_2^2) = 2*sigma^4*(n-1)/n^2 = 2*sigma^4*4/25 = 8*sigma^4/25 = 0.32*sigma^4`

`Bias(hat{sigma}_2^2) = -sigma^2/n = -sigma^2/5`

`Bias^2 = sigma^4/25 = 0.04*sigma^4`

`MSE(hat{sigma}_2^2) = 0.32*sigma^4 + 0.04*sigma^4 = 0.36*sigma^4`

The MLE has lower MSE (0.36 vs 0.5) even though it is biased, because its variance is sufficiently smaller.

---

### 8. Summary Table

| Concept | Formula | Interpretation |
|---------|---------|----------------|
| Relative Efficiency | `Var(hat{theta}_2) / Var(hat{theta}_1)` | Ratio > 1 means estimator 1 is more efficient |
| CRLB | `1 / I_n(theta)` | Lower bound on variance of unbiased estimators |
| Efficiency (of an estimator) | `CRLB / Var(hat{theta})` | Between 0 and 1; 1 means efficient |
| Fisher Information | `I_n(theta) = n * E[(d/dtheta ln f)^2]` | Measures information in sample about `theta` |
| MVUE | Unbiased estimator achieving CRLB | Best possible unbiased estimator |

---

## Practice Problems

**Problem 1:** For a normal distribution `N(mu, 4)`, a sample of size `n = 16` is taken. What is the CRLB for estimating `mu`? What is `Var(bar{X})`? Is `bar{X}` efficient?

   <details>
   <summary>Show Answer</summary>
   **Problem 1:** CRLB `= sigma^2/n = 4/16 = 0.25`. `Var(bar{X}) = 4/16 = 0.25`. `Eff = 1`. Yes, `bar{X}` is efficient.
   </details>

**Problem 2:** Two unbiased estimators of `theta` have variances: `Var(hat{theta}_1) = 2/n` and `Var(hat{theta}_2) = 5/n`. Which estimator is more efficient? Compute the relative efficiency.

   <details>
   <summary>Show Answer</summary>
   **Problem 2:** `hat{theta}_1` is more efficient. `Eff(hat{theta}_1, hat{theta}_2) = (5/n)/(2/n) = 2.5`. Estimator 1 is 2.5 times more efficient.
   </details>

**Problem 3:** Derive the Fisher information `I_1(lambda)` for a single Poisson observation.

   <details>
   <summary>Show Answer</summary>
   **Problem 3:** `ln f = -lambda + x*ln lambda - ln(x!)`. `d/dlambda ln f = -1 + x/lambda`. `d^2/dlambda^2 ln f = -x/lambda^2`. `I_1(lambda) = -E[-X/lambda^2] = E[X]/lambda^2 = lambda/lambda^2 = 1/lambda`.
   </details>

**Problem 4:** For a normal distribution with unknown `mu` and known `sigma^2 = 9`, compare the efficiency of `bar{X}` and the sample median as estimators of `mu` for large `n`.

   <details>
   <summary>Show Answer</summary>
   **Problem 4:** `Var(bar{X}) = 9/n`. `Var(median) approx (pi/2)*(9/n) = 14.137/n`. `Eff = 14.137/9 = 1.571`. `bar{X}` is 1.571 times more efficient.
   </details>

**Problem 5:** What does it mean for an estimator to be asymptotically efficient? Why are MLEs generally preferred over MOM estimators in large samples?
   <details>
   <summary>Show Answer</summary>
   **Problem 5:** Asymptotically efficient means that as `n -> infinity`, the estimator's variance approaches the CRLB. MLEs are asymptotically efficient, while MOM estimators may not achieve the CRLB. Therefore, for large samples, MLEs are preferred.
   </details>
