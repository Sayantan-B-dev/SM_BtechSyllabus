# Cache coherency

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 9  
**Date:** 30-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Cache Coherence vs Memory Consistency

Cache coherence and memory consistency are related but distinct concepts.

### Cache Coherence

**Cache coherence** ensures that all processors see a consistent view of memory with respect to accesses to a **single memory location**. It guarantees:
- Write propagation: A write by one processor eventually becomes visible to others.
- Write serialization: Writes to the same location are seen in the same order by all processors.

Coherence is about **what value is returned by a read** to a specific address.

### Memory Consistency

**Memory consistency** (also called **memory consistency model**) defines the order in which memory operations (reads and writes) from different processors can appear to be performed. It governs the **relative ordering** of accesses to **different memory locations**.

Consistency is about **when a write becomes visible to other processors** relative to other operations.

### Key Distinction

```
Coherence: "If P0 writes X=1, will P1's read of X return 1?"
Consistency: "If P0 writes X=1 then writes Y=1, can P1 see Y=1 before seeing X=1?"
```

A system can be coherent but have unexpected behaviors due to weak consistency.

## Sequential Consistency Model

**Sequential consistency (SC)** is the strongest and most intuitive memory consistency model, defined by Lamport (1979):

> A multiprocessor is sequentially consistent if the result of any execution is the same as if the operations of all processors were executed in some sequential order, and the operations of each individual processor appear in this sequence in the order specified by its program.

### Requirements for SC

1. All memory operations (reads and writes) from all processors appear in a single total order.
2. The operations from any individual processor appear in the order specified by that processor's program.

### SC Example

Initially: X = 0, Y = 0, Flag = 0.

```
P0:              P1:
X = 1            while (Flag == 0);
Y = 1            A = X;
Flag = 1         B = Y;
```

Under SC, the following partial orders must hold:
- P0: X=1 before Y=1, Y=1 before Flag=1.
- P1: read Flag before read X, read X before read Y.

Therefore, if P1 sees Flag=1, it must see X=1 and Y=1. The result (A=1, B=1) is guaranteed.

### SC Violation Example

With a weaker model, the hardware might reorder P0's stores:

```
P0's stores (as seen by hardware):
  Flag = 1    (reordered ahead of X=1 and Y=1)
  X = 1
  Y = 1

P1 sees Flag=1, but reads X=0 and Y=0 (stale values).
```

This violates SC because P0's program order (X=1, Y=1, Flag=1) is not preserved.

### Why Not Always Use SC?

Sequential consistency restricts hardware optimization. To maintain SC, the hardware must:
- Not reorder memory operations within a processor.
- Ensure all writes are globally visible in program order.
- Stall on every memory access until previous accesses complete.

These restrictions reduce performance. **Relaxed consistency models** allow more hardware optimization at the cost of weaker guarantees to the programmer.

## Relaxed Consistency Models

Relaxed models remove some of the ordering constraints of SC, allowing hardware to reorder memory operations for better performance.

### Processor Consistency (PC)

**Processor consistency** (also called **TSO** -- Total Store Order, used by SPARC and x86-TSO) relaxes the order between writes from different processors but maintains program order for writes from the same processor.

**Rules**:
- Writes from the same processor appear in program order.
- A read can bypass an earlier write (read can be performed before a buffered write).
- Writes from different processors can be seen in different orders.

**Effect**:
- A processor can read its own write before it becomes globally visible (store buffer forwarding).
- Different processors may see writes in different orders.

**Example** (PC allows this):

Initially: X = 0, Y = 0.

```
P0:              P1:
X = 1            Y = 1
R1 = Y           R2 = X
```

Under PC, possible outcome: R1 = 0 and R2 = 0.
- P0's write to X and P1's write to Y are held in store buffers.
- Both reads see stale values (0).
- Under SC, this outcome is forbidden.

### Weak Consistency (WC)

**Weak consistency** makes a distinction between **synchronization operations** and **data operations**. Programmers use explicit synchronization to order memory accesses.

**Rules**:
- Synchronization operations are sequentially consistent (total order).
- Data operations (regular reads/writes) between two synchronization operations can be reordered arbitrarily.
- Before a synchronization operation is performed, all previous data operations must be completed.

```
[Data ops] ... [Data ops] [Sync] [Data ops] ... [Data ops] [Sync]
   ^--- can reorder ---^        ^--- can reorder ---^
   All data ops must complete before sync can proceed.
```

