# Addressing modes

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 7  
**Date:** 22-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to Addressing Modes

An **addressing mode** specifies how an instruction identifies the location of its operands. The addressing mode determines:

- Where the operand is located (in a register, in memory, or within the instruction itself).
- How to compute the effective address (the actual memory address of the operand).
- Whether the operand is the data itself or an address pointing to the data.

**Why multiple addressing modes?**
- Different modes provide flexibility for different programming scenarios.
- They allow efficient access to data structures (arrays, records, pointers).
- They reduce code size by allowing complex operand access in a single instruction.

**Effective Address (EA):** The actual memory address of the operand after the addressing mode computation is applied.

### 2. Immediate Addressing

**Description:** The operand value is directly embedded in the instruction itself. No memory or register access is needed for the operand.

**Instruction format:**
```
+----------+----------------+
| Opcode   | Operand Value  |
+----------+----------------+
```

**RTL:** `R1 <- Value` (where Value is the immediate field)

**Assembly example:** `LOAD R1, #25`

(The `#` prefix denotes immediate mode in most assemblers.)

**Execution:**
1. Fetch instruction (instruction contains the value 25).
2. Execute: R1 <- 25 (value from instruction, not from memory).

**Usage:**
- Loading constants into registers.
- Setting initial values.
- Providing immediate offsets or masks.

**Advantages:**
- Very fast (no additional memory access).
- No memory address calculation needed.

**Disadvantages:**
- The constant value is fixed at compile time and cannot be changed at runtime.
- Limited by the number of bits allocated in the instruction format.

**Example:**
```asm
LOAD R1, #100        ; R1 = 100
ADD R1, #1           ; R1 = R1 + 1 = 101
```

### 3. Direct Addressing

**Description:** The instruction contains the memory address of the operand. Also called **absolute addressing**.

**Instruction format:**
```
+----------+----------------+
| Opcode   | Address X      |
+----------+----------------+
```

**RTL:** `R1 <- M[X]`

**Assembly example:** `LOAD R1, 2000`

**Execution:**
1. Fetch instruction.
2. EA = address field of instruction (2000).
3. MAR <- 2000.
4. MemRead; MBR <- M[2000].
5. R1 <- MBR.

**Usage:**
- Accessing global variables whose addresses are known at compile time.
- Simple data access.

**Advantages:**
- Simple to understand and implement.
- Only one memory access (for the operand) after the instruction is fetched.

**Disadvantages:**
- The address is fixed; the same variable/array must always be at the same address.
- Limited address range (limited by address field bits in instruction).
- Not suitable for relocatable code.

**Example:**
```asm
LOAD R1, 2000        ; R1 = M[2000]
STORE R1, 3000       ; M[3000] = R1
```

### 4. Indirect Addressing

**Description:** The instruction contains the address of a memory location that holds the actual address of the operand (pointer). This is a pointer-to-pointer mechanism.

**Instruction format:**
```
+----------+----------------+
| Opcode   | Address X      |
+----------+----------------+
```

**RTL:** `R1 <- M[M[X]]` (two levels of memory access)

**Assembly example:** `LOAD R1, [2000]`

(Brackets denote indirection.)

**Execution:**
1. Fetch instruction.
2. MAR <- address field of instruction (2000).
3. MemRead; MBR <- M[2000] (this is the pointer value).
4. MAR <- MBR (the pointer becomes the new address).
5. MemRead; MBR <- M[MAR] (the actual operand).
6. R1 <- MBR.

**Data flow diagram:**
```
Instruction: LOAD R1, [2000]

Memory[2000] = 5000 (pointer)
Memory[5000] = 42   (actual data)

Step 1: MAR = 2000
Step 2: MBR = M[2000] = 5000
Step 3: MAR = MBR = 5000
Step 4: MBR = M[5000] = 42
Step 5: R1 = 42
```

**Usage:**
- Implementing pointers and linked lists.
- Dynamic data structures where addresses are computed at runtime.
- Jump tables (array of function pointers).

**Advantages:**
- Allows dynamic address computation (the pointer value can change at runtime).
- Useful for implementing pointers, references, and indirection.
- Can access a larger address space if the pointer is wider than the address field.

**Disadvantages:**
- Slower (requires two memory accesses instead of one).
- More complex hardware implementation.

### 5. Register Addressing

**Description:** The operand is located in a register. The instruction specifies a register number (not a memory address).

**Instruction format:**
```
+----------+-------------+
| Opcode   | Register #  |
+----------+-------------+
```

**RTL:** `R1 <- R2`

**Assembly example:** `MOVE R1, R2`

**Execution:**
1. Fetch instruction.
2. Decode: source = R2, destination = R1.
3. Register file provides R2 value.
4. R1 <- R2.

