# Estimation: Sufficiency

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 7  
**Date:** 18-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 17.2.2

## Notes

### 1. Introduction to Sufficiency

The concept of sufficiency addresses an important question: **Does a statistic capture all the information in the sample about the unknown parameter?**

A sufficient statistic condenses the data without losing any information about the parameter. Once we know the value of a sufficient statistic, the raw data contains no additional useful information for estimating the parameter.

---

### 2. Definition of Sufficient Statistic

A statistic `T(X_1, X_2, ..., X_n)` is said to be **sufficient** for a parameter `theta` if the conditional distribution of the sample given `T = t` does **not** depend on `theta`.

**In plain language:** Once we know the value of `T`, the remaining randomness in the data is independent of `theta`. All the information about `theta` in the sample is captured by `T`.

**Intuition:** If two different samples lead to the same value of `T`, they are equally informative about `theta`, regardless of the specific values in the sample.

---

### 3. Neyman-Fisher Factorization Theorem

This theorem provides a practical way to identify sufficient statistics.

#### 3.1 Statement

Let `X_1, X_2, ..., X_n` be a random sample from a distribution with probability function `f(x; theta)`. A statistic `T(X_1, ..., X_n)` is sufficient for `theta` **if and only if** the joint probability function can be factorized as:

`f(x_1, x_2, ..., x_n; theta) = g(T(x_1, ..., x_n); theta) * h(x_1, ..., x_n)`

where:

- `g(t; theta)` depends on `theta` and the statistic `T` (but not on the individual data values except through `T`)
- `h(x_1, ..., x_n)` does **not** depend on `theta` at all

#### 3.2 How to Use the Theorem

1. Write the joint density (or probability mass function) of the sample.
2. Try to factor it into:
   - A part that depends on `theta` only through some function `T` of the data.
   - A part that does not depend on `theta`.
3. The function `T` is a sufficient statistic.

---

### 4. Sufficient Statistics for Common Distributions

#### 4.1 Bernoulli/Binomial

Let `X_1, X_2, ..., X_n` be i.i.d. `Bernoulli(p)`.

**Joint PMF:**

`f(x_1, ..., x_n; p) = prod_{i=1}^{n} p^{x_i} (1-p)^{1-x_i}`

`= p^{sum x_i} * (1-p)^{n - sum x_i}`

`= [p^{t} (1-p)^{n-t}] * 1`

where `t = sum x_i`.

Here:
- `g(t; p) = p^t * (1-p)^{n-t}` (depends on data only through `t = sum x_i`)
- `h(x_1, ..., x_n) = 1` (no dependence on `p`)

By the factorization theorem, **`T = sum X_i` is sufficient for `p`**.

Equivalently, the sample proportion `hat{p} = T/n` is also sufficient (since it is a one-to-one function of `T`).

#### 4.2 Poisson

Let `X_1, X_2, ..., X_n` be i.i.d. `Poisson(lambda)`.

**Joint PMF:**

`f(x_1, ..., x_n; lambda) = prod_{i=1}^{n} (e^{-lambda} * lambda^{x_i}) / (x_i!)`

`= e^{-n*lambda} * lambda^{sum x_i} * (1 / prod x_i!)`

`= [e^{-n*lambda} * lambda^{t}] * [1 / prod x_i!]`

where `t = sum x_i`.

Here:
- `g(t; lambda) = e^{-n*lambda} * lambda^t`
- `h(x_1, ..., x_n) = 1 / prod (x_i!)` (no `lambda`)

**`T = sum X_i` is sufficient for `lambda`**.

Again, `bar{X} = T/n` is also sufficient.

#### 4.3 Normal

Let `X_1, X_2, ..., X_n` be i.i.d. `N(mu, sigma^2)`.

**Case 1: `sigma^2` known, `mu` unknown.**

Joint PDF:

`f(x_1, ..., x_n; mu) = (1 / (2*pi*sigma^2))^{n/2} * exp(-sum (x_i - mu)^2 / (2*sigma^2))`

`= (1 / (2*pi*sigma^2))^{n/2} * exp(-[sum x_i^2 - 2*mu*sum x_i + n*mu^2] / (2*sigma^2))`

`= [exp(mu*sum x_i / sigma^2 - n*mu^2 / (2*sigma^2))] * [(1 / (2*pi*sigma^2))^{n/2} * exp(-sum x_i^2 / (2*sigma^2))]`

