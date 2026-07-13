# RTL interpretation of instructions

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 6  
**Date:** 15-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to Register Transfer Language (RTL)

Register Transfer Language (RTL) is a symbolic notation used to describe the internal data flow and operations of a digital computer at the register level. It provides a precise, concise way to specify:

- Which registers are read and written.
- What operations are performed on data.
- The sequence of micro-operations that implement an instruction.

**Purpose of RTL:**
- To document the architecture of a CPU (the "what") independently of the implementation (the "how").
- To serve as a specification for hardware designers implementing the CPU.
- To help understand and analyze instruction execution step by step.

RTL is NOT a programming language -- it is a **hardware description notation** used in computer architecture design.

### 2. RTL Notation and Conventions

#### 2.1 Basic Symbols

| Symbol | Meaning | Example |
|--------|---------|---------|
| `<-` | Data transfer (assignment) | `R1 <- R2` (copy R2 into R1) |
| `( )` | Part of a register | `PC(L)` (lower byte of PC) |
| `[ ]` | Contents of a memory location | `M[1000]` (memory at address 1000) |
| `,` | Separator for parallel operations | `MAR <- PC, MBR <- R1` |
| `;` | End of a micro-operation sequence | (often implicit per line) |
| `+` | Addition | `R1 <- R2 + R3` |
| `-` | Subtraction | `R1 <- R2 - R3` |
| `*` | Multiplication | `R1 <- R2 * R3` |
| `/` | Division | `R1 <- R2 / R3` |
| `AND` | Bitwise AND | `R1 <- R2 AND R3` |
| `OR` | Bitwise OR | `R1 <- R2 OR R3` |
| `XOR` | Bitwise XOR | `R1 <- R2 XOR R3` |
| `NOT` | Bitwise complement | `R1 <- NOT R2` |
| `SHL` | Shift left | `R1 <- SHL R2, n` |
| `SHR` | Shift right | `R1 <- SHR R2, n` |
| `CONCAT` | Concatenation | `IR <- MBR CONCAT PC` |
| `n` | Constant/literal | `R1 <- R2 + 1` |

#### 2.2 Register Names Used in RTL

| Symbol | Full Name | Description |
|--------|-----------|-------------|
| `PC` | Program Counter | Holds address of next instruction |
| `IR` | Instruction Register | Holds current instruction |
| `MAR` | Memory Address Register | Holds address for memory access |
| `MBR` (or `MDR`) | Memory Buffer Register | Holds data for/from memory |
| `R0, R1, ..., Rn` | General Purpose Registers | Programmer-visible registers |
| `SP` | Stack Pointer | Points to top of stack |
| `FP` | Frame Pointer | Points to current stack frame |
| `PSW` (or `FLAGS`) | Program Status Word | Holds condition and control flags |
| `AC` | Accumulator | Implicit operand in accumulator arch |
| `TEMP` (or `T`) | Temporary Register | Internal CPU temporary storage |
| `M[X]` | Memory at address X | Contents of memory location X |

#### 2.3 Timing and Sequencing

RTL often indicates the timing of operations using a prefix notation:

- `T0: RTL statement` -- Operation occurs during clock cycle T0.
- Multiple operations in one cycle (separated by comma) occur **simultaneously** (same clock edge).

Example:
```
T0: MAR <- PC, PC <- PC + 1
T1: MBR <- M[MAR]
T2: IR <- MBR
```

In T0, MAR is loaded with PC value AND PC is incremented -- both happen in parallel on the same clock edge.

**Important rule:** When two operations occur simultaneously, the right-hand side values are the **old** values (before the clock edge). So `P <- Q, Q <- P` correctly swaps the values.

### 3. RTL for the Basic Fetch Cycle

The fetch cycle is the same for every instruction (except possibly for the amount PC is incremented).

```
T0: MAR <- PC          ; Place PC value onto address bus (via MAR)
T1: MBR <- M[MAR]      ; Read instruction from memory into MBR
T2: IR <- MBR          ; Transfer instruction to IR
T3: PC <- PC + 1       ; Increment PC to point to next instruction
```

