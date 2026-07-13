# Parallel Processors: Introduction to parallel processors

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 5  
**Date:** 16-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Introduction

As clock frequency scaling reached physical limits (power density, heat dissipation), architects turned to **parallelism** to continue improving performance. Parallel processors use multiple processing elements to execute multiple instructions or tasks simultaneously.

## Flynn's Taxonomy

Michael Flynn (1966) classified computer architectures based on two concepts:
- **Instruction stream**: Sequence of instructions executed by the machine.
- **Data stream**: Sequence of data operated on by the instructions.

Each can be **single** (one) or **multiple** (many), giving four categories:

```
                     Data Streams
                  Single     Multiple
                +----------+----------+
Instruction     |  SISD    |  SIMD    |
Stream   Single |          |          |
                +----------+----------+
                |  MISD    |  MIMD    |
         Multiple|          |          |
                +----------+----------+
```

### SISD (Single Instruction, Single Data)

- One instruction stream, one data stream.
- Traditional uniprocessor (von Neumann machine).
- One instruction processes one data element at a time.
- **Examples**: Most single-core processors, early PCs.

```
[Control Unit] --> [Processor] --> [Memory]
     |                  |
 Instruction         Data
```

### SIMD (Single Instruction, Multiple Data)

- One instruction stream, multiple data streams.
- All processing elements execute the SAME instruction on DIFFERENT data elements.
- Exploits **data-level parallelism**.

```
[Control Unit] --> [PE 0] --> [Data 0]
                 -> [PE 1] --> [Data 1]
                 -> [PE 2] --> [Data 2]
                 -> [PE 3] --> [Data 3]
```

- **Examples**: Vector processors, GPU shader cores, Intel MMX/SSE/AVX, ARM NEON.
- **Use case**: Image processing, matrix multiplication, multimedia applications.

### MISD (Multiple Instruction, Single Data)

- Multiple instruction streams, one data stream.
- Different instructions operate on the same data element.
- Rarely used in practice.
- **Examples**: Some fault-tolerant systems (multiple processors execute different instructions on same data, compare results). Not commercially widespread.

```
[Control Unit 0] --> [PE 0] --> +
                                |
[Control Unit 1] --> [PE 1] --> +--> [Single Data]
                                |
[Control Unit 2] --> [PE 2] --> +
```

### MIMD (Multiple Instruction, Multiple Data)

- Multiple instruction streams, multiple data streams.
- Each processing element fetches its own instructions and operates on its own data.
- Most common form of parallel processor today.
- **Examples**: Multicore CPUs, cluster computers, distributed systems.

```
[Control Unit 0] --> [PE 0] --> [Data 0]
[Control Unit 1] --> [PE 1] --> [Data 1]
[Control Unit 2] --> [PE 2] --> [Data 2]
[Control Unit 3] --> [PE 3] --> [Data 3]
```

**Two subcategories of MIMD**:
- **Shared memory**: All processors share a common address space.
- **Message passing**: Each processor has private memory, communicate via messages.

## Shared Memory Multiprocessors

All processors share a single physical address space. Any processor can access any memory location using load/store instructions.

### UMA (Uniform Memory Access)

- All processors have the same access time to all memory locations.
- Memory is equally distant from all processors.

```
    +--------+    +--------+    +--------+
    |  P 0   |    |  P 1   |    |  P 2   |
    +--------+    +--------+    +--------+
         |            |            |
    +----+------------+------------+----+
    |         System Interconnect       |
    |    (Bus / Crossbar / Switch)      |
    +----+------------+------------+----+
         |            |            |
    +--------+    +--------+    +--------+
    |  M 0   |    |  M 1   |    |  M 2   |
    +--------+    +--------+    +--------+
```

**Characteristics**:
- Uniform latency: Any processor to any memory module takes same time.
- Symmetric: All processors are peers.
- Easier to program (shared address space).
- **Limited scalability**: Bus or interconnect bandwidth becomes bottleneck beyond ~8-32 processors.

### NUMA (Non-Uniform Memory Access)

- Access time depends on which memory module is accessed.
- Each processor has "local" memory (fast access) and can access "remote" memory (slower access over interconnect).

