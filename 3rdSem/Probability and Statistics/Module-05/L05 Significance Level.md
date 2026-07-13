# Significance Level

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 5  
**Date:** 15-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.6.2-18.6.4

## Notes

---

### What is the Significance Level?

The **significance level** of a hypothesis test, denoted by `alpha`, is the maximum probability of committing a Type I error (rejecting a true null hypothesis) that the researcher is willing to tolerate.

- `alpha` is chosen *before* collecting data.
- `alpha` determines the critical values of the test.
- `alpha` is the area of the critical region.

---

### Choosing alpha

The choice of `alpha` depends on the consequences of making a Type I error.

| `alpha` | Level of Significance | Typical Use Case |
|---|---|---|
| `0.10` | 10% | Exploratory research, pilot studies, social sciences |
| `0.05` | 5% | Standard in most scientific and business research |
| `0.01` | 1% | Medical trials, quality control, high-stakes decisions |
| `0.001` | 0.1% | Drug approval, clinical trials with severe consequences |

**Key principle:** The more serious the consequence of a false positive, the smaller `alpha` should be.

**Trade-off:** Decreasing `alpha` reduces Type I error but increases Type II error `beta` (and reduces power).

---

### Relationship Between p-value and Significance Level

The **p-value** is the smallest significance level at which `H_0` would be rejected for a given sample. It is the exact probability (assuming `H_0` is true) of obtaining a test statistic as extreme as the one observed.

**Decision rule:**
- If `p-value < alpha`: Reject `H_0` (the result is statistically significant).
- If `p-value >= alpha`: Fail to reject `H_0` (the result is not statistically significant).

**Interpretation:**
- The p-value is *not* the probability that `H_0` is true.
- The p-value is *not* the probability that the result occurred by chance.
- The p-value is: the probability of observing the data (or more extreme data) assuming `H_0` is true.

---

### What Does "Statistically Significant" Mean?

A result is called **statistically significant** at level `alpha` if the p-value is less than `alpha`.

**Common misunderstandings:**
- "Statistically significant" does NOT mean "practically important" or "large effect."
- With a large enough sample size, even a tiny effect can be statistically significant.
- With a very small sample, even a large effect may not be statistically significant.

| p-value | Terminology | Interpretation |
|---|---|---|
| `p < 0.001` | Highly significant | Very strong evidence against `H_0` |
| `0.001 <= p < 0.01` | Very significant | Strong evidence against `H_0` |
| `0.01 <= p < 0.05` | Significant | Moderate evidence against `H_0` |
| `0.05 <= p < 0.10` | Marginally significant | Weak evidence against `H_0` |
| `p >= 0.10` | Not significant | Little to no evidence against `H_0` |

---

### Worked Example 1: Interpreting p-value

**Problem:** A researcher tests a new drug and obtains `p-value = 0.03` for `H_0`: the drug has no effect.

**Interpretation at different significance levels:**

| `alpha` | Decision | Interpretation |
|---|---|---|
| `0.01` | Fail to reject `H_0` | Not significant at the 0.01 level; insufficient evidence that drug works |
| `0.05` | Reject `H_0` | Significant at the 0.05 level; evidence suggests drug has an effect |
| `0.10` | Reject `H_0` | Significant at the 0.10 level; evidence suggests drug has an effect |

The same p-value leads to different conclusions depending on the chosen `alpha`.

---

### Worked Example 2: Complete Interpretation

**Problem:** A machine is supposed to fill bottles with 500 mL of soda. A sample of 50 bottles has a mean of 495 mL with `sigma = 15` mL. Test the claim at `alpha = 0.01`.

**Solution:**

`H_0: mu = 500`  
`H_1: mu != 500` (two-tailed)

Test statistic:
`z = (495 - 500) / (15 / sqrt{50}) = (-5) / (15 / 7.071) = (-5) / 2.121 = -2.357`

p-value: `P(Z < -2.357) = 0.0092` (from z-table). Two-tailed: `p = 2 * 0.0092 = 0.0184`.

**Decision at `alpha = 0.01`:** `p = 0.0184 > 0.01`, so fail to reject `H_0`.

**Interpretation:** There is insufficient evidence at the 0.01 significance level to conclude that the average fill volume differs from 500 mL. The result is NOT statistically significant at `alpha = 0.01`.

**Note:** If we had chosen `alpha = 0.05`, the same p-value `0.0184 < 0.05` would lead to rejection. This illustrates why `alpha` must be chosen before seeing the data -- choosing `alpha` after seeing the p-value is called **p-hacking** and is unethical.

---

### Worked Example 3: Comparing p-values

**Problem:** Three different studies test the same hypothesis. Their p-values are:
- Study A: `p = 0.04`
- Study B: `p = 0.004`
- Study C: `p = 0.20`

Assuming `alpha = 0.05`, what do we conclude?

**Analysis:**

| Study | p-value | Significant at 0.05? | Strength of evidence |
|---|---|---|---|
| A | `0.04` | Yes | Moderate evidence against `H_0` |
| B | `0.004` | Yes | Strong evidence against `H_0` |
| C | `0.20` | No | No evidence against `H_0` |

**Important:** Study A is just barely significant. Study B provides much stronger evidence. Study C provides no evidence to reject `H_0`.

---

### Common Misconceptions About p-values

| Misconception | Correct Statement |
|---|---|
| p-value is the probability that `H_0` is true | The p-value assumes `H_0` is true and computes the probability of the observed data |
| p-value is the probability that `H_1` is true | This is a Bayesian concept (posterior probability), not a p-value |
| If p > 0.05, `H_0` is true | We only say we "fail to reject" `H_0`, not that it is true |
| If p < 0.05, the effect is practically important | Statistical significance does not imply practical significance |
| p-value can tell us the size of the effect | p-value depends on both effect size and sample size |

---

### Reporting Results

Standard format for reporting hypothesis test results:

"The mean score of the treatment group (`bar{x} = 85.3`) was significantly higher than the control group mean at the 0.05 significance level (`t(28) = 2.15, p = 0.04`)."

This format includes:
- The descriptive statistics
- The significance level
- The test statistic and degrees of freedom
- The p-value

---

## Practice Problems

1. A test yields `p-value = 0.06`. At `alpha = 0.05`, is the result statistically significant? What about at `alpha = 0.10`?
   - **Answer:** At `alpha = 0.05`: not significant (`0.06 > 0.05`). At `alpha = 0.10`: significant (`0.06 < 0.10`).

2. Why is it problematic to choose `alpha` after computing the p-value?
   - **Answer:** It is p-hacking and inflates the Type I error rate. The significance level must be set before data collection to maintain the validity of the test.

3. A study finds `p = 0.03` for a new teaching method. Interpret this finding.
   - **Answer:** Assuming the null hypothesis (no effect) is true, there is a 3% probability of observing results as extreme as those found. This provides evidence against `H_0`, and the result is statistically significant at the 0.05 level.

4. Explain the difference between "statistically significant" and "practically significant."
   - **Answer:** A result can be statistically significant (p < alpha) but have such a small effect that it is not meaningful in practice. For example, a drug that reduces blood pressure by 0.5 mmHg might be statistically significant with a large sample, but not clinically relevant.

5. A researcher sets `alpha = 0.01` for a medical trial and obtains `p = 0.015`. What should they conclude?
   - **Answer:** Fail to reject `H_0`. The result is not statistically significant at the 0.01 level. However, they should report the exact p-value as `p = 0.015`.
