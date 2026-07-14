# Case study instruction sets of some common CPUs

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 9  
**Date:** 28-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction

This lecture surveys the instruction set architectures of three major processor families: **Intel x86**, **ARM**, and **MIPS**. These represent different design philosophies and historical evolution:

- **x86 (CISC)**: Dominant in desktop and server computing. Complex, variable-length instructions with a long backward-compatible history.
- **ARM (RISC)**: Dominant in mobile and embedded systems. Clean RISC design with recent 64-bit extensions.
- **MIPS (RISC)**: Foundational RISC architecture influential in academia and embedded systems. Simple, elegant design.

### 2. Intel x86 Architecture

#### 2.1 Overview

- **Type:** CISC (Complex Instruction Set Computer).
- **First introduced:** 1978 (8086), evolved through 80286, 386, 486, Pentium, Core, and Xeon.
- **Bit width:** 16-bit (8086), 32-bit (IA-32, 80386 onwards), 64-bit (x86-64/AMD64, introduced by AMD in 2003).
- **Instruction length:** Variable (1 to 15 bytes).
- **Key characteristic:** Backward compatibility (modern x86 CPUs can still run 8086 code in real mode).

#### 2.2 Register Set (x86-64 mode)

**General Purpose Registers (16 registers, 64-bit each):**

| Register | 64-bit | 32-bit | 16-bit | 8-bit | Purpose/Special Role |
|----------|--------|--------|--------|-------|---------------------|
| RAX | RAX | EAX | AX | AL/AH | Accumulator, return value |
| RBX | RBX | EBX | BX | BL/BH | Base register |
| RCX | RCX | ECX | CX | CL/CH | Counter (loop/string ops) |
| RDX | RDX | EDX | DX | DL/DH | Data register, I/O |
| RSI | RSI | ESI | SI | SIL | Source index (string ops) |
| RDI | RDI | EDI | DI | DIL | Destination index (string ops) |
| RBP | RBP | EBP | BP | BPL | Base/Frame pointer |
| RSP | RSP | ESP | SP | SPL | Stack pointer |
| R8-R15 | R8-R15 | R8D-R15D | R8W-R15W | R8B-R15B | Extended registers (x86-64) |

**Special-purpose registers:**
- **RIP**: Instruction Pointer (Program Counter), 64-bit.
- **RFLAGS**: Status and control flags register, 64-bit (lower 32 bits are EFLAGS).

**RFLAGS register format:**
```
Bit: 31 ... 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0
    +--...--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |       |ID|VIP|VIF|AC|VM|RF| 0|NT|IOPL|OF|DF|IF|TF|SF|ZF| 0|AF| 0|PF| 1|CF|
    +--...--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
                           |  |  |  |  |  |   |  |  |  |  |  |  |  |  |  |  |
                           |  |  |  |  |  |   |  |  |  |  |  |  |  |  |  |  +-> CF (Carry)
                           |  |  |  |  |  |   |  |  |  |  |  |  |  |  |  +----> PF (Parity)
                           |  |  |  |  |  |   |  |  |  |  |  |  |  |  +-------> AF (Aux Carry)
                           |  |  |  |  |  |   |  |  |  |  |  |  |  +----------> ZF (Zero)
                           |  |  |  |  |  |   |  |  |  |  |  |  +-------------> SF (Sign)
                           |  |  |  |  |  |   |  |  |  |  |  +----------------> TF (Trap)
                           |  |  |  |  |  |   |  |  |  |  +-------------------> IF (Interrupt)
                           |  |  |  |  |  |   |  |  |  +----------------------> DF (Direction)
                           |  |  |  |  |  |   |  |  +-------------------------> OF (Overflow)
                           |  |  |  |  |  |   |  +----------------------------> IOPL (I/O Privi)
                           |  |  |  |  |  |   +-------------------------------> NT (Nested Task)
                           |  |  |  |  |  +-----------------------------------> RF (Resume)
                           |  |  |  |  +--------------------------------------> VM (Virtual 8086)
                           |  |  |  +-----------------------------------------> AC (Alignment Check)
                           |  |  +--------------------------------------------> VIF (Virtual Int)
                           |  +-----------------------------------------------> VIP (Virtual Int Pending)
                           +--------------------------------------------------> ID (ID Flag)
```

