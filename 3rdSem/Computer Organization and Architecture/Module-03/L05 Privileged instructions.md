# Privileged instructions

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 5  
**Date:** 26-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Definition of Privileged Instructions

**Privileged instructions** are machine instructions that can only be executed when the processor is operating in **supervisor mode** (also called **kernel mode**, **system mode**, or **privileged mode**). If a program attempts to execute a privileged instruction while in **user mode**, the processor generates a **trap** (general protection fault / privileged instruction exception), and the operating system typically terminates the offending program.

**Core idea:** Certain instructions are too powerful or dangerous for user programs to execute directly. Only the operating system kernel should have the authority to use them.

---

### 2. Dual Mode Operation

Modern processors support at least two privilege levels:

```
                  +---------------------------+
                  |       CPU Modes           |
                  +---------------------------+
                  |                           |
      +-----------+---------+       +---------+-----------+
      |   User Mode (Ring 3)|       | Kernel Mode (Ring 0)|
      |   (Problem State)   |       | (Supervisor State)  |
      +---------------------+       +---------------------+
      |   Executes:         |       |   Executes:         |
      |   - Non-privileged  |       |   - ALL instructions|
      |     instructions    |       |   - OS kernel code  |
      |   - User application|       |   - Device drivers  |
      |   - No direct h/w   |       |   - Memory mgmt     |
      |     access to:      |       |   - Context switch  |
      |     I/O, interrupts,|       |                     |
      |     MMU, etc.       |       |                     |
      +---------------------+       +---------------------+
```

#### Mode Bit

The processor includes a **mode bit** in a control register (e.g., the PSW / EFLAGS register) that indicates the current privilege level:

- **Mode bit = 0:** Kernel mode (supervisor mode). All instructions are allowed.
- **Mode bit = 1:** User mode. Privileged instructions cause a trap.

On x86, the Current Privilege Level (CPL) is stored in the CS register (CPL = 0 for Ring 0, CPL = 3 for Ring 3). On ARM, the mode is indicated by the current processor mode (SVC, IRQ, FIQ, USR, etc.).

#### Mode Switching

- **User to Kernel:** Triggered by **system calls** (software interrupt), **exceptions**, or **external interrupts**. The hardware automatically switches to kernel mode and saves the user context.
- **Kernel to User:** Triggered by the **IRET** (return from interrupt) or **RFE** (return from exception) instruction. The hardware restores the user context and switches to user mode.

```
   User Mode                       Kernel Mode
     App Code                         OS Kernel
        |                               |
        |--- system call (trap) ------->|
        |    (INT 0x80 / SVC)           |
        |                               |--- executes syscall handler
        |                               |--- (privileged instructions used here)
        |<-- return from syscall --------|
        |    (IRET / RFE)               |
        |                               |
        |--- (user code continues)       |
```

---

### 3. Examples of Privileged Instructions

#### 3.1 HLT (Halt)

- **Operation:** Stops the processor until an external interrupt or reset occurs.
- **Why privileged:** If a user program could halt the CPU, the entire system would freeze.
- **Usage:** The OS executes HLT in the idle loop when no processes are ready to run.

```asm
HLT            ; x86: halt processor until next interrupt
```

#### 3.2 I/O Instructions (IN/OUT)

- **Operation:** Read from or write to I/O ports.
- **Why privileged:** User programs could directly manipulate hardware (disk, keyboard, etc.), bypassing the OS and breaking protection and security.
- **Usage:** Only device drivers in kernel mode access I/O ports.

```asm
IN  AL, 60h    ; x86: read byte from port 0x60 (keyboard)
OUT 60h, AL    ; x86: write byte to port 0x60
```

#### 3.3 Setting Interrupt Masks

- **Operation:** Enable or disable interrupts (e.g., setting the IF flag on x86).
- **Why privileged:** A user program could disable interrupts and prevent the OS from ever regaining control, hanging the system.
- **Usage:** The kernel disables interrupts briefly during critical sections to maintain consistency.

```asm
CLI            ; x86: clear interrupt flag (disable maskable interrupts)
STI            ; x86: set interrupt flag (enable maskable interrupts)
```

#### 3.4 Memory Management Unit (MMU) Management

