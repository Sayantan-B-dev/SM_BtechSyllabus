# CPU, memory, input-output subsystems.

**Course:** Computer Organization and Architecture  
**Module:** 1 | **Lecture:** 1  
**Date:** 08-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Von Neumann Architecture Overview

The Von Neumann architecture (also called the Princeton architecture) is the foundational design model for most modern computers. It was first described by John von Neumann in 1945 in his "First Draft of a Report on the EDVAC."

**Key characteristics:**
- A single, shared memory space holds both instructions (programs) and data.
- The processing unit fetches instructions from memory, decodes them, and executes them sequentially.
- The concept is called the **stored program concept** -- the program is stored in memory as binary code, not wired into the hardware.

**Basic components of the Von Neumann architecture:**
1. Central Processing Unit (CPU)
2. Memory Unit
3. Input/Output (I/O) subsystems
4. System Bus (connects all components)

### 2. The Stored Program Concept

The stored program concept is the most important idea in computer architecture. Before this concept, computers were "programmed" by physically rewiring the hardware (e.g., the ENIAC). The stored program concept states:

- Both **instructions** (the program) and **data** are stored in the **same memory**.
- The CPU reads instructions from memory one at a time and executes them.
- A program can be changed simply by writing new data into memory -- no hardware changes required.

This is why we call it a "stored program" -- the program is stored as a pattern of bits in memory, just like data.

### 3. CPU (Central Processing Unit)

The CPU is the "brain" of the computer. It executes instructions stored in memory. It has three main internal components:

#### 3.1 ALU (Arithmetic Logic Unit)
- Performs arithmetic operations: addition, subtraction, multiplication, division.
- Performs logical operations: AND, OR, NOT, XOR, comparison.
- It receives operands from registers and returns results to registers.
- Status flags (carry, zero, overflow, sign) are set based on results.

#### 3.2 Control Unit (CU)
- Fetches instructions from memory.
- Decodes instructions to determine what operation to perform.
- Generates **control signals** that coordinate the ALU, registers, memory, and I/O.
- Manages the instruction cycle (fetch-decode-execute).

#### 3.3 Registers
- Small, very fast storage locations inside the CPU.
- Examples: Program Counter (PC), Instruction Register (IR), Memory Address Register (MAR), Memory Buffer Register (MBR), Accumulator (AC), General Purpose Registers (R0, R1, ..., Rn).
- Registers are the fastest type of memory in the computer hierarchy.

### 4. Memory

Memory stores both instructions and data. It is organized as a linear array of addressable locations (bytes or words).

#### 4.1 RAM (Random Access Memory)
- **Volatile**: data is lost when power is turned off.
- **Read/Write**: both read and write operations are allowed.
- Used for the main memory where active programs and data reside.
- Types: SRAM (static), DRAM (dynamic).

#### 4.2 ROM (Read-Only Memory)
- **Non-volatile**: data is retained even when power is off.
- Primarily **read** operations (though some types can be written under special conditions).
- Used for storing firmware, boot loaders, BIOS/UEFI.
- Types: PROM, EPROM, EEPROM, Flash memory.

#### 4.3 Cache Hierarchy
Cache is a small, fast memory between the CPU and main memory. It stores copies of frequently accessed data/instructions to reduce access time.

**Levels of cache:**

```
+-----------+   +-----------+   +-----------+
| CPU Core  |-->| L1 Cache  |-->| L2 Cache  |
+-----------+   +-----------+   +-----------+
                                     |
                                     v
                               +-----------+
                               | L3 Cache  |
                               +-----------+
                                     |
                                     v
                               +-----------+
                               | Main RAM  |
                               +-----------+
```

- **L1 Cache**: smallest (16-64 KB), fastest, often split into instruction (L1i) and data (L1d).
- **L2 Cache**: larger (128 KB - 1 MB), slightly slower, often per-core.
- **L3 Cache**: largest (2-32 MB), shared among all cores, slower than L1/L2.

**Why hierarchy?** Principle of locality: programs tend to access the same memory locations repeatedly (temporal locality) or nearby locations (spatial locality). Caching exploits this.

### 5. I/O Subsystems

Input/Output subsystems allow the computer to communicate with the outside world.

#### 5.1 Input Devices
- Keyboard, mouse, scanner, microphone, camera, touch screen, sensors.
- Convert physical input into digital signals for the computer.

#### 5.2 Output Devices
- Monitor, printer, speakers, headphones, actuators.
- Convert digital signals from the computer into human-perceptible form.

