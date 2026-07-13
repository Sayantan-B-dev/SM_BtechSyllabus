# Regression , Method of curve fitting

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 8  
**Date:** 24-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Demonstration  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 11.2, 11.12,11.17

## Notes

### Part A: Regression Analysis

### 1. Introduction to Regression

While correlation measures the **strength** of the relationship between two variables, **regression** models the **form** of the relationship. Regression allows us to:
- Predict the value of one variable given the other.
- Understand how much y changes when x changes.
- Estimate the line (or curve) of best fit.

**Key terminology:**
- **Dependent variable (y):** The variable we want to predict (also called response variable).
- **Independent variable (x):** The variable used for prediction (also called predictor or explanatory variable).

---

### 2. Regression Lines

In bivariate analysis, there are **two regression lines**:

1. **Regression line of y on x:** Used to predict y given x.
   ```
   y = a + b*x
   ```
   where b = regression coefficient of y on x (denoted `b_yx`).

2. **Regression line of x on y:** Used to predict x given y.
   ```
   x = a' + b'*y
   ```
   where b' = regression coefficient of x on y (denoted `b_xy`).

These two lines are generally different unless r = +1 or r = -1 (perfect correlation), in which case they coincide.

---

### 3. Derivation using Least Squares Method

The **method of least squares** finds the line that minimizes the sum of squared vertical distances between observed points and the fitted line.

#### 3.1 Regression Line of y on x

We want to find `y = a + b*x` that minimizes `S = sum (yi - a - b*xi)^2`.

Taking partial derivatives with respect to a and b and setting them to zero:

```
dS/da = -2 * sum (yi - a - b*xi) = 0  =>  sum yi = n*a + b*sum xi
dS/db = -2 * sum xi*(yi - a - b*xi) = 0  =>  sum xi*yi = a*sum xi + b*sum xi^2
```

This gives the **normal equations**:

```
(1) sum yi = n*a + b*sum xi
(2) sum xi*yi = a*sum xi + b*sum xi^2
```

Solving for b and a:

```
b = [n*sum xi*yi - sum xi*sum yi] / [n*sum xi^2 - (sum xi)^2]

a = y_bar - b*x_bar
```

The regression coefficient `b` is also denoted as `b_yx` and can be expressed as:

```
b_yx = r * (sigma_y / sigma_x)
```

#### 3.2 Regression Line of x on y

Similarly, for `x = a' + b'*y`:

```
b' = [n*sum xi*yi - sum xi*sum yi] / [n*sum yi^2 - (sum yi)^2] = b_xy

a' = x_bar - b'*y_bar
```

And:

```
b_xy = r * (sigma_x / sigma_y)
```

---

### 4. Properties of Regression Coefficients

1. **Relationship with correlation:**
   ```
   r = sqrt(b_yx * b_xy)
   ```
   The correlation coefficient is the geometric mean of the two regression coefficients.

2. **Sign consistency:** Both `b_yx` and `b_xy` have the same sign as r.

3. **Range:** Regression coefficients are not bounded between -1 and +1 (unlike r). They depend on the units.

4. **Effect of change of origin and scale:**
   - Changing origin (adding a constant) does not affect regression coefficients.
   - Changing scale does affect them proportionally.

5. **The two regression lines intersect at (x_bar, y_bar).**

6. **Angle between regression lines:**
   - If r = 0, the lines are perpendicular.
   - If r = +1 or r = -1, the lines coincide.

---

### 5. Worked Example: Finding Regression Lines

**Problem:** For the following data, find:
a) The regression line of y on x.
b) The regression line of x on y.
c) Estimate y when x = 15.
d) Estimate x when y = 25.

| x | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|
| y | 5 | 7 | 10 | 12 | 14 | 18 |

**Step 1: Compute required sums.**

```
n = 6
sum x = 2+4+6+8+10+12 = 42
sum y = 5+7+10+12+14+18 = 66
sum xy = 2*5 + 4*7 + 6*10 + 8*12 + 10*14 + 12*18 = 10+28+60+96+140+216 = 550
sum x^2 = 4+16+36+64+100+144 = 364
sum y^2 = 25+49+100+144+196+324 = 838
```

**Step 2: Compute means.**

