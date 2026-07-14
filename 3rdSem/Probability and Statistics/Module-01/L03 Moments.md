# Moments

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 3  
**Date:** 14-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 2.53

## Notes

### 1. Introduction to Moments

Moments are quantitative measures that describe the shape and characteristics of a frequency distribution. They provide a systematic way to summarize the properties of a data set. The first four moments are used to describe:

- **First moment:** Central tendency (mean)
- **Second moment:** Dispersion (variance)
- **Third moment:** Skewness (asymmetry)
- **Fourth moment:** Kurtosis (peakedness)

There are two types of moments:
1. **Moments about the origin (Raw moments)** -- denoted by `mu_r'`
2. **Moments about the mean (Central moments)** -- denoted by `mu_r`

---

### 2. Raw Moments (Moments about Origin)

The **r-th raw moment** is defined as the average of the r-th power of the observations.

**For raw data (ungrouped):**

```
mu_r' = (x1^r + x2^r + ... + xn^r) / n = (1/n) * sum_{i=1}^{n} xi^r
```

**For grouped data (frequency distribution):**

```
mu_r' = (sum_{i=1}^{k} fi * xi^r) / N
```

where `N = sum fi`, `k` is the number of classes, `xi` are class marks, and `fi` are frequencies.

#### Special Cases:

- **First raw moment (r = 1):**
  ```
  mu_1' = (sum xi) / n = x_bar
  ```
  This is simply the arithmetic mean.

- **Second raw moment (r = 2):**
  ```
  mu_2' = (sum xi^2) / n
  ```

- **Third raw moment (r = 3):**
  ```
  mu_3' = (sum xi^3) / n
  ```

- **Fourth raw moment (r = 4):**
  ```
  mu_4' = (sum xi^4) / n
  ```

---

### 3. Central Moments (Moments about the Mean)

The **r-th central moment** is defined as the average of the r-th power of deviations from the mean.

**For raw data:**

```
mu_r = (1/n) * sum_{i=1}^{n} (xi - x_bar)^r
```

**For grouped data:**

```
mu_r = (1/N) * sum_{i=1}^{k} fi * (xi - x_bar)^r
```

#### Special Cases:

- **First central moment (r = 1):**
  ```
  mu_1 = (1/n) * sum (xi - x_bar) = 0
  ```
  The sum of deviations from the mean is always zero.

- **Second central moment (r = 2):**
  ```
  mu_2 = (1/n) * sum (xi - x_bar)^2 = sigma^2
  ```
  This is the population variance.

- **Third central moment (r = 3):**
  ```
  mu_3 = (1/n) * sum (xi - x_bar)^3
  ```
  Used to measure skewness.

- **Fourth central moment (r = 4):**
  ```
  mu_4 = (1/n) * sum (xi - x_bar)^4
  ```
  Used to measure kurtosis.

---

### 4. Relationship Between Raw Moments and Central Moments

Central moments can be expressed in terms of raw moments. This is useful because raw moments are easier to compute (no need to calculate deviations from mean first).

Let `mu_1' = x_bar` (the mean).

The relationships are:

```
mu_1 = 0

mu_2 = mu_2' - (mu_1')^2

mu_3 = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3

mu_4 = mu_4' - 4*mu_3'*mu_1' + 6*mu_2'*(mu_1')^2 - 3*(mu_1')^4
```

#### Derivation of mu_2:

```
mu_2 = (1/n) * sum (xi - x_bar)^2
     = (1/n) * sum (xi^2 - 2*xi*x_bar + x_bar^2)
     = (1/n) * sum xi^2 - 2*x_bar*(1/n)*sum xi + x_bar^2
     = mu_2' - 2*x_bar*x_bar + x_bar^2
     = mu_2' - 2*(mu_1')^2 + (mu_1')^2
     = mu_2' - (mu_1')^2
```

#### Derivation of mu_3:

```
mu_3 = (1/n) * sum (xi - x_bar)^3
     = (1/n) * sum (xi^3 - 3*xi^2*x_bar + 3*xi*x_bar^2 - x_bar^3)
     = mu_3' - 3*x_bar*mu_2' + 3*x_bar^2*x_bar - x_bar^3
     = mu_3' - 3*mu_1'*mu_2' + 3*(mu_1')^3 - (mu_1')^3
     = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3
```

#### Derivation of mu_4:

