# Instruction set for CPU

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 3  
**Date:** 14-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Instruction Set Architecture (ISA)

An **Instruction Set Architecture (ISA)** is the interface between a computer's hardware and its software. It defines:
- The set of instructions the processor can execute.
- The data types supported.
- The registers available to programmers.
- The addressing modes for accessing operands.
- The memory model (byte-addressable, word-addressable, etc.).
- The I/O model (memory-mapped I/O, special I/O instructions).

The ISA is the **contract** between the compiler/assembly programmer and the hardware. Different processors can implement the same ISA (e.g., Intel and AMD both implement x86).

**Two major ISA philosophies:**
- **CISC (Complex Instruction Set Computer)**: Many instructions, variable length, complex operations.
- **RISC (Reduced Instruction Set Computer)**: Few instructions, fixed length, simple operations.

### 2. Types of Instructions

Instructions in a typical ISA fall into five major categories:

#### 2.1 Data Transfer Instructions
Move data between memory, registers, and I/O devices without changing the data.

| Instruction | Meaning | Example |
|-------------|---------|---------|
| LOAD | Copy data from memory to register | `LOAD R1, 1000` |
| STORE | Copy data from register to memory | `STORE R1, 1000` |
| MOVE | Copy data between registers | `MOVE R1, R2` |
| PUSH | Push data onto stack | `PUSH R1` |
| POP | Pop data from stack | `POP R1` |
| IN | Read data from I/O port | `IN R1, PORT_A` |
| OUT | Write data to I/O port | `OUT PORT_A, R1` |

#### 2.2 Arithmetic Instructions
Perform arithmetic operations on numeric data.

