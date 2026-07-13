# Review of Basic Probability

**Course:** Probability and Statistics  
**Module:** 2 | **Lecture:** 1  
**Date:** 30-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 3.2 - 3.42

## Notes

### Introduction to Probability Theory

Probability theory is the branch of mathematics that deals with quantifying uncertainty. It provides the framework for making predictions, analyzing random phenomena, and drawing inferences from data.

---

### 1. Random Experiment

A **random experiment** (or trial) is a process or action whose outcome cannot be predicted with certainty in advance, but the set of all possible outcomes is known.

**Characteristics of a random experiment:**
- It can be repeated under identical conditions an indefinite number of times.
- The set of all possible outcomes is known before performing the experiment.
- The actual outcome on any single trial is not known in advance.

**Examples:**
- Tossing a fair coin once (outcomes: Head or Tail)
- Rolling a six-sided die (outcomes: 1, 2, 3, 4, 5, 6)
- Drawing a card from a well-shuffled deck of 52 cards
- Measuring the lifetime of a light bulb

---

### 2. Sample Space

The **sample space** (denoted by `S` or `Omega`) of a random experiment is the set of all possible outcomes of that experiment.

**Types of sample spaces:**
- **Discrete sample space:** Contains a finite or countably infinite number of outcomes. Example: `S = {H, T}` for a coin toss.
- **Continuous sample space:** Contains an uncountably infinite number of outcomes. Example: `S = {t : t >= 0}` for the lifetime of a bulb.

**Example 1:** Tossing two coins simultaneously.
`S = {HH, HT, TH, TT}` (4 outcomes)

**Example 2:** Rolling two dice.
`S = {(1,1), (1,2), ..., (6,6)}` (36 outcomes)

---

### 3. Event

An **event** is a subset of the sample space. An event occurs if the outcome of the experiment belongs to that subset.

**Types of events:**
- **Simple (elementary) event:** An event that contains exactly one outcome. Example: getting a 6 on a die roll.
- **Compound event:** An event that contains more than one outcome. Example: getting an even number on a die roll = `{2, 4, 6}`.
- **Sure (certain) event:** The event that equals the entire sample space `S`. It always occurs.
- **Impossible event:** The empty set `phi` (or `{}`). It never occurs.
- **Complementary event:** The complement of event `A`, denoted `A'` or `A^c`, is the set of outcomes in `S` that are not in `A`.
- **Mutually exclusive events:** Events `A` and `B` are mutually exclusive (disjoint) if they cannot occur simultaneously, i.e., `A cap B = phi`.
- **Exhaustive events:** Events `A_1, A_2, ..., A_n` are exhaustive if their union equals the sample space `S`, i.e., `A_1 cup A_2 cup ... cup A_n = S`.

---

### 4. Classical (Mathematical) Definition of Probability

If a random experiment results in `N` equally likely, mutually exclusive, and exhaustive outcomes, and if `N(A)` of these outcomes are favorable to event `A`, then the probability of event `A` is:

`P(A) = N(A) / N = (Number of favorable outcomes) / (Total number of outcomes)`

**Assumptions:**
1. All outcomes are **equally likely** (each outcome has the same chance of occurring).
2. All outcomes are **mutually exclusive** (no two outcomes can occur together).
3. The set of outcomes is **exhaustive** (covers all possibilities).

**Example 3:** What is the probability of getting a sum of 7 when rolling two fair dice?

