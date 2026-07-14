# I/O transfers interrupt driven and DMA

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 4  
**Date:** 25-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Interrupt-Driven I/O

In **interrupt-driven I/O**, the CPU does not poll the device. Instead, the device **signals** the CPU via an **interrupt** when it is ready for data transfer. The CPU can execute other tasks while the device is busy.

---

### 2. Interrupt Mechanism

#### The Interrupt Sequence

```
   CPU                        I/O Device          Interrupt Controller
    |                            |                       |
    |  (executing main program)  |                       |
    |                            |                       |
    |                            |--- IRQ (Interrupt --->|
    |                            |    Request)           |
    |                            |                       |
    |<------ INT signal --------|-----------------------|
    |                            |                       |
    |   [CPU completes current   |                       |
    |    instruction]            |                       |
    |                            |                       |
    |--- INTA (Interrupt ------>|----------------------->|
    |    Acknowledge)            |                       |
    |                            |                       |
    |<-- Interrupt Vector # ----|-----------------------|
    |     (identifies device)   |                       |
    |                            |                       |
    |   [CPU saves PC, PSW on   |                       |
    |    stack /切换到 kernel]   |                       |
    |                            |                       |
    |   [CPU loads PC with       |                       |
    |    ISR address from        |                       |
    |    interrupt vector table] |                       |
    |                            |                       |
    |   [ISR executes:           |                       |
    |    save registers,         |                       |
    |    process I/O transfer,   |                       |
    |    restore registers,      |                       |
    |    IRET]                   |                       |
    |                            |                       |
    |   [CPU restores PC, PSW,  |                       |
    |    resumes main program]  |                       |
    |                            |                       |
```

#### Steps in Detail

1. **Device asserts Interrupt Request (IRQ):** The I/O device sends a signal to the interrupt controller.
2. **Interrupt Controller prioritizes:** If multiple interrupts are pending, the highest priority is selected. The controller asserts the INT pin of the CPU.
3. **CPU checks interrupts:** At the end of each instruction execution, the CPU checks the INT line (if interrupts are enabled).
4. **CPU sends INTA (Interrupt Acknowledge):** The CPU responds with an acknowledge signal.
5. **Vector number returned:** The device (or interrupt controller) sends a vector number (e.g., on x86, the vector is a byte 0-255).
6. **CPU saves context:** The Program Counter (PC) and Processor Status Word (PSW) are pushed onto the stack.
7. **CPU loads ISR address:** The interrupt vector table is indexed by the vector number to obtain the Interrupt Service Routine (ISR) address. The CPU loads this into the PC.
8. **ISR executes:** Saves remaining registers (general-purpose), performs the I/O operation, and restores registers.
9. **IRET instruction:** Returns from interrupt. The saved PC and PSW are popped from the stack.
10. **CPU resumes main program:** Execution continues from where it was interrupted.

#### Context Save/Restore in Interrupt

```
Before Interrupt (main program):
   Stack: [ ... ]
   
Interrupt Occurs:
   Stack: [ ... | PC | PSW ]    (hardware saves automatically)
   
ISR Begins:
   Stack: [ ... | PC | PSW | R0 | R1 | ... | Rn ]
   (software saves additional registers)
   
   ... perform I/O transfer ...
   
   Stack: [ ... | PC | PSW | R0 | R1 | ... | Rn ]
   (software restores registers)
   
IRET:
   Stack: [ ... ]               (hardware restores PC, PSW)
   
After Interrupt (resume main program):
   Stack: [ ... ]
```

---

### 3. Types of Interrupts

#### 3.1 Maskable vs Non-Maskable Interrupts

| Feature             | Maskable Interrupt           | Non-Maskable Interrupt (NMI)|
|---------------------|------------------------------|-----------------------------|
| Can be disabled?    | Yes (via IF flag in x86)     | No                          |
| Purpose             | Regular device I/O           | Critical events (power fail, memory error)|
| Priority            | Lower                        | Higher                      |
| Example             | Timer interrupt, keyboard    | Hardware reset, watchdog    |

#### 3.2 Vectored vs Non-Vectored Interrupts

| Feature             | Vectored Interrupt           | Non-Vectored Interrupt      |
|---------------------|------------------------------|-----------------------------|
| Device identification| Sends a vector number       | Single ISR for all devices  |
| ISR lookup          | Uses interrupt vector table  | Fixed ISR address           |
| Flexibility         | Each device has its own ISR  | Must poll to identify device|
| Speed               | Faster (direct dispatch)     | Slower (poll loop inside ISR)|
| Complexity          | Higher hardware              | Lower hardware              |

