# Architecture of a CPU registers

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 4  
**Date:** 14-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to CPU Registers

Registers are small, high-speed storage locations inside the CPU. They are the fastest type of memory in the computer memory hierarchy (faster than L1 cache, much faster than RAM). Registers are used to hold:
- Instructions being executed
- Memory addresses being accessed
- Data being processed
- Status information about the CPU

**Key properties of registers:**
- Located inside the CPU (part of the processor chip).
- Accessed by the control unit via dedicated internal buses (not the system bus).
- Typical sizes: 8-bit, 16-bit, 32-bit, or 64-bit (matching the CPU word size).
- Access time: typically 0.5 - 1 clock cycle (nanoseconds).
- Number of registers varies by architecture: x86 has ~16 GPRs, ARM has 16-31, RISC-V has 32.

### 2. Classification of Registers

Registers are broadly classified into two categories:

1. **Programmer-Visible Registers**: Can be accessed (read/written) by the programmer or compiler through instructions.
2. **Control and Status Registers**: Used internally by the CPU control unit; not directly accessible by programmers (though some may be read under special circumstances).

### 3. Programmer-Visible Registers

These are registers that the instruction set architecture (ISA) makes available to the programmer. They are used to hold data and addresses during program execution.

#### 3.1 General Purpose Registers (GPRs)
- Can hold either data or addresses (depending on the instruction).
- Used by arithmetic, logical, data transfer, and comparison instructions.
- In modern RISC architectures (ARM, MIPS, RISC-V), there are 16-32 GPRs.
- In x86, the traditional GPRs are: EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP (8 registers in 32-bit mode; extended to 16 in x86-64).

**Usage examples:**
```
ADD R1, R2, R3   ; R1 = R2 + R3  (all are GPRs)
LOAD R4, [R5]    ; R4 = M[R5]    (R5 holds address)
```

#### 3.2 Data Registers
- A subset of GPRs dedicated to holding data (not addresses).
- In x86: EAX (accumulator), EBX (base), ECX (count), EDX (data).
- Used in arithmetic and logical operations.
- In some architectures, they have special purposes:
  - EAX: accumulator for arithmetic, return value.
  - ECX: loop counter (used by LOOP instruction).
  - EDX: holds remainder after multiplication/division.

#### 3.3 Address Registers
- Dedicated or general-purpose registers used to hold memory addresses.
- Used for base addressing, indexing, and pointer operations.

**Types of address registers:**
- **Base Register**: holds the base address of a data structure or array.
- **Index Register**: holds an offset used in indexed addressing.
- **Stack Pointer (SP)**: points to the top of the system stack.
- **Frame Pointer (FP) / Base Pointer (BP)**: points to the current stack frame for subroutine calls.

**Usage examples:**
```
LOAD R1, [R2 + R3]  ; R1 = M[R2 + R3] (base R2 + index R3)
PUSH R1             ; push R1 onto stack; SP = SP - 4
```

#### 3.4 Index Registers
- Special-purpose or general-purpose registers used for indexed addressing.
- Commonly used in array traversal: the index register holds the offset, and the base register holds the starting address of the array.

**Example: Array sum loop:**
```
; Assume R2 = base address of array, R3 = index (0, 4, 8, ...)
LOAD R1, [R2 + R3]  ; load array element at index R3
ADD R4, R4, R1      ; accumulate sum
ADD R3, R3, #4      ; increment index by 4 (word size)
CMP R3, #40         ; check if we've processed 10 elements
JNE LOOP            ; repeat if not equal
```

#### 3.5 Stack Pointer (SP)
- Points to the top of the stack (a region of memory used for temporary data, function call frames, and return addresses).
- The stack grows downward in most architectures (SP decreases when data is pushed).
- SP is automatically updated by PUSH, POP, CALL, and RET instructions.

**Stack operations:**
```
PUSH R1:  SP = SP - 4; M[SP] = R1
POP R1:   R1 = M[SP]; SP = SP + 4
```

**Diagram:**
```
Before PUSH:              After PUSH R1:
+---------------+         +---------------+
|    Stack      |         |    Stack      |
+---------------+         +---------------+
|               |         |               |
|   higher addr |         |   higher addr |
+---------------+         +---------------+
|   (free)      | <-- SP  |   (free)      |
+---------------+         +---------------+
                           |   R1 (pushed) | <-- SP
                           +---------------+
```

