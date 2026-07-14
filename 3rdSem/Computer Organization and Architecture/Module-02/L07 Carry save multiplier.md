# Carry save multiplier

**Course:** Computer Organization and Architecture  
**Module:** 2 | **Lecture:** 7  
**Date:** 11-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Motivation

The shift-and-add multiplier requires n cycles for n-bit multiplication. Even Booth's algorithm requires n/2 cycles for radix-4. For high-performance computing, we need **parallelism** in multiplication. The **carry save multiplier** (also called the Wallace tree or Dadda multiplier) uses a parallel array of adders to compute all partial products simultaneously and sum them in O(log n) gate delays.

### 2. Carry Save Adder (CSA) Concept

A **carry save adder** takes three input bits and produces two output bits: a sum bit and a carry bit. Unlike a full adder which produces a single output, the CSA keeps the sum and carry separate.

#### CSA Block Diagram

```
A ---|       |
B ---|  CSA  |--- Sum (S)
C ---|       |
     |       |--- Carry (Cout)
     |       |
```

- **Sum** = A XOR B XOR C (same as full adder sum)
- **Carry** = (A AND B) OR (B AND C) OR (A AND C) (same as full adder carry)

A CSA is functionally identical to a full adder but the outputs remain **uncombined** (not added together). This is the key: the carry is not propagated to the next bit position within the same stage.

### 3. CSA Property: Reducing Three Rows to Two

Given three rows of binary numbers, a single stage of CSAs can reduce them to two rows:
- One row of sum bits.
- One row of carry bits (each shifted left by 1 position, since carries go to the next higher bit).

This is called **3:2 compression** (three inputs, two outputs per bit position).

```
    Bit position:  3     2     1     0
                 +----------------------+
Row 1:           a3    a2    a1    a0
Row 2:           b3    b2    b1    b0
Row 3:           c3    c2    c1    c0
                 +----------------------+
                 |   Array of CSAs      |
                 +----------------------+
                 |      |      |      |
                 v      v      v      v
Sum row:         s3     s2     s1     s0
Carry row:      c4     c3     c2     c1    0
(shifted left 1, so carry_i contributes to bit i+1)
```

### 4. Wallace Tree Multiplier

A Wallace tree multiplier uses multiple levels of CSAs to reduce the partial products to just two rows, then a final carry propagate adder (CPA) adds them.

#### Partial Product Generation

For an n x n multiplication, n partial products are generated using AND gates. Each partial product bit p_ij = Ai AND Bj.

Example: 4x4 multiplication, A = A3 A2 A1 A0, B = B3 B2 B1 B0.

```
Partial products (PP):
PP0: A3B0  A2B0  A1B0  A0B0
PP1: A3B1  A2B1  A1B1  A0B1
PP2: A3B2  A2B2  A1B2  A0B2
PP3: A3B3  A2B3  A1B3  A0B3
```

Each PP_i is shifted left by i positions. Together they form an array of 4 rows.

#### Reduction Stages (ASCII Diagram)

```
Stage 0: 4 rows of partial products
  Row0:  . . . .
  Row1: . . . .
  Row2: . . . .
  Row3: . . . .
      |
      |  Use CSAs to reduce
      v
Stage 1: 3 rows (compress one group of 3 rows to 2)
  RowA: . . . .
  RowB: . . . .
  RowC: . . . .
      |
      |  Use CSAs to reduce
      v
Stage 2: 2 rows (compress again)
  Sum:  . . . . . .
  Carry:. . . . . .
      |
      |  Final CPA (carry propagate adder, e.g., CLA)
      v
  Product: 8-bit result
```

The Wallace tree reduction proceeds by:
1. Group rows into sets of 3.
2. Apply CSAs to each group of 3 rows, producing 2 rows.
3. Repeat until only 2 rows remain.
4. Add the final 2 rows with a CPA.

#### Reduction Pattern

Number of rows after each stage:

| Initial rows | After 1 CSA stage | After 2 CSA stages | After 3 CSA stages |
|-------------|-------------------|-------------------|-------------------|
| 3           | 2                 | -                 | -                 |
| 4           | 3                 | 2                 | -                 |
| 5           | 4                 | 3                 | 2                 |
| 6           | 4                 | 3                 | 2                 |
| 7           | 5                 | 4                 | 2                 |
| 8           | 6                 | 4                 | 2                 |
| 9           | 6                 | 4                 | 2                 |

