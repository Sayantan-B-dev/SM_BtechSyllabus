# Instruction execution cycle

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 5  
**Date:** 15-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to the Instruction Cycle

The **instruction cycle** (also called the **fetch-execute cycle** or **machine cycle**) is the basic operation cycle of a CPU. Each instruction in a program goes through a sequence of phases from the time it is fetched from memory to the time its execution is complete.

**The four main phases of the instruction cycle:**

1. **Fetch Cycle**: Read the next instruction from memory into the CPU.
2. **Decode Cycle**: Interpret the instruction (determine opcode and operands).
3. **Execute Cycle**: Perform the operation specified by the instruction.
4. **Interrupt Cycle** (if enabled and pending): Handle any interrupt requests.

Some architectures combine the decode phase with either fetch or execute, but conceptually all four phases exist.

### 2. The Complete Instruction Cycle Flow

```
                    +-----------+
                    |  Start    |
                    +-----------+
                         |
                         v
                    +-----------+     +-----------+
         +--------->| FETCH     |---->| DECODE    |
         |          | (Get next |     | (Interpret|
         |          |  instrn)  |     |  instrn)  |
         |          +-----------+     +-----+-----+
         |                                |
         |                                v
         |                          +-----------+
         |                          | EXECUTE   |
         |                          | (Perform  |
         |                          | operation)|
         |                          +-----+-----+
         |                                |
         |                          +-----------+
         |                          | INTERRUPT?|
         |                          | (Check if |
         |                          |  pending) |
         |                          +-----+-----+
         |                     No        |
         |      +------------------------+--------+
         |      |                                 |
         |      v                                 v (Yes)
         |  +-------+                     +-----------+
         |  | HALT? |                     | INTERRUPT |
         |  | (Stop |                     | (Handle   |
         |  |  exec)|                     |  IRQ)     |
         |  +---+---+                     +-----------+
         | No   | Yes                        |
         +------+                            |
                v                            |
           +--------+                        |
           |  STOP  |                        |
           +--------+                        |
                                             v
                                        +---------+
                                        | (return |
                                        | to user |
                                        | program)|
                                        +---------+
                                             |
                                             +-----------> (back to fetch)
```

### 3. Fetch Cycle (Detailed)

The fetch cycle retrieves the next instruction from memory and places it in the Instruction Register (IR).

**Step-by-step operations:**

```
+-------+-------+---------------------------------------------------------+
| Step  | RTL   | Description                                             |
+-------+-------+---------------------------------------------------------+
| T0    | MAR   | Program Counter (PC) value is transferred to the         |
|       | <- PC | Memory Address Register (MAR). The address of the        |
|       |       | next instruction is now on the address bus.             |
+-------+-------+---------------------------------------------------------+
| T1    | MBR   | Control unit asserts MemRead signal. Memory reads the    |
|       | <- M  | word at address MAR and places it on the data bus.       |
|       | [MAR] | The Memory Buffer Register (MBR) captures this data.    |
+-------+-------+---------------------------------------------------------+
| T2    | IR    | The instruction in MBR is transferred to the            |
|       | <- MBR| Instruction Register (IR).                               |
+-------+-------+---------------------------------------------------------+
| T3    | PC    | The Program Counter is incremented to point to the       |
|       | <- PC | next instruction. The increment amount is the length      |
|       | + 1   | of the instruction (typically 1 word = 4 bytes).         |
+-------+-------+---------------------------------------------------------+
```

**Note:** Steps T2 and T3 are often performed in the same clock cycle.

**Timing diagram for fetch cycle (4 T-states, assuming 1 cycle per step):**

```
Clock:    _-_-_-_-_-_-_-_-_-_-_-_-_-_
          |   |   |   |   |   |   |   |
          | T0| T1| T2| T3| T4| T5|   |
---------|   |   |   |   |   |   |   |
PC -> MAR: ___|^^|______________________
          |   |   |   |   |   |   |   |
MemRead:  _______|^^|__________________
          |   |   |   |   |   |   |   |
Data bus: _______|???|^^|data_________
          |   |   |   |   |   |   |   |
MBR <- M[MAR]: __|???|^^|____________
          |   |   |   |   |   |   |   |
IR <- MBR: ___________|^^|____________
          |   |   |   |   |   |   |   |
PC <- PC+1: ___________|^^|^^|________
          |   |   |   |   |   |   |   |
```