#### 2.3 Instruction Format (x86)

x86 instructions have a complex, variable-length format:

```
[Prefixes] [Opcode] [ModR/M] [SIB] [Displacement] [Immediate]

Prefixes: 0-4 bytes (lock, rep, segment override, operand size, address size)
Opcode: 1-3 bytes (primary opcode, optional opcode extension)
ModR/M: 1 byte (addressing mode, register, register/memory)
SIB: 1 byte (Scale-Index-Base, for indexed addressing)
Displacement: 0, 1, 2, or 4 bytes (offset)
Immediate: 0, 1, 2, or 4 bytes (constant value)
```

**Example: ADD EAX, EBX (32-bit register addition)**
- Encoding: `01 D8` (2 bytes)
- Opcode `01` = ADD r/m, r (register to register/memory)
- ModR/M byte `D8` = mod=11 (register mode), reg=011 (EBX), r/m=000 (EAX)

**Example: ADD EAX, [EBX + 100] (register with memory)**
- Encoding: `03 83 64 00 00 00` (6 bytes)
- Opcode `03` = ADD r, r/m (register from register/memory)
- ModR/M `83` = mod=10 (memory with displacement), reg=000 (EAX), r/m=011 (EBX)
- Displacement `64 00 00 00` = 100 (little-endian, 4 bytes)

#### 2.4 x86 Addressing Modes

The x86 provides many addressing modes, encoded in ModR/M and SIB bytes:

| Mode | Formula | Example |
|------|---------|---------|
| Register | Operand in register | `ADD EAX, EBX` |
| Immediate | Operand in instruction | `ADD EAX, 100` |
| Direct | [address] | `ADD EAX, [2000]` |
| Base | [base] | `ADD EAX, [EBX]` |
| Base+Displacement | [base + disp] | `ADD EAX, [EBX+100]` |
| Index+Displacement | [index*scale + disp] | `ADD EAX, [ESI*4+200]` |
| Base+Index+Displacement | [base + index*scale + disp] | `ADD EAX, [EBX+ESI*4+100]` |
| RIP-Relative | [RIP + disp] (x86-64) | `ADD EAX, [RIP+offset]` |
| Scaled Index | [base + index*scale] | `ADD EAX, [EBX+ESI*4]` |

Scale values: 1, 2, 4, 8 (for byte, word, dword, qword arrays).

#### 2.5 Common x86 Instructions

| Instruction | Operands | Description |
|-------------|----------|-------------|
| MOV | dest, src | Move data (load/store) |
| PUSH | src | Push onto stack |
| POP | dest | Pop from stack |
| ADD | dest, src | Addition |
| SUB | dest, src | Subtraction |
| IMUL | dest, src | Signed multiply |
| IDIV | src | Signed divide (EDX:EAX / src) |
| AND | dest, src | Bitwise AND |
| OR | dest, src | Bitwise OR |
| XOR | dest, src | Bitwise XOR |
| NOT | dest | Bitwise complement |
| SHL | dest, count | Shift left |
| SHR | dest, count | Shift right logical |
| SAR | dest, count | Shift right arithmetic |
| JMP | target | Unconditional jump |
| Jcc | target | Conditional jump (cc = E, NE, L, G, LE, GE, etc.) |
| CMP | op1, op2 | Compare (sets flags) |
| CALL | target | Call subroutine |
| RET | (optional pop) | Return from subroutine |
| LOOP | target | Decrement ECX; jump if ECX != 0 |
| INT | vector | Software interrupt |
| SYSCALL | - | System call (x86-64) |

#### 2.6 x86 Strengths and Weaknesses

