# Programs and processes role of interrupts in process state transitions

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 8  
**Date:** 02-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Program vs Process

**Program:** A passive entity -- a static set of instructions stored on disk (an executable file). A program contains no execution state; it is just a collection of code and data.

**Process:** An active entity -- a program in execution. A process has:
- A current state (register values, program counter, stack pointer).
- Associated resources (memory, open files, I/O devices).
- An execution context that evolves over time.

**Analogy:** A program is like a musical score (sheet music); a process is like the actual performance of that score by an orchestra. The same score can be performed multiple times, each producing a distinct performance (process).

---

### 2. Process States

A process transitions through several states during its lifetime. The classic **five-state model** is:

```
                  +----------+
                  |   New    |
                  +----+-----+
                       |
                       | (admitted)
                       v
                  +----------+
         +------->|   Ready  |<--------+
         |        +----+-----+         |
         |             |               |
         |     (scheduler dispatch)    |
         |             |               |
         |             v               |
         |        +----------+         |
         |        | Running  |---------+------> (exit)
         |        +----+-----+         |
         |             |               |
         |             | (I/O or       |
         |             |  event wait)  |
         |             v               |
         |        +----------+         |
         +--------|  Waiting |---------+
                  | (Blocked)|
                  +----------+
```

**State Descriptions:**

| State    | Description |
|----------|-------------|
| **New**      | The process is being created. The OS is setting up the PCB, allocating initial resources. |
| **Ready**    | The process is in main memory, has all required resources except the CPU, and is waiting to be scheduled for execution. |
| **Running**  | The process is currently executing on the CPU. Only one process per CPU core at any time. |
| **Waiting**  | The process is blocked, waiting for some event to occur (e.g., I/O completion, signal arrival). It cannot run even if the CPU is available. |
| **Terminated** | The process has finished execution (normally or abnormally). The OS is reclaiming its resources. |

---

### 3. Process State Transition Diagram (ASCII)

```
                         +==============+
                         |    NEW       |
                         +======+=======+
                                |
                                | (Admitted to system)
                                v
                   +======================+
            +----->|        READY         |<----+
            |      +===========+==========+     |
            |                  |                 |
            |          (Dispatch by            |
            |           scheduler)              |
            |                  |                 |
            |                  v                 |
            |      +======================+     |
            |      |       RUNNING        |     |
            |      +===========+==========+     |
            |                  |                 |
            |     (I/O wait)   |   (Timer        |
            |                  |    interrupt)   |
            |                  v                 |
            |      +======================+     |
            +------|       WAITING       |------+
            |      +======================+     
            |        (I/O completion)
            |
            |      +======================+
            +------|     TERMINATED       |
                   +======================+
```

**Transitions:**

1. **New -> Ready:** The OS admits the process (enough resources available).
2. **Ready -> Running:** The scheduler selects this process to run (context switch).
3. **Running -> Ready:** The process is preempted (timer interrupt) or voluntarily yields.
4. **Running -> Waiting:** The process requests I/O, waits for a signal/event.
5. **Waiting -> Ready:** The awaited event occurs (I/O completes, signal arrives).
6. **Running -> Terminated:** The process exits (normal or abnormal).

---

### 4. Role of Interrupts in Process State Transitions

Interrupts are the primary mechanism that drives process state transitions in a multitasking system.

#### 4.1 Timer Interrupt -> Context Switch (Running -> Ready)

The **timer interrupt** is generated periodically by the hardware timer (e.g., every 1-100 ms). It ensures that no single process monopolizes the CPU.

```
   Process P1 (Running)          Timer             OS Scheduler
        |                         |                    |
        | (executing)             |                    |
        |                         |                    |
        |<--- Timer Interrupt ----|                    |
        |                         |                    |
        | (CPU switches to kernel mode)                |
        |                         |                    |
        |--- Timer ISR saves -----|------------------->|
        |    registers, PC        |                    |
        |                         |                    | decide to preempt P1
        |                         |                    |
        |                         |                    | save P1 state into PCB1
        |                         |                    | load P2 state from PCB2
        |                         |                    |
        |                         |<-- return to P2 ---|
        |                         |                    |
   Process P2 (Running)          |                    |
```

**Consequence:** P1 moves from Running -> Ready. P2 moves from Ready -> Running.

#### 4.2 I/O Interrupt -> Process Unblock (Waiting -> Ready)

When an I/O device completes an operation, it sends an interrupt. The interrupt handler determines which process was waiting for that I/O and moves it from Waiting to Ready.

```
   Process P1 (Waiting for disk)   Disk Controller     OS Scheduler
        |                              |                    |
        | (P1 issued read() syscall)   |                    |
        |                              |--- Disk seeking --|
        |                              |--- Data transfer -|
        |                              |                    |
        |<--------- IRQ ---------------|                    |
        |                              |                    |
        | (CPU switches to kernel mode)                    |
        |                              |                    |
        |--- Disk ISR handles ---------|------------------->|
        |    interrupt                  |                    |
        |                              |                    | identify P1 as waiter
        |                              |                    | move P1: Waiting -> Ready
        |                              |                    | update PCB1 status
        |                              |                    |
        |<-- return to whatever was ----|-------------------|
        |    running (maybe not P1)     |                    |
```

