# Throughput and speedup

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 2  
**Date:** 09-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Throughput Definition

**Throughput** is the number of instructions completed per unit of time. It measures the work done by the processor.

```
Throughput = Number of Instructions Completed / Total Execution Time
```

Common units:
- MIPS (Millions of Instructions Per Second)
- MFLOPS (Millions of Floating-Point Operations Per Second)
- Instructions per cycle (IPC)

### Non-Pipelined Throughput

In a non-pipelined processor, each instruction takes k clock cycles to complete, where k is the number of stages (or the total cycles per instruction). Instructions execute sequentially -- one must finish before the next begins.

```
Throughput_np = 1 instruction / k cycles
```

If the clock frequency is f Hz (cycle time = 1/f seconds):
```
Throughput_np = f / k instructions per second
```

### Pipelined Throughput

In a pipelined processor, once the pipeline is full (after the first k-1 cycles), one instruction completes every clock cycle.

```
Throughput_p = 1 instruction / 1 cycle (in steady state)
Throughput_p = f instructions per second (ideal, ignoring hazards)
```

## Speedup Definition

**Speedup** is the ratio of execution time on a non-pipelined processor to execution time on a pipelined processor.

```
Speedup = Time(non-pipelined) / Time(pipelined)
```

Or equivalently:
```
Speedup = Throughput(pipelined) / Throughput(non-pipelined)
```

### Ideal Speedup

For a k-stage pipeline executing n instructions:

- Non-pipelined time: T_np = n x k x t (where t is the cycle time)
- Pipelined time: T_p = (k + n - 1) x t

```
S_ideal = T_np / T_p = (n x k x t) / ((k + n - 1) x t) = (n x k) / (k + n - 1)
```

For a very large number of instructions (n -> infinity):
```
S_ideal = k
```

**Ideal speedup equals the number of pipeline stages k.**

## Actual vs Ideal Speedup

In real processors, speedup is less than ideal due to:

1. **Pipeline hazards**: Structural, data, and control hazards cause stalls.
2. **Unequal stage durations**: The clock cycle is limited by the slowest stage.
3. **Pipeline fill/drain overhead**: Not all cycles achieve steady-state throughput.
4. **Added pipeline registers**: Each stage adds register delay (setup + propagation).

The actual speedup can be expressed as:
```
S_actual = k / (1 + Stall_cycles_per_instruction)
```

## CPI in Pipelined vs Non-Pipelined Processors

**CPI (Cycles Per Instruction)** is the average number of clock cycles per instruction.

### Non-Pipelined Processor
Each instruction takes exactly k cycles.
```
CPI_np = k
```

### Pipelined Processor (Ideal, No Hazards)
In the steady state, one instruction completes each cycle.
```
CPI_p = 1 (ideal)
```

### Pipelined Processor (With Hazards)
Stalls increase the average CPI.
```
CPI_p = 1 + Average_stall_cycles_per_instruction
```

**Throughput in terms of CPI**:
```
Throughput = f / CPI
```

### Important Relationship
```
Speedup = CPI_np / CPI_p = k / (1 + Stalls_per_instr)
```

## Worked Numerical Example

Consider a 5-stage pipeline (k = 5) running at 2 GHz (cycle time = 0.5 ns). Execute N = 200 instructions.

### Case A: Non-pipelined

```
CPI_np = 5
T_np = N x CPI_np x cycle_time = 200 x 5 x 0.5 ns = 500 ns
Throughput_np = 200 / 500 ns = 0.4 instructions/ns = 400 MIPS
```

### Case B: Pipelined, No Hazards

```
CPI_p = 1
T_p = (k + N - 1) x cycle_time = (5 + 200 - 1) x 0.5 ns = 204 x 0.5 = 102 ns
Throughput_p = 200 / 102 ns = 1.96 instructions/ns = 1960 MIPS
Speedup = 500 / 102 = 4.90 (ideal = 5)
```

### Case C: Pipelined, With Hazards (20% of instructions cause 2-cycle stalls)

```
Average stall cycles = 0.20 x 2 = 0.4
CPI_p = 1 + 0.4 = 1.4
T_p = (k - 1 + N x CPI_p) x cycle_time = (4 + 200 x 1.4) x 0.5 ns = (4 + 280) x 0.5 = 142 ns
Throughput_p = 200 / 142 ns = 1.41 instructions/ns = 1410 MIPS
Speedup = 500 / 142 = 3.52 (reduced from 4.90)
```

