# Implementing Multiplexer (MUX) and De Multiplexer with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 3  
**Date:** 27-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 4:1 multiplexer and 8:1 multiplexer using behavioral modeling.
- Design a 1:4 demultiplexer using behavioral modeling.
- Simulate and verify all circuits.

## Theory

**Multiplexer (MUX):**
A multiplexer selects one of many input signals and forwards it to a single output line based on select lines.
- 4:1 MUX: 4 data inputs, 2 select lines, 1 output
- 8:1 MUX: 8 data inputs, 3 select lines, 1 output

**Demultiplexer (DEMUX):**
A demultiplexer takes a single input and routes it to one of several output lines based on select lines.
- 1:4 DEMUX: 1 data input, 2 select lines, 4 outputs

## Truth Table

**4:1 MUX:**
| s1 | s0 |  y  |
|----|----|-----|
| 0  | 0  | i0  |
| 0  | 1  | i1  |
| 1  | 0  | i2  |
| 1  | 1  | i3  |

**8:1 MUX:**
| s2 | s1 | s0 |  y  |
|----|----|----|-----|
| 0  | 0  | 0  | i0  |
| 0  | 0  | 1  | i1  |
| 0  | 1  | 0  | i2  |
| 0  | 1  | 1  | i3  |
| 1  | 0  | 0  | i4  |
| 1  | 0  | 1  | i5  |
| 1  | 1  | 0  | i6  |
| 1  | 1  | 1  | i7  |

**1:4 DEMUX:**
| s1 | s0 | y3 | y2 | y1 | y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | d  |
| 0  | 1  | 0  | 0  | d  | 0  |
| 1  | 0  | 0  | d  | 0  | 0  |
| 1  | 1  | d  | 0  | 0  | 0  |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

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
      when "00" => y <= i(0);
      when "01" => y <= i(1);
      when "10" => y <= i(2);
      when "11" => y <= i(3);
      when others => y <= '0';
    end case;
  end process;
end architecture;

library ieee;
use ieee.std_logic_1164.all;

entity mux_8to1 is
  port (
    i   : in  std_logic_vector(7 downto 0);
    sel : in  std_logic_vector(2 downto 0);
    y   : out std_logic
  );
end entity;

architecture behavioral of mux_8to1 is
begin
  process (i, sel) begin
    case sel is
      when "000" => y <= i(0);
      when "001" => y <= i(1);
      when "010" => y <= i(2);
      when "011" => y <= i(3);
      when "100" => y <= i(4);
      when "101" => y <= i(5);
      when "110" => y <= i(6);
      when "111" => y <= i(7);
      when others => y <= '0';
    end case;
  end process;
end architecture;

library ieee;
use ieee.std_logic_1164.all;

entity demux_1to4 is
  port (
    d   : in  std_logic;
    sel : in  std_logic_vector(1 downto 0);
    y   : out std_logic_vector(3 downto 0)
  );
end entity;

architecture behavioral of demux_1to4 is
begin
  process (d, sel) begin
    y <= "0000";
    case sel is
      when "00" => y(0) <= d;
      when "01" => y(1) <= d;
      when "10" => y(2) <= d;
      when "11" => y(3) <= d;
      when others => null;
    end case;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_mux_demux is
end entity;

architecture sim of tb_mux_demux is
  signal i4   : std_logic_vector(3 downto 0);
  signal sel4 : std_logic_vector(1 downto 0);
  signal y4   : std_logic;

  signal i8   : std_logic_vector(7 downto 0);
  signal sel8 : std_logic_vector(2 downto 0);
  signal y8   : std_logic;

  signal d    : std_logic;
  signal sel_d : std_logic_vector(1 downto 0);
  signal y_d  : std_logic_vector(3 downto 0);
begin
  mux4: entity work.mux_4to1 port map (i => i4, sel => sel4, y => y4);
  mux8: entity work.mux_8to1 port map (i => i8, sel => sel8, y => y8);
  demux: entity work.demux_1to4 port map (d => d, sel => sel_d, y => y_d);

  process begin
    i4 <= "1010";
    sel4 <= "00"; wait for 10 ns;
    sel4 <= "01"; wait for 10 ns;
    sel4 <= "10"; wait for 10 ns;
    sel4 <= "11"; wait for 10 ns;

    i8 <= "10101010";
    sel8 <= "000"; wait for 10 ns;
    sel8 <= "001"; wait for 10 ns;
    sel8 <= "010"; wait for 10 ns;
    sel8 <= "011"; wait for 10 ns;
    sel8 <= "100"; wait for 10 ns;
    sel8 <= "101"; wait for 10 ns;
    sel8 <= "110"; wait for 10 ns;
    sel8 <= "111"; wait for 10 ns;

    d <= '1';
    sel_d <= "00"; wait for 10 ns;
    sel_d <= "01"; wait for 10 ns;
    sel_d <= "10"; wait for 10 ns;
    sel_d <= "11"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
=== 4:1 MUX ===
sel=00 i=1010 | y=0
sel=01 i=1010 | y=1
sel=10 i=1010 | y=0
sel=11 i=1010 | y=1
=== 8:1 MUX ===
sel=000 i=10101010 | y=0
sel=001 i=10101010 | y=1
sel=010 i=10101010 | y=0
sel=011 i=10101010 | y=1
sel=100 i=10101010 | y=0
sel=101 i=10101010 | y=1
sel=110 i=10101010 | y=0
sel=111 i=10101010 | y=1
=== 1:4 DEMUX ===
sel=00 d=1 | y=0001
sel=01 d=1 | y=0010
sel=10 d=1 | y=0100
sel=11 d=1 | y=1000
```

## Conclusion

Successfully implemented 4:1 MUX, 8:1 MUX, and 1:4 DEMUX using behavioral modeling. The MUX correctly selects inputs based on select lines, and the DEMUX routes the input to the correct output.
