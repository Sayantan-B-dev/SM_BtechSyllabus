# Multiple regression

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 9  
**Date:** 28-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 12.3

## Notes

### 1. Introduction to Multiple Regression

Simple linear regression models the relationship between **one dependent variable** (y) and **one independent variable** (x). In real-world problems, the dependent variable is often influenced by **multiple independent variables**.

**Multiple linear regression** extends simple regression to include two or more predictors.

**General form (with k independent variables):**

```
y = beta0 + beta1*x1 + beta2*x2 + ... + betak*xk + epsilon
```

where:
- `y` = dependent variable
- `x1, x2, ..., xk` = independent variables
- `beta0` = intercept
- `beta1, beta2, ..., betak` = regression coefficients (slopes)
- `epsilon` = error term

For a sample, we estimate:

```
y_hat = a + b1*x1 + b2*x2 + ... + bk*xk
```

---

### 2. Multiple Regression with Two Independent Variables

The simplest case of multiple regression involves two predictors:

```
y = a + b1*x1 + b2*x2
```

Geometrically, this represents a **regression plane** in three-dimensional space (x1, x2, y).

---

### 3. Setting Up Normal Equations

Using the **method of least squares**, we minimize:

```
S = sum (yi - a - b1*x1i - b2*x2i)^2
```

Taking partial derivatives with respect to a, b1, and b2, and setting them to zero, we obtain the **normal equations**:

```
(1) sum y = n*a + b1*sum x1 + b2*sum x2
(2) sum x1*y = a*sum x1 + b1*sum x1^2 + b2*sum x1*x2
(3) sum x2*y = a*sum x2 + b1*sum x1*x2 + b2*sum x2^2
```

#### Solving the Normal Equations

From equation (1):

```
a = y_bar - b1*x1_bar - b2*x2_bar
```

To find b1 and b2, we first compute the **corrected sums** (deviations from means):

```
S11 = sum (x1 - x1_bar)^2 = sum x1^2 - (sum x1)^2 / n
S22 = sum (x2 - x2_bar)^2 = sum x2^2 - (sum x2)^2 / n
S12 = sum (x1 - x1_bar)*(x2 - x2_bar) = sum x1*x2 - (sum x1)*(sum x2) / n
S1y = sum (x1 - x1_bar)*(y - y_bar) = sum x1*y - (sum x1)*(sum y) / n
S2y = sum (x2 - x2_bar)*(y - y_bar) = sum x2*y - (sum x2)*(sum y) / n
```

Then b1 and b2 are obtained by solving:

```
S11*b1 + S12*b2 = S1y
S12*b1 + S22*b2 = S2y
```

Using Cramer's rule:

```
b1 = (S1y*S22 - S2y*S12) / (S11*S22 - S12^2)
b2 = (S2y*S11 - S1y*S12) / (S11*S22 - S12^2)
```

---

### 4. Worked Example: Multiple Regression with 2 Independent Variables

**Problem:** A researcher wants to predict a student's final exam score (y) based on:
- x1 = number of hours studied
- x2 = number of practice tests taken

Data for 10 students:

| Student | Hours (x1) | Tests (x2) | Score (y) |
|---|---|---|---|
| 1 | 3 | 2 | 75 |
| 2 | 4 | 3 | 80 |
| 3 | 5 | 2 | 82 |
| 4 | 3 | 4 | 78 |
| 5 | 6 | 3 | 88 |
| 6 | 7 | 4 | 92 |
| 7 | 4 | 2 | 76 |
| 8 | 5 | 5 | 85 |
| 9 | 6 | 4 | 90 |
| 10 | 7 | 3 | 86 |

Find the multiple regression equation `y = a + b1*x1 + b2*x2`.

#### Step 1: Compute all sums.