**Strengths:**
- Backward compatible across 40+ years of evolution.
- Rich instruction set enables dense code.
- Variable-length encoding saves memory (code density).
- Powerful addressing modes (base+index*scale+displacement).
- Extensive ecosystem, toolchain, and software support.

**Weaknesses:**
- Complex instruction decoding (variable length, many formats).
- Difficult to pipeline and decode in parallel.
- Limited number of general-purpose registers (8 in 32-bit mode).
- Historical legacy restricts modern design.

### 3. ARM Architecture

#### 3.1 Overview

- **Type:** RISC (Reduced Instruction Set Computer).
- **First introduced:** 1985 (ARM1), evolved through ARM7, ARM9, ARM11, Cortex-A/R/M.
- **Bit width:** 32-bit (ARMv1-ARMv7), 64-bit (ARMv8-A, AArch64).
- **Instruction length:** Fixed 32-bit (ARM mode), 16-bit (Thumb mode), 16/32-bit mixed (Thumb-2).
- **Key characteristic:** Energy-efficient, widely used in mobile/embedded devices.
- **Design philosophy:** Simplicity, low power, high performance per watt.
- **Company:** ARM Holdings (licenses designs; does not manufacture).

#### 3.2 Register Set (ARMv7, 32-bit mode)

**General Purpose Registers (16 registers, 32-bit each):**

| Register | Name | Purpose |
|----------|------|---------|
| R0-R3 | - | Parameter passing, scratch registers |
| R4-R11 | - | Variable registers (callee-saved) |
| R12 | IP | Intra-procedure call scratch register |
| R13 | SP | Stack Pointer |
| R14 | LR | Link Register (return address for subroutine) |
| R15 | PC | Program Counter |

**Special-purpose registers:**
- **CPSR**: Current Program Status Register (32-bit).
- **SPSR**: Saved Program Status Register (for exception handling).

**CPSR format:**
```
Bit: 31 30 29 28 27 26 25-8 7 6 5 4-0
    +--+--+--+--+--+--+---+--+--+--+---+
    | N| Z| C| V| Q|IT|...| I| F| T|Mode|
    +--+--+--+--+--+--+---+--+--+--+---+
    |  |  |  |  |  |   |   |  |  |  |
    |  |  |  |  |  |   |   |  |  |  +----> Mode (processor mode)
    |  |  |  |  |  |   |   |  |  +-------> T (Thumb state)
    |  |  |  |  |  |   |   |  +----------> F (FIQ disable)
    |  |  |  |  |  |   |   +-------------> I (IRQ disable)
    |  |  |  |  |  |   +-----------------> IT (If-Then block, Thumb-2)
    |  |  |  |  |  +----------------------> Q (Saturation flag)
    |  |  |  |  +-------------------------> V (Overflow flag)
    |  |  |  +----------------------------> C (Carry flag)
    |  |  +-------------------------------> Z (Zero flag)
    |  +----------------------------------> N (Negative/Sign flag)
    +-------------------------------------> (reserved)
```

**Key difference from x86:** In ARM, the PC (R15) is a general-purpose register that can be read/written directly. The LR (R14) automatically receives the return address on branch-and-link instructions.

#### 3.3 Instruction Format (ARM, 32-bit)

ARM instructions have a fixed 32-bit format. Example formats:

**Data-processing instruction format:**
```
31 28 27 26 25 24 21 20 19 16 15 12 11 0
+----+--+--+----+--+----+----+----+--------+
|cond|00|I|opcd| S| Rn | Rd |operand2      |
+----+--+--+----+--+----+----+----+--------+
```

- **cond (4 bits):** Condition code (EQ, NE, CS, CC, MI, PL, VS, VC, HI, LS, GE, LT, GT, LE, AL, NV).
- **I (1 bit):** Immediate operand (0=register, 1=immediate).
- **opcode (4 bits):** Operation (AND, EOR, SUB, RSB, ADD, ADC, SBC, RSC, TST, TEQ, CMP, CMN, ORR, MOV, BIC, MVN).
- **S (1 bit):** Set condition codes (if 1, update CPSR flags).
- **Rn (4 bits):** First source operand register.
- **Rd (4 bits):** Destination register.
- **operand2 (12 bits):** Second operand (register with shift, or immediate value).

