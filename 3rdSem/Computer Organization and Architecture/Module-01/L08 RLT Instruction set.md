# RLT Instruction set

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 8  
**Date:** 22-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction

Note: The title "RLT" is a common typographical variant of **RTL** (Register Transfer Language). This lecture continues the RTL discussion from Lecture 6, providing a complete RTL instruction set with detailed examples. We cover RTL for all major instruction categories including arithmetic, logical, shift/rotate, I/O, subroutine call/return, and micro-operations.

RTL provides a formal, precise way to describe the meaning (semantics) of each instruction in a CPU's instruction set. Each instruction is defined by a sequence of Register Transfer operations, often broken down into **micro-operations** -- the smallest indivisible operations performed in one clock cycle.

### 2. RTL Notation Review

**Basic notation:**
- `A <- B` -- Transfer contents of register B to register A.
- `M[X]` -- Contents of memory location at address X.
- `A <- B op C` -- Perform operation on B and C, store result in A.
- `A(B)` -- Part of register A (e.g., `IR(opcode)` for opcode field of IR).
- `--SP` -- Pre-decrement stack pointer (decrement before use).
- `SP++` -- Post-increment stack pointer (use then increment).

**Simultaneous operations:** Operations separated by comma in one line occur in parallel on the same clock edge.

**Conditional operations:** `IF (condition) THEN operation`

### 3. Complete RTL for the Fetch Cycle (Revisited)

The fetch cycle is the same for every instruction:

```
T0: MAR <- PC
T1: MBR <- M[MAR]
T2: IR <- MBR
T3: PC <- PC + 1
```

In many implementations, T2 and T3 are combined:
```
T0: MAR <- PC
T1: MBR <- M[MAR]
T2: IR <- MBR, PC <- PC + 1
```

### 4. RTL for Arithmetic Instructions

#### 4.1 ADD (Addition)

**Instruction:** `ADD Rd, Rs`
**Operation:** Rd <- Rd + Rs

```
; Fetch (standard)
MAR <- PC
MBR <- M[MAR]
IR <- MBR
PC <- PC + 1

; Execute
ALU_A <- Rs
ALU_B <- Rd
ALU_Out <- ALU_A + ALU_B
PSW.Z <- (ALU_Out == 0)
PSW.C <- (carry from MSB)
PSW.S <- ALU_Out(MSB)
PSW.V <- (overflow in signed arithmetic)
Rd <- ALU_Out
```

**Compact RTL:** `Rd <- Rd + Rs`

**Example:** `ADD R1, R2` where R1=5, R2=3 => R1=8

#### 4.2 ADDI (Add Immediate)

**Instruction:** `ADDI Rd, #imm`
**Operation:** Rd <- Rd + imm

```
; Execute
Rd <- Rd + imm
```

**Compact RTL:** `Rd <- Rd + imm`

**Example:** `ADDI R1, #10` where R1=5 => R1=15

#### 4.3 SUB (Subtract)

**Instruction:** `SUB Rd, Rs`
**Operation:** Rd <- Rd - Rs

```
; Execute
ALU_Out <- Rd - Rs
PSW <- Update flags
Rd <- ALU_Out
```

**Compact RTL:** `Rd <- Rd - Rs`

**Example:** `SUB R1, R2` where R1=10, R2=3 => R1=7

#### 4.4 MUL (Multiply)

**Instruction:** `MUL Rd, Rs`
**Operation:** Rd <- Rd * Rs

**Simple (single register result):**
```
Rd <- Rd * Rs
PSW.Z <- (Rd == 0)
PSW.S <- (Rd < 0)
```

**Double register result (common in many architectures):**
```
HI || LO <- Rd * Rs    ; HI = high 32 bits, LO = low 32 bits
```

**Example:** `MUL R1, R2` where R1=7, R2=6 => R1=42

#### 4.5 DIV (Divide)

**Instruction:** `DIV Rd, Rs`
**Operation:** Rd <- Rd / Rs (quotient), remainder in another register

```
; Assuming HI:LO pair
Rd <- LO / Rs          ; quotient
HI <- LO % Rs          ; remainder
PSW <- Update flags (including divide-by-zero check)
```

**Example:** `DIV R1, R2` where R1=42, R2=6 => R1=7 (quotient)

#### 4.6 INC (Increment)

**Instruction:** `INC Rd`
**Operation:** Rd <- Rd + 1