#### 5.3 Storage Devices (Secondary Memory)
- **Hard Disk Drives (HDD)**: magnetic storage, high capacity, slower.
- **Solid State Drives (SSD)**: flash-based, faster, no moving parts.
- **Optical Discs**: CD, DVD, Blu-ray.
- **Magnetic Tape**: archival/backup.
- These are non-volatile and provide long-term storage.

### 6. System Bus

The system bus is a communication pathway that connects the CPU, memory, and I/O devices. It consists of three separate buses:

#### 6.1 Data Bus
- Carries **data** between components.
- **Bidirectional**: data can flow both to and from the CPU.
- Width (number of lines) determines how many bits can be transferred at once: 8-bit, 16-bit, 32-bit, 64-bit buses.
- Example: a 64-bit data bus can transfer 8 bytes per cycle.

#### 6.2 Address Bus
- Carries **memory addresses** from the CPU to memory or I/O.
- **Unidirectional**: address flows only from CPU to memory/I/O.
- Width determines maximum addressable memory: an n-bit address bus can address 2^n memory locations.
- Example: a 32-bit address bus addresses up to 4 GB (2^32 bytes).

#### 6.3 Control Bus
- Carries **control signals** (read, write, interrupt, clock, reset, etc.).
- Some signals are unidirectional, some bidirectional.
- Examples:
  - **MemRead**: CPU requests memory read.
  - **MemWrite**: CPU requests memory write.
  - **I/ORead**: CPU requests input from I/O device.
  - **I/OWrite**: CPU requests output to I/O device.
  - **Interrupt Request (IRQ)**: I/O device signals the CPU.
  - **Clock**: synchronizes all components.

### 7. Block Diagram of a Complete Computer System

```
                     COMPUTER SYSTEM BLOCK DIAGRAM
    
+---------------------+          +-----------------------+
|       CPU           |          |       MEMORY          |
|                     |          |                       |
|  +---------------+  |          |  +-----------------+  |
|  | Control Unit  |  | Address  |  |                 |  |
|  |               |--+--Bus-----+->|   RAM (Main     |  |
|  |   (CU)        |  |          |  |    Memory)      |  |
|  +-------+-------+  |          |  |                 |  |
|          |          |          |  +-----------------+  |
|          v          |          |                       |
|  +---------------+  |          |  +-----------------+  |
|  |      ALU      |<-+-Data Bus-+->|   ROM (BIOS/    |  |
|  |               |  |          |  |   Firmware)     |  |
|  +-------+-------+  |          |  +-----------------+  |
|          |          |          |                       |
|  +-------+-------+  |          |  +-----------------+  |
|  |   Registers   |  |          |  |   Cache Memory  |  |
|  |  (PC, IR,     |  |          |  |  (L1, L2, L3)   |  |
|  |   MAR, MBR,   |  |          |  +-----------------+  |
|  |   R0-Rn, PSW) |  |          +-----------------------+
|  +---------------+  |                     |
+---------------------+                     |
          |                                 |
          |  System Bus                     |
          |  (Data + Address + Control)     |
          |                                 |
          v                                 v
+---------------------+          +-----------------------+
|    I/O SUBSYSTEM    |          |    I/O SUBSYSTEM      |
|                     |          |                       |
|  +---------------+  |          |  +-----------------+  |
|  |  Input        |  |          |  |  Output         |  |
|  |  Devices      |  |          |  |  Devices        |  |
|  |  (Keyboard,   |  |          |  |  (Monitor,      |  |
|  |   Mouse, etc) |  |          |  |   Printer, etc) |  |
|  +---------------+  |          |  +-----------------+  |
|                     |          |                       |
|  +---------------+  |          |  +-----------------+  |
|  |  Storage      |  |          |  |  Network I/F    |  |
|  |  (HDD, SSD,   |  |          |  |  (Ethernet,     |  |
|  |   Optical)    |  |          |  |   WiFi)         |  |
|  +---------------+  |          |  +-----------------+  |
+---------------------+          +-----------------------+
```

### 8. How CPU, Memory, and I/O Interact

The interaction follows a cycle called the **instruction cycle**:

```
+--------+     +--------+     +----------+     +----------+
| FETCH  |---->| DECODE |---->| EXECUTE  |---->| STORE    |
| (from  |     | (by CU)|     | (by ALU |     | (results |
| Memory)|     |        |     |  or I/O)|     | to Mem/Reg)
+--------+     +--------+     +----------+     +----------+
     ^                                               |
     |                                               |
     +---------------------(loop)--------------------+
```

