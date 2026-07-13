# Non-privileged instructions

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 6  
**Date:** 26-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Definition of Non-Privileged Instructions

**Non-privileged instructions** (also called **user-mode instructions**) are machine instructions that can be executed in any processor mode -- both **user mode** and **kernel mode**. These instructions perform operations that do not affect system-wide resources, do not bypass OS protection, and are safe to allow any program to execute.

**Key characteristic:** Non-privileged instructions cannot access or modify:
- I/O devices directly (no port I/O or MMIO without OS mediation)
- Memory management structures (page tables, TLB)
- Interrupt controller or interrupt descriptor tables
- CPU control registers (CR0-CR4)
- Processor modes or privilege levels

---

### 2. Categories of Non-Privileged Instructions

#### 2.1 Arithmetic Instructions

Perform basic mathematical operations on data in registers or memory.

| Instruction (x86) | Operation        | Example                     |
|-------------------|------------------|-----------------------------|
| ADD               | Integer addition | `ADD EAX, EBX` -- EAX = EAX + EBX |
| SUB               | Integer subtraction | `SUB EAX, 1` -- EAX = EAX - 1 |
| MUL               | Unsigned multiply | `MUL EBX` -- EDX:EAX = EAX x EBX |
| IMUL              | Signed multiply  | `IMUL EAX, ECX`             |
| DIV               | Unsigned divide  | `DIV EBX` -- EAX = quotient, EDX = remainder |
| IDIV              | Signed divide    | `IDIV EBX`                  |
| INC               | Increment by 1   | `INC ECX`                   |
| DEC               | Decrement by 1   | `DEC EAX`                   |
| NEG               | Negate           | `NEG EAX` -- EAX = -EAX     |
| CMP               | Compare (sets flags) | `CMP EAX, EBX`          |

#### 2.2 Logical Instructions

Perform bitwise logical operations.

| Instruction (x86) | Operation        | Example                     |
|-------------------|------------------|-----------------------------|
| AND               | Bitwise AND      | `AND EAX, 0xFF`             |
| OR                | Bitwise OR       | `OR EBX, ECX`               |
| XOR               | Bitwise XOR      | `XOR EAX, EAX` (clear register) |
| NOT               | Bitwise NOT (complement) | `NOT EAX`            |
| TEST              | AND without result (sets flags) | `TEST AL, 0x80` |

#### 2.3 Data Transfer Instructions

Move data between registers, memory, and immediate values.

| Instruction (x86) | Operation        | Example                     |
|-------------------|------------------|-----------------------------|
| MOV               | Move data        | `MOV EAX, [EBX]` -- load from memory |
| PUSH              | Push onto stack  | `PUSH EAX`                  |
| POP               | Pop from stack   | `POP EBX`                   |
| MOVS              | Move string (block copy) | `MOVSB` -- byte string copy |
| LEA               | Load effective address | `LEA EAX, [EBX+ECX*4]` |
| XCHG              | Exchange values  | `XCHG EAX, EBX`             |

**Important:** MOV to/from control registers (MOV CRn, reg) is PRIVILEGED. MOV to/from general-purpose registers and memory is NON-PRIVILEGED.

#### 2.4 Control Transfer Instructions

Change the flow of execution.

**Unconditional branch/jump:**
| Instruction (x86) | Operation        | Example                     |
|-------------------|------------------|-----------------------------|
| JMP               | Unconditional jump | `JMP LABEL`                |
| CALL              | Call subroutine (pushes return address) | `CALL FUNCTION` |
| RET               | Return from subroutine | `RET`                    |

**Conditional branch (based on flags):**
| Instruction (x86) | Condition        | Example                     |
|-------------------|------------------|-----------------------------|
| JZ / JE           | Zero / Equal     | `JZ DONE`                   |
| JNZ / JNE         | Not zero / Not equal | `JNZ LOOP`              |
| JG / JNLE         | Signed greater than | `JG LABEL`               |
| JL / JNGE         | Signed less than | `JL LABEL`                  |
| JGE / JNL         | Signed greater or equal | `JGE LABEL`           |
| JLE / JNG         | Signed less or equal | `JLE LABEL`             |
| JA / JNBE         | Unsigned above   | `JA LABEL`                  |
| JB / JNAE         | Unsigned below   | `JB LABEL`                  |
| JC                | Carry set        | `JC ERROR`                  |
| JNC               | Carry clear      | `JNC OK`                    |

#### 2.5 Shift and Rotate Instructions

Move bits left or right within a register or memory location.

| Instruction (x86) | Operation        | Example                     |
|-------------------|------------------|-----------------------------|
| SHL               | Shift left       | `SHL EAX, 1`                |
| SHR               | Shift right (logical) | `SHR EBX, CL`          |
| SAR               | Shift right (arithmetic) | `SAR EAX, 2`        |
| ROL               | Rotate left      | `ROL AL, 4`                 |
| ROR               | Rotate right     | `ROR AL, 4`                 |
| RCL               | Rotate through carry left | `RCL EAX, 1`      |
| RCR               | Rotate through carry right | `RCR EAX, 1`      |

