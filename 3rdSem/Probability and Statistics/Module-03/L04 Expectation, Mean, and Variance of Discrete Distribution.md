# Expectation, Mean, and Variance of Discrete Distribution

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 4  
**Date:** 18-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 6.3

## Notes

### 1. Definition of Expectation E[X]

The **expected value** (or **mean**) of a discrete random variable X with PMF `p(x)` is defined as:

`E[X] = sum_{x} x * p(x)`

This is a weighted average of all possible values of X, where each value is weighted by its probability.

Interpretation: If the random experiment is repeated many times, the average of the observed values will be close to `E[X]`. It is the long-run average value.

Notation: `E[X]`, `mu`, `mu_X`, or `mu_X`.

#### Worked Example 1

A random variable X has PMF: `P(X = 0) = 0.2`, `P(X = 1) = 0.5`, `P(X = 2) = 0.3`. Find `E[X]`.

Solution:
`E[X] = 0 * 0.2 + 1 * 0.5 + 2 * 0.3 = 0 + 0.5 + 0.6 = 1.1`

#### Worked Example 2

Find the expected value of X where X = number on a fair die.

Solution:
X takes values 1, 2, 3, 4, 5, 6, each with probability 1/6.
`E[X] = 1*(1/6) + 2*(1/6) + 3*(1/6) + 4*(1/6) + 5*(1/6) + 6*(1/6)`
`= (1+2+3+4+5+6)/6 = 21/6 = 3.5`

---

### 2. Expectation of a Function of X

If g(X) is a function of X, then:

`E[g(X)] = sum_{x} g(x) * p(x)`

This is a crucial generalization. Important special cases:

- `E[X^2] = sum x^2 * p(x)` (second moment)
- `E[X^n] = sum x^n * p(x)` (n-th moment)
- `E[(X - mu)^2] = sum (x - mu)^2 * p(x)` (variance)

---

### 3. Properties of Expectation

Let X and Y be random variables, and a, b, c be constants.

1. **Linearity:** `E[aX + b] = aE[X] + b`
   - `E[X + Y] = E[X] + E[Y]`
   - `E[aX] = aE[X]`
   - `E[X + c] = E[X] + c`

2. **Constant:** `E[c] = c`

3. **If X >= 0, then E[X] >= 0**

4. **If X and Y are independent, then E[XY] = E[X]E[Y]**

#### Worked Example 3 (Using Properties)

If `E[X] = 5`, find `E[3X + 2]`.

Solution:
`E[3X + 2] = 3E[X] + 2 = 3(5) + 2 = 17`

#### Worked Example 4

From the die example, compute `E[X^2]` and use the linearity property.

`E[X^2] = 1^2*(1/6) + 2^2*(1/6) + ... + 6^2*(1/6)`
`= (1+4+9+16+25+36)/6 = 91/6`

Now, let `Y = 2X + 3`. Find `E[Y]`.
`E[Y] = E[2X + 3] = 2E[X] + 3 = 2(3.5) + 3 = 10`

---

### 4. Variance Definition

The **variance** of a random variable X measures the spread of the distribution around its mean.

`Var(X) = E[(X - mu)^2]` where `mu = E[X]`

**Computational formula (much easier for calculations):**

`Var(X) = E[X^2] - (E[X])^2`

Standard deviation: `sigma = sqrt(Var(X))`

Both variance and standard deviation measure dispersion. Variance is in squared units, while standard deviation is in the original units of X.

#### Worked Example 5

Find the variance of the random variable in Example 1.

Solution:
`E[X] = 1.1` (from Example 1)
`E[X^2] = 0^2 * 0.2 + 1^2 * 0.5 + 2^2 * 0.3 = 0 + 0.5 + 1.2 = 1.7`
`Var(X) = E[X^2] - (E[X])^2 = 1.7 - (1.1)^2 = 1.7 - 1.21 = 0.49`
`sigma = sqrt(0.49) = 0.7`

---

### 5. Properties of Variance

1. `Var(X) >= 0` (variance is always non-negative)
2. `Var(c) = 0` where c is a constant
3. `Var(aX + b) = a^2 Var(X)` (shift does not affect variance, scaling does)
4. `Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)`
5. If X and Y are independent, `Var(X + Y) = Var(X) + Var(Y)`
6. `Var(X) = E[X^2] - (E[X])^2`

