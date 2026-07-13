# Measures of Central Tendency and Dispersion

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 2  
**Date:** 10-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 2.9,2.14,2.18

## Notes

### Part A: Measures of Central Tendency

Central tendency measures describe the center or typical value of a data set. The three main measures are: **Mean**, **Median**, and **Mode**.

---

#### 1. Mean (Arithmetic Mean)

**1.1 Mean for Raw Data (Ungrouped Data)**

If we have n observations: `x1, x2, x3, ..., xn`, the arithmetic mean is:

```
x_bar = (x1 + x2 + ... + xn) / n = (sum_{i=1}^{n} x_i) / n
```

**Example 1:** Find the mean of: 12, 15, 18, 21, 24.

Solution:
```
Sum = 12 + 15 + 18 + 21 + 24 = 90
n = 5
x_bar = 90 / 5 = 18
```

**1.2 Weighted Mean**

When observations have different weights (importance), we use the weighted mean:

```
x_w = (w1*x1 + w2*x2 + ... + wn*xn) / (w1 + w2 + ... + wn)
```

**Example 2:** A student's grades are: Midterm (weight 40%) = 75, Final (weight 50%) = 82, Quiz (weight 10%) = 90. Find the weighted mean.

Solution:
```
x_w = (0.40*75 + 0.50*82 + 0.10*90) / (0.40 + 0.50 + 0.10)
    = (30 + 41 + 9) / 1.00
    = 80
```

**1.3 Combined Mean (Mean of Two or More Groups)**

If we have k groups with sizes n1, n2, ..., nk and means x_bar1, x_bar2, ..., x_bark, the combined mean is:

```
x_bar_combined = (n1*x_bar1 + n2*x_bar2 + ... + nk*x_bark) / (n1 + n2 + ... + nk)
```

**Example 3:** Class A has 30 students with mean marks 72. Class B has 20 students with mean marks 80. Find the combined mean.

Solution:
```
x_bar_c = (30*72 + 20*80) / (30 + 20) = (2160 + 1600) / 50 = 3760 / 50 = 75.2
```

**1.4 Mean for Grouped Data (Frequency Distribution)**

For grouped data with class marks (midpoints) `xi` and frequencies `fi`:

```
x_bar = (sum fi*xi) / (sum fi) = (sum fi*xi) / N
```
where `N = sum fi` is the total frequency.

**Step-by-step process:**
1. Find the class mark (midpoint) of each class: `xi = (Lower limit + Upper limit) / 2`
2. Multiply each class mark by its frequency: `fi * xi`
3. Sum all `fi * xi` values
4. Divide by total frequency N

**Example 4:** Find the mean for the following grouped data:

| Class Interval | Frequency (fi) |
|---|---|
| 0-10 | 5 |
| 10-20 | 8 |
| 20-30 | 12 |
| 30-40 | 7 |
| 40-50 | 3 |

Solution:
```
Step 1: Find class marks.
Class 0-10: xi = (0+10)/2 = 5
Class 10-20: xi = (10+20)/2 = 15
Class 20-30: xi = (20+30)/2 = 25
Class 30-40: xi = (30+40)/2 = 35
Class 40-50: xi = (40+50)/2 = 45

Step 2: Compute fi*xi.
5*5 = 25
8*15 = 120
12*25 = 300
7*35 = 245
3*45 = 135

Step 3: sum fi*xi = 25 + 120 + 300 + 245 + 135 = 825
Step 4: N = sum fi = 5 + 8 + 12 + 7 + 3 = 35

x_bar = 825 / 35 = 23.57
```

---

#### 2. Median

The median is the middle value when data is arranged in ascending or descending order. It divides the data into two equal halves.

**2.1 Median for Raw Data**

- If n is odd: Median = value at position `(n+1)/2`
- If n is even: Median = average of values at positions `n/2` and `(n/2 + 1)`

**Example 5:** Find the median of: 5, 2, 8, 12, 1, 7, 9.

Solution:
```
Step 1: Arrange in ascending order: 1, 2, 5, 7, 8, 9, 12
Step 2: n = 7 (odd)
Step 3: Position = (7+1)/2 = 4th value
Step 4: Median = 7
```

**Example 6:** Find the median of: 3, 6, 1, 9, 4, 8.

Solution:
```
Step 1: Arrange: 1, 3, 4, 6, 8, 9
Step 2: n = 6 (even)
Step 3: Positions: n/2 = 3rd value (4) and (n/2 + 1) = 4th value (6)
Step 4: Median = (4 + 6) / 2 = 5
```

**2.2 Median for Grouped Data**

Formula:

```
Median = L + [(N/2 - cf) / f] * h
```

where:
- L = lower limit of median class
- N = total frequency (sum fi)
- cf = cumulative frequency of the class preceding the median class
- f = frequency of the median class
- h = class width