#### 2.6 Bit Manipulation Instructions

Operate on individual bits.

| Instruction (x86) | Operation               | Example                     |
|-------------------|-------------------------|-----------------------------|
| BT                | Bit test                | `BT EAX, 3` -- test bit 3   |
| BTS               | Bit test and set        | `BTS EAX, 5`               |
| BTR               | Bit test and reset      | `BTR EAX, 7`               |
| BTC               | Bit test and complement | `BTC EAX, 2`               |
| BSF               | Bit scan forward        | `BSF ECX, EAX`             |
| BSR               | Bit scan reverse        | `BSR ECX, EAX`             |

#### 2.7 String Instructions

Operate on sequences of data in memory.

| Instruction (x86) | Operation             | Example                     |
|-------------------|-----------------------|-----------------------------|
| MOVSB / MOVSW / MOVSD | Move string (byte/word/dword) | `REP MOVSB`     |
| CMPSB / CMPSW / CMPSD | Compare strings      | `REPE CMPSB`              |
| SCASB / SCASW / SCASD | Scan string          | `REPNE SCASB`             |
| LODSB / LODSW / LOSD | Load string          | `LODSB`                    |
| STOSB / STOSW / STOSD | Store string         | `REP STOSB`               |

#### 2.8 Conversion Instructions

Convert between data formats.

| Instruction (x86) | Operation               | Example                     |
|-------------------|-------------------------|-----------------------------|
| MOVZX             | Move with zero-extend   | `MOVZX EAX, AL`            |
| MOVSX             | Move with sign-extend   | `MOVSX EAX, AL`            |
| CBW               | Convert byte to word    | `CBW`                      |
| CWD               | Convert word to doubleword | `CWD`                    |
| CWDE              | Convert word to doubleword (extended) | `CWDE`         |
| CDQ               | Convert doubleword to quadword | `CDQ`                  |

#### 2.9 Floating-Point Instructions (x87 FPU)

| Instruction  | Operation            | Example                     |
|--------------|----------------------|-----------------------------|
| FADD         | Floating-point add   | `FADD ST(0), ST(1)`        |
| FSUB         | Floating-point subtract | `FSUB ST(0), ST(1)`       |
| FMUL         | Floating-point multiply | `FMUL ST(0), ST(1)`       |
| FDIV         | Floating-point divide | `FDIV ST(0), ST(1)`        |
| FILD         | Integer load to FP   | `FILD [mem]`               |
| FISTP        | FP store to integer  | `FISTP [mem]`              |

#### 2.10 SIMD Instructions (MMX, SSE, AVX)

| Instruction  | Operation               | Example                     |
|--------------|-------------------------|-----------------------------|
| PADDUSB      | Packed unsigned byte add (MMX) | `PADDUSB mm0, mm1` |
| ADDPS        | Add packed single-precision floats (SSE) | `ADDPS xmm0, [mem]` |
| VMULPD       | Multiply packed double-precision floats (AVX) | `VMULPD ymm0, ymm1, [mem]` |

---

### 3. Limitation: No Direct System Resource Access

Non-privileged instructions cannot:

| Operation                   | Why it is restricted             | How to achieve (via system call) |
|-----------------------------|----------------------------------|----------------------------------|
| Direct disk read/write      | Could corrupt filesystem         | `read()` / `write()` system calls |
| Modify page tables          | Could access other processes' memory | `mmap()`, `sbrk()` system calls |
| Send data to network card   | Could bypass firewall/security   | `send()` system call             |
| Change system clock         | Could break time-dependent features | `settimeofday()` system call  |
| Start another process       | Could spawn unlimited processes  | `fork()` / `execve()` system calls|
| Disable interrupts          | Could hang the system            | N/A (only kernel can)            |

---

### 4. Trapping to Kernel for System Calls

When a user program needs a system service (access to a privileged resource), it uses a **system call** mechanism.

#### System Call Mechanism: Software Interrupt

```
User Program (User Mode)              OS Kernel (Kernel Mode)
                               
   MOV EAX, SYS_READ           ; System call number
   MOV EBX, fd                 ; File descriptor
   MOV ECX, buffer             ; Buffer address
   MOV EDX, count              ; Count
   INT 0x80                    ; Software interrupt (trap)
   --------TRAP-------->       |
                               | CPU switches to kernel mode
                               | Saves registers, PC, PSW on kernel stack
                               | Look up syscall handler in IDT
                               | Jump to system_call entry point
                               | sys_call_table[EAX] -> sys_read
                               |   - Validates parameters
                               |   - Checks permissions
                               |   - Performs I/O operation
                               |   - Returns result in EAX
                               | CPU switches to user mode
   <-------RETURN---------     |
   (EAX now contains bytes read or error code)
   ; Continue execution
```

#### Key Points about System Calls

