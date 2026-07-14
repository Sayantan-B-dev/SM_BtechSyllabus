# Expectation, Mean, and Variance of Joint Distribution

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 10  
**Date:** 01-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Case Studies  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 4.14

## Notes

### 1. Expectation for Joint Distributions

For two random variables X and Y, the expectation of a function g(X, Y) is:

**Discrete case (joint PMF p(x, y)):**
`E[g(X, Y)] = sum_{x} sum_{y} g(x, y) * p(x, y)`

**Continuous case (joint PDF f(x, y)):**
`E[g(X, Y)] = int_{-infty}^{infty} int_{-infty}^{infty} g(x, y) * f(x, y) dx dy`

#### Worked Example 1 (Discrete)

Joint PMF of X and Y:

| X\Y | 1 | 2 | 3 |
|-----|---|---|---|
| 0   | 0.1 | 0.1 | 0.2 |
| 1   | 0.2 | 0.3 | 0.1 |

Find `E[X]`, `E[Y]`, and `E[XY]`.

Solution:
First find marginal PMFs:

Marginal of X:
`P(X=0) = 0.1 + 0.1 + 0.2 = 0.4`
`P(X=1) = 0.2 + 0.3 + 0.1 = 0.6`

Marginal of Y:
`P(Y=1) = 0.1 + 0.2 = 0.3`
`P(Y=2) = 0.1 + 0.3 = 0.4`
`P(Y=3) = 0.2 + 0.1 = 0.3`

`E[X] = 0(0.4) + 1(0.6) = 0.6`
`E[Y] = 1(0.3) + 2(0.4) + 3(0.3) = 0.3 + 0.8 + 0.9 = 2.0`
`E[XY] = sum sum (x*y) * p(x,y)`
`= 0*1*0.1 + 0*2*0.1 + 0*3*0.2 + 1*1*0.2 + 1*2*0.3 + 1*3*0.1`
`= 0 + 0 + 0 + 0.2 + 0.6 + 0.3 = 1.1`

---

### 2. Properties of Expectation for Joint Distributions

1. `E[X + Y] = E[X] + E[Y]` (always true, no independence needed)
2. `E[aX + bY] = aE[X] + bE[Y]`
3. `E[XY] = E[X]E[Y]` if X and Y are independent
4. `E[X]` from joint distribution equals `E[X]` from marginal distribution

---

### 3. Covariance: Definition

**Covariance** measures the linear relationship between two random variables:

`Cov(X, Y) = E[(X - mu_X)(Y - mu_Y)]`

**Computational formula:**
`Cov(X, Y) = E[XY] - E[X]E[Y]`

**Interpretation:**
- `Cov(X, Y) > 0`: X and Y tend to move in the same direction (positive relationship)
- `Cov(X, Y) < 0`: X and Y tend to move in opposite directions (negative relationship)
- `Cov(X, Y) = 0`: No linear relationship (but they could still be dependent nonlinearly)

#### Worked Example 2

From Example 1, compute Cov(X, Y).

Solution:
`E[X] = 0.6`, `E[Y] = 2.0`, `E[XY] = 1.1`
`Cov(X, Y) = 1.1 - (0.6)(2.0) = 1.1 - 1.2 = -0.1`

The negative covariance indicates a slight negative linear relationship.

---

### 4. Properties of Covariance

1. `Cov(X, X) = Var(X)`
2. `Cov(X, Y) = Cov(Y, X)` (symmetric)
3. `Cov(aX + b, cY + d) = ac * Cov(X, Y)`
4. `Cov(X + Y, Z) = Cov(X, Z) + Cov(Y, Z)`
5. `Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)`
6. `Var(X - Y) = Var(X) + Var(Y) - 2Cov(X, Y)`
7. If X and Y are independent, `Cov(X, Y) = 0` (but converse is not necessarily true)

---

### 5. Correlation Coefficient

The **Pearson correlation coefficient** is a standardized measure of linear relationship:

`rho_{XY} = Corr(X, Y) = Cov(X, Y) / (sigma_X * sigma_Y)`

Properties:
- `-1 <= rho <= 1`
- `rho = 1`: perfect positive linear correlation
- `rho = -1`: perfect negative linear correlation
- `rho = 0`: no linear correlation
- `rho` is unitless (unlike covariance)

#### Worked Example 3

From Example 1, find the correlation coefficient. (Assume `Var(X) = 0.24` and `Var(Y) = 0.6`.)

Solution:
`sigma_X = sqrt(0.24) ≈ 0.4899`
`sigma_Y = sqrt(0.6) ≈ 0.7746`
`Cov(X, Y) = -0.1`
`rho = -0.1 / (0.4899 * 0.7746) ≈ -0.1 / 0.3795 ≈ -0.2635`

This indicates a weak negative correlation.

---

### 6. Worked Example 4 (Continuous Case)

Let X and Y have joint PDF `f(x, y) = 2` for `0 <= x <= 1, 0 <= y <= 1, x + y <= 1`.

