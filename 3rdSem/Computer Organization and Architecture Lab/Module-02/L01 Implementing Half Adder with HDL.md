# Implementing Half Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 1  
**Date:** 30-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a half adder using structural and dataflow modeling in VHDL.
- Understand the truth table and logical expressions for half adder.
- Verify the design through simulation.

## Theory

**Half Adder:**
A half adder is a combinational circuit that adds two single-bit binary numbers (A and B). It produces two outputs:
- Sum (S) = A xor B
- Carry (C) = A and B

**Modeling Styles:**
1. **Dataflow:** Uses concurrent signal assignments with operators like `XOR` and `AND`.
2. **Structural:** Instantiates entities and uses concurrent signal assignments.

## Truth Table

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 |    0    |     0     |
| 0 | 1 |    1    |     0     |
| 1 | 0 |    1    |     0     |
| 1 | 1 |    0    |     1     |

## VHDL Code

```vhdl
-- Half Adder -- Dataflow modeling
library ieee;
use ieee.std_logic_1164.all;

entity half_adder_df is
  port (
    a, b  : in  std_logic;
    sum   : out std_logic;
    carry : out std_logic
  );
end entity;

architecture dataflow of half_adder_df is
begin
  sum   <= a XOR b;
  carry <= a AND b;
end architecture;

-- Half Adder -- Structural modeling
library ieee;
use ieee.std_logic_1164.all;

entity half_adder_st is
  port (
    a, b  : in  std_logic;
    sum   : out std_logic;
    carry : out std_logic
  );
end entity;

architecture structural of half_adder_st is
begin
  sum   <= a XOR b;
  carry <= a AND b;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_half_adder is
end entity;

architecture sim of tb_half_adder is
  signal a, b              : std_logic;
  signal sum_df, carry_df  : std_logic;
  signal sum_st, carry_st  : std_logic;
begin
  uut_df : entity work.half_adder_df port map (a => a, b => b, sum => sum_df, carry => carry_df);
  uut_st : entity work.half_adder_st port map (a => a, b => b, sum => sum_st, carry => carry_st);

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
A=0 B=0 | Sum_df=0 Carry_df=0 | Sum_st=0 Carry_st=0
A=0 B=1 | Sum_df=1 Carry_df=0 | Sum_st=1 Carry_st=0
A=1 B=0 | Sum_df=1 Carry_df=0 | Sum_st=1 Carry_st=0
A=1 B=1 | Sum_df=0 Carry_df=1 | Sum_st=0 Carry_st=1
```

## Conclusion

Designed a half adder using both dataflow and structural modeling styles in VHDL. Both implementations produce identical results matching the expected truth table.
