# Expectation, Mean, and Variance of Continous Distribution

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 7  
**Date:** 25-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Demonstration  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 6.3

## Notes

### 1. Expectation for Continuous Random Variables

For a continuous random variable X with PDF f(x), the **expected value** (or **mean**) is defined as:

`E[X] = int_{-infty}^{infty} x * f(x) dx`

This is the continuous analogue of the discrete sum. Instead of summing over point masses, we integrate over the density.

Intuition: The mean is the "center of mass" of the probability distribution.

#### Worked Example 1

Let X have PDF `f(x) = 2x` for `0 <= x <= 1`, and 0 otherwise. Find `E[X]`.

Solution:
`E[X] = int_{0}^{1} x * 2x dx = int_{0}^{1} 2x^2 dx = [2x^3/3]_{0}^{1} = 2/3`

So the mean is 2/3.

#### Worked Example 2

Let X have PDF `f(x) = 3e^{-3x}` for `x >= 0`. Find `E[X]`.

Solution:
`E[X] = int_{0}^{infty} x * 3e^{-3x} dx`

Using integration by parts: let `u = x`, `dv = 3e^{-3x}dx`
`du = dx`, `v = -e^{-3x}`

`int_{0}^{infty} 3x e^{-3x} dx = [-x e^{-3x}]_{0}^{infty} + int_{0}^{infty} e^{-3x} dx`
`= 0 + [e^{-3x}/(-3)]_{0}^{infty}`
`= 0 + 0 - (-1/3) = 1/3`

So `E[X] = 1/3`.

---

### 2. Expectation of a Function of X

If g(X) is a function of a continuous random variable X, then:

`E[g(X)] = int_{-infty}^{infty} g(x) * f(x) dx`

Important special cases:
- `E[X^2] = int x^2 * f(x) dx` (second moment)
- `E[X^n] = int x^n * f(x) dx` (n-th moment)
- `E[(X - mu)^2] = int (x - mu)^2 * f(x) dx` (variance)

#### Worked Example 3

For the PDF `f(x) = 2x` on [0, 1], find `E[X^2]`.

Solution:
`E[X^2] = int_{0}^{1} x^2 * 2x dx = int_{0}^{1} 2x^3 dx = [x^4/2]_{0}^{1} = 1/2`

---

### 3. Properties of Expectation (Continuous)

The same properties hold as for discrete random variables:

1. **Linearity:** `E[aX + b] = aE[X] + b`
2. **Constant:** `E[c] = c`
3. **Sum:** `E[X + Y] = E[X] + E[Y]`
4. **Independence:** If X and Y are independent, `E[XY] = E[X]E[Y]`

#### Worked Example 4

If `E[X] = 2/3` (from Example 1), find `E[3X - 1]`.

Solution:
`E[3X - 1] = 3E[X] - 1 = 3(2/3) - 1 = 2 - 1 = 1`

---

### 4. Variance for Continuous Random Variables

The **variance** for a continuous random variable is defined as:

`Var(X) = E[(X - mu)^2]`

**Computational formula:**
`Var(X) = E[X^2] - (E[X])^2`

**Standard deviation:** `sigma = sqrt(Var(X))`

#### Worked Example 5

For `f(x) = 2x` on [0, 1], find `Var(X)`.

Solution:
From Examples 1 and 3:
`E[X] = 2/3`, `E[X^2] = 1/2`

`Var(X) = 1/2 - (2/3)^2 = 1/2 - 4/9 = 9/18 - 8/18 = 1/18`
`sigma = sqrt(1/18) = 1/(3*sqrt(2)) ≈ 0.2357`

#### Worked Example 6

For `f(x) = 3e^{-3x}` on [0, inf), find `Var(X)`.

Solution:
From Example 2: `E[X] = 1/3`

First find `E[X^2]`:
`E[X^2] = int_{0}^{infty} x^2 * 3e^{-3x} dx`

Using integration by parts twice:
Let `u = x^2`, `dv = 3e^{-3x}dx`
`du = 2x dx`, `v = -e^{-3x}`

`int 3x^2 e^{-3x} dx = [-x^2 e^{-3x}] + int 2x e^{-3x} dx`
First term at limits: 0 - 0 = 0.
`= 2 int x e^{-3x} dx`

Now `int x e^{-3x} dx`:
`u = x, dv = e^{-3x}dx`
`du = dx, v = -e^{-3x}/3`
`= [-x e^{-3x}/3] + int e^{-3x}/3 dx`
`= 0 + [-e^{-3x}/9]`
`= 0 - (-1/9) = 1/9`

So `int x e^{-3x} dx = 1/9`

