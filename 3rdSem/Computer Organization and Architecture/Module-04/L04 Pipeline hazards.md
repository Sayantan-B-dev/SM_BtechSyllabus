# Pipeline hazards

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 4  
**Date:** 16-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Solutions to Pipeline Hazards

This lecture covers practical solutions to the three types of pipeline hazards introduced in Lecture 3.

## Solution to Structural Hazards

### Primary Solution: Separate Hardware Resources

The most effective solution is to duplicate or partition the conflicting resource.

**Problem**: Single memory for instructions (IF) and data (MEM) causes structural hazards.

**Solution**: Use separate instruction cache (I-cache) and data cache (D-cache), known as the **Harvard architecture** at the cache level.

```
+--------+    +-----------+    +--------+
| I-Cache|--->| Processor |--->| D-Cache|
+--------+    +-----------+    +--------+
    |                              |
    +--------+          +----------+
    | Unified Memory Bus           |
    +------------------------------+
```

- **IF stage** reads from I-cache exclusively.
- **MEM stage** reads/writes D-cache exclusively.
- No structural conflict for memory access.

Similarly, structural hazards in the register file (IF reads, WB writes) are solved by:
- **Dual-port register file**: Allows simultaneous read and write.
- **Write in first half of cycle, read in second half**: Time-multiplexing the single port.

### Secondary Solution: Stall (Insert Bubble)

If hardware duplication is not possible, stall one of the conflicting instructions.

```
Structural hazard stall:
Cycle:    1    2    3    4    5    6
I1(MEM):   [ IF][ ID][ EX][ MEM][ WB]
I4(IF):        [ IF][ ID][STALL][STALL][ IF][ ID]
```

## Solutions to Data Hazards

### Solution 1: Forwarding (Bypassing)

**Forwarding** (also called **bypassing**) adds hardware paths that feed the ALU output directly back to the ALU input, bypassing the register file. This eliminates many RAW hazards without stalling.

**Forwarding paths in a 5-stage pipeline**:

```
                         +-----------+
IF ---> ID ---> EX ---->|  ALU out  |---> MEM ---> WB
                  ^       |           |
                  |       +-----------+
                  |           |
                  +-----------+
                 Forwarding MUX
                      |
                  +--------+
                  | EX/MEM |<--- pipeline register
                  +--------+
                      |
                  +--------+
                  | MEM/WB |<--- pipeline register
                  +--------+
```

**How forwarding works**:

The forwarding unit monitors:
- Destination registers of instructions in EX, MEM, and WB stages.
- Source registers of the instruction currently in the EX stage.

If the destination register of an instruction in EX matches a source register of the instruction currently in EX, the ALU result from the earlier instruction is forwarded directly.

**Example without forwarding** (2 stalls needed):
```
I1: ADD R1, R2, R3    ; R1 = R2 + R3 (result in WB, cycle 5)
I2: SUB R4, R1, R5    ; R4 = R1 - R5 (needs R1 in EX, cycle 3)
```

**Pipeline with forwarding**:
```
Cycle:      1      2      3      4      5      6
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I2:           [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
                              ^
                          Forward path:
                          ALU output of I1 (EX) --> ALU input of I2 (EX)
                          No stall needed!
```

The forwarding unit detects that I1's destination (R1) matches I2's source (R1) and routes I1's ALU result directly to I2's ALU input via a multiplexer.

**Load-Use Hazard** -- Special Case:

When an instruction loads a value from memory (LW) and the next instruction immediately uses it, the result is not available until MEM stage. Even with forwarding, one stall cycle is needed:

```
I1: LW R1, 0(R2)      ; R1 = Mem[R2], result ready after MEM (cycle 4)
I2: ADD R3, R1, R4    ; needs R1 in EX (cycle 3)
```

```
Cycle:      1      2      3      4      5      6
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I2:           [ IF ] [ ID ] [STALL][ EX ] [ MEM] [ WB ]
                              ^
                         Forward from MEM (cycle 4) to EX (cycle 4)
                         1 bubble needed (load-use penalty = 1)
```

The "load-use" or "load" hazard requires a 1-cycle stall because the loaded data is only available at the end of MEM, but EX needs it at the start of the cycle. The forwarding path from MEM output to EX input handles this with a single stall.

### Solution 2: Pipeline Interlock and Stall

When forwarding cannot resolve a hazard (e.g., load-use without forwarding, or complex dependencies), the pipeline **interlock** hardware stalls the pipeline.

```
+-------------------+
| Hazard Detection  |
| Unit              |
|                   |
| Inputs:           |
| - IF/ID registers |
| - ID/EX registers |
| - EX/MEM registers|
| - MEM/WB registers|
+-------------------+
         |
         v
+-------------------+
| Control Signals   |
|                   |
| - PC Write Enable |---- (freeze PC)
| - IF/ID Write En  |---- (freeze IF/ID)
| - ID/EX Clear     |---- (insert bubble in EX)
+-------------------+
```

**Stall insertion steps**:
1. Hazard detection unit detects a RAW hazard that cannot be forwarded.
2. PC write enable = 0 (PC does not change; same instruction fetched again next cycle).
3. IF/ID write enable = 0 (current instruction in ID stays there).
4. ID/EX control bits = 0 (NOP/bubble inserted into EX stage).

### Solution 3: Compiler-Based Solutions

The compiler can restructure code to minimize hazards.

**Instruction Reordering**:

The compiler rearranges independent instructions between a load and its use to fill the load-use delay slot.

**Before reordering** (load-use stall):
```
LW   R1, 0(R2)       ; load R1
NOP                  ; compiler-inserted NOP (or stall)
ADD  R3, R1, R4      ; use R1
```

