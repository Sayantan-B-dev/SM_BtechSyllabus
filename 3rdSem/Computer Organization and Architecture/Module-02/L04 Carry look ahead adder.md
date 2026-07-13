# Carry look ahead adder

**Course:** Computer Organization and Architecture  
**Module:** 2 | **Lecture:** 4  
**Date:** 05-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Motivation

The ripple carry adder is slow because carry signals propagate sequentially through all n stages. The **carry look-ahead adder** (CLA) eliminates this sequential dependency by computing all carry signals in **parallel** using additional logic.

### 2. Generate and Propagate Signals

For a single-bit position i, define two signals:

- **Generate (Gi)**: A carry is **generated** at position i when both A and B are 1, regardless of the incoming carry.
  - Gi = Ai AND Bi

- **Propagate (Pi)**: A carry is **propagated** through position i when exactly one of A or B is 1 (or both, in some definitions). If Pi = 1, then Carry-out = Carry-in.
  - Pi = Ai XOR Bi

#### Truth Table for Gi and Pi

| Ai | Bi | Gi = Ai.Bi | Pi = Ai XOR Bi | Carry-out (Co)              |
|----|----|------------|----------------|-----------------------------|
| 0  | 0  | 0          | 0              | 0 (kill)                    |
| 0  | 1  | 0          | 1              | Ci (propagate)              |
| 1  | 0  | 0          | 1              | Ci (propagate)              |
| 1  | 1  | 1          | 0              | 1 (generate)                |

#### Carry-out Expression

Co_i = Gi OR (Pi AND Ci)

Where Ci is the carry-in to bit position i.

### 3. Carry Look-Ahead Logic

Let C0 be the initial carry-in (typically 0).

For a 4-bit adder:

- **C1 = G0 + P0*C0**
- **C2 = G1 + P1*C1 = G1 + P1*G0 + P1*P0*C0**
- **C3 = G2 + P2*C2 = G2 + P2*G1 + P2*P1*G0 + P2*P1*P0*C0**
- **C4 = G3 + P3*C3 = G3 + P3*G2 + P3*P2*G1 + P3*P2*P1*G0 + P3*P2*P1*P0*C0**

Each carry depends only on the initial carry C0 and the Gi, Pi signals, **not** on intermediate carries. All carries can be computed in parallel once Gi and Pi are available.

### 4. 4-bit Carry Look-Ahead Adder Circuit (ASCII)

```
A3 B3    A2 B2    A1 B1    A0 B0
 |  |     |  |     |  |     |  |
 v  v     v  v     v  v     v  v
+--+-+   +--+-+   +--+-+   +--+-+
| XOR |   | XOR |   | XOR |   | XOR |
| AND |   | AND |   | AND |   | AND |
+--+--+   +--+--+   +--+--+   +--+--+
   |          |          |          |
  P3 G3     P2 G2      P1 G1      P0 G0
   |          |          |          |
   +----------+----------+----------+
   |          |          |          |
   v          v          v          v
  +-----------------------------------+
  |    Carry Look-Ahead Logic         |
  |    (AND-OR network)               |
  +-----------------------------------+
   |    |    |    |
   v    v    v    v
   C4   C3   C2   C1
   |    |    |    |
   v    v    v    v
  +--+ +--+ +--+ +--+
  |XOR| |XOR| |XOR| |XOR|
  |   | |   | |   | |   |
  +---+ +---+ +---+ +---+
   |      |      |      |
   v      v      v      v
   S3     S2     S1     S0
```

Note that S_i = Pi XOR Ci.

### 5. Detailed Carry Computation Example

Compute carries for A = 1101 (13) and B = 0110 (6), C0 = 0.

Step 1: Compute Gi and Pi.

| i | Ai | Bi | Gi = Ai.Bi | Pi = Ai XOR Bi |
|---|---|----|------------|----------------|
| 0 | 1  | 0  | 0          | 1              |
| 1 | 0  | 1  | 0          | 1              |
| 2 | 1  | 1  | 1          | 0              |
| 3 | 1  | 0  | 0          | 1              |

Step 2: Compute carries in parallel.

C0 = 0

C1 = G0 + P0*C0 = 0 + 1*0 = 0

C2 = G1 + P1*G0 + P1*P0*C0 = 0 + 1*0 + 1*1*0 = 0

C3 = G2 + P2*G1 + P2*P1*G0 + P2*P1*P0*C0
   = 1 + 0*0 + 0*1*0 + 0*1*1*0 = 1

C4 = G3 + P3*G2 + P3*P2*G1 + P3*P2*P1*G0 + P3*P2*P1*P0*C0
   = 0 + 1*1 + 1*0*0 + 1*0*1*0 + 1*0*1*1*0 = 1

Step 3: Compute sums.

S0 = P0 XOR C0 = 1 XOR 0 = 1
S1 = P1 XOR C1 = 1 XOR 0 = 1
S2 = P2 XOR C2 = 0 XOR 0 = 0
S3 = P3 XOR C3 = 1 XOR 1 = 0