Thus `E[X^2] = 3 * 2 * (1/9) = 6/9 = 2/3`

`Var(X) = 2/3 - (1/3)^2 = 2/3 - 1/9 = 6/9 - 1/9 = 5/9`

---

### 5. Properties of Variance (Continuous)

1. `Var(X) >= 0`
2. `Var(c) = 0` (constant has zero variance)
3. `Var(aX + b) = a^2 Var(X)`
4. `Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)`
5. If X and Y are independent: `Var(X + Y) = Var(X) + Var(Y)`

---

### 6. Step-by-Step Procedure

To find mean and variance of a continuous distribution:

1. Verify PDF: check `f(x) >= 0` and `int f(x)dx = 1`.
2. Compute mean: `mu = int x * f(x) dx`.
3. Compute `E[X^2] = int x^2 * f(x) dx`.
4. Compute variance: `Var(X) = E[X^2] - mu^2`.

---

### 7. Worked Example 7 (Comprehensive)

Let X have PDF `f(x) = 3x^2` for `0 <= x <= 1`.

(a) Find the mean.
(b) Find the variance.
(c) Find `E[5X + 2]`.
(d) Find `Var(5X + 2)`.

Solution:
(a) `E[X] = int_{0}^{1} x * 3x^2 dx = int_{0}^{1} 3x^3 dx = [3x^4/4]_{0}^{1} = 3/4`

(b) `E[X^2] = int_{0}^{1} x^2 * 3x^2 dx = int_{0}^{1} 3x^4 dx = [3x^5/5]_{0}^{1} = 3/5`
`Var(X) = 3/5 - (3/4)^2 = 3/5 - 9/16 = 48/80 - 45/80 = 3/80`

(c) `E[5X + 2] = 5 * 3/4 + 2 = 15/4 + 2 = 23/4 = 5.75`

(d) `Var(5X + 2) = 25 * Var(X) = 25 * 3/80 = 75/80 = 15/16`

---

### 8. Comparison: Discrete vs Continuous Formulas

| Quantity | Discrete | Continuous |
|----------|----------|------------|
| Mean | `sum x * p(x)` | `int x * f(x) dx` |
| E[g(X)] | `sum g(x) * p(x)` | `int g(x) * f(x) dx` |
| Variance | `E[X^2] - (E[X])^2` | `E[X^2] - (E[X])^2` |
| Properties | Same | Same |

The formulas are analogous, with sums replaced by integrals.

---

## Practice Problems

1. Let X have PDF `f(x) = 2(1-x)` for `0 <= x <= 1`. Find `E[X]` and `Var(X)`.

   <details>
   <summary>Show Answer</summary>
   1. `E[X] = int_0^1 2x(1-x)dx = 1/3`. `E[X^2] = int_0^1 2x^2(1-x)dx = 1/6`. `Var = 1/6 - 1/9 = 1/18`.
   </details>

2. Let X have PDF `f(x) = (3/8)(x+1)^2` for `-1 <= x <= 1`. Find the mean and variance.

   <details>
   <summary>Show Answer</summary>
   2. `E[X] = 0` (by symmetry). `E[X^2] = int_{-1}^1 x^2(3/8)(x+1)^2 dx = 1/5`. `Var = 1/5`.
   </details>

3. Let X have PDF `f(x) = 4x^3` for `0 <= x <= 1`. Find `E[2X - 3]` and `Var(2X - 3)`.

   <details>
   <summary>Show Answer</summary>
   3. `E[X] = int_0^1 4x^4 dx = 4/5`. `E[2X-3] = 2(4/5)-3 = -7/5`. `E[X^2] = int_0^1 4x^5 dx = 2/3`. `Var(X) = 2/3 - 16/25 = 2/75`. `Var(2X-3) = 4 * 2/75 = 8/75`.
   </details>

4. The lifetime (in years) of a device has PDF `f(x) = 2e^{-2x}` for x >= 0. Find the mean lifetime and variance.

   <details>
   <summary>Show Answer</summary>
   4. `E[X] = 1/2` (mean of exponential). `E[X^2] = 2/4 = 1/2`. `Var = 1/2 - 1/4 = 1/4`.
   </details>

5. Let `f(x) = k/(1+x)^3` for x >= 0. Find k, then find E[X] and Var(X).
   <details>
   <summary>Show Answer</summary>
   5. `k int_0^{infty} 1/(1+x)^3 dx = k[-1/(2(1+x)^2)]_0^{infty} = k/2 = 1` => k=2. `E[X] = 1`. `E[X^2]` diverges, so Var(X) is infinite.
   </details>