The first factor depends on `mu` and on the data through `sum x_i` only. The second factor does not depend on `mu`.

Therefore, **`T = sum X_i` (or equivalently `bar{X}`) is sufficient for `mu`** when `sigma^2` is known.

**Case 2: Both `mu` and `sigma^2` unknown.**

We need a sufficient statistic for the vector parameter `theta = (mu, sigma^2)`.

From the joint PDF expression, the terms involving the parameters are functions of `sum x_i` and `sum x_i^2`:

`f(x_1, ..., x_n; mu, sigma^2) = (1 / (2*pi*sigma^2))^{n/2} * exp(-[sum x_i^2 - 2*mu*sum x_i + n*mu^2] / (2*sigma^2))`

This depends on the data only through `sum x_i` and `sum x_i^2`.

Therefore, the **pair `(T_1, T_2) = (sum X_i, sum X_i^2)` is jointly sufficient for `(mu, sigma^2)`**.

Equivalently, `(bar{X}, s_n^2)` or `(bar{X}, s^2)` are also jointly sufficient.

---

### 5. Minimal Sufficient Statistics

A sufficient statistic that provides the greatest possible data reduction is called a **minimal sufficient statistic**.

**Definition:** A sufficient statistic `T` is **minimal** if for any other sufficient statistic `S`, `T` can be expressed as a function of `S`.

**Intuition:** Among all sufficient statistics, the minimal sufficient statistic reduces the data to the smallest possible dimension while retaining all information about the parameter.

**Examples:**

| Distribution | Parameter | Minimal Sufficient Statistic |
|-------------|-----------|------------------------------|
| Bernoulli(`p`) | `p` | `sum X_i` |
| Poisson(`lambda`) | `lambda` | `sum X_i` |
| Normal(`mu`, `sigma^2`) (both unknown) | `(mu, sigma^2)` | `(sum X_i, sum X_i^2)` |

**Note:** The full sample `(X_1, ..., X_n)` is always sufficient (it trivially contains all information), but it is not minimal because it does not reduce the data.

---

### 6. Worked Examples

#### Example 1: Checking Sufficiency by Factorization

Let `X_1, X_2, ..., X_n` be i.i.d. `Exponential(lambda)` with PDF:

`f(x; lambda) = lambda * e^{-lambda*x}` for `x > 0`, `lambda > 0`

Show that `T = sum X_i` is sufficient for `lambda`.

**Solution:**

Joint PDF:

`f(x_1, ..., x_n; lambda) = prod_{i=1}^{n} lambda * e^{-lambda*x_i}`

`= lambda^n * exp(-lambda * sum x_i)`

`= [lambda^n * e^{-lambda*t}] * 1`

where `t = sum x_i`.

Here `g(t; lambda) = lambda^n * e^{-lambda*t}` and `h(x) = 1`. By the factorization theorem, `T = sum X_i` is sufficient for `lambda`.

---

#### Example 2: Non-Sufficient Statistic

Let `X_1, X_2` be i.i.d. `Bernoulli(p)`. Is the statistic `T = X_1` (the first observation only) sufficient for `p`?

**Solution:**

Joint PMF:

`f(x_1, x_2; p) = p^{x_1 + x_2} * (1-p)^{2 - (x_1 + x_2)}`

Can we factor this as `g(T(x_1, x_2); p) * h(x_1, x_2)` where `T = X_1`? If `T = x_1`, then we need to write:

`p^{x_1 + x_2} * (1-p)^{2 - x_1 - x_2} = [p^{x_1} * (1-p)^{1-x_1}] * [p^{x_2} * (1-p)^{1-x_2}]`

The second factor `[p^{x_2}*(1-p)^{1-x_2}]` still depends on `p`. It cannot be absorbed into `h` because `h` must not depend on `p`. Therefore, `X_1` alone cannot be a sufficient statistic.

This makes sense: throwing away `X_2` loses information about `p`.

---

#### Example 3: Sufficient Statistic for Uniform Distribution

Let `X_1, X_2, ..., X_n` be i.i.d. `Uniform(0, theta)`. Find a sufficient statistic for `theta`.

**Solution:**

PDF: `f(x; theta) = 1/theta` for `0 <= x <= theta`, and `0` otherwise.

Joint PDF:

