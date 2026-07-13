# Random variables

**Course:** Probability and Statistics  
**Module:** 3 | **Lecture:** 1  
**Date:** 11-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 5.3

## Notes

### 1. Definition of a Random Variable

A **random variable** is a function that assigns a real number to each outcome in the sample space of a random experiment. It is a mapping from the sample space `S` to the real line `R`.

If `S` is the sample space, then a random variable `X` is a function `X: S -> R`.

For example, in an experiment of tossing two coins, the sample space is `S = {HH, HT, TH, TT}`. We can define a random variable `X` = number of heads. Then:
- `X(HH) = 2`
- `X(HT) = 1`
- `X(TH) = 1`
- `X(TT) = 0`

Notation: Random variables are denoted by capital letters (X, Y, Z) and their observed values by lowercase letters (x, y, z).

---

### 2. Discrete vs Continuous Random Variables

| Feature | Discrete Random Variable | Continuous Random Variable |
|---------|--------------------------|----------------------------|
| Possible values | Countable (finite or countably infinite) | Uncountably infinite (an interval) |
| Examples | Number of heads, number of defective items | Height, weight, temperature |
| Probability representation | PMF (Probability Mass Function) | PDF (Probability Density Function) |
| Can take | Specific isolated values | Any value in a range |

**Discrete Random Variable:** Takes values that can be listed. Example: X = number of heads in 3 coin tosses => X in {0, 1, 2, 3}.

**Continuous Random Variable:** Takes values in an interval. Example: X = height of a student => X in [140, 200] cm.

---

### 3. Probability Mass Function (PMF)

For a discrete random variable X, the **Probability Mass Function (PMF)** is the function `p(x)` that gives the probability that X equals a specific value x.

Definition: `P(X = x) = p(x)`

Conditions for a valid PMF:
1. `p(x) >= 0` for all x
2. `sum_{x} p(x) = 1`

#### Worked Example 1

Find the PMF of X = sum of numbers when two fair dice are rolled.

Solution:
Sample space has 36 equally likely outcomes.
- X = 2: (1,1) => P(X=2) = 1/36
- X = 3: (1,2), (2,1) => P(X=3) = 2/36
- X = 4: (1,3), (2,2), (3,1) => P(X=4) = 3/36
- X = 5: (1,4), (2,3), (3,2), (4,1) => P(X=5) = 4/36
- X = 6: (1,5), (2,4), (3,3), (4,2), (5,1) => P(X=6) = 5/36
- X = 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) => P(X=7) = 6/36
- X = 8: (2,6), (3,5), (4,4), (5,3), (6,2) => P(X=8) = 5/36
- X = 9: (3,6), (4,5), (5,4), (6,3) => P(X=9) = 4/36
- X = 10: (4,6), (5,5), (6,4) => P(X=10) = 3/36
- X = 11: (5,6), (6,5) => P(X=11) = 2/36
- X = 12: (6,6) => P(X=12) = 1/36

Verification: Sum of probabilities = `(1+2+3+4+5+6+5+4+3+2+1)/36 = 36/36 = 1`.

---

### 4. Probability Density Function (PDF)

For a continuous random variable X, the **Probability Density Function (PDF)**, denoted `f(x)`, describes the relative likelihood. Probabilities are found by integrating the PDF over an interval.

Definition: For any interval `[a, b]`, `P(a <= X <= b) = int_{a}^{b} f(x) dx`

Conditions for a valid PDF:
1. `f(x) >= 0` for all x
2. `int_{-infty}^{infty} f(x) dx = 1`

Note: For continuous variables, `P(X = a) = 0` for any specific point a. Probability is only meaningful over intervals.

#### Worked Example 2

Check if `f(x) = 2x` for `0 <= x <= 1`, and `0` elsewhere, is a valid PDF.

Solution:
- `f(x) >= 0` on [0, 1] since `2x >= 0`.
- `int_{0}^{1} 2x dx = [x^2]_{0}^{1} = 1 - 0 = 1`.

Both conditions satisfied, so `f(x)` is a valid PDF.

---

### 5. Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function (CDF)**, denoted `F(x)`, gives the probability that X takes a value less than or equal to x.

Definition: `F(x) = P(X <= x)`

**For discrete X:** `F(x) = sum_{t <= x} p(t)` (sum of PMF values up to x)

**For continuous X:** `F(x) = int_{-infty}^{x} f(t) dt` (area under PDF up to x)

#### Properties of CDF