```
x_bar = 42/6 = 7
y_bar = 66/6 = 11
```

**Step 3: Regression of y on x.**

```
b_yx = [n*sum xy - sum x*sum y] / [n*sum x^2 - (sum x)^2]
     = [6*550 - 42*66] / [6*364 - 42^2]
     = [3300 - 2772] / [2184 - 1764]
     = 528 / 420
     = 1.2571

a = y_bar - b*x_bar = 11 - 1.2571*7 = 11 - 8.8 = 2.2

Regression line of y on x: y = 2.2 + 1.2571*x
```

**Step 4: Regression of x on y.**

```
b_xy = [n*sum xy - sum x*sum y] / [n*sum y^2 - (sum y)^2]
     = [6*550 - 42*66] / [6*838 - 66^2]
     = [3300 - 2772] / [5028 - 4356]
     = 528 / 672
     = 0.7857

a' = x_bar - b'*y_bar = 7 - 0.7857*11 = 7 - 8.6429 = -1.6429

Regression line of x on y: x = -1.6429 + 0.7857*y
```

**Step 5: Verify relationship with correlation.**

```
b_yx = 1.2571, b_xy = 0.7857
r = sqrt(1.2571 * 0.7857) = sqrt(0.9878) = 0.9939

Verification using Pearson's formula:
Numerator = 6*550 - 42*66 = 528
Denom = sqrt((6*364-1764)*(6*838-4356)) = sqrt(420*672) = sqrt(282240) = 531.26
r = 528/531.26 = 0.9939 (matches!)
```

**Step 6: Predictions.**

a) Estimate y when x = 15:
```
y = 2.2 + 1.2571*15 = 2.2 + 18.8565 = 21.057
```

b) Estimate x when y = 25:
```
x = -1.6429 + 0.7857*25 = -1.6429 + 19.6425 = 18.0
```

---

### 6. Another Worked Example

**Problem:** Given:
- n = 10
- sum x = 60, sum y = 80
- sum xy = 520
- sum x^2 = 400, sum y^2 = 700

Find the two regression equations and estimate y when x = 8.

**Step 1: Means.**

```
x_bar = 60/10 = 6
y_bar = 80/10 = 8
```

**Step 2: Regression of y on x.**

```
b_yx = (10*520 - 60*80) / (10*400 - 3600) = (5200 - 4800) / (4000 - 3600) = 400/400 = 1
a = 8 - 1*6 = 2
y = 2 + x
```

**Step 3: Regression of x on y.**

```
b_xy = (10*520 - 60*80) / (10*700 - 6400) = 400 / (7000 - 6400) = 400/600 = 0.667
a' = 6 - 0.667*8 = 6 - 5.336 = 0.664
x = 0.664 + 0.667*y
```

**Step 4: Estimate y when x = 8.**

```
y = 2 + 8 = 10
```

---

### 7. Relationship Between Correlation and Regression

| Aspect | Correlation | Regression |
|---|---|---|
| Purpose | Measures strength and direction of relationship | Models the relationship for prediction |
| Variables | Both variables treated symmetrically | One is dependent, other independent |
| Coefficient | r (between -1 and +1) | b_yx, b_xy (no fixed range) |
| Unit-free? | Yes | No (depends on units) |
| Prediction | Not directly used | Used for prediction |
| Formula | r = cov(x,y)/(sigma_x * sigma_y) | b_yx = r * sigma_y / sigma_x |

---

### Part B: Method of Curve Fitting

### 8. Introduction to Curve Fitting

Sometimes the relationship between x and y is not linear. We can fit different types of curves:

1. **Straight line:** `y = a + b*x`
2. **Parabola (quadratic):** `y = a + b*x + c*x^2`
3. **Exponential curve:** `y = a * e^(b*x)` or `y = a * b^x`
4. **Power curve:** `y = a * x^b`

The method of least squares extends naturally to these cases.

---

### 9. Fitting a Straight Line (Review)

Already covered above. The normal equations are:

```
sum y = n*a + b*sum x
sum x*y = a*sum x + b*sum x^2
```

---

### 10. Fitting a Parabola (Second-degree Curve)

Model: `y = a + b*x + c*x^2`

We minimize `S = sum (yi - a - b*xi - c*xi^2)^2`.