| x1 | x2 | y | x1^2 | x2^2 | x1*x2 | x1*y | x2*y |
|---|---|---|---|---|---|---|---|
| 3 | 2 | 75 | 9 | 4 | 6 | 225 | 150 |
| 4 | 3 | 80 | 16 | 9 | 12 | 320 | 240 |
| 5 | 2 | 82 | 25 | 4 | 10 | 410 | 164 |
| 3 | 4 | 78 | 9 | 16 | 12 | 234 | 312 |
| 6 | 3 | 88 | 36 | 9 | 18 | 528 | 264 |
| 7 | 4 | 92 | 49 | 16 | 28 | 644 | 368 |
| 4 | 2 | 76 | 16 | 4 | 8 | 304 | 152 |
| 5 | 5 | 85 | 25 | 25 | 25 | 425 | 425 |
| 6 | 4 | 90 | 36 | 16 | 24 | 540 | 360 |
| 7 | 3 | 86 | 49 | 9 | 21 | 602 | 258 |
| **50** | **32** | **832** | **270** | **112** | **164** | **4232** | **2693** |

```
n = 10
sum x1 = 50
sum x2 = 32
sum y = 832
sum x1^2 = 270
sum x2^2 = 112
sum x1*x2 = 164
sum x1*y = 4232
sum x2*y = 2693
```

#### Step 2: Compute means.

```
x1_bar = 50/10 = 5
x2_bar = 32/10 = 3.2
y_bar = 832/10 = 83.2
```

#### Step 3: Compute corrected sums.

```
S11 = sum x1^2 - (sum x1)^2 / n = 270 - 2500/10 = 270 - 250 = 20
S22 = sum x2^2 - (sum x2)^2 / n = 112 - 1024/10 = 112 - 102.4 = 9.6
S12 = sum x1*x2 - (sum x1)*(sum x2) / n = 164 - 50*32/10 = 164 - 160 = 4
S1y = sum x1*y - (sum x1)*(sum y) / n = 4232 - 50*832/10 = 4232 - 4160 = 72
S2y = sum x2*y - (sum x2)*(sum y) / n = 2693 - 32*832/10 = 2693 - 2662.4 = 30.6
```

#### Step 4: Set up equations for b1 and b2.

```
S11*b1 + S12*b2 = S1y
20*b1 + 4*b2 = 72

S12*b1 + S22*b2 = S2y
4*b1 + 9.6*b2 = 30.6
```

#### Step 5: Solve for b1 and b2.

**Using Cramer's rule:**

```
Denominator = S11*S22 - S12^2 = 20*9.6 - 4^2 = 192 - 16 = 176

b1 = (S1y*S22 - S2y*S12) / (S11*S22 - S12^2)
   = (72*9.6 - 30.6*4) / 176
   = (691.2 - 122.4) / 176
   = 568.8 / 176
   = 3.2318

b2 = (S2y*S11 - S1y*S12) / (S11*S22 - S12^2)
   = (30.6*20 - 72*4) / 176
   = (612 - 288) / 176
   = 324 / 176
   = 1.8409
```

#### Step 6: Find the intercept a.

```
a = y_bar - b1*x1_bar - b2*x2_bar
  = 83.2 - 3.2318*5 - 1.8409*3.2
  = 83.2 - 16.159 - 5.8909
  = 61.1501
```

#### Step 7: Multiple regression equation.

```
y_hat = 61.15 + 3.23*x1 + 1.84*x2
```

#### Step 8: Interpret the coefficients.

- **Intercept (a = 61.15):** When a student studies 0 hours and takes 0 practice tests, the predicted score is 61.15. (This may not be practically meaningful but is mathematically required.)

- **b1 = 3.23:** Holding x2 (practice tests) constant, each additional hour of study increases the predicted score by 3.23 points.

- **b2 = 1.84:** Holding x1 (hours studied) constant, each additional practice test increases the predicted score by 1.84 points.

#### Step 9: Use the equation for prediction.

**Predict the score for a student who studies 8 hours and takes 5 practice tests:**

```
y_hat = 61.15 + 3.23*8 + 1.84*5
      = 61.15 + 25.84 + 9.20
      = 96.19
```

---

### 5. Matrix Approach to Multiple Regression

For the general case with k independent variables, matrix algebra provides a compact solution.

**Model:** `y = X * beta + epsilon`

where:
- `y` = n x 1 vector of observed y values
- `X` = n x (k+1) design matrix (first column of 1s for intercept)
- `beta` = (k+1) x 1 vector of coefficients
- `epsilon` = n x 1 vector of errors

