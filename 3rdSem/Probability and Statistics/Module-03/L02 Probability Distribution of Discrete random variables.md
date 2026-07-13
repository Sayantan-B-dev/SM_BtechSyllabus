# Probability Distribution of Discrete random variables

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 2  
**Date:** 13-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 5.6

## Notes

### 1. Discrete Probability Distribution

A **discrete probability distribution** is a listing of all possible values a discrete random variable X can take, along with their corresponding probabilities. It completely describes the probabilistic behavior of X.

A discrete probability distribution can be represented as:
- A table (values and their probabilities)
- A formula (PMF)
- A graph (bar chart or stem plot)

---

### 2. Conditions for a Valid PMF

A function `p(x)` is a valid probability mass function (PMF) if and only if:

1. **Non-negativity:** `p(x) >= 0` for every possible value x of X.
2. **Total probability:** `sum_{x} p(x) = 1` where the sum is taken over all possible values of X.

These two conditions must always be satisfied for any discrete probability distribution.

---

### 3. Computing Probabilities from PMF

To compute probabilities from a PMF:

- `P(X = a)` = `p(a)` (direct evaluation)
- `P(X <= a)` = `sum_{x <= a} p(x)` (sum all probabilities up to and including a)
- `P(X > a)` = `1 - P(X <= a)`
- `P(a < X <= b)` = `F(b) - F(a)` = `sum_{a < x <= b} p(x)`
- `P(X >= a)` = `1 - P(X < a)` = `sum_{x >= a} p(x)`

#### Worked Example 1

The PMF of a random variable X is given by `p(x) = (x+1)/10` for x = 0, 1, 2, 3.

(a) Verify it is a valid PMF.
(b) Find `P(X <= 1)`.
(c) Find `P(X > 2)`.
(d) Find `P(0 < X <= 2)`.

Solution:

(a) Check conditions:
- `p(0) = 1/10`, `p(1) = 2/10`, `p(2) = 3/10`, `p(3) = 4/10`. All are >= 0.
- Sum = `1/10 + 2/10 + 3/10 + 4/10 = 10/10 = 1`. Valid.

(b) `P(X <= 1) = p(0) + p(1) = 1/10 + 2/10 = 3/10 = 0.3`

(c) `P(X > 2) = P(X = 3) = 4/10 = 0.4`

(d) `P(0 < X <= 2) = p(1) + p(2) = 2/10 + 3/10 = 5/10 = 0.5`

#### Worked Example 2

For the PMF `p(x) = k/x` for x = 1, 2, 3, find k and compute `P(X >= 2)`.

Solution:
- Sum condition: `sum_{x=1}^{3} k/x = k(1 + 1/2 + 1/3) = k(11/6) = 1` => `k = 6/11`
- `P(X >= 2) = p(2) + p(3) = k/2 + k/3 = k(1/2 + 1/3) = (6/11)(5/6) = 5/11`

---

### 4. Finding Mean (Expected Value) from PMF

The **mean** or **expected value** of a discrete random variable X with PMF p(x) is:

`mu = E[X] = sum_{x} x * p(x)`

The mean is a weighted average of all possible values, weighted by their probabilities. It represents the long-run average value of X if the experiment is repeated many times.

#### Worked Example 3

Find the mean of X with PMF: `p(0) = 0.1`, `p(1) = 0.3`, `p(2) = 0.4`, `p(3) = 0.2`.

Solution:
`E[X] = 0*(0.1) + 1*(0.3) + 2*(0.4) + 3*(0.2)`
`E[X] = 0 + 0.3 + 0.8 + 0.6 = 1.7`

So the mean of X is 1.7.

---

### 5. Finding Variance from PMF

The **variance** of a discrete random variable X measures the spread or dispersion of the distribution around the mean.

`Var(X) = sigma^2 = E[(X - mu)^2] = sum_{x} (x - mu)^2 * p(x)`

A computationally simpler formula:

`Var(X) = E[X^2] - (E[X])^2`

where `E[X^2] = sum_{x} x^2 * p(x)` is the second raw moment.

The **standard deviation** is `sigma = sqrt(Var(X))`.

#### Worked Example 4

For the same PMF in Example 3, find the variance.

Solution:
Step 1: Compute `E[X]` (already found) = 1.7

Step 2: Compute `E[X^2]`:
`E[X^2] = 0^2*(0.1) + 1^2*(0.3) + 2^2*(0.4) + 3^2*(0.2)`
`E[X^2] = 0 + 0.3 + 1.6 + 1.8 = 3.7`

Step 3: Compute variance:
`Var(X) = E[X^2] - (E[X])^2 = 3.7 - (1.7)^2 = 3.7 - 2.89 = 0.81`

The standard deviation is `sigma = sqrt(0.81) = 0.9`.

---