**Alternative (compact) notation:**
```
T0: MAR <- PC
T1: MBR <- M[MAR]
T2: IR <- MBR, PC <- PC + 1
```

(T2 combines two operations in one cycle.)

**Explanation of each micro-operation:**

```
T0: MAR <- PC
    +-------+            +-------+
    |  PC   |--(bus)---->|  MAR  |
    +-------+            +-------+
    (MAR now holds the instruction address)

T1: MBR <- M[MAR]
    +-------+            +-------+
    |  MAR  |--(addr)--->|Memory |--(data)--->| MBR  |
    +-------+            +-------+            +-------+
    (Memory returns instruction; MBR captures it)

T2: IR <- MBR
    +-------+            +-------+
    |  MBR  |--(bus)---->|  IR   |
    +-------+            +-------+
    (Instruction now in IR for decoding)

T3: PC <- PC + 1
    +-------+
    |  PC   |--(increment)-->|  PC' = PC + 1  |
    +-------+
    (For variable-length instructions, increment amount varies)
```

### 4. RTL for Specific Instructions

#### 4.1 ADD R1, R2 (Register-to-Register Addition)

**Instruction:** Add contents of register R2 to register R1. Result in R1.
**Assembly:** `ADD R1, R2`
**Operation:** R1 <- R1 + R2

**Complete RTL sequence:**

```
; ---- Fetch Cycle (same for all instructions) ----
T0: MAR <- PC
T1: MBR <- M[MAR]
T2: IR <- MBR
T3: PC <- PC + 1

; ---- Decode Phase ----
T4: IR(opcode) decoded to determine operation (ADD)
    ; Control unit identifies: ADD R1, R2

; ---- Execute Cycle ----
T5: ALU_A <- R2        ; Send R2 to ALU input A
T6: ALU_B <- R1        ; Send R1 to ALU input B
T7: ALU_Out <- ALU_A + ALU_B  ; Perform addition
T8: PSW <- Update flags based on ALU_Out (Z, C, S, V)
T9: R1 <- ALU_Out      ; Write result back to R1
```

**Compact RTL notation (combining steps):**

```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
R1 <- R1 + R2  ; Single RTL statement for the entire ADD operation
```

The compact form is used when we are not concerned with the exact cycle-by-cycle timing.

#### 4.2 LOAD R1, X (Load from Memory to Register)

**Instruction:** Load register R1 with the contents of memory address X.
**Assembly:** `LOAD R1, X`
**Operation:** R1 <- M[X]

**RTL sequence:**

```
; ---- Fetch Cycle ----
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; ---- Decode ----
; Control unit identifies: LOAD R1, X
; Address X is in the operand field of IR

; ---- Execute Cycle ----
MAR <- IR[address]    ; Extract address X from instruction
MBR <- M[MAR]         ; Read memory location X
R1 <- MBR             ; Transfer data to register R1
```

**Compact RTL:** `R1 <- M[X]`

**Data flow diagram for LOAD:**
```
Instruction: LOAD R1, 2000
                  +-------+
IR[address]=2000->|  MAR  |
                  +---+---+
                      |
                      v
                +-----+------+
                | Memory      |
                | addr 2000   |
                +-----+------+
                      |
                      v
                 +----+----+
                 |   MBR   |
                 +----+----+
                      |
                      v
                 +----+----+
                 |   R1    |
                 +---------+
```

#### 4.3 STORE R1, X (Store Register to Memory)

**Instruction:** Store contents of register R1 into memory address X.
**Assembly:** `STORE R1, X`
**Operation:** M[X] <- R1

**RTL sequence:**

```
; ---- Fetch Cycle ----
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; ---- Decode ----
; Control unit identifies: STORE R1, X

; ---- Execute Cycle ----
MAR <- IR[address]    ; Extract address X from instruction
MBR <- R1             ; Transfer data from R1 to MBR
M[MAR] <- MBR         ; Write MBR to memory at address MAR
```

