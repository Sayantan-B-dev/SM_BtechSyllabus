# Rank Correlation

**Course:** Probability and Statistics  
**Module:** 1 | **Lecture:** 7  
**Date:** 23-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 10.16

## Notes

### 1. Introduction to Rank Correlation

Karl Pearson's correlation coefficient requires the data to be quantitative and assumes a linear relationship. However, sometimes we have data that is **ordinal** (rankable but not precisely measurable) or the relationship is not necessarily linear.

**Spearman's rank correlation coefficient** (denoted by `rho` or `r_s`) is a non-parametric measure of correlation that:
- Works with ranks rather than actual values.
- Measures the monotonic relationship between two variables.
- Does not assume a normal distribution.
- Is less sensitive to outliers.

**When to use rank correlation:**
- Data is ordinal (e.g., rankings in a competition, preferences).
- Data does not satisfy normality assumptions.
- Sample size is small.
- Only relative order is known, not actual values.

---

### 2. Spearman's Rank Correlation Coefficient

#### 2.1 Formula (Without Tied Ranks)

When there are **no tied ranks** (all ranks are distinct):

```
r_s = 1 - (6 * sum di^2) / (n * (n^2 - 1))
```

where:
- `di = R(xi) - R(yi)` = difference between the ranks of the i-th observation in the two variables
- `n` = number of paired observations

#### Derivation of the Formula

Spearman's coefficient is simply Karl Pearson's correlation coefficient applied to the ranks. If we denote ranks as `R(xi)` and `R(yi)`, then:

For ranks, `sum R(xi) = sum R(yi) = n(n+1)/2` and `sum R(xi)^2 = sum R(yi)^2 = n(n+1)(2n+1)/6`.

It can be shown that:
```
sum di^2 = sum [R(xi) - R(yi)]^2 = 2 * [n(n+1)(2n+1)/6] - 2 * sum R(xi)*R(yi)
```

Substituting into Pearson's formula and simplifying yields the formula above.

#### Properties of r_s

- `-1 <= r_s <= +1`
- `r_s = +1`: Perfect positive rank correlation (ranks agree perfectly)
- `r_s = -1`: Perfect negative rank correlation (ranks in reverse order)
- `r_s = 0`: No rank correlation
- It is symmetric: `r_s(x, y) = r_s(y, x)`

---

#### 2.2 Example 1: No Tied Ranks

Two judges ranked 8 participants in a competition as follows:

| Participant | Judge A Rank (x) | Judge B Rank (y) |
|---|---|---|
| 1 | 3 | 4 |
| 2 | 1 | 2 |
| 3 | 6 | 5 |
| 4 | 8 | 7 |
| 5 | 2 | 1 |
| 6 | 4 | 6 |
| 7 | 5 | 3 |
| 8 | 7 | 8 |

Find Spearman's rank correlation coefficient.

**Step 1: Compute the differences and squared differences.**

| Participant | Rank A (x) | Rank B (y) | d = x - y | d^2 |
|---|---|---|---|---|
| 1 | 3 | 4 | -1 | 1 |
| 2 | 1 | 2 | -1 | 1 |
| 3 | 6 | 5 | 1 | 1 |
| 4 | 8 | 7 | 1 | 1 |
| 5 | 2 | 1 | 1 | 1 |
| 6 | 4 | 6 | -2 | 4 |
| 7 | 5 | 3 | 2 | 4 |
| 8 | 7 | 8 | -1 | 1 |

**Step 2: Compute sum of d^2.**

```
sum d^2 = 1 + 1 + 1 + 1 + 1 + 4 + 4 + 1 = 14
```

**Step 3: Apply the formula.**

```
r_s = 1 - (6 * 14) / (8 * (64 - 1))
    = 1 - 84 / (8 * 63)
    = 1 - 84 / 504
    = 1 - 0.1667
    = 0.8333
```

Interpretation: Strong positive rank correlation (r_s = 0.833). The two judges generally agree on rankings.

---

#### 2.3 Example 2: Another Example

Find the rank correlation between the marks in Mathematics and Physics for 10 students:

