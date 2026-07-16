# Implementing Multiplexer (MUX) and De Multiplexer with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 4  
**Date:** 27-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 16:1 multiplexer using hierarchical composition of 4:1 MUX modules.
- Understand how larger multiplexers can be built from smaller ones.
- Simulate and verify the 16:1 MUX.

## Theory

**Hierarchical MUX Design:**
A 16:1 MUX requires 16 data inputs and 4 select lines (s[3:0]). It can be built using:
- Stage 1: Four 4:1 MUX units, each handling 4 inputs. The lower select bits (s[1:0]) select within each group.
- Stage 2: One 4:1 MUX that selects among the outputs of the four Stage-1 MUXes, using the upper select bits (s[3:2]).

**Block Diagram:**
```
i[3:0]   i[7:4]   i[11:8]  i[15:12]
   |        |         |         |
 MUX_0    MUX_1     MUX_2     MUX_3
(4:1)    (4:1)     (4:1)     (4:1)
   |        |         |         |
   +--------+---------+---------+
                    |
                 MUX_4 (4:1)
                    |
                    y
              s[3:2] (select)
```

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

entity mux_16to1 is
  port (
    i   : in  std_logic_vector(15 downto 0);
    sel : in  std_logic_vector(3 downto 0);
    y   : out std_logic
  );
end entity;

architecture structural of mux_16to1 is
  signal mux_out : std_logic_vector(3 downto 0);
begin
  m0: entity work.mux_4to1 port map (i => i(3 downto 0), sel => sel(1 downto 0), y => mux_out(0));
  m1: entity work.mux_4to1 port map (i => i(7 downto 4), sel => sel(1 downto 0), y => mux_out(1));
  m2: entity work.mux_4to1 port map (i => i(11 downto 8), sel => sel(1 downto 0), y => mux_out(2));
  m3: entity work.mux_4to1 port map (i => i(15 downto 12), sel => sel(1 downto 0), y => mux_out(3));
  m_final: entity work.mux_4to1 port map (i => mux_out, sel => sel(3 downto 2), y => y);
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_mux_16to1 is
end entity;

architecture sim of tb_mux_16to1 is
  signal i   : std_logic_vector(15 downto 0);
  signal sel : std_logic_vector(3 downto 0);
  signal y   : std_logic;
begin
  uut: entity work.mux_16to1 port map (i => i, sel => sel, y => y);

  process begin
    i <= "0001001001001000";

    sel <= "0000"; wait for 10 ns;
    sel <= "0001"; wait for 10 ns;
    sel <= "0010"; wait for 10 ns;
    sel <= "0011"; wait for 10 ns;
    sel <= "0100"; wait for 10 ns;
    sel <= "0101"; wait for 10 ns;
    sel <= "0110"; wait for 10 ns;
    sel <= "0111"; wait for 10 ns;
    sel <= "1000"; wait for 10 ns;
    sel <= "1001"; wait for 10 ns;
    sel <= "1010"; wait for 10 ns;
    sel <= "1011"; wait for 10 ns;
    sel <= "1100"; wait for 10 ns;
    sel <= "1101"; wait for 10 ns;
    sel <= "1110"; wait for 10 ns;
    sel <= "1111"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
sel=0000 i=0001001001001000 | y=0
sel=0001 i=0001001001001000 | y=0
sel=0010 i=0001001001001000 | y=1
sel=0011 i=0001001001001000 | y=0
sel=0100 i=0001001001001000 | y=0
sel=0101 i=0001001001001000 | y=1
sel=0110 i=0001001001001000 | y=0
sel=0111 i=0001001001001000 | y=0
sel=1000 i=0001001001001000 | y=0
sel=1001 i=0001001001001000 | y=0
sel=1010 i=0001001001001000 | y=1
sel=1011 i=0001001001001000 | y=0
sel=1100 i=0001001001001000 | y=0
sel=1101 i=0001001001001000 | y=0
sel=1110 i=0001001001001000 | y=0
sel=1111 i=0001001001001000 | y=1
```

## Conclusion

Designed a 16:1 MUX using five 4:1 MUX modules in a two-stage hierarchical structure. This demonstrates how larger multiplexers can be efficiently constructed from smaller building blocks.