```
    +--------+        +--------+        +--------+
    |  P 0   |        |  P 1   |        |  P 2   |
    +--------+        +--------+        +--------+
    |  M 0   |        |  M 1   |        |  M 2   |
    +--------+        +--------+        +--------+
         \              |              /
          \             |             /
           +-------+---------+-------+
                   | Interconnect |
                   +--------------+
```

**Local access**: P0 to M0 (fast, e.g., 100 ns).
**Remote access**: P0 to M1 (slower, e.g., 300 ns).

**Characteristics**:
- Non-uniform: Latency varies by location. Programmers must be aware of memory placement for performance.
- More scalable: Can support hundreds of processors (e.g., SGI Origin, AMD EPYC with multiple CCX/CCD).
- **ccNUMA** (cache-coherent NUMA): Hardware maintains cache coherence across the entire system.

**Comparison: UMA vs NUMA**

| Feature | UMA | NUMA |
|---|---|---|
| Access time | Uniform | Non-uniform |
| Scalability | Low (8-32 CPUs) | High (100s of CPUs) |
| Programming | Easy (uniform) | Harder (data locality matters) |
| Cost | Lower interconnect | Higher complexity |
| Example | Early SMP systems | Modern multi-socket servers |

## Message Passing Systems

Processors have **private memory** and communicate by sending messages over a network.

```
    +--------+        +--------+        +--------+
    |  P 0   |        |  P 1   |        |  P 2   |
    +--------+        +--------+        +--------+
    | Priv M |        | Priv M |        | Priv M |
    +--------+        +--------+        +--------+
         |                |                |
    +----+----------------+----------------+----+
    |           Interconnection Network           |
    +---------------------------------------------+
```

**Communication**:
- Send/Receive primitives (e.g., MPI_Send, MPI_Recv).
- No shared address space. Data is explicitly copied between nodes.

**Advantages**:
- Highly scalable (thousands of nodes).
- No cache coherence overhead.
- Simple hardware (no snooping/directory logic).

**Disadvantages**:
- Programming complexity: Programmer must manage data distribution and communication.
- Communication latency: Message passing has higher overhead than shared memory loads/stores.

**Example**: Massively Parallel Processors (MPPs), clusters (Beowulf), supercomputers.

## Multicore Processors

Multiple processor cores on a single chip (die). Each core can be a full-fledged CPU with private L1/L2 caches, sharing L3 cache and memory controller.

```
+--------------------------------------------------+
|                 Multicore Chip                     |
|                                                    |
|  +---------+  +---------+  +---------+  +---------+|
|  | Core 0  |  | Core 1  |  | Core 2  |  | Core 3  ||
|  | L1 I/D  |  | L1 I/D  |  | L1 I/D  |  | L1 I/D  ||
|  | L2      |  | L2      |  | L2      |  | L2      ||
|  +---------+  +---------+  +---------+  +---------+|
|                                                    |
|  +------------------------------------------------+|
|  |             Shared L3 Cache                     ||
|  +------------------------------------------------+|
|                                                    |
|  +------------------------------------------------+|
|  |          Memory Controller / I/O               ||
|  +------------------------------------------------+|
+--------------------------------------------------+
```

**Benefits**:
- Higher throughput without increasing clock frequency.
- Better power efficiency (lower frequency per core, more cores).
- Thread-level parallelism (TLP): Different cores run different threads.

**Examples**: Intel Core i7 (8-16 cores), AMD Ryzen, ARM big.LITTLE.

## Amdahl's Law

**Amdahl's Law** states that the maximum speedup of a parallel computation is limited by the fraction of the program that must be executed sequentially.

### Formula

```
Speedup = 1 / ((1 - P) + P / N)
```

Where:
- P = fraction of the program that can be parallelized (0 <= P <= 1)
- (1 - P) = fraction that must be executed sequentially
- N = number of processors

### Derivation

Let total execution time on 1 processor = 1 unit.

- Sequential portion: (1 - P) time units.
- Parallel portion: P time units. On N processors, it takes P/N time units.

Total time on N processors:
```
T(N) = (1 - P) + P/N
```