Find `E[X]`, `E[Y]`, `E[XY]`, and `Cov(X, Y)`.

Solution:
The region is a triangle: x >= 0, y >= 0, x + y <= 1.

First, find marginal PDF of X:
`f_X(x) = int_{0}^{1-x} 2 dy = 2(1-x)` for `0 <= x <= 1`

`E[X] = int_{0}^{1} x * 2(1-x) dx = int_{0}^{1} (2x - 2x^2) dx`
`= [x^2 - 2x^3/3]_{0}^{1} = 1 - 2/3 = 1/3`

By symmetry: `E[Y] = 1/3`

`E[XY] = int_{0}^{1} int_{0}^{1-x} xy * 2 dy dx`
`= int_{0}^{1} 2x * [y^2/2]_{0}^{1-x} dx`
`= int_{0}^{1} x * (1-x)^2 dx`
`= int_{0}^{1} x(1 - 2x + x^2) dx`
`= int_{0}^{1} (x - 2x^2 + x^3) dx`
`= [x^2/2 - 2x^3/3 + x^4/4]_{0}^{1}`
`= 1/2 - 2/3 + 1/4 = 6/12 - 8/12 + 3/12 = 1/12`

`Cov(X, Y) = E[XY] - E[X]E[Y] = 1/12 - (1/3)(1/3) = 1/12 - 1/9 = 3/36 - 4/36 = -1/36`

---

### 7. Variance of Sum of Multiple Variables

For random variables `X_1, X_2, ..., X_n`:

`Var(X_1 + X_2 + ... + X_n) = sum_{i=1}^{n} Var(X_i) + 2 sum_{i < j} Cov(X_i, X_j)`

If all pairs are uncorrelated (Cov = 0), this simplifies to sum of variances.

---

### 8. Key Distinctions

| Quantity | Measures | Range | Units |
|----------|---------|-------|-------|
| Covariance | Direction of linear relationship | (-inf, inf) | Product of units |
| Correlation | Strength of linear relationship | [-1, 1] | Unitless |

---

## Practice Problems

1. Joint PMF:

| X\Y | 0 | 1 |
|-----|---|---|
| 0   | 0.2 | 0.3 |
| 1   | 0.4 | 0.1 |

Find `E[X]`, `E[Y]`, `E[XY]`, `Cov(X, Y)`, and `Corr(X, Y)`.

   <details>
   <summary>Show Answer</summary>
   1. `E[X] = 0.5`, `E[Y] = 0.4`, `E[XY] = 0.1`. `Cov = 0.1 - 0.5*0.4 = -0.1`. `Var(X) = 0.25`, `Var(Y)=0.24`. `Corr = -0.1/sqrt(0.06) = -0.408`.
   </details>

2. Joint PDF: `f(x, y) = 4xy` for `0 <= x <= 1, 0 <= y <= 1`. Find `E[X]`, `E[Y]`, `E[XY]`, and `Cov(X, Y)`. Are X and Y independent?

   <details>
   <summary>Show Answer</summary>
   2. `E[X] = int_0^1 int_0^1 x*4xy dy dx = 4/5`. By symmetry `E[Y]=4/5`. `E[XY] = int_0^1 int_0^1 4x^2 y^2 dy dx = 4/9`. `Cov = 4/9 - 16/25 = 100/225 - 144/225 = -44/225`. X and Y are independent since f(x,y) = (2x)(2y) = f_X(x)f_Y(y).
   </details>

3. If `Var(X) = 4`, `Var(Y) = 9`, and `Cov(X, Y) = -3`, find `Var(2X + Y)` and `Corr(X, Y)`.

   <details>
   <summary>Show Answer</summary>
   3. `Var(2X+Y) = 4Var(X) + Var(Y) + 4Cov(X,Y) = 16 + 9 + 4(-3) = 13`. `Corr = -3/(2*3) = -0.5`.
   </details>

4. The joint PMF of X and Y is: `p(x, y) = (x+y)/k` for x = 0, 1 and y = 0, 1, 2. Find k and Cov(X, Y).

   <details>
   <summary>Show Answer</summary>
   4. `k = sum sum (x+y) = (0+0)+(0+1)+(0+2)+(1+0)+(1+1)+(1+2) = 0+1+2+1+2+3 = 9`. `E[X] = 1/9 * (0+0+0+1+1+1) = 3/9 = 1/3`. `E[Y] = 1/9 * (0+1+2+0+1+2) = 6/9 = 2/3`. `E[XY] = 1/9 * (0+0+0+0+1+2) = 3/9 = 1/3`. `Cov = 1/3 - (1/3)(2/3) = 1/3 - 2/9 = 1/9`.
   </details>

5. If X and Y are independent, show that Cov(X, Y) = 0.
   <details>
   <summary>Show Answer</summary>
   5. `E[XY] = sum sum xy p(x,y) = sum sum xy p_X(x)p_Y(y) = (sum x p_X(x))(sum y p_Y(y)) = E[X]E[Y]`. So `Cov = E[X]E[Y] - E[X]E[Y] = 0`.
   </details>