**Example: ADD R0, R1, R2 (R0 = R1 + R2)**
- Encoding: `E0810002` (hex) = `1110 0000 1000 0001 0000 0000 0000 0010`
- cond=1110 (AL=always), 00, I=0, opcode=0100 (ADD), S=0, Rn=0001 (R1), Rd=0000 (R0), operand2=000000000010 (R2)

#### 3.4 ARM Addressing Modes

| Mode | Example | Effective Address |
|------|---------|-------------------|
| Register | `ADD R0, R1, R2` | R0 = R1 + R2 |
| Immediate | `ADD R0, R1, #100` | R0 = R1 + 100 |
| Register with shift | `ADD R0, R1, R2, LSL #4` | R0 = R1 + (R2 << 4) |
| Base (Register indirect) | `LDR R0, [R1]` | R0 = M[R1] |
| Base+offset | `LDR R0, [R1, #100]` | R0 = M[R1 + 100] |
| Pre-indexed | `LDR R0, [R1, #100]!` | R0 = M[R1 + 100]; R1 = R1 + 100 |
| Post-indexed | `LDR R0, [R1], #100` | R0 = M[R1]; R1 = R1 + 100 |
| Register offset | `LDR R0, [R1, R2]` | R0 = M[R1 + R2] |
| Scaled register offset | `LDR R0, [R1, R2, LSL #2]` | R0 = M[R1 + (R2 << 2)] |
| PC-relative | `LDR R0, [PC, #offset]` | R0 = M[PC + offset] |

#### 3.5 ARM Conditional Execution

**Unique ARM feature:** Almost every instruction can be conditionally executed based on the CPSR flags. The condition is encoded in the top 4 bits of every instruction.

| Condition Code | Suffix | Flags | Meaning |
|----------------|--------|-------|---------|
| 0000 | EQ | Z=1 | Equal |
| 0001 | NE | Z=0 | Not Equal |
| 0010 | CS/HS | C=1 | Carry set / Unsigned higher or same |
| 0011 | CC/LO | C=0 | Carry clear / Unsigned lower |
| 0100 | MI | N=1 | Minus / Negative |
| 0101 | PL | N=0 | Plus / Positive or zero |
| 0110 | VS | V=1 | Overflow set |
| 0111 | VC | V=0 | Overflow clear |
| 1000 | HI | C=1 & Z=0 | Unsigned higher |
| 1001 | LS | C=0 or Z=1 | Unsigned lower or same |
| 1010 | GE | N=V | Signed greater than or equal |
| 1011 | LT | N!=V | Signed less than |
| 1100 | GT | Z=0 & N=V | Signed greater than |
| 1101 | LE | Z=1 or N!=V | Signed less than or equal |
| 1110 | AL | (any) | Always (default) |
| 1111 | NV | (none) | Never (reserved) |

**Example of conditional execution:**
```asm
; Instead of:
CMP R0, R1
ADDGT R2, R2, #1   ; Only executes if R0 > R1
SUBLT R3, R3, #1   ; Only executes if R0 < R1

; Without conditional execution (x86 style):
CMP R0, R1
BLE SKIP1
ADD R2, R2, #1
SKIP1:
BGE SKIP2
SUB R3, R3, #1
SKIP2:
```

The ARM version is shorter and avoids branch penalties.

#### 3.6 Common ARM Instructions