(??? = data not yet valid; ^^ = signal active)

### 4. Decode Cycle

During the decode cycle, the control unit interprets the instruction in the IR.

**Step-by-step operations:**

```
+-------+-------+---------------------------------------------------------+
| Step  | Action| Description                                             |
+-------+-------+---------------------------------------------------------+
| T4    | Decode| Control unit decodes the opcode field of the instruction  |
|       | Opcode| in IR. A decoder circuit or microcode sequencer          |
|       |       | identifies the instruction type (ADD, LOAD, JUMP, etc.). |
+-------+-------+---------------------------------------------------------+
| T4    | Check | Control unit examines the addressing mode bits (if any)  |
|       | Addr  | to determine how operand addresses are to be computed.    |
|       | Mode  |                                                         |
+-------+-------+---------------------------------------------------------+
| T4    | Prep  | If the instruction references registers, the register    |
|       | Oper- | addresses in the IR are sent to the register file to     |
|       | ands  | begin reading operand values (or preparing to write).     |
+-------+-------+---------------------------------------------------------+
```

The decode phase often overlaps with the beginning of the execute phase in pipelined processors.

### 5. Execute Cycle

The execute cycle performs the actual operation. The specific steps depend on the instruction type.

#### 5.1 Execute Cycle for ADD R1, R2 (Register-to-Register Add)

```
+-------+-------+---------------------------------------------------------+
| Step  | RTL   | Description                                             |
+-------+-------+---------------------------------------------------------+
| T5    | ALU   | Register R2 is read from the register file and sent to   |
|       | Input | one input of the ALU.                                     |
|       | A <-  |                                                         |
|       | R2    |                                                         |
+-------+-------+---------------------------------------------------------+
| T5    | ALU   | Register R1 is read and sent to the other ALU input.     |
|       | Input | (R1 is both source and destination in a two-address      |
|       | B <-  | instruction.)                                            |
|       | R1    |                                                         |
+-------+-------+---------------------------------------------------------+
| T6    | ALU   | Control unit sets the ALU operation to ADD (opcode       |
|       | Opr = | selects the adder circuit). Result appears at ALU        |
|       | ADD   | output.                                                  |
+-------+-------+---------------------------------------------------------+
| T6    | PSW   | Condition flags (Zero, Carry, Sign, Overflow) are        |
|       | Update| updated based on the ALU result.                         |
+-------+-------+---------------------------------------------------------+
| T7    | R1    | The ALU result is written back to register R1.           |
|       | <- ALU| (RegWrite signal enables the register write.)            |
|       | Out   |                                                         |
+-------+-------+---------------------------------------------------------+
```

#### 5.2 Execute Cycle for LOAD R1, Address

```
+-------+-------+---------------------------------------------------------+
| Step  | RTL   | Description                                             |
+-------+-------+---------------------------------------------------------+
| T5    | MAR   | The address field from the IR is extracted and loaded    |
|       | <- IR | into MAR. (For direct addressing, the address is in the  |
|       | [addr]| instruction itself.)                                     |
+-------+-------+---------------------------------------------------------+
| T6    | MBR   | Control unit asserts MemRead. Memory returns data at     |
|       | <- M  | address MAR. Data is loaded into MBR.                    |
|       | [MAR] |                                                         |
+-------+-------+---------------------------------------------------------+
| T7    | R1    | The data in MBR is transferred to the destination        |
|       | <- MBR| register R1.                                             |
+-------+-------+---------------------------------------------------------+
```

#### 5.3 Execute Cycle for STORE R1, Address

