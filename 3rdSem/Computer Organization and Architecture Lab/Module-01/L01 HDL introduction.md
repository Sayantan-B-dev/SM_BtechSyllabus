# HDL introduction

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 1  
**Date:** 09-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Computer Organization and Design: The Hardware/Software Interface, David A. Patterson and John L. Hennessy, 5th edition, Elsevier. & Lab Manual

## Lab Objectives

- Understand the fundamental structure of a VHDL entity and architecture.
- Learn basic VHDL data types: `std_logic` and `std_logic_vector`.
- Implement and simulate basic logic gates (AND, OR, NOT) using dataflow modeling.

## Theory

**HDL (Hardware Description Language)** allows designers to describe digital circuits textually. VHDL is one of the most widely used HDLs.

**Entity and Architecture Structure:**
```vhdl
entity entity_name is
  port (
    input_port  : in  std_logic;
    output_port : out std_logic
  );
end entity;

architecture arch_name of entity_name is
begin
  -- concurrent statements
end architecture;
```

**Data Types:**
- `std_logic` -- Standard logic type (0, 1, Z, X, etc.). Used for single-bit signals.
- `std_logic_vector` -- Array of std_logic elements. Used for multi-bit buses.

**Basic Gates (Dataflow operators):**
- AND:  `y <= a AND b;`
- OR:   `y <= a OR b;`
- NOT:  `y <= NOT a;`

## Truth Table

**AND Gate:**
| a | b | y = a & b |
|---|---|-----------|
| 0 | 0 |     0     |
| 0 | 1 |     0     |
| 1 | 0 |     0     |
| 1 | 1 |     1     |

**OR Gate:**
| a | b | y = a | b |
|---|---|-----------|
| 0 | 0 |     0     |
| 0 | 1 |     1     |
| 1 | 0 |     1     |
| 1 | 1 |     1     |

**NOT Gate:**
| a | y = ~a |
|---|--------|
| 0 |   1    |
| 1 |   0    |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

-- AND gate entity
entity and_gate is
  port (
    a : in  std_logic;
    b : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of and_gate is
begin
  y <= a AND b;
end architecture;

-- OR gate entity
entity or_gate is
  port (
    a : in  std_logic;
    b : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of or_gate is
begin
  y <= a OR b;
end architecture;

-- NOT gate entity
entity not_gate is
  port (
    a : in  std_logic;
    y : out std_logic
  );
end entity;

architecture dataflow of not_gate is
begin
  y <= NOT a;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_gates is
end entity;

architecture sim of tb_gates is
  signal a, b     : std_logic;
  signal y_and,
         y_or,
         y_not    : std_logic;
begin
  -- Instantiate the gates
  u1: entity work.and_gate port map (a => a, b => b, y => y_and);
  u2: entity work.or_gate  port map (a => a, b => b, y => y_or);
  u3: entity work.not_gate port map (a => a,       y => y_not);

  process begin
    report "a b AND OR NOT(a)";

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
a=0 b=0  AND=0 OR=0 NOT(a)=1
a=0 b=1  AND=0 OR=1 NOT(a)=1
a=1 b=0  AND=0 OR=1 NOT(a)=0
a=1 b=1  AND=1 OR=1 NOT(a)=0
```

## Conclusion

Successfully implemented AND, OR, and NOT gates using dataflow modeling in VHDL. The simulation results match the expected truth tables, confirming correct functionality.
