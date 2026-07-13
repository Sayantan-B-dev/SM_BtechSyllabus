# Expectation, Mean, and Variance of Joint Distribution

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 11  
**Date:** 03-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 4.14

## Notes

### 1. Conditional Expectation: Definition

The **conditional expectation** of X given Y = y is the expected value of X computed using the conditional distribution of X given Y = y.

**Discrete case:**
`E[X | Y = y] = sum_{x} x * P(X = x | Y = y) = sum_{x} x * (p(x, y) / p_Y(y))`

**Continuous case:**
`E[X | Y = y] = int_{-infty}^{infty} x * f_{X|Y}(x | y) dx`

where `f_{X|Y}(x | y) = f(x, y) / f_Y(y)` is the conditional PDF.

Note: `E[X | Y = y]` is a function of y (a number for each specific y). As a random variable, it depends on Y, so `E[X | Y]` is itself a random variable.

#### Worked Example 1 (Discrete Conditional Expectation)

Using the joint PMF from L10 Example 1:

| X\Y | 1 | 2 | 3 |
|-----|---|---|---|
| 0   | 0.1 | 0.1 | 0.2 |
| 1   | 0.2 | 0.3 | 0.1 |

Find `E[X | Y = 1]` and `E[X | Y = 2]`.

Solution:
Marginal of Y: `P(Y=1)=0.3`, `P(Y=2)=0.4`, `P(Y=3)=0.3`

Conditional PMF of X given Y = 1:
`P(X=0 | Y=1) = p(0,1)/P(Y=1) = 0.1/0.3 = 1/3`
`P(X=1 | Y=1) = 0.2/0.3 = 2/3`
`E[X | Y=1] = 0*(1/3) + 1*(2/3) = 2/3`

Conditional PMF of X given Y = 2:
`P(X=0 | Y=2) = 0.1/0.4 = 1/4`
`P(X=1 | Y=2) = 0.3/0.4 = 3/4`
`E[X | Y=2] = 0*(1/4) + 1*(3/4) = 3/4`

So `E[X | Y=1] = 2/3`, `E[X | Y=2] = 3/4`. Also compute `E[X | Y=3]`:
`P(X=0 | Y=3) = 0.2/0.3 = 2/3`
`P(X=1 | Y=3) = 0.1/0.3 = 1/3`
`E[X | Y=3] = 0*(2/3) + 1*(1/3) = 1/3`

---

### 2. Conditional Expectation as a Random Variable

Since `E[X | Y]` is a function of Y, it is a random variable. If Y takes values y_1, y_2, ..., then `E[X | Y]` takes values `E[X | Y = y_i]` with probabilities `P(Y = y_i)`.

From Example 1:
`E[X | Y]` takes values: 2/3 (when Y=1, prob 0.3), 3/4 (when Y=2, prob 0.4), 1/3 (when Y=3, prob 0.3).

#### Worked Example 2 (Continuous Conditional Expectation)

Joint PDF: `f(x, y) = 6x^2 y` for `0 <= x <= 1, 0 <= y <= 1`. Find `E[X | Y = 0.5]`.

Solution:
Marginal of Y: `f_Y(y) = int_{0}^{1} 6x^2 y dx = 6y * [x^3/3]_{0}^{1} = 6y * (1/3) = 2y` for `0 <= y <= 1`

Conditional PDF of X given Y = y:
`f_{X|Y}(x | y) = f(x, y) / f_Y(y) = (6x^2 y) / (2y) = 3x^2` for `0 <= x <= 1`

Note: `f_{X|Y}(x | y) = 3x^2` does not depend on y! This means X is independent of Y.

`E[X | Y = 0.5] = int_{0}^{1} x * 3x^2 dx = int_{0}^{1} 3x^3 dx = [3x^4/4]_{0}^{1} = 3/4`

Since X is independent of Y, `E[X | Y = y] = E[X] = 3/4` for all y.

---

### 3. Conditional Variance

The **conditional variance** of X given Y = y is:

`Var(X | Y = y) = E[(X - E[X|Y=y])^2 | Y = y]`

Computational formula:
`Var(X | Y = y) = E[X^2 | Y = y] - (E[X | Y = y])^2`

Like conditional expectation, `Var(X | Y)` is a random variable (function of Y).

#### Worked Example 3

From Example 1, find `Var(X | Y = 1)` and `Var(X | Y = 2)`.

Solution:
For Y = 1: `E[X | Y=1] = 2/3`
`E[X^2 | Y=1] = sum x^2 * P(X=x|Y=1) = 0^2*(1/3) + 1^2*(2/3) = 2/3`
`Var(X | Y=1) = 2/3 - (2/3)^2 = 2/3 - 4/9 = 6/9 - 4/9 = 2/9`

For Y = 2: `E[X | Y=2] = 3/4`
`E[X^2 | Y=2] = 0^2*(1/4) + 1^2*(3/4) = 3/4`
`Var(X | Y=2) = 3/4 - (3/4)^2 = 3/4 - 9/16 = 12/16 - 9/16 = 3/16`