Result: C4 S3 S2 S1 S0 = 1 0 0 1 1 = 19. Check: 13 + 6 = 19. Correct.

### 6. Speed Comparison with Ripple Carry

#### Delay Calculation for CLA

The CLA has three stages of computation:
1. **Stage 1**: Compute Gi and Pi (1 gate delay, typically 1 unit).
2. **Stage 2**: Compute all carries using the look-ahead network (2 gate delays for AND-OR logic).
3. **Stage 3**: Compute sums using XOR of Pi and Ci (1 gate delay).

**Total** = 1 + 2 + 1 = 4 gate delays (constant, independent of n).

For a **ripple carry adder**: total delay = n * t_FA (e.g., for 4-bit, about 4 FA delays, each FA is ~2 gate delays, so ~8 gate delays).

| n (bits) | RCA delay (gate delays) | CLA delay (gate delays) |
|----------|------------------------|-------------------------|
| 4        | 8                      | 4                       |
| 8        | 16                     | 5-6                     |
| 16       | 32                     | 6-8                     |
| 32       | 64                     | 8-10                    |
| 64       | 128                    | 10-12                   |

Note: For CLA, as n increases beyond 4, multi-level (hierarchical) CLA is used, so delay grows as O(log n) instead of O(n).

### 7. Hierarchical (Block) Carry Look-Ahead

For wider adders (16, 32, 64 bits), a single-level CLA becomes impractical due to fan-in limitations on the AND-OR gates. Instead, a **hierarchical** approach is used:

1. Group bits into blocks (e.g., 4-bit blocks).
2. Each block produces:
   - **Block Generate (GG)**: G = G3 + P3*G2 + P3*P2*G1 + P3*P2*P1*G0
   - **Block Propagate (PP)**: P = P3 * P2 * P1 * P0
3. A second-level CLA computes carries between blocks.
4. This can be extended to multiple levels.

#### 16-bit Hierarchical CLA

```
                     +-----------------------------+
                     |  Second-Level Look-Ahead    |
                     +-----------------------------+
                    /        |        |        \
                   v         v        v         v
           +-------+  +-------+  +-------+  +-------+
           |CLA    |  |CLA    |  |CLA    |  |CLA    |
           |block 3|  |block 2|  |block 1|  |block 0|
           |(12-15)|  |(8-11) |  |(4-7)  |  |(0-3)  |
           +-------+  +-------+  +-------+  +-------+
```

Each CLA block computes 4-bit addition and outputs GG and PP to the second-level look-ahead.

### 8. Advantages of CLA

1. **Fast**: Carry computation time is O(log n) instead of O(n).
2. **Parallel computation**: All carries computed simultaneously.
3. **Scalable**: With hierarchical design, works for 64-bit and wider.
4. **Used in practice**: Modern processors use CLA-based designs (or variations like Kogge-Stone, Brent-Kung).

### 9. Disadvantages of CLA

1. **High gate count**: O(n log n) gates vs O(n) for RCA.
2. **High power consumption**: More gates means more switching activity.
3. **Fan-in limitations**: For wide adders, the AND-OR gates require many inputs, necessitating hierarchical design.
4. **Larger chip area**: More complex routing and logic.

---

## Practice Problems

1. **Carry expression**: Write the carry expression for C5 in a 5-bit CLA (bits 0-4).
   - **Answer**: C5 = G4 + P4*G3 + P4*P3*G2 + P4*P3*P2*G1 + P4*P3*P2*P1*G0 + P4*P3*P2*P1*P0*C0.

2. **CLA computation**: For A = 1010, B = 0101, C0 = 0, compute all G, P, and carries. Find the sum.
   - **Answer**: 
     G0=0,P0=1; G1=0,P1=1; G2=1,P2=0; G3=0,P3=1.
     C1=0, C2=0, C3=1, C4=0.
     S0=1, S1=1, S2=0, S3=1. Sum = 01111 = 15. Check: 10+5=15.

3. **Delay comparison**: A 32-bit RCA has t_FA = 300 ps. A 32-bit hierarchical CLA has 8 gate delays where each gate delay = 100 ps. Compare total delay.
   - **Answer**: RCA: 32 * 300 = 9600 ps = 9.6 ns. CLA: 8 * 100 = 800 ps = 0.8 ns. CLA is 12x faster.

4. **Block-level**: For a 4-bit CLA block, derive the block generate GG and block propagate PP expressions.
   - **Answer**: GG = G3 + P3*G2 + P3*P2*G1 + P3*P2*P1*G0. PP = P3 * P2 * P1 * P0.

5. **Hierarchical**: Show how a 16-bit CLA would be constructed using four 4-bit CLA blocks and a second-level look-ahead.
   - **Answer**: Four 4-bit CLA blocks compute GG[3:0] and PP[3:0]. A second-level CLA takes these four sets of GG, PP plus a block-level C0 to compute carry-in to each 4-bit block. Each block then uses the incoming carry to compute its internal carries and final sums.