**Consequence:** P1 moves from Waiting -> Ready. P1 will run when the scheduler picks it.

#### 4.3 I/O Request (System Call) -> Process Blocks (Running -> Waiting)

A process that requests I/O (e.g., read from disk, write to network) cannot proceed until the I/O completes. The kernel puts the process to sleep (Waiting state) and schedules another process.

```
   Process P1 (Running)          OS Kernel           Disk Driver       Process P2
        |                          |                     |                 |
        |--- read() syscall ------>|                     |                 |
        |                          |                     |                 |
        |                          | start disk I/O      |                 |
        |                          |-------------------->|                 |
        |                          |                     |                 |
        |                          | save P1 state       |                 |
        |                          | move P1: Running -> Waiting            |
        |                          |                     |                 |
        |                          | choose P2 to run   |                 |
        |                          |------------------------------------->|
        |                          |                     |                 |
   Process P1 (Waiting)            |                     |           P2 (Running)
```

#### 4.4 Process Exit/Error (Running -> Terminated)

When a process finishes or encounters a fatal error, it transitions from Running to Terminated. The OS cleans up its resources.

---

### 5. Process Control Block (PCB)

The **Process Control Block** is a data structure in the OS kernel that stores all information about a process. Each process has exactly one PCB.

#### PCB Contents

```
   +==========================================+
   |         Process Control Block (PCB)      |
   +==========================================+
   | Process ID (PID)          (unique number)|
   | Process State             (Ready/Running/|
   |                            Waiting/New/  |
   |                            Terminated)   |
   | Program Counter (PC)      (next instruc- |
   |                            tion address) |
   | CPU Registers             (general purp- |
   |                           ose registers, |
   |                           stack pointer, |
   |                           frame pointer) |
   | Memory Management Info    (page table    |
   |                           base, segment  |
   |                           tables)        |
   | Scheduling Info           (priority,     |
   |                           time quantum,  |
   |                           CPU burst hist)|
   | I/O Status                (open file     |
   |                           descriptors,   |
   |                           pending I/O)   |
   | Accounting Info           (CPU time      |
   |                           used, start    |
   |                           time, etc.)    |
   | Parent Process ID (PPID)                 |
   | Child Process List                       |
   | Signal Handlers                          |
   +==========================================+
```

#### PCB Organization

PCBs are typically stored in a **linked list** or **array** in kernel memory. The OS maintains separate queues for each state:

- **Ready Queue:** List of PCBs of ready processes.
- **Waiting/Blocked Queue(s):** Lists of PCBs waiting for specific events (one queue per device, or a general queue).
- **Run Queue:** The PCB of the currently running process (usually pointed to by a CPU-specific variable).

```
   Ready Queue:         PCB1 -> PCB2 -> PCB3 -> ... -> PCBn
                       (head)                         (tail)
   
   Disk Waiting Queue:  PCB5 -> PCB8 -> PCB12
   
   Keyboard Waiting:    PCB7
   
   Currently Running:   [CPU] -> PCB4
```

---

### 6. Context Switching

A **context switch** is the mechanism by which the OS saves the state of the currently running process and restores the state of the next process to run.

#### Steps in a Context Switch

```
   Step 1: Save the context of the current process (P1)
           - Save Program Counter (PC) into PCB1
           - Save all general-purpose registers into PCB1
           - Save stack pointer (SP) and frame pointer (FP) into PCB1
           - Save processor status word (PSW) into PCB1
           - Save memory management info (e.g., page table pointer) into PCB1
   
   Step 2: Update P1's PCB state to Ready (or Waiting/Terminated)
   
   Step 3: Move P1's PCB to the appropriate queue (Ready Queue, etc.)
   
   Step 4: Select the next process to run (P2) = scheduling decision
   
   Step 5: Load P2's context from PCB2
           - Load Program Counter (PC) from PCB2
           - Load general-purpose registers from PCB2
           - Load stack pointer (SP) and frame pointer (FP) from PCB2
           - Load processor status word (PSW) from PCB2
           - Load memory management info from PCB2
             (e.g., load page table base into CR3 on x86)
   
   Step 6: Update P2's PCB state to Running
   
   Step 7: Return to user mode
           - Jump to the address in PC (P2's saved instruction pointer)
```

#### Context Switch Timing Diagram

```
   P1 Running         OS (Kernel)            P2 Running
   |                     |                       |
   | (timer interrupt)   |                       |
   |---------------------|                       |
   |                     |                       |
   |                     | Save P1 context       |
   |                     | to PCB1               |
   |                     |                       |
   |                     | Load P2 context       |
   |                     | from PCB2             |
   |                     |                       |
   |                     | (IRET)                |
   |                     |---------------------->|
   |                     |                       |
   |                     |                  P2 executes
   |                     |
   
   <--- P1 saved ---><-- context switch ----><--- P2 running --->
   
   Overhead: This time is "wasted" -- the CPU does no useful application work during the switch.
```