`f(x_1, ..., x_n; theta) = (1/theta)^n * I(0 <= x_1 <= theta) * ... * I(0 <= x_n <= theta)`

where `I` is the indicator function.

`= (1/theta)^n * I(0 <= min(x_i)) * I(max(x_i) <= theta)`

`= [(1/theta)^n * I(max(x_i) <= theta)] * [I(0 <= min(x_i))]`

Let `T = max(X_i)`. Then:

`= g(t; theta) * h(x_1, ..., x_n)`

where `g(t; theta) = (1/theta)^n * I(t <= theta)` and `h(x) = I(0 <= min(x_i))`.

By the factorization theorem, **`T = max X_i` is sufficient for `theta`**.

**Note:** For the Uniform distribution, the sufficient statistic is `max X_i`, not `sum X_i`. This is different from the exponential family distributions.

---

#### Example 4: Using Sufficiency to Find MVUE

If `T` is a complete sufficient statistic for `theta`, then any unbiased estimator based on `T` is the **minimum variance unbiased estimator (MVUE)**.

**Application:** For Bernoulli(`p`), `T = sum X_i` is a complete sufficient statistic. The estimator `hat{p} = T/n = bar{X}` is unbiased and based on `T`, so it is the MVUE of `p`.

---

### 7. Summary Table

| Distribution | Parameter | Sufficient Statistic | Minimal? |
|-------------|-----------|---------------------|----------|
| Bernoulli(`p`) | `p` | `sum X_i` | Yes |
| Binomial(`n`, `p`) | `p` | `sum X_i` | Yes |
| Poisson(`lambda`) | `lambda` | `sum X_i` | Yes |
| Normal(`mu`, known `sigma^2`) | `mu` | `sum X_i` (or `bar{X}`) | Yes |
| Normal(`mu`, `sigma^2`) (both unknown) | `(mu, sigma^2)` | `(sum X_i, sum X_i^2)` | Yes |
| Exponential(`lambda`) | `lambda` | `sum X_i` | Yes |
| Uniform(`0`, `theta`) | `theta` | `max X_i` | Yes |

---

## Practice Problems

**Problem 1:** Let `X_1, X_2, ..., X_n` be i.i.d. `Bernoulli(p)`. Use the Neyman-Fisher factorization theorem to show that `sum X_i` is sufficient for `p`.

**Problem 2:** Let `X_1, X_2, ..., X_n` be i.i.d. `Poisson(lambda)`. Is `T = sum X_i^2` sufficient for `lambda`? Explain.

**Problem 3:** For a normal distribution with both parameters unknown, why do we need two statistics `(sum X_i, sum X_i^2)` rather than just `sum X_i`?

**Problem 4:** Let `X_1, X_2, ..., X_n` be i.i.d. `Exponential(lambda)`. Show that the sample mean `bar{X}` is sufficient for `lambda`.

**Problem 5:** What is a minimal sufficient statistic? Why is the full sample `(X_1, ..., X_n)` considered sufficient but not minimal?

---

### Answers / Hints

**Problem 1:** `f(x; p) = prod p^{x_i} (1-p)^{1-x_i} = p^{sum x_i} (1-p)^{n - sum x_i} = [p^{t} (1-p)^{n-t}] * 1`. So `T = sum X_i` is sufficient.

**Problem 2:** No. The joint PMF is `e^{-n*lambda} * lambda^{sum x_i} / prod (x_i!)`. This depends on the data only through `sum x_i`, not `sum x_i^2`. So `sum x_i` is sufficient, but `sum x_i^2` is not (it does not factor in the same way).

**Problem 3:** The joint normal PDF contains terms `-sum x_i^2/(2*sigma^2)` and `mu*sum x_i/sigma^2`. The parameter `sigma^2` appears in the `sum x_i^2` term, so we need both `sum X_i` and `sum X_i^2` to capture all information.

**Problem 4:** Joint PDF: `lambda^n * e^{-lambda * sum x_i}`. This is `[lambda^n * e^{-lambda * n * bar{x}}] * 1`. So `T = bar{X}` is sufficient (since `bar{X} = sum X_i / n` is a one-to-one function of `sum X_i`).

**Problem 5:** A minimal sufficient statistic achieves the maximum possible data reduction while remaining sufficient. The full sample is trivially sufficient but does not reduce the data at all; it has the same dimension as the data.
