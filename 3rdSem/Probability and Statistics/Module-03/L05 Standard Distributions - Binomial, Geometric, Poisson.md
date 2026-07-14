# Standard Distributions - Binomial, Geometric, Poisson

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 5  
**Date:** 20-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 8.4 , 8.30,8.60

## Notes

### 1. Overview

This lecture covers three important discrete probability distributions: Binomial, Geometric, and Poisson. Each models specific types of random experiments.

| Distribution | Models | Parameter(s) | Mean | Variance |
|-------------|--------|--------------|------|----------|
| Binomial | Number of successes in n trials | n, p | np | np(1-p) |
| Geometric | Number of trials until first success | p | 1/p | (1-p)/p^2 |
| Poisson | Number of events in fixed interval | lambda | lambda | lambda |

---

### 2. Binomial Distribution

**Assumptions (Bernoulli trials):**
1. Fixed number n of independent trials.
2. Each trial has exactly two outcomes: success (S) or failure (F).
3. Probability of success p is constant across all trials.
4. The random variable X = number of successes in n trials.

**PMF:** `P(X = x) = C(n, x) p^x (1-p)^{n-x}` for x = 0, 1, 2, ..., n

where `C(n, x) = n! / (x! (n-x)!)` is the binomial coefficient.

**Mean:** `E[X] = np`
**Variance:** `Var(X) = np(1-p)`

#### Worked Example 1

A fair coin is tossed 10 times. Find:
(a) Probability of exactly 6 heads.
(b) Probability of at most 2 heads.
(c) Mean and variance.

Solution:
(a) `P(X = 6) = C(10, 6) (0.5)^6 (0.5)^4 = C(10, 6) (0.5)^10`
`C(10, 6) = 10!/(6!4!) = 210`
`P(X = 6) = 210 * (0.5)^10 = 210/1024 = 105/512 ≈ 0.2051`

(b) `P(X <= 2) = P(X=0) + P(X=1) + P(X=2)`
`P(X=0) = C(10,0)(0.5)^10 = 1/1024`
`P(X=1) = C(10,1)(0.5)^10 = 10/1024`
`P(X=2) = C(10,2)(0.5)^10 = 45/1024`
`P(X <= 2) = (1 + 10 + 45)/1024 = 56/1024 = 7/128 ≈ 0.0547`

(c) `E[X] = np = 10(0.5) = 5`
`Var(X) = np(1-p) = 10(0.5)(0.5) = 2.5`
`sigma = sqrt(2.5) ≈ 1.581`

#### Worked Example 2

In a manufacturing process, 5% of items are defective. A sample of 20 items is selected. Find the probability that:
(a) Exactly 2 are defective.
(b) At least 1 is defective.
(c) Mean and variance.

Solution:
(a) `P(X = 2) = C(20, 2) (0.05)^2 (0.95)^18`
`= 190 * 0.0025 * (0.95)^18`
`= 0.475 * (0.95)^18`
`≈ 0.1887` (using calculator)

(b) `P(X >= 1) = 1 - P(X = 0) = 1 - C(20, 0)(0.05)^0(0.95)^20`
`= 1 - (0.95)^20 ≈ 1 - 0.3585 = 0.6415`

(c) `E[X] = 20(0.05) = 1`
`Var(X) = 20(0.05)(0.95) = 0.95`

---

### 3. Poisson Distribution

**Assumptions:**
1. Events occur independently in time or space.
2. The average rate (lambda) is constant.
3. Two events cannot occur at exactly the same instant.
4. The probability of an event in a small interval is proportional to the length of the interval.

**PMF:** `P(X = x) = (e^{-lambda} lambda^x) / x!` for x = 0, 1, 2, ...

**Mean:** `E[X] = lambda`
**Variance:** `Var(X) = lambda` (mean equals variance)

#### Worked Example 3

A call center receives an average of 4 calls per minute. Find:
(a) Probability of exactly 3 calls in a minute.
(b) Probability of at most 2 calls in a minute.
(c) Mean and variance.

Solution:
`lambda = 4`

(a) `P(X = 3) = e^{-4} * 4^3 / 3! = e^{-4} * 64 / 6 = (64/6) e^{-4} ≈ 10.667 * 0.0183 ≈ 0.1952`

(b) `P(X <= 2) = P(0) + P(1) + P(2)`
`P(0) = e^{-4} * 4^0 / 0! = e^{-4} ≈ 0.0183`
`P(1) = e^{-4} * 4 / 1 = 4e^{-4} ≈ 0.0733`
`P(2) = e^{-4} * 16 / 2 = 8e^{-4} ≈ 0.1465`
`P(X <= 2) = e^{-4}(1 + 4 + 8) = 13e^{-4} ≈ 13 * 0.0183 = 0.2379`

(c) `E[X] = 4`, `Var(X) = 4`

#### Worked Example 4

In a 500-page book, there are 250 typos. Find the probability that a given page has at least 2 typos.

Solution:
Average typos per page = `lambda = 250/500 = 0.5`

