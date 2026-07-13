# Concurrent access to memory

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 8  
**Date:** 30-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Organization: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Directory-Based Cache Coherence

Snooping protocols rely on a shared bus for all communication. As the number of processors increases beyond 8-16, the bus becomes a bottleneck. **Directory-based protocols** solve this scalability problem by maintaining a directory of which caches hold which blocks.

### Why Directory-Based?

- **Snooping limitation**: Every cache sees every bus transaction. O(N) bus traffic per transaction. Bus bandwidth shared among N processors.
- **Directory solution**: Only send messages to caches that actually hold the block. Uses a point-to-point network instead of a shared bus.
- **Scalable**: Can support 64-1024+ processors in a NUMA system.

## Directory Structure

The **directory** is a data structure that tracks the state of each memory block. It can be stored alongside main memory.

### Directory Entry for One Block

For a system with N processors, each directory entry contains:

```
+----------+----------+-----------------------------+
| Dirty Bit| Presence | Presence Vector (N bits)    |
| (1 bit)  | Bits     |                             |
+----------+----------+-----------------------------+
```

- **Dirty bit (1 bit)**: Indicates whether the block is modified in some cache (1 = modified, 0 = clean).
- **Presence vector (N bits)**: Each bit corresponds to a processor (or cache). Bit i = 1 means processor i has a copy of this block in its cache.
  - If Dirty = 0: Processors in presence vector share a clean copy. Memory copy is valid.
  - If Dirty = 1: Exactly one processor in presence vector has the Modified copy. Memory is stale.

### Directory Organization

```
Main Memory:
+----------+  Directory:
| Block 0  |  | Dir entry 0 |  <-- tracks block 0
+----------+  +------------+
| Block 1  |  | Dir entry 1 |  <-- tracks block 1
+----------+  +------------+
| Block 2  |  | Dir entry 2 |  <-- tracks block 2
+----------+  +------------+
  ...            ...
+----------+  +------------+
| Block M-1|  | Dir entry M-1|
+----------+  +------------+
```

The directory can be stored with memory (in-memory directory) or in a separate SRAM (for faster access).

## Directory-Based Protocol Operations

A basic directory protocol handles the following messages between caches and directories:

### Message Types

| Message | From | To | Meaning |
|---|---|---|---|
| ReadReq | Local cache | Home directory | Request read access to block |
| WriteReq | Local cache | Home directory | Request write (exclusive) access |
| ReadReply | Home directory / Remote cache | Local cache | Supplies requested block data |
| WriteReply | Home directory / Remote cache | Local cache | Supplies block for write |
| Invalidate | Directory | Remote cache | Invalidate your copy |
| Update | Directory | Remote cache | Update your copy with new data |
| Fetch | Directory | Remote cache | Send block back to home directory |

### Example Scenario

Consider a system with 4 processors (P0-P3), each with private caches. The directory is at the home memory node. Block X initially in memory (no cached copies).

**Case 1: P0 reads X (first access)**

```
P0 -> Directory: ReadReq(X)
  Directory looks up X: presence vector = 0000, dirty = 0.
  Directory: ReadReply(X) sent to P0.
  Directory updates: presence vector bit 0 = 1, dirty = 0.
  P0 cache: X in Exclusive (or Shared, depending on protocol variant).
```

**Case 2: P1 reads X (already shared)**

```
P1 -> Directory: ReadReq(X)
  Directory: presence vector = 1000 (P0 has it).
  Directory: ReadReply(X) sent to P1 (data from memory, which is clean).
  Directory updates: presence vector bit 1 = 1 (now 1100), dirty = 0.
  P1 cache: X in Shared.
  Optionally: Directory notifies P0 that P1 has a copy (P0 stays Shared).
```

**Case 3: P2 writes X (exclusive access)**

```
P2 -> Directory: WriteReq(X)
  Directory: presence vector = 1100 (P0 and P1 have copies).
  Dirty = 0, memory is clean.
  Directory sends: Invalidate(X) to P0 and P1.
  P0 receives Invalidate: invalidates its copy, sends Ack.
  P1 receives Invalidate: invalidates its copy, sends Ack.
  Directory waits for all acks, then:
    Directory: WriteReply(X) sent to P2 (data from memory).
    Directory updates: presence vector = 0100 (P2 only), dirty = 1.
  P2 receives reply, writes X, cache state = Modified.
```

**Case 4: P0 reads X (after P2 wrote it)**