**Implication**: Between synchronization points, the hardware can freely reorder memory accesses for performance.

### Release Consistency (RC)

**Release consistency** refines weak consistency further by distinguishing between **acquire** and **release** synchronization operations.

**Rules**:
- **Acquire** (e.g., lock): All operations following the acquire must wait until the acquire completes.
- **Release** (e.g., unlock): All operations before the release must complete before the release is performed.
- Regular memory operations can be reordered freely as long as they do not cross a release (backward) or an acquire (forward).

```
[Data ops] [RELEASE] | [ACQUIRE] [Data ops]
   must complete       |    must wait until
   before release      |    acquire completes
```

**Release consistency** provides:
- **Acquire semantics**: Data operations after an acquire see all operations before the corresponding release.
- **Release semantics**: Data operations before a release become visible to all other processors before the release.

**Examples**: C++11 memory model (acquire/release semantics), Java volatile.

## Memory Barrier / Fence Instructions

A **memory barrier** (also called **memory fence**) is an instruction that enforces an ordering constraint on memory operations. It prevents the compiler and the CPU from reordering memory accesses across the fence.

### Common Fence Types

| Fence Type | Before-After Ordering | Use Case |
|---|---|---|
| **Full fence** (dmb, mfence) | All memory ops before fence complete before any after | Full ordering |
| **Load fence** (lfence) | All loads before fence complete before loads after | Load-load, load-store ordering |
| **Store fence** (sfence) | All stores before fence complete before stores after | Store-store ordering (e.g., x86 SFENCE) |
| **Load-Acquire** | Load-acquire acts as an acquire (prevents later ops from moving before) | Lock acquisition |
| **Store-Release** | Store-release acts as a release (prevents earlier ops from moving after) | Lock release |

### Examples in x86 Assembly

```asm
; Full memory barrier (mfence)
mov [X], 1     ; write X
mfence          ; ensure X=1 is globally visible
mov [Y], 1     ; write Y (only after X=1 is visible)

; Store fence (sfence) - ensures store-store ordering
mov [X], 1
sfence
mov [Y], 1     ; Y=1 not visible before X=1

; Load fence (lfence) - ensures load-load ordering
mov eax, [flag] ; read flag
lfence
mov ebx, [X]    ; read X (only after flag is read)
```

### Code Example: Effect of Missing Fence

**Problematic code** (no fence, weak consistency):

```c
// Shared variables
int data[100];
int flag = 0;

// P0 (producer)
void producer() {
    data[0] = 42;      // A
    data[1] = 100;     // B
    flag = 1;          // C  -- data should be visible before flag
}

// P1 (consumer)
void consumer() {
    while (flag == 0); // D  -- wait for flag
    int x = data[0];   // E
    int y = data[1];   // F
}
```

**Problem**: On a weakly ordered system, the hardware may reorder C before A or B. P1 sees flag=1 but reads stale data[0]=0 and data[1]=0.

**Solution with fences**:

```c
// P0
void producer() {
    data[0] = 42;
    data[1] = 100;
    STORE_FENCE();     // ensure data writes complete before flag write
    flag = 1;
}

// P1
void consumer() {
    while (flag == 0);
    LOAD_FENCE();      // ensure flag read completes before data reads
    int x = data[0];
    int y = data[1];
}
```

Or use release/acquire semantics:

```c
// P0: release semantics (like unlock)
data[0] = 42;
data[1] = 100;
atomic_flag.store(1, memory_order_release);  // all previous ops before this

// P1: acquire semantics (like lock)
while (atomic_flag.load(memory_order_acquire) == 0);  // all subsequent ops after this
int x = data[0];
int y = data[1];
```

## Examples: Effect of Different Consistency Models

### Example 1: Dekker's Algorithm (Mutual Exclusion)

Initially: X = 0, Y = 0.

```
P0:              P1:
X = 1            Y = 1
R1 = Y           R2 = X
```

**Under SC**:
- Possible outcomes: (R1=0, R2=1), (R1=1, R2=0), (R1=1, R2=1).
- Impossible: (R1=0, R2=0), because either P0's X=1 or P1's Y=1 must be visible first.

**Under TSO (x86)**:
- (R1=0, R2=0) is possible because both writes are in store buffers and both reads bypass (read stale values).

**Fix**: Insert a full memory barrier between the write and read on each processor:

```
P0:              P1:
X = 1            Y = 1
MFENCE           MFENCE
R1 = Y           R2 = X
```

