# Analysis of bivariate data

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 5  
**Date:** 17-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 20.2

## Notes

### 1. Introduction to Bivariate Data

So far, we have analyzed **univariate data** (one variable at a time). In real-world problems, we often want to study the relationship between **two variables** simultaneously. This is called **bivariate data analysis**.

**Examples of bivariate data:**
- Height and weight of students
- Hours studied and exam score
- Temperature and ice cream sales
- Advertising expenditure and sales revenue

**Goals of bivariate analysis:**
1. Determine whether two variables are related.
2. Measure the strength and direction of the relationship.
3. Predict the value of one variable given the other.

---

### 2. Scatter Diagram (Scatter Plot)

A scatter diagram is the simplest way to visualize bivariate data. Each observation is plotted as a point `(x, y)` on a Cartesian plane.

**How to construct a scatter diagram:**
1. Take the independent variable (x) on the horizontal axis.
2. Take the dependent variable (y) on the vertical axis.
3. Plot each pair `(x, y)` as a point.

**Interpreting scatter diagrams:**

```
Positive Correlation:       Negative Correlation:       No Correlation:
    y                        y                          y
    ^                        ^                          ^
    |    * * *               | * *                      |   *
    |  * * * *               |* * *                     | *   *
    | * * * *                |* *   *                   |  *   *
    |* * *                   |   * *                    |   *
    +--------> x             +--------> x               +--------> x
    (upward trend)           (downward trend)           (random pattern)
```

**Types of relationships visible from scatter plots:**
- **Linear:** Points cluster around a straight line.
- **Non-linear (curvilinear):** Points follow a curve.
- **No relationship:** Points show no pattern.
- **Positive:** As x increases, y increases.
- **Negative:** As x increases, y decreases.

---

### 3. Bivariate Frequency Distribution

When data is numerous, we organize it into a **bivariate frequency table** (also called a **correlation table** or **two-way frequency table**).

#### Structure of a Bivariate Frequency Table

The table has:
- **Rows:** Classes of one variable (say x)
- **Columns:** Classes of the other variable (say y)
- **Cells:** Frequency of observations falling in the corresponding x and y class intervals
- **Row totals:** Frequencies for each x class (called marginal distribution of x)
- **Column totals:** Frequencies for each y class (called marginal distribution of y)

#### General Format:

| x \ y | y1 | y2 | ... | yj | ... | ym | Row Total (fx) |
|---|---|---|---|---|---|---|---|
| x1 | f11 | f12 | ... | f1j | ... | f1m | f1. |
| x2 | f21 | f22 | ... | f2j | ... | f2m | f2. |
| ... | ... | ... | ... | ... | ... | ... | ... |
| xi | fi1 | fi2 | ... | fij | ... | fim | fi. |
| ... | ... | ... | ... | ... | ... | ... | ... |
| xn | fn1 | fn2 | ... | fnj | ... | fnm | fn. |
| **Column Total (fy)** | f.1 | f.2 | ... | f.j | ... | f.m | **N** |

Where:
- `fij` = frequency of pairs where x is in class i and y is in class j
- `fi.` = sum of frequencies in row i (marginal frequency of x)
- `f.j` = sum of frequencies in column j (marginal frequency of y)
- `N = sum(fi.) = sum(f.j)` = total number of observations

---

### 4. Step-by-Step: Constructing a Bivariate Frequency Table

#### Example: Marks of 30 Students in Two Subjects

Consider the marks (out of 50) of 30 students in Mathematics (x) and Statistics (y):

```
Student:  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
x (Math): 22  35  18  42  28  15  38  45  20  30  25  40  33  48  12
y (Stat): 25  32  20  40  30  18  35  42  22  28  28  38  35  45  15

Student: 16  17  18  19  20  21  22  23  24  25  26  27  28  29  30
x (Math): 36  28  44  20  38  15  32  42  25  18  35  30  40  22  33
y (Stat): 33  25  42  24  36  20  30  40  28  22  38  32  35  26  36
```

**Step 1: Determine the range and class intervals for each variable.**

For x (Mathematics):
- Minimum = 12, Maximum = 48
- Range = 48 - 12 = 36
- Choose class width of 10. Classes: 10-20, 20-30, 30-40, 40-50

For y (Statistics):
- Minimum = 15, Maximum = 45
- Range = 45 - 15 = 30
- Choose class width of 10. Classes: 10-20, 20-30, 30-40, 40-50

**Step 2: Create the empty table with row and column headers.**

| x \ y | 10-20 | 20-30 | 30-40 | 40-50 | Row Total |
|---|---|---|---|---|---|
| 10-20 | | | | | |
| 20-30 | | | | | |
| 30-40 | | | | | |
| 40-50 | | | | | |
| **Col Total** | | | | | **30** |

**Step 3: Tally the frequencies for each pair.**

Process each student and place them in the appropriate cell:

```
Student 1:  x=22 (20-30), y=25 (20-30)  -> cell (20-30, 20-30)
Student 2:  x=35 (30-40), y=32 (30-40)  -> cell (30-40, 30-40)
Student 3:  x=18 (10-20), y=20 (10-20)  -> cell (10-20, 10-20)
Student 4:  x=42 (40-50), y=40 (40-50)  -> cell (40-50, 40-50)
Student 5:  x=28 (20-30), y=30 (30-40)  -> cell (20-30, 30-40)
Student 6:  x=15 (10-20), y=18 (10-20)  -> cell (10-20, 10-20)
Student 7:  x=38 (30-40), y=35 (30-40)  -> cell (30-40, 30-40)
Student 8:  x=45 (40-50), y=42 (40-50)  -> cell (40-50, 40-50)
Student 9:  x=20 (20-30), y=22 (20-30)  -> cell (20-30, 20-30)
Student 10: x=30 (30-40), y=28 (20-30)  -> cell (30-40, 20-30)
Student 11: x=25 (20-30), y=28 (20-30)  -> cell (20-30, 20-30)
Student 12: x=40 (40-50), y=38 (30-40)  -> cell (40-50, 30-40)
Student 13: x=33 (30-40), y=35 (30-40)  -> cell (30-40, 30-40)
Student 14: x=48 (40-50), y=45 (40-50)  -> cell (40-50, 40-50)
Student 15: x=12 (10-20), y=15 (10-20)  -> cell (10-20, 10-20)
Student 16: x=36 (30-40), y=33 (30-40)  -> cell (30-40, 30-40)
Student 17: x=28 (20-30), y=25 (20-30)  -> cell (20-30, 20-30)
Student 18: x=44 (40-50), y=42 (40-50)  -> cell (40-50, 40-50)
Student 19: x=20 (20-30), y=24 (20-30)  -> cell (20-30, 20-30)
Student 20: x=38 (30-40), y=36 (30-40)  -> cell (30-40, 30-40)
Student 21: x=15 (10-20), y=20 (10-20)  -> cell (10-20, 10-20)
Student 22: x=32 (30-40), y=30 (30-40)  -> cell (30-40, 30-40)
Student 23: x=42 (40-50), y=40 (40-50)  -> cell (40-50, 40-50)
Student 24: x=25 (20-30), y=28 (20-30)  -> cell (20-30, 20-30)
Student 25: x=18 (10-20), y=22 (20-30)  -> cell (10-20, 20-30)
Student 26: x=35 (30-40), y=38 (30-40)  -> cell (30-40, 30-40)
Student 27: x=30 (30-40), y=32 (30-40)  -> cell (30-40, 30-40)
Student 28: x=40 (40-50), y=35 (30-40)  -> cell (40-50, 30-40)
Student 29: x=22 (20-30), y=26 (20-30)  -> cell (20-30, 20-30)
Student 30: x=33 (30-40), y=36 (30-40)  -> cell (30-40, 30-40)
```

**Step 4: Count tallies and fill the table.**

| x \ y | 10-20 | 20-30 | 30-40 | 40-50 | Row Total |
|---|---|---|---|---|---|
| 10-20 | 4 | 1 | 0 | 0 | 5 |
| 20-30 | 0 | 7 | 1 | 0 | 8 |
| 30-40 | 0 | 1 | 9 | 0 | 10 |
| 40-50 | 0 | 0 | 2 | 5 | 7 |
| **Col Total** | **4** | **9** | **12** | **5** | **30** |

**Verification:** All row totals sum to 30, all column totals sum to 30, and N = 30. Confirmed.

---

### 5. Marginal Distributions

The **marginal distribution** of a variable is the frequency distribution of that variable ignoring the other variable.

#### Marginal Distribution of x (from the row totals):

| x Class | Frequency | Relative Frequency |
|---|---|---|
| 10-20 | 5 | 5/30 = 0.167 |
| 20-30 | 8 | 8/30 = 0.267 |
| 30-40 | 10 | 10/30 = 0.333 |
| 40-50 | 7 | 7/30 = 0.233 |
| **Total** | **30** | **1.000** |

#### Marginal Distribution of y (from the column totals):

| y Class | Frequency | Relative Frequency |
|---|---|---|
| 10-20 | 4 | 4/30 = 0.133 |
| 20-30 | 9 | 9/30 = 0.300 |
| 30-40 | 12 | 12/30 = 0.400 |
| 40-50 | 5 | 5/30 = 0.167 |
| **Total** | **30** | **1.000** |

---

### 6. Conditional Distributions

A **conditional distribution** shows the distribution of one variable for a **specific class** of the other variable.

#### Example: Distribution of y given x is in the class 20-30

We look at the row for x = 20-30:
- y = 10-20: 0
- y = 20-30: 7
- y = 30-40: 1
- y = 40-50: 0
- Row total: 8

Conditional distribution (relative frequencies):

| y Class | Frequency | Conditional Probability |
|---|---|---|
| 10-20 | 0 | 0/8 = 0.00 |
| 20-30 | 7 | 7/8 = 0.875 |
| 30-40 | 1 | 1/8 = 0.125 |
| 40-50 | 0 | 0/8 = 0.000 |
| **Total** | **8** | **1.000** |