**Compact RTL:** `M[X] <- R1`

**Data flow diagram for STORE:**
```
Instruction: STORE R1, 2000
                  +-------+
IR[address]=2000->|  MAR  |
                  +---+---+
                      |
+---------+      +----+----+      +--------+
|   R1    |----->|   MBR   |----->| Memory |
+---------+      +---------+      | addr   |
                                  | 2000   |
                                  +--------+
```

#### 4.4 JUMP X (Unconditional Branch)

**Instruction:** Jump to instruction at address X.
**Assembly:** `JUMP X`
**Operation:** PC <- X

**RTL sequence:**

```
; ---- Fetch Cycle ----
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1         ; (This increment gets overridden by jump)

; ---- Decode ----
; Control unit identifies: JUMP X

; ---- Execute Cycle ----
PC <- IR[address]    ; Override PC with target address X
```

**Compact RTL:** `PC <- X`

**Important:** The PC increment during fetch is irrelevant because the execute phase overwrites PC with the jump target.

#### 4.5 Conditional Jump (e.g., JZ X)

**Instruction:** Jump to address X if the Zero flag (Z) is set.
**Assembly:** `JZ X`
**Operation:** If (Z == 1) then PC <- X else continue

**RTL sequence:**

```
; ---- Fetch Cycle ----
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; ---- Decode ----
; Control unit identifies: JZ X

; ---- Execute Cycle ----
T5: Check PSW_Z flag
; If PSW_Z = 1:
    PC <- IR[address]    ; Jump taken
; If PSW_Z = 0:
    ; PC unchanged (continue sequential execution)
```

**Compact RTL:**
```
IF (Z == 1) THEN PC <- X ELSE PC <- PC
```

**Conditional jumps for other flags:**
```
JNZ X:  IF (Z == 0) THEN PC <- X
JC X:   IF (C == 1) THEN PC <- X
JNC X:  IF (C == 0) THEN PC <- X
JS X:   IF (S == 1) THEN PC <- X
JNS X:  IF (S == 0) THEN PC <- X
JO X:   IF (V == 1) THEN PC <- X
JNO X:  IF (V == 0) THEN PC <- X
```

### 5. Additional RTL Examples

#### 5.1 SUB R1, R2 (Subtract)

**Assembly:** `SUB R1, R2`
**RTL:** `R1 <- R1 - R2`

**Full sequence:**
```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
R1 <- R1 - R2
PSW <- Update flags based on (R1 - R2)
```

#### 5.2 MUL R1, R2 (Multiply)

**Assembly:** `MUL R1, R2`
**RTL:** `R1 <- R1 * R2`

Note: Multiplication often takes multiple clock cycles and may use a pair of registers for the result (e.g., HI:LO in MIPS).

```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
HI || LO <- R1 * R2   ; HI holds high 32 bits, LO holds low 32 bits
; Or for simpler architectures:
R1 <- R1 * R2         ; (may truncate if result exceeds register width)
```

#### 5.3 AND R1, R2 (Bitwise AND)

**Assembly:** `AND R1, R2`
**RTL:** `R1 <- R1 AND R2`

```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
R1 <- R1 AND R2
PSW <- Update flags (Z=1 if result=0, S=1 if MSB=1)
```

#### 5.4 NOT R1 (Bitwise Complement)

**Assembly:** `NOT R1`
**RTL:** `R1 <- NOT R1`

```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
R1 <- NOT R1
```

#### 5.5 SHL R1, n (Shift Left)

**Assembly:** `SHL R1, n`
**RTL:** `R1 <- SHL(R1, n)`

Shifts all bits in R1 left by n positions. Vacated positions (least significant) are filled with 0. The most significant bits shifted out go into the Carry flag.

```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
C <- R1(MSB)          ; Save the bit shifted out
R1 <- R1 << n         ; Shift left by n
; (PSW updated accordingly)
```