1. The system call instruction (INT 0x80, SYSENTER, SYSCALL) itself is **non-privileged** -- any user program can execute it.
2. However, the instruction causes a **trap that switches the CPU to kernel mode**.
3. Once in kernel mode, the OS validates the request before performing privileged operations.
4. The OS returns to user mode after completing the service.

**Modern fast system call instructions:**
- x86: SYSENTER (Intel) / SYSCALL (AMD) -- faster than INT 0x80.
- ARM: SVC (Supervisor Call).
- RISC-V: ECALL (Environment Call).

---

### 5. Example: C Program to Non-Privileged Instructions Mapping

```c
int a = 5, b = 10, c;
c = a + b;               // ADD instruction (non-privileged)
if (c > 10) {            // CMP + JG instructions (non-privileged)
    c = c * 2;           // MUL instruction (non-privileged)
}
printf("%d", c);         // Requires write() system call (traps to kernel)
```

The first three operations (addition, comparison, multiplication) use only non-privileged instructions and execute entirely in user mode. The `printf()` function eventually calls `write()` which is a system call, triggering a trap to kernel mode to perform the actual console I/O.

```
Assembly translation (simplified):

   MOV [a], 5              ; Non-privileged
   MOV [b], 10             ; Non-privileged
   MOV EAX, [a]            ; Non-privileged
   ADD EAX, [b]            ; Non-privileged
   MOV [c], EAX            ; Non-privileged
   CMP EAX, 10             ; Non-privileged (sets flags)
   JLE skip                ; Non-privileged
   MUL EAX, 2              ; Non-privileged
   MOV [c], EAX            ; Non-privileged
skip:
   ; System call for printf
   MOV EAX, SYS_WRITE      ; Non-privileged (setup)
   MOV EBX, 1              ; stdout
   MOV ECX, format_string
   MOV EDX, len
   INT 0x80                ; --> traps to kernel (privileged operations happen inside)
```

---

### 6. Summary: Non-Privileged vs Privileged Instructions

| Feature                | Non-Privileged Instructions      | Privileged Instructions         |
|------------------------|----------------------------------|---------------------------------|
| Execution mode         | User mode AND kernel mode        | Only kernel mode                |
| Effect on system       | No system-wide impact             | Can affect entire system        |
| Examples               | ADD, MOV, JMP, CALL, PUSH        | HLT, IN/OUT, CLI/STI, MOV CR3  |
| OS intervention        | Not needed                        | Requires OS to validate         |
| Hardware access        | None (indirect via syscall)       | Direct                          |
| Safety                 | Safe for arbitrary user code      | Dangerous in wrong hands        |
| Protection mechanism   | None needed                       | Traps to OS on violation        |

---

## Practice Problems

**Q1:** Explain why the ADD instruction is non-privileged while the IN instruction is privileged.

**A1:** ADD performs arithmetic on user data in registers or memory. It cannot affect any other process or system hardware. IN reads from I/O ports, giving direct access to hardware devices (keyboard, disk, network). A user program reading keyboard input directly could implement a keylogger without OS awareness. Therefore, only the kernel (device drivers) may execute IN/OUT.

**Q2:** What sequence of instructions might a user program execute to read a file from disk? Identify which are non-privileged and which require a system call.

**A2:** The program sets up arguments (non-privileged: MOV instructions), invokes a system call via INT 0x80 or SYSENTER (non-privileged but causes a trap). Inside the kernel: the file system code validates permissions, interacts with the disk driver (privileged: IN/OUT to disk controller), copies data to user buffer (non-privileged MOV), and returns. After the trap, the program processes the data (non-privileged arithmetic, logical, etc.).

**Q3:** Describe the role of the system call instruction (e.g., INT 0x80 on x86) and why it is not a privileged instruction.

**A3:** INT 0x80 is a software interrupt instruction that triggers a trap to the kernel. It is not privileged because user programs must be able to request kernel services. However, the instruction causes the CPU to switch to kernel mode and jump to a predetermined handler in the OS. The OS then validates the request before executing any privileged operations. This provides a controlled gateway between user space and kernel space.

**Q4:** Which of the following instructions are non-privileged and which are privileged on a typical x86 system? (a) XOR EAX, EAX (b) CLI (c) PUSH EBX (d) MOV CR0, EAX (e) RET (f) IN AL, 0x60

**A4:** (a) Non-privileged (bitwise XOR). (b) Privileged (modifies interrupt flag). (c) Non-privileged (stack operation). (d) Privileged (modifies control register). (e) Non-privileged (return from subroutine). (f) Privileged (I/O port access).

**Q5:** A user program needs to allocate more memory. Show the interaction between non-privileged and privileged components.

**A5:** The user program calls `malloc(n)`. Internally, malloc may invoke `brk()` or `mmap()` which are system calls. The program: (a) loads arguments (non-privileged MOV). (b) executes SYSCALL/INT 0x80 (non-privileged trap). (c) Kernel mode: validates the request, modifies page tables (privileged -- MOV CR3 changes may be involved), updates process memory map (non-privileged data operations). (d) Returns to user mode. (e) The program continues with the new memory available (non-privileged).

---