### 4. Control and Status Registers

These registers are used by the control unit to manage instruction execution. They are not typically modified directly by arithmetic/logical instructions but are critical for CPU operation.

#### 4.1 Program Counter (PC)
- Also called Instruction Pointer (IP) in x86.
- Holds the address of the **next** instruction to be fetched.
- Automatically incremented after each instruction fetch (by the instruction length).
- Modified by jump, branch, call, and return instructions.

**Normal flow:**
```
1. CPU fetches instruction at address PC.
2. PC incremented: PC = PC + instruction_length.
3. If instruction is a JUMP, PC is set to the target address.
```

**Example:**
```
Initial: PC = 100
Step 1: Fetch instruction at 100, PC = 104 (assuming 4-byte instructions)
Step 2: Decode: it's a JUMP to 500
Step 3: PC = 500
Step 4: Fetch instruction at 500, PC = 504
```

#### 4.2 Instruction Register (IR)
- Holds the currently executing instruction (the fetched instruction).
- The control unit decodes the operation code (opcode) from the IR.
- The IR is loaded from the MBR at the end of the fetch cycle.

**IR contents after fetch:**
```
+----------------------------------------+
|   Opcode    |   Operand(s)             |
|  (e.g., ADD)|  (e.g., R1, R2, 1000)   |
+----------------------------------------+
```

#### 4.3 Memory Address Register (MAR)
- Holds the memory address for the next read or write operation.
- Connected directly to the address bus.
- Loaded by the control unit during memory access operations.

**Usage sequence:**
```
1. MAR = address (from PC, from instruction, or from register)
2. Address bus receives the contents of MAR
3. Memory read/write operation begins
```

#### 4.4 Memory Buffer Register (MBR)
- Also called Memory Data Register (MDR).
- Holds the data being transferred to or from memory.
- Connected directly to the data bus.

**Two uses:**
- **On memory read:** MBR receives data from the data bus (memory -> CPU).
- **On memory write:** MBR provides data to the data bus (CPU -> memory).

#### 4.5 Program Status Word (PSW)
- Also called Flag Register, Condition Code Register (CCR), or Status Register.
- Holds individual **condition flags** that reflect the result of the most recent arithmetic/logical operation.
- Also holds control flags that govern CPU operation.

**Common condition flags:**

| Flag | Symbol | Meaning | Set When |
|------|--------|---------|----------|
| Zero | Z | Result is zero | ALU output = 0 |
| Carry | C | Carry/borrow from MSB | Addition produces carry out; subtraction requires borrow |
| Sign/Negative | N/S | Result is negative | MSB of result = 1 |
| Overflow | V | Arithmetic overflow | Signed result exceeds representable range |
| Parity | P | Parity of result | Result has even/odd number of 1 bits |
| Auxiliary Carry | AC | Carry from bit 3 | Used in BCD arithmetic |

**Common control flags:**

| Flag | Meaning |
|------|---------|
| Interrupt Enable (I) | When set, CPU responds to interrupts; when clear, interrupts are masked |
| Direction (D) | Controls string operation direction (increment or decrement index) |
| Supervisor/User Mode | Indicates privilege level (supervisor = full access, user = restricted) |

**PSW format example (simplified 16-bit):**
```
Bit: 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |  | I| D|  |  | OV| S| Z| C|
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
                                  |  |  |  |  |   |  |
                                  |  |  |  |  |   |  +-> Carry
                                  |  |  |  |  |   +----> Zero
                                  |  |  |  |  +--------> Sign
                                  |  |  |  +-----------> Overflow
                                  |  |  +--------------> (unused)
                                  |  +-----------------> Direction
                                  +--------------------> Interrupt Enable
```

### 5. Register Organization Diagrams

#### 5.1 Simplified CPU Register Set