```
+-------+-------+---------------------------------------------------------+
| Step  | RTL   | Description                                             |
+-------+-------+---------------------------------------------------------+
| T5    | MAR   | The address field from IR is loaded into MAR.            |
|       | <- IR |                                                         |
|       | [addr]|                                                         |
+-------+-------+---------------------------------------------------------+
| T6    | MBR   | The contents of register R1 are transferred to MBR.      |
|       | <- R1 |                                                         |
+-------+-------+---------------------------------------------------------+
| T7    | M[MAR]| Control unit asserts MemWrite. Memory stores the data    |
|       | <- MBR| from MBR at the address in MAR.                          |
+-------+-------+---------------------------------------------------------+
```

#### 5.4 Execute Cycle for JUMP Address

```
+-------+-------+---------------------------------------------------------+
| Step  | RTL   | Description                                             |
+-------+-------+---------------------------------------------------------+
| T5    | PC    | The address field from the instruction is loaded         |
|       | <- IR | directly into the PC. The next fetch cycle will read     |
|       | [addr]| from this new address.                                   |
+-------+-------+---------------------------------------------------------+
```

**Note:** For conditional jumps (JZ, JNZ, JC, etc.), the control unit first checks the relevant flag in PSW:

```
+-------+-------+---------------------------------------------------------+
| T5    | Check | Control unit checks the condition flag (e.g., Zero flag |
|       | Flag  | for JZ).                                                |
+-------+-------+---------------------------------------------------------+
| T5a   | PC    | If flag = 1 (condition true): PC <- IR[address]          |
|       | Update| If flag = 0 (condition false): do nothing (continue      |
|       |       | sequential execution).                                  |
+-------+-------+---------------------------------------------------------+
```

### 6. Interrupt Cycle

After the execute cycle completes, the control unit checks whether an interrupt request is pending.

**What is an interrupt?**
An interrupt is a signal from an I/O device or an internal condition that requires the CPU's attention. Interrupts allow the CPU to handle events asynchronously (e.g., keyboard input, timer expiry, disk I/O completion).

**Steps in the interrupt cycle:**

```
+-------+-------+---------------------------------------------------------+
| Step  | RTL   | Description                                             |
+-------+-------+---------------------------------------------------------+
| T8    | Check | CU checks the interrupt request line (INTR). If no      |
|       | INTR  | interrupt is pending, the next instruction cycle begins  |
|       |       | (go to T0).                                              |
+-------+-------+---------------------------------------------------------+
| T8    | Save  | If interrupt is pending AND interrupts are enabled        |
|       | PC    | (IF flag in PSW = 1), the current PC value (return       |
|       |       | address) is saved. Typically: SP <- SP - 1; M[SP] <- PC. |
+-------+-------+---------------------------------------------------------+
| T9    | Load  | The address of the Interrupt Service Routine (ISR) is    |
|       | ISR   | loaded into PC. The ISR address may be:                   |
|       | Addr  | - Fixed (e.g., interrupt vector table entry)             |
|       |       | - Provided by the interrupting device                    |
+-------+-------+---------------------------------------------------------+
| T9    | Clear | The interrupt enable flag (IF) in PSW is cleared so that |
|       | IF    | further interrupts are masked during ISR execution.      |
+-------+-------+---------------------------------------------------------+
|       | Fetch | The next instruction is fetched from the ISR address.     |
|       | ISR   |                                                         |
+-------+-------+---------------------------------------------------------+
```

**Interrupt cycle flow:**

```
                    +-----------+
                    | Execute   |
                    | Complete  |
                    +-----------+
                         |
                         v
                    +-----------+
              No    | Interrupt |
         +-------->| Pending?  |
         |         +-----+-----+
         |               | Yes
         |               v
         |         +-----------+
         |         | Save PC   |
         |         | on Stack  |
         |         +-----------+
         |               |
         |               v
         |         +-----------+
         |         | Load ISR  |
         |         | Address   |
         |         | into PC   |
         |         +-----------+
         |               |
         |               v
         |         +-----------+
         |         | Clear IF  |
         |         +-----------+
         |               |
         +-------+-------+
                 |
                 v
            +-----------+
            | Fetch next|
            | Inst.     |
            +-----------+
```

