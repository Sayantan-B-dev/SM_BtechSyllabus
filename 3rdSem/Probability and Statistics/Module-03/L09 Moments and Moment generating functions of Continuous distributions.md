# Moments and Moment generating functions of Continuous distributions

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 9  
**Date:** 28-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 7.3

## Notes

### 1. MGF for Continuous Distributions

For a continuous random variable X with PDF f(x), the **moment generating function (MGF)** is defined as:

`M_X(t) = E[e^{tX}] = int_{-infty}^{infty} e^{tx} * f(x) dx`

The MGF exists if the integral converges for t in some interval around 0. The same properties hold as for discrete distributions:

1. `M(0) = 1`
2. `E[X^r] = M^{(r)}(0)` (r-th derivative at 0)
3. Linear transformation: `M_{aX+b}(t) = e^{bt} M_X(at)`
4. Sum of independent variables: `M_{X+Y}(t) = M_X(t) * M_Y(t)`
5. Uniqueness: Same MGF implies same distribution.

---

### 2. MGF of Uniform Distribution

If `X ~ Uniform(a, b)`, then:

`M_X(t) = (e^{bt} - e^{at}) / (t(b-a))` for t != 0, and `M_X(0) = 1`

Derivation:
`M(t) = int_{a}^{b} e^{tx} * (1/(b-a)) dx`
`= (1/(b-a)) * [e^{tx}/t]_{a}^{b}`
`= (e^{bt} - e^{at}) / (t(b-a))`

#### Worked Example 1

For `X ~ Uniform(0, 1)`, find the MGF and use it to find `E[X]` and `E[X^2]`.

Solution:
`M(t) = (e^{t} - e^{0}) / (t(1-0)) = (e^{t} - 1)/t` for t != 0

To find E[X], we need `M'(0)`. Using series expansion:
`e^{t} = 1 + t + t^2/2! + t^3/3! + t^4/4! + ...`
`e^{t} - 1 = t + t^2/2! + t^3/3! + t^4/4! + ...`
`(e^{t} - 1)/t = 1 + t/2! + t^2/3! + t^3/4! + ...`

So `M(t) = 1 + t/2 + t^2/6 + t^3/24 + ...`

`M'(t) = 1/2 + t/3 + t^2/8 + ...`
`M'(0) = 1/2` => `E[X] = 1/2`

`M''(t) = 1/3 + t/4 + ...`
`M''(0) = 1/3` => `E[X^2] = 1/3`

`Var(X) = 1/3 - (1/2)^2 = 1/3 - 1/4 = 1/12` (matches formula `(b-a)^2/12`)

---

### 3. MGF of Normal Distribution

If `X ~ N(mu, sigma^2)`, then:

`M_X(t) = exp(mu t + sigma^2 t^2 / 2)`

**Derivation for standard normal Z ~ N(0, 1):**
`M_Z(t) = int_{-infty}^{infty} e^{tz} * (1/sqrt{2pi}) * e^{-z^2/2} dz`
`= 1/sqrt{2pi} int_{-infty}^{infty} e^{-(z^2 - 2tz)/2} dz`
`= 1/sqrt{2pi} int_{-infty}^{infty} e^{-[(z - t)^2 - t^2]/2} dz`
`= e^{t^2/2} * (1/sqrt{2pi}) int_{-infty}^{infty} e^{-(z-t)^2/2} dz`
`= e^{t^2/2} * 1` (the integral is the total probability of N(t, 1))
`= e^{t^2/2}`

For general `X = mu + sigma Z`:
`M_X(t) = e^{mu t} * M_Z(sigma t) = e^{mu t} * e^{sigma^2 t^2 / 2} = exp(mu t + sigma^2 t^2/2)`

#### Worked Example 2

For `X ~ N(2, 9)`, find the MGF and use it to find `E[X]` and `Var(X)`.

Solution:
`M(t) = exp(2t + 9t^2/2)`

`M'(t) = M(t) * (2 + 9t)`
`M'(0) = M(0) * 2 = 1 * 2 = 2` => `E[X] = 2 = mu`

`M''(t) = M'(t)(2 + 9t) + M(t)(9)`
`M''(0) = M'(0)(2) + M(0)(9) = 2(2) + 9 = 13`
`E[X^2] = 13`
`Var(X) = 13 - 4 = 9 = sigma^2`

#### Worked Example 3

If `M_X(t) = e^{3t + 2t^2}`, find `E[X]` and `Var(X)`.

Solution:
Comparing with `exp(mu t + sigma^2 t^2/2)`:
`mu = 3`, and `sigma^2/2 = 2` => `sigma^2 = 4`
So `E[X] = 3`, `Var(X) = 4`.

