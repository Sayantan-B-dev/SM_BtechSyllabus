# Critical region

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 4  
**Date:** 13-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Interactive Learning  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.2

## Notes

---

### Definition of Critical Region

The **critical region** (also called the **rejection region**) is the set of all values of the test statistic that lead to rejection of `H_0`. If the computed test statistic falls in the critical region, we reject the null hypothesis.

The critical region is located at the tail(s) of the sampling distribution of the test statistic, and its total area equals the significance level `alpha`.

---

### Critical Values

**Critical values** are the boundary points that separate the critical region from the non-critical (acceptance) region. They are determined by:
- The significance level `alpha`
- Whether the test is one-tailed or two-tailed
- The sampling distribution of the test statistic (z, t, etc.)

---

### Relationship Between Critical Region and Significance Level

The total area of the critical region equals `alpha`.

| Test Type | Number of Critical Values | Area in Each Tail | Total Area (alpha) |
|---|---|---|---|
| Two-tailed | 2 | `alpha/2` in each tail | `alpha` |
| Right-tailed | 1 | `alpha` in right tail | `alpha` |
| Left-tailed | 1 | `alpha` in left tail | `alpha` |

---

### One-Tailed vs Two-Tailed Critical Regions

#### Two-Tailed Test (`H_1: !=`)

```
Critical region: Z < -z_{alpha/2} or Z > z_{alpha/2}
Total area of rejection = alpha
```

The rejection region is split equally between the two tails.

#### Right-Tailed Test (`H_1: >`)

```
Critical region: Z > z_alpha
Area of rejection = alpha in the upper tail
```

#### Left-Tailed Test (`H_1: <`)

```
Critical region: Z < -z_alpha
Area of rejection = alpha in the lower tail
```

---

### Determining Critical Values from Tables

#### z-critical values (standard normal distribution)

For a given `alpha`, find `z_alpha` such that `P(Z > z_alpha) = alpha`.

| `alpha` | `z_{alpha/2}` (two-tailed) | `z_alpha` (one-tailed) |
|---|---|---|
| `0.10` | `1.645` | `1.282` |
| `0.05` | `1.960` | `1.645` |
| `0.01` | `2.576` | `2.326` |
| `0.001` | `3.291` | `3.090` |

**How to read from z-table:**
1. For `z_{0.025}`: find the z-value where the area to the left is `1 - 0.025 = 0.9750`. From the table, `z = 1.96`.
2. For `z_{0.05}`: find the z-value where the area to the left is `1 - 0.05 = 0.9500`. From the table, `z = 1.645`.

#### t-critical values (t-distribution)

t-critical values depend on both `alpha` and degrees of freedom `df = n - 1`.

| `df` | `t_{0.05}` (one-tailed) | `t_{0.025}` (two-tailed) | `t_{0.01}` (one-tailed) |
|---|---|---|---|
| 5 | `2.015` | `2.571` | `3.365` |
| 10 | `1.812` | `2.228` | `2.764` |
| 20 | `1.725` | `2.086` | `2.528` |
| 30 | `1.697` | `2.042` | `2.457` |
| `infinity` | `1.645` | `1.960` | `2.326` |

Notice: As `df` increases, t-critical values approach z-critical values.

---

### Worked Examples: Finding Critical Regions

#### Example 1: z-test, two-tailed

**Given:** `alpha = 0.05`, two-tailed z-test.

**Find:** The critical region.

**Solution:**
- `alpha/2 = 0.025`
- `z_{0.025} = 1.96`
- Critical region: `z < -1.96` or `z > 1.96`
- Decision rule: Reject `H_0` if `|z| > 1.96`.

#### Example 2: z-test, left-tailed

**Given:** `alpha = 0.01`, left-tailed z-test.

**Find:** The critical region.

**Solution:**
- `z_{0.01} = 2.326`
- Since left-tailed, critical value = `-2.326`
- Critical region: `z < -2.326`
- Decision rule: Reject `H_0` if `z < -2.326`.

#### Example 3: t-test, right-tailed

**Given:** `alpha = 0.05`, right-tailed t-test, `n = 16`.

**Find:** The critical region.

**Solution:**
- `df = 16 - 1 = 15`
- From t-table: `t_{0.05, 15} = 1.753`
- Critical region: `t > 1.753`
- Decision rule: Reject `H_0` if `t > 1.753`.

#### Example 4: t-test, two-tailed

**Given:** `alpha = 0.10`, two-tailed t-test, `n = 9`.

**Find:** The critical region.

**Solution:**
- `df = 8`
- `alpha/2 = 0.05`
- From t-table: `t_{0.05, 8} = 1.860`
- Critical region: `t < -1.860` or `t > 1.860`
- Decision rule: Reject `H_0` if `|t| > 1.860`.

#### Example 5: z-test, right-tailed

**Given:** `alpha = 0.10`, right-tailed z-test.

**Find:** The critical region.

**Solution:**
- `z_{0.10} = 1.282`
- Critical region: `z > 1.282`
- Decision rule: Reject `H_0` if `z > 1.282`.

---

### Visualizing Critical Regions

For a two-tailed z-test at `alpha = 0.05`:

- The sampling distribution is a standard normal curve.
- 95% of the area lies between `z = -1.96` and `z = 1.96` (the non-critical or acceptance region).
- 2.5% of the area lies in the left tail (`z < -1.96`).
- 2.5% of the area lies in the right tail (`z > 1.96`).
- Total rejection area = 5% = `alpha`.

---

### Summary Table

| Test Type | `H_1` | Critical Region | Example (`alpha = 0.05`) |
|---|---|---|---|
| Two-tailed | `!=` | `|text(stat)| > text(critical value)` | `|z| > 1.96` |
| Right-tailed | `>` | `text(stat) > text(critical value)` | `z > 1.645` |
| Left-tailed | `<` | `text(stat) < -text(critical value)` | `z < -1.645` |

---

## Practice Problems

1. Find the critical region for a two-tailed z-test at `alpha = 0.01`.
   - **Answer:** Critical values `pm 2.576`. Reject if `|z| > 2.576`.

2. Find the critical region for a left-tailed t-test with `n = 20` at `alpha = 0.05`.
   - **Answer:** `df = 19`, `t_{0.05,19} = 1.729`. Critical region: `t < -1.729`.

3. Find the critical region for a right-tailed z-test at `alpha = 0.05`.
   - **Answer:** `z_{0.05} = 1.645`. Critical region: `z > 1.645`.

4. Find the critical region for a two-tailed t-test with `n = 12` at `alpha = 0.10`.
   - **Answer:** `df = 11`, `t_{0.05,11} = 1.796`. Critical region: `t < -1.796` or `t > 1.796`.

5. Explain why the critical region for a two-tailed test at `alpha = 0.05` is NOT the same as `|z| > 1.645`.
   - **Answer:** `z = 1.645` corresponds to `alpha = 0.05` for a one-tailed test. For a two-tailed test, we need `alpha/2 = 0.025` in each tail, which gives `z_{0.025} = 1.96`. The two-tailed region must be wider to keep the total area at 0.05.
