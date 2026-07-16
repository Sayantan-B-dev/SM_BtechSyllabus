# Implementing Full Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 4  
**Date:** 06-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a full subtractor using VHDL.
- Understand the borrow logic in multi-bit subtraction.
- Verify the full subtractor truth table through exhaustive simulation.

## Theory

**Full Subtractor:**
A full subtractor performs subtraction of three single-bit inputs: A (minuend), B (subtrahend), and Bin (borrow-in). It produces:
- Difference (D) = A xor B xor Bin
- Borrow-out (Bout) = (~A & B) | (~A & Bin) | (B & Bin)
- Simplified: Bout = (~A & (B | Bin)) | (B & Bin)

The borrow-out indicates whether the subtraction of the current bit position requires a borrow from the next higher bit.

## Truth Table

| A | B | Bin | Diff | Bout |
|---|---|-----|------|------|
| 0 | 0 |  0  |  0   |  0   |
| 0 | 0 |  1  |  1   |  1   |
| 0 | 1 |  0  |  1   |  1   |
| 0 | 1 |  1  |  0   |  1   |
| 1 | 0 |  0  |  1   |  0   |
| 1 | 0 |  1  |  0   |  0   |
| 1 | 1 |  0  |  0   |  0   |
| 1 | 1 |  1  |  1   |  1   |

## VHDL Code

```vhdl
-- Full Subtractor -- Behavioral
library ieee;
use ieee.std_logic_1164.all;

entity full_subtractor_beh is
  port (
    a, b, bin : in  std_logic;
    diff, bout : out std_logic
  );
end entity;

architecture behavioral of full_subtractor_beh is
begin
  diff <= a XOR b XOR bin;
  bout <= (NOT a AND b) OR (NOT a AND bin) OR (b AND bin);
end architecture;

-- Half Subtractor sub-module (for structural)
library ieee;
use ieee.std_logic_1164.all;

entity half_subtractor is
  port (
    a, b   : in  std_logic;
    diff   : out std_logic;
    borrow : out std_logic
  );
end entity;

architecture dataflow of half_subtractor is
begin
  diff   <= a XOR b;
  borrow <= NOT a AND b;
end architecture;

-- Full Subtractor -- Structural using half subtractors
library ieee;
use ieee.std_logic_1164.all;

entity full_subtractor_str is
  port (
    a, b, bin : in  std_logic;
    diff, bout : out std_logic
  );
end entity;

architecture structural of full_subtractor_str is
  signal d1, b1, b2 : std_logic;
begin
  hs1 : entity work.half_subtractor port map (a => a, b => b, diff => d1, borrow => b1);
  hs2 : entity work.half_subtractor port map (a => d1, b => bin, diff => diff, borrow => b2);
  bout <= b1 OR b2;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_full_subtractor is
end entity;

architecture sim of tb_full_subtractor is
  signal a, b, bin, diff, bout : std_logic;
begin
  uut : entity work.full_subtractor_beh port map (a => a, b => b, bin => bin, diff => diff, bout => bout);

  process begin
    (a, b, bin) <= std_logic_vector'("000"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("001"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("010"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("011"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("100"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("101"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("110"); wait for 10 ns;
    (a, b, bin) <= std_logic_vector'("111"); wait for 10 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=0 B=0 Bin=0 | Diff=0 Bout=0
A=0 B=0 Bin=1 | Diff=1 Bout=1
A=0 B=1 Bin=0 | Diff=1 Bout=1
A=0 B=1 Bin=1 | Diff=0 Bout=1
A=1 B=0 Bin=0 | Diff=1 Bout=0
A=1 B=0 Bin=1 | Diff=0 Bout=0
A=1 B=1 Bin=0 | Diff=0 Bout=0
A=1 B=1 Bin=1 | Diff=1 Bout=1
```

## Conclusion

Implemented a full subtractor using both behavioral and structural modeling in VHDL. The borrow-out logic correctly handles the cases where A < (B + Bin).