#### 3.3 Priority Interrupts

Interrupts can be assigned priorities. When multiple interrupts occur:
- The interrupt controller sends the highest-priority interrupt to the CPU.
- A lower-priority ISR can be interrupted by a higher-priority interrupt (nested interrupts).
- Common priority schemes: fixed priority, rotating priority, programmable priority.

**Daisy Chain Priority:**

```
    CPU <---- Device 0 <---- Device 1 <---- Device 2
             (Highest)                   (Lowest)
```

- Devices are connected in a chain.
- The device closest to the CPU has the highest priority.
- If a device receives INTA and does not need service, it passes INTA to the next device.

---

### 4. Direct Memory Access (DMA)

**Direct Memory Access (DMA)** allows I/O devices to transfer data directly to/from memory **without CPU intervention** for each word. A dedicated **DMA controller** handles the transfer.

#### Why DMA is Needed

- In interrupt-driven I/O, the CPU still transfers each byte/word.
- For high-speed devices (disk, network, graphics), having the CPU handle every byte is inefficient.
- DMA offloads the transfer, freeing the CPU for other work.

#### DMA Controller (DMAC)

```
   +==============+        +==============+        +==============+
   |              |        | DMA Controller|        |              |
   |     CPU      |        |              |        |   Memory     |
   |              |        | +----------+ |        |              |
   +======+=======+        | | Address   | |        +======+=======+
          |                | | Register | |               |
          |   HOLD/HLDA    | +----------+ |               |
          |<-------------->| | Word Count| |               |
          |                | | Register | |               |
          |                | +----------+ |               |
          |    Bus         | | Control   | |    Bus        |
          |<-------------->| | Logic     | |<-------------->
          |                | +----------+ |               |
          +================+ +============+ +=============+
                                  |
                                  | DREQ / DACK
                                  |
                             +============+
                             |  I/O Device|
                             | (e.g., Disk)|
                             +============+
```

#### DMA Transfer Steps

1. **CPU programs the DMA controller:**
   - Sets the starting memory address (Address Register).
   - Sets the number of bytes/words to transfer (Word Count Register).
   - Sets the direction (read from device -> memory, or memory -> device).
   - Sets the device identifier.

2. **DMA controller asserts Bus Request (HOLD):** Requests control of the system bus from the CPU.

3. **CPU grants bus (HLDA):** The CPU completes the current bus cycle, then tri-states its bus signals, granting bus control to the DMA controller.

4. **DMA controller asserts DREQ (DMA Request) to the device:** Signals the I/O device to start the transfer.

5. **Device responds with DACK (DMA Acknowledge):** Acknowledges the request.

6. **DMA transfers data directly:** For each word/byte:
   - DMA controller places the address on the address bus.
   - For memory-to-device: reads from memory, writes to device.
   - For device-to-memory: reads from device, writes to memory.
   - Address Register increments.
   - Word Count Register decrements.

7. **Transfer complete:** When Word Count reaches zero, the DMA controller asserts an interrupt to the CPU, indicating completion.

8. **CPU resumes:** The CPU regains bus control and processes the completed I/O operation.

---

### 5. DMA Transfer Modes

#### 5.1 Burst Mode (Block Mode)

- DMA controller transfers an entire block of data in one contiguous sequence.
- DMA retains bus control for the entire duration of the block transfer.
- **Advantage:** Maximum transfer rate.
- **Disadvantage:** CPU is blocked from accessing the bus for the entire duration.

```
   CPU:   XXXX....XXXXXXXXXXXXXXXXXXXX....XXXX
   DMA:      BBBBBBBBBBBBBBBB
   
   X = CPU executing, B = DMA burst transfer
   (dots = CPU idle/suspended)
```

#### 5.2 Cycle Stealing Mode

- DMA transfers one word at a time, then releases the bus.
- DMA "steals" one bus cycle from the CPU for each word.
- **Advantage:** Minimal CPU slowdown -- CPU is only delayed by one cycle per word.
- **Disadvantage:** Lower transfer rate than burst mode.

```
   CPU:   XXXX X X X X X X X X X X X X XXXX
   DMA:     S S S S S S S S S S S S S S
   
   X = CPU executing, S = DMA cycle steal
   (each steal delays the CPU by one bus cycle)
```

