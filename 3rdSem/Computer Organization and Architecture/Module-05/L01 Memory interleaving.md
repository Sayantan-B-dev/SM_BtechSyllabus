# Memory interleaving

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 1  
**Date:** 07-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. What is Memory Interleaving?

Memory interleaving is a technique that divides the main memory into a number of modules (or banks) that can be accessed simultaneously. The purpose is to reduce memory access time by exploiting parallelism. Instead of having one large monolithic memory, we split it into N independent modules, each with its own address buffer, data buffer, and control logic.

When the CPU requests a sequence of consecutive addresses, these requests can be distributed across different modules. While one module is busy servicing a request (accessing its storage cells), another module can simultaneously service a different request. This overlapping of memory accesses improves the effective memory bandwidth.

### 2. High-Order Interleaving (Consecutive Addresses in Same Module)

In high-order interleaving, the higher-order address bits select the memory module, and the lower-order bits select the word within that module. Consecutive memory addresses fall within the same module.

**Address division:**

```
+------------------+-------------------+
| Module Select    | Word/Offset       |
| (high-order bits)| (low-order bits)  |
+------------------+-------------------+
```

**Example:** For 4 modules (M0, M1, M2, M3), each with 4 words:

```
Module 0 (M0):  addresses 0,  1,  2,  3
Module 1 (M1):  addresses 4,  5,  6,  7
Module 2 (M2):  addresses 8,  9,  10, 11
Module 3 (M3):  addresses 12, 13, 14, 15
```

Since consecutive addresses (e.g., 0, 1, 2, 3) all map to the same module M0, a sequential memory access pattern causes all requests to go to the same module. This means no parallelism is exploited for sequential access. High-order interleaving is simple but does not improve sequential access performance.

### 3. Low-Order Interleaving (Consecutive Addresses Across Modules)

In low-order interleaving, the lower-order address bits select the memory module, and the higher-order bits select the word within that module. Consecutive memory addresses are distributed across different modules.

**Address division:**

```
+------------------+-------------------+
| Word/Offset      | Module Select     |
| (high-order bits)| (low-order bits)  |
+------------------+-------------------+
```

**Example:** For 4 modules (M0, M1, M2, M3), each with 4 words:

```
Module 0 (M0):  addresses 0,  4,  8,  12
Module 1 (M1):  addresses 1,  5,  9,  13
Module 2 (M2):  addresses 2,  6,  10, 14
Module 3 (M3):  addresses 3,  7,  11, 15
```

Now consecutive addresses (0, 1, 2, 3) map to different modules (M0, M1, M2, M3). A sequential access pattern can exploit all four modules in parallel. This significantly improves effective bandwidth for sequential access patterns.

### 4. Number of Modules

The number of modules is typically a power of 2: 2, 4, 8, 16, etc. The choice depends on the memory bus width, the degree of parallelism desired, and cost considerations. More modules give higher potential parallelism but also increase bus complexity and cost.

If there are N modules and each module has an access time of T_access, the effective access time for a sequence of consecutive reads can approach: T_effective = T_access / N (in the ideal case where requests can be perfectly pipelined).

### 5. Address Mapping Formulas

Let:
- N = Number of memory modules
- M = Size of each module (number of words per module)
- A = Physical address (word address)

**High-Order Interleaving:**
```
Module Number = floor(A / M)
Word Offset   = A mod M
```

**Low-Order Interleaving:**
```
Module Number = A mod N
Word Offset   = floor(A / N)
```

If addresses are in bytes and block size is B bytes per module access:

**Low-Order Interleaving (byte address):**
```
Module Number = (byte_address / B) mod N
Block Address = floor(byte_address / (B * N))
Offset within block = byte_address mod B
```

### 6. Access Time Improvement

Without interleaving, accessing N consecutive words takes: T_sequential = N * T_access

With N modules and low-order interleaving (ideal pipelining), accessing N consecutive words takes approximately: T_interleaved = T_access + (N - 1) * T_bus

where T_bus is the bus transfer time per word (much smaller than T_access). For large N, the speedup is approximately: Speedup = N / (1 + (N-1) * T_bus / T_access)

If T_bus is negligible compared to T_access, speedup approaches N.

### 7. ASCII Diagram: 4-Module Interleaved Memory

