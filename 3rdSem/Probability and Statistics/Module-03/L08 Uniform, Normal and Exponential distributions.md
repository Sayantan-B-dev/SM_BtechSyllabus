# Uniform, Normal and Exponential distributions

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 8  
**Date:** 27-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 9.4 , 9.30 , 9.53

## Notes

### 1. Uniform Distribution

The **continuous uniform distribution** models a random variable equally likely to fall anywhere in an interval [a, b].

**PDF:** `f(x) = 1/(b-a)` for `a <= x <= b`, and 0 elsewhere.

**CDF:** `F(x) = (x-a)/(b-a)` for `a <= x <= b`.

**Mean:** `E[X] = (a + b)/2`

**Variance:** `Var(X) = (b-a)^2 / 12`

**MGF:** `M_X(t) = (e^{bt} - e^{at}) / (t(b-a))` for t != 0, and `M_X(0) = 1`.

Notation: `X ~ U(a, b)` or `X ~ Uniform(a, b)`.

#### Worked Example 1

If X is uniformly distributed on [2, 8], find:
(a) PDF
(b) P(3 < X < 5)
(c) P(X > 6)
(d) Mean and variance

Solution:
(a) `f(x) = 1/(8-2) = 1/6` for `2 <= x <= 8`.

(b) `P(3 < X < 5) = int_{3}^{5} (1/6) dx = (5-3)/6 = 2/6 = 1/3`

(c) `P(X > 6) = int_{6}^{8} (1/6) dx = (8-6)/6 = 2/6 = 1/3`

(d) `E[X] = (2+8)/2 = 5`
`Var(X) = (8-2)^2/12 = 36/12 = 3`

#### Worked Example 2

A bus arrives every 15 minutes at a stop. A person arrives at a random time. What is the probability they wait less than 5 minutes?

Solution:
Let X = waiting time, `X ~ U(0, 15)`.
`f(x) = 1/15` on [0, 15].
`P(X < 5) = int_{0}^{5} (1/15) dx = 5/15 = 1/3`

---

### 2. Normal Distribution

The **normal distribution** (also called Gaussian distribution) is the most important continuous distribution in statistics.

**PDF:** `f(x) = 1/(sigma * sqrt{2pi}) * exp(-(x - mu)^2 / (2 sigma^2))` for `-infty < x < infty`

**Parameters:**
- `mu` = mean (location parameter, determines center)
- `sigma` = standard deviation (scale parameter, determines spread)

**Mean:** `E[X] = mu`
**Variance:** `Var(X) = sigma^2`
**MGF:** `M_X(t) = exp(mu t + sigma^2 t^2 / 2)`

Notation: `X ~ N(mu, sigma^2)`

**Properties of the Normal Curve:**
1. Bell-shaped, symmetric about the mean mu.
2. Mean = Median = Mode (all equal).
3. Total area under the curve = 1.
4. Tails extend to infinity in both directions.
5. Points of inflection at `x = mu +/- sigma`.

---

### 3. Standard Normal Distribution

If `mu = 0` and `sigma = 1`, we have the **standard normal distribution**, denoted `Z ~ N(0, 1)`.

**Standard normal PDF:** `phi(z) = 1/sqrt{2pi} * exp(-z^2/2)`

**Standard normal CDF:** `Phi(z) = P(Z <= z)` (tabulated values)

**Z-score transformation:** Any normal variable X ~ N(mu, sigma^2) can be converted to standard normal:

`Z = (X - mu) / sigma`

This is called **standardization** or computing the **z-score**.

#### Worked Example 3

If X ~ N(100, 25), find:
(a) P(X < 105)
(b) P(X > 90)
(c) P(95 < X < 110)

Solution:
`mu = 100`, `sigma = sqrt(25) = 5`

(a) `Z = (105 - 100)/5 = 1`
`P(X < 105) = P(Z < 1) = Phi(1)`
From standard normal table: `Phi(1) = 0.8413`

(b) `Z = (90 - 100)/5 = -2`
`P(X > 90) = P(Z > -2) = P(Z < 2) = Phi(2) = 0.9772`

(c) For X = 95: `Z = (95-100)/5 = -1`
For X = 110: `Z = (110-100)/5 = 2`
`P(95 < X < 110) = P(-1 < Z < 2) = Phi(2) - Phi(-1) = 0.9772 - 0.1587 = 0.8185`

---

### 4. Empirical Rule (68-95-99.7 Rule)

For any normal distribution:
- Approximately 68% of data lies within `mu +/- sigma`
- Approximately 95% of data lies within `mu +/- 2sigma`
- Approximately 99.7% of data lies within `mu +/- 3sigma`

| Interval | Percentage | Z-score range |
|----------|-----------|---------------|
| mu +/- sigma | 68.27% | -1 to 1 |
| mu +/- 2sigma | 95.45% | -2 to 2 |
| mu +/- 3sigma | 99.73% | -3 to 3 |