**After reordering** (no stall):
```
LW   R1, 0(R2)       ; load R1
OR   R5, R6, R7      ; independent instruction fills gap
ADD  R3, R1, R4      ; use R1 (no stall needed)
```

**NOP Insertion**: If no independent instruction exists, the compiler inserts explicit NOP instructions.

**Code Scheduling** (for branches):

The compiler moves an instruction from BEFORE or AFTER the branch into the **branch delay slot** (the instruction slot immediately after a branch, which always executes regardless of branch outcome).

**Before scheduling**:
```
BEQ  R1, R2, target   ; branch
ADD  R3, R4, R5       ; may be flushed if branch taken
target: ...
```

**After filling delay slot** (if safe):
```
ADD  R3, R4, R5       ; moved before branch (always executes)
BEQ  R1, R2, target   ; branch
target: ...
```

## Solutions to Control Hazards

### Solution 1: Branch Prediction

**Static prediction**: Always predict taken or always predict not-taken.
- "Predict not-taken" is common: fetch continues sequentially. If branch is taken, flush wrong-path instructions.
- Simpler and less hardware.

**Dynamic prediction**: Use branch history table (BHT) to record past behavior.
- 1-bit predictor: Remember last outcome (taken/not-taken). Predict same next time.
- 2-bit saturating counter: More accurate. Four states: strongly not-taken, weakly not-taken, weakly taken, strongly taken.

### Solution 2: Branch Target Buffer (BTB)

Cache that stores the target address of previously executed branches. On a branch instruction, the BTB provides the predicted target address in the IF stage itself, reducing the penalty to zero if predicted correctly.

### Solution 3: Delayed Branching

Used in some RISC architectures (e.g., MIPS). The instruction slot after a branch (delay slot) is always executed. The compiler fills it with a useful instruction that does not depend on the branch.

## Code Example: Forwarding Illustrated

Consider the following sequence of instructions and show how forwarding resolves hazards:

```
I1: ADD R1, R2, R3    ; R1 = R2 + R3
I2: SUB R4, R1, R5    ; R4 = R1 - R5  (RAW on R1)
I3: OR  R6, R1, R7    ; R6 = R1 OR R7 (RAW on R1)
I4: AND R8, R9, R10   ; R8 = R9 AND R10 (no dependency)
```

**Pipeline diagram with forwarding**:

```
Cycle:      1       2       3       4       5       6       7
I1:      [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I2:           [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I3:                [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
I4:                     [ IF ] [ ID ] [ EX ] [ MEM] [ WB ]
```

**Forwarding actions**:
- Cycle 3: I1 is in EX (computing R1). I2 is in ID (needs R1). Forwarding from EX output of I1 to EX input of I2.
- Cycle 4: I2 is in EX. I3 is in ID (needs R1). Forwarding from EX/MEM pipeline register (which holds I1's result) to EX input of I3. Alternatively, if I1's result passes to MEM, forwarding from MEM/WB or MEM output.
- Cycle 4: I4 has no dependencies, proceeds normally.

**Result**: Zero stalls for the entire sequence, despite three RAW dependencies.

---

## Practice Problems

**Problem 1**: Consider the code sequence:
```
LW R1, 0(R2)
SW R1, 0(R3)
```
How many stalls are needed with full forwarding?

**Answer**: LW loads R1, available after MEM (cycle 4). SW uses R1 for data in MEM stage. SW reads register in ID (cycle 3), but the data is needed in MEM (cycle 4). With forwarding from MEM output to MEM data write port: zero stalls. The value is forwarded directly from LW's MEM stage to SW's MEM stage.

**Problem 2**: The following code has no independent instructions between a load and its use. How many cycles does it take to execute 3 instructions with full forwarding?
```
LW R1, 0(R2)
ADD R3, R1, R4
SUB R5, R3, R6
```

**Answer**:
- LW -> ADD: load-use hazard, 1 stall.
- ADD -> SUB: ALU-ALU forwarding, 0 stalls.
- Total cycles: (1+1+1) + (stall) = 5 cycles for 3 instructions. CPI = 5/3 = 1.67.

**Problem 3**: Show the pipeline diagram with forwarding for:
```
I1: ADD R1, R2, R3
I2: SW R1, 0(R4)
```

**Answer**: SW uses R1 as store data in MEM stage, which occurs at cycle 4. I1 produces R1 in EX (cycle 3). Forwarding from I1's EX output to SW's MEM stage works with 0 stalls.
```
Cycle:     1    2    3    4    5
I1:     [ IF][ ID][ EX][MEM][WB]
I2:        [ IF][ ID][ EX][MEM]
```

**Problem 4**: What is the difference between a pipeline interlock and forwarding?

**Answer**: Forwarding adds additional data paths to route results directly to dependent instructions without using the register file. An interlock detects hazards that cannot be forwarded and stalls the pipeline by freezing the earlier stages and inserting bubbles. They work together: forwarding resolves most ALU hazards, interlock handles the remaining cases (e.g., load-use, complex structural conflicts).

**Problem 5**: A compiler schedules 200 instructions such that 10 load-use hazards remain, each requiring 1 stall. The rest are handled by forwarding. What is the total execution time on a 5-stage pipeline at 2 GHz?

**Answer**:
- Base cycles = 5 + 200 - 1 = 204 cycles (ideal)
- Stall cycles = 10 x 1 = 10
- Total cycles = 214
- Cycle time = 1/2 GHz = 0.5 ns
- Total time = 214 x 0.5 = 107 ns
