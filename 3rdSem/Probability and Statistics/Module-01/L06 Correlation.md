# Correlation

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 6  
**Date:** 21-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 10.2

## Notes

### 1. Definition of Correlation

Correlation is a statistical measure that describes the degree and direction of the relationship between two variables. When two variables are such that a change in one is accompanied by a change in the other, they are said to be correlated.

**Key points:**
- Correlation measures association, not causation.
- It quantifies how strongly two variables move together.
- The correlation coefficient is a number between -1 and +1.

---

### 2. Types of Correlation

#### 2.1 Based on Direction

**a) Positive Correlation:**
- Both variables move in the same direction.
- As x increases, y increases; as x decreases, y decreases.
- Examples: Height and weight, study hours and exam scores.
- Correlation coefficient r > 0.

**b) Negative Correlation:**
- Variables move in opposite directions.
- As x increases, y decreases (and vice versa).
- Examples: Price and demand, speed and travel time.
- Correlation coefficient r < 0.

**c) Zero Correlation:**
- No linear relationship exists.
- Changes in x do not systematically affect y.
- Examples: Shoe size and IQ, height and exam score.
- Correlation coefficient r = 0.

#### 2.2 Based on Form

**a) Linear Correlation:**
- The relationship follows a straight-line pattern.
- Points on a scatter plot cluster around a straight line.
- Measured by Karl Pearson's correlation coefficient.

**b) Non-linear (Curvilinear) Correlation:**
- The relationship follows a curved pattern.
- Examples: y = x^2, y = log(x).
- Karl Pearson's coefficient may underestimate the relationship.

---

### 3. Karl Pearson's Coefficient of Correlation

Also called the **product-moment correlation coefficient**, denoted by `r`.

#### 3.1 Formula for Raw Data

```
r = cov(x, y) / (sigma_x * sigma_y)
```

where:

```
cov(x, y) = sum (xi - x_bar)(yi - y_bar) / n
sigma_x = sqrt( sum (xi - x_bar)^2 / n )
sigma_y = sqrt( sum (yi - y_bar)^2 / n )
```

**Computational formula (easier for calculations):**

```
r = (n * sum xi*yi - sum xi * sum yi) / sqrt( [n * sum xi^2 - (sum xi)^2] * [n * sum yi^2 - (sum yi)^2] )
```

#### 3.2 Step-by-step Calculation Procedure

1. Compute `sum xi`, `sum yi`, `sum xi*yi`, `sum xi^2`, `sum yi^2`.
2. Substitute into the computational formula.
3. Simplify numerator and denominator.
4. Compute r.

#### 3.3 Example 1: Raw Data

Find Karl Pearson's correlation coefficient for the following data:

| x | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| y | 3 | 5 | 7 | 9 | 11 |

Solution:

```
Step 1: Compute sums.
xi: 2, 4, 6, 8, 10
yi: 3, 5, 7, 9, 11
n = 5

sum xi = 2+4+6+8+10 = 30
sum yi = 3+5+7+9+11 = 35
sum xi*yi = 2*3 + 4*5 + 6*7 + 8*9 + 10*11 = 6+20+42+72+110 = 250
sum xi^2 = 4+16+36+64+100 = 220
sum yi^2 = 9+25+49+81+121 = 285

Step 2: Apply formula.
Numerator = n*sum xi*yi - sum xi*sum yi = 5*250 - 30*35 = 1250 - 1050 = 200

Denominator = sqrt( [n*sum xi^2 - (sum xi)^2] * [n*sum yi^2 - (sum yi)^2] )
            = sqrt( [5*220 - 30^2] * [5*285 - 35^2] )
            = sqrt( [1100 - 900] * [1425 - 1225] )
            = sqrt( 200 * 200 )
            = sqrt(40000)
            = 200

r = 200 / 200 = 1.0
```

Interpretation: Perfect positive correlation (r = +1). The data lies exactly on a straight line.

#### 3.4 Example 2: Raw Data with Partial Correlation

| x | 10 | 14 | 18 | 22 | 26 | 30 |
|---|---|---|---|---|---|---|
| y | 12 | 18 | 20 | 28 | 30 | 36 |

Solution:

```
n = 6

Step 1: Compute sums.
sum xi = 10+14+18+22+26+30 = 120
sum yi = 12+18+20+28+30+36 = 144
sum xi*yi = 10*12 + 14*18 + 18*20 + 22*28 + 26*30 + 30*36
          = 120 + 252 + 360 + 616 + 780 + 1080 = 3208
sum xi^2 = 100+196+324+484+676+900 = 2680
sum yi^2 = 144+324+400+784+900+1296 = 3848

Step 2: Apply formula.
Numerator = 6*3208 - 120*144 = 19248 - 17280 = 1968

Denominator = sqrt( [6*2680 - 120^2] * [6*3848 - 144^2] )
            = sqrt( [16080 - 14400] * [23088 - 20736] )
            = sqrt( 1680 * 2352 )
            = sqrt( 3951360 )
            = 1987.80

r = 1968 / 1987.80 = 0.990
```

