# Simulating VHDL Logic Gates in ModelSim (Without a Testbench)

This guide shows how to simulate the **AND, OR, NAND, NOR, XOR, XNOR, and NOT gates** directly in **ModelSim** using the **`force`** command.

---

# Step 1: Create a New Project

1. Open **ModelSim**.
2. Select **File → New → Project**.
3. Enter a project name (e.g., `Logic_Gates`).
4. Choose a project location.
5. Click **OK**.

---

# Step 2: Add VHDL Files

Click **Add Existing File** and add the following files:

* `and_gate.vhd`
* `or_gate.vhd`
* `nand_gate.vhd`
* `nor_gate.vhd`
* `xor_gate.vhd`
* `xnor_gate.vhd`
* `not_gate.vhd`

Click **OK**.

---

# Step 3: Compile the Files

From the menu:

```
Compile → Compile All
```

If successful, the Transcript should display:

```
Compile of and_gate.vhd was successful.
Compile of or_gate.vhd was successful.
Compile of nand_gate.vhd was successful.
Compile of nor_gate.vhd was successful.
Compile of xor_gate.vhd was successful.
Compile of xnor_gate.vhd was successful.
Compile of not_gate.vhd was successful.

7 compiles, 0 failed.
```

---

# Step 4: Open the Transcript Window

If it is not already visible:

```
View → Transcript
```

All simulation commands below are entered into the **Transcript**.

---

# Step 5: Simulate the AND Gate

```tcl
vsim work.and_gate
add wave *

force A 0
force B 0
run 100 ns

force A 0
force B 1
run 100 ns

force A 1
force B 0
run 100 ns

force A 1
force B 1
run 100 ns
```

Observe the waveform.

---

# Step 6: Simulate the OR Gate

```tcl
quit -sim

vsim work.or_gate
add wave *

force A 0
force B 0
run 100 ns

force A 0
force B 1
run 100 ns

force A 1
force B 0
run 100 ns

force A 1
force B 1
run 100 ns
```

Observe the waveform.

---

# Step 7: Simulate the NAND Gate

```tcl
quit -sim

vsim work.nand_gate
add wave *

force A 0
force B 0
run 100 ns

force A 0
force B 1
run 100 ns

force A 1
force B 0
run 100 ns

force A 1
force B 1
run 100 ns
```

Observe the waveform.

---

# Step 8: Simulate the NOR Gate

```tcl
quit -sim

vsim work.nor_gate
add wave *

force A 0
force B 0
run 100 ns

force A 0
force B 1
run 100 ns

force A 1
force B 0
run 100 ns

force A 1
force B 1
run 100 ns
```

Observe the waveform.

---

# Step 9: Simulate the XOR Gate

```tcl
quit -sim

vsim work.xor_gate
add wave *

force A 0
force B 0
run 100 ns

force A 0
force B 1
run 100 ns

force A 1
force B 0
run 100 ns

force A 1
force B 1
run 100 ns
```

Observe the waveform.

---

# Step 10: Simulate the XNOR Gate

```tcl
quit -sim

vsim work.xnor_gate
add wave *

force A 0
force B 0
run 100 ns

force A 0
force B 1
run 100 ns

force A 1
force B 0
run 100 ns

force A 1
force B 1
run 100 ns
```

Observe the waveform.

---

# Step 11: Simulate the NOT Gate

```tcl
quit -sim

vsim work.not_gate
add wave *

force A 0
run 100 ns

force A 1
run 100 ns
```

Observe the waveform.

---

# Step 12: Viewing the Results

The **Wave** window will display:

* Inputs (`A`, `B`)
* Output (`C` or your output signal name)

Verify the outputs using the logic tables.

### AND Gate

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 0      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |

### OR Gate

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

### NAND Gate

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 1      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 0      |

### NOR Gate

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 1      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 0      |

### XOR Gate

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 0      |

### XNOR Gate

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 1      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |

### NOT Gate

| A | Output |
| - | ------ |
| 0 | 1      |
| 1 | 0      |

---

# Summary

1. Create a new ModelSim project.
2. Add all VHDL files.
3. Compile all files.
4. Simulate each gate using `vsim work.<gate_name>`.
5. Use `force` commands to apply input combinations.
6. Run each input combination for **100 ns**.
7. Observe the output waveform and verify it against the corresponding truth table.

This approach is ideal for simple combinational circuits when you want to verify functionality without writing separate VHDL testbench files.
