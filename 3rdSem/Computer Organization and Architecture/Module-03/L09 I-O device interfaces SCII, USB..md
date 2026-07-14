# I/O device interfaces SCSI, USB

**Course:** Computer Organization and Architecture  
**Module:** 3 | **Lecture:** 9  
**Date:** 08-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to I/O Interfaces

An **I/O interface** is a standardized protocol and physical connection that allows peripheral devices to communicate with the computer system. Two historically significant interfaces are:
- **SCSI (Small Computer System Interface)** -- a parallel interface used for high-performance storage.
- **USB (Universal Serial Bus)** -- a serial interface used for a wide variety of peripherals.

---

### 2. SCSI (Small Computer System Interface)

SCSI is a **parallel interface** standard for connecting storage devices (hard drives, tape drives, CD-ROMs, scanners) to a computer. It was widely used in servers and high-end workstations before SATA and SAS became dominant.

#### 2.1 SCSI Architecture

SCSI uses a **daisy-chain** topology where multiple devices are connected in a linear chain to a host adapter.

```
   +===========+       +===========+       +===========+       +===========+
   |  Host     |       |  HDD 0    |       |  HDD 1    |       |  Scanner  |
   | Adapter   |=======| (ID 0)    |=======| (ID 1)    |=======| (ID 2)    |
   | (Initiator)|       | (Target)  |       | (Target)  |       | (Target)  |
   +===========+       +===========+       +===========+       +===========+
         |
         |                   (up to 7 or 15 devices)
         |
         +===================== Terminator ===========================+
```

**Key Characteristics:**
- **Parallel bus:** 8-bit (narrow) or 16-bit (wide) data bus.
- **Daisy-chain topology:** Devices are connected in sequence.
- **Termination:** Both ends of the SCSI bus must be terminated (with resistors or active terminators) to prevent signal reflections.
- **Maximum cable length:** Up to 12 meters (differential) or 1.5-6 meters (single-ended), depending on speed.

#### 2.2 SCSI IDs

Each device on the SCSI bus has a unique **SCSI ID** (0-7 for 8-bit bus, 0-15 for 16-bit bus).

- SCSI ID 7 has the **highest priority** (usually assigned to the host adapter).
- Priority decreases: 7 > 6 > 5 > ... > 0.
- IDs are set via physical jumpers or switches on older devices; modern devices use plug-and-play.

| SCSI ID | Typical Device              | Priority Level |
|---------|-----------------------------|----------------|
| 7       | Host adapter (initiator)    | Highest        |
| 6       | High-priority disk          |                |
| 5       | Disk                        |                |
| 4       | Disk                        |                |
| 3       | CD-ROM / tape               |                |
| 2       | Scanner                     |                |
| 1       | Low-priority disk           |                |
| 0       | Boot disk (often)           | Lowest         |

#### 2.3 Initiator and Target

- **Initiator:** The device that starts a command (usually the host adapter). The initiator sends SCSI commands.
- **Target:** The device that receives and executes commands (the peripheral device, e.g., disk drive).
- A device can act as both initiator and target in some configurations.

#### 2.4 SCSI Phases of Operation

SCSI bus communication follows a defined sequence of phases:

```
   Bus Free Phase            (no device using the bus)
        |
   Arbitration Phase        (device with highest ID wins bus control)
        |
   Selection Phase          (initiator selects a target)
        |
   Command Phase            (initiator sends Command Descriptor Block)
        |
   Data Phase               (data transfer: Data In or Data Out)
        |
   Message Phase            (status and control messages)
        |
   Status Phase             (target sends status: Good, Check Condition, etc.)
        |
   Bus Free Phase           (bus released for next operation)
```

#### 2.5 SCSI Versions

| Version          | Bus Width | Max Speed  | Max Devices | Max Cable Length |
|------------------|-----------|------------|-------------|------------------|
| SCSI-1 (1986)    | 8-bit     | 5 MB/s     | 8           | 6 m              |
| SCSI-2 (Fast)    | 8-bit     | 10 MB/s    | 8           | 3 m              |
| SCSI-2 (Wide)    | 16-bit    | 20 MB/s    | 16          | 3 m              |
| Ultra SCSI       | 8-bit     | 20 MB/s    | 8           | 1.5 m            |
| Ultra Wide SCSI  | 16-bit    | 40 MB/s    | 16          | 1.5 m            |
| Ultra-2 SCSI     | 8-bit     | 40 MB/s    | 8           | 12 m (LVD)       |
| Ultra-2 Wide SCSI| 16-bit    | 80 MB/s    | 16          | 12 m (LVD)       |
| Ultra-3 (Ultra160)| 16-bit   | 160 MB/s   | 16          | 12 m (LVD)       |
| Ultra-4 (Ultra320)| 16-bit   | 320 MB/s   | 16          | 12 m (LVD)       |