In general, the number of stages required is O(log n).

### 5. Example: 4x4 Multiplication Using CSA

Compute A = 0110 (6) x B = 0101 (5).

#### Step 1: Generate partial products

```
PP0 (shift 0):  A3*B0 A2*B0 A1*B0 A0*B0
                  0     1     0     0    (because B0=1)

PP1 (shift 1):  A3*B1 A2*B1 A1*B1 A0*B1
                  0     1     0     0     (B1=0, so all 0)

PP2 (shift 2):  A3*B2 A2*B2 A1*B2 A0*B2
                  1     0     0     0     (B2=1)

PP3 (shift 3):  A3*B3 A2*B3 A1*B3 A0*B3
                  0     0     0     0     (B3=0)
```

Aligned by bit position:

```
Bit position:  6  5  4  3  2  1  0
PP0:                   0  1  0  0
PP1:                0  1  0  0
PP2:             1  0  0  0
PP3:          0  0  0  0
                         (actually PP3=all 0)
```

Let me write them properly aligned (with 0s for empty positions):

```
Pos:    6   5   4   3   2   1   0
PP0:                    0   1   0   0
PP1:                0   1   0   0   0
PP2:            1   0   0   0   0
PP3:        0   0   0   0   0
```

Wait, PP1 shifted by 1: A3B1 A2B1 A1B1 A0B1 = 0,1,0,0 at positions 4,3,2,1.
PP2 shifted by 2: A3B2 A2B2 A1B2 A0B2 = 1,0,0,0 at positions 5,4,3,2.
PP3 shifted by 3: A3B3 A2B3 A1B3 A0B3 = 0,0,0,0 at positions 6,5,4,3.

So:
```
Pos:    6   5   4   3   2   1   0
PP0:                    0   1   0   0
PP1:                0   1   0   0   0
PP2:            1   0   0   0   0
PP3:        0   0   0   0   0   0   0
```

#### Step 2: Reduction Stage 1

Group PP0, PP1, PP2 (3 rows) into 2 rows using CSAs.

For each bit position (0 to 5), apply a CSA to the three bits:

```
Pos 0: PP0=0, PP1=0, PP2=0 => S=0, C=0
Pos 1: PP0=0, PP1=0, PP2=0 => S=0, C=0
Pos 2: PP0=0, PP1=0, PP2=0 => S=0, C=0
Pos 3: PP0=1, PP1=0, PP2=0 => S=1, C=0
Pos 4: PP0=0, PP1=1, PP2=0 => S=1, C=0
Pos 5: PP0=0, PP1=0, PP2=1 => S=1, C=0
```

After Stage 1:
Sum row:  ...0 1 1 1 0 0 0 (positions 5-0)
Carry row:...0 0 0 0 0 0 0 (all 0, shifted left 1)

#### Step 3: Reduction Stage 2

We now have 2 rows (Sum and Carry from Stage 1) plus PP3 (all 0s). Total 3 rows -> reduce to 2.

Since PP3 is all 0s, the result after Stage 2 is the same as after Stage 1.

#### Step 4: Final addition

Add Sum and Carry with a CPA:

Sum:  0 1 1 1 0 0 0
Carry:0 0 0 0 0 0 0
-------------------
Prod: 0 1 1 1 0 0 0 = 24 + 16 + 8 + 4 = ... wait.

Let me trace more carefully. A = 0110 (6), B = 0101 (5).

PP0: B0=1, so PP0 = A = 0110
PP1: B1=0, so PP1 = 0
PP2: B2=1, so PP2 = A shifted left 2 = 011000
PP3: B3=0, so PP3 = 0

Aligning:
```
Pos: 7  6  5  4  3  2  1  0
PP0:            0  1  1  0    (6)
PP1:         0  0  0  0  0    (0)
PP2:   0  1  1  0  0  0  0    (24)
PP3: 0 0  0  0  0  0  0  0    (0)
```

So let's do the reduction properly.

Stage 1: CSA on PP0, PP1, PP2 (3 rows -> 2 rows)