#### Context Switch Overhead

The context switch is **pure overhead** -- it takes CPU time away from executing user processes. Factors:

- **Direct costs:** Saving/restoring registers (typically 50-200 CPU cycles).
- **Indirect costs:** Cache pollution (the new process does not have its data in cache), TLB flushes (if ASID not used).
- **Total cost:** Typically 1-10 microseconds on modern systems (though it varies widely by architecture and OS).

#### Context Switch vs Mode Switch

| Feature        | Mode Switch                      | Context Switch                   |
|----------------|----------------------------------|----------------------------------|
| What changes   | Privilege level (user <-> kernel) | Process / thread                  |
| State saved    | Minimal (PC, PSW, stack pointers) | Full CPU register state          |
| Cost           | Low (50-200 cycles)              | High (500-10,000+ cycles)        |
| Frequency      | Very frequent (every syscall)    | Less frequent (every scheduler tick)|
| Trigger        | Syscall, interrupt, exception    | Timer interrupt, voluntary yield |

A context switch always involves at least two mode switches (user -> kernel -> user), but a mode switch does not necessarily involve a context switch.

---

### 7. Complete Example: Process State Changes

Consider a system with two processes: P1 (CPU-bound, computing prime numbers) and P2 (I/O-bound, reading from disk).

```
Time   Event                        P1 State       P2 State
----   -----                        --------       --------
0      System boots, P1 created     New            New
1      P1 admitted                  Ready          New
2      P2 admitted                  Ready          Ready
3      Scheduler picks P1           Running        Ready
4      P1 runs (computing)
5      Timer interrupt (quantum     Ready          Running
       expires), scheduler picks P2
6      P2 runs
7      P2 requests disk I/O         Ready          Waiting
       (read system call)
8      P2 blocks, scheduler         Running        Waiting
       picks P1
9      Disk I/O completes,          Ready          Ready
       interrupt moves P2 to Ready
10     Timer interrupt, scheduler   Ready          Running
       picks P2
11     P2 finishes file operation   Running        Running
12     P2 runs
13     Timer interrupt, scheduler   Running        Ready
       picks P1
...
```

---

## Practice Problems

**Q1:** List the five process states and describe the transitions between them. What triggers each transition?

**A1:** The five states are: New, Ready, Running, Waiting (Blocked), Terminated. Transitions: (1) New -> Ready: OS admits process. (2) Ready -> Running: scheduler dispatches process. (3) Running -> Ready: timer interrupt (preemption) or voluntary yield. (4) Running -> Waiting: process requests I/O or waits for event. (5) Waiting -> Ready: I/O completion interrupt or event arrival. (6) Running -> Terminated: process exits.

**Q2:** Explain the role of the timer interrupt in process state transitions.

**A2:** The timer interrupt is generated periodically by a hardware timer. When it fires, the OS scheduler gains control. The scheduler inspects the currently running process; if its time quantum has expired, the process is moved from Running to Ready, and another process is dispatched from the Ready queue. This ensures fair CPU time sharing among processes and prevents any single process from monopolizing the CPU. Without timer interrupts, a process could run indefinitely unless it voluntarily yielded.

**Q3:** What information is stored in a Process Control Block (PCB)? Why is it needed?

**A3:** The PCB stores: Process ID (PID), process state, program counter, CPU registers, memory management info (page table base), scheduling info (priority, time quantum), I/O status (open files), accounting info (CPU time used), parent PID, signal handlers. The PCB is needed because it contains all the information required to suspend and resume a process. During a context switch, the OS saves the running process's context into its PCB and loads the next process's context from its PCB. Without the PCB, the OS would have no way to restore a process's exact execution state.

**Q4:** Describe the complete sequence of steps in a context switch initiated by a timer interrupt.

**A4:** (1) Timer generates interrupt. (2) CPU completes current instruction. (3) CPU saves PC, PSW, stack pointers (mode switch to kernel). (4) Timer ISR saves remaining registers. (5) ISR calls scheduler. (6) Scheduler: saves current process state into its PCB, adds PCB to Ready queue, selects next process (highest priority), removes next process's PCB from Ready queue, loads its state from PCB. (7) Scheduler loads CR3 with next process's page table base (if needed). (8) Scheduler restores registers, executes IRET. (9) Next process resumes execution.

**Q5:** What is the difference between a mode switch and a context switch? Why is a context switch more expensive?

**A5:** A mode switch changes only the privilege level (user mode to kernel mode and back), saving minimal context (PC, PSW, stack). A context switch switches between entirely different processes, requiring saving ALL registers (general-purpose, floating-point, SIMD, etc.), flushing/reloading the TLB (unless ASIDs are used), and potentially warming new cache lines. A mode switch costs ~50-200 cycles; a context switch costs ~500-10,000+ cycles depending on architecture and the amount of state saved/restored. A context switch always involves at least two mode switches, but a mode switch does not always involve a context switch (e.g., a system call in the same process).

---