#### 2.6 SCSI Command Descriptor Block (CDB)

Commands are sent as a CDB structure:

```
   Byte 0:   Operation Code (e.g., 0x28 = READ(10), 0x2A = WRITE(10))
   Byte 1:   LUN, DPO, FUA, Reserved, RelAdr
   Bytes 2-5: Logical Block Address (LBA)
   Byte 6:   Reserved
   Byte 7-8: Transfer Length
   Byte 9:   Control
```

Example: READ(10) command reads blocks from the specified LBA.

---

### 3. USB (Universal Serial Bus)

USB is a **serial interface** standard designed to connect a wide variety of peripherals to a computer. It is hot-pluggable, self-configuring, and supports power delivery.

#### 3.1 USB Architecture

USB uses a **tiered star topology** with a single **host controller** at the root.

```
                     +====================+
                     |      Computer      |
                     |   (Host Controller)|
                     +========+===========+
                              |
                        +-----+-----+
                        |   Root    |
                        |   Hub     |
                        +-----+-----+
                              |
               +--------------+--------------+
               |              |              |
         +-----+-----+  +----+----+   +-----+-----+
         |   Hub      |  | Device  |   | Device     |
         +-----+------+  |(Keyboard)|  |(Mouse)     |
               |         +---------+   +-----------+
          +----+----+
          | Device  |
          |(Printer)|
          +---------+
```

**Key Components:**

1. **Host Controller:** The root of the USB system. Manages the bus, schedules transfers, and communicates with devices. Connects to the system via PCIe or similar.

2. **Hubs:** Provide additional connection points (ports). Hubs can be cascaded up to 7 tiers (including the root hub). Hubs repeat signals and manage power distribution.

3. **Devices:** Peripherals that connect to the bus. Each device has a unique **device address** (assigned by the host during enumeration).

#### 3.2 USB Enumeration Process

When a USB device is plugged in, the host performs **enumeration**:

1. **Hub detects device:** The hub detects a voltage change on the D+ or D- data line.
2. **Hub reports to host:** The hub sends an interrupt transfer to the host with port status change.
3. **Host resets device:** The host sends a reset signal to the device.
4. **Device responds at address 0:** After reset, the device responds at default address 0.
5. **Host reads device descriptor:** The host sends a GET_DESCRIPTOR request to learn about the device (vendor ID, product ID, class, etc.).
6. **Host assigns unique address:** The host assigns a unique 7-bit address to the device.
7. **Host reads configuration descriptors:** The host learns about the device's interfaces, endpoints, and capabilities.
8. **Host selects configuration:** The host sends SET_CONFIGURATION to activate the device.
9. **Device is ready:** The device is now fully operational.

#### 3.3 USB Transfer Types

USB supports four transfer types, optimized for different needs:

| Transfer Type  | Guarantees              | Latency  | Bandwidth  | Error Handling        | Typical Use           |
|----------------|-------------------------|----------|------------|-----------------------|-----------------------|
| Control        | Delivery                | Moderate | Low        | Retry + CRC           | Enumeration, commands |
| Bulk           | Delivery                | Variable | High       | Retry + CRC           | Storage, printers     |
| Interrupt      | Periodic polling        | Bounded  | Low        | Retry + CRC           | HID (keyboard, mouse) |
| Isochronous    | Bandwidth, no retry     | Bounded  | High       | CRC only (no retry)   | Audio, video          |

**Control Transfers:**
- Used for configuration, command, and status operations.
- Always initiated by the host.
- Guaranteed delivery with retry.
- Maximum packet size: 8, 16, 32, or 64 bytes.

**Bulk Transfers:**
- Used for large, non-time-sensitive data transfers.
- Guaranteed delivery (retry on error).
- Bandwidth is variable -- uses whatever bandwidth is available after other transfers.
- Example: USB mass storage (flash drives, external HDDs).
- Maximum packet size: 64 bytes (USB 2.0 full-speed), 512 bytes (USB 2.0 high-speed), 1024 bytes (USB 3.0).