**Usage:**
- Most common mode for ALU operations.
- Data manipulation within the CPU (no memory access).

**Advantages:**
- Very fast (no memory access for the operand).
- Small address field (only need log2(N) bits for N registers).
- Instructions are short (fewer bits needed).

**Disadvantages:**
- Limited number of registers (cannot store large data sets in registers).
- Data must be loaded from memory into registers before use.

**Example:**
```asm
ADD R1, R2           ; R1 = R1 + R2 (register operands)
MOVE R3, R4          ; R3 = R4
```

### 6. Register Indirect Addressing

**Description:** The instruction specifies a register that holds the memory address of the operand. Similar to indirect addressing, but the pointer is in a register instead of memory.

**Instruction format:**
```
+----------+-------------+
| Opcode   | Register #  |
+----------+-------------+
```

**RTL:** `R1 <- M[R2]`

**Assembly example:** `LOAD R1, [R2]`

**Execution:**
1. Fetch instruction.
2. Decode: base register = R2.
3. EA = contents of R2.
4. MAR <- R2.
5. MemRead; MBR <- M[MAR].
6. R1 <- MBR.

**Usage:**
- Accessing data via pointers (the pointer is in a register).
- Traversing linked lists or dynamic arrays.
- Parameter passing (pass address of data in register).

**Advantages:**
- Fast (only one memory access after the instruction fetch).
- The address can be computed at runtime (dynamically).
- Supports pointer-based data structures efficiently.

**Disadvantages:**
- Still requires one memory access for the operand.
- Register must be loaded with address beforehand.

**Example:**
```asm
; Assume R2 = 2000 (pointer to data)
LOAD R1, [R2]        ; R1 = M[R2] = M[2000]
STORE R1, [R3]       ; M[R3] = R1
```

### 7. Displacement Addressing

**Description:** The effective address is computed as the sum of a **base register** value and a **displacement** (offset) that is part of the instruction. Also called base+offset addressing.

**Instruction format:**
```
+----------+-------------+----------------+
| Opcode   | Base Reg    | Displacement   |
+----------+-------------+----------------+
```

**RTL:** `R1 <- M[R2 + disp]`

**Assembly example:** `LOAD R1, 10[R2]`

**Execution:**
1. Fetch instruction.
2. Decode: base register = R2, displacement = 10.
3. EA = R2 + 10.
4. MAR <- EA.
5. MemRead; MBR <- M[MAR].
6. R1 <- MBR.

**Usage:**
- Accessing fields of a structure/record at a known offset from a base pointer.
- Accessing array elements where the base is the array start address.
- Stack frame access (base pointer + offset to local variables).

**Advantages:**
- Flexible (same base register can access many locations with different displacements).
- Supports data structures (records, arrays) efficiently.
- Supports relocatable code.

**Disadvantages:**
- Requires an adder for address computation (base + offset).
- Displacement range is limited by the bits allocated in the instruction.

**Example:**
```asm
; Assume R2 = address of a structure
; Structure has fields at offsets 0, 4, 8
LOAD R1, 0[R2]       ; R1 = M[R2 + 0] (field 1)
LOAD R3, 4[R2]       ; R3 = M[R2 + 4] (field 2)
LOAD R4, 8[R2]       ; R4 = M[R2 + 8] (field 3)
```

### 8. Indexed Addressing

**Description:** The effective address is computed as the sum of a **base address** and an **index register** content. The index register is typically incremented or decremented for array traversal.

**Instruction format:**
```
+----------+-------------+-------------+
| Opcode   | Base Reg    | Index Reg   |
+----------+-------------+-------------+
```

**RTL:** `R1 <- M[Rbase + Rindex]`

**Assembly example:** `LOAD R1, [R2 + R3]`

**Execution:**
1. Fetch instruction.
2. Decode: base = R2, index = R3.
3. EA = R2 + R3.
4. MAR <- EA.
5. MemRead; MBR <- M[MAR].
6. R1 <- MBR.

**Usage:**
- Array traversal: base is array start address, index is element offset.
- Table lookup: index selects the table entry.

**Example: Array sum**
```asm
; R2 = base address of array (1000)
; R3 = index (initially 0)
LOOP:
LOAD R1, [R2 + R3]   ; Load array element at index R3
ADD R4, R4, R1       ; Accumulate sum
ADD R3, R3, #4       ; Increment index by 4 (word size)
CMP R3, #40          ; 10 elements x 4 bytes = 40
JLT LOOP             ; Continue if R3 < 40
```

**Auto-indexing variants:**
- **Post-index:** Access at EA = R2+R3, then R3 = R3 + offset.
- **Pre-index:** EA = R2+R3+disp, then R3 = R3 + disp; access at new EA.

### 9. Relative Addressing

