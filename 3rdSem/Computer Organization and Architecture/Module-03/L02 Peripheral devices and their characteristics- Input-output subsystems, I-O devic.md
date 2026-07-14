# Peripheral devices and their characteristics: Input-output subsystems, I/O device interface

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 2  
**Date:** 19-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to Peripheral Devices

A **peripheral device** is any hardware device connected to a computer system that provides input, output, or storage functions. Peripherals expand the capabilities of the computer beyond the CPU and main memory.

**Categories:**

1. **Input devices:** Provide data to the computer.
2. **Output devices:** Present data from the computer to the user.
3. **Storage devices:** Store data persistently.

---

### 2. Types of Peripheral Devices

#### 2.1 Input Devices

| Device   | Function                                                      | Data Rate (approx) | Data Representation       |
|----------|---------------------------------------------------------------|--------------------|---------------------------|
| Keyboard | Converts key presses into scan codes                          | ~10 B/s (human)    | ASCII / scan codes        |
| Mouse    | Tracks movement and button clicks                             | ~100 B/s           | Relative (dx, dy), clicks |
| Scanner  | Converts text/images into digital bitmaps                     | ~10 MB/s           | Raster image (TIFF, JPEG) |
| Microphone| Converts sound waves into digital audio samples              | ~44-192 KB/s       | PCM samples (16/24-bit)   |
| Webcam   | Captures video frames as digital images                       | ~30-100 MB/s       | YUV / RGB frames          |
| Touchscreen| Detects touch position and pressure                         | ~1 KB/s            | (x, y, pressure) coordinates|
| Barcode Reader| Reads optical barcodes                                   | ~1 KB/s            | Encoded numeric/alpha     |

#### 2.2 Output Devices

| Device   | Function                                                      | Data Rate (approx) | Data Representation       |
|----------|---------------------------------------------------------------|--------------------|---------------------------|
| Monitor  | Displays visual output (pixels)                               | ~100-500 MB/s      | RGB pixel data (framebuffer)|
| Printer  | Produces hardcopy output                                      | ~1-50 MB/s         | Page description lang. (PCL, PostScript) or raster|
| Speakers | Converts electrical signals to sound                          | ~44-192 KB/s       | PCM audio samples         |
| Headphones| Same as speakers, personal                                  | ~44-192 KB/s       | PCM audio samples         |
| Projector| Projects visual output onto a screen                          | ~100-500 MB/s      | RGB pixel data            |
| Plotter  | Draws vector graphics on paper                                | ~1 MB/s            | Vector commands (HPGL)    |

#### 2.3 Storage Devices

| Device     | Function                                                      | Data Rate            | Data Representation       |
|------------|---------------------------------------------------------------|----------------------|---------------------------|
| HDD        | Magnetic disk storage                                         | 100-200 MB/s         | Sectors (512B-4KB blocks) |
| SSD        | Flash-based storage (NAND)                                    | 200-7000 MB/s        | Pages/blocks (NVMe/SATA)  |
| Optical (CD/DVD/Blu-ray)| Optical disc storage                              | 1-50 MB/s            | Sectors (2048B frames)    |
| Magnetic Tape| Sequential access archival storage                          | 100-300 MB/s (stream)| Blocks (variable length)  |
| USB Flash  | Portable flash storage                                        | 10-500 MB/s          | Logical blocks (LBA)      |

---

### 3. Device Characteristics

Key characteristics that define a peripheral device:

#### 3.1 Data Rate (Bandwidth)

The speed at which data can be transferred to/from the device. Measured in bits per second (bps), bytes per second (B/s), or MB/s.

- **Keyboard:** ~10 B/s (limited by human typing speed).
- **HDD:** ~150 MB/s (mechanical latency bound).
- **SSD (NVMe):** ~3-7 GB/s (limited by PCIe bandwidth).
- **Monitor (4K@60Hz):** ~12 Gb/s (DisplayPort).

#### 3.2 Unit of Transfer

The smallest quantum of data exchanged.

- **Character-oriented:** Keyboard (character), printer (character or line).
- **Block-oriented:** Disk (sector, 512 bytes), network (packet, 1500 bytes).
- **Stream-oriented:** Audio/video (continuous stream of samples/frames).

#### 3.3 Data Representation

How information is encoded.

- **Keyboard:** Scan codes (keyboard-specific) mapped to ASCII/Unicode.
- **Mouse:** Relative coordinate packets (delta-X, delta-Y, buttons).
- **Display:** RGB pixel values (8-10 bits per channel).
- **Audio:** PCM (Pulse Code Modulation) samples.
- **Storage:** Binary data organized into filesystems.

#### 3.4 Timing and Synchronization

- **Synchronous:** Data transfer is coordinated with a clock (e.g., SPI, I2C).
- **Asynchronous:** Data transfer uses handshaking (e.g., RS-232, USB).
- **Isynchronous:** Guaranteed bandwidth with bounded latency (e.g., USB isochronous for audio).

---

### 4. I/O Module Functions

The **I/O module** is the interface between the CPU/memory bus and the peripheral device. It handles the differences in data rates, formats, and timing.

#### Key Functions

**Function 1: Control and Timing**
- Coordinates the flow of data between internal resources (CPU, memory) and external devices.
- Manages bus arbitration, command sequencing, and timing signals.
- Example: CPU sends a "read" command to the I/O module, which then issues the appropriate sequence of control signals to the disk drive.

