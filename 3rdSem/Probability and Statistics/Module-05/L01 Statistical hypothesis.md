# Statistical hypothesis

**Course:** Probability and Statistics  
**Module:** 5 | **Lecture:** 1  
**Date:** 06-Oct-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 18.1

## Notes

---

### What is a Statistical Hypothesis?

A **statistical hypothesis** is an assumption or a claim about a population parameter (such as the population mean `mu`, proportion `p`, or variance `sigma^2`) that we test using sample data. Unlike a general scientific hypothesis, a statistical hypothesis must be stated in a way that allows it to be tested using probability theory.

For example:
- "The average height of students in this college is 170 cm" is a statistical hypothesis about `mu`.
- "The proportion of defective items in a factory is less than 2%" is a statistical hypothesis about `p`.

---

### Null Hypothesis (`H_0`)

The **null hypothesis**, denoted by `H_0`, is a statement of no effect, no difference, or status quo. It is the hypothesis we initially assume to be true and we test whether there is sufficient evidence to reject it.

- `H_0` always contains an equality: `=`, `<=`, or `>=`.
- The null hypothesis is what we seek to challenge or disprove.

**Examples:**

| Research Question | Null Hypothesis `H_0` |
|---|---|
| Is a new drug effective? | `H_0: mu_new = mu_standard` (no difference) |
| Is the coin fair? | `H_0: p = 0.5` |
| Has the mean weight changed? | `H_0: mu = 50` kg |

---

### Alternative Hypothesis (`H_1` or `H_a`)

The **alternative hypothesis**, denoted by `H_1` (or `H_a`), is a statement that contradicts the null hypothesis. It represents what we hope to prove or what we suspect is true.

- `H_1` never contains equality; it uses `!=`, `<`, or `>`.
- The conclusion of a hypothesis test is either "reject `H_0`" (in favor of `H_1`) or "fail to reject `H_0`".

**Examples:**

| `H_0` | `H_1` (Two-tailed) | `H_1` (Left-tailed) | `H_1` (Right-tailed) |
|---|---|---|---|
| `mu = 50` | `mu != 50` | `mu < 50` | `mu > 50` |
| `p = 0.5` | `p != 0.5` | `p < 0.5` | `p > 0.5` |

---

### Simple vs Composite Hypothesis

**Simple Hypothesis:** A hypothesis that specifies the population parameter *completely* (a single value).

- Example: `H_0: mu = 100` (specifies the mean exactly)
- Example: `H_0: p = 0.3` (specifies the proportion exactly)

**Composite Hypothesis:** A hypothesis that specifies a range of values for the parameter, not a single value.

- Example: `H_0: mu <= 100` (covers all values less than or equal to 100)
- Example: `H_1: mu > 100` (covers all values greater than 100)

| Type | Definition | Example |
|---|---|---|
| Simple | Parameter is a single specified value | `H_0: sigma = 5` |
| Composite | Parameter belongs to a range | `H_1: sigma != 5` |

---

### One-Tailed and Two-Tailed Tests

The **tail** of a test refers to which side of the distribution the alternative hypothesis lies.

**Two-tailed test:** `H_1` uses `!=`. We look for evidence in both tails of the distribution.
- Example: `H_0: mu = 100` vs `H_1: mu != 100`

**Right-tailed test:** `H_1` uses `>`. We look for evidence only in the right (upper) tail.
- Example: `H_0: mu <= 100` vs `H_1: mu > 100`

**Left-tailed test:** `H_1` uses `<`. We look for evidence only in the left (lower) tail.
- Example: `H_0: mu >= 100` vs `H_1: mu < 100`

| Test Type | Sign in `H_1` | Rejection Region |
|---|---|---|
| Two-tailed | `!=` | Both tails |
| Right-tailed | `>` | Upper tail |
| Left-tailed | `<` | Lower tail |

---

### Worked Examples: Formulating Hypotheses

#### Example 1: Claim about average weight

A researcher claims that the average weight of adult males in a city is 75 kg. Test this claim.

- `H_0: mu = 75` (the claim is true)
- `H_1: mu != 75` (the claim is false -- two-tailed, since we only want to detect a difference, not a direction)

#### Example 2: Claim about effectiveness

A company claims their new fertilizer increases crop yield compared to the standard (average yield = 200 kg/acre).

- `H_0: mu <= 200` (fertilizer does not increase yield)
- `H_1: mu > 200` (fertilizer increases yield -- right-tailed)

#### Example 3: Claim about defect rate

A manufacturer claims the defect rate has decreased from the previous 5%.

- `H_0: p >= 0.05` (defect rate has not decreased)
- `H_1: p < 0.05` (defect rate has decreased -- left-tailed)

#### Example 4: Claim about blood pressure medicine

A new medicine claims to reduce blood pressure. The current average systolic BP is 130 mmHg.

- **Scenario A:** We want to check if the medicine changes BP (either direction).
  - `H_0: mu = 130`
  - `H_1: mu != 130` (two-tailed)
- **Scenario B:** We want to check if the medicine *reduces* BP.
  - `H_0: mu >= 130`
  - `H_1: mu < 130` (left-tailed)

---

### Key Points to Remember

1. `H_0` always contains `=`, `<=`, or `>=`. `H_1` always contains `!=`, `<`, or `>`.
2. The direction of `H_1` determines whether the test is one-tailed or two-tailed.
3. We never "accept" `H_0`; we either "reject `H_0`" or "fail to reject `H_0`".
4. The null hypothesis is the status quo; the burden of proof is on the alternative.
5. A simple hypothesis gives an exact value; a composite hypothesis gives a range.

---

## Practice Problems

1. A school claims its students have an average IQ of 110. Formulate `H_0` and `H_1` to test this claim.
   - **Answer:** `H_0: mu = 110`, `H_1: mu != 110` (two-tailed)

2. A car manufacturer claims that a new engine gives more than 18 km/L mileage. Formulate the hypotheses.
   - **Answer:** `H_0: mu <= 18`, `H_1: mu > 18` (right-tailed)

3. A researcher wants to test if a new drug reduces recovery time compared to the current average of 10 days. State the hypotheses.
   - **Answer:** `H_0: mu >= 10`, `H_1: mu < 10` (left-tailed)

4. Classify each hypothesis as simple or composite: (a) `H: mu = 50`, (b) `H: mu > 50`, (c) `H: p = 0.25`, (d) `H: sigma != 3`.
   - **Answer:** (a) simple, (b) composite, (c) simple, (d) composite

5. A coin is suspected of being biased towards heads. Formulate `H_0` and `H_1`.
   - **Answer:** `H_0: p <= 0.5`, `H_1: p > 0.5` (right-tailed)
