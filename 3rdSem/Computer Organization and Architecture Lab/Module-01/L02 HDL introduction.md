# HDL introduction

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 2  
**Date:** 09-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Computer Organization and Design: The Hardware/Software Interface, David A. Patterson and John L. Hennessy, 5th edition, Elsevier. & Lab Manual

## Lab Objectives

- Implement and simulate NAND, NOR, XOR, and XNOR gates using dataflow VHDL.
- Understand the concept of universal gates (NAND and NOR) and their ability to implement any Boolean function.
- Verify all gates through simulation testbench.

## Theory

**Universal Gates:**
- NAND gate: `y <= NOT (a AND b)` -- A NAND gate alone can implement AND, OR, NOT, and any other logic function.
- NOR gate: `y <= NOT (a OR b)` -- Similarly universal; any Boolean expression can be realized using only NOR gates.

**XOR and XNOR:**
- XOR (exclusive-OR): `y <= a XOR b` -- Output is 1 when inputs differ.
- XNOR (exclusive-NOR): `y <= NOT (a XOR b)` -- Output is 1 when inputs are equal.

## Truth Table

| a | b | NAND | NOR | XOR | XNOR |
|---|---|------|-----|-----|------|
| 0 | 0 |  1   |  1  |  0  |  1   |
| 0 | 1 |  1   |  0  |  1  |  0   |
| 1 | 0 |  1   |  0  |  1  |  0   |
| 1 | 1 |  0   |  0  |  0  |  1   |

**NAND as Universal Gate -- Basic Equivalents:**
- NOT: `NAND(a, a)` = NOT a
- AND: `NAND(NAND(a,b), NAND(a,b))` = a AND b
- OR:  `NAND(NAND(a,a), NAND(b,b))` = a OR b

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

-- NAND gate
entity nand_gate is
  port (
    a : in  std_logic;
    b : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of nand_gate is
begin
  y <= NOT (a AND b);
end architecture;

-- NOR gate
entity nor_gate is
  port (
    a : in  std_logic;
    b : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of nor_gate is
begin
  y <= NOT (a OR b);
end architecture;

-- XOR gate
entity xor_gate is
  port (
    a : in  std_logic;
    b : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of xor_gate is
begin
  y <= a XOR b;
end architecture;

-- XNOR gate
entity xnor_gate is
  port (
    a : in  std_logic;
    b : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of xnor_gate is
begin
  y <= NOT (a XOR b);
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_gates2 is
end entity;

architecture sim of tb_gates2 is
  signal a, b               : std_logic;
  signal y_nand, y_nor,
         y_xor, y_xnor      : std_logic;
begin
  u1: entity work.nand_gate port map (a => a, b => b, y => y_nand);
  u2: entity work.nor_gate  port map (a => a, b => b, y => y_nor);
  u3: entity work.xor_gate  port map (a => a, b => b, y => y_xor);
  u4: entity work.xnor_gate port map (a => a, b => b, y => y_xnor);

  process begin
    report "a b NAND NOR XOR XNOR";

    a <= '0'; b <= '0'; wait for 10 ns;
    a <= '0'; b <= '1'; wait for 10 ns;
    a <= '1'; b <= '0'; wait for 10 ns;
    a <= '1'; b <= '1'; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
a=0 b=0 | NAND=1 NOR=1 XOR=0 XNOR=1
a=0 b=1 | NAND=1 NOR=0 XOR=1 XNOR=0
a=1 b=0 | NAND=1 NOR=0 XOR=1 XNOR=0
a=1 b=1 | NAND=0 NOR=0 XOR=0 XNOR=1
```

## Conclusion

Successfully implemented NAND, NOR, XOR, and XNOR gates using dataflow modeling in VHDL. The universal nature of NAND and NOR gates was discussed -- any logic circuit can be built using only these gates.