---

### 4. MGF of Exponential Distribution

If `X ~ Exp(lambda)`, then:

`M_X(t) = lambda / (lambda - t)` for `t < lambda`

Derivation:
`M(t) = int_{0}^{infty} e^{tx} * lambda e^{-lambda x} dx`
`= lambda int_{0}^{infty} e^{-(lambda - t)x} dx`
`= lambda * [(-1/(lambda - t)) * e^{-(lambda - t)x}]_{0}^{infty}`
`= lambda/(lambda - t)` (converges when `lambda - t > 0`)

#### Worked Example 4

For `X ~ Exp(2)`, find the MGF and derive the mean.

Solution:
`M(t) = 2/(2 - t)` for `t < 2`

`M'(t) = 2 * [d/dt (1/(2-t))] = 2 * [1/(2-t)^2]`
`M'(0) = 2 * 1/4 = 1/2` => `E[X] = 1/2 = 1/lambda`

`M''(t) = 2 * [2/(2-t)^3] = 4/(2-t)^3`
`M''(0) = 4/8 = 1/2`
`Var(X) = 1/2 - (1/2)^2 = 1/2 - 1/4 = 1/4 = 1/lambda^2`

---

### 5. Using MGF to Find Moments: General Procedure

1. Compute (or recall) the MGF `M(t)`.
2. Differentiate repeatedly to get `M^{(r)}(t)`.
3. Evaluate at `t = 0` to get `E[X^r] = M^{(r)}(0)`.

#### Worked Example 5

For `X ~ N(0, 1)`, find `E[X^4]`.

Solution:
`M(t) = e^{t^2/2}`
`M'(t) = t e^{t^2/2}`
`M''(t) = e^{t^2/2} + t^2 e^{t^2/2}` (1 + t^2)e^{t^2/2}
`M'''(t) = 2t e^{t^2/2} + (1+t^2)t e^{t^2/2} = t(3+t^2)e^{t^2/2}`
`M''''(t) = (3+t^2)e^{t^2/2} + 2t^2 e^{t^2/2} + t(3+t^2)t e^{t^2/2}`
At t=0: all terms with t factor vanish.
`M''''(0) = 3 * 1 = 3`

So `E[Z^4] = 3` (fourth moment of standard normal).

---

### 6. Summary Table

| Distribution | PDF | MGF | E[X] | Var(X) |
|-------------|-----|-----|------|--------|
| Uniform(a,b) | 1/(b-a), x in [a,b] | (e^{bt}-e^{at})/(t(b-a)) | (a+b)/2 | (b-a)^2/12 |
| Normal(mu, s^2) | 1/(s sqrt(2p)) e^{-(x-m)^2/(2s^2)} | e^{mu t + s^2 t^2/2} | mu | s^2 |
| Exponential(l) | l e^{-l x}, x>=0 | l/(l-t), t<l | 1/l | 1/l^2 |

---

## Practice Problems

1. For `X ~ Uniform(2, 6)`, find the MGF and use it to compute `E[X]` and `E[X^2]`.

   <details>
   <summary>Show Answer</summary>
   1. `M(t) = (e^{6t} - e^{2t})/(4t)`. Using expansion: `M(t) = 1 + 4t + (28/3)t^2 + ...`. So `E[X] = 4`, `E[X^2] = 56/3`, `Var = 56/3 - 16 = 56/3 - 48/3 = 8/3 = (b-a)^2/12`.
   </details>

2. If `M_X(t) = exp(4t + 2t^2)`, identify the distribution and find `P(X > 4)`.

   <details>
   <summary>Show Answer</summary>
   2. `X ~ N(4, 4)`. `P(X > 4) = P(Z > 0) = 0.5`.
   </details>

3. For `X ~ Exp(0.5)`, use the MGF to find the variance.

   <details>
   <summary>Show Answer</summary>
   3. `M(t) = 0.5/(0.5 - t) = 1/(1-2t)`. `M'(0) = 2`, `M''(0) = 8`. `Var = 8 - 4 = 4 = 1/(0.5)^2`.
   </details>

4. Find the MGF of `X ~ N(-1, 4)`. Use it to find `E[X^3]`.

   <details>
   <summary>Show Answer</summary>
   4. `M(t) = e^{-t + 2t^2}`. Find `M'''(0)`. `E[X^3] = -4`.
   </details>

5. If X has MGF `M(t) = (0.4 + 0.6e^t)^3`, identify the distribution (discrete). Find `E[X]` and `Var(X)`.
   <details>
   <summary>Show Answer</summary>
   5. Binomial(3, 0.6). `E[X] = 1.8`. `Var(X) = 3(0.6)(0.4) = 0.72`.
   </details>
