# Skewness and Kurtosis

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 4  
**Date:** 16-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Case Studies  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 2.58,2.60

## Notes

### 1. Introduction

After computing measures of central tendency (mean, median, mode) and dispersion (variance, standard deviation), we need to understand the **shape** of a distribution. Two key shape characteristics are:

- **Skewness:** Measures the asymmetry of the distribution.
- **Kurtosis:** Measures the peakedness or flatness of the distribution.

---

### Part A: Skewness

### 2. Definition of Skewness

Skewness refers to the lack of symmetry in a frequency distribution. A distribution is symmetric if the left half is a mirror image of the right half.

#### Types of Skewness

**a) Zero Skewness (Symmetric Distribution):**
- Mean = Median = Mode
- The distribution is perfectly balanced.
- Example: Normal distribution (bell curve).

**b) Positive Skewness (Right-Skewed):**
- Mean > Median > Mode
- The tail on the right side is longer.
- Most values are concentrated on the left.
- Example: Income distribution (most people earn moderate income, few earn very high).

**c) Negative Skewness (Left-Skewed):**
- Mean < Median < Mode
- The tail on the left side is longer.
- Most values are concentrated on the right.
- Example: Age at retirement (most retire around a certain age, some retire early).

#### Visual Comparison

```
Symmetric (Zero Skew):      Positive Skew:           Negative Skew:
    / \                       / \                      / \
   /   \                     /   \                    /   \
  /     \                   /     \                  /     \
 /       \                 /       \                /       \
+---------+               +---------+              +---------+
  Mean=Med=Mode            Mode<Med<Mean            Mean<Med<Mode
```

---

### 3. Measures of Skewness

#### 3.1 Karl Pearson's Coefficient of Skewness

This is the most commonly used measure.

```
Sk_p = (Mean - Mode) / Standard Deviation
```

Since `Mode = 3*Median - 2*Mean` (for moderately skewed distributions), an alternative formula is:

```
Sk_p = 3*(Mean - Median) / Standard Deviation
```

**Interpretation:**
- `Sk_p = 0`: Symmetric distribution
- `Sk_p > 0`: Positive skewness
- `Sk_p < 0`: Negative skewness
- Larger |Sk_p| indicates greater skewness.
- Typically, |Sk_p| lies between -3 and +3, but usually between -1 and +1.

**Example 1:** For a data set, Mean = 45, Median = 42, SD = 8. Find Karl Pearson's coefficient of skewness.

Solution:
```
Sk_p = 3*(45 - 42) / 8 = 3*3/8 = 9/8 = 1.125
```
Interpretation: The distribution is positively skewed. The value 1.125 indicates moderate to high positive skewness.

**Example 2:** For a data set, Mean = 60, Mode = 65, SD = 10.

Solution:
```
Sk_p = (60 - 65) / 10 = -5/10 = -0.5
```
Interpretation: Negative skewness (left-skewed), relatively mild.

#### 3.2 Bowley's Coefficient of Skewness (Quartile-based)

This is based on quartiles and is useful when extreme values are present.

```
Sk_b = (Q3 + Q1 - 2*Q2) / (Q3 - Q1)
```

where Q1 = first quartile, Q2 = median (second quartile), Q3 = third quartile.

**Interpretation:**
- `Sk_b = 0`: Symmetric
- `Sk_b > 0`: Positive skewness
- `Sk_b < 0`: Negative skewness
- Value ranges between -1 and +1.

**Example 3:** For a data set, Q1 = 25, Q2 = 35, Q3 = 50. Find Bowley's coefficient.

Solution:
```
Sk_b = (50 + 25 - 2*35) / (50 - 25) = (75 - 70) / 25 = 5/25 = 0.2
```
Interpretation: Slight positive skewness.

#### 3.3 Moment-based Measure of Skewness

Using the third central moment `mu_3` and standard deviation `sigma`:

**Beta-1 (beta1):**
```
beta1 = mu_3^2 / mu_2^3 = mu_3^2 / sigma^6
```

**Gamma-1 (gamma1) -- also called the coefficient of skewness:**
```
gamma1 = sqrt(beta1) = mu_3 / sigma^3
```

**Interpretation:**
- `gamma1 = 0`: Symmetric distribution
- `gamma1 > 0`: Positive skewness
- `gamma1 < 0`: Negative skewness

**Example 4:** For a distribution, `mu_2 = 4` and `mu_3 = 6`. Find `beta1` and `gamma1`.

Solution:
```
sigma = sqrt(4) = 2
beta1 = 6^2 / 4^3 = 36 / 64 = 0.5625
gamma1 = 6 / (2^3) = 6 / 8 = 0.75
```
Interpretation: Positive skewness (gamma1 > 0).

**Example 5:** For a distribution, `mu_2 = 9` and `mu_3 = -12`. Find `beta1` and `gamma1`.