```
Pos 0: 0,0,0 => S=0, C=0
Pos 1: 0,0,0 => S=0, C=0
Pos 2: 1,0,0 => S=1, C=0
Pos 3: 1,0,0 => S=1, C=0
Pos 4: 0,0,1 => S=1, C=0
Pos 5: 0,0,1 => S=1, C=0
Pos 6: 0,0,0 => S=0, C=0
```

Sum row (Stage 1): 0 1 1 1 1 0 0 (positions 6-0)
Carry row (Stage 1): all 0s

Stage 2: Sum row + Carry row + PP3 (all 0s) -> 2 rows. Again same.

Final CPA: Sum + 0 = Sum = 0 1 1 1 1 0 0

0111100 = 32 + 16 + 8 + 4 = 60. Check: 6 x 5 = 30. Wait, that's wrong.

Ah I made an error in PP2. A = 0110, B = 0101. PP2 uses B2=1, shifted left 2: 0110 << 2 = 011000 = 24. But PP0 is 0110 = 6. So PP0 + PP2 = 30. But PP1 = 0.

Let me redo: 6 x 5 = 30. In binary 30 = 0011110 (7 bits).

So the CSA should give 30. Let me recalculate with correct shifting.

Actually I think my alignment was wrong. Let me be more systematic.

For 4-bit multiplication:
PP(i) = A AND (replicate Bi) shifted left by i

PP0: each bit = Aj AND B0. B0 = 1, so PP0 = A = 0110
PP1: each bit = Aj AND B1. B1 = 0, so PP1 = 0
PP2: each bit = Aj AND B2. B2 = 1, so PP2 = A shifted left 2 = 11000
PP3: each bit = Aj AND B3. B3 = 0, so PP3 = 0

Wait, for PP2, A3B2, A2B2, A1B2, A0B2:
A3=0, A2=1, A1=1, A0=0. B2=1. So PP2 bits = 0,1,1,0 at positions 5,4,3,2.

So:
```
Pos:    6   5   4   3   2   1   0
PP0:                    0   1   1   0
PP1:                0   0   0   0   0
PP2:            0   1   1   0   0
PP3:        0   0   0   0   0   0   0
```

Wait, PP2 values at positions 5,4,3,2: A3B2=0, A2B2=1, A1B2=1, A0B2=0. So bits: pos5=0, pos4=1, pos3=1, pos2=0. But we also have implicit 0s. So:

```
Pos:    6   5   4   3   2   1   0
PP0:                    0   1   1   0
PP1:                0   0   0   0   0
PP2:            0   1   1   0   0   0   0  (PP2 starts at pos 2, so pos5=0, pos4=1, pos3=1, pos2=0, pos1=0, pos0=0)
```

Wait, A = 0110 means A3=0, A2=1, A1=1, A0=0.
PP2 = bits at position 2,3,4,5:
- A0B2 at pos 2: 0 * 1 = 0
- A1B2 at pos 3: 1 * 1 = 1
- A2B2 at pos 4: 1 * 1 = 1
- A3B2 at pos 5: 0 * 1 = 0

So PP2 = 0 1 1 0 at positions 5 4 3 2.

```
Pos:    6   5   4   3   2   1   0
PP0:    0   0   0   0   1   1   0   (0 1 1 0 at positions 3 2 1 0)
PP1:    0   0   0   0   0   0   0   (all zeros)
PP2:    0   0   1   1   0   0   0   (0 1 1 0 at positions 5 4 3 2, shifted from PP0)
```

No wait, I'm confusing myself. Let me use a proper representation.

PP0 (shift 0): A3B0, A2B0, A1B0, A0B0 = 0*1, 1*1, 1*1, 0*1 = 0,1,1,0
At bit positions: 3,2,1,0

PP1 (shift 1): A3B1, A2B1, A1B1, A0B1 = 0*0, 1*0, 1*0, 0*0 = 0,0,0,0
At bit positions: 4,3,2,1

PP2 (shift 2): A3B2, A2B2, A1B2, A0B2 = 0*1, 1*1, 1*1, 0*1 = 0,1,1,0
At bit positions: 5,4,3,2

PP3 (shift 3): A3B3, A2B3, A1B3, A0B3 = 0*0, 1*0, 1*0, 0*0 = 0,0,0,0
At bit positions: 6,5,4,3

