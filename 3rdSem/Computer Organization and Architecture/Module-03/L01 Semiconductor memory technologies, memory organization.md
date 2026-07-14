# Semiconductor memory technologies, memory organization

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 1  
**Date:** 19-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Classification of Semiconductor Memory

Semiconductor memory is broadly classified into two categories:

- **RAM (Random Access Memory)** -- Read/Write memory, volatile.
- **ROM (Read Only Memory)** -- Read-only memory, non-volatile.

---

### 2. RAM: SRAM vs DRAM

#### SRAM (Static RAM)

- Uses a **latch** (flip-flop) circuit to store each bit.
- Typically built from 6 transistors per cell (4 for the latch, 2 for access control).
- Data remains valid as long as power is supplied.
- **No refresh** required.
- **Faster** than DRAM (access time ~1-10 ns).
- **Lower density** (fewer bits per chip area).
- **Higher power consumption** per bit (but no refresh power).
- Used for **cache memory** (L1, L2, L3).

**SRAM Cell Operation:**

```
         Vdd
          |
        +---+ 
        |   |
        +---+ 
          |
    Q ---+--- Q'
          |
        +---+
        |   |
        +---+
          |
         GND
```

The cross-coupled inverters form a bistable latch. Two access transistors (not shown above) connect the cell to bit lines when the word line is asserted.

#### DRAM (Dynamic RAM)

- Uses a **capacitor** and a single transistor to store each bit.
- Capacitor charge represents a 1 (charged) or 0 (discharged).
- Capacitor **leaks charge** over time -- requires **periodic refresh** (every ~64 ms).
- **Slower** than SRAM (access time ~10-50 ns).
- **Higher density** (4-8x more than SRAM).
- **Lower cost per bit**.
- Used for **main memory** (system RAM).

**DRAM Cell Operation:**

```
      Word Line
         |
         +
         |
    Bit Line ----+----
                 |
                 T
                 |
                ===  (capacitor)
                 |
                GND
```

- **Read:** Precharge bit line to Vdd/2. Assert word line. Charge sharing between capacitor and bit line causes a small voltage change. Sense amplifier detects the change.
- **Write:** Drive bit line to desired voltage. Assert word line. Capacitor charges/discharges to match.
- **Refresh:** Read the cell and immediately write back the same value. Performed by the memory controller.

#### Comparison: SRAM vs DRAM

| Feature            | SRAM                          | DRAM                        |
|--------------------|-------------------------------|-----------------------------|
| Storage element    | Flip-flop (latch)             | Capacitor + transistor      |
| Transistors per bit| 6                             | 1                           |
| Speed              | Fast (1-10 ns)                | Moderate (10-50 ns)         |
| Density            | Low                           | High                        |
| Power              | Higher static, no refresh     | Lower static, needs refresh |
| Volatility         | Volatile                      | Volatile                    |
| Refreshing         | Not required                  | Required (~64 ms)           |
| Cost per bit       | Higher                        | Lower                       |
| Primary use        | Cache memory                  | Main memory                 |

---

### 3. ROM: PROM, EPROM, EEPROM, Flash

#### Mask ROM (Read Only Memory)

- Data programmed during manufacturing using a mask.
- Cannot be modified after fabrication.
- Used for firmware in high-volume production.

#### PROM (Programmable ROM)

- Can be programmed once by the user.
- Each cell contains a fuse or anti-fuse.
- Programming blows the fuse (or creates a connection).
- Cannot be erased or reprogrammed.

#### EPROM (Erasable Programmable ROM)

- Can be programmed electrically by the user.
- Erased by exposing the chip to **ultraviolet (UV) light** through a quartz window.
- Erasure takes 10-30 minutes.
- Can be reprogrammed multiple times.
- Requires removal from the circuit for erasure.

#### EEPROM (Electrically Erasable Programmable ROM)

- Can be programmed and erased **electrically** while in the circuit.
- Erasure is byte-by-byte.
- Slower write speed than Flash.
- Finite number of write/erase cycles (~100,000).
- Used for configuration data, BIOS settings (CMOS).

#### Flash Memory