- **Operation:** Load page table base register, invalidate TLB entries, set memory protection attributes.
- **Why privileged:** User programs should not be able to modify page tables, which would let them access any physical memory.
- **Examples:**
  - x86: `MOV CR3, EAX` (load page table base address)
  - ARM: `MCR p15, 0, r0, c2, c0, 0` (set TTBR0 -- Translation Table Base Register)
  - RISC-V: `CSRW satp, x1` (set supervisor address translation and protection)

```asm
MOV CR3, EAX   ; x86: load page directory base register (privileged)
INVLPG [mem]   ; x86: invalidate TLB entry (privileged)
```

#### 3.5 Context Switching Instructions

- **Operation:** Save and restore processor state (registers, PC, PSW) when switching between processes.
- **Why privileged:** Only the OS scheduler should perform context switches. A user program switching context arbitrarily could hijack the system.
- **Usage:** The scheduler saves the current process state and loads the next process state using these instructions.

```asm
PUSHAD         ; x86: push all general-purpose registers
POPAD          ; x86: pop all general-purpose registers
IRET           ; x86: return from interrupt (restores CS, EIP, EFLAGS)
```

#### 3.6 Processor Control Registers Modification

- **Operation:** Write to control registers (CR0, CR2, CR3, CR4 on x86) that configure processor operating modes.
- **Why privileged:** These registers control critical processor features like paging, cache, protection.
- **Examples:**
  - `MOV CR0, EAX` -- can enable/disable paging, cache, etc.
  - `MOV CR4, EAX` -- controls features like PAE, SSE, VMX.

#### 3.7 Interrupt Descriptor Table (IDT) Management

- **Operation:** Load the IDT base address (LIDT), modify interrupt gate descriptors.
- **Why privileged:** User programs could redirect interrupts to their own handlers, intercepting keystrokes or other sensitive data.

```asm
LIDT [mem]     ; x86: load interrupt descriptor table register
SIDT [mem]     ; x86: store IDT register (sometimes unprivileged, but dangerous)
```

#### 3.8 Special System Instructions

| Instruction  | x86 Mnemonic    | Purpose                            |
|-------------|-----------------|------------------------------------|
| Read MSR    | RDMSR           | Read model-specific register       |
| Write MSR   | WRMSR           | Write model-specific register      |
| CPUID       | CPUID           | CPU identification (often unprivileged)|
| Halt        | HLT             | Halt processor                     |
| Wait        | WAIT            | Wait for FPU ready                 |
| Invalidate  | INVD            | Invalidate cache (no writeback)    |
| Write back  | WBINVD          | Write back and invalidate cache    |

---

### 4. Why Privileged Instructions Need Protection

| Reason                    | Explanation |
|---------------------------|-------------|
| **System stability**      | A user program executing HLT would halt the entire system. |
| **Security**              | A user program manipulating page tables could read any memory (including passwords, encryption keys). |
| **Resource isolation**    | Without protection, a user program could monopolize the CPU by disabling interrupts. |
| **Data integrity**        | Direct I/O access could corrupt filesystem structures or device firmware. |
| **OS control**            | The OS must retain ultimate control over hardware to manage multitasking and resource allocation. |
| **Protection ring model** | Privileges are layered; higher rings can access more resources. A bug in user code should not crash the entire system. |

#### What Happens if a User Program Executes a Privileged Instruction?

```
   User Program: "MOV CR3, EAX"   (attempts to load page table base)
        |
        v
   CPU detects: CPL (Current Privilege Level) != 0 (not kernel mode)
        |
        v
   CPU generates: General Protection Fault (#GP) exception
        |
        v
   OS exception handler runs:
        - Determines the faulting program
        - Sends signal (SIGSEGV / SIGILL) to the process
        - Terminates or debugs the process
        |
        v
   OS scheduler runs next process
```

---

### 5. Privilege Levels on x86 (Protection Rings)

x86 supports four privilege levels (Ring 0 through Ring 3):

```
            Ring 0 (Kernel) --- Most privileged
          Ring 1 (Device drivers)
        Ring 2 (Custom OS services)
      Ring 3 (User applications) --- Least privileged
```