Total outcomes: 36
Favorable outcomes (sum = 7): (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes
`P(sum = 7) = 6/36 = 1/6`

**Limitations of classical definition:**
- It fails when outcomes are not equally likely.
- It cannot handle infinite sample spaces easily.
- The term "equally likely" itself presupposes the concept of probability (circular reasoning).

---

### 5. Axiomatic Definition of Probability (Kolmogorov's Axioms)

Let `S` be a sample space and let `A` be an event (a subset of `S`). A probability function `P` is a real-valued function defined on events such that the following three axioms hold:

**Axiom 1 (Non-negativity):** For any event `A`,
`P(A) >= 0`

**Axiom 2 (Normalization):** The probability of the sample space is 1:
`P(S) = 1`

**Axiom 3 (Countable Additivity):** For any countable sequence of pairwise mutually exclusive events `A_1, A_2, A_3, ...` (i.e., `A_i cap A_j = phi` for `i != j`),
`P(A_1 cup A_2 cup A_3 cup ...) = sum_{i=1}^{infty} P(A_i)`

These three axioms form the foundation of all of probability theory.

---

### 6. Properties of Probability (Derived from the Axioms)

**Property 1: Probability of the empty set**
`P(phi) = 0`

**Property 2: Complement rule**
For any event `A`,
`P(A') = 1 - P(A)`

**Property 3: Monotonicity**
If `A subseteq B`, then `P(A) <= P(B)`.

**Property 4: Boundedness**
For any event `A`,
`0 <= P(A) <= 1`

**Property 5: Probability of union of two events (Addition Theorem)**
For any two events `A` and `B`,
`P(A cup B) = P(A) + P(B) - P(A cap B)`

**Property 6: Probability of union of three events**
For any three events `A`, `B`, and `C`,
`P(A cup B cup C) = P(A) + P(B) + P(C) - P(A cap B) - P(B cap C) - P(A cap C) + P(A cap B cap C)`

**Property 7: If A and B are mutually exclusive**
If `A cap B = phi`, then `P(A cup B) = P(A) + P(B)`.

**Property 8: Boole's inequality**
`P(A cup B) <= P(A) + P(B)` (equality holds when `A` and `B` are mutually exclusive)

**Property 9: Bonferroni's inequality**
`P(A cap B) >= P(A) + P(B) - 1`

---

### 7. Addition Theorem (Proof and Explanation)

**Theorem 1:** For any two events `A` and `B`:
`P(A cup B) = P(A) + P(B) - P(A cap B)`

**Proof:**
We can write `A cup B` as the union of three disjoint sets:
`A cup B = (A - B) cup (A cap B) cup (B - A)`

Since `(A - B)`, `(A cap B)`, and `(B - A)` are mutually exclusive, by Axiom 3:
`P(A cup B) = P(A - B) + P(A cap B) + P(B - A)`

Now, `A = (A - B) cup (A cap B)`, so `P(A) = P(A - B) + P(A cap B)` implies `P(A - B) = P(A) - P(A cap B)`.
Similarly, `P(B - A) = P(B) - P(A cap B)`.

Substituting:
`P(A cup B) = [P(A) - P(A cap B)] + P(A cap B) + [P(B) - P(A cap B)]`
`P(A cup B) = P(A) + P(B) - P(A cap B)`.

Hence proved.

---

### 8. Addition Theorem for Three Events

**Theorem 2:** For any three events `A`, `B`, and `C`:
`P(A cup B cup C) = P(A) + P(B) + P(C) - P(A cap B) - P(B cap C) - P(A cap C) + P(A cap B cap C)`

**Intuition:** When we add the individual probabilities, we overcount the pairwise intersections. Subtracting them overcorrects (removes the triple intersection three times), so we add it back once.

---

### 9. Worked Examples

**Example 4:** A card is drawn from a well-shuffled deck of 52 cards. Find the probability that it is:
(a) a king
(b) a red card
(c) a king or a red card

**Solution:**
Total outcomes = 52

(a) Number of kings = 4
`P(king) = 4/52 = 1/13`

(b) Number of red cards = 26 (13 hearts + 13 diamonds)
`P(red) = 26/52 = 1/2`

(c) Let A = event of drawing a king, B = event of drawing a red card.
`P(A cup B) = P(A) + P(B) - P(A cap B)`
`P(A cap B)` = probability of drawing a red king = 2/52 (king of hearts, king of diamonds)
`P(A cup B) = 4/52 + 26/52 - 2/52 = 28/52 = 7/13`

---

**Example 5:** Two dice are rolled. Find the probability that the sum is at least 9 or the first die shows a 5.

**Solution:**
Let A = event that sum >= 9, B = event that first die shows 5.

Favorable outcomes for A:
Sum = 9: (3,6), (4,5), (5,4), (6,3) = 4
Sum = 10: (4,6), (5,5), (6,4) = 3
Sum = 11: (5,6), (6,5) = 2
Sum = 12: (6,6) = 1
Total for A = 4 + 3 + 2 + 1 = 10
`P(A) = 10/36 = 5/18`

Favorable outcomes for B:
First die shows 5: (5,1), (5,2), (5,3), (5,4), (5,5), (5,6) = 6
`P(B) = 6/36 = 1/6`

Favorable outcomes for `A cap B`:
First die = 5 AND sum >= 9: (5,4)=9, (5,5)=10, (5,6)=11 = 3 outcomes
`P(A cap B) = 3/36 = 1/12`

`P(A cup B) = 5/18 + 1/6 - 1/12 = 10/36 + 6/36 - 3/36 = 13/36`

---

**Example 6:** A die is rolled. Let A = {1, 3, 5} (odd number), B = {2, 4, 6} (even number), C = {4, 5, 6} (number >= 4). Compute:
(a) `P(A cup B)`
(b) `P(A cup C)`
(c) `P(A cup B cup C)`

**Solution:**
`P(A) = 3/6 = 1/2`, `P(B) = 3/6 = 1/2`, `P(C) = 3/6 = 1/2`

(a) `A cap B = phi` (mutually exclusive)
`P(A cup B) = P(A) + P(B) = 1/2 + 1/2 = 1`

(b) `A cap C = {5}` (since A = {1,3,5}, C = {4,5,6})
`P(A cap C) = 1/6`
`P(A cup C) = P(A) + P(C) - P(A cap C) = 1/2 + 1/2 - 1/6 = 5/6`

(c) For three events:
`A cap B = phi`, `A cap C = {5}`, `B cap C = {4, 6}` (since B = {2,4,6}, C = {4,5,6})
`A cap B cap C = phi` (no element common to all three)
`P(A cup B cup C) = 1/2 + 1/2 + 1/2 - 0 - 2/6 - 1/6 + 0 = 3/2 - 3/6 = 3/2 - 1/2 = 1`
This makes sense since `A cup B cup C = {1,2,3,4,5,6} = S`.

---

**Example 7:** Among 100 students, 45 take Mathematics, 30 take Physics, and 15 take both. Find the probability that a randomly selected student takes Mathematics or Physics.

**Solution:**
Let M = event that student takes Mathematics, P = event that student takes Physics.

`P(M) = 45/100`, `P(P) = 30/100`, `P(M cap P) = 15/100`

`P(M cup P) = P(M) + P(P) - P(M cap P)`
`= 45/100 + 30/100 - 15/100 = 60/100 = 3/5`

---

### Summary of Key Formulas

| Concept | Formula |
|---|---|
| Complement | `P(A') = 1 - P(A)` |
| Union of two events | `P(A cup B) = P(A) + P(B) - P(A cap B)` |
| Union of three events | `P(A cup B cup C) = P(A) + P(B) + P(C) - P(A cap B) - P(B cap C) - P(A cap C) + P(A cap B cap C)` |
| Mutually exclusive events | `P(A cup B) = P(A) + P(B)` |
| Empty set | `P(phi) = 0` |

---

## Practice Problems

1. Three coins are tossed. Find the probability of getting:
   (a) exactly two heads
   (b) at least two heads
   (c) at most one head
   (d) no heads

2. Two dice are thrown. Find the probability of getting:
   (a) a doublet (same number on both dice)
   (b) a sum of 8
   (c) a sum greater than 9
   (d) a product that is a multiple of 6

3. A bag contains 3 red balls, 5 white balls, and 2 blue balls. A ball is drawn at random. Find the probability that it is:
   (a) red or white
   (b) not blue
   (c) neither red nor blue

4. In a group of 200 people, 120 like tea, 80 like coffee, and 50 like both. Find the probability that a randomly selected person likes at least one of the two beverages.

5. Let A, B, C be three events such that `P(A)=0.4`, `P(B)=0.3`, `P(C)=0.5`, `P(A cap B)=0.1`, `P(B cap C)=0.15`, `P(A cap C)=0.2`, and `P(A cap B cap C)=0.05`. Find:
   (a) `P(A cup B)`
   (b) `P(A cup B cup C)`
   (c) `P(A' cap B')`

---

**Answers/Hints:**
1. (a) 3/8 (b) 1/2 (c) 1/2 (d) 1/8
2. (a) 1/6 (b) 5/36 (c) 1/6 (d) Hint: Count favorable pairs systematically.
3. (a) 8/10 = 4/5 (b) 8/10 = 4/5 (c) 5/10 = 1/2
4. 120/200 + 80/200 - 50/200 = 150/200 = 3/4
5. (a) 0.6 (b) 0.8 (c) `P(A' cap B') = P((A cup B)') = 1 - P(A cup B) = 0.4`
