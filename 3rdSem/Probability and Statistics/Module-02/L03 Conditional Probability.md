# Conditional Probability

**Course:** Probability and Statistics  
**Module:** 2 | **Lecture:** 3  
**Date:** 04-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 2  
**Learning Methodology:** Interactive Learning  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 3.41

## Notes

### Introduction

Conditional probability answers the question: "Given that some event B has occurred, what is the probability that event A also occurs?" This is fundamental to understanding dependent events, Bayesian reasoning, and statistical inference.

---

### 1. Definition of Conditional Probability

**Definition:** Let `A` and `B` be two events with `P(B) > 0`. The conditional probability of `A` given `B`, denoted by `P(A | B)`, is defined as:

`P(A | B) = P(A cap B) / P(B)`

Similarly, the conditional probability of `B` given `A` (when `P(A) > 0`) is:

`P(B | A) = P(A cap B) / P(A)`

**Interpretation:** `P(A | B)` is the probability that A occurs, recalculated under the knowledge that B has already occurred. The sample space effectively shrinks from S to B.

---

### 2. Derivation and Intuition

**Intuition:** When we are told that event B has occurred, B becomes the new sample space. The only part of A that can still occur is `A cap B`. So we take the probability of `A cap B` and renormalize it by dividing by the probability of B.

**Venn diagram explanation:**
- The original sample space is S with `P(S) = 1`.
- Given that B has occurred, all outcomes outside B are impossible.
- The probability of A within this reduced space is the proportion of B that is also in A: `P(A cap B) / P(B)`.

---

### 3. Key Properties of Conditional Probability

1. **Non-negativity:** `P(A | B) >= 0`
2. **Normalization:** `P(B | B) = 1`
3. **Additivity:** If A_1 and A_2 are mutually exclusive, then:
   `P(A_1 cup A_2 | B) = P(A_1 | B) + P(A_2 | B)`
4. `P(A' | B) = 1 - P(A | B)`
5. If A and B are independent, then `P(A | B) = P(A)` and `P(B | A) = P(B)`.

---

### 4. Multiplication Theorem for Dependent Events

From the definition of conditional probability, we can rearrange to get the **multiplication theorem**:

`P(A cap B) = P(B) * P(A | B)`

or equivalently:

`P(A cap B) = P(A) * P(B | A)`

**Generalization for three events:**
`P(A cap B cap C) = P(A) * P(B | A) * P(C | A cap B)`

**Generalization for n events:**
`P(A_1 cap A_2 cap ... cap A_n) = P(A_1) * P(A_2 | A_1) * P(A_3 | A_1 cap A_2) * ... * P(A_n | A_1 cap A_2 cap ... cap A_{n-1})`

This is known as the **chain rule of probability**.

---

### 5. Worked Examples

#### Example 1: Drawing Cards Without Replacement

Two cards are drawn from a well-shuffled deck of 52 cards WITHOUT replacement. Find the probability that:
(a) both are aces
(b) the second card is an ace given that the first was an ace
(c) the second card is a king given that the first was an ace

**Solution:**
Let `A_1` = event that the first card is an ace, `A_2` = event that the second card is an ace.

(a) Using the multiplication theorem:
`P(A_1 cap A_2) = P(A_1) * P(A_2 | A_1)`
`P(A_1) = 4/52 = 1/13`
After one ace is drawn, 51 cards remain, with 3 aces remaining.
`P(A_2 | A_1) = 3/51 = 1/17`
`P(A_1 cap A_2) = (1/13) * (1/17) = 1/221`

(b) As computed above, `P(A_2 | A_1) = 3/51 = 1/17`.

(c) Let `K_2` = event that the second card is a king, given first was an ace.
After drawing an ace, 51 cards remain, with 4 kings still in the deck.
`P(K_2 | A_1) = 4/51`

---

#### Example 2: Drawing Without Replacement (Sequential)

A bag contains 5 red balls and 3 black balls. Three balls are drawn one by one WITHOUT replacement. Find the probability that:
(a) all three are red
(b) the first two are red and the third is black

**Solution:**
Let `R_i` = event that the i-th ball is red, `B_i` = event that the i-th ball is black.

(a) `P(R_1 cap R_2 cap R_3) = P(R_1) * P(R_2 | R_1) * P(R_3 | R_1 cap R_2)`
`= (5/8) * (4/7) * (3/6)`
`= (5/8) * (4/7) * (1/2)`
`= 20/112 = 5/28`

