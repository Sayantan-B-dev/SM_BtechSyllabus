# Basic digital logic base programming with HDL through Behavioural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 5  
**Date:** 23-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Understand behavioral modeling in VHDL using the `process` block.
- Use `if-then-else` and `case` statements for decision-based hardware description.
- Design and simulate a 4:1 multiplexer using behavioral modeling.

## Theory

**Behavioral Modeling:**
Behavioral modeling describes a circuit's functionality at a high level of abstraction, without explicitly specifying gate-level interconnections. It uses constructs like `process`, `if-then-else`, `case`, and `for` loops.

**Process block:**
```vhdl
process (sensitivity_list) begin
    -- sequential or combinational logic
end process;
```
For combinational logic, all input signals are listed in the sensitivity list.

**4:1 Multiplexer:**
A multiplexer selects one of several input signals and forwards it to the output. A 4:1 MUX has 4 data inputs (i0, i1, i2, i3), 2 select lines (s1, s0), and 1 output (y).

## Truth Table

| s1 | s0 |  y   |
|----|----|------|
| 0  | 0  |  i0  |
| 0  | 1  |  i1  |
| 1  | 0  |  i2  |
| 1  | 1  |  i3  |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

-- 4:1 Multiplexer using behavioral modeling (case statement)
entity mux_4to1 is
  port (
    i   : in  std_logic_vector(3 downto 0);
    sel : in  std_logic_vector(1 downto 0);
    y   : out std_logic
  );
end entity;

architecture behavioral of mux_4to1 is
begin
  process (i, sel) begin
    case sel is
      when "00"   => y <= i(0);
      when "01"   => y <= i(1);
      when "10"   => y <= i(2);
      when "11"   => y <= i(3);
      when others => y <= '0';
    end case;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_mux_4to1 is
end entity;

architecture sim of tb_mux_4to1 is
  signal i   : std_logic_vector(3 downto 0);
  signal sel : std_logic_vector(1 downto 0);
  signal y   : std_logic;
begin
  uut: entity work.mux_4to1 port map (i => i, sel => sel, y => y);

  process begin
    report "sel i y";

    -- Set inputs to known pattern
    i <= "1010";

    sel <= "00"; wait for 10 ns;
    sel <= "01"; wait for 10 ns;
    sel <= "10"; wait for 10 ns;
    sel <= "11"; wait for 10 ns;

    -- Try another pattern
    i <= "0110";
    sel <= "00"; wait for 10 ns;
    sel <= "01"; wait for 10 ns;
    sel <= "10"; wait for 10 ns;
    sel <= "11"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
sel=00 i=1010 | y=0
sel=01 i=1010 | y=1
sel=10 i=1010 | y=0
sel=11 i=1010 | y=1
sel=00 i=0110 | y=0
sel=01 i=0110 | y=1
sel=10 i=0110 | y=1
sel=11 i=0110 | y=0
```

## Conclusion

Designed a 4:1 multiplexer using behavioral modeling in VHDL with the `case` statement. The simulation confirms that the correct input is routed to the output based on the select line combination.