| Student | Math (x) | Physics (y) |
|---|---|---|
| A | 85 | 78 |
| B | 72 | 70 |
| C | 90 | 85 |
| D | 65 | 68 |
| E | 78 | 75 |
| F | 95 | 92 |
| G | 60 | 55 |
| H | 88 | 82 |
| I | 70 | 72 |
| J | 80 | 76 |

**Step 1: Assign ranks.** (Rank 1 = highest score)

| Student | Math | Rank (x) | Physics | Rank (y) | d | d^2 |
|---|---|---|---|---|---|---|
| A | 85 | 3 | 78 | 4 | -1 | 1 |
| B | 72 | 7 | 70 | 8 | -1 | 1 |
| C | 90 | 2 | 85 | 2 | 0 | 0 |
| D | 65 | 9 | 68 | 9 | 0 | 0 |
| E | 78 | 6 | 75 | 6 | 0 | 0 |
| F | 95 | 1 | 92 | 1 | 0 | 0 |
| G | 60 | 10 | 55 | 10 | 0 | 0 |
| H | 88 | 3 | 82 | 3 | 0 | 0 |
| I | 70 | 8 | 72 | 7 | 1 | 1 |
| J | 80 | 5 | 76 | 5 | 0 | 0 |

Wait, H and C both have different ranks. Let me re-rank:

Math scores sorted: 95(F), 90(C), 88(H), 85(A), 80(J), 78(E), 72(B), 70(I), 65(D), 60(G)
Rank x: F=1, C=2, H=3, A=4, J=5, E=6, B=7, I=8, D=9, G=10

Physics scores sorted: 92(F), 85(C), 82(H), 78(A), 76(J), 75(E), 72(I), 70(B), 68(D), 55(G)
Rank y: F=1, C=2, H=3, A=4, J=5, E=6, I=7, B=8, D=9, G=10

| Student | x-rank | y-rank | d | d^2 |
|---|---|---|---|---|
| A | 4 | 4 | 0 | 0 |
| B | 7 | 8 | -1 | 1 |
| C | 2 | 2 | 0 | 0 |
| D | 9 | 9 | 0 | 0 |
| E | 6 | 6 | 0 | 0 |
| F | 1 | 1 | 0 | 0 |
| G | 10 | 10 | 0 | 0 |
| H | 3 | 3 | 0 | 0 |
| I | 8 | 7 | 1 | 1 |
| J | 5 | 5 | 0 | 0 |

```
sum d^2 = 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 = 2
n = 10

r_s = 1 - (6*2) / (10*(100-1))
    = 1 - 12 / (10*99)
    = 1 - 12/990
    = 1 - 0.0121
    = 0.9879
```

Interpretation: Very strong positive rank correlation (r_s = 0.988). Students who score high in Math also tend to score high in Physics.

---

### 3. Rank Correlation with Tied Ranks

When two or more observations have the same value, they are said to have **tied ranks**. In this case, we assign **average ranks** to the tied values.

#### Average Ranks Method

If m observations are tied for a set of ranks, each is given the **average** of those ranks.

**Example of average rank assignment:**
Values: 10, 12, 12, 15, 18
- Smallest (10) gets rank 1.
- Two values of 12 are tied for positions 2 and 3. Each gets rank (2+3)/2 = 2.5.
- Next (15) gets rank 4.
- Next (18) gets rank 5.

#### Formula with Tied Ranks

When ties exist, we use the same formula but with a **correction factor**:

```
r_s = 1 - (6 * sum d^2) / (n * (n^2 - 1))
```

However, if many ties are present, a correction is applied:

```
r_s = [sum a^2 + sum b^2 - sum d^2] / [2 * sqrt(sum a^2 * sum b^2)]
```

where:
- `sum a^2 = (n^3 - n)/12 - sum (tx^3 - tx)/12` for variable x
- `sum b^2 = (n^3 - n)/12 - sum (ty^3 - ty)/12` for variable y
- `tx` = number of observations tied at a particular rank in x
- `ty` = number of observations tied at a particular rank in y
- `sum d^2` = sum of squared differences of ranks (after assigning average ranks)

**Simplified approach (most commonly used):**
When the number of ties is small, simply assign average ranks and use the standard formula. The result is approximately correct.

---

#### 3.1 Example 3: With Tied Ranks