**Description:** The effective address is computed as the sum of the **Program Counter (PC)** and a **displacement** from the instruction. This is displacement addressing where the base register is the PC.

**RTL:** `R1 <- M[PC + disp]`

**Assembly example:** `LOAD R1, label` (assembler computes disp from current PC)

**Execution:**
1. Fetch instruction.
2. Decode: displacement = signed offset.
3. EA = PC + displacement.
4. MAR <- EA.
5. MemRead; MBR <- M[MAR].
6. R1 <- MBR.

**Usage:**
- Position-independent code (code that can run at any memory address).
- Relative jumps and branches (most branch instructions use PC-relative addressing).
- Accessing nearby data without hard-coded addresses.

**Important note for branches:** The PC value used in EA calculation is the **updated PC** (after increment during fetch), not the original PC.

**Example:**
```asm
; Code:
100: LOAD R1, 2000    ; (4 bytes)
104: JMP +4           ; PC-relative jump: PC = 104 + 4 = 108
108: ADD R1, R2
```

**Calculation:**
For a PC-relative branch at address X with displacement D:
- New PC = X + instruction_length + D
- (Because PC has already been incremented past the current instruction)

### 10. Stack Addressing

**Description:** The operand is implicitly on the top of the stack. The stack pointer (SP) points to the top of the stack. No explicit address or register is specified in the instruction.

**RTL:** (implicitly uses SP and stack memory)

**Assembly examples:** `PUSH R1`, `POP R1`, `ADD`

**Execution for PUSH:**
1. SP <- SP - 1 (or -4, depending on word size).
2. M[SP] <- R1.

**Execution for POP:**
1. R1 <- M[SP].
2. SP <- SP + 1.

**Execution for ADD (stack-based):**
1. Operand1 <- M[SP]; SP <- SP + 1.
2. Operand2 <- M[SP]; SP <- SP + 1.
3. Result <- Operand1 + Operand2.
4. SP <- SP - 1; M[SP] <- Result.

**Usage:**
- Expression evaluation (postfix/Reverse Polish Notation).
- Subroutine call/return (saving/restoring return addresses and registers).
- Local variable storage.
- Interrupt handling (saving CPU state).

**Advantages:**
- Very compact code (no address fields needed).
- Natural for expression evaluation.
- Supports recursion.

**Disadvantages:**
- Stack top is the only accessible operand (for stack machines).
- Not efficient for random data access.

**Expression evaluation example (postfix):**
```
Expression: (A + B) * C

Postfix: A B + C *

PUSH A
PUSH B
ADD        ; pop A, pop B, push A+B
PUSH C
MUL        ; pop (A+B), pop C, push (A+B)*C
POP result ; store final result
```

### 11. Summary Table: Addressing Modes

| Addressing Mode | Effective Address (EA) | Memory Accesses | RTL Example | Typical Use |
|----------------|----------------------|-----------------|-------------|-------------|
| Immediate | N/A (operand in instr) | 0 | `R1 <- #25` | Constants |
| Direct | EA = address field | 1 | `R1 <- M[2000]` | Global variables |
| Indirect | EA = M[address field] | 2 | `R1 <- M[M[2000]]` | Pointers |
| Register | N/A (operand in register) | 0 | `R1 <- R2` | ALU operations |
| Register Indirect | EA = register | 1 | `R1 <- M[R2]` | Pointer dereference |
| Displacement | EA = base + disp | 1 | `R1 <- M[R2+10]` | Struct fields |
| Indexed | EA = base + index | 1 | `R1 <- M[R2+R3]` | Arrays |
| Relative | EA = PC + disp | 1 | `R1 <- M[PC+100]` | Position-independent |
| Stack | EA = SP (implied) | 0-1 | `PUSH R1` | Expression eval |

### 12. Comparison Table: Pros and Cons

| Mode | Speed | Code Size | Flexibility | Complexity |
|------|-------|-----------|-------------|------------|
| Immediate | Fastest | Small | Low (constant only) | Simplest |
| Direct | Fast | Medium | Low (fixed address) | Simple |
| Indirect | Slow (2 mem accesses) | Medium | High (dynamic addr) | Complex |
| Register | Fastest | Smallest | Medium | Simple |
| Register Indirect | Fast | Small | High | Medium |
| Displacement | Fast | Medium | High | Medium |
| Indexed | Fast | Large | Very High | Complex |
| Relative | Fast | Small | Medium | Medium |
| Stack | Fast | Smallest | Low (implicit) | Simple |

### 13. RTL Examples for Each Mode

Assume we want to load register R1 with a value using each mode:

| Mode | Assembly | RTL |
|------|----------|-----|
| Immediate | `LOAD R1, #100` | `R1 <- 100` |
| Direct | `LOAD R1, 2000` | `R1 <- M[2000]` |
| Indirect | `LOAD R1, [2000]` | `R1 <- M[M[2000]]` |
| Register | `MOVE R1, R2` | `R1 <- R2` |
| Register Indirect | `LOAD R1, [R2]` | `R1 <- M[R2]` |
| Displacement | `LOAD R1, 10[R2]` | `R1 <- M[R2 + 10]` |
| Indexed | `LOAD R1, [R2+R3]` | `R1 <- M[R2 + R3]` |
| Relative | `LOAD R1, label` | `R1 <- M[PC + disp]` |
| Stack | `PUSH R1` | `M[--SP] <- R1` |

### 14. Practical Programming Examples

#### Example 1: Summing an Array (Indexed + Register Indirect)

```asm
; R1 = base address of array
; R2 = index (0, 4, 8, 12, ...)
; R3 = sum (accumulator)
; R4 = element count

LOAD R1, #1000       ; Immediate: base address
LOAD R2, #0          ; Immediate: index = 0
LOAD R3, #0          ; Immediate: sum = 0
LOAD R4, #10         ; Immediate: count = 10

LOOP:
LOAD R5, [R1 + R2]   ; Indexed: array element
ADD R3, R3, R5       ; Register: accumulate
ADD R2, R2, #4       ; Immediate: advance to next element
SUB R4, R4, #1       ; Immediate: decrement count
JNZ LOOP             ; Relative: conditional branch
```

#### Example 2: Linked List Traversal (Register Indirect + Displacement)

```asm
; R1 = pointer to current node (initially head)
; Node structure: offset 0 = data, offset 4 = next pointer

LOOP:
LOAD R2, 0[R1]       ; Displacement: R2 = node.data
ADD R3, R3, R2       ; Register: accumulate sum
LOAD R1, 4[R1]       ; Displacement: R1 = node.next pointer
JNZ R1, LOOP         ; Register Indirect: if R1 != 0, continue
```

#### Example 3: Subroutine with Stack Frame (Stack + Displacement)

```asm
; Save registers on stack
PUSH R1              ; Stack: save R1
PUSH R2              ; Stack: save R2
PUSH R3              ; Stack: save R3

; Access local variables (assume SP points to locals)
LOAD R4, 0[SP]       ; Displacement: first local variable
ADD R4, R4, R5
STORE R4, 0[SP]      ; Displacement: store result back

; Restore registers
POP R3               ; Stack: restore R3
POP R2               ; Stack: restore R2
POP R1               ; Stack: restore R1
RET                  ; Stack: return (pop PC from stack)
```

---

## Practice Problems

1. **Problem**: For the instruction `LOAD R1, 1000`, explain what happens in each addressing mode (direct, indirect, register indirect) and how the effective address is computed.
   **Answer**: 
   - Direct: EA = 1000. R1 = M[1000]. One memory access for the operand.
   - Indirect: EA = M[1000]. First, read M[1000] to get the pointer value P, then EA = P. R1 = M[P]. Two memory accesses.
   - Register indirect: The 1000 is treated differently or the instruction format is wrong. For register indirect, the address would be in a register: `LOAD R1, [R2]` where R2 = 1000. EA = R2. One memory access for operand.

2. **Problem**: Write assembly code using displacement addressing to access the 5th element of an array (each element is 4 bytes) whose base address is in register R2.
   **Answer**: `LOAD R1, 16[R2]` (5th element means index 4, so offset = 4 x 4 = 16). R1 = M[R2 + 16].

3. **Problem**: Explain the difference between indexed addressing and displacement addressing. Give an example where each is most useful.
   **Answer**: 
   - Displacement addressing uses a fixed displacement (constant offset) added to a base register. Best for accessing struct fields at known offsets.
   - Indexed addressing uses a variable index register that can be incremented. Best for array traversal.
   - Often they overlap: `LOAD R1, 10[R2]` and `LOAD R1, [R2+R3]` can both be considered displacement+indexed combined.

4. **Problem**: Given the code `LOAD R1, [R2]`, where R2 = 3000 and M[3000] = 42, what is the value loaded into R1?
   **Answer**: This is register indirect addressing. EA = R2 = 3000. R1 = M[3000] = 42.

5. **Problem**: A CPU has 16 general purpose registers, 4-bit opcode, and supports 5 addressing modes. Each instruction is 16 bits. Design the instruction format for a LOAD instruction using register indirect with displacement addressing.
   **Answer**: 
   - 4 bits: opcode (LOAD)
   - 3 bits: addressing mode (5 modes need 3 bits, with 3 spare)
   - 4 bits: base register (16 registers)
   - 5 bits: displacement (signed, range -16 to +15)
   Total: 4 + 3 + 4 + 5 = 16 bits.