(b) `P(R_1 cap R_2 cap B_3) = P(R_1) * P(R_2 | R_1) * P(B_3 | R_1 cap R_2)`
`= (5/8) * (4/7) * (3/6)` (after 2 reds drawn: 3 reds, 3 blacks remain; probability of black = 3/6)
`= (5/8) * (4/7) * (1/2)`
`= 20/112 = 5/28`

---

#### Example 3: Disease Screening

A medical test for a disease has the following characteristics:
- The disease affects 2% of the population (prevalence rate).
- Sensitivity (true positive rate): The test correctly identifies 95% of those who have the disease. So `P(positive | disease) = 0.95`.
- Specificity (true negative rate): The test correctly identifies 90% of those who do NOT have the disease. So `P(negative | no disease) = 0.90`.

If a randomly selected person tests positive, what is the probability that they actually have the disease?

**Solution:**
Let D = event that the person has the disease, T = event that the test is positive.

Given: `P(D) = 0.02`, `P(T | D) = 0.95`, `P(T' | D') = 0.90` so `P(T | D') = 0.10`.

We want `P(D | T)`. From the definition of conditional probability:

`P(D | T) = P(D cap T) / P(T)`

Using the multiplication theorem:
`P(D cap T) = P(D) * P(T | D) = 0.02 * 0.95 = 0.019`

To find `P(T)`, we use the law of total probability (preview of the next lecture):
`P(T) = P(D cap T) + P(D' cap T)`
`= P(D)*P(T|D) + P(D')*P(T|D')`
`= 0.02*0.95 + 0.98*0.10`
`= 0.019 + 0.098`
`= 0.117`

Therefore:
`P(D | T) = 0.019 / 0.117 = 0.1624`

So even with a positive test result, there is only about a 16.24% chance that the person actually has the disease. This is a striking result! Most positive results are false positives because the disease is rare.

---

#### Example 4: Conditional Probability with Dice

Two dice are rolled. Given that the sum is 7, find the probability that the first die shows a 3.

**Solution:**
Let A = event that sum = 7, B = event that first die shows 3.

`A = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}` -- 6 outcomes
`B = {(3,1), (3,2), (3,3), (3,4), (3,5), (3,6)}` -- 6 outcomes

`A cap B = {(3,4)}` -- 1 outcome (sum=7 and first die=3)

`P(A) = 6/36 = 1/6`
`P(A cap B) = 1/36`

`P(B | A) = P(A cap B) / P(A) = (1/36) / (1/6) = 1/6`

Alternatively, using the reduced sample space: given A (sum=7), there are 6 equally likely outcomes, and only one of them has first die = 3. So `P(B | A) = 1/6`.

---

#### Example 5: Conditional Probability from a Contingency Table

The following table shows the results of a survey of 200 people categorized by gender and preference for a product:

| | Like Product | Dislike Product | Total |
|---|---|---|---|
| Male | 60 | 40 | 100 |
| Female | 50 | 50 | 100 |
| Total | 110 | 90 | 200 |

Find:
(a) `P(like | male)` -- probability that a randomly selected male likes the product
(b) `P(male | like)` -- probability that a randomly selected person who likes the product is male
(c) Are gender and product preference independent?

**Solution:**
(a) `P(like | male) = P(like cap male) / P(male)`
`P(like cap male) = 60/200 = 0.3`
`P(male) = 100/200 = 0.5`
`P(like | male) = 0.3 / 0.5 = 0.6`

(b) `P(male | like) = P(male cap like) / P(like)`
`P(like) = 110/200 = 0.55`
`P(male | like) = 0.3 / 0.55 = 6/11 = 0.5455`

(c) For independence, we need `P(like | male) = P(like)`, i.e., `0.6 = 0.55`. Since `0.6 != 0.55`, gender and preference are NOT independent.

Alternatively, check if `P(male cap like) = P(male) * P(like)`:
`P(male cap like) = 0.3`
`P(male) * P(like) = 0.5 * 0.55 = 0.275`
Since `0.3 != 0.275`, they are dependent.

---

#### Example 6: The Monty Hall Problem (Preview)

Suppose you are on a game show with three doors. One door hides a car, and the other two hide goats. You pick Door 1. The host (who knows what is behind the doors) opens Door 3, revealing a goat. He then offers you the chance to switch to Door 2. Should you switch?

**Solution using conditional probability:**
Let `C_i` = event that the car is behind Door i (i = 1, 2, 3).
Initially, `P(C_1) = P(C_2) = P(C_3) = 1/3`.