```
+---------------------------+
|      CPU (Internal)       |
|                           |
|  +---------------------+  |
|  |   Programmer-Visible |  |
|  |   Registers          |  |
|  |                     |  |
|  |  R0  = 32 bits      |  |
|  |  R1  = 32 bits      |  |
|  |  R2  = 32 bits      |  |
|  |  R3  = 32 bits      |  |
|  |  R4  = 32 bits      |  |
|  |  R5  = 32 bits      |  |
|  |  R6  = 32 bits      |  |
|  |  R7  = 32 bits      |  |
|  |  SP  = 32 bits      |  |
|  |  FP  = 32 bits      |  |
|  +---------------------+  |
|                           |
|  +---------------------+  |
|  |   Control & Status   |  |
|  |   Registers          |  |
|  |                     |  |
|  |  PC  = 32 bits      |  |
|  |  IR  = 32 bits      |  |
|  |  MAR = 32 bits      |  |
|  |  MBR = 32 bits      |  |
|  |  PSW = 16 bits      |  |
|  +---------------------+  |
|                           |
|  +---------------------+  |
|  |   Internal Bus       |  |
|  |   (connects all      |  |
|  |    registers inside  |  |
|  |    the CPU)          |  |
|  +---------------------+  |
+---------------------------+
```

#### 5.2 Data Flow Between Registers and Memory

```
                        +-----------+
                        |  Memory   |
                        |  (RAM)    |
                        +-----------+
                             |
                    Address  |  Data
                     Bus     |  Bus
                      |      |
                      v      v
                +-----+------+-----+
                |      MAR    MBR  |
                |      |        |   |
                |      v        v   |
                |  +----+   +----+  |
                |  | PC |   | IR |  |
                |  +----+   +----+  |
                |    |         |     |
                |    v         v     |
                |  +----+   +----+  |
                |  | R0 |...| R7 |  |
                |  +----+   +----+  |
                |    |         |     |
                |    +----+----+     |
                |         |          |
                |      +--+--+       |
                |      | ALU |       |
                |      +--+--+       |
                |         |          |
                |   +-----+-----+    |
                |   |    PSW    |    |
                |   +----------+    |
                |       CPU         |
                +-------------------+
```

### 6. Detailed Usage Examples for Each Register

#### Example 1: PC (Program Counter)

```
; Code sequence at addresses 100-108
100: LOAD R1, 2000    ; 4-byte instruction
104: ADD R1, R2       ; 4-byte instruction
108: STORE R1, 3000   ; 4-byte instruction
```

**PC behavior:**
- Initially PC = 100.
- Fetch: instruction at 100 loaded, PC becomes 104.
- Execute: LOAD R1, 2000.
- Fetch: instruction at 104 loaded, PC becomes 108.
- Execute: ADD R1, R2.
- Fetch: instruction at 108 loaded, PC becomes 112.
- Execute: STORE R1, 3000.
- Fetch: instruction at 112...

#### Example 2: IR (Instruction Register)

```
After fetch from address 100:
  IR = "ADD R1, R2"  (binary: 0010 0001 0010)
                      opcode=0010 (ADD)
                      dest=R1 (001)
                      src=R2 (010)

Control unit decodes IR bits:
  0010 -> selects ADD operation in ALU
  001 -> destination is register R1
  010 -> source is register R2
```

#### Example 3: MAR and MBR during LOAD

```
Instruction: LOAD R1, 2000

Step 1: MAR = 2000    (address field from instruction)
Step 2: Address bus carries 2000
Step 3: MemRead signal asserted
Step 4: Memory returns data at address 2000
Step 5: MBR = data (from data bus)
Step 6: R1 = MBR     (data transferred to register)
```

#### Example 4: MAR and MBR during STORE

```
Instruction: STORE R1, 3000

Step 1: MAR = 3000    (address field from instruction)
Step 2: MBR = R1      (data from register)
Step 3: Address bus carries 3000, Data bus carries R1 value
Step 4: MemWrite signal asserted
Step 5: Memory stores MBR data at address 3000
```

#### Example 5: PSW (Status Flags)

```
; Example showing how flags are set

LOAD R1, #5       ; R1 = 5
LOAD R2, #-5      ; R2 = -5 (two's complement: ...11111011)
ADD R3, R1, R2    ; R3 = 5 + (-5) = 0
                  ; PSW.Z = 1 (result is zero)
                  ; PSW.C = 1 (carry out)
                  ; PSW.S = 0 (result non-negative)
                  ; PSW.V = 0 (no overflow)

SUB R4, R1, R2    ; R4 = 5 - (-5) = 10
                  ; PSW.Z = 0 (result non-zero)
                  ; PSW.C = 0 (no borrow)
                  ; PSW.S = 0 (positive)
                  ; PSW.V = 0 (no overflow)

; Using flags for conditional branching
JZ SKIP           ; Jump to SKIP if Z=1 (first ADD sets Z=1)
                  ; This jump WILL be taken
```