```
P0 -> Directory: ReadReq(X)
  Directory: presence vector = 0100, dirty = 1 (P2 has Modified copy).
  Directory sends: Fetch(X) to P2.
  P2 receives Fetch: Flushes X to directory (write-back).
  P2: Transitions to Shared (or Invalid, depending on protocol).
  Directory receives data: Updates memory with X.
    Dirty = 0, presence vector bit 2 stays 1, bit 0 added (now 0101).
  Directory sends: ReadReply(X) to P0.
  P0 cache: X in Shared.
```

### Directory Operations Summary

```
P(i) -> Dir: ReadReq(X)
  if (Dir.Dirty == 0):
    Dir.Data = Memory[X]
    Dir.Presence.set(i)
    Dir -> P(i): ReadReply(Data)
  else: // Dirty == 1
    j = index of dirty owner from Presence
    Dir -> P(j): Fetch(X)
    P(j) -> Dir: Data (flush)
    Memory[X] = Data
    Dir.Dirty = 0
    Dir.Presence.set(i)
    Dir.Presence.clear(j)
    Dir.Presence.set(i)  // now includes both i and possibly j
    Dir -> P(i): ReadReply(Data)

P(i) -> Dir: WriteReq(X)
  if (Dir.Dirty == 1):
    j = owner
    Dir -> P(j): Fetch+Invalidate(X)
    P(j) -> Dir: Data (flush)
    Memory[X] = Data
    Dir.Presence.clear(j)
  // Now Dir.Dirty = 0, handle sharers
  for each k in Dir.Presence where k != i:
    Dir -> P(k): Invalidate(X)
    P(k) -> Dir: Ack
  Dir.Presence.clear all except i
  Dir.Data = Memory[X] (or fetched data)
  Dir -> P(i): WriteReply(Data)
  Dir.Dirty = 1
  P(i) now has Modified copy
```

## Comparison: Snooping vs Directory-Based

| Feature | Snooping | Directory-Based |
|---|---|---|
| Interconnect | Shared bus (broadcast) | Point-to-point network (unicast/multicast) |
| Scalability | Low (8-16 processors) | High (64-1024+ processors) |
| Latency | Low (bus is fast, short distance) | Higher (network hops, directory lookup) |
| Bandwidth | Shared bus (bottleneck) | Distributed (point-to-point links) |
| Hardware cost | Low (bus + snoop logic) | Higher (directory memory, network) |
| Protocol complexity | Lower (all caches see all) | Higher (directory management) |
| Cache-to-cache transfer | Fast (snoop response) | Slower (via directory) |
| Typical use | Small SMP systems | Large ccNUMA systems |

## Scalability Considerations

### Snooping Scalability

Each bus transaction is seen by ALL caches. As N increases:
- Bus bandwidth: Each cache generates traffic. Total bus traffic ~ O(N^2) for some patterns.
- Snoop bandwidth: Each cache must examine EVERY transaction. Snoop logic must keep up.
- Wire delay: Long buses have high latency at high clock frequencies.

**Practical limit**: ~8-16 processors on a single snooping bus.

Hierarchical snooping (e.g., Intel's QuickPath Interconnect, AMD's HyperTransport) extends this by using point-to-point links between processor groups, with each group having its own snooping domain.

### Directory Scalability

Directory size grows with N (processors) and M (memory blocks):
- Directory entry size = 1 (dirty) + N (presence bits) bits = O(N) per block.
- Total directory size = M x (1 + N) bits = O(M x N).

For a large system (N = 1024 processors, M = 4 GB in 64-byte blocks):
- Number of blocks = 4 GB / 64 B = 67,108,864 blocks.
- Presence vector = 1024 bits = 128 bytes per block.
- Total directory = 67M x 128 bytes = 8.5 GB! This is too large.

**Solutions**:
- **Sparse directory**: Only track blocks that are actually cached (most blocks are not cached by anyone at a given time). Use a directory cache instead of a full directory.
- **Limited pointer directory**: Instead of N presence bits, store k pointers to caches that have the block. If more than k sharers, broadcast (saturate the block).
- **Coarse vector**: Use one bit per group of processors (e.g., per node in a cluster).

## False Sharing

**False sharing** occurs when two or more processors access different data that happens to reside in the same cache block, and at least one processor writes to its data. The cache coherence protocol treats this as a true sharing conflict, causing unnecessary invalidations and data transfers.

### False Sharing Example