1. **Monotonic non-decreasing:** If `a < b`, then `F(a) <= F(b)`
2. **Range:** `0 <= F(x) <= 1`
3. **Limits:** `lim_{x -> -infty} F(x) = 0` and `lim_{x -> +infty} F(x) = 1`
4. **Right-continuous:** `F(x+) = F(x)` (continuous from the right)
5. **Probability from CDF:** `P(a < X <= b) = F(b) - F(a)`
6. For continuous X, the CDF is continuous. For discrete X, the CDF is a step function that jumps at each possible value of X.

#### Worked Example 3 (Discrete CDF)

For the sum of two dice (Worked Example 1), find `F(4)` and `F(7)`.

Solution:
`F(4) = P(X <= 4) = P(X=2) + P(X=3) + P(X=4) = 1/36 + 2/36 + 3/36 = 6/36 = 1/6`

`F(7) = P(X <= 7) = P(X=2) + ... + P(X=7) = (1+2+3+4+5+6)/36 = 21/36 = 7/12`

#### Worked Example 4 (Continuous CDF)

For `f(x) = 2x`, `0 <= x <= 1`, find the CDF `F(x)`.

Solution:
For `x < 0`: `F(x) = 0`
For `0 <= x <= 1`: `F(x) = int_{0}^{x} 2t dt = [t^2]_{0}^{x} = x^2`
For `x > 1`: `F(x) = 1`

So: `F(x) = { 0 for x < 0; x^2 for 0 <= x <= 1; 1 for x > 1 }`

Check: `F(0.5) = (0.5)^2 = 0.25`. This means `P(X <= 0.5) = 0.25`.

---

### 6. Relationship Between PDF and CDF

For continuous random variables:
- `F(x) = int_{-infty}^{x} f(t) dt`
- `f(x) = d/dx F(x)` (the PDF is the derivative of the CDF)

This relationship is powerful: if we have the CDF, we can find the PDF by differentiation, and vice versa by integration.

#### Worked Example 5

If `F(x) = 1 - e^{-x}` for `x >= 0`, find the PDF `f(x)`.

Solution:
`f(x) = d/dx F(x) = d/dx [1 - e^{-x}] = e^{-x}` for `x >= 0`.

This is the PDF of the exponential distribution with parameter 1.

---

### 7. Summary Table

| Concept | Discrete | Continuous |
|---------|----------|------------|
| Function | PMF `p(x) = P(X=x)` | PDF `f(x)` |
| Total probability | `sum p(x) = 1` | `int f(x) dx = 1` |
| CDF | `F(x) = sum_{t<=x} p(t)` | `F(x) = int_{-infty}^{x} f(t) dt` |
| Probability of interval | Sum over values | Integral of PDF |
| P(X = a) | Can be > 0 | Always 0 |

---

## Practice Problems

1. A random variable X has PMF: `P(X=x) = c(x^2 + 1)` for x = 0, 1, 2, 3. Find the value of c and compute `P(X >= 2)`.

2. For a continuous random variable with PDF `f(x) = kx(1-x)` on `0 <= x <= 1`, find k, compute `P(0.2 < X < 0.6)`, and find the CDF.

3. The CDF of a random variable X is `F(x) = 0` for x < 0, `F(x) = x/4` for 0 <= x < 2, `F(x) = (x^2)/8` for 2 <= x < sqrt(8), and `F(x) = 1` for x >= sqrt(8). Find `P(1 < X < 3)` and the PDF `f(x)`.

4. A fair coin is tossed 3 times. Let X = number of heads. Write the PMF and CDF of X. Find `P(X <= 2)`.

5. Determine if `f(x) = 3e^{-3x}` for x >= 0 is a valid PDF. If yes, find the CDF.

**Answers / Hints:**
1. `sum_{x=0}^{3} c(x^2+1) = c(1+2+5+10) = 18c = 1` => `c = 1/18`. `P(X>=2) = P(2)+P(3) = 5/18 + 10/18 = 15/18 = 5/6`.
2. `int_0^1 kx(1-x)dx = k/6 = 1` => `k = 6`. `P(0.2 < X < 0.6) = int_{0.2}^{0.6} 6x(1-x)dx = 0.544`. CDF: `F(x) = 3x^2 - 2x^3` on [0,1].
3. `P(1 < X < 3) = F(3-) - F(1) = (9/8) - (1/4) = 7/8`. PDF: f(x) = 1/4 for [0,2), x/4 for [2, sqrt(8)).
4. PMF: P(0)=1/8, P(1)=3/8, P(2)=3/8, P(3)=1/8. CDF: step function. P(X<=2) = 7/8.
5. Yes. `int_0^{infty} 3e^{-3x} dx = 1`. CDF: `F(x) = 1 - e^{-3x}` for x >= 0.