### 6. Worked Example: Distribution of Sum of Two Dice

Let X = sum of numbers when two fair six-sided dice are rolled.

**Step 1: Find the PMF**

| x | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|----|----|----|----|----|----|----|----|-----|-----|-----|
| p(x) | 1/36 | 2/36 | 3/36 | 4/36 | 5/36 | 6/36 | 5/36 | 4/36 | 3/36 | 2/36 | 1/36 |

Verification: sum of probabilities = 1.

**Step 2: Compute the Mean**

`E[X] = sum_{x=2}^{12} x * p(x)`
`= 2(1/36) + 3(2/36) + 4(3/36) + 5(4/36) + 6(5/36) + 7(6/36) + 8(5/36) + 9(4/36) + 10(3/36) + 11(2/36) + 12(1/36)`
`= (2 + 6 + 12 + 20 + 30 + 42 + 40 + 36 + 30 + 22 + 12)/36`
`= 252/36 = 7`

The expected sum of two dice is 7.

**Step 3: Compute the Variance**

First find `E[X^2]`:
`E[X^2] = sum_{x=2}^{12} x^2 * p(x)`
`= 4(1/36) + 9(2/36) + 16(3/36) + 25(4/36) + 36(5/36) + 49(6/36) + 64(5/36) + 81(4/36) + 100(3/36) + 121(2/36) + 144(1/36)`
`= (4 + 18 + 48 + 100 + 180 + 294 + 320 + 324 + 300 + 242 + 144)/36`
`= 1974/36 = 54.8333...`

`Var(X) = E[X^2] - (E[X])^2 = 1974/36 - (7)^2 = 1974/36 - 49`
`= 1974/36 - 1764/36 = 210/36 = 35/6 ≈ 5.8333`

Standard deviation: `sigma = sqrt(35/6) ≈ 2.415`

---

### 7. Step-by-Step Procedure for Analyzing a Discrete Distribution

1. List all possible values x that X can take.
2. Assign probability p(x) to each value (ensuring sum = 1 and each p(x) >= 0).
3. Compute mean: `mu = sum x * p(x)`.
4. Compute `E[X^2] = sum x^2 * p(x)`.
5. Compute variance: `sigma^2 = E[X^2] - mu^2`.
6. Compute standard deviation: `sigma = sqrt(sigma^2)`.

---

### 8. Properties of Mean and Variance

- If c is a constant: `E[c] = c`, `Var(c) = 0`
- If a and b are constants: `E[aX + b] = aE[X] + b`, `Var(aX + b) = a^2 Var(X)`
- These properties are useful for scaling and shifting distributions.

---

## Practice Problems

1. A discrete random variable X has PMF: `p(x) = cx` for x = 1, 2, 3, 4, 5. Find c, the mean, and variance of X.

2. A random variable X takes values 0, 1, 2, 3 with probabilities 0.2, 0.3, 0.4, 0.1 respectively. Find `E[X]`, `E[X^2]`, and `Var(X)`.

3. In a game, a player rolls a fair die and wins rupees equal to the number shown. Find the expected winnings and variance per roll.

4. Let X be the number of heads when 4 fair coins are tossed. Find the PMF of X and compute the mean.

5. For the PMF `p(x) = (x+2)/k` for x = 0, 1, 2, 3, 4, find k, `P(X < 3)`, mean, and variance.

**Answers / Hints:**
1. `c(1+2+3+4+5) = 15c = 1` => `c = 1/15`. `E[X] = (1+4+9+16+25)/15 = 55/15 = 11/3`. `E[X^2] = (1+8+27+64+125)/15 = 225/15 = 15`. `Var = 15 - (11/3)^2 = 15 - 121/9 = 14/9`.
2. `E[X] = 0(0.2)+1(0.3)+2(0.4)+3(0.1) = 1.4`. `E[X^2] = 0+1(0.3)+4(0.4)+9(0.1) = 3`. `Var = 3 - 1.96 = 1.04`.
3. Each number 1-6 has P = 1/6. `E[X] = (1+2+3+4+5+6)/6 = 3.5`. `E[X^2] = (1+4+9+16+25+36)/6 = 91/6`. `Var = 91/6 - (3.5)^2 = 91/6 - 49/4 = 35/12`.
4. PMF: `P(X=x) = C(4,x)/16` for x = 0,1,2,3,4. `E[X] = 4 * 0.5 = 2`.
5. `k = (0+2)+(1+2)+(2+2)+(3+2)+(4+2) = 20` => `k = 20`. `P(X<3) = (2+3+4)/20 = 9/20`. `E[X] = (0*2+1*3+2*4+3*5+4*6)/20 = 50/20 = 2.5`. `E[X^2] = (0*2+1*3+4*4+9*5+16*6)/20 = 160/20 = 8`. `Var = 8 - 6.25 = 1.75`.