Aligned array:
```
Bit:    6   5   4   3   2   1   0
PP0:                    0   1   1   0
PP1:                0   0   0   0   0
PP2:            0   1   1   0   0
PP3:        0   0   0   0   0   0
```

Now let's add all 4 rows: 6 (PP0) + 0 (PP1) + 24 (PP2) + 0 (PP3) = 30. 30 in binary = 011110 (6 bits).

Let me verify adding them manually:
```
PP0:         0 1 1 0   (6)
PP1:       0 0 0 0 0   (0, shifted 1 = 0)
PP2:     0 1 1 0 0 0   (24, shifted 2)
PP3:   0 0 0 0 0 0 0   (0)
```

Bit addition:
- Bit 0: 0 = 0
- Bit 1: 1 = 1
- Bit 2: 1+0 = 1
- Bit 3: 0+0+1 = 1
- Bit 4: 0+0+1 = 1
- Bit 5: 0+0+0 = 0
- Bit 6: 0 = 0

Result: 011110 = 30. Correct!

OK so for this simple example, the partial products are only 2 non-trivial rows (PP0 and PP2). The CSA just passes them through and the final CPA adds them.

For a more complex example, we'd need more active rows. Let me use A=1111 (15), B=1111 (15) instead.

A=1111, B=1111, all Bi=1, so all PP are non-zero.

PP0 = 1111 (shift 0) at positions 3,2,1,0
PP1 = 1111 (shift 1) at positions 4,3,2,1
PP2 = 1111 (shift 2) at positions 5,4,3,2
PP3 = 1111 (shift 3) at positions 6,5,4,3

```
Bit:     6   5   4   3   2   1   0
PP0:                    1   1   1   1
PP1:                1   1   1   1   0
PP2:            1   1   1   1   0   0
PP3:        1   1   1   1   0   0   0
```

Total = 15 x 15 = 225 = 11100001.

Stage 1: CSA reduces PP0, PP1, PP2 (3 rows) -> 2 rows.

For each bit position (0 to 5):
```
Pos 0: 1,0,0 => S=1, C=0
Pos 1: 1,1,0 => S=0, C=1
Pos 2: 1,1,1 => S=1, C=1
Pos 3: 1,1,1 => S=1, C=1
Pos 4: 0,1,1 => S=0, C=1
Pos 5: 0,0,1 => S=1, C=0
```

After Stage 1:
Sum (S):    1 0 1 1 0 1 0 (positions 5-0, carries generated)
Actually, S bits: pos0=1, pos1=0, pos2=1, pos3=1, pos4=0, pos5=1
Carry (C):  pos1=1, pos2=1, pos3=1, pos4=1, pos5=0, pos6=0
Shifted left: C contributes to pos+1

So after Stage 1:
Sum row:   1 0 1 1 0 1  (positions 5-0)
Carry row: 0 1 1 1 1 0  (positions 6-1, shifted)

Aligning with PP3:
```
Bit:     6   5   4   3   2   1   0
Sum:         1   0   1   1   0   1
Carry:   0   1   1   1   1   0
PP3:     1   1   1   1   0   0   0
```

Stage 2: CSA on Sum, Carry, PP3 (3 rows -> 2 rows).

Pos 0: 1,0,0 => S=1, C=0
Pos 1: 0,0,0 => S=0, C=0
Pos 2: 1,1,0 => S=0, C=1
Pos 3: 1,1,1 => S=1, C=1
Pos 4: 0,1,1 => S=0, C=1
Pos 5: 1,1,1 => S=1, C=1
Pos 6: 0,0,1 => S=1, C=0

After Stage 2:
Sum:   1 0 1 0 0 1 (positions 6-0, need to work this out properly)

S: pos0=1, pos1=0, pos2=0, pos3=1, pos4=0, pos5=1, pos6=1
C:           pos2=1, pos3=1, pos4=1, pos5=1, pos6=0

Wait, let me compute carefully:

Sum bits: S_i = (Sum_in_i + Carry_in_i + PP3_i) mod 2

Sum_in:   [6]=0, [5]=1, [4]=0, [3]=1, [2]=1, [1]=0, [0]=1  (correcting - Sum row had positions 5-0)
Wait, I wrote Sum row after Stage 1 as having bits at positions 5-0:
Pos 5: 1, Pos 4: 0, Pos 3: 1, Pos 2: 1, Pos 1: 0, Pos 0: 1