Interpretation: Very strong positive correlation (r = 0.99). As x increases, y increases almost linearly.

---

#### 3.5 Karl Pearson's Coefficient for Grouped Data (Bivariate Frequency Table)

For data presented in a bivariate frequency table, the formula becomes:

```
r = (N * sum sum fij * xi * yj - (sum fi.* xi) * (sum f.j * yj)) /
    sqrt( [N * sum fi.* xi^2 - (sum fi.* xi)^2] * [N * sum f.j * yj^2 - (sum f.j * yj)^2] )
```

where:
- `N` = total frequency
- `fij` = frequency in cell (i, j)
- `xi` = class mark of i-th x class
- `yj` = class mark of j-th y class
- `fi.` = marginal frequency of i-th x class (row total)
- `f.j` = marginal frequency of j-th y class (column total)

#### Example 3: Grouped Data

Using the bivariate frequency table from Lecture 5:

| x \ y | 10-20 | 20-30 | 30-40 | 40-50 | fi. |
|---|---|---|---|---|---|
| 10-20 | 4 | 1 | 0 | 0 | 5 |
| 20-30 | 0 | 7 | 1 | 0 | 8 |
| 30-40 | 0 | 1 | 9 | 0 | 10 |
| 40-50 | 0 | 0 | 2 | 5 | 7 |
| f.j | 4 | 9 | 12 | 5 | N=30 |

Class marks: x: 15, 25, 35, 45 and y: 15, 25, 35, 45

**Step 1: Compute marginal sums.**

```
sum fi.*xi = 5*15 + 8*25 + 10*35 + 7*45 = 75 + 200 + 350 + 315 = 940
sum fi.*xi^2 = 5*225 + 8*625 + 10*1225 + 7*2025 = 1125 + 5000 + 12250 + 14175 = 32550
sum f.j*yj = 4*15 + 9*25 + 12*35 + 5*45 = 60 + 225 + 420 + 225 = 930
sum f.j*yj^2 = 4*225 + 9*625 + 12*1225 + 5*2025 = 900 + 5625 + 14700 + 10125 = 31350
```

**Step 2: Compute sum of fij * xi * yj for each cell.**

| x\y | y=15 | y=25 | y=35 | y=45 | Row sum fij*xi*yj |
|---|---|---|---|---|---|
| x=15 | 4*15*15=900 | 1*15*25=375 | 0 | 0 | 1275 |
| x=25 | 0 | 7*25*25=4375 | 1*25*35=875 | 0 | 5250 |
| x=35 | 0 | 1*35*25=875 | 9*35*35=11025 | 0 | 11900 |
| x=45 | 0 | 0 | 2*45*35=3150 | 5*45*45=10125 | 13275 |
| **Total** | | | | | **31700** |

```
sum sum fij*xi*yj = 31700
```

**Step 3: Apply formula.**

```
Numerator = N*sum sum fij*xi*yj - (sum fi.*xi)*(sum f.j*yj)
          = 30*31700 - 940*930
          = 951000 - 874200
          = 76800

Denominator = sqrt( [N*sum fi.*xi^2 - (sum fi.*xi)^2] * [N*sum f.j*yj^2 - (sum f.j*yj)^2] )
            = sqrt( [30*32550 - 940^2] * [30*31350 - 930^2] )
            = sqrt( [976500 - 883600] * [940500 - 864900] )
            = sqrt( 92900 * 75600 )
            = sqrt( 7023240000 )
            = 83804.8

r = 76800 / 83804.8 = 0.916
```

Interpretation: Strong positive correlation (r = 0.916) between Mathematics and Statistics marks.

---

### 4. Properties of Correlation Coefficient

1. **Range:** `-1 <= r <= +1`
2. **Unit-free:** r is independent of the units of measurement.
3. **Symmetry:** `r(x, y) = r(y, x)`
4. **Linear measure:** r measures only linear relationships.
5. **Effect of scaling:** If we change the scale (multiply by a constant), r remains unchanged. If we multiply x by a and y by b (a, b > 0), r is unchanged.
6. **Effect of adding constants:** Adding constants does not change r.
7. **r = +1:** Perfect positive linear correlation.
8. **r = -1:** Perfect negative linear correlation.
9. **r = 0:** No linear correlation.
10. **r is a parameter of the population (rho) estimated by the sample statistic r.**

---

### 5. Interpretation of r Values

| Value of r | Interpretation |
|---|---|
| r = +1 | Perfect positive correlation |
| +0.8 to +0.99 | Very strong positive correlation |
| +0.6 to +0.79 | Strong positive correlation |
| +0.4 to +0.59 | Moderate positive correlation |
| +0.2 to +0.39 | Weak positive correlation |
| 0 to +0.19 | Very weak or no correlation |
| 0 | No linear correlation |
| -0.01 to -0.19 | Very weak negative correlation |
| -0.2 to -0.39 | Weak negative correlation |
| -0.4 to -0.59 | Moderate negative correlation |
| -0.6 to -0.79 | Strong negative correlation |
| -0.8 to -0.99 | Very strong negative correlation |
| r = -1 | Perfect negative correlation |