**Step-by-step process:**
1. Compute cumulative frequencies
2. Find N/2
3. Identify the median class (the class where cumulative frequency >= N/2)
4. Apply the formula

**Example 7:** Find the median for the data:

| Class | Frequency | Cumulative Frequency |
|---|---|---|
| 0-10 | 5 | 5 |
| 10-20 | 8 | 13 |
| 20-30 | 12 | 25 |
| 30-40 | 7 | 32 |
| 40-50 | 3 | 35 |

Solution:
```
N = 35, N/2 = 17.5
Median class: 20-30 (since cf = 25 >= 17.5)
L = 20, cf = 13, f = 12, h = 10

Median = 20 + [(17.5 - 13) / 12] * 10
       = 20 + (4.5 / 12) * 10
       = 20 + 3.75
       = 23.75
```

---

#### 3. Mode

The mode is the value that occurs most frequently in a data set. A data set can have one mode (unimodal), two modes (bimodal), or more (multimodal).

**3.1 Mode for Raw Data**

Simply identify the value that appears most often.

**Example 8:** Find the mode: 2, 5, 5, 7, 8, 5, 9, 3.

Solution: 5 appears 3 times (most frequent). Mode = 5.

**3.2 Mode for Grouped Data**

Formula:

```
Mode = L + [(f1 - f0) / (2f1 - f0 - f2)] * h
```

where:
- L = lower limit of modal class (class with highest frequency)
- f1 = frequency of modal class
- f0 = frequency of class preceding modal class
- f2 = frequency of class succeeding modal class
- h = class width

**Example 9:** Find the mode for:

| Class | Frequency |
|---|---|
| 0-10 | 5 |
| 10-20 | 8 |
| 20-30 | 12 |
| 30-40 | 7 |
| 40-50 | 3 |

Solution:
```
Modal class: 20-30 (highest frequency = 12)
L = 20, f1 = 12, f0 = 8, f2 = 7, h = 10

Mode = 20 + [(12 - 8) / (2*12 - 8 - 7)] * 10
     = 20 + [4 / (24 - 15)] * 10
     = 20 + (4/9) * 10
     = 20 + 4.44
     = 24.44
```

**Empirical relationship for moderately skewed distributions:**
```
Mode = 3 * Median - 2 * Mean
```

---

### Part B: Measures of Dispersion

Measures of dispersion quantify the spread or variability in data. Central tendency alone is insufficient -- two data sets can have the same mean but very different spreads.

---

#### 4. Range

The simplest measure of dispersion.

```
Range = Maximum value - Minimum value
```

**Example 10:** Data: 5, 12, 8, 21, 3, 15. Range = 21 - 3 = 18.

**Coefficient of Range:**
```
Coefficient of Range = (Max - Min) / (Max + Min)
```

---

#### 5. Quartile Deviation (Semi-Interquartile Range)

Quartiles divide data into four equal parts:
- Q1 (First Quartile or Lower Quartile): 25th percentile
- Q2 (Second Quartile or Median): 50th percentile
- Q3 (Third Quartile or Upper Quartile): 75th percentile

```
Quartile Deviation (QD) = (Q3 - Q1) / 2
```

**Coefficient of Quartile Deviation:**
```
Coefficient of QD = (Q3 - Q1) / (Q3 + Q1)
```

**Example 11:** Find Q1, Q3, QD for: 3, 6, 7, 8, 9, 11, 13, 15, 18.

Solution:
```
n = 9
Q1 position = (n+1)/4 = 10/4 = 2.5 => Q1 = average of 2nd and 3rd values
             = (6 + 7)/2 = 6.5
Q3 position = 3(n+1)/4 = 3*10/4 = 30/4 = 7.5 => Q3 = average of 7th and 8th values
             = (13 + 15)/2 = 14
QD = (14 - 6.5) / 2 = 3.75
```

---

#### 6. Mean Deviation

Mean deviation is the average of absolute deviations from a measure of central tendency (usually mean or median).

```
MD = (sum |xi - x_bar|) / n   (for raw data)
MD = (sum fi * |xi - x_bar|) / N   (for grouped data)
```

**Coefficient of Mean Deviation:**
```
Coefficient of MD = MD / (mean or median)
```

**Example 12:** Find mean deviation about the mean for: 5, 8, 10, 12, 15.

Solution:
```
Mean = (5+8+10+12+15)/5 = 50/5 = 10
Deviations: |5-10|=5, |8-10|=2, |10-10|=0, |12-10|=2, |15-10|=5
Sum of deviations = 5+2+0+2+5 = 14
MD = 14/5 = 2.8
```

---

#### 7. Variance and Standard Deviation

Variance is the average of squared deviations from the mean. Standard deviation is the square root of variance. These are the most important measures of dispersion.

**7.1 Variance and Standard Deviation for Raw Data**