- Most modern operating systems (Windows, Linux) use only Ring 0 and Ring 3.
- Ring 0 executes all instructions with full hardware access.
- Ring 3 executes only non-privileged instructions; privileged instructions cause faults.
- Data segment descriptors and code segment descriptors have their own privilege levels (DPL -- Descriptor Privilege Level).

---

### 6. Summary Table: Privileged vs Non-Privileged

| Instruction Category        | Privileged? | Reason for Privilege          |
|----------------------------|-------------|-------------------------------|
| HLT (halt)                 | Yes         | Would freeze system           |
| IN, OUT (I/O)              | Yes         | Direct hardware access        |
| CLI, STI (interrupt flags) | Yes         | Could disable OS control      |
| MOV CRn, reg (control regs)| Yes         | Memory/CPU configuration      |
| LIDT, LGDT (table regs)    | Yes         | Could redirect interrupts     |
| INVLPG (TLB invalidation)  | Yes         | Memory management control     |
| Arithmetic (ADD, SUB)      | No          | No system impact              |
| Data transfer (MOV)        | No          | User-level data operations    |
| Control transfer (JMP)     | No          | User-level branch             |
| System call (INT 0x80/SVC) | No*         | *Traps to kernel, but instruction itself is not privileged|

---

## Practice Problems

**Q1:** List four privileged instructions and explain why each must be restricted to kernel mode.

<details>
<summary>Show Answer</summary>
(1) HLT -- halts the CPU; a user program halting the CPU would freeze the entire system. (2) IN/OUT -- provides direct hardware I/O access; user programs could manipulate devices bypassing OS security. (3) CLI/STI -- disables/enables interrupts; a user program disabling interrupts would prevent the OS from regaining control. (4) MOV CR3, EAX -- loads page table base address; a user program could point page tables to arbitrary physical memory.
</details>

**Q2:** What is the mode bit and how does it relate to the execution of privileged instructions?

<details>
<summary>Show Answer</summary>
The mode bit (typically in the PSW/EFLAGS register) indicates the current privilege level of the processor. When the mode bit indicates kernel mode (0 on many architectures), all instructions are allowed. When it indicates user mode (1), the processor checks each instruction; if a privileged instruction is detected, it generates a trap/exception. The mode bit is automatically changed by the hardware during interrupts, exceptions, and system calls.
</details>

**Q3:** Describe the sequence of events that occurs when a user program attempts to execute a privileged instruction.

<details>
<summary>Show Answer</summary>
(1) CPU fetches the instruction and determines it is privileged. (2) CPU checks the current privilege level (CPL) against the required privilege level (typically 0). (3) Since CPL != 0, the CPU does not execute the instruction. (4) CPU generates a General Protection Fault (#GP) exception. (5) CPU switches to kernel mode, saves user context (PC, PSW, registers). (6) OS exception handler runs, identifies the faulting instruction and process. (7) OS sends an appropriate signal (SIGSEGV, SIGILL) to the process. (8) Process is terminated or the OS delivers a signal handler.
</details>

**Q4:** Why do most modern operating systems use only two rings (Ring 0 and Ring 3) instead of all four available on x86?

<details>
<summary>Show Answer</summary>
Maintaining four distinct privilege rings adds significant complexity to the OS design. The additional rings were originally designed for system architectures that are rarely used today (e.g., for separating OS core from system services). Modern OS design philosophy favors simplicity, portability, and security through other mechanisms (user vs kernel mode, virtual memory, capabilities). Two levels are sufficient to implement protection: privileged kernel code and unprivileged user code.
</details>

**Q5:** What is the relationship between system calls and privileged instructions?

<details>
<summary>Show Answer</summary>
System calls are the mechanism through which user programs request kernel services (e.g., file I/O, process creation, memory allocation). The system call instruction (e.g., INT 0x80, SYSCALL, SVC) itself is NOT privileged -- it is available to user programs. However, the instruction causes a software trap that switches the CPU to kernel mode. Once in kernel mode, the OS executes privileged instructions on behalf of the user program (e.g., IN/OUT for I/O, modifying page tables for memory allocation). This provides a controlled interface: user programs request services, and the kernel validates and performs privileged operations.
</details>

---