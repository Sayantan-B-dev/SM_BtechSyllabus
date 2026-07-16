# Basic digital logic base programming with HDL through structural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 3  
**Date:** 16-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Understand structural modeling in VHDL by instantiating components.
- Design a half adder using structural modeling with XOR and AND logic.
- Simulate and verify the half adder circuit.

## Theory

**Structural Modeling:**
In structural modeling, a digital circuit is described by interconnecting smaller components or entities. This resembles building a circuit on a breadboard by wiring components together.

**Half Adder:**
A half adder adds two single-bit binary numbers (A and B) and produces:
- Sum (S) = A xor B
- Carry (C) = A and B

**Component Instantiation:**
```vhdl
label_name : entity work.entity_name port map (
  port_a => signal_a,
  port_b => signal_b
);
```

## Truth Table

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 |    0    |     0     |
| 0 | 1 |    1    |     0     |
| 1 | 0 |    1    |     0     |
| 1 | 1 |    0    |     1     |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

-- Half Adder using dataflow modeling
entity half_adder is
  port (
    a     : in  std_logic;
    b     : in  std_logic;
    sum   : out std_logic;
    carry : out std_logic
  );
end entity;

architecture dataflow of half_adder is
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
  signal a, b, sum, carry : std_logic;
begin
  uut: entity work.half_adder port map (
    a => a, b => b, sum => sum, carry => carry
  );

  process begin
    report "A B Sum Carry";

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
A=0 B=0 | Sum=0 Carry=0
A=0 B=1 | Sum=1 Carry=0
A=1 B=0 | Sum=1 Carry=0
A=1 B=1 | Sum=0 Carry=1
```

## Conclusion

Designed a half adder using dataflow modeling in VHDL. The simulation results match the expected half adder truth table.