#### Worked Example 6 (Using Variance Properties)

If `Var(X) = 4`, find `Var(2X - 5)`.

Solution:
`Var(2X - 5) = 2^2 Var(X) = 4 * 4 = 16`

#### Worked Example 7 (Comprehensive)

Let X have PMF: `P(X = -2) = 0.2`, `P(X = 0) = 0.3`, `P(X = 1) = 0.4`, `P(X = 3) = 0.1`.

Compute `E[X]`, `E[X^2]`, and `Var(X)`.

Solution:
`E[X] = (-2)(0.2) + 0(0.3) + 1(0.4) + 3(0.1) = -0.4 + 0 + 0.4 + 0.3 = 0.3`
`E[X^2] = 4(0.2) + 0(0.3) + 1(0.4) + 9(0.1) = 0.8 + 0 + 0.4 + 0.9 = 2.1`
`Var(X) = 2.1 - (0.3)^2 = 2.1 - 0.09 = 2.01`
`sigma = sqrt(2.01) approx 1.418`

---

### 6. Step-by-Step Procedure

To compute the mean and variance of any discrete distribution:

1. Verify the PMF is valid (all p(x) >= 0, sum p(x) = 1).
2. Compute `mu = E[X] = sum x * p(x)`.
3. Compute `E[X^2] = sum x^2 * p(x)`.
4. Compute `Var(X) = E[X^2] - mu^2`.
5. Compute `sigma = sqrt(Var(X))`.

---

### 7. Comparison: Mean vs Variance

| Property | Mean (mu) | Variance (sigma^2) |
|----------|-----------|---------------------|
| Definition | Central value | Spread around mean |
| Formula | `sum x p(x)` | `E[X^2] - (E[X])^2` |
| Units | Same as X | Squared units of X |
| Effect of constant shift | Shifted by same amount | Unchanged |
| Effect of scaling | Scaled by same factor | Scaled by square of factor |
| Range | Can be negative | Always >= 0 |

---

## Practice Problems

1. X has PMF: `P(X=1) = 0.2`, `P(X=2) = 0.3`, `P(X=3) = 0.4`, `P(X=4) = 0.1`. Find `E[X]`, `E[X^2]`, and `Var(X)`.

   <details>
   <summary>Show Answer</summary>
   1. `E[X] = 1(0.2)+2(0.3)+3(0.4)+4(0.1) = 2.4`. `E[X^2] = 1(0.2)+4(0.3)+9(0.4)+16(0.1) = 6.6`. `Var = 6.6 - 5.76 = 0.84`.
   </details>

2. If `E[X] = 2` and `E[X^2] = 6`, find `Var(X)` and `E[3X - 4]`.

   <details>
   <summary>Show Answer</summary>
   2. `Var(X) = 6 - 4 = 2`. `E[3X - 4] = 3(2) - 4 = 2`.
   </details>

3. A random variable X takes values -1, 0, 2, 5 with probabilities 0.1, 0.3, 0.4, 0.2. Find `E[X]` and `Var(X)`.

   <details>
   <summary>Show Answer</summary>
   3. `E[X] = -0.1+0+0.8+1.0 = 1.7`. `E[X^2] = 0.1+0+1.6+5.0 = 6.7`. `Var = 6.7 - 2.89 = 3.81`.
   </details>

4. For a fair die, let `Y = 3X + 1` where X is the number rolled. Find `E[Y]` and `Var(Y)` using properties (use known E[X] and Var(X) from earlier examples).

   <details>
   <summary>Show Answer</summary>
   4. `E[Y] = 3(3.5)+1 = 11.5`. `Var(Y) = 9 * Var(X) = 9 * (35/12) = 105/4 = 26.25`.
   </details>

5. If `Var(X) = 9` and `Var(Y) = 16` and X, Y are independent, find `Var(2X - 3Y + 5)`.
   <details>
   <summary>Show Answer</summary>
   5. `Var(2X - 3Y + 5) = 4 Var(X) + 9 Var(Y) = 4(9) + 9(16) = 36 + 144 = 180`.
   </details>