Interpretation: If a student scores 20-30 in Mathematics, there is an 87.5% chance they score 20-30 in Statistics.

#### Example: Distribution of x given y is in the class 30-40

We look at the column for y = 30-40:
- x = 10-20: 0
- x = 20-30: 1
- x = 30-40: 9
- x = 40-50: 2
- Column total: 12

| x Class | Frequency | Conditional Probability |
|---|---|---|
| 10-20 | 0 | 0/12 = 0.00 |
| 20-30 | 1 | 1/12 = 0.083 |
| 30-40 | 9 | 9/12 = 0.75 |
| 40-50 | 2 | 2/12 = 0.167 |
| **Total** | **12** | **1.000** |

Interpretation: If a student scores 30-40 in Statistics, there is a 75% chance they score 30-40 in Mathematics.

---

### 7. Uses of Bivariate Frequency Distribution

1. **Data reduction:** Large volumes of paired data are summarized compactly.
2. **Pattern identification:** See how two variables co-vary at a glance.
3. **Base for correlation and regression:** The bivariate table provides the foundation for computing correlation coefficients and regression lines.
4. **Conditional analysis:** Study behavior of one variable for fixed values of another.
5. **Marginal analysis:** Study each variable independently when needed.

---

### 8. Mean of Marginal Distributions

We can compute the mean of each marginal distribution using the class marks:

| x Class | Midpoint (x) | Frequency (f) | f*x |
|---|---|---|---|
| 10-20 | 15 | 5 | 75 |
| 20-30 | 25 | 8 | 200 |
| 30-40 | 35 | 10 | 350 |
| 40-50 | 45 | 7 | 315 |
| **Total** | | **30** | **940** |

```
Mean of x = 940 / 30 = 31.33
```

| y Class | Midpoint (y) | Frequency (f) | f*y |
|---|---|---|---|
| 10-20 | 15 | 4 | 60 |
| 20-30 | 25 | 9 | 225 |
| 30-40 | 35 | 12 | 420 |
| 40-50 | 45 | 5 | 225 |
| **Total** | | **30** | **930** |

```
Mean of y = 930 / 30 = 31.00
```

---

## Practice Problems

1. Construct a bivariate frequency table for the following 20 pairs of data (x = height in cm, y = weight in kg):

   (155, 55), (160, 58), (165, 62), (170, 68), (175, 72),
   (158, 52), (162, 60), (168, 65), (172, 70), (178, 75),
   (156, 54), (163, 61), (167, 64), (171, 69), (176, 73),
   (160, 56), (165, 63), (170, 67), (174, 71), (180, 78)

   Use classes: Height: 150-160, 160-170, 170-180. Weight: 50-60, 60-70, 70-80.

2. From the bivariate table in Problem 1, find:
   a) The marginal distribution of height.
   b) The marginal distribution of weight.
   c) The conditional distribution of weight given height 160-170.

3. For the following bivariate frequency table, find the mean of x and the mean of y:

| x\y | 0-10 | 10-20 | 20-30 |
|---|---|---|---|
| 0-10 | 5 | 3 | 2 |
| 10-20 | 4 | 6 | 1 |
| 20-30 | 1 | 2 | 6 |

4. Distinguish between marginal distribution and conditional distribution with an example.

5. Explain what a scatter diagram would look like in the case of:
   a) Perfect positive correlation
   b) Perfect negative correlation
   c) No correlation between variables

**Answers/Hints:**
1. Bivariate table:

| Height\Weight | 50-60 | 60-70 | 70-80 | Total |
|---|---|---|---|---|
| 150-160 | 4 | 0 | 0 | 4 |
| 160-170 | 1 | 6 | 0 | 7 |
| 170-180 | 0 | 2 | 7 | 9 |
| **Total** | **5** | **8** | **7** | **20** |

2a. Height: 150-160: 4, 160-170: 7, 170-180: 9.
2b. Weight: 50-60: 5, 60-70: 8, 70-80: 7.
2c. Weight given Height 160-170: 50-60: 1/7, 60-70: 6/7, 70-80: 0/7.

3. Midpoints: x: 5, 15, 25. y: 5, 15, 25.
   Row totals: 10, 11, 9. N = 30.
   Mean of x = (10*5 + 11*15 + 9*25)/30 = (50+165+225)/30 = 440/30 = 14.67.
   Col totals: 10, 11, 9.
   Mean of y = (10*5 + 11*15 + 9*25)/30 = 440/30 = 14.67.

4. Marginal distribution shows the distribution of one variable irrespective of the other. Conditional distribution shows the distribution of one variable given a specific value/class of the other variable. Example: Marginal distribution of height considers all students; conditional distribution of height given weight 60-70 considers only students in that weight range.

5a. Perfect positive: All points lie exactly on an upward-sloping straight line.
5b. Perfect negative: All points lie exactly on a downward-sloping straight line.
5c. No correlation: Points are scattered randomly with no pattern.