**Function 2: Device Communication**
- Translates CPU commands into device-specific signals.
- Handles device-specific protocols (e.g., ATA commands for disk, HID protocol for keyboard).

**Function 3: Data Buffering**
- Compensates for speed differences between the CPU/memory bus (fast) and the peripheral device (typically slower).
- Data is temporarily stored in buffers inside the I/O module.
- Example: Printer buffer holds a page of data while the printer prints it slowly.

**Function 4: Error Detection**
- Detects and reports errors that occur during transmission or device operation.
- Uses parity bits, CRC (Cyclic Redundancy Check), checksums.
- Reports errors to the CPU via status registers or interrupts.

**Additional Functions:**
- **Address decoding:** Determines which device is being accessed.
- **Data format conversion:** Serial-to-parallel, parallel-to-serial, analog-to-digital.
- **Power management:** Device power-up/power-down sequencing.

---

### 5. I/O Module Structure

#### Block Diagram of an I/O Module

```
          +=======================+
          |       I/O Module      |
          |                       |
  CPU /   |  +-------+ +-------+  |  +-------+  Peripheral
  Memory  |  | Data   | | Status|  |  |Device  |  Device
  Bus ----+->| Buffer| |Reg   |  +->|Interface|---->
          |  |       | |      |  |  |Circuitry|  |
          |  +-------+ +-------+  |  +-------+  |
          |                       |              |
          |  +-------+ +-------+  |              |
          |  |Control| |Address|  |              |
          |  | Logic | |Decoder|  |              |
          |  |       | |      |  |              |
          |  +-------+ +-------+  |              |
          +=======================+              |
                 |                               |
            Control Bus                    Device-specific
            Address Bus                   cables/signals
            Data Bus
```

**Components explained:**

1. **Address Decoder:** Determines if the I/O module is being addressed by checking address lines against the assigned device address.
2. **Data Buffer:** Holds data temporarily during transfers. Size depends on the device (e.g., 1 byte for keyboard, 512 bytes for disk sector).
3. **Status Register:** Contains flags indicating device status (ready, busy, error).
4. **Control Logic:** Interprets commands from the CPU (read, write, seek, etc.) and generates device control signals.
5. **Device Interface Circuitry:** Handles device-specific electrical and protocol requirements (e.g., SATA controller, USB PHY).

---

### 6. I/O Module Types

| Type         | Examples                       | Characteristics                         |
|--------------|--------------------------------|-----------------------------------------|
| Programmed   | Simple parallel port           | CPU directly controls all operations    |
| Interrupt-driven| Keyboard controller         | Device signals CPU when ready           |
| DMA          | Disk controller, graphics card | Device accesses memory independently    |
| Channel I/O  | Mainframe I/O processors       | Dedicated I/O processor                 |

---

### 7. Device Interface Standards

Common interface standards that define how I/O modules connect to devices:

- **USB:** Universal Serial Bus, hot-pluggable, daisy-chain.
- **SATA:** Serial ATA, for storage devices.
- **PCIe:** PCI Express, high-speed internal bus.
- **HDMI/DisplayPort:** Digital video interfaces.
- **Thunderbolt:** High-speed combined protocol (PCIe + DisplayPort).

---

## Practice Problems

**Q1:** A 4K monitor (3840 x 2160 pixels) runs at 60 Hz with 24-bit color (8 bits per RGB channel). What is the data rate required to drive this display?

<details>
<summary>Show Answer</summary>
Pixels per frame = 3840 x 2160 = 8,294,400. Bits per frame = 8,294,400 x 24 = 199,065,600 bits = 199.07 Mb. Data rate = 199.07 Mb x 60 fps = 11,944 Mbps = ~11.9 Gbps.
</details>

**Q2:** Why is data buffering important in an I/O module?

<details>
<summary>Show Answer</summary>
The CPU and memory bus operate at very high speeds (GHz, GB/s), while peripherals are typically slower (KB/s to MB/s). Buffering allows the CPU to transfer data at bus speed into the buffer and return to other tasks, while the I/O module transfers data to/from the device at its own slower pace. Without buffering, the CPU would have to wait for the slow device for every byte.
</details>

**Q3:** Distinguish between character-oriented and block-oriented I/O devices with examples.

<details>
<summary>Show Answer</summary>
Character-oriented devices transfer data one character (typically 1 byte) at a time. Examples: keyboard (each keystroke generates one scan code), serial port (each byte). Block-oriented devices transfer a block of data (multiple bytes) in a single operation. Examples: hard disk (sector = 512 bytes or 4 KB), SSD (page = 4 KB), network interface (frame/packet = up to 1500 bytes).
</details>

**Q4:** List four essential functions performed by an I/O module and explain each briefly.

<details>
<summary>Show Answer</summary>
(1) Control and timing: coordinates the sequence of operations between CPU and device. (2) Device communication: translates CPU commands into device-specific signals. (3) Data buffering: temporarily stores data to bridge speed differences. (4) Error detection: checks for transmission errors using parity, CRC, or checksums and reports them to the CPU.
</details>

**Q5:** What is the unit of transfer for a hard disk drive and why?

<details>
<summary>Show Answer</summary>
The unit of transfer is a sector (typically 512 bytes or 4096 bytes). Disks are block devices that read and write entire sectors at once because the physical mechanism (spinning platters with magnetic heads) naturally reads a complete sector as the head passes over the track. Reading individual bytes from a disk would be extremely inefficient due to mechanical seek and rotational latency.
</details>

---