#### Worked Example 4

The heights of adult men are normally distributed with mean 170 cm and standard deviation 8 cm. What percentage of men are between 162 cm and 178 cm?

Solution:
`mu = 170`, `sigma = 8`
`162 = mu - 8 = mu - sigma`
`178 = mu + 8 = mu + sigma`
This is the `mu +/- sigma` range, so approximately 68%.

---

### 5. Exponential Distribution

The **exponential distribution** models waiting times between events in a Poisson process.

**PDF:** `f(x) = lambda e^{-lambda x}` for `x >= 0`, and 0 elsewhere.

**CDF:** `F(x) = 1 - e^{-lambda x}` for `x >= 0`.

**Mean:** `E[X] = 1/lambda`

**Variance:** `Var(X) = 1/lambda^2`

**MGF:** `M_X(t) = lambda / (lambda - t)` for `t < lambda`.

**Memoryless property:** For any s, t > 0:

`P(X > s + t | X > s) = P(X > t)`

This means the remaining lifetime does not depend on how long you have already waited. The exponential is the only continuous distribution with this property.

Notation: `X ~ Exp(lambda)`.

#### Worked Example 5

The time between arrivals at a service center follows Exponential distribution with mean 10 minutes.
(a) Find lambda.
(b) Probability that the next customer arrives within 5 minutes.
(c) Probability that the next customer takes more than 15 minutes.

Solution:
(a) `E[X] = 1/lambda = 10` => `lambda = 0.1` per minute

(b) `P(X < 5) = F(5) = 1 - e^{-0.1*5} = 1 - e^{-0.5} = 1 - 0.6065 = 0.3935`

(c) `P(X > 15) = 1 - F(15) = e^{-0.1*15} = e^{-1.5} = 0.2231`

#### Worked Example 6 (Memoryless Property)

A machine has exponential lifetime with mean 100 hours. If it has already been running for 50 hours, what is the probability it runs for another 100 hours?

Solution:
`P(X > 150 | X > 50) = P(X > 100)` (by memoryless property)
`lambda = 1/100 = 0.01`
`P(X > 100) = e^{-0.01*100} = e^{-1} = 0.3679`

---

### 6. Summary Table

| Distribution | PDF | Mean | Variance | Parameter(s) |
|-------------|-----|------|----------|--------------|
| Uniform(a,b) | 1/(b-a) on [a,b] | (a+b)/2 | (b-a)^2/12 | a, b |
| Normal(mu, sigma^2) | 1/(s sqrt(2p)) e^{-(x-m)^2/(2s^2)} | mu | sigma^2 | mu, sigma |
| Exponential(lambda) | l e^{-l x}, x>=0 | 1/l | 1/l^2 | lambda |

---

### 7. Relationship Between Distributions

- Exponential is related to Poisson: if events follow Poisson(lambda) per unit time, the inter-arrival times follow Exp(lambda).
- Normal distribution arises from the Central Limit Theorem: sums of independent random variables are approximately normal.
- Normal distribution with mu=0, sigma=1 is standard normal. Every normal can be standardized to N(0,1).

---

## Practice Problems

1. X ~ U(0, 20). Find P(X > 15 | X > 10).

   <details>
   <summary>Show Answer</summary>
   1. `P(X>15|X>10) = P(X>15)/P(X>10) = (5/20)/(10/20) = 5/10 = 0.5`.
   </details>

2. IQ scores are normally distributed with mean 100 and standard deviation 15. Find the probability that a randomly selected person has IQ between 85 and 115.

   <details>
   <summary>Show Answer</summary>
   2. Z-scores: (85-100)/15 = -1, (115-100)/15 = 1. So 68.27% (by empirical rule).
   </details>

3. The lifetime of a light bulb follows Exp(lambda) with mean 2000 hours. Find the probability it lasts more than 3000 hours, and the probability it lasts more than 3000 hours given it has already lasted 1000 hours.

   <details>
   <summary>Show Answer</summary>
   3. l = 1/2000. `P(X>3000) = e^{-1.5} = 0.2231`. By memoryless: same as P(X>2000) = e^{-1} = 0.3679.
   </details>

4. If Z ~ N(0, 1), find P(Z < -1.5) and P(-0.5 < Z < 1.5) using the standard normal table.

   <details>
   <summary>Show Answer</summary>
   4. `P(Z<-1.5) = 0.0668`. `P(-0.5<Z<1.5) = Phi(1.5) - Phi(-0.5) = 0.9332 - 0.3085 = 0.6247`.
   </details>

5. A random variable X is uniformly distributed on [5, 10]. Find its mean, variance, and P(6 < X < 9).
   <details>
   <summary>Show Answer</summary>
   5. E[X] = 7.5. Var = (10-5)^2/12 = 25/12. P(6<X<9) = (9-6)/(10-5) = 3/5 = 0.6.
   </details>