```
Rd <- Rd + 1
PSW <- Update flags
```

#### 4.7 DEC (Decrement)

**Instruction:** `DEC Rd`
**Operation:** Rd <- Rd - 1

```
Rd <- Rd - 1
PSW <- Update flags
```

#### 4.8 NEG (Negate)

**Instruction:** `NEG Rd`
**Operation:** Rd <- -Rd (two's complement negation)

```
Rd <- NOT Rd + 1       ; Two's complement: invert and add 1
PSW <- Update flags
```

#### 4.9 CMP (Compare)

**Instruction:** `CMP Rd, Rs`
**Operation:** Set flags based on Rd - Rs (without storing result)

```
; Execute
Temp <- Rd - Rs        ; Result is discarded
PSW.Z <- (Temp == 0)
PSW.C <- (borrow)
PSW.S <- (Temp < 0)
PSW.V <- (overflow)
; No result stored -- only flags updated
```

### 5. RTL for Logical Instructions

#### 5.1 AND

**Instruction:** `AND Rd, Rs`
**Operation:** Rd <- Rd AND Rs (bitwise)

```
Rd <- Rd AND Rs
PSW.Z <- (Rd == 0)
PSW.S <- Rd(MSB)
```

**Example:** `AND R1, R2` where R1=0xFF, R2=0x0F => R1=0x0F

#### 5.2 OR

**Instruction:** `OR Rd, Rs`
**Operation:** Rd <- Rd OR Rs (bitwise)

```
Rd <- Rd OR Rs
PSW.Z <- (Rd == 0)
PSW.S <- Rd(MSB)
```

**Example:** `OR R1, R2` where R1=0xF0, R2=0x0F => R1=0xFF

#### 5.3 XOR

**Instruction:** `XOR Rd, Rs`
**Operation:** Rd <- Rd XOR Rs (bitwise exclusive OR)

```
Rd <- Rd XOR Rs
PSW.Z <- (Rd == 0)
PSW.S <- Rd(MSB)
```

**Example:** `XOR R1, R2` where R1=0xFF, R2=0x0F => R1=0xF0

#### 5.4 NOT

**Instruction:** `NOT Rd`
**Operation:** Rd <- NOT Rd (bitwise complement)

```
Rd <- NOT Rd
PSW.Z <- (Rd == 0)
PSW.S <- Rd(MSB)
```

**Example:** `NOT R1` where R1=0x0F => R1=0xF0

#### 5.5 ANDI, ORI, XORI (Immediate Logical)

```
ANDI Rd, #imm:  Rd <- Rd AND imm
ORI Rd, #imm:   Rd <- Rd OR imm
XORI Rd, #imm:  Rd <- Rd XOR imm
```

### 6. RTL for Shift and Rotate Instructions

#### 6.1 SHL (Shift Left Logical)

**Instruction:** `SHL Rd, #n`
**Operation:** Shift bits in Rd left by n positions. LSBs filled with 0. MSBs shifted out go into Carry.

```
; n-bit shift
For i = 1 to n:
    C <- Rd(MSB)       ; Save MSB to Carry
    Rd <- Rd << 1      ; Shift left by 1 (LSB = 0)
    
; Or combinational:
Rd <- Rd << n
C <- Rd_in(MSB-n+1)    ; Last bit shifted out
```

**Diagram:**
```
Before: Rd = 1011 0100 (0xB4), n = 2
        C = ? (unknown)

After:  Rd = 1101 0000 (0xD0), C = 1 (bits shifted out: 10, MSB-first)
                ^^ LSB = 00 filled
        ^^ MSB bits lost: 10, last one (1) goes to C
```

**Example:** `SHL R1, #1` where R1=4 (0100) => R1=8 (1000), C=0

#### 6.2 SHR (Shift Right Logical)

**Instruction:** `SHR Rd, #n`
**Operation:** Shift bits in Rd right by n positions. MSBs filled with 0. LSBs shifted out go into Carry.

```
Rd <- Rd >> n
C <- Rd_in(n-1)        ; Last bit shifted out
```

**Example:** `SHR R1, #1` where R1=8 (1000) => R1=4 (0100), C=0

#### 6.3 SAR (Shift Arithmetic Right)

**Instruction:** `SAR Rd, #n`
**Operation:** Shift right arithmetic -- preserves the sign bit (MSB). MSB is copied into the vacated positions.

```
; Sign extension during shift
sign <- Rd(MSB)
For i = 1 to n:
    C <- Rd(0)         ; LSB shifted out
    Rd <- Rd >> 1
    Rd(MSB) <- sign    ; Restore sign bit

; Or:
Rd <- Rd >>> n         ; Arithmetic right shift notation
```

**Example:** `SAR R1, #1` where R1=-8 (1111 1000) => R1=-4 (1111 1100), C=0

#### 6.4 ROL (Rotate Left)

**Instruction:** `ROL Rd, #n`
**Operation:** Rotate bits left. MSB wraps around to LSB position.

```
temp <- Rd(MSB-n+1 to MSB)   ; n MSBs
Rd <- Rd << n                 ; Shift left
Rd(n-1 to 0) <- temp         ; Put old MSBs into LSB positions
```

**Example:** `ROL R1, #1` where R1=1001 0110 => R1=0010 1101

#### 6.5 ROR (Rotate Right)

**Instruction:** `ROR Rd, #n`
**Operation:** Rotate bits right. LSB wraps around to MSB position.

```
temp <- Rd(0 to n-1)          ; n LSBs
Rd <- Rd >> n                 ; Shift right
Rd(MSB downto MSB-n+1) <- temp  ; Put old LSBs into MSB positions
```

**Example:** `ROR R1, #1` where R1=1001 0110 => R1=0100 1011

#### 6.6 RCL / RCR (Rotate Through Carry)

**Instruction:** `RCL Rd, #n` (Rotate through Carry Left)
**Operation:** The carry flag acts as an extension of the register, creating a 17-bit rotate (for 16-bit register).

```
; RCL: Rotate left through carry
temp <- C
C <- Rd(MSB)
Rd <- Rd << 1
Rd(0) <- temp
```

### 7. RTL for I/O Instructions

#### 7.1 IN (Input from I/O Port)

**Instruction:** `IN Rd, PortAddr`
**Operation:** Read data from I/O port into register Rd.

```
; Method 1: Isolated I/O (separate I/O address space)
MAR <- PortAddr        ; I/O address
I/ORead <- 1           ; Assert I/O read signal
MBR <- Port_Data_Bus   ; Read data from I/O data bus
Rd <- MBR
I/ORead <- 0

; Method 2: Memory-mapped I/O (uses standard LOAD)
; IN Rd, PortAddr is equivalent to:
Rd <- M[PortAddr]      ; (PortAddr is mapped to an I/O device)
```

#### 7.2 OUT (Output to I/O Port)

**Instruction:** `OUT PortAddr, Rs`
**Operation:** Write data from register Rs to I/O port.

```
; Isolated I/O
MAR <- PortAddr
MBR <- Rs
I/OWrite <- 1          ; Assert I/O write signal
; Data on Port_Data_Bus written to I/O device
I/OWrite <- 0

; Memory-mapped I/O:
M[PortAddr] <- Rs
```

### 8. RTL for Subroutine Call and Return

#### 8.1 CALL (Call Subroutine)

**Instruction:** `CALL SubroutineAddr`
**Operation:** Save the return address on the stack, then jump to the subroutine.

```
; Full RTL:
T0: MAR <- PC
T1: MBR <- M[MAR]
T2: IR <- MBR
T3: PC <- PC + 1          ; PC now points to instruction after CALL
T4: Decode: CALL instruction
T5: SP <- SP - 1          ; Decrement stack pointer
T6: M[SP] <- PC           ; Save return address on stack
T7: PC <- IR[address]     ; Jump to subroutine
```

**Compact RTL:**
```
M[--SP] <- PC             ; Push return address
PC <- IR[address]         ; Jump to subroutine
```

**Stack diagram for CALL:**
```
Before CALL:                After CALL:
+-------------------+       +-------------------+
|   (free stack)    |       |   (free stack)    |
+-------------------+       +-------------------+
|                   |       | return address    | <-- SP
|   (stack data)    |       +-------------------+
+-------------------+       |   (stack data)    |
| <- SP (old)       |       +-------------------+
+-------------------+
```

#### 8.2 RET (Return from Subroutine)

**Instruction:** `RET`
**Operation:** Pop the return address from the stack back into the PC.

```
; Full RTL:
T0: MAR <- PC
T1: MBR <- M[MAR]
T2: IR <- MBR
T3: PC <- PC + 1          ; (will be overridden)
T4: Decode: RET instruction
T5: PC <- M[SP]           ; Load return address from stack
T6: SP <- SP + 1          ; Pop stack
```

**Compact RTL:**
```
PC <- M[SP++]             ; Pop return address into PC
```

#### 8.3 CALL with Parameter Passing

**Instructions can pass parameters via registers or stack.**

**Register-based calling convention:**
```
; Before CALL:
LOAD R1, #param1         ; Parameter 1 in R1
LOAD R2, #param2         ; Parameter 2 in R2
CALL subroutine

; Subroutine uses R1, R2 as parameters
```

**Stack-based calling convention:**
```
; Push parameters in reverse order
PUSH R3                  ; Push parameter 2
PUSH R2                  ; Push parameter 1
CALL subroutine

; Subroutine accesses parameters as:
; M[SP+2] = param1
; M[SP+4] = param2 (assuming 32-bit words)
; Return value often left in R0 or on stack
```

### 9. Micro-operations

A **micro-operation (micro-op)** is the smallest indivisible operation performed by the CPU in one clock cycle. Complex instructions are broken down into sequences of micro-operations.

**Characteristics of micro-operations:**
- Each micro-operation completes in one clock cycle.
- Multiple micro-operations can occur in parallel if they use different hardware resources.
- The control unit sequences micro-operations based on the instruction.

#### 9.1 Types of Micro-operations

| Category | Examples |
|----------|----------|
| Data transfer | MAR <- PC, IR <- MBR, R1 <- R2 |
| Arithmetic | ADD, SUB, INC, DEC |
| Logic | AND, OR, XOR, NOT |
| Shift | SHL, SHR, ROL, ROR |
| Memory access | MemRead, MemWrite |
| I/O access | I/ORead, I/OWrite |
| Control | PC <- IR[addr], IF (Z=1) THEN PC <- X |

#### 9.2 Decomposing Instructions into Micro-operations

**Example: `LOAD R1, [R2 + 100]` (Indexed with displacement)**

This complex instruction breaks down into micro-operations:

```
; Fetch cycle (always 4 micro-ops)
uop1:  MAR <- PC
uop2:  MBR <- M[MAR]
uop3:  IR <- MBR
uop4:  PC <- PC + 1

; Decode (1 micro-op)
uop5:  Decode instruction

; Execute cycle
uop6:  Temp <- R2          ; Read base register
uop7:  Temp <- Temp + 100  ; Add displacement (EA calculated)
uop8:  MAR <- Temp         ; Set address for memory read
uop9:  MBR <- M[MAR]       ; Read from memory
uop10: R1 <- MBR           ; Write to destination register
```

#### 9.3 Micro-operation Table for Common Instructions

| Instruction | Micro-operation Sequence |
|-------------|------------------------|
| LOAD Rd, X | MAR <- IR[address]; MBR <- M[MAR]; Rd <- MBR |
| LOAD Rd, [Rs] | MAR <- Rs; MBR <- M[MAR]; Rd <- MBR |
| STORE Rs, X | MAR <- IR[address]; MBR <- Rs; M[MAR] <- MBR |
| ADD Rd, Rs | ALU_A <- Rd; ALU_B <- Rs; ALU_Out <- ALU_A + ALU_B; Rd <- ALU_Out; PSW <- flags |
| SUB Rd, Rs | ALU_A <- Rd; ALU_B <- Rs; ALU_Out <- ALU_A - ALU_B; Rd <- ALU_Out; PSW <- flags |
| JUMP X | PC <- IR[address] |
| JZ X | IF (PSW.Z == 1) THEN PC <- IR[address] |
| PUSH Rs | SP <- SP - 1; M[SP] <- Rs |
| POP Rd | Rd <- M[SP]; SP <- SP + 1 |
| CALL X | SP <- SP - 1; M[SP] <- PC; PC <- IR[addr] |
| RET | PC <- M[SP]; SP <- SP + 1 |

### 10. Worked Examples: Translating Assembly to RTL

#### Example 1: Simple Arithmetic Sequence

**Assembly:**
```asm
LOAD R1, #5        ; R1 = 5
LOAD R2, #3        ; R2 = 3
ADD R1, R2         ; R1 = R1 + R2
STORE R1, 1000     ; M[1000] = R1
```

**RTL translation:**
```
; LOAD R1, #5
R1 <- 5

; LOAD R2, #3
R2 <- 3

; ADD R1, R2
R1 <- R1 + R2      ; R1 = 5 + 3 = 8

; STORE R1, 1000
M[1000] <- R1      ; M[1000] = 8
```

**Final state:** R1=8, R2=3, M[1000]=8

#### Example 2: Array Access with Indexed Addressing

**Assembly:**
```asm
; R1 = base address of array (1000)
; R2 = index (8, meaning 3rd element, 2*4=8)
LOAD R3, [R1 + R2] ; R3 = M[R1 + R2]
ADD R3, R3, #1     ; R3 = R3 + 1
STORE R3, [R1 + R2] ; M[R1 + R2] = R3
```

**RTL translation:**
```
; LOAD R3, [R1 + R2]
Temp <- R1 + R2             ; EA = 1000 + 8 = 1008
R3 <- M[Temp]               ; R3 = M[1008]

; ADD R3, R3, #1
R3 <- R3 + 1                ; R3 = M[1008] + 1

; STORE R3, [R1 + R2]
Temp <- R1 + R2             ; EA = 1000 + 8 = 1008
M[Temp] <- R3               ; M[1008] = R3
```

#### Example 3: Conditional Execution

**Assembly:**
```asm
LOAD R1, 2000      ; R1 = M[2000]
CMP R1, #0         ; Compare R1 with 0
JNZ NOT_ZERO       ; If R1 != 0, jump to NOT_ZERO
LOAD R1, #1        ; R1 = 1 (if R1 was 0)
JUMP DONE          ; Skip the else part
NOT_ZERO:
MUL R1, R1, #2     ; R1 = R1 * 2 (if R1 was not 0)
DONE:
STORE R1, 2000     ; M[2000] = R1
```

**RTL translation:**
```
; LOAD R1, 2000
R1 <- M[2000]

; CMP R1, #0
Temp <- R1 - 0
PSW.Z <- (Temp == 0)
PSW.S <- (Temp < 0)

; JNZ NOT_ZERO
IF (PSW.Z == 0) THEN PC <- address_of_NOT_ZERO

; If Z=1 (R1 was 0):
R1 <- 1

; JUMP DONE
PC <- address_of_DONE

; NOT_ZERO:
R1 <- R1 * 2

; DONE:
M[2000] <- R1
```

**Execution trace:**
```
Case 1: M[2000] = 0
R1 = 0
PSW.Z = 1 (since R1 - 0 = 0)
JNZ not taken (Z=1)
R1 = 1 (LOAD #1 executed)
M[2000] = 1

Case 2: M[2000] = 5
R1 = 5
PSW.Z = 0 (since R1 - 0 = 5 != 0)
JNZ taken (Z=0) -> jump to NOT_ZERO
R1 = 5 * 2 = 10
M[2000] = 10
```

#### Example 4: Loop with Decrement and Branch

**Assembly:**
```asm
; R1 = loop count (10)
; R2 = base address of array (1000)
; R3 = sum (initially 0)

LOAD R1, #10       ; R1 = 10
LOAD R2, #1000     ; R2 = 1000
LOAD R3, #0        ; R3 = 0
LOOP:
LOAD R4, [R2]      ; R4 = M[R2] (current array element)
ADD R3, R3, R4     ; R3 = R3 + R4 (accumulate)
ADD R2, R2, #4     ; R2 = R2 + 4 (next element)
DEC R1             ; R1 = R1 - 1 (decrement count)
JNZ LOOP           ; if R1 != 0, loop
STORE R3, 2000     ; M[2000] = sum
```

**RTL translation:**
```
; LOAD R1, #10
R1 <- 10

; LOAD R2, #1000
R2 <- 1000

; LOAD R3, #0
R3 <- 0

; LOOP label

; LOAD R4, [R2]
R4 <- M[R2]

; ADD R3, R3, R4
R3 <- R3 + R4

; ADD R2, R2, #4
R2 <- R2 + 4

; DEC R1
R1 <- R1 - 1
PSW.Z <- (R1 == 0)

; JNZ LOOP
IF (PSW.Z == 0) THEN PC <- address_of_LOOP

; STORE R3, 2000
M[2000] <- R3
```

**Iteration trace (R1 iterations):**
```
Iter 1: R1=10, R2=1000, R4=M[1000], R3=0+M[1000], R2=1004, R1=9, Z=0 -> loop
Iter 2: R1=9,  R2=1004, R4=M[1004], R3=sum+M[1004], R2=1008, R1=8, Z=0 -> loop
...
Iter 10: R1=1, R2=1036, R4=M[1036], R3=total, R2=1040, R1=0, Z=1 -> no jump
STORE: M[2000] = total
```

#### Example 5: Subroutine Call and Return

**Assembly:**
```asm
; Main program
LOAD R1, #10       ; R1 = 10
LOAD R2, #20       ; R2 = 20
CALL ADD_SUB       ; Call subroutine
STORE R3, 3000     ; M[3000] = result

; Subroutine
ADD_SUB:
ADD R3, R1, R2     ; R3 = R1 + R2
RET                ; Return to caller
```

**RTL translation:**
```
; LOAD R1, #10
R1 <- 10

; LOAD R2, #20
R2 <- 20

; CALL ADD_SUB
M[--SP] <- PC      ; Save return address (address of STORE instruction)
PC <- address_of_ADD_SUB

; ADD_SUB: ADD R3, R1, R2
R3 <- R1 + R2      ; R3 = 10 + 20 = 30

; RET
PC <- M[SP++]     ; Load return address, pop stack

; STORE R3, 3000
M[3000] <- R3      ; M[3000] = 30
```

### 11. RTL for Less Common Instructions

#### 11.1 SWAP (Exchange Registers)

**Instruction:** `SWAP Rd, Rs`
**Operation:** Exchange contents of Rd and Rs.

```
Temp <- Rd
Rd <- Rs
Rs <- Temp

; Note: This requires 3 micro-ops and 1 temporary register
```

#### 11.2 CLR (Clear Register)

**Instruction:** `CLR Rd`
**Operation:** Set register Rd to 0.

```
Rd <- 0
PSW.Z <- 1
PSW.S <- 0
```

#### 11.3 NOP (No Operation)

**Instruction:** `NOP`
**Operation:** Do nothing for one instruction cycle.

```
; Execute
; (No micro-operations; just consume time)
```

#### 11.4 HALT (Halt Execution)

**Instruction:** `HLT`
**Operation:** Stop the clock or enter a wait state. The CPU stops fetching and executing instructions until an external interrupt or reset occurs.

```
; Execute
Clock_Enable <- 0    ; Stop the instruction cycle
; Or: enter low-power wait state
```

### 12. Summary: Complete RTL Instruction Set Table

| Instruction | Assembly Format | RTL (Compact) |
|-------------|----------------|---------------|
| Load | `LOAD Rd, X` | `Rd <- M[X]` |
| Store | `STORE Rs, X` | `M[X] <- Rs` |
| Load Immediate | `LOAD Rd, #imm` | `Rd <- imm` |
| Move | `MOVE Rd, Rs` | `Rd <- Rs` |
| Add | `ADD Rd, Rs` | `Rd <- Rd + Rs` |
| Add Immediate | `ADDI Rd, #imm` | `Rd <- Rd + imm` |
| Subtract | `SUB Rd, Rs` | `Rd <- Rd - Rs` |
| Multiply | `MUL Rd, Rs` | `Rd <- Rd * Rs` |
| Divide | `DIV Rd, Rs` | `Rd <- Rd / Rs; HI <- Rd % Rs` |
| Increment | `INC Rd` | `Rd <- Rd + 1` |
| Decrement | `DEC Rd` | `Rd <- Rd - 1` |
| Negate | `NEG Rd` | `Rd <- -Rd` |
| Compare | `CMP Rd, Rs` | `Temp <- Rd - Rs; Update PSW` |
| AND | `AND Rd, Rs` | `Rd <- Rd AND Rs` |
| OR | `OR Rd, Rs` | `Rd <- Rd OR Rs` |
| XOR | `XOR Rd, Rs` | `Rd <- Rd XOR Rs` |
| NOT | `NOT Rd` | `Rd <- NOT Rd` |
| Shift Left | `SHL Rd, #n` | `Rd <- Rd << n` |
| Shift Right | `SHR Rd, #n` | `Rd <- Rd >> n` |
| Shift Arithmetic Right | `SAR Rd, #n` | `Rd <- Rd >>> n` |
| Rotate Left | `ROL Rd, #n` | `Rd <- Rd ROL n` |
| Rotate Right | `ROR Rd, #n` | `Rd <- Rd ROR n` |
| Jump | `JUMP X` | `PC <- X` |
| Jump if Zero | `JZ X` | `IF Z THEN PC <- X` |
| Jump if Not Zero | `JNZ X` | `IF NOT Z THEN PC <- X` |
| Jump if Carry | `JC X` | `IF C THEN PC <- X` |
| Jump if Negative | `JN X` | `IF S THEN PC <- X` |
| Call | `CALL X` | `M[--SP] <- PC; PC <- X` |
| Return | `RET` | `PC <- M[SP++]` |
| Push | `PUSH Rs` | `M[--SP] <- Rs` |
| Pop | `POP Rd` | `Rd <- M[SP++]` |
| Input | `IN Rd, Port` | `Rd <- I/O[Port]` |
| Output | `OUT Port, Rs` | `I/O[Port] <- Rs` |
| NOP | `NOP` | (no operation) |
| HALT | `HLT` | Stop execution |
| Swap | `SWAP Rd, Rs` | `Rd <-> Rs` |
| Clear | `CLR Rd` | `Rd <- 0` |

---

## Practice Problems

1. **Problem**: Write the complete RTL for the instruction `XOR R3, R4` including fetch, decode, and execute phases.
   **Answer**:
   ```
   ; Fetch
   MAR <- PC
   MBR <- M[MAR]
   IR <- MBR
   PC <- PC + 1
   ; Decode
   ; (opcode decoded as XOR, dest = R3, src = R4)
   ; Execute
   ALU_A <- R3
   ALU_B <- R4
   ALU_Out <- ALU_A XOR ALU_B
   R3 <- ALU_Out
   PSW.Z <- (R3 == 0)
   PSW.S <- R3(MSB)
   ```

2. **Problem**: Translate the following assembly code into compact RTL:
   ```asm
   LOAD R1, #100
   LOAD R2, #200
   LOOP:
   LOAD R3, [R1]
   STORE R3, [R2]
   INC R1
   INC R2
   DEC R5
   JNZ LOOP
   ```
   **Answer**:
   ```
   R1 <- 100
   R2 <- 200
   LOOP:
   R3 <- M[R1]
   M[R2] <- R3
   R1 <- R1 + 1
   R2 <- R2 + 1
   R5 <- R5 - 1
   IF (Z == 0) THEN PC <- LOOP
   ```

3. **Problem**: Write the micro-operation sequence for `SAR R1, #3` (arithmetic shift right by 3 positions). Assume a 32-bit register.
   **Answer**:
   ```
   uop1: Temp <- R1(31)     ; Save sign bit
   uop2: C <- R1(0)         ; LSB 0 shifted out
   uop3: R1 <- R1 >> 1      ; Shift right by 1
   uop4: R1(31) <- Temp     ; Restore sign bit (arithmetic)
   ; Repeat uop2-uop4 two more times for n=3
   uop5: C <- R1(0)
   uop6: R1 <- R1 >> 1
   uop7: R1(31) <- Temp
   uop8: C <- R1(0)
   uop9: R1 <- R1 >> 1
   uop10: R1(31) <- Temp
   ; Or in a single cycle:
   R1 <- R1 >>> 3   ; combinational barrel shifter
   C <- R1_original(2)  ; bit 2 of original R1
   ```

4. **Problem**: Show the RTL for executing `CALL 500` when the current PC = 200 and SP = 1000. Show the state of stack, PC, and SP after execution.
   **Answer**:
   ```
   ; Fetch (PC=200)
   MAR <- 200
   MBR <- M[200]     ; Instruction "CALL 500"
   IR <- MBR
   PC <- 200 + 4 = 204   ; PC now = 204 (return address)
   ; Execute
   SP <- 1000 - 1 = 999
   M[999] <- 204     ; Save return address on stack
   PC <- 500         ; Jump to subroutine
   ```
   **Final state:** PC=500, SP=999, Stack[999] = 204

5. **Problem**: Write RTL for a `MULTIPLY-AND-ACCUMULATE` instruction: `MAC Rd, Rs, Rt` which computes `Rd <- Rd + (Rs * Rt)` in a single step.
   **Answer**:
   ```
   ; Execute
   Temp <- Rs * Rt
   Rd <- Rd + Temp
   PSW <- Update flags based on Rd
   ; Note: This requires both a multiplier and an adder in the ALU,
   ; and typically takes multiple clock cycles in practice.
   ```