**Step-by-step example: ADD two numbers**

1. **FETCH**: CPU places the address of the next instruction (from PC) on the address bus. Control unit sends a "memory read" signal on the control bus. Memory reads the instruction and places it on the data bus. CPU loads it into IR (Instruction Register).

2. **DECODE**: Control unit decodes the instruction in IR (identifies it as "ADD").

3. **EXECUTE**: The control unit sends signals to:
   - Read operand1 from memory (address bus -> MemRead -> data bus -> MBR -> register).
   - Read operand2 from memory.
   - ALU performs addition.
   - Result stored in destination.

4. **STORE**: If needed, result is written back to memory or left in register.

**I/O interaction:**
- **Programmed I/O**: CPU actively waits and checks I/O device status (polling).
- **Interrupt-driven I/O**: I/O device sends an interrupt signal to CPU when ready. CPU suspends current program, handles I/O, then resumes.
- **DMA (Direct Memory Access)**: I/O device transfers data directly to/from memory without CPU involvement. A DMA controller manages the transfer, freeing the CPU for other tasks.

### 9. The System Bus and Data Flow Example

Consider the instruction: `LOAD R1, 1000` (load the contents of memory address 1000 into register R1).

```
Step 1: CPU places address 1000 on Address Bus
Step 2: CPU asserts "MemRead" on Control Bus
Step 3: Memory reads address 1000, places data on Data Bus
Step 4: CPU reads data from Data Bus into MBR
Step 5: CPU transfers MBR to R1
```

```
+-------+
|  CPU  |---> Address Bus (1000) ------------------> Memory
|       |---> Control Bus (MemRead active) ---------> Memory
|       |<--- Data Bus  (contents of addr 1000) ----- Memory
+-------+
```

### 10. Summary of Key Concepts

| Concept | Description |
|---------|-------------|
| Von Neumann Architecture | Single memory for instructions and data; sequential execution |
| Stored Program Concept | Programs stored as binary data in memory |
| CPU | Fetches, decodes, and executes instructions |
| ALU | Performs arithmetic and logical operations |
| Control Unit | Generates control signals, coordinates execution |
| Registers | Fast on-CPU storage for temporary data and addresses |
| RAM | Volatile main memory for active programs/data |
| ROM | Non-volatile memory for firmware |
| Cache | Fast intermediate memory exploiting locality |
| System Bus | Data + Address + Control buses connecting components |

---

## Practice Problems

1. **Problem**: A computer has a 32-bit address bus and a 64-bit data bus. What is the maximum amount of memory it can address? How many bytes can it transfer in one bus cycle?
   **Answer**: With a 32-bit address bus, it can address 2^32 = 4,294,967,296 locations (4 GB). With a 64-bit data bus, it can transfer 64 bits = 8 bytes per bus cycle.

2. **Problem**: Explain why the Von Neumann architecture is also known as a "stored-program" computer.
   **Answer**: Because the program instructions are stored in memory as binary data, just like the data. The CPU fetches instructions from memory, decodes them, and executes them. Programs can be changed by writing new instructions into memory, without rewiring the hardware.

3. **Problem**: A program accesses memory locations 100, 101, 102, 103, 100, 101, 102, 103 repeatedly. Which type of locality does this exhibit? How would cache help?
   **Answer**: This exhibits both spatial locality (sequential addresses 100-103) and temporal locality (same addresses repeated). Cache stores copies of these locations after the first access; subsequent accesses are serviced from fast cache instead of slow main memory.

4. **Problem**: Draw a simplified diagram showing how the data bus, address bus, and control bus connect CPU, memory, and an I/O device.
   **Answer**: (ASCII diagram)
   ```
   CPU --[Address Bus]--> Memory
   CPU --[Address Bus]--> I/O Device
   CPU <--[Data Bus]----> Memory
   CPU <--[Data Bus]----> I/O Device
   CPU --[Control Bus]--> Memory (MemRead, MemWrite)
   CPU --[Control Bus]--> I/O Device (I/ORead, I/OWrite)
   I/O Device --[IRQ]--> CPU (interrupt)
   ```

5. **Problem**: In the context of DMA, why is it beneficial compared to programmed I/O?
   **Answer**: In programmed I/O, the CPU must repeatedly check the I/O device status (polling), wasting CPU cycles. In interrupt-driven I/O, the CPU is interrupted for each data transfer, still consuming CPU time for data movement. DMA allows the DMA controller to transfer data directly between I/O device and memory without CPU involvement, freeing the CPU to execute other tasks during the transfer.