| Instruction | Description |
|-------------|-------------|
| MOV Rd, operand | Move (copy) |
| MVN Rd, operand | Move negated (complement) |
| ADD Rd, Rn, operand | Add |
| SUB Rd, Rn, operand | Subtract |
| RSB Rd, Rn, operand | Reverse subtract: operand - Rn |
| MUL Rd, Rn, Rm | Multiply (Rd = Rn * Rm) |
| MLA Rd, Rn, Rm, Ra | Multiply-accumulate: Rd = Ra + (Rn * Rm) |
| AND Rd, Rn, operand | Bitwise AND |
| ORR Rd, Rn, operand | Bitwise OR |
| EOR Rd, Rn, operand | Bitwise XOR |
| BIC Rd, Rn, operand | Bit clear: Rd = Rn AND NOT operand |
| LDR Rd, [addr] | Load register from memory |
| STR Rd, [addr] | Store register to memory |
| LDMIA Rn!, {reglist} | Load multiple registers |
| STMIA Rn!, {reglist} | Store multiple registers |
| B label | Branch (relative jump) |
| BL label | Branch and link (call) |
| BX Rm | Branch and exchange (return) |
| CMP Rn, operand | Compare and set flags |
| TST Rn, operand | Test bits (AND, set flags) |

#### 3.7 ARM Thumb Mode

Thumb is a 16-bit instruction set for ARM processors, providing better code density:

**Characteristics:**
- 16-bit fixed instruction length (half the size of ARM mode).
- Fewer instructions available (subset of ARM ISA).
- Fewer registers accessible (R0-R7 only in most instructions).
- No conditional execution on most instructions.
- Designed for memory-constrained embedded systems.

**Thumb-2** (introduced in ARMv6T2) extends Thumb with some 32-bit instructions, achieving performance close to ARM mode with code density close to Thumb mode.

#### 3.8 ARM64 (AArch64)

64-bit ARM architecture features:
- 31 general-purpose 64-bit registers (X0-X30).
- X30 = Link Register (LR), X29 = Frame Pointer (FP).
- SP (stack pointer) is a separate register.
- PC is no longer a general-purpose register.
- Fixed 32-bit instruction length.
- No conditional execution on most instructions (simplified).
- More registers, wider data paths.

### 4. MIPS Architecture

#### 4.1 Overview

- **Type:** RISC (Reduced Instruction Set Computer).
- **First introduced:** 1981 (Stanford MIPS project), 1985 (MIPS R2000).
- **Bit width:** 32-bit (original), 64-bit (MIPS64).
- **Instruction length:** Fixed 32-bit.
- **Key characteristic:** Clean, simple, highly regular design -- ideal for teaching computer architecture.
- **Company:** MIPS Technologies (now Wave Computing).
- **Influence:** Heavily influenced later RISC designs; used in education for decades.

#### 4.2 Register Set (MIPS32)

**General Purpose Registers (32 registers, 32-bit each):**

| Register | Name | Purpose |
|----------|------|---------|
| R0 | $zero | Always zero (hardwired) |
| R1 | $at | Assembler temporary |
| R2-R3 | $v0-$v1 | Function return values |
| R4-R7 | $a0-$a3 | Function arguments |
| R8-R15 | $t0-$t7 | Temporaries (caller-saved) |
| R16-R23 | $s0-$s7 | Saved registers (callee-saved) |
| R24-R25 | $t8-$t9 | More temporaries |
| R26-R27 | $k0-$k1 | Kernel reserved |
| R28 | $gp | Global pointer |
| R29 | $sp | Stack pointer |
| R30 | $fp | Frame pointer |
| R31 | $ra | Return address |

**Special-purpose registers:**
- **PC**: Program Counter (not directly accessible).
- **HI**: High 32 bits of multiplication/division result.
- **LO**: Low 32 bits of multiplication/division result.
- **SR**: Status Register.
- **Cause**: Cause of exception.
- **EPC**: Exception Program Counter.

**Key MIPS feature:** Register R0 is hardwired to the value 0. Writes to R0 are ignored (or simply have no effect). This simplifies instruction encoding (e.g., `JR $zero` is equivalent to NOP).

#### 4.3 Instruction Format (MIPS)

MIPS has three main instruction formats, all 32 bits:

**R-type (Register):**
```
31 26 25 21 20 16 15 11 10 6 5 0
+-----+-----+-----+-----+-----+-----+
|opcode| rs  | rt  | rd  |shamt|funct|
+-----+-----+-----+-----+-----+-----+
  6      5     5     5     5     6
```