Now (R1=0, R2=0) is impossible.

### Example 2: Producer-Consumer

Initially: flag = 0, data = 0.

```
P0 (producer):   P1 (consumer):
data = 100       while (flag == 0);
flag = 1         result = data;
```

**Expected**: result = 100.

**Under SC**: Guaranteed (flag=1 implies data=100 before it).

**Under weak consistency (no fences)**:
- Possible outcome: result = 0 (flag=1 visible before data=100).
- Possible outcome: result = 100 (by chance).
- Behavior is non-deterministic.

**Under release consistency with acquire/release on flag**: Guaranteed (result=100).

## Performance Implications

### Cost of Strong Consistency

Sequential consistency requires:
- Writes to be globally visible before the next instruction.
- No store buffering, or stall on every store.
- Memory access latency directly impacts pipeline.

**Performance loss**: SC can reduce performance by 10-50% compared to relaxed models, depending on the workload and hardware design.

### Cost of Memory Barriers

- A memory barrier flushes the store buffer (if a full fence).
- It may stall the pipeline until all pending memory operations complete.
- On modern x86, MFENCE is a relatively expensive instruction (20-100 cycles).
- Lighter fences (LFENCE, SFENCE) have lower cost.

### Trade-off Summary

| Model | Hardware complexity | Performance | Programming effort |
|---|---|---|---|
| Sequential Consistency (SC) | Simple (no reorder) | Low (restricted) | Easy (intuitive) |
| Processor Consistency (TSO) | Moderate (store buffer) | Medium | Moderate |
| Weak Consistency | Complex | High | Hard (fences needed) |
| Release Consistency | Complex | Highest | Hard (acquire/release) |

### Modern Practice

- **x86/x64**: Uses TSO (Total Store Order) -- effectively processor consistency. Stronger than most RISC architectures. Most x86 programs do not need fences.
- **ARM/PowerPC**: Use weak consistency. Programmers must use proper memory ordering primitives (DMB, DSB on ARM; sync, lwsync on PowerPC).
- **GPU**: Very weak consistency (e.g., Nvidia PTX has .rel, .acq, .relaxed modifiers).
- **C++11/C11**: Provides atomic operations with memory_order_relaxed, memory_order_acquire, memory_order_release, memory_order_seq_cst. Programmer specifies the desired ordering.

---

## Practice Problems

**Problem 1**: Explain the difference between cache coherence and memory consistency in one sentence each.

**Answer**: Coherence ensures that writes to the same memory location are seen in a consistent order by all processors. Consistency defines the order in which writes to different memory locations become visible to other processors relative to program order.

**Problem 2**: Under SC, is the following outcome possible given the code below? Initially: X=0, Y=0.

```
P0: X=1; R1=Y;
P1: Y=1; R2=X;
```
Outcome: R1=0, R2=0.

**Answer**: No, because SC requires a total order. Either P0's X=1 is visible first (then R2 cannot be 0) or P1's Y=1 is visible first (then R1 cannot be 0). One of the two writes must be first in the total order.

**Problem 3**: On a weakly consistent system, what is the minimum fix for the following code to ensure correct producer-consumer communication?

```c
// P0
shared_data = 42;
ready = 1;

// P1
while (ready == 0);
x = shared_data;
```

**Answer**: Insert a release fence before ready=1 in P0 (or use store-release for ready) and an acquire fence after the while loop in P1 (or use load-acquire for ready). This ensures ready=1 is visible only after shared_data=42, and the read of shared_data occurs only after seeing ready=1.

**Problem 4**: In x86-TSO, why is (R1=0, R2=0) possible in Dekker's algorithm without fences?

**Answer**: Each processor's store buffer holds the writes (X=1 for P0, Y=1 for P1). The reads on each processor can bypass the store buffer and read stale values from memory. Both writes are still in the store buffers, and both reads go to memory (where X=0, Y=0). Result: (R1=0, R2=0).

**Problem 5**: A program uses C++ atomics with memory_order_relaxed. The programmer observes unexpected results on a weakly-ordered ARM CPU that do not appear on x86. Why?

**Answer**: memory_order_relaxed imposes no ordering constraints. The compiler and CPU can reorder these operations freely. On x86 (TSO), the hardware naturally preserves some ordering (e.g., store-store ordering is implicit). On ARM (weak consistency), the hardware reorders aggressively, exposing the relaxed semantics. The programmer must use stronger memory ordering to ensure correctness across architectures.