| Instruction | Meaning | Example |
|-------------|---------|---------|
| ADD | Add two operands | `ADD R1, R2` (R1 = R1 + R2) |
| SUB | Subtract two operands | `SUB R1, R2` (R1 = R1 - R2) |
| MUL | Multiply two operands | `MUL R1, R2` (R1 = R1 x R2) |
| DIV | Divide two operands | `DIV R1, R2` (R1 = R1 / R2) |
| INC | Increment by 1 | `INC R1` |
| DEC | Decrement by 1 | `DEC R1` |
| NEG | Negate (two's complement) | `NEG R1` |

#### 2.3 Logical Instructions
Perform bitwise logical operations.

| Instruction | Meaning | Example |
|-------------|---------|---------|
| AND | Bitwise AND | `AND R1, R2` |
| OR | Bitwise OR | `OR R1, R2` |
| XOR | Bitwise XOR | `XOR R1, R2` |
| NOT | Bitwise complement | `NOT R1` |
| SHL | Shift left (logical) | `SHL R1, 2` |
| SHR | Shift right (logical) | `SHR R1, 2` |
| ROL | Rotate left | `ROL R1, 1` |
| ROR | Rotate right | `ROR R1, 1` |

#### 2.4 Control Transfer Instructions
Change the flow of program execution (alter the PC).

| Instruction | Meaning | Example |
|-------------|---------|---------|
| JUMP (JMP) | Unconditional branch | `JMP 2000` |
| JUMP IF ZERO (JZ) | Branch if zero flag set | `JZ 2000` |
| JUMP IF NOT ZERO (JNZ) | Branch if zero flag clear | `JNZ 2000` |
| JUMP IF CARRY (JC) | Branch if carry flag set | `JC 2000` |
| CALL | Call subroutine (save return addr) | `CALL 3000` |
| RETURN (RET) | Return from subroutine | `RET` |
| IRET | Return from interrupt | `IRET` |
| HALT | Stop execution | `HLT` |

#### 2.5 I/O Instructions
Communicate with input/output devices.

| Instruction | Meaning | Example |
|-------------|---------|---------|
| IN | Read from I/O port | `IN R1, 0x60` (read keyboard) |
| OUT | Write to I/O port | `OUT 0x378, R1` (write LPT) |
| (Memory-mapped I/O uses LOAD/STORE instead) | | |

### 3. Instruction Formats

An instruction format defines how the bits of an instruction are organized. A typical instruction contains:
- **Opcode**: Specifies the operation (ADD, LOAD, etc.).
- **Operand(s)**: Specify the data or addresses of data.

Instructions are classified by the number of address fields they contain.

#### 3.1 Zero-Address Instructions
Used in **stack-based architectures**. Operands are implicitly on the top of the stack.

Example: `ADD` -- pops top two values from stack, adds them, pushes result.

```
Format: [ OPCODE ]
         (no address field)
```

**Example:** For `c = a + b`, the assembly would be:
```
PUSH a      ; push a onto stack
PUSH b      ; push b onto stack
ADD         ; pop top two, add, push result
POP c       ; pop result into c
```

#### 3.2 One-Address Instructions
Used in **accumulator-based architectures**. One operand is implicitly the accumulator (AC).

Example: `ADD X` -- adds contents of memory location X to the accumulator.

```
Format: [ OPCODE | ADDRESS ]
         (one operand address)
```

**Example:** For `c = a + b`:
```
LOAD a      ; AC = M[a]
ADD b       ; AC = AC + M[b]
STORE c     ; M[c] = AC
```

#### 3.3 Two-Address Instructions
Used in **general register architectures**. Two operands are specified.

Example: `ADD R1, R2` -- R1 = R1 + R2 (first operand is both source and destination).

```
Format: [ OPCODE | DEST ADDR | SRC ADDR ]
```

**Example:** For `c = a + b`:
```
LOAD R1, a   ; R1 = M[a]
ADD R1, b    ; R1 = R1 + M[b] -- wait, this mixes register and memory
             ; More likely in a load-store architecture:
LOAD R1, a   ; R1 = M[a]
LOAD R2, b   ; R2 = M[b]
ADD R3, R1, R2 ; R3 = R1 + R2 (three-address style)
             ; In two-address style:
MOVE R1, a   ; R1 = M[a]
ADD R1, b    ; R1 = R1 + M[b]
STORE c, R1  ; M[c] = R1
```

#### 3.4 Three-Address Instructions
Typical in RISC architectures. Three operands: two sources and one destination.

Example: `ADD R1, R2, R3` -- R1 = R2 + R3.

```
Format: [ OPCODE | DEST | SRC1 | SRC2 ]
```

**Example:** For `c = a + b`:
```
LOAD R1, a   ; R1 = M[a]
LOAD R2, b   ; R2 = M[b]
ADD R3, R1, R2 ; R3 = R1 + R2
STORE c, R3  ; M[c] = R3
```

**Comparison of instruction formats:**

| Format | Number of Addresses | Code Size | Example ISA |
|--------|-------------------|-----------|-------------|
| Zero-address | 0 | Small (implicit) | Java Virtual Machine, HP 3000 |
| One-address | 1 | Medium | Intel 8080, Motorola 6800 |
| Two-address | 2 | Medium | x86 (many instructions) |
| Three-address | 3 | Large (but fewer instructions) | MIPS, ARM, RISC-V |

### 4. RISC vs CISC Comparison

| Feature | RISC (Reduced Instruction Set Computer) | CISC (Complex Instruction Set Computer) |
|---------|----------------------------------------|----------------------------------------|
| **Instruction Count** | Few (< 100) | Many (> 200) |
| **Instruction Length** | Fixed (usually 32 bits) | Variable (1 to 15+ bytes) |
| **Instruction Format** | Simple, regular | Complex, many formats |
| **Addressing Modes** | Few (1-3) | Many (5-20+) |
| **Operands** | Register-to-register (load-store) | Register and memory (mem-to-mem) |
| **Execution Time** | Single cycle (pipelined) | Multiple cycles per instruction |
| **Control Unit** | Hardwired (fast) | Microprogrammed (slow) |
| **Register Count** | Many (32+ general purpose) | Few (8-16 general purpose) |
| **Compiler Friendliness** | Easy (simple, orthogonal) | Hard (many special cases) |
| **Examples** | ARM, MIPS, RISC-V, PowerPC | x86, 68000, VAX |
| **Pipelining** | Efficient (simple, uniform) | Difficult (complex dependencies) |

### 5. Stack, Accumulator, and General Register Organization

#### 5.1 Stack Organization
- All operations use the top of the stack implicitly.
- The stack pointer (SP) points to the top of the stack.
- No explicit register names in instructions.

**Advantages:** Very compact code (short instructions).
**Disadvantages:** Performance bottleneck (stack top is the only implicit operand).

#### 5.2 Accumulator Organization
- One register (the accumulator, AC) is the implicit destination and source.
- One operand is always the accumulator.

**Advantages:** Simple to implement.
**Disadvantages:** Every operation modifies AC -- extra LOAD/STORE needed to preserve values.

#### 5.3 General Register Organization
- Multiple general-purpose registers (GPRs) are available.
- Instructions explicitly name registers.
- Two main sub-categories:
  - **Register-Memory**: One operand is a register, one is in memory (e.g., x86 `ADD R1, M[X]`).
  - **Load-Store (Register-Register)**: Only LOAD/STORE access memory; all ALU operations are register-to-register (e.g., MIPS, ARM).

**Advantages:**
- Most flexible (compiler can optimize register usage).
- Best performance for modern compilers.
- Load-store architecture simplifies pipelining.

### 6. Detailed Examples

#### Example 1: ADD R1, R2
**Meaning:** Add the contents of register R2 to register R1. Result stored in R1.

**RTL:** `R1 <- R1 + R2`

**Instruction format (assume 32-bit):**
```
31    26 25   21 20   16 15    0
+--------+------+------+--------+
| 000001 | R1   | R2   | unused |
+--------+------+------+--------+
  OPCODE  DEST   SRC1
```

**Execution:**
1. Fetch instruction (memory -> IR).
2. Decode: opcode = 000001 (ADD).
3. Read R2 from register file.
4. ALU performs R1 + R2.
5. Write result back to R1.

#### Example 2: LOAD R1, 1000
**Meaning:** Load register R1 with the contents of memory address 1000.

**RTL:** `R1 <- M[1000]`

**Instruction format:**
```
31    26 25   21 20    0
+--------+------+--------+
| 000010 | R1   | 1000   |
+--------+------+--------+
  OPCODE  DEST   ADDRESS
```

**Execution:**
1. Fetch instruction.
2. Decode.
3. MAR <- 1000 (address field from IR).
4. MemRead signal.
5. MBR <- M[1000] (data from memory).
6. R1 <- MBR.

#### Example 3: STORE R1, 2000
**Meaning:** Store contents of register R1 into memory address 2000.

**RTL:** `M[2000] <- R1`

**Execution:**
1. Fetch instruction.
2. Decode.
3. MAR <- 2000.
4. MBR <- R1.
5. MemWrite signal.
6. Memory writes at address MAR with data from MBR.

#### Example 4: JUMP 3000
**Meaning:** Unconditionally transfer execution to address 3000.

**RTL:** `PC <- 3000`

**Instruction format:**
```
31    26 25    0
+--------+--------+
| 000011 | 3000   |
+--------+--------+
  OPCODE   ADDRESS
```

**Execution:**
1. Fetch instruction.
2. Decode.
3. PC <- address field from IR (3000).
4. Next fetch cycle reads from address 3000.

### 7. Instruction Encoding Example

Assume a simple 16-bit ISA with:
- 4-bit opcode (16 possible instructions).
- 12-bit address (4 KB addressable memory).
- 4 general purpose registers (R0-R3, encoded in 2 bits).

**One-address format:**
```
15 12 11 10 9  8 7     0
+------+------+---------+
| opcd | reg  | address |
+------+------+---------+
  4 bits 2 bits  8 bits (?)
```

(Actually design with consistent bit widths):

**Example instruction set encoding (16-bit fixed length):**

| Instruction | Opcode (4 bits) | Format |
|-------------|----------------|--------|
| LOAD | 0000 | `0000 R1 XXXX` (load M[X] into R1) |
| STORE | 0001 | `0001 R1 XXXX` (store R1 into M[X]) |
| ADD | 0010 | `0010 Rd Rs` (Rd = Rd + Rs) |
| SUB | 0011 | `0011 Rd Rs` (Rd = Rd - Rs) |
| JUMP | 0100 | `0100 XXXX` (PC = X) |
| JZ | 0101 | `0101 XXXX` (if Z=1, PC = X) |
| AND | 0110 | `0110 Rd Rs` (Rd = Rd AND Rs) |
| OR | 0111 | `0111 Rd Rs` (Rd = Rd OR Rs) |

---

## Practice Problems

1. **Problem**: For the expression `X = (A + B) * (C - D)`, write assembly code using (a) zero-address (stack), (b) one-address (accumulator), and (c) three-address (load-store) architectures.
   **Answer**:
   (a) Stack:
   ```
   PUSH A
   PUSH B
   ADD
   PUSH C
   PUSH D
   SUB
   MUL
   POP X
   ```
   (b) Accumulator:
   ```
   LOAD A
   ADD B
   STORE T1
   LOAD C
   SUB D
   MUL T1
   STORE X
   ```
   (c) Three-address (load-store):
   ```
   LOAD R1, A
   LOAD R2, B
   ADD R3, R1, R2
   LOAD R4, C
   LOAD R5, D
   SUB R6, R4, R5
   MUL R7, R3, R6
   STORE X, R7
   ```

2. **Problem**: Explain why three-address instructions often result in shorter programs (fewer total instructions) than one-address instructions, even though each instruction is longer.
   **Answer**: Three-address instructions can express complex operations directly (e.g., `ADD R1, R2, R3` performs a complete operation). In one-address architectures, temporary results must be stored to and loaded from memory, requiring additional LOAD and STORE instructions. The total number of instructions is fewer in three-address format, even though each instruction has more bits.

3. **Problem**: What is the primary advantage of a load-store architecture over a register-memory architecture?
   **Answer**: In a load-store architecture, only LOAD and STORE instructions access memory; all ALU operations work on registers. This simplifies instruction decoding, pipelining, and execution (uniform instruction length and timing). It also allows the control unit to be simpler and faster. The trade-off is that more instructions may be needed (extra LOAD/STORE) compared to register-memory architectures where ALU instructions can directly access memory.

4. **Problem**: A CPU has 16 registers, 64 instructions, and can address 32 KB of memory. What is the minimum instruction length if all instructions are fixed-length and use three-address format (Rd, Rs1, Rs2)?
   **Answer**: Registers: 16 => 4 bits each. Three registers => 12 bits. Instructions: 64 => 6 bits for opcode. Total: 6 + 4 + 4 + 4 = 18 bits. Minimum fixed instruction length is 18 bits (rounded to 24 bits, or 3 bytes, for byte alignment).

5. **Problem**: Compare the execution of `ADD M[X], M[Y]` (memory-to-memory add) in a CISC ISA versus the equivalent in a RISC load-store ISA. Which is faster and why?
   **Answer**: In CISC, a single instruction `ADD X, Y` might fetch both operands from memory, add them, and store the result, taking many cycles but only one instruction fetch. In RISC, the equivalent requires `LOAD R1, X`, `LOAD R2, Y`, `ADD R3, R1, R2`, `STORE X, R3` -- four instructions. However, the RISC version may execute faster overall due to simpler hardware, pipelining (each instruction takes one clock cycle ideally), and the ability of compilers to optimize register usage, eliminating redundant loads/stores.