#### Example 6: SP (Stack Pointer) in Subroutine Call

```
; Main program
100: CALL SUBROUTINE   ; address 200
104: ADD R1, R2

; Subroutine at 200
200: SUBROUTINE: PUSH R1
204: ... (subroutine body)
208: POP R1
212: RET

; SP behavior during CALL:
; Before CALL: SP = 1000
; CALL: SP = SP - 4 = 996; M[996] = 104 (return address)
; PC = 200 (jump to subroutine)

; SP behavior during RET:
; RET: R1 = M[SP]; but wait -- RET pops into PC
; Actually: PC = M[SP]; SP = SP + 4 = 1000
; Execution resumes at address 104
```

### 7. Register Sizes in Different Architectures

| Register | x86 (IA-32) | x86-64 | ARMv7 | MIPS32 | RISC-V64 |
|----------|-------------|--------|-------|--------|----------|
| GPRs | 8 (32-bit) | 16 (64-bit) | 16 (32-bit) | 32 (32-bit) | 32 (64-bit) |
| PC | 32-bit (EIP) | 64-bit (RIP) | 32-bit | 32-bit | 64-bit |
| IR | 32-bit | Variable (1-15 bytes) | 32-bit | 32-bit | 32-bit |
| MAR | 32-bit | 64-bit | 32-bit | 32-bit | 64-bit |
| MBR | 32-bit | 64-bit | 32-bit | 32-bit | 64-bit |
| PSW | 32-bit (EFLAGS) | 64-bit (RFLAGS) | 32-bit | 32-bit | 64-bit |

---

## Practice Problems

1. **Problem**: List all the registers that are involved in executing the instruction `LOAD R1, [R2]` (load M[R2] into R1) and describe the role of each.
   **Answer**: The instruction goes through fetch and execute phases:
   - **Fetch**: PC (provides address of instruction), MAR (receives PC value for memory read), MBR (receives instruction from data bus), IR (receives instruction from MBR), PC (incremented).
   - **Execute**: R2 (provides the memory address), MAR (receives R2 value), MBR (receives data from memory at that address), R1 (receives data from MBR).

2. **Problem**: After executing the instruction `ADD R1, R2`, the zero flag (Z) and sign flag (S) in the PSW are both 0. What can you conclude about the result?
   **Answer**: Z = 0 means the result is non-zero. S = 0 means the result is non-negative (MSB = 0). Therefore, the result in R1 is a positive non-zero number.

3. **Problem**: If the PC register is 16 bits wide, what is the maximum addressable memory (in bytes) if the architecture is byte-addressable?
   **Answer**: A 16-bit PC can hold 2^16 = 65,536 distinct addresses. For a byte-addressable architecture, this means 64 KB of addressable memory. (Note: some architectures use the PC differently, e.g., if it points to words instead of bytes, the addressable space changes.)

4. **Problem**: Explain why the MAR and MBR registers are needed instead of connecting the address/data buses directly to registers or the ALU.
   **Answer**: The system bus is external to the CPU and operates at a slower speed than the CPU's internal components. MAR and MBR serve as **buffers** that isolate the fast internal CPU components from the slower external bus. This allows the CPU to continue internal operations while a memory access is in progress (the MAR/MBR hold the address/data externally). Without these buffers, the CPU would be forced to wait idle during every memory access.

5. **Problem**: For the x86 EFLAGS register, name three condition flags and three control flags. Give an example instruction that sets each condition flag.
   **Answer**:
   - Condition flags: ZF (Zero) set by `CMP EAX, EBX` when EAX = EBX; CF (Carry) set by `ADD` when unsigned overflow occurs; SF (Sign) set by `SUB` when result is negative.
   - Control flags: IF (Interrupt Flag) -- set/cleared by `STI`/`CLI`; DF (Direction Flag) -- set/cleared by `STD`/`CLD`; IOPL (I/O Privilege Level) -- modified by `POPF`.