`P(X >= 2) = 1 - P(X <= 1) = 1 - [P(0) + P(1)]`
`P(0) = e^{-0.5} * 0.5^0 / 0! = e^{-0.5} ≈ 0.6065`
`P(1) = e^{-0.5} * 0.5 / 1 = 0.5e^{-0.5} ≈ 0.3033`
`P(X >= 2) = 1 - 0.6065 - 0.3033 = 0.0902`

---

### 4. Geometric Distribution

**Assumptions:**
1. Independent Bernoulli trials with success probability p.
2. The random variable X = number of trials needed to get the first success.
3. Support: x = 1, 2, 3, ... (unbounded).

**PMF:** `P(X = x) = (1-p)^{x-1} p` for x = 1, 2, 3, ...

**CDF:** `P(X <= k) = 1 - (1-p)^k`

**Mean:** `E[X] = 1/p`
**Variance:** `Var(X) = (1-p)/p^2`

#### Worked Example 5

A fair die is rolled until a 6 appears. Find:
(a) Probability that the first 6 occurs on the 4th roll.
(b) Probability that it takes at most 3 rolls.
(c) Mean and variance.

Solution:
`p = 1/6`

(a) `P(X = 4) = (1 - 1/6)^3 * (1/6) = (5/6)^3 * (1/6) = 125/1296 ≈ 0.0965`

(b) `P(X <= 3) = 1 - (1 - 1/6)^3 = 1 - (5/6)^3 = 1 - 125/216 = 91/216 ≈ 0.4213`

(c) `E[X] = 1/p = 6` (expected 6 rolls to get a 6)
`Var(X) = (1-p)/p^2 = (5/6)/(1/36) = (5/6)*36 = 30`

#### Worked Example 6

A student has a 30% chance of passing an exam. What is the probability she passes on her third attempt? What is the expected number of attempts?

Solution:
`p = 0.3`
`P(X = 3) = (0.7)^2 * 0.3 = 0.49 * 0.3 = 0.147`
`E[X] = 1/0.3 ≈ 3.33`

---

### 5. When to Use Each Distribution

| Scenario | Distribution | Reason |
|----------|-------------|--------|
| Fixed number of trials, count successes | Binomial | n fixed, p constant |
| Count events in fixed interval | Poisson | Rare events, constant rate |
| Number of trials to first success | Geometric | Waiting for first success |
| n large, p small, np moderate | Poisson approximates Binomial | Good approximation when n >= 50, p <= 0.1 |

---

### 6. Summary Table

| Property | Binomial(n, p) | Poisson(lambda) | Geometric(p) |
|----------|---------------|----------------|--------------|
| PMF | C(n,x) p^x (1-p)^{n-x} | e^{-l} l^x / x! | (1-p)^{x-1} p |
| Support | {0,1,...,n} | {0,1,2,...} | {1,2,3,...} |
| Mean | np | l | 1/p |
| Variance | np(1-p) | l | (1-p)/p^2 |
| Uses | Defects in sample, heads in coin tosses | Calls, accidents, typos | First success, waiting times |

---

## Practice Problems

1. A coin is biased with P(H) = 0.6. It is tossed 8 times. Find the probability of exactly 5 heads, and the mean number of heads.

   <details>
   <summary>Show Answer</summary>
   1. `P(X=5) = C(8,5)(0.6)^5(0.4)^3 = 56 * 0.07776 * 0.064 ≈ 0.279`. Mean = 8(0.6) = 4.8.
   </details>

2. On average, 3 customers arrive at a store per hour. Find the probability that exactly 5 customers arrive in a 2-hour period.

   <details>
   <summary>Show Answer</summary>
   2. lambda = 3*2 = 6. `P(X=5) = e^{-6} * 6^5 / 5! = e^{-6} * 7776/120 ≈ 0.1606`.
   </details>

3. A player has a 15% chance of winning a game. Find the probability that the first win occurs on the 5th game, and the expected number of games to win.

   <details>
   <summary>Show Answer</summary>
   3. `P(X=5) = (0.85)^4(0.15) ≈ 0.0783`. `E[X] = 1/0.15 ≈ 6.67`.
   </details>

4. In a class, 10% of students fail. If 15 students are selected at random, find P(at most 2 fail). Use both Binomial and Poisson approximation.

   <details>
   <summary>Show Answer</summary>
   4. Binomial: `P(X<=2) = C(15,0)(0.9)^15 + C(15,1)(0.1)(0.9)^14 + C(15,2)(0.1)^2(0.9)^13 ≈ 0.206 + 0.343 + 0.267 = 0.816`. Poisson: lambda = 1.5. `P(X<=2) = e^{-1.5}(1+1.5+1.125) = 3.625e^{-1.5} ≈ 0.809`.
   </details>

5. A fair die is rolled until a 5 or 6 appears. Find the probability that it takes exactly 3 rolls, and the expected number of rolls.
   <details>
   <summary>Show Answer</summary>
   5. p = 2/6 = 1/3. `P(X=3) = (2/3)^2(1/3) = 4/27 ≈ 0.148`. `E[X] = 3`.
   </details>