---

### 4. Law of Total Expectation

The **law of total expectation** (also called the law of iterated expectations or the tower property):

`E[X] = E[E[X | Y]]`

This means: the expected value of X equals the expected value of the conditional expectation of X given Y.

Proof for discrete case:
`E[E[X | Y]] = sum_{y} E[X | Y = y] * P(Y = y)`
`= sum_{y} [sum_{x} x * P(X = x | Y = y)] * P(Y = y)`
`= sum_{y} sum_{x} x * P(X = x, Y = y)`
`= sum_{x} x * sum_{y} P(X = x, Y = y)`
`= sum_{x} x * P(X = x) = E[X]`

#### Worked Example 4

From Example 1, verify the law of total expectation.

Solution:
`E[X | Y = 1] = 2/3`, `E[X | Y = 2] = 3/4`, `E[X | Y = 3] = 1/3`
`P(Y = 1) = 0.3`, `P(Y = 2) = 0.4`, `P(Y = 3) = 0.3`

`E[E[X | Y]] = (2/3)(0.3) + (3/4)(0.4) + (1/3)(0.3)`
`= 0.2 + 0.3 + 0.1 = 0.6`

From L10 Example 1: `E[X] = 0.6`. Verified. `E[X] = E[E[X | Y]]`.

---

### 5. Law of Total Variance