```
mu_4 = (1/n) * sum (xi - x_bar)^4
     = (1/n) * sum (xi^4 - 4*xi^3*x_bar + 6*xi^2*x_bar^2 - 4*xi*x_bar^3 + x_bar^4)
     = mu_4' - 4*x_bar*mu_3' + 6*x_bar^2*mu_2' - 4*x_bar^3*x_bar + x_bar^4
     = mu_4' - 4*mu_1'*mu_3' + 6*(mu_1')^2*mu_2' - 4*(mu_1')^4 + (mu_1')^4
     = mu_4' - 4*mu_3'*mu_1' + 6*mu_2'*(mu_1')^2 - 3*(mu_1')^4
```

---

### 5. Worked Example: Computing First Four Moments

**Problem:** For the following data, compute the first four raw moments and the first four central moments.

Data: 2, 4, 6, 8, 10

#### Step 1: Compute raw moments

| xi | xi^2 | xi^3 | xi^4 |
|---|---|---|---|
| 2 | 4 | 8 | 16 |
| 4 | 16 | 64 | 256 |
| 6 | 36 | 216 | 1296 |
| 8 | 64 | 512 | 4096 |
| 10 | 100 | 1000 | 10000 |
| sum = 30 | sum = 220 | sum = 1800 | sum = 15664 |

```
mu_1' = 30 / 5 = 6
mu_2' = 220 / 5 = 44
mu_3' = 1800 / 5 = 360
mu_4' = 15664 / 5 = 3132.8
```

#### Step 2: Compute central moments using relationships

```
mu_1 = 0
mu_2 = mu_2' - (mu_1')^2 = 44 - 6^2 = 44 - 36 = 8
mu_3 = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3
     = 360 - 3*44*6 + 2*6^3
     = 360 - 792 + 432
     = 0
mu_4 = mu_4' - 4*mu_3'*mu_1' + 6*mu_2'*(mu_1')^2 - 3*(mu_1')^4
     = 3132.8 - 4*360*6 + 6*44*36 - 3*6^4
     = 3132.8 - 8640 + 9504 - 3888
     = 108.8
```

#### Step 3: Verification by direct computation

Compute deviations from mean (x_bar = 6):

| xi | xi - x_bar | (xi - x_bar)^2 | (xi - x_bar)^3 | (xi - x_bar)^4 |
|---|---|---|---|---|
| 2 | -4 | 16 | -64 | 256 |
| 4 | -2 | 4 | -8 | 16 |
| 6 | 0 | 0 | 0 | 0 |
| 8 | 2 | 4 | 8 | 16 |
| 10 | 4 | 16 | 64 | 256 |
| sum | 0 | 40 | 0 | 544 |

```
mu_1 = 0/5 = 0 (verified)
mu_2 = 40/5 = 8 (verified)
mu_3 = 0/5 = 0 (verified)
mu_4 = 544/5 = 108.8 (verified)
```

#### Interpretation:
- `mu_2 = 8` is the population variance. Standard deviation = sqrt(8) = 2.83.
- `mu_3 = 0` indicates the distribution is symmetric (no skewness).
- `mu_4 = 108.8` will be used to compute kurtosis.

---

### 6. Worked Example with Grouped Data

**Problem:** Compute the first four moments for the following frequency distribution.

| Class | Frequency (fi) |
|---|---|
| 0-10 | 5 |
| 10-20 | 8 |
| 20-30 | 12 |
| 30-40 | 7 |
| 40-50 | 3 |

#### Step 1: Create computation table

| Class | fi | xi | fi*xi | fi*xi^2 | fi*xi^3 | fi*xi^4 |
|---|---|---|---|---|---|---|
| 0-10 | 5 | 5 | 25 | 125 | 625 | 3125 |
| 10-20 | 8 | 15 | 120 | 1800 | 27000 | 405000 |
| 20-30 | 12 | 25 | 300 | 7500 | 187500 | 4687500 |
| 30-40 | 7 | 35 | 245 | 8575 | 300125 | 10504375 |
| 40-50 | 3 | 45 | 135 | 6075 | 273375 | 12301875 |
| **Total** | **N=35** | | **825** | **24075** | **788625** | **27901875** |

#### Step 2: Raw moments

```
mu_1' = 825 / 35 = 23.5714
mu_2' = 24075 / 35 = 687.8571
mu_3' = 788625 / 35 = 22532.1429
mu_4' = 27901875 / 35 = 797196.4286
```

#### Step 3: Central moments