- A type of EEPROM but **erased in blocks** (not byte-by-byte).
- Faster than EEPROM for bulk erase/write.
- NAND Flash vs NOR Flash:
  - NAND: Higher density, used in SSDs, USB drives.
  - NOR: Random access, used for firmware (BIOS/UEFI).
- Used in SSDs, USB flash drives, SD cards, smartphones.

#### Comparison: ROM Types

| Type    | Programmable | Erasable    | Erase Method   | Byte Erase | Typical Use              |
|---------|-------------|-------------|----------------|------------|--------------------------|
| Mask ROM| Factory      | No          | N/A            | N/A        | High-volume firmware     |
| PROM    | User (once)  | No          | N/A            | No         | Low-volume firmware      |
| EPROM   | User         | Yes (UV)    | UV light       | No         | Development/prototyping  |
| EEPROM  | User         | Yes (elec)  | Electrical     | Yes        | Configuration data       |
| Flash   | User         | Yes (elec)  | Electrical     | Block only | SSDs, USBs, firmware     |

---

### 4. Memory Chip Organization

A memory chip is organized as a **2D array of cells**.

Basic components:
- **Address lines (A0-Ak-1):** Select a specific memory location. 2^k locations.
- **Data lines (D0-Dn-1):** Carry data to/from the chip.
- **Chip Select (CS):** Enables the chip for operation.
- **Read/Write (R/W):** Determines direction of data transfer.
- **Decoders:** Convert binary address into a unique word/bit line selection.

#### Memory Array Structure

```
          Address Bus (k bits)
                 |
              +--+--+
              |Address|
              |Register|
              +-----+
                 |
            +----+----+
            | Row      |
            | Decoder  |
            +----+----+
                 |
            =====+===== Word Lines
            |   |   |
          +-+-+ +-+-+ +-+-+
          |Mem| |Mem| |Mem|  ... Memory Cells in a row
          +-+-+ +-+-+ +-+-+
            |   |   |
          Column Decoder / Multiplexer
                 |
              +--+--+
              |Sense  |
              |Amps   |
              +------+
                 |
              Data Bus (n bits)
```

- **Rows** are selected by the row decoder using the high-order address bits.
- **Columns** are selected by the column decoder using the low-order address bits.
- Each row corresponds to a **word line** that activates all cells in that row.
- Each column corresponds to a **bit line** that carries data to/from the selected cell.

#### Example: 4x3 Memory Chip

- 4 locations (2 address lines) x 3 bits per location (3 data lines).
- Address lines: A1, A0. Data lines: D2, D1, D0.

| Address (A1 A0) | Data (D2 D1 D0) Selected |
|-----------------|--------------------------|
| 00              | Row 0, 3-bit word        |
| 01              | Row 1, 3-bit word        |
| 10              | Row 2, 3-bit word        |
| 11              | Row 3, 3-bit word        |

---

### 5. Building Larger Memories from Chips

#### Word Width Expansion

Increase the number of data lines (wider words). Example: Build a 4x8 memory using two 4x4 chips.

```
                Address Bus (2 lines)
                      |
        +-------------+-------------+
        |                           |
     +--+--+                     +--+--+
     | 4x4  |                     | 4x4  |
     | Chip |                     | Chip |
     |  0   |                     |  1   |
     +--+---+                     +--+---+
        | D3-D0                      | D7-D4
        +-------------+-------------+
                      |
                   Data Bus (D7-D0)
```

- CS of both chips tied together.
- High 4 data bits come from chip 1, low 4 from chip 0.

#### Address Space Expansion

Increase number of addressable locations. Example: Build an 8x4 memory using two 4x4 chips.

```
                Address Bus (A2 A1 A0)
                      |
                 +---------+        
                 | Decoder |        
                 +----+----+        
                      |             
            +---------+---------+   
            | A2=0             | A2=1
         +--+--+            +--+--+
         | 4x4  |            | 4x4  |
         | Chip |            | Chip |
         |  0   |            |  1   |
         +-----+             +-----+
            |                    |
            +---------+----------+
                      |
                   Data Bus (D3-D0)
```

- Chip 0 selected when A2 = 0 (addresses 000-011).
- Chip 1 selected when A2 = 1 (addresses 100-111).
- Data lines are shared.

#### Combined Expansion