**Example:** If R1 = 0000 0101 (5) and n = 2:
```
R1 <- 0001 0100 (20)
C <- 0 (last bit shifted out was 0)
```

#### 5.6 MOVE R1, R2 (Register-to-Register Copy)

**Assembly:** `MOVE R1, R2`
**RTL:** `R1 <- R2`

```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
R1 <- R2
```

### 6. PUSH and POP Operations (Stack Instructions)

#### 6.1 PUSH R1

**Assembly:** `PUSH R1`
**Operation:** Push contents of R1 onto the stack. SP is decremented (stack grows downward).

**RTL:**
```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
SP <- SP - 1          ; Decrement stack pointer
M[SP] <- R1           ; Store R1 at new top of stack
```

#### 6.2 POP R1

**Assembly:** `POP R1`
**Operation:** Pop top of stack into R1. SP is incremented.

**RTL:**
```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
R1 <- M[SP]           ; Read top of stack
SP <- SP + 1          ; Increment stack pointer
```

### 7. CALL and RETURN (Subroutine Instructions)

#### 7.1 CALL X

**Assembly:** `CALL X`
**Operation:** Call subroutine at address X. Save return address (current PC) on stack, then jump to X.

**RTL:**
```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1          ; PC now points to instruction after CALL

; Execute
SP <- SP - 1          ; Make room on stack
M[SP] <- PC           ; Save return address (instruction after CALL)
PC <- IR[address]     ; Jump to subroutine address X
```

**Compact RTL:**
```
M[--SP] <- PC
PC <- X
```

#### 7.2 RETURN

**Assembly:** `RET`
**Operation:** Return from subroutine. Pop the return address from stack into PC.

**RTL:**
```
; Fetch
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
PC <- M[SP]           ; Load return address from stack
SP <- SP + 1          ; Pop stack
```

**Compact RTL:**
```
PC <- M[SP++]
```

### 8. Complete RTL Example: Executing a Program Fragment

**Program in assembly:**
```
100: LOAD R1, 2000    ; R1 = M[2000]
104: ADD R1, R2       ; R1 = R1 + R2
108: STORE R1, 3000   ; M[3000] = R1
112: JUMP 100         ; Loop back
```

**RTL execution trace (compact notation):**

```
; Initial state: PC = 100, R2 = 3, M[2000] = 5

; Instruction 1: LOAD R1, 2000
; Fetch:
MAR <- PC (=100)
MBR <- M[MAR]         ; MBR = instruction at 100
IR <- MBR             ; IR = "LOAD R1, 2000"
PC <- PC + 1          ; PC = 104
; Execute:
MAR <- IR[address]    ; MAR = 2000
MBR <- M[MAR]         ; MBR = M[2000] = 5
R1 <- MBR             ; R1 = 5

; Instruction 2: ADD R1, R2
; Fetch:
MAR <- PC (=104)
MBR <- M[MAR]         ; MBR = instruction at 104
IR <- MBR             ; IR = "ADD R1, R2"
PC <- PC + 1          ; PC = 108
; Execute:
R1 <- R1 + R2         ; R1 = 5 + 3 = 8

; Instruction 3: STORE R1, 3000
; Fetch:
MAR <- PC (=108)
MBR <- M[MAR]         ; MBR = instruction at 108
IR <- MBR             ; IR = "STORE R1, 3000"
PC <- PC + 1          ; PC = 112
; Execute:
MAR <- IR[address]    ; MAR = 3000
MBR <- R1             ; MBR = R1 = 8
M[MAR] <- MBR         ; M[3000] = 8

; Instruction 4: JUMP 100
; Fetch:
MAR <- PC (=112)
MBR <- M[MAR]         ; MBR = instruction at 112
IR <- MBR             ; IR = "JUMP 100"
PC <- PC + 1          ; PC = 116 (will be overridden)
; Execute:
PC <- IR[address]     ; PC = 100 (program loops back)
```

