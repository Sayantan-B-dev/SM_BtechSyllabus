# Probability Distribution of Continuous random variables, Joint Distributions

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 3  
**Date:** 14-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 5.12

## Notes

### Part A: Continuous Probability Distributions

### 1. Continuous Random Variables

A continuous random variable X can take any value in an interval (or union of intervals) of real numbers. Unlike discrete variables, there are infinitely many uncountable values.

Examples: time between arrivals, weight of a product, temperature, voltage.

---

### 2. Probability Density Function (PDF)

For a continuous random variable X, the **probability density function (PDF)**, denoted `f(x)`, is a function that satisfies:

1. `f(x) >= 0` for all x in R.
2. `int_{-infty}^{infty} f(x) dx = 1` (total area under the curve = 1).
3. For any interval `[a, b]`:

`P(a <= X <= b) = int_{a}^{b} f(x) dx`

The probability that X falls in an interval is the **area under the PDF curve** over that interval.

Key point: `P(X = a) = int_{a}^{a} f(x) dx = 0` for any specific value a. This means the probability of any single point is zero.

---

### 3. Computing Probabilities as Area Under PDF

#### Worked Example 1

Let X have PDF `f(x) = 3x^2` for `0 <= x <= 1`, and 0 elsewhere.

Find: (a) `P(0 < X < 0.5)` (b) `P(X > 0.75)` (c) `P(0.2 <= X <= 0.4)`

Solution:

(a) `P(0 < X < 0.5) = int_{0}^{0.5} 3x^2 dx = [x^3]_{0}^{0.5} = (0.5)^3 - 0 = 0.125`

(b) `P(X > 0.75) = int_{0.75}^{1} 3x^2 dx = [x^3]_{0.75}^{1} = 1 - (0.75)^3 = 1 - 0.421875 = 0.578125`

(c) `P(0.2 <= X <= 0.4) = int_{0.2}^{0.4} 3x^2 dx = [x^3]_{0.2}^{0.4} = (0.4)^3 - (0.2)^3 = 0.064 - 0.008 = 0.056`

#### Worked Example 2

Given `f(x) = k(1-x^2)` for `-1 <= x <= 1`, find k.

Solution:
`int_{-1}^{1} k(1-x^2) dx = 1`
`k [x - x^3/3]_{-1}^{1} = 1`
`k[(1 - 1/3) - (-1 + 1/3)] = 1`
`k[2/3 - (-2/3)] = 1`
`k[4/3] = 1`
`k = 3/4`

---

### 4. Relationship Between PDF and CDF (Review)

- `F(x) = P(X <= x) = int_{-infty}^{x} f(t) dt`
- `f(x) = d/dx F(x)` (at points where F is differentiable)

---

### Part B: Joint Distributions

### 5. Joint Distributions: Motivation

Often we need to study two or more random variables simultaneously. For example:
- Height and weight of individuals
- Temperature and humidity
- X = number of heads, Y = number of tails in coin tosses

A **joint distribution** describes the probabilistic relationship between multiple random variables.

---

### 6. Joint PMF for Discrete Random Variables

For two discrete random variables X and Y, the **joint probability mass function (joint PMF)** is:

`P(X = x, Y = y) = p(x, y)`

Conditions:
1. `p(x, y) >= 0` for all x, y
2. `sum_{x} sum_{y} p(x, y) = 1`

#### Worked Example 3 (Joint PMF Table)

Let X and Y be the outcomes of two fair dice rolls. The joint PMF is:

`P(X = i, Y = j) = 1/36` for all i, j in {1, 2, 3, 4, 5, 6}

This is a uniform joint distribution over 36 points.

#### Worked Example 4

The joint PMF of X and Y is given in the table:

| X\Y | 0 | 1 | 2 |
|-----|---|---|---|
| 0   | 0.1 | 0.2 | 0.1 |
| 1   | 0.2 | 0.1 | 0.1 |
| 2   | 0.1 | 0.05 | 0.05 |

Verify this is a valid joint PMF.

Solution: Sum of all entries = `0.1 + 0.2 + 0.1 + 0.2 + 0.1 + 0.1 + 0.1 + 0.05 + 0.05 = 1.0`. All entries are >= 0. Valid.

---

### 7. Joint PDF for Continuous Random Variables

For continuous X and Y, the **joint probability density function (joint PDF)**, `f(x, y)`, satisfies:

1. `f(x, y) >= 0` for all (x, y)
2. `int_{-infty}^{infty} int_{-infty}^{infty} f(x, y) dx dy = 1`
3. `P((X, Y) in A) = intint_{A} f(x, y) dx dy`

#### Worked Example 5

Check if `f(x, y) = 12x^2 y` for `0 <= x <= 1, 0 <= y <= 1` is a valid joint PDF.

Solution:
`int_{0}^{1} int_{0}^{1} 12x^2 y dx dy`
= `int_{0}^{1} [4x^3 y]_{x=0}^{x=1} dy`
= `int_{0}^{1} 4y dy`
= `[2y^2]_{0}^{1} = 2`