```
Population variance: sigma^2 = sum (xi - mu)^2 / N
Sample variance: s^2 = sum (xi - x_bar)^2 / (n - 1)

Population standard deviation: sigma = sqrt(sigma^2)
Sample standard deviation: s = sqrt(s^2)
```

**Computational formula (easier for calculation):**

```
sigma^2 = [sum xi^2 / N] - [sum xi / N]^2 = (sum xi^2 / N) - (x_bar)^2
```

**Step-by-step process:**
1. Calculate the mean x_bar
2. Find deviations (xi - x_bar)
3. Square the deviations
4. Sum the squared deviations
5. Divide by n (population) or (n-1) (sample)
6. Take square root for standard deviation

**Example 13:** Find variance and standard deviation for: 10, 12, 15, 18, 20.

Solution:
```
Step 1: Mean = (10+12+15+18+20)/5 = 75/5 = 15
Step 2 & 3:
xi     xi - x_bar    (xi - x_bar)^2
10     -5            25
12     -3            9
15     0             0
18     3             9
20     5             25
Step 4: sum = 25+9+0+9+25 = 68
Step 5: sigma^2 = 68/5 = 13.6 (population variance)
Step 6: sigma = sqrt(13.6) = 3.69

Using computational formula:
sum xi = 75, sum xi^2 = 100+144+225+324+400 = 1193
sigma^2 = 1193/5 - (75/5)^2 = 238.6 - 225 = 13.6
```

**7.2 Variance and Standard Deviation for Grouped Data**

```
sigma^2 = [sum fi*xi^2 / N] - [sum fi*xi / N]^2
```

**Example 14:** Find variance for the grouped data:

| Class | fi | xi | fi*xi | fi*xi^2 |
|---|---|---|---|---|
| 0-10 | 5 | 5 | 25 | 125 |
| 10-20 | 8 | 15 | 120 | 1800 |
| 20-30 | 12 | 25 | 300 | 7500 |
| 30-40 | 7 | 35 | 245 | 8575 |
| 40-50 | 3 | 45 | 135 | 6075 |
| Total | 35 | | 825 | 24075 |

```
sigma^2 = 24075/35 - (825/35)^2
       = 687.86 - (23.57)^2
       = 687.86 - 555.54
       = 132.32
sigma = sqrt(132.32) = 11.50
```

---

#### 8. Summary Table of Dispersion Measures

| Measure | Formula | Unit | Pros | Cons |
|---|---|---|---|---|
| Range | Max - Min | Same as data | Simple | Affected by outliers |
| Quartile Deviation | (Q3 - Q1)/2 | Same as data | Not affected by outliers | Ignores half the data |
| Mean Deviation | sum \|xi - x_bar\| / n | Same as data | Uses all data | Absolute values are hard to work with mathematically |
| Standard Deviation | sqrt(sum (xi - mu)^2 / N) | Same as data | Most commonly used, mathematically tractable | Affected by outliers |

---

## Practice Problems

1. Find the mean, median, and mode for: 11, 14, 17, 14, 19, 22, 14, 25.
2. The mean of 10 observations is 15. If one observation 8 is removed, find the new mean.
3. For the following grouped data, find the mean and standard deviation:

| Class | Frequency |
|---|---|
| 0-10 | 4 |
| 10-20 | 6 |
| 20-30 | 10 |
| 30-40 | 8 |
| 40-50 | 2 |

4. Calculate Q1, Q3, and Quartile Deviation for: 5, 8, 12, 15, 18, 20, 22, 25, 28, 30.
5. Two groups have means 65 and 75 with sizes 40 and 60 respectively. Find the combined mean.

**Answers/Hints:**
1. Mean = 17, Median = 14 (arrange: 11,14,14,14,17,19,22,25; n=8 even, avg of 4th and 5th = (14+17)/2 = 15.5), Mode = 14. (Note: mean = (11+14+14+14+17+19+22+25)/8 = 136/8 = 17)
2. Sum = 10*15 = 150. New sum = 150 - 8 = 142. New n = 9. New mean = 142/9 = 15.78.
3. Mean = (4*5 + 6*15 + 10*25 + 8*35 + 2*45)/30 = (20+90+250+280+90)/30 = 730/30 = 24.33.
   Variance = (4*25 + 6*225 + 10*625 + 8*1225 + 2*2025)/30 - (24.33)^2 = (100+1350+6250+9800+4050)/30 - 592.0 = 21550/30 - 592 = 718.33 - 592 = 126.33. SD = sqrt(126.33) = 11.24.
4. n=10, Q1 at position (n+1)/4 = 2.75, Q1 = 8 + 0.75*(12-8) = 11. Q3 at position 3(n+1)/4 = 8.25, Q3 = 25 + 0.25*(28-25) = 25.75. QD = (25.75 - 11)/2 = 7.375.
5. Combined mean = (40*65 + 60*75) / (40+60) = (2600 + 4500) / 100 = 7100/100 = 71.