The host always opens a door with a goat, and never opens the door you picked.

We want `P(C_1 | host opens Door 3)` vs. `P(C_2 | host opens Door 3)`.

If the car is behind Door 1 (your pick), the host can open either Door 2 or Door 3 (both have goats). Assume he chooses randomly:
`P(opens 3 | C_1) = 1/2`

If the car is behind Door 2, the host must open Door 3 (the only goat door besides your pick):
`P(opens 3 | C_2) = 1`

If the car is behind Door 3, the host cannot open Door 3 (it has the car):
`P(opens 3 | C_3) = 0`

Using the definition of conditional probability and the law of total probability:
`P(C_1 | opens 3) = P(opens 3 | C_1) * P(C_1) / P(opens 3)`
`P(opens 3) = P(opens 3|C_1)*P(C_1) + P(opens 3|C_2)*P(C_2) + P(opens 3|C_3)*P(C_3)`
`= (1/2)(1/3) + (1)(1/3) + (0)(1/3) = 1/6 + 1/3 = 1/2`

`P(C_1 | opens 3) = (1/2 * 1/3) / (1/2) = 1/3`
`P(C_2 | opens 3) = (1 * 1/3) / (1/2) = 2/3`

Switching doubles your chance of winning from 1/3 to 2/3. This is a famous counterintuitive result.

---

### Relationship Between Independence and Conditional Probability

| Condition | Mathematical Statement |
|---|---|
| A and B are independent | `P(A cap B) = P(A) * P(B)` |
| Equivalent for conditional | `P(A | B) = P(A)` (if `P(B) > 0`) |
| Equivalent for conditional | `P(B | A) = P(B)` (if `P(A) > 0`) |

If `P(A | B) = P(A)`, then knowing B gives no information about A -- this is the intuitive meaning of independence.

---

### Summary Table

| Concept | Formula |
|---|---|
| Definition of conditional probability | `P(A | B) = P(A cap B) / P(B)` |
| Multiplication theorem | `P(A cap B) = P(A) * P(B | A) = P(B) * P(A | B)` |
| Chain rule (3 events) | `P(A cap B cap C) = P(A) * P(B | A) * P(C | A cap B)` |
| Complement rule | `P(A' | B) = 1 - P(A | B)` |
| Independence condition | `P(A | B) = P(A)` iff A and B are independent |

---

## Practice Problems

1. A bag contains 6 red and 4 blue balls. Two balls are drawn one after another WITHOUT replacement. Find:
   (a) `P(both red)`
   (b) `P(second is blue | first is red)`
   (c) `P(first is red | second is blue)`

2. In a class of 60 students, 35 are boys and 25 are girls. Among them, 20 boys and 15 girls wear glasses. A student is selected at random.
   (a) Find the probability that the student wears glasses given that the student is a boy.
   (b) Find the probability that the student is a girl given that the student wears glasses.
   (c) Are gender and wearing glasses independent?

3. A card is drawn from a standard deck. Given that the card is a face card (Jack, Queen, King), find the probability that it is a heart.

4. Two dice are rolled. Find the probability that the sum is at least 8, given that the first die shows a 5.

5. In a certain population, 5% have a disease. A test for the disease has 90% sensitivity and 85% specificity. If a person tests positive, what is the probability they actually have the disease?

---

**Answers/Hints:**
1. (a) `(6/10)(5/9) = 30/90 = 1/3` (b) `4/9` (c) Use Bayes' rule or definition: `P(R_1 | B_2)`. Compute `P(B_2)` via total probability: `(6/10)(4/9)+(4/10)(3/9)=36/90=0.4`. `P(R_1 cap B_2) = (6/10)(4/9)=24/90`. So `P(R_1 | B_2) = 24/36 = 2/3`.
2. (a) 20/35 = 4/7 (b) 15/35 = 3/7 (c) No, `P(glasses) = 35/60 = 7/12`, `P(glasses|boy) = 4/7 != 7/12`.
3. There are 12 face cards, 3 of which are hearts. `P = 3/12 = 1/4`.
4. First die = 5: possible outcomes: (5,1) through (5,6). Sum >= 8: (5,3), (5,4), (5,5), (5,6) = 4 outcomes. `P = 4/6 = 2/3`.
5. `P(D|T) = (0.05*0.90) / (0.05*0.90 + 0.95*0.15) = 0.045/0.1875 = 0.24` (24%).
