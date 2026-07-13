# Bayes Theorem

**Course:** Probability and Statistics  
**Module:** 2 | **Lecture:** 4  
**Date:** 06-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 4.4

## Notes

### Introduction

Bayes' Theorem is one of the most important results in probability theory. It describes how to update our beliefs about an event in light of new evidence. Named after Reverend Thomas Bayes (1701-1761), this theorem forms the foundation of Bayesian statistics, machine learning, and many modern data science techniques.

---

### 1. Law of Total Probability (Prerequisite)

Before stating Bayes' Theorem, we need the Law of Total Probability.

**Theorem (Law of Total Probability):** Let `B_1, B_2, ..., B_n` be a partition of the sample space `S`. This means:
- `B_i cap B_j = phi` for all `i != j` (mutually exclusive)
- `B_1 cup B_2 cup ... cup B_n = S` (exhaustive)
- `P(B_i) > 0` for all i

Then for any event `A`:
`P(A) = P(B_1) * P(A | B_1) + P(B_2) * P(A | B_2) + ... + P(B_n) * P(A | B_n)`

**Proof:**
Since `B_1, B_2, ..., B_n` partition `S`, event `A` can be written as:
`A = (A cap B_1) cup (A cap B_2) cup ... cup (A cap B_n)`
The sets `A cap B_i` are mutually exclusive (since the `B_i` are disjoint).
Therefore:
`P(A) = P(A cap B_1) + P(A cap B_2) + ... + P(A cap B_n)`
`= P(B_1)*P(A|B_1) + P(B_2)*P(A|B_2) + ... + P(B_n)*P(A|B_n)`

The theorem is proved.

---

### 2. Bayes' Theorem: Statement