#### 5.3 Transparent Mode

- DMA transfers only when the CPU is not using the bus (e.g., when CPU is executing an internal operation).
- **Advantage:** No CPU slowdown at all.
- **Disadvantage:** Slowest transfer rate (depends on availability of free bus cycles).

---

### 6. Performance Comparison

| Aspect                | Programmed I/O          | Interrupt-Driven I/O     | DMA                    |
|-----------------------|------------------------|--------------------------|------------------------|
| CPU involvement       | Every byte             | Every byte (in ISR)      | Only setup and finish  |
| CPU utilization       | Very low               | Moderate                 | High                   |
| Hardware complexity   | Low                    | Medium                   | High                   |
| Transfer overhead     | Highest                | Medium                   | Lowest                 |
| Best for              | Simple/slow devices    | Moderate-speed devices   | High-speed devices     |
| Example               | 8-bit microcontroller  | Keyboard, mouse          | Disk, network, GPU     |

---

### 7. ASCII Diagram: Complete I/O System with Interrupt and DMA

```
          +======================================+
          |              CPU                      |
          |  +-------+   +---------+             |
          |  |  ALU  |   | Control |             |
          |  +-------+   | Unit    |             |
          |               +---------+             |
          |          +--------+                   |
          |          | INT    |                   |
          |          | Logic  |                   |
          |          +--------+                   |
          +====+======+=====+=====+==============+
               |      |     |     |
            Address |  Data  | Control
               |      |     |     |
          +====+======+=====+=====+==============+
          |         System Bus                     |
          +====+======+=====+=====+==============+
               |            |            |
          +========+  +========+  +===========+
          | Memory |  | Interrupt|  | DMA       |
          |        |  | Controller|  | Controller|
          +========+  +========+  +============+
                                   |         |
                              +========+  +========+
                              | Disk   |  | Network|
                              | Ctrlr  |  | Ctrlr  |
                              +========+  +========+
```

---

## Practice Problems

**Q1:** Explain the sequence of events that occurs when an I/O device generates an interrupt, from the moment the device asserts the interrupt line until the CPU begins executing the ISR.

<details>
<summary>Show Answer</summary>
(1) Device asserts IRQ. (2) Interrupt controller prioritizes and sends INT to CPU. (3) CPU finishes current instruction, checks INT line. (4) CPU sends INTA. (5) Controller/device returns vector number. (6) CPU saves PC and PSW on stack. (7) CPU looks up ISR address in interrupt vector table using the vector number. (8) CPU loads ISR address into PC. (9) ISR begins executing, saves additional registers.
</details>

**Q2:** A DMA controller is configured to transfer 64 KB of data from a disk to memory. The bus cycle takes 50 ns. In burst mode, how long does the DMA transfer take? How many bus cycles does the CPU lose?

<details>
<summary>Show Answer</summary>
64 KB = 65536 bytes. Assuming 1 byte per bus cycle: 65536 cycles x 50 ns = 3,276,800 ns = 3.2768 ms. In burst mode, the CPU loses all 65536 bus cycles during this time.
</details>

**Q3:** Compare burst mode and cycle stealing mode in DMA.

<details>
<summary>Show Answer</summary>
Burst mode: DMA holds the bus for the entire block transfer. Maximum transfer rate but CPU is blocked for the whole duration. Cycle stealing: DMA holds the bus for only one word/byte at a time, then releases it. Lower transfer rate but CPU is only delayed by a single bus cycle per word, allowing interleaved CPU execution.
</details>

**Q4:** What is the difference between vectored and non-vectored interrupts?

<details>
<summary>Show Answer</summary>
Vectored interrupts: Each device supplies a unique vector number that the CPU uses to index an interrupt vector table to find the specific ISR for that device. Non-vectored interrupts: All devices share a single ISR entry point. The ISR must poll each device to identify which one generated the interrupt. Vectored is faster but requires more hardware.
</details>

**Q5:** Why can't a non-maskable interrupt (NMI) be disabled, and what kind of events typically trigger an NMI?

<details>
<summary>Show Answer</summary>
NMIs are reserved for critical system events that must be handled immediately regardless of the current state. They cannot be disabled because ignoring them could lead to data corruption or hardware damage. Typical NMI sources: hardware reset button, power failure warning, memory parity error, watchdog timer expiration.
</details>

---