```
mu_1 = 0
mu_2 = mu_2' - (mu_1')^2 = 687.8571 - (23.5714)^2 = 687.8571 - 555.6122 = 132.2449
mu_3 = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3
     = 22532.1429 - 3*687.8571*23.5714 + 2*(23.5714)^3
     = 22532.1429 - 48646.4286 + 2*13095.9184
     = 22532.1429 - 48646.4286 + 26191.8368
     = 77.5511
mu_4 = mu_4' - 4*mu_3'*mu_1' + 6*mu_2'*(mu_1')^2 - 3*(mu_1')^4
     = 797196.4286 - 4*22532.1429*23.5714 + 6*687.8571*(23.5714)^2 - 3*(23.5714)^4
     = 797196.4286 - 2124387.7554 + 6*687.8571*555.6122 - 3*308739.5918
     = 797196.4286 - 2124387.7554 + 2292857.1429 - 926218.7754
     = 39447.0407
```

---

### 7. Key Points to Remember

1. Raw moments are computed about the origin (zero). Central moments are computed about the mean.
2. `mu_1 = 0` always (deviations from mean sum to zero).
3. `mu_2 = sigma^2` (variance).
4. The formulas converting raw to central moments are derived from the binomial expansion of `(xi - x_bar)^r`.
5. For computation, it is usually easier to first compute raw moments, then convert to central moments.
6. Moments are dimensionless when normalized appropriately (we will see this in skewness and kurtosis).

#### Summary of Relationships

| Raw Moment | Central Moment Relationship |
|---|---|
| `mu_1'` | `mu_1 = 0` |
| `mu_2'` | `mu_2 = mu_2' - (mu_1')^2` |
| `mu_3'` | `mu_3 = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3` |
| `mu_4'` | `mu_4 = mu_4' - 4*mu_3'*mu_1' + 6*mu_2'*(mu_1')^2 - 3*(mu_1')^4` |

---

## Practice Problems

1. For the data: 5, 7, 9, 11, 13, compute the first four raw moments and the first four central moments.
   <details>
   <summary>Show Answer</summary>
   1. `mu_1' = 9`, `mu_2' = 89`, `mu_3' = 945`, `mu_4' = 10505`. Central: `mu_1 = 0`, `mu_2 = 8`, `mu_3 = 0`, `mu_4 = 97.6`. (Check: mean = 9; deviations sum to 0, symmetric.)
   </details>

2. For the data: 3, 6, 9, 12, 15, 18, compute `mu_2` and `mu_3`. Is the distribution symmetric?
   <details>
   <summary>Show Answer</summary>
   2. `mu_1' = 10.5`, `mu_2' = 124.5`, `mu_3' = 1606.5`. `mu_2 = 124.5 - 10.5^2 = 14.25`. `mu_3 = 1606.5 - 3*124.5*10.5 + 2*10.5^3 = 1606.5 - 3921.75 + 2315.25 = 0`. Yes, symmetric.
   </details>

3. The first two raw moments of a distribution are `mu_1' = 10` and `mu_2' = 125`. Find the variance `mu_2`.
   <details>
   <summary>Show Answer</summary>
   3. `mu_2 = 125 - 10^2 = 25`.
   </details>

4. Show that `mu_3` can be expressed as `mu_3 = mu_3' - 3*mu_2'*mu_1' + 2*(mu_1')^3` by expanding `(x - mu)^3`.
   <details>
   <summary>Show Answer</summary>
   4. Expand `(x - mu)^3 = x^3 - 3x^2*mu + 3x*mu^2 - mu^3`. Take expectation (average) of both sides: `E[(x-mu)^3] = E[x^3] - 3*mu*E[x^2] + 3*mu^2*E[x] - mu^3 = mu_3' - 3*mu*mu_2' + 3*mu^2*mu_1' - mu^3`. Since `mu_1' = mu`, this gives `mu_3 = mu_3' - 3*mu_2'*mu + 2*mu^3`.
   </details>

5. For a grouped data set with `N = 50`, `sum fi*xi = 600`, `sum fi*xi^2 = 9000`, `sum fi*xi^3 = 150000`, and `sum fi*xi^4 = 2700000`, compute all four central moments.
   <details>
   <summary>Show Answer</summary>
   5. `mu_1' = 12`, `mu_2' = 180`, `mu_3' = 3000`, `mu_4' = 54000`. `mu_2 = 180 - 144 = 36`. `mu_3 = 3000 - 3*180*12 + 2*12^3 = 3000 - 6480 + 3456 = -24`. `mu_4 = 54000 - 4*3000*12 + 6*180*12^2 - 3*12^4 = 54000 - 144000 + 155520 - 62208 = 3312`.
   </details>