### 9. RTL Summary Reference Table

| Instruction | Assembly | RTL |
|-------------|----------|-----|
| Load | `LOAD Rd, X` | `Rd <- M[X]` |
| Store | `STORE Rs, X` | `M[X] <- Rs` |
| Move | `MOVE Rd, Rs` | `Rd <- Rs` |
| Add | `ADD Rd, Rs` | `Rd <- Rd + Rs` |
| Subtract | `SUB Rd, Rs` | `Rd <- Rd - Rs` |
| Multiply | `MUL Rd, Rs` | `Rd <- Rd * Rs` |
| Divide | `DIV Rd, Rs` | `Rd <- Rd / Rs` |
| AND | `AND Rd, Rs` | `Rd <- Rd AND Rs` |
| OR | `OR Rd, Rs` | `Rd <- Rd OR Rs` |
| XOR | `XOR Rd, Rs` | `Rd <- Rd XOR Rs` |
| NOT | `NOT Rd` | `Rd <- NOT Rd` |
| Shift Left | `SHL Rd, n` | `Rd <- Rd << n` |
| Shift Right | `SHR Rd, n` | `Rd <- Rd >> n` |
| Jump | `JUMP X` | `PC <- X` |
| Jump if Zero | `JZ X` | `IF Z=1 THEN PC <- X` |
| Jump if Not Zero | `JNZ X` | `IF Z=0 THEN PC <- X` |
| Jump if Carry | `JC X` | `IF C=1 THEN PC <- X` |
| Call | `CALL X` | `M[--SP] <- PC; PC <- X` |
| Return | `RET` | `PC <- M[SP++]` |
| Push | `PUSH Rs` | `M[--SP] <- Rs` |
| Pop | `POP Rd` | `Rd <- M[SP++]` |

---

## Practice Problems

1. **Problem**: Write the complete RTL sequence (fetch + execute) for the instruction `ADD R3, R5` assuming two-address format where R3 is both source and destination.
   **Answer**:
   ```
   ; Fetch
   MAR <- PC
   MBR <- M[MAR]
   IR <- MBR
   PC <- PC + 1
   ; Execute
   R3 <- R3 + R5
   PSW <- Update flags
   ```

2. **Problem**: Translate the following assembly code into RTL (compact notation): `LOAD R1, 500; ADD R1, R2; STORE R1, 600`
   **Answer**:
   ```
   R1 <- M[500]
   R1 <- R1 + R2
   M[600] <- R1
   ```

3. **Problem**: In RTL notation, what does `M[--SP] <- PC` mean? Explain each symbol.
   **Answer**: This is the CALL instruction's save operation. `--SP` means "decrement SP first, then use the new value" (pre-decrement). `M[--SP]` means "the memory location addressed by the decremented SP". `<- PC` means "the value of PC is written to that memory location". So the operation saves the return address on the stack and adjusts the stack pointer.

4. **Problem**: Given the RTL sequence:
   ```
   T0: MAR <- PC
   T1: MBR <- M[MAR]
   T2: IR <- MBR, PC <- PC + 1
   T3: MAR <- IR[address]
   T4: MBR <- M[MAR]
   T5: R1 <- MBR
   ```
   What instruction does this implement? Which cycle does T3-T5 belong to?
   **Answer**: This implements `LOAD R1, X`. T0-T2 is the fetch cycle. T3-T5 is the execute cycle (load phase: get address, read memory, transfer to register).

5. **Problem**: Write RTL for a decrement-and-skip-if-zero instruction: `DSZ R1` (decrement R1; if R1 becomes zero, skip the next instruction by incrementing PC again).
   **Answer**:
   ```
   ; Fetch (normal)
   MAR <- PC
   MBR <- M[MAR]
   IR <- MBR
   PC <- PC + 1
   ; Execute
   R1 <- R1 - 1
   IF (R1 == 0) THEN PC <- PC + 1  ; Skip next instruction
   ```
