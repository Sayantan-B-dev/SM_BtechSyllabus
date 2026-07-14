# Ripple carry adder

**Course:** Computer Organization and Architecture  
**Module:** 2 | **Lecture:** 3  
**Date:** 29-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Full Adder Review

A **full adder** (FA) adds three 1-bit inputs (A, B, Carry-in Ci) and produces two outputs: Sum (S) and Carry-out (Co).

#### Truth Table

| A | B | Ci | S  | Co |
|---|---|----|----|----|
| 0 | 0 | 0  | 0  | 0  |
| 0 | 0 | 1  | 1  | 0  |
| 0 | 1 | 0  | 1  | 0  |
| 0 | 1 | 1  | 0  | 1  |
| 1 | 0 | 0  | 1  | 0  |
| 1 | 0 | 1  | 0  | 1  |
| 1 | 1 | 0  | 0  | 1  |
| 1 | 1 | 1  | 1  | 1  |

#### Logic Expressions

- **S** = A XOR B XOR Ci
- **Co** = (A AND B) OR (Ci AND (A XOR B))
  *Alternate form*: Co = AB + ACi + BCi

#### Gate-Level Implementation

```
A ---|      |
     | XOR  |--- A XOR B ---|      |
B ---|      |               | XOR  |--- S
                            |      |
Ci ------------------------|      |

A ---|      |
     | AND  |--- AB -------|      |
B ---|      |               | OR   |--- Co
                            |      |
A ---|      |               |      |
     | XOR  |--- A XOR B --| AND  |
B ---|      |              |      |
                    Ci ----|      |
```

### 2. Ripple Carry Adder (RCA) Concept

A **ripple carry adder** connects multiple full adders in series. The carry-out of each full adder becomes the carry-in of the next higher-order full adder. The carry "ripples" from the least significant bit (LSB) to the most significant bit (MSB).

#### 4-bit Ripple Carry Adder ASCII Diagram

```
A3  B3               A2  B2               A1  B1               A0  B0
 |   |                |   |                |   |                |   |
 v   v                v   v                v   v                v   v
+-------+            +-------+            +-------+            +-------+
|  FA   |<--- C3 --- |  FA   |<--- C2 --- |  FA   |<--- C1 --- |  FA   |<--- Cin (0 for add)
|       |            |       |            |       |            |       |
+-------+            +-------+            +-------+            +-------+
  |                        |                        |                        |
  v                        v                        v                        v
 S3 (MSB)                 S2                       S1                       S0 (LSB)
  |
Cout (overflow)
```

Here Cin is the input carry to the least significant bit (typically 0 for addition, 1 for subtraction when complemented).

### 3. Carry Propagation Delay

The key drawback of the ripple carry adder is the **carry propagation delay**. Each full adder must wait for the carry from the previous stage before it can compute its sum and carry-out.

#### Delay Calculation

Let t_FA be the delay of one full adder from carry-in to carry-out.

For an n-bit ripple carry adder:
- Stage 0: Sum S0 available after t_FA (since Ci0 = Cin is known).
- Stage 1: Carry C1 available after t_FA, then S1 available after another t_FA.
- Stage k: Sum Sk available after (k+1) * t_FA.

**Total delay** for n-bit addition:
- t_adder = n * t_FA

For the final carry-out (overflow), delay = n * t_FA.
For the MSB sum, delay = n * t_FA (since it depends on carry from stage n-2 through stage n-1).

#### Numerical Example

If each full adder has a gate delay of 2 ns:
- 4-bit RCA: 4 x 2 = 8 ns
- 16-bit RCA: 16 x 2 = 32 ns
- 32-bit RCA: 32 x 2 = 64 ns
- 64-bit RCA: 64 x 2 = 128 ns

As bit-width increases, the delay grows linearly, making the RCA very slow for large n.

### 4. Why Ripple Carry Is Slow

The slowness comes from the **sequential dependency** of the carry signal:
- The carry must propagate through every full adder stage sequentially.
- This is a linear chain: each stage depends on the previous stage's carry output.
- No parallelism is possible in the carry path.
- The path: C0 -> FA0 -> C1 -> FA1 -> C2 -> ... -> FA(n-1) -> Cn.

