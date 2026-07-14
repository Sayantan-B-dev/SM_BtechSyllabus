# Pipeline hazards

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 3  
**Date:** 09-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## What is a Pipeline Hazard?

A **pipeline hazard** is a situation that prevents the next instruction in the pipeline from executing during its designated clock cycle. Hazards reduce the ideal speedup achieved by pipelining. When a hazard occurs, the pipeline must be **stalled** (insert bubbles) to maintain correct execution.

There are three types of hazards:
1. **Structural hazards**: Hardware resource conflicts.
2. **Data hazards**: Dependencies between instructions that access the same data.
3. **Control hazards**: Branches and jumps that change the program flow.

## 1. Structural Hazards

A **structural hazard** occurs when two or more instructions in the pipeline require the same hardware resource at the same time.

### Example: Single Memory for Instructions and Data

Consider a 5-stage pipeline where there is only ONE memory unit for both instruction fetch (IF) and data memory access (MEM).

```
Clock Cycle:   1    2    3    4    5
             +----+----+----+----+----+
    I1 (load):| IF | ID | EX | MEM| WB |
             +----+----+----+----+----+
    I2:       |    | IF | ID | EX | MEM|
             +----+----+----+----+----+
    I3:       |    |    | IF | ID | EX |
             +----+----+----+----+----+
    I4:       |    |    |    | IF | ID |
             +----+----+----+----+----+
```

In cycle 4:
- I1 wants to use MEM (load data from memory).
- I4 wants to use IF (fetch instruction from memory).

Both need the same memory port. Conflict! The pipeline must stall I4 until I1 finishes MEM.

```
Cycle 4 (with stall): MEM for I1 executes; IF for I4 stalls (bubble inserted).
```

### Other Examples of Structural Hazards

- Single-port register file: IF stage reads registers, WB stage writes registers -- conflicts if both need access simultaneously.
- Single ALU: EX stage uses ALU, but some pipelines might need ALU for address calculation in MEM -- rare in typical designs.
- Shared cache bus: When multiple pipeline stages need the cache at the same time.

### Solutions to Structural Hazards

- **Separate hardware**: Separate instruction cache (I-cache) and data cache (D-cache).
- **Multiple ports**: Multi-port register files or memories.
- **Pipeline stall**: Insert bubbles when the conflict cannot be avoided.

## 2. Data Hazards

A **data hazard** occurs when an instruction depends on the result of a previous instruction that has not yet completed. This is the most common type of hazard.

### Three Types of Data Dependencies

**RAW (Read After Write) -- True Dependency**:
An instruction reads a register that a previous instruction writes to.

```
I1: ADD R1, R2, R3   ; R1 = R2 + R3
I2: SUB R4, R1, R5   ; R4 = R1 - R5  (needs R1 from I1)
```

I2 must wait until I1 writes R1 in WB stage. If I2 reads R1 in ID stage before I1 writes it, I2 gets the old value.

**WAR (Write After Read) -- Anti-Dependency**:
An instruction writes to a register that a later instruction reads.

```
I1: ADD R1, R2, R3   ; R1 = R2 + R3  (reads R2)
I2: SUB R2, R4, R5   ; R2 = R4 - R5  (writes R2 before I1 reads it?)
```

In a simple 5-stage pipeline, I1 reads R2 in ID (cycle 2), and I2 writes R2 in WB (cycle 5). Since I1 reads R2 at cycle 2 and I2 writes at cycle 5, there is no actual conflict in this pipeline. WAR hazards are uncommon in simple in-order pipelines.

**WAW (Write After Write) -- Output Dependency**:
Two instructions write to the same register.

```
I1: ADD R1, R2, R3   ; R1 = R2 + R3
I2: SUB R1, R4, R5   ; R1 = R4 - R5 (writes same register later)
```

The final value of R1 should come from I1 (then I2). If I2 completes WB before I1 due to some out-of-order execution, the wrong value persists. In simple in-order pipelines, WAW does not occur because instructions complete in order.

### RAW Hazard Example -- Detailed

```
I1: LW R1, 0(R2)     ; R1 = Memory[R2]   (load word)
I2: ADD R3, R1, R4   ; R3 = R1 + R4      (uses R1)
```

**Pipeline execution without hazard handling**:

```
Cycle:      1       2       3       4       5       6
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]   |
I2:           [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
                      ^
                      |
                   I2 reads R1 in ID (cycle 3)
                   I1 writes R1 in WB (cycle 5)
                   I2 gets stale value!
```

I2 reads R1 in cycle 3 (ID stage), but I1 does not write R1 until cycle 5 (WB stage). This gives I2 the wrong (old) value of R1.

**Solution -- Pipeline Interlock**: Hardware detects the hazard and stalls I2 for 2 cycles (inserts bubbles):

```
Cycle:      1       2       3       4       5       6       7       8
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I2:           [ IF ] [ ID ] [STALL][STALL][ ID ] [ EX ] [ MEM] [ WB ]
                                      (R1 available now)
```

I2 is stalled at ID (kept in ID stage) for 2 cycles until I1 writes R1. Two bubbles (NOPs) are inserted in EX and MEM.