**Interrupt Transfers:**
- Used for devices that need guaranteed polling frequency.
- Host polls the device at a specified interval (1-255 ms for USB 1.x/2.0, 1-65535 units of 125 us for USB 2.0 microframes).
- Bounded latency and guaranteed delivery.
- Example: Keyboard reports every 8 ms (125 Hz polling rate).
- Maximum packet size: 64 bytes (USB 2.0), 1024 bytes (USB 3.0).

**Isochronous Transfers:**
- Used for time-sensitive data (audio, video streams).
- Guaranteed bandwidth but NO retry on error (CRC detected errors are not corrected).
- Pre-allocated bandwidth at enumeration.
- Example: USB microphone sending 48 kHz 16-bit stereo audio = 192 KB/s.
- Maximum packet size: 1023 bytes (USB 2.0), 1024 bytes (USB 3.0).

#### 3.4 USB Versions

| USB Version | Year | Max Data Rate | Signaling Rate | Connector Types    | Notes                     |
|-------------|------|---------------|----------------|---------------------|---------------------------|
| USB 1.0     | 1996 | 1.5 Mbps      | 1.5 Mbps       | Type A, Type B      | Low Speed (keyboard, mouse)|
| USB 1.1     | 1998 | 12 Mbps       | 12 Mbps        | Type A, Type B      | Full Speed               |
| USB 2.0     | 2000 | 480 Mbps      | 480 Mbps       | Type A, Type B, Mini| High Speed, backward compatible |
| USB 3.0     | 2008 | 5 Gbps        | 5 Gbps         | Type A, Type B, Micro B, Type C| SuperSpeed, 2 additional differential pairs |
| USB 3.1 Gen2| 2013 | 10 Gbps       | 10 Gbps        | Type A, Type C      | SuperSpeed+             |
| USB 3.2      | 2017 | 20 Gbps (2x2) | 10 Gbps x2 lanes| Type C only       | Uses two-lane operation  |
| USB4         | 2019 | 40 Gbps       | 20 Gbps x2     | Type C only        | Based on Thunderbolt 3   |

#### 3.5 USB Connector Types

```
   Type A (Host/Upstream):
   +------------------+
   | 1  2  3  4       |
   |  Vb  D- D+ Gnd   |
   +------------------+
   USB 1.x/2.0: 4 pins
   USB 3.0: additional 5 pins inside (SS)

   Type B (Device/Downstream):
   +----------+
   | 1  2     |
   | 3  4     |
   +----------+
   Squarish shape with beveled corners.

   Mini USB:
   +------+
   |1 2 3 |
   |4 5   |
   +------+
   5 pins, used in older devices.

   Micro USB:
   +-------+
   |1 2 3  |
   |4 5    |
   +-------+
   5 pins, thinner than Mini USB.

   Type C:
   +------------------+
   | 24 pins, reversible|
   | symmetrical, supports|
   | USB 3.x, USB4, DP,|
   | Thunderbolt, PD   |
   +------------------+
   Reversible plug, supports Alternate Modes (DisplayPort, HDMI, Thunderbolt).
```

#### 3.6 USB Power Delivery (USB-PD)

USB Type C with USB-PD supports:
- **Standard:** 5V @ 500mA (USB 2.0) / 900mA (USB 3.0).
- **USB-PD:** Up to 48V @ 5A = 240W (USB-PD 3.1).
- **Negotiation:** Devices negotiate voltage and current via configuration channel (CC) wire.
- **Direction:** Power can flow either direction (host charges device, or device charges host).

---

### 4. Comparison: SCSI vs USB

| Feature              | SCSI                               | USB                                |
|----------------------|------------------------------------|------------------------------------|
| Bus type             | Parallel                           | Serial                             |
| Topology             | Daisy chain                        | Tiered star (hub-based)            |
| Max devices          | 8 or 16                            | 127 per host controller            |
| Hot-pluggable        | Yes (later versions) / Usually not | Yes                                |
| Cable length         | Up to 12 m (LVD)                   | 5 m per segment (hub to device)    |
| Data rate            | Up to 320 MB/s (Ultra320)          | Up to 40 Gbps (USB4)              |
| addressing           | Physical ID (jumper/switch)        | Dynamic address (enumeration)      |
| Termination required | Yes (physical terminators)         | No (built-in)                      |
| Primary use          | Storage devices (HDD, tape)        | General purpose peripherals        |
| Power delivery       | No (separate power)                | Yes (up to 240W with USB-PD)       |
| Plug and play        | Limited                            | Full                               |
| Protocol overhead    | Lower                              | Higher                             |
| Cost                 | Higher (controller + cable)        | Lower                              |
| Host adapter         | Dedicated SCSI HBA                 | Often integrated on motherboard    |