Two teachers graded 8 answer scripts and gave the following scores:

| Script | Teacher A | Teacher B |
|---|---|---|
| 1 | 85 | 80 |
| 2 | 75 | 75 |
| 3 | 85 | 78 |
| 4 | 70 | 72 |
| 5 | 90 | 85 |
| 6 | 75 | 70 |
| 7 | 80 | 82 |
| 8 | 75 | 76 |

**Step 1: Assign ranks to Teacher A's scores.**

Teacher A scores: 70, 75, 75, 75, 80, 85, 85, 90

Sorted: 70(1), 75, 75, 75 (positions 2,3,4 -- average = 3), 80(5), 85, 85 (positions 6,7 -- average = 6.5), 90(8)

| Script | Score A | Rank A |
|---|---|---|
| 1 | 85 | 6.5 |
| 2 | 75 | 3 |
| 3 | 85 | 6.5 |
| 4 | 70 | 1 |
| 5 | 90 | 8 |
| 6 | 75 | 3 |
| 7 | 80 | 5 |
| 8 | 75 | 3 |

**Step 2: Assign ranks to Teacher B's scores.**

Teacher B scores: 70, 72, 75, 76, 78, 80, 82, 85

Sorted: 70(1), 72(2), 75(3), 76(4), 78(5), 80(6), 82(7), 85(8)

No ties in Teacher B's scores.

| Script | Score B | Rank B |
|---|---|---|
| 1 | 80 | 6 |
| 2 | 75 | 3 |
| 3 | 78 | 5 |
| 4 | 72 | 2 |
| 5 | 85 | 8 |
| 6 | 70 | 1 |
| 7 | 82 | 7 |
| 8 | 76 | 4 |

**Step 3: Compute differences and d^2.**

| Script | Rank A | Rank B | d | d^2 |
|---|---|---|---|---|
| 1 | 6.5 | 6 | 0.5 | 0.25 |
| 2 | 3 | 3 | 0 | 0 |
| 3 | 6.5 | 5 | 1.5 | 2.25 |
| 4 | 1 | 2 | -1 | 1 |
| 5 | 8 | 8 | 0 | 0 |
| 6 | 3 | 1 | 2 | 4 |
| 7 | 5 | 7 | -2 | 4 |
| 8 | 3 | 4 | -1 | 1 |

**Step 4: Compute sum d^2 and r_s.**

```
sum d^2 = 0.25 + 0 + 2.25 + 1 + 0 + 4 + 4 + 1 = 12.5

r_s = 1 - (6 * 12.5) / (8 * (64 - 1))
    = 1 - 75 / (8 * 63)
    = 1 - 75 / 504
    = 1 - 0.1488
    = 0.8512
```

Interpretation: Strong positive rank correlation (r_s = 0.851). The two teachers' grading is consistent.

---

### 4. Tied Rank Correction (Detailed)

For the tie correction formula, we compute the correction factor for each variable.

For Teacher A (x):
- 70 appears 1 time: t = 1, t^3 - t = 0
- 75 appears 3 times: t = 3, t^3 - t = 27 - 3 = 24
- 80 appears 1 time: t = 1, 0
- 85 appears 2 times: t = 2, t^3 - t = 8 - 2 = 6
- 90 appears 1 time: t = 1, 0

```
sum (tx^3 - tx) = 24 + 6 = 30
sum a^2 = (n^3 - n)/12 - sum(tx^3 - tx)/12 = (512 - 8)/12 - 30/12 = 504/12 - 2.5 = 42 - 2.5 = 39.5
```

For Teacher B (y): No ties, so `sum (ty^3 - ty) = 0`.
```
sum b^2 = (512 - 8)/12 - 0 = 42
```

Using the alternative formula:
```
r_s = (39.5 + 42 - 12.5) / (2 * sqrt(39.5 * 42))
    = 69 / (2 * sqrt(1659))
    = 69 / (2 * 40.73)
    = 69 / 81.46
    = 0.847
```

The result (0.847) is very close to the uncorrected value (0.851), confirming that the correction is minor when ties are few.

### 5. Advantages of Spearman's Rank Correlation

