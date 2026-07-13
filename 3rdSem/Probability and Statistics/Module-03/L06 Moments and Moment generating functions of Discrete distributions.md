# Moments and Moment generating functions of Discrete distributions

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 6  
**Date:** 21-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 7.3

## Notes

### 1. Definition of Moment Generating Function (MGF)

The **moment generating function (MGF)** of a random variable X is defined as:

`M_X(t) = E[e^{tX}]`

For a discrete random variable with PMF p(x):

`M_X(t) = sum_{x} e^{tx} * p(x)`

The MGF is a function of t that "generates" moments by differentiation. It exists if the sum/integral converges for t in some neighborhood of 0.

Notation: The MGF is often written as `M(t)` when the random variable is clear from context.

---

### 2. Properties of MGF

1. **Generates moments:** The r-th moment about the origin is:
   `E[X^r] = M^{(r)}(0)` (the r-th derivative of M(t) evaluated at t = 0)

   Specifically:
   - `E[X] = M'(0)` (first moment = first derivative at 0)
   - `E[X^2] = M''(0)` (second moment = second derivative at 0)
   - `E[X^r] = M^{(r)}(0)` (r-th moment = r-th derivative at 0)

2. **MGF at t = 0:** `M_X(0) = E[e^{0}] = E[1] = 1`

3. **Linear transformation:** If `Y = aX + b`, then `M_Y(t) = e^{bt} * M_X(at)`

4. **Sum of independent variables:** If X and Y are independent, then
   `M_{X+Y}(t) = M_X(t) * M_Y(t)`

5. **Uniqueness:** If two random variables have the same MGF (in a neighborhood of 0), they have the same distribution. This is a powerful property used to identify distributions.

---

### 3. Generating Moments from MGF

The process:
1. Compute the MGF: `M(t) = E[e^{tX}]`
2. Differentiate M(t) with respect to t.
3. Evaluate the derivative at t = 0 to get the corresponding moment.

#### Worked Example 1

For a discrete random variable with PMF: `P(X = -1) = 0.2`, `P(X = 0) = 0.3`, `P(X = 1) = 0.5`, find the MGF and use it to find `E[X]` and `E[X^2]`.

Solution:
`M(t) = E[e^{tX}] = e^{-t}(0.2) + e^{0}(0.3) + e^{t}(0.5)`
`M(t) = 0.2e^{-t} + 0.3 + 0.5e^{t}`

First derivative: `M'(t) = -0.2e^{-t} + 0.5e^{t}`
`M'(0) = -0.2(1) + 0.5(1) = 0.3`
So `E[X] = 0.3`

Second derivative: `M''(t) = 0.2e^{-t} + 0.5e^{t}`
`M''(0) = 0.2(1) + 0.5(1) = 0.7`
So `E[X^2] = 0.7`

Check: `Var(X) = 0.7 - 0.09 = 0.61`. Verify directly: `E[X] = -0.2+0+0.5=0.3`, `E[X^2]=0.2+0+0.5=0.7`. Correct.

---

### 4. MGF of Binomial Distribution

If `X ~ Binomial(n, p)`, then:

`M_X(t) = (1 - p + pe^{t})^n`

Derivation:
`M(t) = sum_{x=0}^{n} e^{tx} * C(n,x) p^x (1-p)^{n-x}`
`= sum_{x=0}^{n} C(n,x) (pe^{t})^x (1-p)^{n-x}`
`= (1-p + pe^{t})^n` (using binomial theorem)

Finding mean using MGF:
`M'(t) = n(1-p + pe^{t})^{n-1} * pe^{t}`
`M'(0) = n(1-p + p)^{n-1} * p = n(1)^{n-1} * p = np` => `E[X] = np`

Finding second moment:
`M''(t) = n(n-1)(1-p+pe^{t})^{n-2} (pe^{t})^2 + n(1-p+pe^{t})^{n-1} * pe^{t}`
`M''(0) = n(n-1)p^2 + np`
`Var(X) = M''(0) - [M'(0)]^2 = n(n-1)p^2 + np - (np)^2 = np - np^2 = np(1-p)`

---

### 5. MGF of Poisson Distribution

If `X ~ Poisson(lambda)`, then:

`M_X(t) = exp(lambda(e^{t} - 1))`

Derivation:
`M(t) = sum_{x=0}^{infty} e^{tx} * e^{-lambda} * lambda^x / x!`
`= e^{-lambda} sum_{x=0}^{infty} (lambda e^{t})^x / x!`
`= e^{-lambda} * e^{lambda e^{t}}` (using the exponential series `sum u^x/x! = e^u`)
`= e^{lambda(e^{t} - 1)}`

