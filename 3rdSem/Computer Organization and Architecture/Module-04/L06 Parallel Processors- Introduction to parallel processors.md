# Parallel Processors: Introduction to parallel processors

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 6  
**Date:** 29-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Advanced Parallel Architectures

This lecture continues the discussion on parallel processors, focusing on vector processors, GPU architecture, hardware multi-threading techniques, and a comparison of modern parallel systems.

## Vector Processors

A **vector processor** is a specialized CPU that operates on arrays (vectors) of data with a single instruction. It exploits data-level parallelism (DLP).

### How Vector Processors Work

A single vector instruction performs an operation on multiple data elements in parallel.

**Scalar approach** (add two arrays of length 64):
```
for i = 0 to 63:
    C[i] = A[i] + B[i]
```
This requires:
- 64 load instructions (A[i])
- 64 load instructions (B[i])
- 64 add instructions
- 64 store instructions (C[i])
- 64 loop control instructions
= 256+ instructions, plus loop overhead.

**Vector approach**:
```
VADD C, A, B
```
1 instruction! The vector processor has vector registers (each holding multiple elements) and vector functional units that pipeline the operations.

### Vector Processor Architecture

```
+------------------+
|  Vector Control  |
+------------------+
         |
+--------+--------+
| Scalar Unit     | (handles scalars, addresses)
+-----------------+
         |
+--------+--------+
| Vector Registers |  (e.g., 32 x 64-bit elements x 32 registers)
+------------------+
         |
+--------+---------+
| Vector ALU       |  (pipelined, one result per cycle)
+------------------+
         |
+--------+---------+
| Vector Load/Store|  (gather/scatter for non-contiguous memory)
+------------------+
```

### Vector Processor Characteristics

- **Vector registers**: Wide registers holding multiple data elements (e.g., 64 x 64-bit).
- **Vector functional units**: Deeply pipelined to produce one result per cycle.
- **Vector length register**: Controls how many elements to process.
- **Memory stride**: Ability to access non-contiguous memory patterns.
- **Chaining**: Results of one vector operation feed directly into the next, similar to forwarding.

### Examples

- Cray-1 (1976): First successful vector supercomputer.
- NEC SX series: Vector supercomputers.
- Modern CPUs with SIMD extensions (AVX-512): 512-bit vectors = 8 double-precision or 16 single-precision operations per instruction.

## GPU Architecture (Brief Overview)

**GPUs (Graphics Processing Units)** are massively parallel processors designed for graphics (and general-purpose computation, GPGPU).

### Key Concepts

- **Massive SIMD**: GPUs use SIMD-like execution (called SIMT -- Single Instruction, Multiple Threads).
- **Thousands of cores**: A modern GPU has 1000s of simple cores grouped into streaming multiprocessors (SMs -- Nvidia) or compute units (CUs -- AMD).
- **Warp/Wavefront**: A group of threads (32 for Nvidia, 64 for AMD) executing the same instruction on different data.
- **High memory bandwidth**: GPUs use wide memory buses (e.g., 384-bit) and high-bandwidth memory (HBM, GDDR6).

### Simplified GPU Architecture

```
+----------------------------------------------------+
|                    GPU Chip                          |
|                                                      |
| +------------------+     +------------------+       |
| |   SM 0           |     |   SM 1           |       |
| | +--+ +--+ ... +--+|     | +--+ +--+ ... +--+|      |
| | |CU| |CU|     |CU||     | |CU| |CU|     |CU||      |
| | +--+ +--+     +--+|     | +--+ +--+     +--+|      |
| | Shared Memory     |     | Shared Memory     |      |
| +------------------+     +------------------+       |
|                                                      |
| +------------------+     +------------------+       |
| |   SM 2           |     |   SM 3           |       |
| | ...              |     | ...              |       |
| +------------------+     +------------------+       |
|                                                      |
| +--------------------------------------------------+|
| |            L2 Cache / Memory Controller          ||
| +--------------------------------------------------+|
+----------------------------------------------------+
```