## Detailed Speedup Derivation

Let's derive the speedup formula step by step.

**Given**:
- Non-pipelined: Each instruction takes k cycles. Total cycles for N instructions = N x k.
- Pipelined: First instruction takes k cycles. Remaining (N-1) instructions each add 1 cycle. Total cycles = k + (N-1).

Add stall cycles s (average stalls per instruction, includes all hazard penalties):
```
Total_pipeline_cycles = k + (N-1) + s x N
```

**Speedup**:
```
S = (N x k) / (k + N - 1 + s x N)
```

For large N (N >> k):
```
S = (N x k) / (N + s x N) = k / (1 + s)
```

This confirms that stalls directly reduce speedup.

## Graphical Interpretation

```
Non-pipelined:
Instr 1: [  Stage 1  ][  Stage 2  ][  Stage 3  ][  Stage 4  ][  Stage 5  ]
Instr 2:              [  Stage 1  ][  Stage 2  ][  Stage 3  ][  Stage 4  ][  Stage 5  ]
Time:    |---k cycles---||---k cycles---|

Pipelined (ideal):
Instr 1: [  Stage 1  ][  Stage 2  ][  Stage 3  ][  Stage 4  ][  Stage 5  ]
Instr 2:              [  Stage 1  ][  Stage 2  ][  Stage 3  ][  Stage 4  ][  Stage 5  ]
Instr 3:                           [  Stage 1  ][  Stage 2  ][  Stage 3  ][  Stage 4  ][  Stage 5  ]
Time:    |---(k+N-1) cycles---|
```

The shaded region shows the overlap of instructions, which is the source of speedup.

---

## Practice Problems

**Problem 1**: A 4-stage pipeline (k=4) runs at 1.5 GHz. Execute 1000 instructions with an average of 0.3 stall cycles per instruction. Find execution time, throughput, and speedup.

<details>
<summary>Show Answer</summary>
- Cycle time = 1 / 1.5 GHz = 0.667 ns
- CPI_p = 1 + 0.3 = 1.3
- T_p = (k - 1 + N x CPI_p) x t = (3 + 1000 x 1.3) x 0.667 = (3 + 1300) x 0.667 = 869.4 ns
- Throughput = 1000 / 869.4 ns = 1.15 instr/ns = 1150 MIPS
- Non-pipelined: T_np = N x k x t = 1000 x 4 x 0.667 = 2668 ns
- S = 2668 / 869.4 = 3.07
</details>

**Problem 2**: A 6-stage pipeline achieves speedup of 4.5 for a large program. What is the average number of stall cycles per instruction?

<details>
<summary>Show Answer</summary>
- S = k / (1 + s) => 4.5 = 6 / (1 + s) => 1 + s = 6 / 4.5 = 1.333 => s = 0.333 stalls per instruction
</details>

**Problem 3**: Compare the throughput of a 5-stage pipeline at 3 GHz with a non-pipelined processor at 5 GHz (same technology). Which is faster?

<details>
<summary>Show Answer</summary>
- Pipelined: Throughput = 3 G instructions/sec = 3000 MIPS (ideal, no hazards)
- Non-pipelined: Throughput = 5 GHz / 5 = 1 G instructions/sec = 1000 MIPS
- The pipelined processor (3 GHz) is 3x faster even at a lower clock frequency.
</details>

**Problem 4**: For a 5-stage pipeline, what percentage of maximum throughput is achieved when executing 50 instructions?

<details>
<summary>Show Answer</summary>
- Maximum throughput = f (one instruction per cycle)
- Actual throughput = N / (k + N - 1) x f = 50 / (5 + 50 - 1) x f = 50/54 x f = 0.926f
- Percentage = 92.6%
</details>

**Problem 5**: If a pipeline has 8 stages but stalls add 0.5 cycles/instruction on average, what is the speedup? How does this compare to a 4-stage pipeline with 0.1 stalls/instruction?

<details>
<summary>Show Answer</summary>
- 8-stage: S = 8 / (1 + 0.5) = 8 / 1.5 = 5.33
- 4-stage: S = 4 / (1 + 0.1) = 4 / 1.1 = 3.64
- The 8-stage pipeline is still faster (5.33 > 3.64), despite more stalls, because more stages give higher potential speedup.
</details>