Finding mean using MGF:
`M'(t) = e^{lambda(e^{t} - 1)} * lambda e^{t}`
`M'(0) = e^{lambda(1-1)} * lambda * 1 = e^0 * lambda = lambda` => `E[X] = lambda`

`M''(t) = e^{lambda(e^{t}-1)}[(lambda e^{t})^2 + lambda e^{t}]`
`M''(0) = lambda^2 + lambda`
`Var(X) = (lambda^2 + lambda) - lambda^2 = lambda`

---

### 6. MGF of Geometric Distribution

If `X ~ Geometric(p)` with support x = 1, 2, 3, ..., then:

`M_X(t) = (p e^{t}) / (1 - (1-p)e^{t})` for `(1-p)e^{t} < 1`

Derivation:
`M(t) = sum_{x=1}^{infty} e^{tx} * (1-p)^{x-1} * p`
`= p e^{t} sum_{x=1}^{infty} [(1-p)e^{t}]^{x-1}`
`= p e^{t} / (1 - (1-p)e^{t})` (using geometric series `sum_{n=0}^{infty} r^n = 1/(1-r)`)

The series converges when `|(1-p)e^{t}| < 1`, i.e., `t < -ln(1-p)`.

---

### 7. Uniqueness Property

The **uniqueness property** of the MGF states:

If `M_X(t) = M_Y(t)` for all t in some interval around 0, then X and Y have the same probability distribution.

This is used to:
- Identify distributions by matching their MGFs to known forms.
- Prove that sums of independent random variables follow certain distributions (e.g., sum of independent Poissons is Poisson).

#### Worked Example 2

If `M_X(t) = (0.3 + 0.7e^{t})^{10}`, identify the distribution of X.

Solution: This matches the Binomial MGF `(1-p + pe^{t})^n`.
Comparing: `n = 10`, `p = 0.7`, `1-p = 0.3`.
So `X ~ Binomial(10, 0.7)`.

#### Worked Example 3

If `M_X(t) = e^{5(e^{t} - 1)}`, identify the distribution and find its mean.

Solution: This is `exp(lambda(e^{t} - 1))`, the Poisson MGF.
`lambda = 5`, so `X ~ Poisson(5)`.
Mean = `lambda = 5`.

---

### 8. Summary Table

| Distribution | PMF | MGF | Mean | Variance |
|-------------|-----|-----|------|----------|
| Binomial(n, p) | C(n,x)p^x(1-p)^{n-x} | (1-p+pe^t)^n | np | np(1-p) |
| Poisson(lambda) | e^{-l} l^x/x! | e^{l(e^t-1)} | l | l |
| Geometric(p) | (1-p)^{x-1}p | pe^t/(1-(1-p)e^t) | 1/p | (1-p)/p^2 |

---

## Practice Problems

1. Find the MGF of X with PMF: `P(X=0)=0.1, P(X=1)=0.4, P(X=2)=0.5`. Then find `E[X]` and `E[X^2]`.

2. If `M_X(t) = (0.6 + 0.4e^{t})^{15}`, identify the distribution and find its mean and variance.

3. If X ~ Poisson(3), find the MGF and use it to find `E[X]` and `E[X^2]`.

4. Show that the MGF of a Geometric distribution yields the correct mean.

5. Two independent random variables X ~ Poisson(2) and Y ~ Poisson(3). Find the MGF of `Z = X + Y` and identify its distribution.

**Answers / Hints:**
1. `M(t) = 0.1 + 0.4e^t + 0.5e^{2t}`. `M'(t) = 0.4e^t + e^{2t}` => `M'(0) = 1.4`. `M''(t) = 0.4e^t + 2e^{2t}` => `M''(0)=2.4`.
2. Binomial(15, 0.4). Mean = 6. Variance = 15(0.4)(0.6) = 3.6.
3. `M(t) = e^{3(e^t-1)}`. `M'(0)=3`, `M''(0)=9+3=12`. So `E[X]=3`, `E[X^2]=12`.
4. `M'(t) = [pe^t(1-(1-p)e^t) - pe^t(-(1-p)e^t)]/[1-(1-p)e^t]^2`. At t=0: `M'(0) = [p(1-(1-p)) + p(1-p)]/[1-(1-p)]^2 = [p*p + p(1-p)]/p^2 = (p^2+p-p^2)/p^2 = p/p^2 = 1/p`.
5. By independence: `M_Z(t) = M_X(t)*M_Y(t) = e^{2(e^t-1)} * e^{3(e^t-1)} = e^{5(e^t-1)}`. So Z ~ Poisson(5).