---

### 5. ASCII Diagram: USB vs SCSI System Architecture

```
   SCSI System:

   +----------+      +------+      +------+      +------+
   | Host     |======| HDD 0|======| HDD 1|======| Tape |
   | Adapter  |      | ID 0 |      | ID 1 |      | ID 2 |
   +----------+      +------+      +------+      +------+
   (Initiator)        (Targets)                 (terminated)

   Parallel bus shared by all devices.
   One device transfers at a time (bus arbitration).


   USB System:

   +-------------+
   | Host Ctrlr  |-----> Hub -----> Device A
   | (Root)      |       |
   |             |       +-----> Device B
   |             |       |
   |             |       +-----> Hub -----> Device C
   +-------------+                       |
                                         +-----> Device D
   Serial point-to-point links.
   Host controls all communication.
   Devices only speak when spoken to.
```

---

### 6. Legacy Note on "SCII"

The original filename listed "SCII" which is a common typographical error. The correct acronym is **SCSI** (Small Computer System Interface), pronounced "scuzzy."

---

## Practice Problems

**Q1:** A SCSI bus has 8 devices including the host adapter. What is the maximum number of disk drives that can be connected? If the bus uses Ultra320 SCSI, what is the maximum theoretical throughput?

<details>
<summary>Show Answer</summary>
8 total IDs - 1 host adapter = 7 devices (disk drives). In practice, one or more IDs may be used for other peripherals. Ultra320 SCSI provides 320 MB/s theoretical throughput using a 16-bit bus at 160 MHz double-edged clocking (16 bits x 160 MHz x 2 = 5120 Mbps = 320 MB/s).
</details>

**Q2:** Describe the USB enumeration process from the moment a device is plugged in to the moment it is ready for use.

<details>
<summary>Show Answer</summary>
(1) Hub detects device via voltage change on D+/D- lines. (2) Hub reports port status change to host (interrupt transfer). (3) Host sends port reset to device. (4) Device is now at default address 0. (5) Host sends GET_DESCRIPTOR (Device Descriptor). (6) Host assigns unique 7-bit address to device via SET_ADDRESS. (7) Host reads Configuration Descriptors (interfaces, endpoints). (8) Host sends SET_CONFIGURATION to activate device. (9) Device is ready for data transfers.
</details>

**Q3:** Compare the four USB transfer types. When would you use each?

<details>
<summary>Show Answer</summary>
(1) Control: used for device enumeration and commands -- guaranteed delivery, low bandwidth. (2) Bulk: used for mass storage -- guaranteed delivery, variable bandwidth, uses leftover bus time. (3) Interrupt: used for HID devices (keyboard, mouse) -- guaranteed periodic polling, bounded latency, guaranteed delivery. (4) Isochronous: used for audio/video streaming -- guaranteed bandwidth, no retry on error, time-sensitive delivery is more important than perfect accuracy.
</details>

**Q4:** Why does SCSI require bus termination while USB does not?

<details>
<summary>Show Answer</summary>
SCSI is a parallel bus where signals travel in both directions. Without termination, signal reflections occur at the ends of the bus, corrupting data. Terminators absorb the signals at both endpoints. USB uses point-to-point serial links with built-in impedance matching -- transmitters and receivers are designed to match the characteristic impedance of the cable, so no external termination is needed.
</details>

**Q5:** A USB 3.0 device sends isochronous audio data. The audio is 2-channel, 24-bit samples at 96 kHz. What is the raw data rate? Can USB 2.0 isochronous transfers handle this?

<details>
<summary>Show Answer</summary>
Raw data rate = 2 channels x 24 bits x 96000 Hz = 4,608,000 bps = 4.608 Mbps. USB 2.0 isochronous transfers support up to 1023 bytes per microframe (125 us). Max isochronous bandwidth = 1023 bytes x 8000 microframes/sec = 8,184,000 bytes/sec = 65.472 Mbps. So yes, USB 2.0 can easily handle 4.608 Mbps. USB 3.0 would also handle it easily.
</details>

---