Setting partial derivatives to zero gives **three normal equations**:

```
(1) sum y = n*a + b*sum x + c*sum x^2
(2) sum x*y = a*sum x + b*sum x^2 + c*sum x^3
(3) sum x^2*y = a*sum x^2 + b*sum x^3 + c*sum x^4
```

Solve these three equations simultaneously for a, b, and c.

#### Example: Fit a Parabola

Fit a parabola `y = a + b*x + c*x^2` to the data:

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| y | 1 | 3 | 7 | 13 | 21 |

**Step 1: Compute the required sums.**

| x | y | x^2 | x^3 | x^4 | xy | x^2*y |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 3 | 1 | 1 | 1 | 3 | 3 |
| 2 | 7 | 4 | 8 | 16 | 14 | 28 |
| 3 | 13 | 9 | 27 | 81 | 39 | 117 |
| 4 | 21 | 16 | 64 | 256 | 84 | 336 |
| **10** | **45** | **30** | **100** | **354** | **140** | **484** |

**Step 2: Set up normal equations.**

```
n = 5

(1) sum y = n*a + b*sum x + c*sum x^2
    45 = 5a + 10b + 30c

(2) sum x*y = a*sum x + b*sum x^2 + c*sum x^3
    140 = 10a + 30b + 100c

(3) sum x^2*y = a*sum x^2 + b*sum x^3 + c*sum x^4
    484 = 30a + 100b + 354c
```

**Step 3: Solve the system.**