## 3. Control Hazards

A **control hazard** (also called **branch hazard**) occurs when the pipeline makes decisions based on the outcome of a branch instruction, but the outcome is not known until later stages.

### Example: Conditional Branch

```
I1: BEQ R1, R2, target   ; branch if R1 == R2
I2: ADD R3, R4, R5       ; next sequential instruction (may be wrong!)
I3: SUB R6, R7, R8
...
target: XOR R9, R10, R11  ; branch target
```

**Problem**: The next instruction to fetch after I1 depends on whether the branch is taken. The branch condition is evaluated in EX stage (or MEM), but by then, I2 and I3 are already fetched and partially executed.

```
Cycle:      1       2       3       4       5
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I2:           [ IF ] [ ID ] [ EX ]  (wrong! if branch taken)
I3:                [ IF ] [ ID ]   (wrong! if branch taken)
                          ^
                     Branch evaluated here (cycle 3)
```

If the branch is taken, I2 and I3 should not execute. Their results must be discarded (flushed).

### Pipeline Flushing

When the branch is resolved in EX (cycle 3), the pipeline flushes I2 and I3 from IF and ID:

```
Cycle:      1       2       3       4       5       6       7
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
Taken:   --------flush I2, I3---------
target:                  [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
```

The penalty is 2 cycles (the flushed instructions). The pipeline must fetch the correct instruction from the target address.

### Branch Penalty

- **Branch penalty**: Number of cycles lost due to a mispredicted or incorrectly fetched branch. In simple pipelines, this is typically 1-3 cycles.
- For k stages before branch resolution, penalty = k - 2 cycles (if resolved in EX, penalty = 2).

### Hazard Classification Summary Table

| Hazard Type | Cause | Example | Common Solution |
|---|---|---|---|
| Structural | Resource conflict | Single memory for IF and MEM | Separate I-cache/D-cache |
| Data (RAW) | True dependency | LW followed by ADD | Forwarding, stalling |
| Data (WAR) | Anti-dependency | ADD reads R1, later SUB writes R1 | Register renaming |
| Data (WAW) | Output dependency | Two writes to same register | In-order completion |
| Control | Branch/jump | BEQ changes program flow | Branch prediction, flushing |

## The Pipeline Interlock

A **pipeline interlock** is a hardware mechanism that detects hazards and stalls the pipeline until the hazard is resolved.

### How an Interlock Works

1. **Hazard detection unit**: Monitors source registers of instructions in ID and destination registers of instructions in later stages.
2. **Comparison logic**: Checks if the destination register of an instruction in EX, MEM, or WB matches a source register of the instruction in ID.
3. **Stall generation**: If a match is found, the interlock asserts a stall signal.
4. **Pipeline freeze**: The PC is frozen (no new fetch), and the ID stage is frozen (re-read the same instruction next cycle). A bubble (NOP) is inserted into the EX stage.

The interlock inserts **bubbles** (also called pipeline stalls or NOPs) into the pipeline. A bubble represents a clock cycle where no useful work is done in that stage.

---

## Practice Problems

**Problem 1**: Identify the hazard type in this code sequence:
```
I1: LW R2, 100(R3)
I2: OR R1, R2, R2
I3: SW R2, 200(R3)
```

<details>
<summary>Show Answer</summary>
RAW hazard between I1 (write R2) and I2 (read R2). Also RAW between I1 and I3 (read R2 for store address).
</details>

**Problem 2**: In a 5-stage pipeline, how many stall cycles are needed for a RAW hazard between an ALU instruction and its dependent instruction?

<details>
<summary>Show Answer</summary>
Zero stalls if forwarding is implemented (result forwarded from EX of first to EX of second). Without forwarding, 2 stalls (the dependent instruction waits until the result is available in WB).
</details>

**Problem 3**: What is the branch penalty for a 5-stage pipeline where the branch condition is evaluated in MEM stage?

<details>
<summary>Show Answer</summary>
If branch resolves in MEM (cycle 4), three wrong-path instructions have been fetched (in cycles 2, 3, 4). Penalty = 3 cycles. Typically, branches resolve earlier (EX stage) to reduce penalty.
</details>

**Problem 4**: Show the pipeline diagram for:
```
I1: LW R1, 0(R2)
I2: ADD R3, R1, R4
```
Assume no forwarding, only interlock+stall.

<details>
<summary>Show Answer</summary>
```
Cycle:    1    2    3    4    5    6    7    8
I1:    [ IF][ ID][ EX][ MEM][ WB]
I2:        [ IF][ ID][STALL][STALL][ ID][ EX][ MEM][ WB]
```
</details>

**Problem 5**: Can a structural hazard cause a data hazard? Explain with an example.

<details>
<summary>Show Answer</summary>
Not directly, but they can compound. Example: if an I-cache miss stalls the IF stage, the later stages empty out. When IF resumes, the ID stage may get an instruction that reads a register that is also being updated by a long-latency instruction still in MEM. The interlock logic must handle both the control stall (cache miss) and the data hazard simultaneously.
</details>