**Theorem (Bayes' Theorem):** Let `B_1, B_2, ..., B_n` be a partition of the sample space `S` with `P(B_i) > 0` for all i. For any event `A` with `P(A) > 0`, the conditional probability of `B_k` given `A` is:

`P(B_k | A) = P(B_k cap A) / P(A) = P(B_k) * P(A | B_k) / sum_{i=1}^{n} P(B_i) * P(A | B_i)`

for `k = 1, 2, ..., n`.

In simpler notation with two events:

`P(B | A) = P(B) * P(A | B) / P(A)`

---

### 3. Bayes' Theorem: Proof

**Proof:**
From the definition of conditional probability:
`P(B_k | A) = P(B_k cap A) / P(A)` ... (1)

From the multiplication theorem:
`P(B_k cap A) = P(B_k) * P(A | B_k)` ... (2)

From the law of total probability:
`P(A) = sum_{i=1}^{n} P(B_i) * P(A | B_i)` ... (3)

Substituting (2) and (3) into (1):
`P(B_k | A) = P(B_k) * P(A | B_k) / sum_{i=1}^{n} P(B_i) * P(A | B_i)`

Hence proved.

---

### 4. Prior and Posterior Probabilities

- **Prior probability:** `P(B_k)` is the probability assigned to event `B_k` before observing any evidence. It represents our initial belief about `B_k`.
- **Likelihood:** `P(A | B_k)` is the probability of observing the evidence `A` given that `B_k` is true.
- **Posterior probability:** `P(B_k | A)` is the updated probability of `B_k` after observing evidence `A`. It represents our revised belief incorporating the new information.

**The Bayesian updating process:**
`Posterior = (Prior * Likelihood) / Evidence`

---

### 5. Step-by-Step Procedure for Bayes Problems

**Step 1:** Identify the events that form a partition of the sample space (the "causes" or "hypotheses"). These are the `B_i` events.

**Step 2:** Write down the prior probabilities `P(B_i)`.

**Step 3:** Write down the likelihoods `P(A | B_i)` -- the probability of the observed evidence under each hypothesis.

**Step 4:** Compute `P(A)` using the law of total probability:
`P(A) = sum P(B_i) * P(A | B_i)`

**Step 5:** Apply Bayes' Theorem to find each `P(B_i | A)`:
`P(B_i | A) = P(B_i) * P(A | B_i) / P(A)`

---

### 6. Worked Example 1: The Classic Disease Testing Problem

**Problem:** A disease affects 1% of the population. A diagnostic test has:
- 99% sensitivity: `P(positive | disease) = 0.99`
- 95% specificity: `P(negative | no disease) = 0.95`

If a randomly selected person tests positive, what is the probability that they actually have the disease?

**Solution using the step-by-step approach:**

**Step 1:** Identify the partition events.
- `D` = person has the disease
- `D'` = person does NOT have the disease

These form a partition since a person either has the disease or does not.

**Step 2:** Priors.
`P(D) = 0.01`
`P(D') = 0.99`

**Step 3:** Likelihoods.
`P(positive | D) = 0.99`
`P(positive | D') = 1 - 0.95 = 0.05` (false positive rate)

**Step 4:** Compute `P(positive)` using total probability.
`P(positive) = P(D) * P(positive | D) + P(D') * P(positive | D')`
`= (0.01)(0.99) + (0.99)(0.05)`
`= 0.0099 + 0.0495`
`= 0.0594`

**Step 5:** Apply Bayes' Theorem.
`P(D | positive) = P(D) * P(positive | D) / P(positive)`
`= 0.0099 / 0.0594`
`= 0.1667`

**Interpretation:** Only about 16.67% of positive test results actually indicate the disease. This is because the disease is rare, so false positives (5% of the 99% healthy population) outnumber true positives (99% of the 1% diseased population).

---

### 7. Worked Example 2: Three Machines Producing Items

**Problem:** A factory has three machines A, B, and C that produce 50%, 30%, and 20% of the total output, respectively. The defective rates for these machines are 2%, 3%, and 4%, respectively. If a randomly selected item is found defective, what is the probability that it was produced by machine A? By machine B? By machine C?

**Solution:**

**Step 1:** Partition events.
`A` = item produced by machine A
`B` = item produced by machine B
`C` = item produced by machine C

These partition the sample space (every item comes from exactly one machine).

**Step 2:** Priors.
`P(A) = 0.50`
`P(B) = 0.30`
`P(C) = 0.20`

**Step 3:** Likelihoods (probability of being defective given the machine).
`P(defective | A) = 0.02`
`P(defective | B) = 0.03`
`P(defective | C) = 0.04`

**Step 4:** Compute `P(defective)` using total probability.
`P(defective) = P(A)*P(def|A) + P(B)*P(def|B) + P(C)*P(def|C)`
`= (0.50)(0.02) + (0.30)(0.03) + (0.20)(0.04)`
`= 0.01 + 0.009 + 0.008`
`= 0.027`

**Step 5:** Apply Bayes' Theorem.

`P(A | defective) = P(A) * P(def | A) / P(defective) = 0.01 / 0.027 = 0.3704`

`P(B | defective) = 0.009 / 0.027 = 0.3333`

`P(C | defective) = 0.008 / 0.027 = 0.2963`

**Verification:** Sum of posterior probabilities = 0.3704 + 0.3333 + 0.2963 = 1.0000.

**Interpretation:** Even though machine A has the lowest defect rate (2%), it contributes the most to total defects (37%) because it produces the largest share of items (50%). Machine C has the highest defect rate (4%) but contributes the least to overall defects (29.6%) because it produces only 20% of all items.

---

### 8. Tree Diagram Approach

The tree diagram is a visual method to solve Bayes' theorem problems. Let us use it for Example 2.

```
                      /-- Defective (0.02) -- 0.50 * 0.02 = 0.010
         /-- A (0.50) 
        /             \-- Good (0.98)   -- 0.50 * 0.98 = 0.490
       /
Start (1)
       \
        \             /-- Defective (0.03) -- 0.30 * 0.03 = 0.009
         \-- B (0.30)
                      \-- Good (0.97)   -- 0.30 * 0.97 = 0.291
         
         /-- C (0.20)
        /             \-- Defective (0.04) -- 0.20 * 0.04 = 0.008
                      \-- Good (0.96)   -- 0.20 * 0.96 = 0.192
```

**Using the tree to find `P(A | defective)`:**
- Numerator: Path probability through A to defective = `0.50 * 0.02 = 0.010`
- Denominator: Sum of all path probabilities ending at defective = `0.010 + 0.009 + 0.008 = 0.027`
- Answer: `0.010 / 0.027 = 0.3704`

This visual approach makes Bayes' theorem intuitive.

---

### 9. Worked Example 3: Communication Channel

**Problem:** A binary communication channel transmits 0s and 1s. Due to noise, errors occur:
- 60% of transmitted bits are 0s.
- 40% of transmitted bits are 1s.
- If a 0 is sent, the probability of receiving 0 is 0.95 (so error probability = 0.05).
- If a 1 is sent, the probability of receiving 1 is 0.90 (so error probability = 0.10).

If a 0 is received, what is the probability that a 0 was actually sent?

**Solution:**

Let `S_0` = event that 0 is sent, `S_1` = event that 1 is sent.
Let `R_0` = event that 0 is received.

**Priors:** `P(S_0) = 0.60`, `P(S_1) = 0.40`

**Likelihoods:** `P(R_0 | S_0) = 0.95`, `P(R_0 | S_1) = 0.10`

**Total probability:**
`P(R_0) = P(S_0)*P(R_0|S_0) + P(S_1)*P(R_0|S_1)`
`= 0.60*0.95 + 0.40*0.10`
`= 0.57 + 0.04`
`= 0.61`

**Bayes' Theorem:**
`P(S_0 | R_0) = 0.57 / 0.61 = 0.9344`

There is a 93.44% chance that a 0 was actually sent given that a 0 was received. The channel's reliability is quite high.

---

### 10. Worked Example 4: Two-Stage Experiment

**Problem:** Box I contains 3 red and 2 blue marbles. Box II contains 2 red and 4 blue marbles. A box is chosen at random (equal probability), and then a marble is drawn from that box. If the drawn marble is red, what is the probability it came from Box I?

**Solution:**

Let `B1` = Box I chosen, `B2` = Box II chosen.
Let `R` = red marble drawn.

**Priors:** `P(B1) = P(B2) = 1/2`

**Likelihoods:** `P(R | B1) = 3/5`, `P(R | B2) = 2/6 = 1/3`

**Total probability:**
`P(R) = P(B1)*P(R|B1) + P(B2)*P(R|B2)`
`= (1/2)*(3/5) + (1/2)*(1/3)`
`= 3/10 + 1/6`
`= 9/30 + 5/30 = 14/30 = 7/15`

**Bayes' Theorem:**
`P(B1 | R) = (1/2)*(3/5) / (7/15) = (3/10) / (7/15) = (3/10)*(15/7) = 45/70 = 9/14`

So the probability is 9/14 that the red marble came from Box I.

---

### Summary

| Term | Formula | Meaning |
|---|---|---|
| Prior | `P(B_i)` | Initial belief before evidence |
| Likelihood | `P(A | B_i)` | Probability of evidence under hypothesis |
| Evidence | `P(A) = sum P(B_i) P(A | B_i)` | Total probability of evidence |
| Posterior | `P(B_i | A)` | Updated belief after evidence |

Bayes' Theorem: `P(B_i | A) = P(B_i) * P(A | B_i) / sum_j P(B_j) * P(A | B_j)`

---

## Practice Problems

1. In a certain college, 60% of students are male and 40% are female. 5% of males and 2% of females are color-blind. A student is selected at random and is found to be color-blind. Find the probability that the student is male.

2. Two machines produce items in a factory. Machine X produces 40% of the items, and Machine Y produces 60%. Machine X produces 5% defective items, while Machine Y produces 8% defective items. An item is randomly selected and found to be defective. What is the probability it was produced by Machine X?

3. There are three bags:
   - Bag 1 contains 2 white and 3 black balls
   - Bag 2 contains 4 white and 2 black balls
   - Bag 3 contains 3 white and 5 black balls
   A bag is chosen at random, and a ball is drawn from it. The ball is white. Find the probability that it was drawn from Bag 2.

4. A car rental company has three locations: Airport (50% of rentals), Downtown (30%), and Suburb (20%). The probability that a car needs maintenance after a rental from these locations is 0.05, 0.03, and 0.02 respectively. A returned car needs maintenance. What is the probability it was rented from the Airport?

5. In a multiple-choice question with 4 options, a student either knows the answer (probability 0.7) or guesses (probability 0.3). If the student knows, they answer correctly with probability 1. If they guess, they answer correctly with probability 1/4. If the student answers correctly, what is the probability they actually knew the answer?

---

**Answers/Hints:**
1. `P(M|C) = (0.60*0.05) / (0.60*0.05 + 0.40*0.02) = 0.03/0.038 = 15/19`
2. `P(X|D) = (0.40*0.05) / (0.40*0.05 + 0.60*0.08) = 0.02/0.068 = 10/34 = 5/17`
3. `P(B2|W) = (1/3)*(4/6) / [(1/3)*(2/5) + (1/3)*(4/6) + (1/3)*(3/8)] = (4/18) / (2/15 + 4/18 + 3/24)`. Compute common denominator and simplify.
4. `P(A|M) = (0.50*0.05) / (0.50*0.05 + 0.30*0.03 + 0.20*0.02) = 0.025/0.038 = 25/38`
5. `P(K|C) = (0.7*1) / (0.7*1 + 0.3*0.25) = 0.7/0.775 = 700/775 = 28/31`