Divide equation (1) by 5: `9 = a + 2b + 6c` ... (1')

Divide equation (2) by 10: `14 = a + 3b + 10c` ... (2')

Subtract (1') from (2'): `5 = b + 4c` ... (A)

Divide equation (3) by 2: `242 = 15a + 50b + 177c` ... (3')

Multiply (1') by 15: `135 = 15a + 30b + 90c` ... (1'')

Subtract (1'') from (3'): `107 = 20b + 87c` ... (B)

From (A): `b = 5 - 4c`

Substitute into (B):
```
107 = 20*(5 - 4c) + 87c
107 = 100 - 80c + 87c
107 = 100 + 7c
7c = 7
c = 1
```

From (A): `b = 5 - 4*1 = 1`
From (1'): `a = 9 - 2*1 - 6*1 = 9 - 2 - 6 = 1`

**Step 4: Result.**

```
y = 1 + x + x^2
```

Verification: When x = 0, y = 1 (matches). x = 1, y = 3 (matches). x = 2, y = 7 (matches). x = 3, y = 13 (matches). x = 4, y = 21 (matches). Perfect fit.

---

### 11. Fitting an Exponential Curve

**Case 1:** `y = a * e^(b*x)`

Take natural log on both sides:
```
ln(y) = ln(a) + b*x
```

Let `Y = ln(y)`, `A = ln(a)`. Then:
```
Y = A + b*x
```

This is a linear equation. Use the method of least squares on (x, Y) to find A and b, then `a = e^A`.

**Case 2:** `y = a * b^x`

Take log (any base, usually base 10):
```
log(y) = log(a) + x*log(b)
```

Let `Y = log(y)`, `A = log(a)`, `B = log(b)`. Then:
```
Y = A + B*x
```

Use least squares to find A and B, then `a = 10^A`, `b = 10^B`.

#### Example: Fit an Exponential Curve

Fit `y = a * e^(b*x)` to the data:

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| y | 2 | 4 | 8 | 16 | 32 |

**Step 1: Transform to linear form.**

```
Y = ln(y)
```

| x | y | Y = ln(y) |
|---|---|---|
| 0 | 2 | 0.6931 |
| 1 | 4 | 1.3863 |
| 2 | 8 | 2.0794 |
| 3 | 16 | 2.7726 |
| 4 | 32 | 3.4657 |

**Step 2: Compute sums for linear regression of Y on x.**

```
n = 5
sum x = 10
sum Y = 0.6931+1.3863+2.0794+2.7726+3.4657 = 10.3971
sum x*Y = 0*0.6931 + 1*1.3863 + 2*2.0794 + 3*2.7726 + 4*3.4657 = 0+1.3863+4.1588+8.3178+13.8628 = 27.7257
sum x^2 = 0+1+4+9+16 = 30
```

**Step 3: Find b and A.**

```
b = [n*sum x*Y - sum x*sum Y] / [n*sum x^2 - (sum x)^2]
  = [5*27.7257 - 10*10.3971] / [5*30 - 100]
  = [138.6285 - 103.971] / [150 - 100]
  = 34.6575 / 50
  = 0.69315

A = Y_bar - b*x_bar = (10.3971/5) - 0.69315*(10/5) = 2.07942 - 1.3863 = 0.69312
```

**Step 4: Transform back.**

```
a = e^A = e^0.69312 = 2.0
b = 0.69315

y = 2 * e^(0.69315*x)
```

Since `e^0.69315 = 2`, this is equivalent to `y = 2 * 2^x = 2^(x+1)`.

Verification: x=0 => y=2, x=1 => y=4, x=2 => y=8, x=3 => y=16, x=4 => y=32. Perfect fit.

---

### 12. Summary of Curve Fitting Models

| Model | Form | Linearization | Parameters |
|---|---|---|---|
| Straight line | y = a + bx | None | a, b |
| Parabola | y = a + bx + cx^2 | None | a, b, c |
| Exponential | y = a*e^(bx) | Y = ln(y) = ln(a) + bx | a = e^A, b |
| Power | y = a*x^b | Y = log(y) = log(a) + b*log(x) | a = 10^A, b |
| Exponential | y = a*b^x | Y = log(y) = log(a) + x*log(b) | a = 10^A, b = 10^B |

---

## Practice Problems

1. For the data:

| x | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| y | 3 | 5 | 7 | 9 | 11 |

Find the regression line of y on x. Predict y when x = 7.

2. Given: n = 8, sum x = 40, sum y = 64, sum xy = 340, sum x^2 = 220, sum y^2 = 540.
   Find the two regression lines.

3. Fit a parabola y = a + bx + cx^2 to the data:

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| y | 0 | 1 | 4 | 9 |

4. Fit an exponential curve y = a * b^x to:

| x | 0 | 1 | 2 |
|---|---|---|---|
| y | 3 | 6 | 12 |

5. The regression coefficients are b_yx = 0.8 and b_xy = 0.5. Find the correlation coefficient r.

**Answers/Hints:**
1. sum x = 15, sum y = 35, sum xy = 125, sum x^2 = 55.
   b = (5*125 - 15*35)/(5*55 - 225) = (625-525)/(275-225) = 100/50 = 2.
   a = 7 - 2*3 = 1.
   y = 1 + 2x. For x = 7, y = 1 + 14 = 15.

2. x_bar = 5, y_bar = 8.
   b_yx = (8*340 - 40*64)/(8*220 - 1600) = (2720-2560)/(1760-1600) = 160/160 = 1.
   a = 8 - 1*5 = 3. y = 3 + x.
   b_xy = (8*340 - 40*64)/(8*540 - 4096) = 160/(4320-4096) = 160/224 = 0.7143.
   a' = 5 - 0.7143*8 = 5 - 5.7144 = -0.7144. x = -0.7144 + 0.7143*y.

3. sum x = 6, sum y = 14, sum x^2 = 14, sum x^3 = 36, sum x^4 = 98, sum xy = 38, sum x^2y = 98.
   Normal equations:
   14 = 4a + 6b + 14c
   38 = 6a + 14b + 36c
   98 = 14a + 36b + 98c
   Solving: a = 0, b = 1, c = 1. y = x + x^2 = x(x+1).

4. Transform Y = log(y):
   x: 0, 1, 2. Y = log(3)=0.4771, log(6)=0.7782, log(12)=1.0792.
   sum x = 3, sum Y = 2.3345, sum xY = 0.7782+2.1584 = 2.9366, sum x^2 = 5.
   b = (3*2.9366-3*2.3345)/(3*5-9) = (8.8098-7.0035)/(15-9) = 1.8063/6 = 0.30105.
   A = 2.3345/3 - 0.30105*1 = 0.77817 - 0.30105 = 0.47712.
   a = 10^0.47712 = 3, b = 10^0.30105 = 2.
   y = 3 * 2^x.

5. r = sqrt(b_yx * b_xy) = sqrt(0.8 * 0.5) = sqrt(0.4) = 0.6325.
