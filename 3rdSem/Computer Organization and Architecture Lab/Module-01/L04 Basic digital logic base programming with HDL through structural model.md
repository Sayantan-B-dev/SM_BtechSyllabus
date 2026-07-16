# Basic digital logic base programming with HDL through structural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 4  
**Date:** 16-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a full adder using structural modeling by cascading two half adders.
- Understand hierarchical design -- using one entity inside another.
- Verify functionality through exhaustive simulation.

## Theory

**Full Adder:**
A full adder adds three single-bit inputs: A, B, and Carry-in (Cin). It produces:
- Sum (S) = A xor B xor Cin
- Carry-out (Cout) = (A AND B) OR (Cin AND (A XOR B))

**Structural Implementation using two Half Adders:**
A full adder can be built with two half adders and one OR gate:
1. First half adder: sum1 = A xor B, carry1 = A & B
2. Second half adder: Sum = sum1 xor Cin, carry2 = sum1 & Cin
3. Cout = carry1 OR carry2

## Truth Table

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0  |
| 0 | 0 |  1  |  1  |  0  |
| 0 | 1 |  0  |  1  |  0  |
| 0 | 1 |  1  |  0  |  1  |
| 1 | 0 |  0  |  1  |  0  |
| 1 | 0 |  1  |  0  |  1  |
| 1 | 1 |  0  |  0  |  1  |
| 1 | 1 |  1  |  1  |  1  |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

-- Half Adder (building block)
entity half_adder is
  port (
    a, b  : in  std_logic;
    sum,
    carry : out std_logic
  );
end entity;

architecture dataflow of half_adder is
begin
  sum   <= a XOR b;
  carry <= a AND b;
end architecture;

-- Full Adder using two half adders
entity full_adder is
  port (
    a, b, cin : in  std_logic;
    sum, cout : out std_logic
  );
end entity;

architecture structural of full_adder is
  signal sum1, carry1, carry2 : std_logic;
begin
  ha1: entity work.half_adder port map (
    a => a, b => b, sum => sum1, carry => carry1
  );
  ha2: entity work.half_adder port map (
    a => sum1, b => cin, sum => sum, carry => carry2
  );
  cout <= carry1 OR carry2;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_full_adder is
end entity;

architecture sim of tb_full_adder is
  signal a, b, cin, sum, cout : std_logic;
begin
  uut: entity work.full_adder port map (
    a => a, b => b, cin => cin, sum => sum, cout => cout
  );

  process begin
    report "A B Cin Sum Cout";

    -- Exhaustive test: 8 combinations
    (a, b, cin) <= std_logic_vector'("000"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("001"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("010"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("011"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("100"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("101"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("110"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("111"); wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=0 B=0 Cin=0 | Sum=0 Cout=0
A=0 B=0 Cin=1 | Sum=1 Cout=0
A=0 B=1 Cin=0 | Sum=1 Cout=0
A=0 B=1 Cin=1 | Sum=0 Cout=1
A=1 B=0 Cin=0 | Sum=1 Cout=0
A=1 B=0 Cin=1 | Sum=0 Cout=1
A=1 B=1 Cin=0 | Sum=0 Cout=1
A=1 B=1 Cin=1 | Sum=1 Cout=1
```

## Conclusion

Successfully designed a full adder using structural modeling by instantiating two half adders and an OR gate in VHDL. The hierarchical design approach was demonstrated and verified against the full adder truth table.