### 5. Worked Example: 4-bit Addition Timing

Add A = 0111 (7) and B = 0001 (1), Cin = 0.

| Time   | Event                                                       |
|--------|-------------------------------------------------------------|
| t = 0  | Inputs applied: A=0111, B=0001, Cin=0                       |
| t = 2ns| FA0 computes: S0 = 1 XOR 1 XOR 0 = 0, C1 = 1 AND 1 = 1     |
| t = 4ns| FA1 receives C1=1. S1 = 1 XOR 0 XOR 1 = 0, C2 = 1 AND 0 OR (1 AND (1 XOR 0)) = 1 |
| t = 6ns| FA2 receives C2=1. S2 = 1 XOR 0 XOR 1 = 0, C3 = 1 AND 0 OR ... = 1 |
| t = 8ns| FA3 receives C3=1. S3 = 0 XOR 0 XOR 1 = 1, C4 = 0          |

Final result: C4 S3 S2 S1 S0 = 0 1 0 0 0 = 8. Correct (7+1=8).

### 6. Advantages of Ripple Carry Adder

1. **Simple design**: Only requires full adders connected in series.
2. **Low hardware cost**: No extra logic gates beyond the full adders.
3. **Regular layout**: Easy to implement in VLSI (bit-slice design).
4. **Small chip area**: Minimal transistor count.
5. **Conceptually straightforward**: Easy to understand and teach.

### 7. Disadvantages of Ripple Carry Adder

1. **Slow speed**: Delay grows linearly with n (O(n)).
2. **Not scalable**: Unsuitable for wide adders (32, 64 bits) in high-performance systems.
3. **Long critical path**: The carry chain is the critical path that limits the clock frequency.
4. **Poor performance in pipelined systems**: The long delay reduces throughput.

### 8. Comparison: RCA vs Other Adders

| Parameter        | Ripple Carry Adder | Carry Look-Ahead Adder |
|------------------|--------------------|------------------------|
| Speed            | O(n)               | O(log n)               |
| Gate count       | O(n)               | O(n log n)             |
| Power consumption| Low                | Moderate-High          |
| Design complexity| Simple             | Complex                |
| Area             | Small              | Large                  |

---

## Practice Problems

1. **Delay calculation**: A 16-bit ripple carry adder uses full adders with t_FA = 0.5 ns each. What is the total addition time?
<details>
<summary>Show Answer</summary>
t = 16 x 0.5 = 8 ns.
</details>

2. **Truth table**: Draw the truth table for a full adder and derive the expression for carry-out using K-map.
<details>
<summary>Show Answer</summary>
Co = AB + ACi + BCi. (Derived from grouping minterms: Co = 1 for rows 3,5,6,7 of the truth table).
</details>

3. **4-bit addition**: Show the ripple carry propagation for A = 1010, B = 0110, Cin = 0. Track each C1, C2, C3.
<details>
<summary>Show Answer</summary>
     FA0: 0+0+0, S0=0, C1=0
     FA1: 1+1+0, S1=0, C2=1
     FA2: 0+1+1, S2=0, C3=1
     FA3: 1+0+1, S3=0, C4=1
     Result: 10000 (16). Check: 10 + 6 = 16. Correct.
</details>

4. **Critical path**: Explain why the critical path of an RCA goes through the carry chain and not through the sum generation.
<details>
<summary>Show Answer</summary>
The sum at each stage depends on the carry from the previous stage. While the XOR for A XOR B can be computed in parallel in all stages, the actual sum S = (A XOR B) XOR Ci must wait for Ci, which depends on all lower-order stages. Thus the carry chain is the critical path.
</details>

5. **Scaling**: If a 4-bit RCA takes 2 ns, how long would a 64-bit RCA take (assuming same FA delay)?
<details>
<summary>Show Answer</summary>
4-bit takes 2 ns => t_FA = 2/4 = 0.5 ns. 64-bit: 64 x 0.5 = 32 ns.
</details>