Carry row after Stage 1 (shifted left 1):
Pos 6: 0 (from pos5 carry=0)
Pos 5: 1 (from pos4 carry=1)
Pos 4: 1 (from pos3 carry=1)
Pos 3: 1 (from pos2 carry=1)
Pos 2: 1 (from pos1 carry=1)
Pos 1: 0

PP3: [6]=1, [5]=1, [4]=1, [3]=1, [2]=0, [1]=0, [0]=0

Stage 2 CSA inputs:

Pos 0: Sum=1, Carry=0, PP3=0 -> S=1, C=0
Pos 1: Sum=0, Carry=0, PP3=0 -> S=0, C=0
Pos 2: Sum=1, Carry=1, PP3=0 -> S=0, C=1
Pos 3: Sum=1, Carry=1, PP3=1 -> S=1 (1+1+1=3, 3 mod 2 = 1), C=1
Pos 4: Sum=0, Carry=1, PP3=1 -> S=0 (0+1+1=2, 2 mod 2 = 0), C=1
Pos 5: Sum=1, Carry=1, PP3=1 -> S=1 (1+1+1=3), C=1
Pos 6: Sum=0, Carry=0, PP3=1 -> S=1, C=0

After Stage 2:
Sum row: S6=1, S5=1, S4=0, S3=1, S2=0, S1=0, S0=1 = 1101001
Carry row (shifted): C7=0, C6=0, C5=1, C4=1, C3=1, C2=0 = 011100

Final CPA adds Sum + Carry:

Sum:    1 1 0 1 0 0 1 (positions 6-0)
Carry:  0 1 1 1 0 0   (positions 6-1, shifted)
Wait, the carry row from Stage 2: pos2 C=1, pos3 C=1, pos4 C=1, pos5 C=1, pos6 C=0.
So carry contributes to positions 3,4,5,6: bits at pos3=1, pos4=1, pos5=1, pos6=0.

Let me redo Carry row from Stage 2:
C0=0 at pos1 (from pos0)
C1=0 at pos2 (from pos1)
C2=1 at pos3 (from pos2)
C3=1 at pos4 (from pos3)
C4=1 at pos5 (from pos4)
C5=1 at pos6 (from pos5)
C6=0 at pos7 (from pos6)

Carry row bits: pos7=0, pos6=1, pos5=1, pos4=1, pos3=1, pos2=0, pos1=0

Adding Sum (1101001) and Carry (0111100):
```
  1111
  1101001
  0111100
  --------
 11100001
```

Wait: 1101001 + 0111100:

```
Pos 0: 1+0=1
Pos 1: 0+0=0
Pos 2: 0+1(carry from pos1=0)+0=0 
```

Actually let me add properly:

```
        1 1 0 1 0 0 1
+       0 1 1 1 1 0 0
= 1 1 1 0 0 0 0 1
```

Wait:
- Bit 0: 1+0 = 1, carry 0
- Bit 1: 0+0 = 0, carry 0
- Bit 2: 0+1 = 1, carry 0... 

Hmm, let me just do binary addition:
```
Carry: 1 1 1 0 0 0 0
Sum:   1 1 0 1 0 0 1
Carry: 0 1 1 1 1 0 0
       -----------
       1 1 1 0 0 0 0 1
```

Starting from LSB (bit 0):
1+0=1, carry 0
0+0=0, carry 0
0+1=1, carry 0
1+1=0, carry 1
0+1+carry1=0, carry 1
1+1+carry1=1, carry 1
1+0+carry1=0, carry 1
carry 1

Result: 11100001 = 225. Correct!

This demonstrates the CSA reduction correctly.

### 6. Speed Advantage

The Wallace tree multiplier has O(log n) delay compared to O(n) for shift-and-add:

- **Partial product generation**: 1 gate delay (AND gates).
- **Reduction tree**: O(log n) CSA stages. Each CSA stage adds ~1 gate delay.
- **Final CPA**: O(log n) using CLA.

**Total delay** = 1 + O(log n) + O(log n) = O(log n).

For n=64:
- Shift-and-add: 64 cycles = 64 x t_cycle (could be hundreds of gate delays).
- Wallace tree: ~12-15 CSA stages + CLA = ~15-20 gate delays.