**Least squares solution:**

```
beta_hat = (X' * X)^(-1) * X' * y
```

where `X'` is the transpose of X.

#### Example in Matrix Form (for the 2-variable case above)

**Step 1: Construct the matrices.**

```
y = [75, 80, 82, 78, 88, 92, 76, 85, 90, 86]'

X = [1  3  2
     1  4  3
     1  5  2
     1  3  4
     1  6  3
     1  7  4
     1  4  2
     1  5  5
     1  6  4
     1  7  3]
```

**Step 2: Compute X'X.**

```
X'X = [n        sum x1       sum x2
       sum x1   sum x1^2     sum x1*x2
       sum x2   sum x1*x2    sum x2^2]

     = [10     50      32
        50     270     164
        32     164     112]
```

**Step 3: Compute X'y.**

```
X'y = [sum y      = 832
       sum x1*y   = 4232
       sum x2*y   = 2693]
```

**Step 4: Solve (X'X)^(-1) * X'y.**

Computing the inverse and multiplying gives the same coefficients: a = 61.15, b1 = 3.23, b2 = 1.84.

---

### 6. Properties of Multiple Regression Coefficients

1. **Partial regression coefficients:** Each coefficient measures the effect of that variable **holding all other variables constant**.

2. **Units:** Each coefficient is in units of y per unit of the respective x variable.

3. **Sign and magnitude:** The sign indicates the direction of the relationship. The magnitude depends on the scale of the variables.

4. **Least squares property:** The sum of residuals is zero: `sum (yi - y_hat_i) = 0`.

5. **The regression plane passes through the point of means:** `(x1_bar, x2_bar, y_bar)`.

6. **Multiple correlation coefficient (R):** Measures the strength of the relationship between y and the set of x variables. R^2 is the **coefficient of multiple determination**.

---

### 7. Coefficient of Multiple Determination (R^2)

```
R^2 = SSR / SST = 1 - SSE / SST
```

where:
- `SST = sum (yi - y_bar)^2` (total sum of squares)
- `SSR = sum (y_hat_i - y_bar)^2` (regression sum of squares)
- `SSE = sum (yi - y_hat_i)^2` (error sum of squares)

R^2 represents the proportion of variance in y explained by the regression model.

**For our example:**

```
SST = sum (yi - y_bar)^2 = (75-83.2)^2 + (80-83.2)^2 + ... + (86-83.2)^2
    = (-8.2)^2 + (-3.2)^2 + (-1.2)^2 + (-5.2)^2 + (4.8)^2 + (8.8)^2 + (-7.2)^2 + (1.8)^2 + (6.8)^2 + (2.8)^2
    = 67.24 + 10.24 + 1.44 + 27.04 + 23.04 + 77.44 + 51.84 + 3.24 + 46.24 + 7.84
    = 315.6

SSR = b1*S1y + b2*S2y = 3.2318*72 + 1.8409*30.6 = 232.69 + 56.33 = 289.02

R^2 = 289.02 / 315.6 = 0.9158
```

Interpretation: About 91.6% of the variation in exam scores is explained by hours studied and number of practice tests. This is a very good fit.

---

### 8. Comparison: Simple vs Multiple Regression

| Aspect | Simple Regression | Multiple Regression |
|---|---|---|
| Number of predictors | One | Two or more |
| Equation | y = a + bx | y = a + b1*x1 + b2*x2 + ... |
| Geometric representation | Line in 2D | Plane (2 predictors) or hyperplane (k>2) |
| Coefficient interpretation | Slope of the line | Partial slope (holding others constant) |
| R^2 | Square of r | Proportion of variance explained by all predictors |

---

### 9. Assumptions of Multiple Linear Regression

1. **Linearity:** The relationship between y and each x is linear.
2. **Independence:** Observations are independent of each other.
3. **Homoscedasticity:** The variance of errors is constant.
4. **Normality:** Errors are normally distributed.
5. **No multicollinearity:** The independent variables are not highly correlated with each other.

**Multicollinearity** occurs when x1 and x2 are highly correlated. This can make the coefficient estimates unstable and difficult to interpret. In our example, S12 = 4, which is small relative to S11 (20) and S22 (9.6), so multicollinearity is not a concern.

---

### 10. Extensions

1. **More than 2 predictors:** The same method extends to k predictors, but manual calculation becomes tedious. Software (Excel, Python, R, SPSS) is used in practice.

2. **Non-linear terms:** You can include x^2, x1*x2, etc., as additional variables.

3. **Categorical variables:** Can be included using dummy variables (0/1 encoding).

4. **Interaction effects:** The product x1*x2 represents an interaction where the effect of x1 depends on the level of x2.

---

## Practice Problems

1. For the data:

| y | x1 | x2 |
|---|---|---|
| 10 | 2 | 1 |
| 12 | 3 | 2 |
| 14 | 4 | 1 |
| 16 | 5 | 3 |
| 18 | 6 | 2 |

Find the multiple regression equation `y = a + b1*x1 + b2*x2`.

   <details>
   <summary>Show Answer</summary>
   1. sum x1 = 20, sum x2 = 9, sum y = 70, sum x1^2 = 90, sum x2^2 = 19, sum x1*x2 = 39, sum x1*y = 298, sum x2*y = 134.
      x1_bar = 4, x2_bar = 1.8, y_bar = 14.
      S11 = 90 - 400/5 = 90-80 = 10.
      S22 = 19 - 81/5 = 19-16.2 = 2.8.
      S12 = 39 - 180/5 = 39-36 = 3.
      S1y = 298 - 1400/5 = 298-280 = 18.
      S2y = 134 - 630/5 = 134-126 = 8.
      Denom = 10*2.8 - 9 = 28-9 = 19.
      b1 = (18*2.8 - 8*3)/19 = (50.4-24)/19 = 26.4/19 = 1.3895.
      b2 = (8*10 - 18*3)/19 = (80-54)/19 = 26/19 = 1.3684.
      a = 14 - 1.3895*4 - 1.3684*1.8 = 14 - 5.558 - 2.463 = 5.979.
      y = 5.98 + 1.39*x1 + 1.37*x2.
   </details>

2. Given: n = 8, sum x1 = 48, sum x2 = 32, sum y = 120, sum x1^2 = 300, sum x2^2 = 140, sum x1*x2 = 200, sum x1*y = 740, sum x2*y = 500. Find b1 and b2.

   <details>
   <summary>Show Answer</summary>
   2. x1_bar = 6, x2_bar = 4, y_bar = 15.
      S11 = 300 - 2304/8 = 300-288 = 12.
      S22 = 140 - 1024/8 = 140-128 = 12.
      S12 = 200 - 1536/8 = 200-192 = 8.
      S1y = 740 - 5760/8 = 740-720 = 20.
      S2y = 500 - 3840/8 = 500-480 = 20.
      Denom = 12*12 - 64 = 144-64 = 80.
      b1 = (20*12 - 20*8)/80 = (240-160)/80 = 80/80 = 1.
      b2 = (20*12 - 20*8)/80 = 80/80 = 1.
   </details>

3. In a multiple regression with two predictors, R^2 = 0.75. Interpret this value.

   <details>
   <summary>Show Answer</summary>
   3. R^2 = 0.75 means 75% of the variation in the dependent variable y is explained by the two independent variables together. The remaining 25% is due to other factors not included in the model.
   </details>

4. Explain the meaning of b1 = 2.5 in the equation `y_hat = 15 + 2.5*x1 + 1.2*x2`.

   <details>
   <summary>Show Answer</summary>
   4. b1 = 2.5 means that for every one-unit increase in x1, the predicted value of y increases by 2.5 units, holding x2 constant. (The intercept 15 is the predicted value when both x1 and x2 are zero.)
   </details>

5. What is multicollinearity and why is it a problem in multiple regression?
   <details>
   <summary>Show Answer</summary>
   5. Multicollinearity occurs when two or more independent variables are highly correlated with each other. Problems include: (a) unstable coefficient estimates (small changes in data cause large changes in coefficients), (b) inflated standard errors making coefficients statistically insignificant, (c) difficulty in interpreting individual effects. It can be detected using variance inflation factor (VIF).
   </details>