### 7. Step-by-Step Walkthrough: ADD Instruction Execution

#### Full Walkthrough: `ADD R1, R2` (R1 = R1 + R2)

**Initial state:**
- PC = 1000 (instruction is at address 1000)
- R1 = 5
- R2 = 7
- Memory[1000] = 0x2412 (encoded instruction: opcode=ADD, dest=R1, src=R2)

**Step-by-step execution:**

| Cycle | Phase | Action | Registers Changed | Explanation |
|-------|-------|--------|-------------------|-------------|
| 1 | Fetch | MAR <- PC | MAR = 1000 | PC value placed on address bus |
| 2 | Fetch | MBR <- M[MAR] | MBR = 0x2412 | Memory read; instruction loaded into MBR |
| 3 | Fetch | IR <- MBR | IR = 0x2412 | Instruction transferred to IR |
| 4 | Fetch | PC <- PC + 1 | PC = 1004 | PC incremented (assuming 4-byte instr) |
| 5 | Decode | Decode IR | -- | CU decodes opcode (ADD), dest (R1), src (R2) |
| 6 | Execute | ALU_A <- R2 | ALU_A = 7 | Register R2 value sent to ALU input A |
| 7 | Execute | ALU_B <- R1 | ALU_B = 5 | Register R1 value sent to ALU input B |
| 8 | Execute | ALU_op = ADD | ALU_out = 12 | ALU performs addition |
| 9 | Execute | Update PSW | PSW: Z=0,S=0,C=0,V=0 | Result non-zero, positive, no carry/overflow |
| 10 | Execute | R1 <- ALU_out | R1 = 12 | Result written to destination register R1 |
| 11 | Int. | Check INTR | -- | If no interrupt pending, go to next fetch |

**Final state:**
- PC = 1004 (ready for next instruction)
- R1 = 12 (5 + 7 = 12)
- R2 = 7 (unchanged)
- PSW flags reflect the result (Z=0, S=0)

### 8. Timing Diagram Description

A timing diagram shows how signals change over time during instruction execution.

**Key signals in the timing diagram:**

| Signal | Description |
|--------|-------------|
| CLK | System clock (square wave) |
| T0, T1, T2,... | T-state signals (one active per cycle) |
| PC | Program Counter value on internal bus |
| MAR | Memory Address Register value |
| Address Bus | Address on external address bus |
| MemRead | Memory read control signal |
| Data Bus | Data on external data bus |
| MBR | Memory Buffer Register value |
| IR | Instruction Register value |
| ALU_A, ALU_B | ALU input operands |
| ALU_Out | ALU output |
| RegWrite | Register write enable signal |

**Detailed timing for ADD R1, R2 (assuming 11 cycles total):**

```
          T0    T1    T2    T3    T4    T5    T6    T7    T8    T9   T10
CLK     _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

PC         1000  1000  1000  1004  1004  1004  1004  1004  1004  1004  1004
MAR               1000  1000  1000  1000  1000  1000  1000  1000  1000  1000
AddressBus        1000  1000  1000
DataBus                2412  2412  2412
MBR                      2412  2412  2412
IR                            2412  2412  2412
ALU_A (R2)                                 7     7     7     7
ALU_B (R1)                                 5     5     5     5
ALU_Out                                       12    12    12
R1 (value)       5     5     5     5     5     5     5     5     12    12
RegWrite                                                                _
PSW.Z                                                                  0
PSW.S                                                                  0
```

**Phases:**
- **T0-T3**: Fetch phase (MAR<-PC, MBR<-M[MAR], IR<-MBR, PC<-PC+1)
- **T4**: Decode phase
- **T5-T9**: Execute phase (read registers, ALU op, write back)
- **T10**: Interrupt check (not shown fully)

### 9. Instruction Cycle Summary Table

