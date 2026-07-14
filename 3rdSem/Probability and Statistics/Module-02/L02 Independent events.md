# Independent events

**Course:** Probability and Statistics  
**Module:** 2 | **Lecture:** 2  
**Date:** 31-Jul-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 3.43

## Notes

### Introduction

The concept of independence is central to probability theory. Two events are independent if the occurrence (or non-occurrence) of one does not affect the probability of the occurrence of the other. This idea allows us to simplify many probability calculations.

---

### 1. Definition of Independent Events

**Definition:** Two events `A` and `B` are said to be **independent** if and only if:

`P(A cap B) = P(A) * P(B)`

If this condition does not hold, the events are called **dependent**.

**Intuitive meaning:** Knowing that `B` has occurred gives no information about whether `A` has occurred, and vice versa.

---

### 2. Equivalent Conditions for Independence

If `A` and `B` are independent, then the following pairs are also independent:
- `A` and `B'` (complement of B)
- `A'` and `B` (complement of A)
- `A'` and `B'` (both complements)

**Proof (for A and B'):**
`P(A cap B') = P(A) - P(A cap B)`
`= P(A) - P(A) * P(B)` (since A and B are independent)
`= P(A) * [1 - P(B)]`
`= P(A) * P(B')`

Hence `A` and `B'` are independent.

---

### 3. Pairwise Independence vs. Mutual Independence

**Pairwise independence:** Events `A_1, A_2, ..., A_n` are pairwise independent if every pair of events satisfies the independence condition:
`P(A_i cap A_j) = P(A_i) * P(A_j)` for all `i != j`

**Mutual (or complete) independence:** Events `A_1, A_2, ..., A_n` are mutually independent if for every subset of these events, the probability of their intersection equals the product of their individual probabilities:

`P(A_i cap A_j) = P(A_i) * P(A_j)` for all `i != j`
`P(A_i cap A_j cap A_k) = P(A_i) * P(A_j) * P(A_k)` for all distinct `i, j, k`
...and so on for all subsets.

**Important:** Pairwise independence does NOT imply mutual independence. The classic example below demonstrates this.

---

### 4. Example: Pairwise but Not Mutually Independent

**Example 1 (Bernstein's Example):** Consider tossing two fair coins. Let:
- A = event that the first coin shows Heads
- B = event that the second coin shows Heads
- C = event that exactly one of the two coins shows Heads

Check pairwise independence:
`P(A) = 1/2`, `P(B) = 1/2`, `P(C) = 1/2`

`P(A cap B) = 1/4 = P(A) * P(B)` -- A and B are independent
`P(A cap C)`: A and exactly one head. If A occurs (first coin H), then exactly one head means second coin T. So outcome is HT. `P(A cap C) = 1/4 = P(A) * P(C)` -- A and C are independent
`P(B cap C)`: Similarly, `P(B cap C) = 1/4 = P(B) * P(C)` -- B and C are independent

So A, B, C are pairwise independent.

But check mutual independence (triple intersection):
`P(A cap B cap C)`: A and B and exactly one head. If both coins show Heads (A and B both occur), we have HH, which means NOT exactly one head. So `A cap B cap C = phi`.
`P(A cap B cap C) = 0`
`P(A) * P(B) * P(C) = (1/2)(1/2)(1/2) = 1/8 != 0`

Hence A, B, C are NOT mutually independent, even though they are pairwise independent.

---

### 5. Independent vs. Mutually Exclusive Events

This is a common point of confusion. These two concepts are completely different.

| Property | Mutually Exclusive Events | Independent Events |
|---|---|---|
| Definition | `A cap B = phi` | `P(A cap B) = P(A) * P(B)` |
| Can they occur together? | NO | MAYBE (if both have positive probability) |
| `P(A cap B)` | 0 | `P(A) * P(B)` (non-zero if both probabilities > 0) |
| `P(A cup B)` | `P(A) + P(B)` | `P(A) + P(B) - P(A)P(B)` |
| Relationship when `P(A) > 0` and `P(B) > 0` | Mutually exclusive events with positive probability CANNOT be independent | Independent events with positive probability CANNOT be mutually exclusive |

**Why mutually exclusive events (with positive probability) cannot be independent:**
If `A` and `B` are mutually exclusive, then `P(A cap B) = 0`. For independence, we need `P(A cap B) = P(A) * P(B)`. If `P(A) > 0` and `P(B) > 0`, then `P(A) * P(B) > 0`, which contradicts `P(A cap B) = 0`.

Similarly, if `A` and `B` are independent and both have positive probability, then `P(A cap B) = P(A) * P(B) > 0`, so they cannot be mutually exclusive.

---

### 6. Multiplication Theorem for Independent Events

**Theorem:** If `A` and `B` are independent events, then:
`P(A cap B) = P(A) * P(B)`

**Generalization:** If `A_1, A_2, ..., A_n` are mutually independent events, then:
`P(A_1 cap A_2 cap ... cap A_n) = P(A_1) * P(A_2) * ... * P(A_n)`

**Special case (complements):** If `A_1, A_2, ..., A_n` are independent events, then:
`P(A_1' cap A_2' cap ... cap A_n') = P(A_1') * P(A_2') * ... * P(A_n')`

---

### 7. Worked Examples

**Example 2 (Coin Toss):** A fair coin is tossed 3 times. Find the probability of getting:
(a) Three heads
(b) At least one head
(c) Exactly two heads

**Solution:**
Let `H_i` = event of getting head on the i-th toss. Since the coin is fair and tosses are independent:
`P(H_i) = 1/2` for each i.

(a) `P(H_1 cap H_2 cap H_3) = P(H_1) * P(H_2) * P(H_3) = (1/2)^3 = 1/8`

(b) `P(at least one head) = 1 - P(no heads) = 1 - P(H_1' cap H_2' cap H_3')`
`= 1 - P(H_1') * P(H_2') * P(H_3') = 1 - (1/2)^3 = 1 - 1/8 = 7/8`

(c) Exactly two heads: any one of the three tosses is a tail.
`P(HT H) + P(TH T) + P(T T H)` approach: First, probability of any specific sequence with exactly 2 heads (e.g., HHT) = `(1/2)^3 = 1/8`
Number of sequences with exactly 2 heads = `C(3,2) = 3`
`P(exactly 2 heads) = 3 * 1/8 = 3/8`

---

**Example 3 (Dice Roll):** Two fair dice are rolled. Are the following pairs of events independent?
(a) A = first die shows even, B = second die shows odd
(b) A = sum is 7, B = first die shows 4

**Solution:**
(a) `P(A) = 1/2`, `P(B) = 1/2`
`A cap B` = {first die even, second die odd}. Number of outcomes: 3 (even on first) * 3 (odd on second) = 9
`P(A cap B) = 9/36 = 1/4 = P(A) * P(B)`
Hence A and B are independent.

(b) `P(A) = P(sum = 7) = 6/36 = 1/6`
`P(B) = P(first die = 4) = 6/36 = 1/6`
`A cap B` = {first die = 4, sum = 7} = {(4,3)} -- 1 outcome
`P(A cap B) = 1/36`
`P(A) * P(B) = (1/6)(1/6) = 1/36`
Since `P(A cap B) = P(A)*P(B)`, A and B are independent.

---

**Example 4 (Cards):** Two cards are drawn from a well-shuffled deck of 52 cards WITH replacement.
(a) Find the probability that both are aces.
(b) Find the probability that the first is a king and the second is a queen.

**Solution:**
Since the card is replaced, the draws are independent.

(a) `P(both aces) = P(ace on 1st) * P(ace on 2nd) = (4/52) * (4/52) = (1/13)^2 = 1/169`

(b) `P(king then queen) = (4/52) * (4/52) = 1/169`

---

**Example 5 (System Reliability):** A system consists of three components A, B, C connected in series (all must work for the system to function). The components work independently with probabilities: `P(A works) = 0.9`, `P(B works) = 0.85`, `P(C works) = 0.95`. Find the reliability of the system.

**Solution:**
System reliability = `P(all three components work)`
`= P(A) * P(B) * P(C)` (since independent)
`= 0.9 * 0.85 * 0.95`
`= 0.72675`

The system reliability is about 0.727.

---

**Example 6 (Parallel System):** For the same three components, if they are connected in parallel (at least one must work for the system to function), find the reliability.

**Solution:**
System fails only if ALL components fail.
`P(A fails) = 1 - 0.9 = 0.1`
`P(B fails) = 1 - 0.85 = 0.15`
`P(C fails) = 1 - 0.95 = 0.05`

`P(system fails) = P(A fails) * P(B fails) * P(C fails) = 0.1 * 0.15 * 0.05 = 0.00075`

`P(system works) = 1 - P(system fails) = 1 - 0.00075 = 0.99925`

Parallel systems are much more reliable than series systems.

---

**Example 7 (Conditional Probability View):** A problem in a test is given to three students A, B, C whose probabilities of solving it independently are 1/2, 1/3, and 1/4 respectively. Find the probability that:
(a) All three solve it
(b) None solves it
(c) At least one solves it

**Solution:**
(a) `P(all solve) = (1/2)(1/3)(1/4) = 1/24`

(b) `P(none solves) = P(A fails)*P(B fails)*P(C fails) = (1-1/2)(1-1/3)(1-1/4) = (1/2)(2/3)(3/4) = 6/24 = 1/4`

(c) `P(at least one solves) = 1 - P(none solves) = 1 - 1/4 = 3/4`

---

### Summary

- Two events A and B are independent iff `P(A cap B) = P(A) * P(B)`.
- Pairwise independence does not imply mutual independence; the coin-toss example demonstrates this.
- Mutually exclusive events (with positive probability) cannot be independent, and vice versa.
- The multiplication theorem simplifies probability calculations for independent events, especially in series/parallel system reliability problems.

---

## Practice Problems

1. A fair coin is tossed 5 times. Find the probability of getting:
   (a) all heads
   (b) at least one tail
   (c) exactly 3 heads

   <details>
   <summary>Show Answer</summary>
   1. (a) 1/32 (b) 31/32 (c) `C(5,3)/32 = 10/32 = 5/16`
   </details>

2. The probability that A hits a target is 1/4 and the probability that B hits the same target is 2/5. If each fires one shot independently, find the probability that:
   (a) both hit the target
   (b) the target is hit at least once
   (c) exactly one of them hits the target

   <details>
   <summary>Show Answer</summary>
   2. (a) 1/10 (b) 11/20 (c) `P(A hits, B misses) + P(A misses, B hits) = (1/4)(3/5) + (3/4)(2/5) = 9/20`
   </details>

3. A bag contains 4 red and 3 black balls. A ball is drawn at random, its color is noted, and the ball is replaced. Then another ball is drawn. Find the probability of getting:
   (a) both red
   (b) first red, second black
   (c) one red and one black

   <details>
   <summary>Show Answer</summary>
   3. Note: with replacement, draws are independent. (a) `(4/7)^2 = 16/49` (b) `(4/7)(3/7) = 12/49` (c) `2 * (4/7)(3/7) = 24/49`
   </details>

4. Events A and B are such that `P(A) = 0.6`, `P(B) = 0.4`, and `P(A cap B) = 0.24`. Check if:
   (a) A and B are independent
   (b) A and B are mutually exclusive

   <details>
   <summary>Show Answer</summary>
   4. (a) Yes, because `P(A)*P(B) = 0.24 = P(A cap B)` (b) No, because `P(A cap B) != 0`
   </details>

5. A system has 4 components in series, each with reliability 0.9. Find the system reliability. What would it be if they were in parallel?
   <details>
   <summary>Show Answer</summary>
   5. Series: `0.9^4 = 0.6561`. Parallel: `1 - (0.1)^4 = 0.9999`.
   </details>