---

### 6. Important Caveats

1. **Correlation does not imply causation.** A high correlation between ice cream sales and drowning does not mean ice cream causes drowning. Both are influenced by a third variable (temperature).

2. **Outliers can dramatically affect r.** Always check the scatter plot.

3. **r measures only linear relationships.** Two variables could have a perfect non-linear relationship (e.g., y = x^2) and r could be close to zero.

4. **Spurious correlation:** Two unrelated variables may appear correlated by chance or due to a third factor.

5. **Range restriction:** r may be small if the range of x or y is restricted.

---

### 7. Coefficient of Determination

The square of the correlation coefficient, `r^2`, is called the **coefficient of determination**.

- `r^2` represents the proportion of variance in y that is explained by x.
- Range: `0 <= r^2 <= 1`
- If r = 0.8, then r^2 = 0.64, meaning 64% of the variation in y is explained by x.

---

## Practice Problems

1. Compute Karl Pearson's correlation coefficient for:

| x | 5 | 10 | 15 | 20 | 25 |
|---|---|---|---|---|---|
| y | 8 | 12 | 16 | 20 | 24 |

2. For the data:

| x | 3 | 6 | 9 | 12 | 15 |
|---|---|---|---|---|---|
| y | 14 | 12 | 8 | 6 | 4 |

Find r and interpret.

3. If r = 0.6 between two variables, what is the coefficient of determination? Interpret it.

4. For the following bivariate frequency table, find r:

| x\y | 0-10 | 10-20 | 20-30 |
|---|---|---|---|
| 10-20 | 3 | 4 | 1 |
| 20-30 | 2 | 5 | 3 |
| 30-40 | 1 | 3 | 5 |

5. Explain why correlation does not imply causation, using an example.

**Answers/Hints:**
1. sum x = 75, sum y = 80, sum xy = 1300, sum x^2 = 1375, sum y^2 = 1440.
   Numerator = 5*1300 - 75*80 = 6500 - 6000 = 500.
   Denominator = sqrt((5*1375 - 5625)*(5*1440 - 6400)) = sqrt((6875-5625)*(7200-6400)) = sqrt(1250*800) = sqrt(1000000) = 1000.
   r = 500/1000 = 0.5. Moderate positive correlation.

2. sum x = 45, sum y = 44, sum xy = 144, sum x^2 = 495, sum y^2 = 456.
   Numerator = 5*144 - 45*44 = 720 - 1980 = -1260.
   Denominator = sqrt((5*495-2025)*(5*456-1936)) = sqrt((2475-2025)*(2280-1936)) = sqrt(450*344) = sqrt(154800) = 393.45.
   r = -1260/393.45 = -3.20. Wait, this is impossible since |r| <= 1.
   Recheck: sum x = 3+6+9+12+15 = 45. sum y = 14+12+8+6+4 = 44. sum xy = 3*14 + 6*12 + 9*8 + 12*6 + 15*4 = 42+72+72+72+60 = 318.
   Numerator = 5*318 - 45*44 = 1590 - 1980 = -390.
   Denominator = sqrt((5*495-2025)*(5*456-1936)) = sqrt(450*344) = sqrt(154800) = 393.45.
   r = -390/393.45 = -0.991. Strong negative correlation.

3. r^2 = 0.36. So 36% of the variation in y is explained by x. The remaining 64% is due to other factors.

4. Midpoints: x: 15, 25, 35. y: 5, 15, 25.
   Row totals: 8, 10, 9. Col totals: 6, 12, 9. N = 27.
   sum fi.*xi = 8*15 + 10*25 + 9*35 = 120+250+315 = 685.
   sum fi.*xi^2 = 8*225 + 10*625 + 9*1225 = 1800+6250+11025 = 19075.
   sum f.j*yj = 6*5 + 12*15 + 9*25 = 30+180+225 = 435.
   sum f.j*yj^2 = 6*25 + 12*225 + 9*625 = 150+2700+5625 = 8475.
   sum sum fij*xi*yj = 3*15*5 + 4*15*15 + 1*15*25 + 2*25*5 + 5*25*15 + 3*25*25 + 1*35*5 + 3*35*15 + 5*35*25
   = 225 + 900 + 375 + 250 + 1875 + 1875 + 175 + 1575 + 4375 = 11625.
   Numerator = 27*11625 - 685*435 = 313875 - 297975 = 15900.
   Denom = sqrt((27*19075-685^2)*(27*8475-435^2)) = sqrt((515025-469225)*(228825-189225)) = sqrt(45800*39600) = sqrt(1813680000) = 42587.3.
   r = 15900/42587.3 = 0.373. Weak positive correlation.

5. Example: There is a high positive correlation between the number of firefighters at a fire and the damage caused. This does not mean firefighters cause damage -- rather, bigger fires require more firefighters and also cause more damage. The third variable (size of fire) explains the correlation.