- **opcode (6 bits):** Operation code (0 for R-type, funct field specifies actual op).
- **rs (5 bits):** First source register.
- **rt (5 bits):** Second source register.
- **rd (5 bits):** Destination register.
- **shamt (5 bits):** Shift amount (for shift instructions).
- **funct (6 bits):** Function code (specifies exact operation for R-type).

**I-type (Immediate):**
```
31 26 25 21 20 16 15 0
+-----+-----+-----+-----------+
|opcode| rs  | rt  | immediate |
+-----+-----+-----+-----------+
  6      5     5       16
```

**J-type (Jump):**
```
31 26 25 0
+-----+-----------+
|opcode| target   |
+-----+-----------+
  6       26
```

#### 4.4 MIPS Instruction Examples

**R-type example: ADD $t0, $s1, $s2**
```
opcode=0 (000000), rs=$s1(10001), rt=$s2(10010), rd=$t0(01000), shamt=00000, funct=100000
= 0000 0010 0011 0010 0100 0000 0010 0000 (binary)
= 0x02324020 (hex)
```

**I-type example: LW $t0, 100($s1) (load word)**
```
opcode=35 (100011), rs=$s1(10001), rt=$t0(01000), immediate=100 (0000 0000 0110 0100)
= 1000 1101 0001 0000 0000 0000 0110 0100
= 0x8D100064 (hex)
```

**J-type example: J 10000 (jump to address)**
```
opcode=2 (000010), target=10000 (00 0000 0000 0000 0010 0111 0001 0000)
But target is 26 bits; the full 32-bit address is formed as:
  {PC+4[31:28], target[25:0], 00}
```

#### 4.5 Common MIPS Instructions

| Instruction | Format | Description | RTL |
|-------------|--------|-------------|-----|
| ADD rd, rs, rt | R | Add | `rd <- rs + rt` |
| ADDI rt, rs, imm | I | Add immediate | `rt <- rs + imm` |
| SUB rd, rs, rt | R | Subtract | `rd <- rs - rt` |
| MUL rd, rs, rt | R | Multiply | `HI:LO <- rs * rt` |
| DIV rs, rt | R | Divide | `LO <- rs / rt; HI <- rs % rt` |
| AND rd, rs, rt | R | Bitwise AND | `rd <- rs AND rt` |
| OR rd, rs, rt | R | Bitwise OR | `rd <- rs OR rt` |
| XOR rd, rs, rt | R | Bitwise XOR | `rd <- rs XOR rt` |
| NOR rd, rs, rt | R | Bitwise NOR | `rd <- rs NOR rt` |
| SLT rd, rs, rt | R | Set less than (signed) | `rd <- (rs < rt) ? 1 : 0` |
| LW rt, imm(rs) | I | Load word | `rt <- M[rs + imm]` |
| SW rt, imm(rs) | I | Store word | `M[rs + imm] <- rt` |
| LB rt, imm(rs) | I | Load byte | `rt <- SignExt(M[rs + imm])` |
| BEQ rs, rt, offset | I | Branch if equal | `IF rs==rt THEN PC <- PC+4+offset` |
| BNE rs, rt, offset | I | Branch if not equal | `IF rs!=rt THEN PC <- PC+4+offset` |
| J target | J | Jump | `PC <- {PC+4[31:28], target, 00}` |
| JR rs | R | Jump register | `PC <- rs` |
| JAL target | J | Jump and link | `$ra <- PC+4; PC <- target` |
| SLL rd, rt, shamt | R | Shift left logical | `rd <- rt << shamt` |
| SRL rd, rt, shamt | R | Shift right logical | `rd <- rt >> shamt` |
| SRA rd, rt, shamt | R | Shift right arithmetic | `rd <- rt >>> shamt` |
| LUI rt, imm | I | Load upper immediate | `rt <- imm << 16` |

#### 4.6 MIPS Addressing Modes

MIPS has a simpler set of addressing modes compared to x86:

| Mode | Example | Effective Address |
|------|---------|-------------------|
| Register | `ADD $t0, $s1, $s2` | (operands in registers) |
| Immediate | `ADDI $t0, $s1, 100` | (immediate value in instr) |
| Base (Displacement) | `LW $t0, 100($s1)` | EA = $s1 + 100 |
| PC-relative | `BEQ $t0, $t1, label` | EA = PC + 4 + (offset << 2) |
| Pseudo-direct | `J target` | EA = (PC+4)[31:28] || target || 00 |

No indirect, no register indirect, no indexed modes! MIPS keeps it simple -- all memory access is via base+offset. The pseudo-direct jump forms the full address by combining the upper 4 bits of the current PC with the 26-bit target field.

### 5. Comparison Table: x86 vs ARM vs MIPS

| Feature | x86 (CISC) | ARM (RISC) | MIPS (RISC) |
|---------|-----------|------------|-------------|
| **Design philosophy** | Complex, backward-compatible | Simple, energy-efficient | Simplest, clean |
| **Instruction length** | Variable (1-15 bytes) | Fixed 32-bit (ARM), 16-bit (Thumb) | Fixed 32-bit |
| **General registers** | 8 (32-bit), 16 (64-bit) | 16 (32-bit), 31 (64-bit) | 32 (all general purpose) |
| **Special registers** | RIP, RFLAGS | CPSR, SPSR | HI, LO, SR, Cause |
| **Hardwired zero** | No | No | Yes ($zero = R0) |
| **Addressing modes** | Many (10+) | Moderate (8-10) | Few (4-5) |
| **Register/memory ops** | Register-memory | Load-store | Load-store |
| **Conditional execution** | Via Jcc instructions | Every instruction (ARM mode) | No |
| **Instruction encoding** | Variable, complex | Regular, fixed | Regular, 3 formats |
| **Typical IPC** | 0.5-2 (CISC complexity) | 1-2 (pipelined) | 1-2 (pipelined) |
| **Power efficiency** | Lower | Very high | High |
| **Primary market** | Desktop, server | Mobile, embedded | Embedded, networking |
| **Backward compatible** | Yes (40+ years) | Yes (within families) | Yes (32/64 bit) |

### 6. Detailed Comparison Example

**Same operation in all three ISAs: `A = B + C`**

**x86 (assuming variables in memory):**
```asm
MOV EAX, [B]      ; EAX = M[B]
ADD EAX, [C]      ; EAX = EAX + M[C]
MOV [A], EAX      ; M[A] = EAX
; 3 instructions, variable length (approx 6-12 bytes total)
```

**ARM (assuming registers loaded previously):**
```asm
; Load data into registers
LDR R1, =B        ; R1 = address of B (pseudo-instruction)
LDR R2, =C        ; R2 = address of C
LDR R3, [R1]      ; R3 = B
LDR R4, [R2]      ; R4 = C
ADD R5, R3, R4    ; R5 = B + C
LDR R0, =A        ; R0 = address of A
STR R5, [R0]      ; M[A] = R5
; 7 instructions, 28 bytes (32-bit ARM mode)
```

**MIPS (with proper load-store):**
```asm
lui $t0, B_hi     ; Load upper immediate for B address
ori $t0, $t0, B_lo; Load lower for B address
lw $t1, 0($t0)    ; $t1 = B
lui $t2, C_hi
ori $t2, $t2, C_lo
lw $t3, 0($t2)    ; $t3 = C
add $t4, $t1, $t3 ; $t4 = B + C
lui $t5, A_hi
ori $t5, $t5, A_lo
sw $t4, 0($t5)    ; M[A] = $t4
; 9 instructions, 36 bytes
```

**With MIPS addressing mode (base+offset, global pointer):**
```asm
lw $t0, B_offset($gp)  ; $t0 = B (base address in $gp)
lw $t1, C_offset($gp)  ; $t1 = C
add $t2, $t0, $t1      ; $t2 = B + C
sw $t2, A_offset($gp)  ; M[A] = $t2
; 4 instructions, 16 bytes
```