Build a 16x8 memory using 4 chips of 4x4: first expand word width to 8 bits (pairs of chips), then expand address space using a decoder.

---

### 6. Speed, Cost, and Volatility Comparison

| Memory Type | Speed (Access Time) | Volatility | Relative Cost per Bit | Density | Primary Use        |
|-------------|---------------------|------------|----------------------|---------|--------------------|
| SRAM        | 1-10 ns             | Volatile   | Highest              | Low     | Cache memory       |
| DRAM        | 10-50 ns            | Volatile   | Low                  | High    | Main memory        |
| Mask ROM    | 10-50 ns            | Non-volatile| Lowest (high volume)| High    | Mass-produced FW   |
| PROM        | 10-50 ns            | Non-volatile| Low                 | Medium  | Low-vol firmware   |
| EPROM       | 10-50 ns            | Non-volatile| Medium              | Medium  | Development        |
| EEPROM      | 10-200 ns           | Non-volatile| High                | Medium  | Config data        |
| Flash (NOR) | 50-100 ns (read)    | Non-volatile| Medium-low          | High    | Firmware, BIOS     |
| Flash (NAND)| 10-50 us (read)     | Non-volatile| Low                 | Very High| SSDs, USB drives   |

---

### 7. Memory Hierarchy Context

```
   Registers  (1 cycle, few bytes)
       |
    L1 Cache (SRAM, 1-3 ns, few KB)
       |
    L2 Cache (SRAM, 3-10 ns, few MB)
       |
    L3 Cache (SRAM, 10-30 ns, few MB)
       |
   Main Memory (DRAM, 10-50 ns, GB)
       |
         SSD/HDD (NAND Flash/Magnetic, ms, TB)
```

The hierarchy exploits:
- **Temporal locality:** Recently accessed data is likely to be accessed again.
- **Spatial locality:** Data near recently accessed data is likely to be accessed.

---

## Practice Problems

**Q1:** A memory chip has 12 address lines and 8 data lines. What is the storage capacity in bits? In bytes?

<details>
<summary>Show Answer</summary>
2^12 = 4096 locations. Each location is 8 bits. Total = 4096 x 8 = 32,768 bits = 4096 bytes (4 KB).
</details>

**Q2:** Why does DRAM require periodic refreshing while SRAM does not?

<details>
<summary>Show Answer</summary>
DRAM stores charge on a capacitor, which leaks over time (typically loses charge in ~64 ms). Without refreshing, the stored data would be lost. SRAM uses a flip-flop (cross-coupled inverters) that maintains its state as long as power is supplied, as long as the transistors remain in saturation or cutoff the data persists indefinitely without any refresh.
</details>

**Q3:** You need to design a 16K x 8 memory using 4K x 4 memory chips. How many chips are needed, and how are they organized?

<details>
<summary>Show Answer</summary>
Each chip is 4K x 4 = 4096 x 4 bits. Target is 16K x 8 = 16384 x 8 bits. Total target bits = 16384 x 8 = 131072 bits. Per chip bits = 4096 x 4 = 16384 bits. Chips needed = 131072 / 16384 = 8 chips. Organization: Create 2 banks of 4 chips each for word width (4-bit to 8-bit), then use a 2-to-4 decoder on the two highest address lines to select among the 4 banks for address expansion.
</details>

**Q4:** Distinguish between NAND Flash and NOR Flash in terms of access characteristics and typical usage.

<details>
<summary>Show Answer</summary>
NOR Flash provides random-access read (byte-addressable) with fast read times, making it suitable for execute-in-place (XIP) firmware like BIOS/UEFI. NAND Flash is block-oriented with slower random read but much faster sequential read/write, higher density, and lower cost per bit, making it ideal for mass storage devices like SSDs and USB drives.
</details>

**Q5:** A DRAM requires a refresh operation every 64 ms. If the memory has 8192 rows and each refresh operation takes 50 ns to refresh one row, what fraction of the memory's time is spent on refreshing?

<details>
<summary>Show Answer</summary>
Time to refresh all rows = 8192 x 50 ns = 409,600 ns = 0.4096 ms. Fraction = 0.4096 ms / 64 ms = 0.0064 = 0.64%.
</details>

---