```
                        +-------------------------------------------+
                        |              CPU / Memory Controller       |
                        +-------------------------------------------+
                                        |       |       |       |
                             +----------+       |       |       +----------+
                             |                  |       |                  |
                        +----v----+       +-----v---+  +-----v---+   +----v----+
                        | Module 0 |       | Module 1|  | Module 2|   | Module 3|
                        | Bank 0   |       | Bank 1  |  | Bank 2  |   | Bank 3  |
                        +----------+       +---------+  +---------+   +----------+
                        | Word 0   |       | Word 1  |  | Word 2  |   | Word 3  |
                        | Word 4   |       | Word 5  |  | Word 6  |   | Word 7  |
                        | Word 8   |       | Word 9  |  | Word 10 |   | Word 11 |
                        | Word 12  |       | Word 13 |  | Word 14 |   | Word 15 |
                        | ...      |       | ...     |  | ...     |   | ...     |
                        +----------+       +---------+  +---------+   +----------+

        Low-order interleaving address assignment:
        Address bits:  A1 A0  -> Module Select (2 bits for 4 modules)
                       A3 A2  -> Word Select within module
                       Higher bits -> Block number

        Example for 16 words (4 modules x 4 words each):
        Addr 0  -> M0, Word 0      Addr 1  -> M1, Word 0
        Addr 2  -> M2, Word 0      Addr 3  -> M3, Word 0
        Addr 4  -> M0, Word 1      Addr 5  -> M1, Word 1
        Addr 6  -> M2, Word 1      Addr 7  -> M3, Word 1
        Addr 8  -> M0, Word 2      Addr 9  -> M1, Word 2
        Addr 10 -> M2, Word 2      Addr 11 -> M3, Word 2
        Addr 12 -> M0, Word 3      Addr 13 -> M1, Word 3
        Addr 14 -> M2, Word 3      Addr 15 -> M3, Word 3
```

### 8. Worked Example: 4-Module Interleaving

**Problem:** A memory system uses 4-way low-order interleaving. Each memory module has an access time of 60 ns. The bus transfer time per word is 10 ns. The CPU reads a block of 8 consecutive words starting at address 0.

(a) How long would this take without interleaving (single module)?
(b) How long with 4-way low-order interleaving?

**Solution (a):** Without interleaving:
- Each word access: 60 ns (access) + 10 ns (transfer) = 70 ns
- 8 words: 8 x 70 = 560 ns

**Solution (b):** With 4-way low-order interleaving:
- Module assignment for addresses 0-7:
  - Addr 0 -> M0, Addr 1 -> M1, Addr 2 -> M2, Addr 3 -> M3
  - Addr 4 -> M0, Addr 5 -> M1, Addr 6 -> M2, Addr 7 -> M3
- Timeline:
  - t=0 to 60: M0 starts accessing addr 0; M1, M2, M3 idle
  - t=10 to 70: M0 transfers addr 0 (10 ns); M1 starts accessing addr 1 at t=10
  - t=20 to 80: M1 transfers addr 1; M2 starts accessing addr 2 at t=20
  - t=30 to 90: M2 transfers addr 2; M3 starts accessing addr 3 at t=30
  - t=40 to 100: M3 transfers addr 3; M0 starts accessing addr 4 at t=40
  - t=70 to 130: M0 transfers addr 4; M1 starts accessing addr 5 at t=70
  - t=80 to 140: M1 transfers addr 5; M2 starts accessing addr 6 at t=80
  - t=90 to 150: M2 transfers addr 6; M3 starts accessing addr 7 at t=90
  - t=100 to 160: M3 transfers addr 7
- Total time: first access starts at t=0, last transfer ends at t=160 ns
- Effective time = 60 + 7 x 10 = 130 ns  (first access + remaining 7 transfers)
- Speedup = 560 / 160 = 3.5x

---

## Practice Problems

**Problem 1:** A memory system has 8 modules with low-order interleaving. Each module access time is 50 ns, bus transfer time is 5 ns. How long does it take to read 16 consecutive words?

<details>
<summary>Show Answer</summary>
First word: 50 ns access + 5 ns transfer = 55 ns (but first transfer overlaps with next access). Total = 50 + 15 x 5 = 125 ns. Without interleaving: 16 x 55 = 880 ns. Speedup = 7.04x.
</details>

**Problem 2:** Given a 32-bit address and 16 memory modules, how many bits are used for module selection in low-order interleaving if each module stores 2^28 words?

<details>
<summary>Show Answer</summary>
16 modules require log2(16) = 4 bits for module selection. The remaining 28 bits are for word offset within the module.
</details>

**Problem 3:** Distinguish between high-order and low-order interleaving in terms of sequential access performance.

<details>
<summary>Show Answer</summary>
High-order interleaving places consecutive addresses in the same module, so sequential accesses hit the same module -- no parallelism. Low-order interleaving distributes consecutive addresses across different modules, enabling overlapped access and improved bandwidth for sequential patterns.
</details>

**Problem 4:** A system uses 4-way low-order interleaving with 32-bit addresses and 4-byte words. What are the module number and word offset for address 0x1C (28 decimal)?

<details>
<summary>Show Answer</summary>
Word address = 28 / 4 = 7 (word number). Module = 7 mod 4 = 3 (M3). Word offset = floor(7 / 4) = 1 (word 1 within the module). Byte offset within word = 28 mod 4 = 0.
</details>

**Problem 5:** Prove that low-order interleaving with N modules reduces the effective memory access time for a burst of N consecutive reads to approximately T_access + (N-1) * T_bus.

<details>
<summary>Show Answer</summary>
The first access takes T_access. After the first module completes its access in T_access, it starts transferring on the bus for T_bus. Each subsequent module can start its access T_bus after the previous one (pipelined start). The last module finishes its transfer at time T_access + (N-1) * T_bus, assuming the bus transfers are non-overlapping for each word.
</details>