1. **Non-parametric:** No assumption about the distribution of data.
2. **Simple to compute:** Only requires ranking, not actual measurements.
3. **Handles ordinal data:** Can be used when only ranks are available.
4. **Less affected by outliers:** Extreme values do not distort the correlation as much.
5. **Measures monotonic relationships:** Detects any consistent increasing/decreasing trend, not just linear.

### 6. Disadvantages

1. **Loss of information:** Converting actual values to ranks loses magnitude information.
2. **Less powerful:** For normally distributed data, Pearson's r is more sensitive.
3. **Ties require adjustment:** Average ranks can introduce small biases.

### 7. When to Use Pearson vs Spearman

| Situation | Use Pearson | Use Spearman |
|---|---|---|
| Data is normally distributed | Yes | Not necessary |
| Relationship is linear | Yes | Not necessary |
| Data is ordinal | No | Yes |
| Data has outliers | Sensitive | Robust |
| Sample size is small | Needs normality | Works well |
| Only ranks available | Cannot use | Yes |

---

## Practice Problems

1. Compute Spearman's rank correlation for the following data:

| Candidate | Judge 1 Rank | Judge 2 Rank |
|---|---|---|
| A | 1 | 2 |
| B | 2 | 1 |
| C | 3 | 4 |
| D | 4 | 3 |
| E | 5 | 6 |
| F | 6 | 5 |
| G | 7 | 8 |
| H | 8 | 7 |

   <details>
   <summary>Show Answer</summary>
   1. d: -1, 1, -1, 1, -1, 1, -1, 1. d^2: 1,1,1,1,1,1,1,1. sum = 8.
      r_s = 1 - 6*8/(8*63) = 1 - 48/504 = 1 - 0.0952 = 0.9048. Strong positive correlation (judges somewhat agree).
   </details>

2. The marks of 6 students in two subjects are:

| Student | Subject A | Subject B |
|---|---|---|
| P | 82 | 78 |
| Q | 75 | 80 |
| R | 68 | 65 |
| S | 90 | 88 |
| T | 72 | 74 |
| U | 85 | 82 |

Find the rank correlation coefficient.

   <details>
   <summary>Show Answer</summary>
   2. Ranks: P(3,4), Q(5,3), R(6,6), S(1,1), T(4,5), U(2,2).
      d: -1, 2, 0, 0, -1, 0. d^2: 1,4,0,0,1,0. sum = 6.
      r_s = 1 - 6*6/(6*35) = 1 - 36/210 = 1 - 0.1714 = 0.8286.
   </details>

3. For 10 pairs of observations, sum d^2 = 60. Find Spearman's rank correlation coefficient.

   <details>
   <summary>Show Answer</summary>
   3. r_s = 1 - 6*60/(10*99) = 1 - 360/990 = 1 - 0.3636 = 0.6364. Moderate positive rank correlation.
   </details>

4. Calculate the rank correlation for the following (with ties):

| Student | Score in Test 1 | Score in Test 2 |
|---|---|---|
| X1 | 88 | 85 |
| X2 | 72 | 70 |
| X3 | 88 | 90 |
| X4 | 65 | 68 |
| X5 | 72 | 72 |
| X6 | 90 | 88 |

   <details>
   <summary>Show Answer</summary>
   4. Test 1: 65(1), 72,72(avg 2.5), 88,88(avg 4.5), 90(6).
      Test 2: 68(1), 70(2), 72(3), 85(4), 88(5), 90(6).
      x-ranks: 4.5, 2.5, 4.5, 1, 2.5, 6.
      y-ranks: 4, 2, 6, 1, 3, 5.
      d: 0.5, 0.5, -1.5, 0, -0.5, 1. d^2: 0.25, 0.25, 2.25, 0, 0.25, 1. sum = 4.
      r_s = 1 - 6*4/(6*35) = 1 - 24/210 = 1 - 0.1143 = 0.8857.
   </details>

5. Explain the difference between Pearson's and Spearman's correlation coefficients.
   <details>
   <summary>Show Answer</summary>
   5. Pearson's r measures linear relationships using actual values and assumes normality. Spearman's r_s measures monotonic relationships using ranks and makes no distributional assumptions. Spearman is preferred for ordinal data, non-normal data, or when outliers are present.
   </details>