Solution:
```
sigma = sqrt(9) = 3
beta1 = (-12)^2 / 9^3 = 144 / 729 = 0.1975
gamma1 = -12 / (3^3) = -12 / 27 = -0.444
```
Interpretation: Negative skewness (gamma1 < 0).

---

### 4. Worked Example: Computing Skewness from Raw Data

**Problem:** For the data: 4, 8, 12, 15, 20, 22, 28, compute Karl Pearson's coefficient and the moment-based measure of skewness.

**Step 1: Compute mean, median, mode, and standard deviation.**

```
Data in order: 4, 8, 12, 15, 20, 22, 28
n = 7

Mean = (4+8+12+15+20+22+28)/7 = 109/7 = 15.571

Median = 4th value = 15 (since n=7, position = (7+1)/2 = 4)

Mode: No value repeats, so mode is not uniquely defined.
We will use the formula Mode = 3*Median - 2*Mean = 3*15 - 2*15.571 = 45 - 31.142 = 13.858
```

**Step 2: Compute deviations and variance.**

| xi | xi - x_bar | (xi - x_bar)^2 | (xi - x_bar)^3 |
|---|---|---|---|
| 4 | -11.571 | 133.888 | -1549.26 |
| 8 | -7.571 | 57.320 | -433.97 |
| 12 | -3.571 | 12.752 | -45.54 |
| 15 | -0.571 | 0.326 | -0.19 |
| 20 | 4.429 | 19.616 | 86.88 |
| 22 | 6.429 | 41.332 | 265.72 |
| 28 | 12.429 | 154.480 | 1920.04 |
| **Sum** | **0** | **419.714** | **243.68** |

```
sigma^2 = 419.714 / 7 = 59.959
sigma = sqrt(59.959) = 7.743

mu_3 = 243.68 / 7 = 34.811
```

**Step 3: Karl Pearson's coefficient.**

```
Sk_p = (Mean - Mode) / sigma = (15.571 - 13.858) / 7.743 = 1.713 / 7.743 = 0.221

Or: Sk_p = 3*(Mean - Median) / sigma = 3*(15.571 - 15) / 7.743 = 3*0.571/7.743 = 1.713/7.743 = 0.221
```

**Step 4: Moment-based measure.**

```
gamma1 = mu_3 / sigma^3 = 34.811 / (7.743)^3 = 34.811 / 464.247 = 0.075
```

Interpretation: Both measures show slight positive skewness (values close to zero).

---

### Part B: Kurtosis

### 5. Definition of Kurtosis

Kurtosis measures the peakedness (or flatness) of a distribution compared to the normal distribution.

#### Three Types of Kurtosis

**a) Mesokurtic:**
- Kurtosis equal to that of the normal distribution.
- `beta2 = 3` (or `gamma2 = 0`).
- Moderate peak, moderate tails.

**b) Leptokurtic:**
- More peaked than the normal distribution.
- `beta2 > 3` (or `gamma2 > 0`).
- Heavy tails (more outliers).

**c) Platykurtic:**
- Flatter than the normal distribution.
- `beta2 < 3` (or `gamma2 < 0`).
- Light tails (fewer outliers).

```
Leptokurtic:    Mesokurtic:     Platykurtic:
    /\           / \              ___
   /  \         /   \           /     \
  /    \       /     \         /       \
 /      \     /       \       /         \
+--------+   +---------+     +-----------+
(beta2 > 3)  (beta2 = 3)    (beta2 < 3)
```

---

### 6. Measures of Kurtosis

#### 6.1 Moment-based Measure

**Beta-2 (beta2):**
```
beta2 = mu_4 / mu_2^2 = mu_4 / sigma^4
```

**Gamma-2 (gamma2) -- excess kurtosis:**
```
gamma2 = beta2 - 3
```

**Interpretation:**
- `beta2 = 3` or `gamma2 = 0`: Mesokurtic (normal distribution)
- `beta2 > 3` or `gamma2 > 0`: Leptokurtic
- `beta2 < 3` or `gamma2 < 0`: Platykurtic

**Example 6:** For a distribution, `mu_2 = 16` and `mu_4 = 400`. Find `beta2` and `gamma2`.

Solution:
```
beta2 = 400 / 16^2 = 400 / 256 = 1.5625
gamma2 = 1.5625 - 3 = -1.4375
```
Interpretation: Platykurtic (beta2 < 3).

**Example 7:** For a distribution, `mu_2 = 25` and `mu_4 = 2500`. Find `beta2`.

Solution:
```
beta2 = 2500 / 25^2 = 2500 / 625 = 4
```
Interpretation: Leptokurtic (beta2 > 3).

---

### 7. Worked Example: Computing Both Skewness and Kurtosis

**Problem:** For the data: 2, 5, 7, 9, 11, 13, 15, 17, 19, compute `mu_2`, `mu_3`, `mu_4`, `beta1`, `gamma1`, `beta2`, and `gamma2`. Interpret.

**Step 1: Compute raw moments.**