**CU** = CUDA Core (Nvidia), a simple FP/INT unit.
**SM** = Streaming Multiprocessor, contains 64-128 CUDA cores, shared memory, warp scheduler.

### GPU vs CPU Comparison

| Aspect | CPU | GPU |
|---|---|---|
| Core count | 4-16 (large cores) | 1000-10000 (small cores) |
| Control logic | Complex (OoO, branch pred.) | Simple (SIMT, hides latency) |
| Cache | Large L1/L2/L3 | Smaller L1, moderate L2 |
| Memory | DDR4/DDR5 (low latency) | GDDR6/HBM (high bandwidth) |
| Threads | 2-64 threads | 10000+ threads |
| Best for | Sequential, latency-sensitive | Parallel, throughput-oriented |

## Hardware Multi-Threading

**Multi-threading** allows multiple threads to share the execution resources of a single processor core. It keeps the pipeline busy when one thread stalls (cache miss, branch misprediction).

### Fine-Grained Multi-Threading

- Switch between threads on every cycle (interleaved).
- Each thread gets a dedicated set of registers (register renaming).
- Pipeline never has a bubble -- if one thread stalls, another runs.

```
Cycles:    1   2   3   4   5   6   7   8   9
Thread 0: [IF][ID][EX][MEM][WB]
Thread 1:      [IF][ID][EX][MEM][WB]
Thread 2:           [IF][ID][EX][MEM][WB]
Thread 3:                [IF][ID][EX][MEM][WB]
```

Each cycle picks a different thread's instruction. No thread dependency stalls propagate.

**Example**: Sun Microsystems Niagara (UltraSPARC T1) -- 8 cores, 4 threads each, fine-grained multi-threading.

### Coarse-Grained Multi-Threading

- Switch threads only when the current thread suffers a long-latency event (e.g., L2 cache miss).
- Less overhead than fine-grained (fewer context switches).
- Throughput is improved, but bubbles may still appear during short stalls.

```
Thread 0: ---- active ---- waits for cache miss ----
Thread 1:                     ---- active ----------
Thread 2:                                            ---- active ---
```

### Simultaneous Multi-Threading (SMT / Hyper-Threading)

