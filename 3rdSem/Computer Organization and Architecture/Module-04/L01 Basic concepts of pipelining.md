# Basic concepts of pipelining

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 1  
**Date:** 08-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## What is Pipelining?

Pipelining is a technique where multiple instructions are overlapped in execution. The execution of an instruction is broken into several stages, and each stage processes a different instruction concurrently. This does NOT reduce the execution time of a single instruction, but it increases the throughput (number of instructions completed per unit time).

### The Laundry Analogy

Consider doing laundry for four loads of clothes. Without pipelining:
- Step 1: Wash Load A (30 min) -- machine idle
- Step 2: Dry Load A (40 min) -- machine idle
- Step 3: Fold Load A (20 min) -- you idle
- Step 4: Wash Load B (30 min) -- repeat...

Total time for 4 loads without pipelining: 4 x (30 + 40 + 20) = 4 x 90 = 360 minutes.

With pipelining (assembly line):
- Minute 0-30: Wash Load A
- Minute 30-70: Dry Load A, simultaneously Wash Load B
- Minute 70-90: Fold Load A, simultaneously Dry Load B, simultaneously Wash Load C
- Minute 90-110: Fold Load B, simultaneously Dry Load C, simultaneously Wash Load D
- Minute 110-130: Fold Load C, simultaneously Dry Load D
- Minute 130-150: Fold Load D

Total time for 4 loads with pipelining: 150 minutes (instead of 360).

The non-pipelined approach took 360 minutes; the pipelined approach took 150 minutes. After the pipeline is full (at minute 90), a new load finishes every 40 minutes (the longest stage).

## 5-Stage RISC Pipeline

A classic RISC pipeline divides instruction execution into 5 stages:

```
+---------+        +---------+        +---------+        +---------+        +---------+
|   IF    | -----> |   ID    | -----> |   EX    | -----> |   MEM   | -----> |   WB    |
+---------+        +---------+        +---------+        +---------+        +---------+
```

1. **IF (Instruction Fetch)**: Fetch the instruction from memory using the Program Counter (PC). Increment PC to point to the next instruction.

2. **ID (Instruction Decode)**: Decode the instruction to determine the operation and operand locations. Read register values from the register file. Sign-extend immediate values.

3. **EX (Execute)**: Perform the ALU operation (add, subtract, AND, OR, etc.). Compute effective addresses for memory loads/stores. Evaluate branch conditions.

4. **MEM (Memory Access)**: Access data memory for load (read) and store (write) instructions. For ALU instructions, this stage is a pass-through (no operation).

5. **WB (Write Back)**: Write the result (from ALU or memory load) back into the register file.

### Pipeline Diagram

Consider 5 instructions I1, I2, I3, I4, I5. The following ASCII table shows their flow through the pipeline:

```
Clock Cycle:   1    2    3    4    5    6    7    8    9
             +----+----+----+----+----+----+----+----+----+
    I1       | IF | ID | EX | MEM| WB |    |    |    |    |
             +----+----+----+----+----+----+----+----+----+
    I2       |    | IF | ID | EX | MEM| WB |    |    |    |
             +----+----+----+----+----+----+----+----+----+
    I3       |    |    | IF | ID | EX | MEM| WB |    |    |
             +----+----+----+----+----+----+----+----+----+
    I4       |    |    |    | IF | ID | EX | MEM| WB |    |
             +----+----+----+----+----+----+----+----+----+
    I5       |    |    |    |    | IF | ID | EX | MEM| WB |
             +----+----+----+----+----+----+----+----+----+
```

Key observation: After cycle 5, the pipeline is full -- execution of one instruction completes every cycle.

## Speedup Formula

**Ideal Speedup**: In an ideal pipeline with k stages, the speedup over a non-pipelined processor is k.

Let:
- k = number of pipeline stages
- n = number of instructions to execute
- t = time per stage (assuming each stage takes 1 clock cycle)

**Non-pipelined execution time (T_np)**: T_np = n x k x t
(Each instruction takes k cycles to complete, and instructions execute sequentially.)

**Pipelined execution time (T_p)**: T_p = (k + n - 1) x t
(The first instruction takes k cycles; subsequent instructions complete every cycle.)

**Speedup (S)**:
```
S = T_np / T_p = (n x k x t) / ((k + n - 1) x t)
S = (n x k) / (k + n - 1)
```

For large n (n >> k):
```
S ~ (n x k) / n = k
```

Thus, ideal speedup approximates the number of pipeline stages k.

### Example

For k = 5 stages and n = 1000 instructions:
```
S = (1000 x 5) / (5 + 1000 - 1) = 5000 / 1004 = 4.98
```
Close to the ideal speedup of 5.

## Pipeline Throughput

**Throughput** is the number of instructions completed per unit time.

- Non-pipelined throughput: 1 instruction per k cycles.
- Pipelined throughput (steady state): 1 instruction per cycle.

In the steady state (pipeline full), one instruction completes every clock cycle.

**Throughput formula**:
```
Throughput = n / T_p = n / ((k + n - 1) x t)
```

For large n: Throughput ~ 1/t (one instruction per cycle).

### Example

A 5-stage pipeline runs at 1 GHz (t = 1 ns). For 1000 instructions:
- T_p = (5 + 1000 - 1) x 1 ns = 1004 ns
- Throughput = 1000 / 1004 ns = 0.996 instructions/ns = 996 million instructions/sec (MIPS)

Non-pipelined throughput at same clock rate:
- T_np = 1000 x 5 ns = 5000 ns
- Throughput = 1000 / 5000 ns = 0.2 instructions/ns = 200 MIPS

**Speedup in throughput**: 996 / 200 = 4.98 (same as before).

---

## Practice Problems

**Problem 1**: A 6-stage pipeline executes 500 instructions. Each stage takes 2 ns. Calculate the total execution time, speedup, and throughput.

**Answer**:
- T_np = 500 x 6 x 2 = 6000 ns
- T_p = (6 + 500 - 1) x 2 = 505 x 2 = 1010 ns
- S = 6000 / 1010 = 5.94
- Throughput = 500 / 1010 ns = 495 MIPS

**Problem 2**: If a non-pipelined processor takes 12 ns per instruction and a pipelined version (5 stages) at the same clock rate achieves 0.9 instructions/ns, find speedup.

**Answer**:
- Non-pipelined throughput = 1/12 = 0.0833 instr/ns
- Pipelined throughput = 0.9 instr/ns
- S = 0.9 / 0.0833 = 10.8

**Problem 3**: A 4-stage pipeline has 1 ns per stage. How many instructions are needed to achieve at least 95% of ideal speedup?

**Answer**:
- S = (n x 4) / (4 + n - 1) >= 0.95 x 4
- 4n / (n + 3) >= 3.8
- 4n >= 3.8n + 11.4
- 0.2n >= 11.4
- n >= 57 instructions

**Problem 4**: What happens to speedup if pipeline stages are unequal in duration?

**Answer**: The clock cycle must be set to the longest stage time. If stages are unbalanced, the pipeline is only as fast as the slowest stage. The ideal speedup is reduced because the clock period is longer than the average stage time.

**Problem 5**: Explain why pipelining does not reduce latency of a single instruction.

**Answer**: A single instruction still goes through all k stages, taking the same total time (k cycles). Pipelining overlaps multiple instructions, improving throughput, but the latency from start to completion of any single instruction remains k cycles.