### 7. Disadvantage

1. **Irregular layout**: Wallace tree has irregular wiring, making VLSI layout difficult.
2. **High area**: Many CSAs and complex routing.
3. **High power**: More gates switching simultaneously.
4. **Routing congestion**: The irregular reduction tree requires many interconnections.

The **Dadda multiplier** is a variant that minimizes the number of CSAs and has a more regular structure, at the cost of slightly more delay.

### 8. Hardware Diagram for 4x4 CSA Multiplier (ASCII)

```
A3A2A1A0 (multiplicand)        B3B2B1B0 (multiplier)
    |                              |
    +------+----+----+----+-------+
           |    |    |    |
           v    v    v    v
    +----+ AND gates (16 total)
    |    | generate 4 partial products
    +----+
    |    |    |    |
    v    v    v    v
   PP3  PP2  PP1  PP0  (4 rows of partial products)
    |    |    |    |
    +----+----+----+
         |
         v
    +---------+
    | CSA     |  Stage 1: Reduce 3 rows (PP0, PP1, PP2) -> 2 rows
    | Tree    |           (or 3 CSAs per bit position)
    +---------+
         |
         v
    +---------+
    | CSA     |  Stage 2: Reduce 3 rows (Sum1, Carry1, PP3) -> 2 rows
    | Tree    |
    +---------+
         |
         v
    +---------+
    |  CPA    |  Final carry propagate adder (e.g., CLA)
    |(n-bit)  |
    +---------+
         |
         v
    Product (8 bits)
```

---

## Practice Problems

1. **3:2 compression**: Show how three numbers X=101, Y=110, Z=011 are reduced to two numbers using a carry save adder.
<details>
<summary>Show Answer</summary>
     Bit 0: 1+0+1=2 => S=0, C=1 (pos 1)
     Bit 1: 0+1+1=2 => S=0, C=1 (pos 2)
     Bit 2: 1+1+0=2 => S=0, C=1 (pos 3)
     Sum = 000, Carry = 1110
     Sum + Carry = 000 + 1110 = 1110 = 14. Check: 5+6+3 = 14. Correct.
</details>

2. **Wallace tree reduction**: For an 8x8 multiplier, how many partial products are generated, and how many reduction stages are needed?
<details>
<summary>Show Answer</summary>
8 partial products. Reduction: 8->6 (stage 1), 6->4 (stage 2), 4->3 (stage 3), 3->2 (stage 4). Total 4 stages. Final CPA. Total ~5-6 stages.
</details>

3. **CSA advantage**: Why is keeping the carry separate in a CSA beneficial for multiplication?
<details>
<summary>Show Answer</summary>
The carry does not propagate within the CSA stage, so all CSAs in a stage operate in parallel with O(1) delay. Only the final CPA has carry propagation. This avoids the O(n) carry chain for intermediate sums.
</details>

4. **4x4 CSA**: Multiply A=1010 (10) by B=0011 (3) using the CSA reduction method.
<details>
<summary>Show Answer</summary>
     PP0=1010, PP1=0000 (B1=0), PP2=101000<<2=10<<2... Actually: PP2 = A shifted 2 = 101000 = 40, PP3=0. 
     PP0=1010 at pos 3-0, PP2=1010 at pos 5-2.
     Stage 1: Reduce PP0, PP1, PP2: 
      Pos 0: 0,0,0=0
      Pos 1: 1,0,0 => sum=1, carry=0
      Pos 2: 0,0,1 => sum=1, carry=0
      Pos 3: 1,0,0 => sum=1, carry=0
      Pos 4: 0,0,1 => sum=1, carry=0
      Pos 5: 0,0,0 => sum=0, carry=0
     Sum=011110, Carry=0. + PP3=0 => 011110 = 30. Check: 10x3=30.
</details>

5. **Compare**: Compare the number of full adders needed for a 4-bit shift-and-add multiplier vs a 4-bit CSA multiplier.
<details>
<summary>Show Answer</summary>
Shift-and-add: 1 n-bit adder (4 FAs) reused 4 times sequentially. CSA: ~4 CSAs per stage, 2 stages + final CPA (4 FAs) = ~12 FAs. CSA uses more hardware but is faster.
</details>