- Multiple threads issue instructions to the superscalar pipeline in the SAME cycle.
- The processor has multiple independent architectural states (PC, registers) but shares execution units.
- Better utilization of wide superscalar pipelines (e.g., if one thread has no floating-point work, another thread's FP instruction can use the FP unit).

```
     Cycle 1            Cycle 2            Cycle 3
T0: ADD R1,R2,R3    T0: LOAD R4,0(R1)   T0: STALL (cache)
T1: SUB R5,R6,R7    T1: BEQ R8,R9,label T1: MUL R10,R11,R12
     |                    |                    |
     v                    v                    v
[IF: T0,T1] [ID: T0,T1] [EX: T0 ADD, T1 SUB] [MEM: T0 LOAD] [WB]
```

In cycle 1, both T0 and T1 fetch instructions. In cycle 3, the EX stage processes T0's ADD and T1's SUB simultaneously.

**Example**: Intel Hyper-Threading Technology (since Pentium 4). Modern Intel/AMD processors support 2 threads per core (some Intel E-core or Xeon support 2 threads, some server processors support 4).

### Multi-Threading Comparison

| Feature | Fine-Grained | Coarse-Grained | SMT |
|---|---|---|---|
| Switch granularity | Every cycle | Only on long stalls | Same cycle (parallel issue) |
| Threads sharing units | No (one thread per cycle) | No (one thread per cycle) | Yes (multiple in same cycle) |
| Hardware cost | High (many register sets) | Moderate | High (register renaming, issue logic) |
| Best for | Hiding all latency | Hiding long latency | Superscalar utilization |

## Examples: Modern Implementations

### Intel Core i7 (Alder Lake / Raptor Lake)

- **Type**: Multicore, MIMD, SMT
- **Cores**: 8 Performance-cores (P-cores, Hyper-Threading) + 8 Efficiency-cores (E-cores, no HT) = 16 cores, 24 threads
- **SIMD**: AVX-512 (some generations), AVX2, SSE4.2
- **Cache**: Private L1 (32KB I + 48KB D per P-core), Private L2 (1.25MB per P-core), Shared L3 (up to 30MB)
- **Memory**: Dual-channel DDR5
- **Parallelism types**: ILP (superscalar, OoO), TLP (SMT, multicore), DLP (SIMD)

### Nvidia GPU (Ada Lovelace / Hopper)

- **Type**: SIMT (SIMD-like), massively parallel
- **CUDA Cores**: 16384+ (in large GPUs)
- **Tensor Cores**: Specialized matrix multiply units (AI/ML)
- **Memory**: GDDR6X / HBM3 (high bandwidth)
- **Warp size**: 32 threads
- **Parallelism type**: DLP dominated
- **Use case**: Graphics, deep learning, scientific computing

## Comparison Table: Parallel Architectures

| Architecture | Parallelism Type | Granularity | Example Hardware | Best Workload |
|---|---|---|---|---|
| Superscalar (ILP) | Instruction-level | Fine | Modern CPU cores | General-purpose |
| SMT / Hyper-Threading | Thread-level | Medium | Intel Core i7, AMD Ryzen | Mixed, server |
| Multicore | Thread-level | Coarse | All modern CPUs | Multi-threaded apps |
| Vector Processor | Data-level | Fine (vector elements) | Cray, NEC SX | Scientific computing |
| SIMD Extensions | Data-level | Fine (vector lanes) | AVX-512, NEON, SVE | Multimedia, ML |
| GPU (SIMT) | Data-level + Thread-level | Fine (threads/warps) | Nvidia, AMD, Intel | Graphics, ML, HPC |
| MPP (Massively Parallel) | Process-level | Coarse (processes) | Clusters, supercomputers | Large-scale simulations |

---

## Practice Problems

**Problem 1**: How many vector instructions are needed to perform A = B * C + D (element-wise) for vectors of length 128 on a vector processor?

**Answer**: 3 vector instructions:
1. VMUL T, B, C (multiply B and C, store in temporary T)
2. VADD A, T, D (add T and D)
3. No loop overhead. With chaining, both operations can be overlapped.

**Problem 2**: A GPU has 80 SMs, each with 64 CUDA cores. Each SM can run 64 warps (32 threads each). What is the maximum number of threads the GPU can have in flight?

**Answer**:
- Threads per SM = 64 warps x 32 threads = 2048 threads
- Total threads = 80 x 2048 = 163,840 threads

**Problem 3**: Compare fine-grained multi-threading and SMT in terms of utilization of a 6-issue superscalar processor.

**Answer**: Fine-grained MT issues at most one thread's instruction per cycle, so only one thread can utilize the 6-wide pipeline. SMT allows multiple threads to issue instructions in the same cycle, potentially using all 6 issue slots (e.g., 2 from thread A, 4 from thread B). SMT achieves higher throughput on wide superscalars.

**Problem 4**: A vector processor has vector registers of length 256. A program processes an array of 1024 elements. How many iterations of a scalar loop are replaced by one vector loop?

**Answer**: With vector length 256, 1024/256 = 4 vector iterations replace 1024 scalar iterations. The vector loop also has reduced control overhead (4 loop iterations vs 1024).

**Problem 5**: Explain why GPUs use many simple cores rather than a few complex cores.

**Answer**: GPU workloads (graphics, matrix operations) exhibit massive data-level parallelism. Simple cores occupy less area, allowing thousands on a chip. Complexity (OoO, branch prediction) is not needed because threads are interleaved to hide latency. Area efficiency is paramount for throughput computing.