Speedup:
```
S(N) = T(1) / T(N) = 1 / ((1 - P) + P/N)
```

### Key Insights

1. Even with infinite processors (N -> infinity), speedup is bounded:
```
S_max = 1 / (1 - P)
```

2. A small sequential fraction severely limits speedup.

### Worked Example

**Example 1**: A program is 90% parallelizable (P = 0.9). Compute speedup for N = 2, 4, 8, 16, and infinity.

```
P = 0.9

N=2:    S = 1 / ((1-0.9) + 0.9/2) = 1 / (0.1 + 0.45) = 1 / 0.55 = 1.82
N=4:    S = 1 / (0.1 + 0.9/4) = 1 / (0.1 + 0.225) = 1 / 0.325 = 3.08
N=8:    S = 1 / (0.1 + 0.9/8) = 1 / (0.1 + 0.1125) = 1 / 0.2125 = 4.70
N=16:   S = 1 / (0.1 + 0.9/16) = 1 / (0.1 + 0.05625) = 1 / 0.15625 = 6.40
N=inf:  S = 1 / 0.1 = 10
```

**Interpretation**: Even with 90% parallelism and 16 processors, speedup is only 6.4x -- far from the ideal 16x. The 10% sequential code dominates as N increases.

**Example 2**: What fraction of a program must be parallelizable to achieve a speedup of 100 on 200 processors?

```
S = 1 / ((1 - P) + P/N)
100 = 1 / ((1 - P) + P/200)
(1 - P) + P/200 = 0.01
1 - P + 0.005P = 0.01
1 - 0.995P = 0.01
0.995P = 0.99
P = 0.995 = 99.5%
```

You need 99.5% of the program to be parallelizable to get 100x speedup on 200 processors.

### Amdahl's Law Graph

```
Speedup
  10 |                     *
   9 |                   *
   8 |                 *
   7 |               *
   6 |             *
   5 |           *
   4 |        *
   3 |     *
   2 |  *
   1 *
     +--+--+--+--+--+--+--+--+--+--+
     1  2  4  8  16 32 64 128 256   
                   Processors (N)
     
     * = P = 0.9 (90% parallel)
     + = P = 0.5 (50% parallel)
```

### Amdahl's Law and Multicore

In multicore design, Amdahl's Law guides the number of cores:
- For workloads with high parallelism (P close to 1), many cores are beneficial.
- For workloads with significant serial portions, increasing cores gives diminishing returns.
- This is why some processors combine a few fast cores with many efficient cores (heterogeneous architecture).

---

## Practice Problems

**Problem 1**: A program takes 100 seconds on a single processor. The parallelizable portion takes 80 seconds. What is the speedup on 5 processors?

**Answer**:
- P = 80/100 = 0.8, 1-P = 0.2
- S = 1 / (0.2 + 0.8/5) = 1 / (0.2 + 0.16) = 1 / 0.36 = 2.78

**Problem 2**: What is the maximum possible speedup for a program that is 95% parallelizable?

**Answer**:
- S_max = 1 / (1 - 0.95) = 1 / 0.05 = 20

**Problem 3**: If 5% of a program is inherently sequential, what is the minimum number of processors needed to achieve a speedup of at least 10?

**Answer**:
- 1-P = 0.05, P = 0.95
- 10 = 1 / (0.05 + 0.95/N)
- 0.05 + 0.95/N = 0.1
- 0.95/N = 0.05
- N = 0.95 / 0.05 = 19 processors

**Problem 4**: Classify these architectures using Flynn's taxonomy: (a) A vector supercomputer, (b) A dual-core laptop, (c) An FPGA configured to run 3 different algorithms on 1 data stream.

**Answer**:
- (a) SIMD: Single instruction operates on vector elements.
- (b) MIMD: Each core runs its own instruction stream on its own data.
- (c) MISD: Multiple instructions on single data stream.

**Problem 5**: Compare shared memory (UMA) and message passing for a system with 64 processors.

**Answer**: UMA with 64 processors is impractical due to bus/network contention. NUMA (ccNUMA) or message passing is preferred. NUMA offers shared address space (easier programming) but requires cache coherence hardware. Message passing scales better but requires explicit data management.