### 7. Summary of Key Architectural Differences

**Instruction format complexity:**
- x86: Most complex. Variable length means a single instruction can be 1-15 bytes. Decoding requires parsing prefixes, opcodes, ModR/M, SIB, displacement, and immediate fields.
- ARM: Fixed 32-bit with regular format. Easier to decode. Condition codes in every instruction.
- MIPS: Fixed 32-bit with only 3 formats (R, I, J). Simplest to decode and pipeline.

**Register model:**
- x86: Fewer general-purpose registers, each with historical special purposes.
- ARM: 16 general registers including SP, LR, PC. PC-relative addressing is natural.
- MIPS: 32 general registers with R0 hardwired to 0. Separate HI/LO for multiply/divide.

**Memory access:**
- x86: Many instructions can directly access memory (ADD can add memory to register, memory to memory, etc.).
- ARM: Load-store architecture. Only LDR/STR access memory. All ALU ops work on registers.
- MIPS: Load-store architecture. Only LW/SW (and byte variants) access memory. Simplest memory model.

---

## Practice Problems

1. **Problem**: Compare how the instruction `ADD R3, R1, R2` would be encoded in ARM and MIPS. What are the key differences in format?
<details>
<summary>Show Answer</summary>
   - ARM: `ADD R3, R1, R2` encoding: cond=1110(AL), 00, I=0, opcode=0100(ADD), S=0, Rn=0001(R1), Rd=0011(R3), operand2=000000000010(R2) = 0xE0813002. Has condition field and optional S bit for flag updates.
   - MIPS: `ADD $t1, $s1, $s2` ($t1=R9, $s1=R17, $s2=R18): opcode=0(R-type), rs=10001($s1), rt=10010($s2), rd=01001($t1), shamt=00000, funct=100000 = 0x02324820. No condition field; always executes. Function code distinguishes R-type ops.
</details>

2. **Problem**: Explain the purpose of the hardwired zero register ($zero/R0) in MIPS. Give three practical uses.
<details>
<summary>Show Answer</summary>
$zero is permanently 0; writes to it are ignored. Uses: (1) `MOVE $t0, $s1` = `ADD $t0, $s1, $zero`; (2) `LI $t0, 100` = `ADDI $t0, $zero, 100` (load immediate using $zero as base); (3) `NOP` = `ADD $zero, $zero, $zero` (no effective operation since result goes to $zero).
</details>

3. **Problem**: The x86 instruction `ADD EAX, [EBX + ESI*4 + 100]` uses which addressing mode? How many bytes are needed to encode this instruction (approximately)?
<details>
<summary>Show Answer</summary>
This is base+index*scale+displacement addressing. It uses ModR/M and SIB bytes. Approximate encoding: prefixes (0), opcode (1), ModR/M (1), SIB (1), displacement 4 bytes = 7 bytes total (plus possible immediate if any).
</details>

4. **Problem**: What is the ARM Thumb mode and why was it introduced? How does it compare to ARM mode in terms of code density and performance?
<details>
<summary>Show Answer</summary>
Thumb is a 16-bit instruction subset introduced to improve code density for memory-constrained embedded systems. Thumb code is typically 30-40% smaller than ARM mode but may execute 5-15% slower (fewer instructions, more instructions needed for same task). Thumb-2 adds 32-bit instructions for a balance of density and performance.
</details>

5. **Problem**: A MIPS `BEQ $t0, $t1, offset` instruction is at address 0x00400010. The target label is at address 0x00400028. What is the value of the offset field in the instruction?
<details>
<summary>Show Answer</summary>
In MIPS, BEQ computes: if condition true, PC = PC + 4 + (offset << 2). PC+4 = 0x00400014. Target = 0x00400028. So: 0x00400028 = 0x00400014 + (offset << 2). (offset << 2) = 0x00000014 = 20. Offset = 20/4 = 5. The offset field is 5 (encoded as 16-bit signed immediate).
</details>