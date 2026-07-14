# I/O transfers program controlled

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 3  
**Date:** 25-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Programmed I/O (Polling)

**Programmed I/O** (also called **polling**) is the simplest method of I/O data transfer. In this method, the CPU is responsible for all aspects of the I/O operation. The CPU must continuously check the status of the I/O device to determine if it is ready for data transfer.

**Key characteristic:** The CPU actively waits for the device, wasting processing cycles.

---

### 2. I/O Instructions

In programmed I/O, the CPU uses special **I/O instructions** to communicate with devices. There are two common approaches:

#### 2.1 Isolated I/O (Port-Mapped I/O)

- Separate address space for I/O ports.
- Special instructions: IN (read from port), OUT (write to port).
- I/O address lines are distinct from memory address lines.
- Used in x86 architecture (IN/OUT instructions).

Example (x86 assembly):
```asm
IN   AL, 60h      ; Read byte from port 0x60 (keyboard controller)
OUT  60h, AL      ; Write byte to port 0x60
```

#### 2.2 Memory-Mapped I/O

- I/O devices are mapped into the main memory address space.
- Regular memory instructions (LOAD, STORE) are used for I/O.
- No special I/O instructions needed.
- Used in ARM, RISC-V, and many embedded systems.

Example (pseudo-assembly):
```asm
LOAD R1, [KEYBOARD_STATUS]   ; Read status register at memory address KEYBOARD_STATUS
STORE [KEYBOARD_DATA], R2    ; Write data to device at memory address KEYBOARD_DATA
```

| Feature            | Isolated I/O                  | Memory-Mapped I/O           |
|--------------------|-------------------------------|-----------------------------|
| Address space      | Separate                      | Shared with memory          |
| Instructions       | IN, OUT (special)             | LOAD, STORE (same as memory)|
| Address lines      | Fewer (typically 16-bit port) | Full address bus            |
| Hardware protection| Yes (dedicated instructions)  | Requires MMU configuration  |
| Example arch       | x86                           | ARM, RISC-V, AVR            |

---

### 3. Steps in Programmed I/O

The typical sequence for a programmed I/O data transfer (e.g., reading a character from keyboard):

#### Step-by-step Process

```
              CPU                     I/O Device
               |                          |
    Step 1:    |--- Read Status Reg ----->|
        (CPU issues a read of the I/O module's status register)
               |                          |
    Step 2:    |<-- Status (Busy/Ready) --|
        (I/O module returns the status; CPU checks the ready bit)
               |                          |
    Step 3:    |                          |  (if NOT ready, go back to Step 1)
               |                          |
        (if READY, proceed to data transfer)
               |                          |
    Step 4:    |--- Read/Write Data ----> |
        (CPU reads data from or writes data to the I/O module's data register)
               |                          |
    Step 5:    |<-- Data (on read) --/--> |
        (Data is transferred between CPU and I/O module)
               |                          |
    Step 6:    |--- Set status to ready-->| (for next operation)
        (I/O module updates status bit to signal completion)
               |                          |
```

**Detailed steps for a keyboard input operation:**

1. **CPU reads the status register** of the keyboard I/O module.
   - The status register contains a **ready bit** (often bit 0 or bit 7).
   - Example: `IN AL, 64h` (read keyboard status port).

2. **CPU checks the ready bit.**
   - If ready bit = 0: device is busy / no data available. Go back to step 1.
   - If ready bit = 1: data is available. Proceed to step 3.

3. **CPU reads the data register** to get the keyboard scan code.
   - Example: `IN AL, 60h` (read keyboard data port).

4. **CPU processes the character** (e.g., converts scan code to ASCII, stores in buffer).

5. **Repeat** for the next character.

#### Pseudocode for Programmed Keyboard Input

```
function read_keyboard_char():
    loop:
        status = read_port(KEYBOARD_STATUS_PORT)   // Step 1
        if (status & READY_BIT) == 0:               // Step 2: check ready bit
            goto loop                               // Poll again
        data = read_port(KEYBOARD_DATA_PORT)        // Step 3: read data
        return data
```

---

### 4. Programmed I/O Example: Printing a String

Consider a program that prints "Hello" to a line printer using programmed I/O.

```
Memory: "Hello" stored starting at address STRING

Program:
    R1 = address of STRING           ; Pointer to string
    R2 = 0                           ; Character counter (optional)

LOOP:
    [Poll printer status]
    IN  AL, PRINTER_STATUS_PORT      ; Read status register
    TEST AL, READY_BIT               ; Check if printer is ready
    JZ  LOOP                         ; If not ready, poll again

    [Device is ready, send a character]
    LOAD R3, [R1]                    ; Load character from string
    OUT PRINTER_DATA_PORT, R3        ; Send character to printer

    [Advance pointer]
    R1 = R1 + 1                      ; Next character
    CMP R3, 0                        ; Check for null terminator
    JNZ LOOP                         ; Continue if not null

    [Done]
    HALT
```

**Problem:** The CPU spends most of its time polling (checking the status register in a loop), doing no useful work.

---

### 5. Advantages and Disadvantages

#### Advantages

