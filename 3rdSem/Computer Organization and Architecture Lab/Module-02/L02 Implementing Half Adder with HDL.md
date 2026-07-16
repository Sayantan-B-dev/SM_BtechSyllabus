# Implementing Half Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 2  
**Date:** 30-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a half subtractor using VHDL.
- Understand the difference between half adder and half subtractor in VHDL.
- Verify the half subtractor truth table through simulation.

## Theory

**Half Subtractor:**
A half subtractor subtracts one single-bit binary number (B) from another (A). It produces two outputs:
- Difference (D) = A xor B
- Borrow-out (B_out) = (not A) and B

When A < B, a borrow is needed, so B_out = 1.

## Truth Table

| A | B | Difference (D) | Borrow-out (B_out) |
|---|---|----------------|--------------------|
| 0 | 0 |       0        |         0          |
| 0 | 1 |       1        |         1          |
| 1 | 0 |       1        |         0          |
| 1 | 1 |       0        |         0          |

## VHDL Code

```vhdl
-- Half Subtractor -- Dataflow
library ieee;
use ieee.std_logic_1164.all;

entity half_subtractor_df is
  port (
    a, b   : in  std_logic;
    diff   : out std_logic;
    borrow : out std_logic
  );
end entity;

architecture dataflow of half_subtractor_df is
begin
  diff   <= a XOR b;
  borrow <= NOT a AND b;
end architecture;

-- Half Subtractor -- Structural
library ieee;
use ieee.std_logic_1164.all;

entity half_subtractor_st is
  port (
    a, b   : in  std_logic;
    diff   : out std_logic;
    borrow : out std_logic
  );
end entity;

architecture structural of half_subtractor_st is
  signal not_a : std_logic;
begin
  not_a  <= NOT a;
  diff   <= a XOR b;
  borrow <= not_a AND b;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_half_subtractor is
end entity;

architecture sim of tb_half_subtractor is
  signal a, b, diff, borrow : std_logic;
begin
  uut : entity work.half_subtractor_df port map (a => a, b => b, diff => diff, borrow => borrow);

  process begin
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
A=0 B=0 | Diff=0 Borrow=0
A=0 B=1 | Diff=1 Borrow=1
A=1 B=0 | Diff=1 Borrow=0
A=1 B=1 | Diff=0 Borrow=0
```

## Conclusion

Implemented a half subtractor using dataflow and structural modeling in VHDL. The borrow output is 1 only when A=0 and B=1, correctly indicating that a borrow is needed.