|x | x^2 | x^3 | x^4 |
|---|---|---|---|
|2 | 4 | 8 | 16 |
|5 | 25 | 125 | 625 |
|7 | 49 | 343 | 2401 |
|9 | 81 | 729 | 6561 |
|11 | 121 | 1331 | 14641 |
|13 | 169 | 2197 | 28561 |
|15 | 225 | 3375 | 50625 |
|17 | 289 | 4913 | 83521 |
|19 | 361 | 6859 | 130321 |
|**98** | **1324** | **19880** | **317272** |

```
n = 9
mu_1' = 98/9 = 10.889
mu_2' = 1324/9 = 147.111
mu_3' = 19880/9 = 2208.889
mu_4' = 317272/9 = 35252.444
```

**Step 2: Compute central moments.**

```
mu_2 = mu_2' - (mu_1')^2 = 147.111 - (10.889)^2 = 147.111 - 118.574 = 28.537
sigma = sqrt(28.537) = 5.342

mu_3 = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3
     = 2208.889 - 3*147.111*10.889 + 2*(10.889)^3
     = 2208.889 - 4804.037 + 2*1291.074
     = 2208.889 - 4804.037 + 2582.148
     = -12.999 ≈ -13

mu_4 = mu_4' - 4*mu_3'*mu_1' + 6*mu_2'*(mu_1')^2 - 3*(mu_1')^4
     = 35252.444 - 4*2208.889*10.889 + 6*147.111*(10.889)^2 - 3*(10.889)^4
     = 35252.444 - 96203.630 + 6*147.111*118.574 - 3*14066.926
     = 35252.444 - 96203.630 + 104641.371 - 42200.778
     = 1489.407
```

**Step 3: Compute skewness measures.**

```
beta1 = mu_3^2 / mu_2^3 = (-13)^2 / (28.537)^3 = 169 / 23237.7 = 0.00727
gamma1 = sqrt(beta1) = mu_3 / sigma^3 = -13 / (5.342)^3 = -13 / 152.443 = -0.0853
```

**Step 4: Compute kurtosis measures.**

```
beta2 = mu_4 / mu_2^2 = 1489.407 / (28.537)^2 = 1489.407 / 814.393 = 1.829
gamma2 = beta2 - 3 = 1.829 - 3 = -1.171
```

**Interpretation:**
- `gamma1 = -0.0853`: Very slight negative skewness (nearly symmetric).
- `beta2 = 1.829`: Since beta2 < 3, the distribution is **platykurtic** (flatter than normal).
- `gamma2 = -1.171`: Confirms platykurtic nature.

---

### 8. Summary Comparison

| Property | Measure | Formula | Range |
|---|---|---|---|
| Skewness | Karl Pearson's | (Mean - Mode)/SD | Typically -3 to +3 |
| Skewness | Bowley's | (Q3+Q1-2Q2)/(Q3-Q1) | -1 to +1 |
| Skewness (moment) | beta1 | mu_3^2 / mu_2^3 | >= 0 |
| Skewness (moment) | gamma1 | mu_3 / sigma^3 | -inf to +inf |
| Kurtosis | beta2 | mu_4 / mu_2^2 | >= 1 |
| Kurtosis | gamma2 | beta2 - 3 | -2 to +inf |

---

## Practice Problems

1. For a distribution, Mean = 50, Median = 55, SD = 10. Compute Karl Pearson's coefficient of skewness and interpret.
2. For a data set, Q1 = 20, Q2 = 30, Q3 = 45. Compute Bowley's coefficient of skewness.
3. For a distribution, `mu_2 = 25` and `mu_3 = 40`. Compute `beta1` and `gamma1`. What do they indicate?
4. For a distribution, `mu_2 = 9` and `mu_4 = 243`. Compute `beta2` and determine the type of kurtosis.
5. For the data: 10, 12, 14, 16, 18, 20, 22, compute `gamma1` and `gamma2`. Interpret the shape.

**Answers/Hints:**
1. `Sk_p = 3*(50-55)/10 = -1.5`. Negative skewness (left-skewed).
2. `Sk_b = (45+20-2*30)/(45-20) = (65-60)/25 = 5/25 = 0.2`. Slight positive skewness.
3. `sigma = 5`. `beta1 = 40^2/25^3 = 1600/15625 = 0.1024`. `gamma1 = 40/125 = 0.32`. Positive skewness.
4. `beta2 = 243/9^2 = 243/81 = 3`. Mesokurtic (same kurtosis as normal distribution).
5. Mean = 16. Deviations: -6,-4,-2,0,2,4,6. `mu_2 = (36+16+4+0+4+16+36)/7 = 112/7 = 16`. `mu_3 = (-216-64-8+0+8+64+216)/7 = 0/7 = 0`. `mu_4 = (1296+256+16+0+16+256+1296)/7 = 3136/7 = 448`. `gamma1 = 0/64 = 0` (symmetric). `beta2 = 448/16^2 = 448/256 = 1.75`. `gamma2 = 1.75-3 = -1.25` (platykurtic).