| Phase | Duration (cycles) | Key Activities |
|-------|-------------------|----------------|
| Fetch | 2-4 | MAR <- PC; MBR <- M[MAR]; IR <- MBR; PC <- PC + 1 |
| Decode | 1-2 | Decode opcode; identify operands; set up control signals |
| Execute | 1-10+ | Varies by instruction; ALU operations, memory access, register write |
| Interrupt | 2-4 | Check INTR; save PC; load ISR address; clear IF |

**Note:** The number of cycles per phase depends on the architecture (pipelined vs non-pipelined, presence of cache, memory speed, instruction complexity).

### 10. Performance Considerations

**Factors affecting instruction cycle time:**
- **Clock frequency**: Higher frequency = shorter cycle time.
- **Memory access time**: Slower memory = more wait states (extra cycles).
- **Cache hit rate**: Cache hits reduce memory access time.
- **Instruction complexity**: Complex CISC instructions may need many execute cycles.
- **Pipelining**: Overlaps fetch, decode, execute phases for different instructions (improves throughput).

**Example: Effect of pipeline on ADD execution**

**Non-pipelined (sequential):**
```
Instruction 1: [FETCH][DECODE][EXECUTE][INTERRUPT]
Instruction 2:              [FETCH][DECODE][EXECUTE][INTERRUPT]
Total: 8 cycles for 2 instructions (4 cycles/instruction)
```

**Pipelined (3-stage):**
```
Instr 1: [FETCH][DECODE][EXECUTE]
Instr 2:        [FETCH][DECODE][EXECUTE]
Instr 3:               [FETCH][DECODE][EXECUTE]
Total: 5 cycles for 3 instructions (1.67 cycles/instruction)
```

---

## Practice Problems

1. **Problem**: Assume a CPU with a 4-cycle fetch phase. If memory access takes 3 clock cycles (one wait state), what is the total time to fetch an instruction, assuming a 2 GHz clock?
   **Answer**: Fetch = 4 cycles + 3 cycles (wait for memory) = 7 cycles. At 2 GHz, one cycle = 0.5 ns. Total fetch time = 7 x 0.5 = 3.5 ns.

2. **Problem**: During the execute phase of a `JZ 2000` instruction, the Zero flag (Z) in the PSW is 0. What happens to the PC?
   **Answer**: Since Z = 0, the condition is false (not zero). The PC is not modified and continues to point to the next sequential instruction (it was already incremented during the fetch phase). Execution continues with the next instruction in sequence.

3. **Problem**: List the differences between the execute phase of a LOAD instruction and a STORE instruction.
   **Answer**:
   - LOAD: MAR <- IR[address]; MBR <- M[MAR]; register <- MBR (memory to register).
   - STORE: MAR <- IR[address]; MBR <- register; M[MAR] <- MBR (register to memory).
   The key difference: LOAD reads from memory into MBR then into a register; STORE reads from a register into MBR then writes MBR to memory. LOAD uses MemRead; STORE uses MemWrite.

4. **Problem**: During the interrupt cycle, the PC is saved on the stack. Why must the PC be saved rather than just continuing from the current PC value after the ISR returns?
   **Answer**: When the interrupt is acknowledged, the PC has already been incremented during the fetch phase and now points to the next instruction to be executed, not the instruction that was just executed. After the ISR completes, the CPU must resume the interrupted program at the correct point -- the instruction following the one that was interrupted. The saved PC provides this return address.

5. **Problem**: Draw the state diagram for a basic instruction cycle with four states: Fetch, Decode, Execute, Interrupt. Label the transitions.
   **Answer**:
   ```
           +-----------+
           |  FETCH    |
           +-----+-----+
                 |
                 v
           +-----+-----+
           |  DECODE   |
           +-----+-----+
                 |
                 v
           +-----+-----+
           |  EXECUTE  |
           +-----+-----+
                 |
         +-------+-------+
         |               |
         v               v
   +-----+-----+   +-----+-----+
   |  No Int   |   | Interrupt |
   |  (go to   |   | (save PC, |
   |  Fetch)   |   |  load ISR)|
   +-----------+   +-----+-----+
                           |
                           v
                     +-----+-----+
                     |  (go to   |
                     |  Fetch)   |
                     +-----------+
   ```