| Advantage | Explanation |
|-----------|-------------|
| Simple to implement | No interrupt controller, DMA controller, or complex hardware needed |
| Full CPU control | CPU has complete control over when and how transfers occur |
| Predictable timing | No interrupts to cause unpredictable execution flow |
| Low hardware cost | Minimal additional hardware beyond the I/O module |
| Easy to debug | CPU executes a deterministic sequence of instructions |

#### Disadvantages

| Disadvantage | Explanation |
|--------------|-------------|
| Wasteful of CPU time | CPU spends most time in a polling loop, unable to execute other tasks |
| Poor for high-speed devices | If the device is fast, polling frequency must be high, consuming even more CPU time |
| Poor for low-speed devices | Even waiting for a slow key press, the CPU polls thousands of times before data arrives |
| No multitasking efficiency | In a multiprogramming system, polling blocks the CPU from running other processes |
| Scalability problem | Multiple devices require multiple polling loops, making the situation worse |

#### Quantitative Waste

Consider a keyboard with a human typing at 50 characters per second (20 ms between keystrokes). If a polling check takes 200 ns:

- CPU polls every 200 ns.
- Number of polls per keystroke = 20 ms / 200 ns = 100,000 polls.
- Useful work done per keystroke: 1 data transfer.
- Efficiency = (time for 1 data transfer) / (time for 100,000 polls + 1 data transfer) ~= 0.001%.

---

### 6. Comparison with Interrupt-Driven I/O

| Aspect                | Programmed I/O (Polling)        | Interrupt-Driven I/O           |
|-----------------------|---------------------------------|--------------------------------|
| CPU waiting method    | Active polling (busy-wait)      | Device notifies CPU via interrupt |
| CPU utilization       | Low (wasted cycles)             | High (CPU does other work)     |
| Hardware complexity   | Low                             | Medium (needs interrupt controller)|
| Response latency      | Depends on polling frequency    | Immediate (device-driven)      |
| Best suited for       | Simple systems, well-defined timing| General purpose, multitasking OS |
| Multiple devices      | Complex polling sequence        | Easy (priorities handle it)    |

---

### 7. When is Programmed I/O Still Useful?

- **Very simple microcontrollers** (8-bit MCUs without interrupt capability).
- **Devices with predictable, high-speed data rates** (e.g., reading from a FIFO buffer in a fast ADC).
- **Critical sections** where interrupts must be disabled and polling is the safe alternative.
- **Legacy/simple systems** like 8051-based embedded systems.

---

## Practice Problems

**Q1:** A CPU polls a device every 400 ns. The device becomes ready for data transfer every 2 ms. How many polling cycles are wasted per data transfer?

<details>
<summary>Show Answer</summary>
Time between ready states = 2 ms = 2,000,000 ns. Poll interval = 400 ns. Number of polls = 2,000,000 / 400 = 5,000 polls. Of these, only the last poll finds the device ready. Wasted polls = 5,000 - 1 = 4,999.
</details>

**Q2:** Write pseudocode for polling a device that requires checking two status bits: READY (bit 0) and ERROR (bit 1) before performing a data read.

<details>
<summary>Show Answer</summary>
```
function read_byte():
    loop:
        status = read_device_status()
        if (status & 0x02) != 0:           // Check ERROR bit
            handle_error()
            return error_code
        if (status & 0x01) != 0:           // Check READY bit
            data = read_device_data()
            return data
        goto loop                          // Keep polling
```
</details>

**Q3:** Explain why programmed I/O is inefficient in a multitasking operating system.

<details>
<summary>Show Answer</summary>
In a multitasking OS, the CPU should be shared among multiple processes. With programmed I/O, a process performing I/O enters a polling loop where it repeatedly checks device status. During this time, the CPU cannot be used by any other process (unless the OS implements a timer interrupt to preempt the polling process). This wastes CPU cycles that could otherwise be used to execute other processes.
</details>

**Q4:** What is the difference between isolated I/O and memory-mapped I/O in terms of I/O instructions used?

<details>
<summary>Show Answer</summary>
Isolated I/O uses dedicated I/O instructions (e.g., IN and OUT on x86) that access a separate I/O address space. Memory-mapped I/O uses the same LOAD and STORE instructions used for memory access, treating device registers as locations in the memory address space. The choice affects instruction set design, address space partitioning, and hardware protection.
</details>

**Q5:** A system has three devices: A (ready every 1 us, fast), B (ready every 50 ms, slow), C (ready every 10 ms, medium). The CPU polls devices in round-robin order A -> B -> C, taking 100 ns per poll. Calculate the maximum polling latency for device B (how long after it becomes ready before it is polled?).

<details>
<summary>Show Answer</summary>
One round = 3 polls x 100 ns = 300 ns. If device B becomes ready immediately after it was polled, it must wait for A and C to be polled next. That is 2 polls = 200 ns latency. In the worst case, B becomes ready just after B was polled, and the next poll of B happens after polling A and C in the current cycle, which takes 200 ns. So max latency = 200 ns, which is negligible compared to 50 ms -- so polling order is fine. (Problem occurs when many slow devices are polled with high frequency.)
</details>

---