Since the double integral = 2, not 1, this is NOT a valid joint PDF. A normalizing constant `k = 1/2` would be needed.

---

### 8. Marginal Distributions

The **marginal distribution** of a single random variable is obtained by summing (for discrete) or integrating (for continuous) over the other variable.

**Discrete marginal PMF:**
- `p_X(x) = sum_{y} P(X = x, Y = y) = sum_{y} p(x, y)`
- `p_Y(y) = sum_{x} p(x, y)`

**Continuous marginal PDF:**
- `f_X(x) = int_{-infty}^{infty} f(x, y) dy`
- `f_Y(y) = int_{-infty}^{infty} f(x, y) dx`

Marginal distributions describe each variable individually, ignoring the other.

#### Worked Example 6 (Marginal from Joint PMF)

From the joint PMF in Example 4, find marginal distributions of X and Y.

Solution:

Marginal PMF of X:
`P(X=0) = sum_{y} p(0,y) = 0.1 + 0.2 + 0.1 = 0.4`
`P(X=1) = 0.2 + 0.1 + 0.1 = 0.4`
`P(X=2) = 0.1 + 0.05 + 0.05 = 0.2`

Verification: `0.4 + 0.4 + 0.2 = 1`.

Marginal PMF of Y:
`P(Y=0) = 0.1 + 0.2 + 0.1 = 0.4`
`P(Y=1) = 0.2 + 0.1 + 0.05 = 0.35`
`P(Y=2) = 0.1 + 0.1 + 0.05 = 0.25`

Verification: `0.4 + 0.35 + 0.25 = 1`.

#### Worked Example 7 (Marginal from Joint PDF)

Let `f(x, y) = 6/5 (x + y^2)` for `0 <= x <= 1, 0 <= y <= 1`. Find the marginal PDF of X.

Solution:
`f_X(x) = int_{0}^{1} 6/5 (x + y^2) dy`
`= 6/5 int_{0}^{1} (x + y^2) dy`
`= 6/5 [xy + y^3/3]_{0}^{1}`
`= 6/5 [x + 1/3]`
`= (6x + 2)/5` for `0 <= x <= 1`

Check: `int_{0}^{1} (6x+2)/5 dx = [3x^2 + 2x]/5 |_{0}^{1} = (3+2)/5 = 1`. Valid.

---

### 9. Summary

| Aspect | Discrete | Continuous |
|--------|----------|------------|
| Joint representation | Joint PMF `p(x,y)` | Joint PDF `f(x,y)` |
| Total probability | `sum sum p(x,y) = 1` | `int int f(x,y) dx dy = 1` |
| Marginal of X | `p_X(x) = sum_{y} p(x,y)` | `f_X(x) = int f(x,y) dy` |
| Marginal of Y | `p_Y(y) = sum_{x} p(x,y)` | `f_Y(y) = int f(x,y) dx` |

---

## Practice Problems

1. Let X have PDF `f(x) = 2e^{-2x}` for `x >= 0`. Find `P(X > 1)` and `P(0.5 < X < 1.5)`.

2. Find c such that `f(x) = c/sqrt(x)` for `0 < x < 4` is a valid PDF. Then compute `P(X < 1)`.

3. The joint PMF of X and Y is: `p(0,0) = 0.1`, `p(0,1) = 0.2`, `p(1,0) = 0.3`, `p(1,1) = 0.4`. Find the marginal PMFs of X and Y.

4. Let `f(x, y) = 2x + 3y` for `0 <= x <= 1, 0 <= y <= 1`. Determine if this is a valid joint PDF. If not, find the normalizing constant k.

5. For the joint PDF `f(x, y) = 2e^{-x}e^{-2y}` for `x >= 0, y >= 0`, find the marginal PDFs of X and Y.

**Answers / Hints:**
1. `P(X>1) = int_1^{infty} 2e^{-2x}dx = e^{-2} approx 0.1353`. `P(0.5<X<1.5) = e^{-1} - e^{-3} approx 0.318`.
2. `c int_0^4 x^{-1/2} dx = c[2sqrt{x}]_0^4 = 4c = 1` => `c = 1/4`. `P(X<1) = 1/4 int_0^1 x^{-1/2} dx = 1/4 * 2 = 0.5`.
3. `P(X=0)=0.3`, `P(X=1)=0.7`. `P(Y=0)=0.4`, `P(Y=1)=0.6`.
4. `int_0^1 int_0^1 (2x+3y)dx dy = int_0^1 [x^2+3xy]_0^1 dy = int_0^1 (1+3y)dy = [y+3y^2/2]_0^1 = 2.5`. Not valid. k=2/5.
5. `f_X(x) = int_0^{infty} 2e^{-x}e^{-2y} dy = 2e^{-x} * 1/2 = e^{-x}` for x>=0. `f_Y(y) = int_0^{infty} 2e^{-x}e^{-2y} dx = 2e^{-2y}` for y>=0.