The **law of total variance** (also called the Eve's law):

`Var(X) = E[Var(X | Y)] + Var(E[X | Y])`

This decomposes the total variance into two components:
- **Within-group variance:** `E[Var(X | Y)]` = average of conditional variances
- **Between-group variance:** `Var(E[X | Y])` = variance of conditional means

#### Worked Example 5

From Example 1 and 3, verify the law of total variance.

Solution:
Step 1: Compute `E[Var(X | Y)]`
`Var(X | Y=1) = 2/9`, `Var(X | Y=2) = 3/16`, `Var(X | Y=3) = ?`

For Y = 3: `P(X=0|Y=3)=2/3`, `P(X=1|Y=3)=1/3`
`E[X|Y=3] = 1/3`
`E[X^2|Y=3] = 0^2*(2/3) + 1^2*(1/3) = 1/3`
`Var(X|Y=3) = 1/3 - (1/3)^2 = 1/3 - 1/9 = 2/9`

`E[Var(X|Y)] = (2/9)(0.3) + (3/16)(0.4) + (2/9)(0.3)`
`= 0.0667 + 0.075 + 0.0667 = 0.2084` (approx)

Step 2: Compute `Var(E[X | Y])`
`E[X|Y]` takes values 2/3, 3/4, 1/3 with probabilities 0.3, 0.4, 0.3.
`E[E[X|Y]] = 0.6` (the overall mean)

`E[(E[X|Y])^2] = (2/3)^2(0.3) + (3/4)^2(0.4) + (1/3)^2(0.3)`
`= (4/9)(0.3) + (9/16)(0.4) + (1/9)(0.3)`
`= 0.1333 + 0.225 + 0.0333 = 0.3916`

`Var(E[X|Y]) = 0.3916 - (0.6)^2 = 0.3916 - 0.36 = 0.0316`

Step 3: Total
`Var(X) = 0.2084 + 0.0316 = 0.24`

Check directly from L10: `Var(X) = 0.24`. Verified.

---

### 6. Applications of the Laws

**Prediction:** The conditional expectation `E[X | Y]` is the best predictor of X given Y (minimizing mean squared error).

**Variance decomposition:** The law of total variance helps analyze how much of the variability in X is explained by Y versus within-group variability.

---

### 7. Summary Table

| Concept | Formula | Meaning |
|---------|---------|---------|
| Conditional expectation | `E[X | Y = y]` | Expected X given Y = y |
| Conditional variance | `Var(X | Y = y) = E[X^2|Y=y] - (E[X|Y=y])^2` | Variance of X given Y = y |
| Law of total expectation | `E[X] = E[E[X | Y]]` | Unconditional = expectation of conditional |
| Law of total variance | `Var(X) = E[Var(X|Y)] + Var(E[X|Y])` | Total variance = within + between |

---

### 8. Worked Example 6 (Comprehensive)

Joint PDF: `f(x, y) = 8xy` for `0 < x < y < 1`.

Find `E[X | Y = y]`, `E[X]` using total expectation, and `Var(X)` using total variance.

Solution:
Marginal of Y: `f_Y(y) = int_{0}^{y} 8xy dx = 8y * [x^2/2]_{0}^{y} = 4y^3` for `0 < y < 1`

Conditional PDF of X given Y = y:
`f_{X|Y}(x|y) = (8xy)/(4y^3) = 2x/y^2` for `0 < x < y`

`E[X | Y = y] = int_{0}^{y} x * (2x/y^2) dx = (2/y^2) int_{0}^{y} x^2 dx = (2/y^2)[y^3/3] = 2y/3`

`E[X] = E[E[X|Y]] = int_{0}^{1} (2y/3) * 4y^3 dy = (8/3) int_{0}^{1} y^4 dy = (8/3)[y^5/5]_{0}^{1} = (8/3)(1/5) = 8/15`

`E[X^2 | Y = y] = int_{0}^{y} x^2 * (2x/y^2) dx = (2/y^2) int_{0}^{y} x^3 dx = (2/y^2)[y^4/4] = y^2/2`

`Var(X|Y=y) = y^2/2 - (2y/3)^2 = y^2/2 - 4y^2/9 = (9y^2 - 8y^2)/18 = y^2/18`

`E[Var(X|Y)] = int_{0}^{1} (y^2/18) * 4y^3 dy = (4/18) int_{0}^{1} y^5 dy = (2/9)[y^6/6]_{0}^{1} = 2/(54) = 1/27`

`Var(E[X|Y]) = Var(2Y/3) = (4/9) Var(Y)`
`E[Y] = int_{0}^{1} y * 4y^3 dy = 4 int_{0}^{1} y^4 dy = 4/5`
`E[Y^2] = int_{0}^{1} y^2 * 4y^3 dy = 4 int_{0}^{1} y^5 dy = 4/6 = 2/3`
`Var(Y) = 2/3 - (4/5)^2 = 2/3 - 16/25 = 50/75 - 48/75 = 2/75`
`Var(E[X|Y]) = (4/9)*(2/75) = 8/675`

`Var(X) = 1/27 + 8/675 = 25/675 + 8/675 = 33/675`

---

## Practice Problems

1. Joint PMF:

| X\Y | 0 | 1 | 2 |
|-----|---|---|---|
| 0   | 0.1 | 0.2 | 0.1 |
| 1   | 0.2 | 0.1 | 0.1 |
| 2   | 0.1 | 0.1 | 0.0 |

Find `E[Y | X = 0]`, `E[Y | X = 1]`, and `E[Y]` using the law of total expectation.

2. If `E[X | Y] = 2Y + 1` and `E[Y] = 3`, find `E[X]`.

3. If `Var(X | Y) = Y` and `E[X | Y] = 3Y - 2`, and `E[Y] = 2`, `Var(Y) = 4`, find `Var(X)` using the law of total variance.

4. Joint PDF: `f(x, y) = 8x^3 y` for `0 < x < 1, 0 < y < 1/x`. Find `E[Y | X = x]` and `E[Y]`.

5. Show that `Var(X) = E[Var(X | Y)] + Var(E[X | Y])` (proof in outline form).

**Answers / Hints:**
1. `P(X=0)=0.4`. `P(Y|X=0): P(Y=0)=0.1/0.4=0.25, P(Y=1)=0.2/0.4=0.5, P(Y=2)=0.1/0.4=0.25`. `E[Y|X=0]=0(0.25)+1(0.5)+2(0.25)=1.0`. `E[Y|X=1]: P(Y=0)=0.2/0.4=0.5, P(Y=1)=0.1/0.4=0.25, P(Y=2)=0.1/0.4=0.25`. `E[Y|X=1]=0(0.5)+1(0.25)+2(0.25)=0.75`. `E[Y] = E[E[Y|X]] = 1.0(0.4)+0.75(0.4)+?`. Need `E[Y|X=2]`: `P(Y=0|X=2)=0.1/0.2=0.5, P(Y=1)=0.1/0.2=0.5`. `E[Y|X=2]=0.5`. `E[Y] = 1.0(0.4)+0.75(0.4)+0.5(0.2) = 0.4+0.3+0.1 = 0.8`.
2. `E[X] = E[E[X|Y]] = E[2Y+1] = 2E[Y] + 1 = 2(3) + 1 = 7`.
3. `E[Var(X|Y)] = E[Y] = 2`. `Var(E[X|Y]) = Var(3Y-2) = 9 Var(Y) = 36`. `Var(X) = 2 + 36 = 38`.
4. `f_Y(y)` is complicated, but `E[Y] = E[E[Y|X]]`. Find marginal of X: `f_X(x) = int_0^{1/x} 8x^3 y dy = 8x^3 [y^2/2]_0^{1/x} = 4x`. `E[Y|X=x] = int_0^{1/x} y * (8x^3 y / (4x)) dy = int_0^{1/x} 2x^2 y^2 dy = 2x^2 [y^3/3]_0^{1/x} = 2/(3x)`. `E[Y] = int_0^1 (2/(3x)) * 4x dx = 8/3 int_0^1 1 dx = 8/3`.
5. `Var(X) = E[X^2] - (E[X])^2 = E[E[X^2|Y]] - (E[E[X|Y]])^2`. Then `E[X^2|Y] = Var(X|Y) + (E[X|Y])^2`. Substituting: `Var(X) = E[Var(X|Y)] + E[(E[X|Y])^2] - (E[E[X|Y]])^2 = E[Var(X|Y)] + Var(E[X|Y])`.