```
Cache block X (64 bytes):
  Bytes 0-3:   data_A   (used by P0)
  Bytes 4-7:   data_B   (used by P1)

P0 repeatedly writes data_A.
P1 repeatedly writes data_B.
```

Although P0 and P1 access DIFFERENT variables (data_A and data_B), they share the same cache block. Each write by P0 invalidates P1's copy, and vice versa.

```
P0 writes data_A:
  - P0's cache block goes to M.
  - P1's copy invalidated.
  - Next, P1 writes data_B, misses (because invalidated).
  - P1 broadcasts BusRdX, fetches the block.
  - P0's copy invalidated.
  - Next, P0 writes data_A again, misses...
  - This ping-pong continues each time either writes.
```

**Impact**: Massive performance degradation. The cache block constantly bounces between caches. This is called the **ping-pong effect**.

### Solutions to False Sharing

1. **Compiler optimization**: Align data structures so that frequently written variables are in separate cache blocks (pad data structures to cache line boundaries).

2. **Data structure restructuring**: Use per-processor data structures (e.g., array of structs -> struct of arrays).

3. **Manual padding**: Insert unused bytes between frequently modified fields.

```
// Before (false sharing prone):
struct {
    int counter;  // written by P0
    int flag;     // written by P1
};

// After (padded to avoid false sharing):
struct {
    int counter;          // written by P0
    char pad[60];         // fill remaining cache line
    int flag;             // written by P1 (different cache line)
    char pad2[60];        // fill remaining cache line
};
```

4. **Page-level or block-level coloring**: Ensure non-shared data maps to different cache sets (OS/hardware technique).

---

## Practice Problems

**Problem 1**: For a system with 64 processors and a directory with 16K blocks, what is the minimum directory size using (a) full bit vector, (b) limited pointer with 4 pointers?

**Answer**:
- (a) Full bit vector: 1 dirty + 64 presence = 65 bits per block. Total = 16K x 65 bits = 16,384 x 65 = 1,064,960 bits = 130 KB.
- (b) Limited pointer (4 pointers): 1 dirty + 4 x 6 bits (log2(64)=6) = 1 + 24 = 25 bits per block. Total = 16K x 25 = 409,600 bits = 50 KB.

**Problem 2**: In a directory protocol, P0 has block Y in Modified state. P1 issues a ReadReq for Y. List all messages exchanged and state changes.

**Answer**:
1. P1 -> Directory: ReadReq(Y)
2. Directory (dirty=1, owner=P0) -> P0: Fetch(Y)
3. P0 flushes Y, state to Invalid (or Shared), P0 -> Directory: Data(Y)
4. Directory updates memory, dirty=0, presence = P0(optional)+P1
5. Directory -> P1: ReadReply(Y)
6. P1 state: Shared

Total: 5 messages (ReadReq, Fetch, Data, ReadReply) -- plus possible ack.

**Problem 3**: Distinguish between true sharing and false sharing.

**Answer**: True sharing: multiple processors access the SAME variable and the coherence protocol correctly synchronizes them. False sharing: processors access DIFFERENT variables within the same cache block. The coherence protocol treats it as if they were sharing, causing unnecessary invalidations and thrashing.

**Problem 4**: Why does snooping not scale well beyond 16 processors?

**Answer**: (1) The shared bus has finite bandwidth; each transaction is broadcast to all, limiting throughput. (2) Each cache must snoop every transaction, consuming power and potentially creating snoop filter bottlenecks. (3) Bus arbitration becomes complex with many requesters. (4) Electrical limitations of bus length and capacitance at high frequencies.

**Problem 5**: A system has 8 processors and uses a directory protocol. A block starts uncached. Trace all messages for: P0 reads, P1 reads, P2 writes, P3 reads.

**Answer**: 
- P0 ReadReq: Dir -> P0 ReadReply (dir: presence[0]=1)
- P1 ReadReq: Dir -> P1 ReadReply (dir: presence[0,1]=2)
- P2 WriteReq: Dir -> P0 Invalidate, Dir -> P1 Invalidate, P0 Ack, P1 Ack, Dir -> P2 WriteReply (dir: dirty=1, presence[2]=1)
- P3 ReadReq: Dir -> P2 Fetch, P2 -> Dir Data, Dir -> P3 ReadReply (dir: dirty=0, presence[2,3]=2)
Total messages: 10 (4 requests + 2 replies + 2 invalidations + 2 acks = 10)
