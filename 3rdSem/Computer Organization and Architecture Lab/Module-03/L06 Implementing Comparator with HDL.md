# Implementing Comparator with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 6  
**Date:** 03-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit comparator with an enable input using behavioral modeling.
- Use `if-else` statements for the comparator logic.
- Simulate with the enable signal disabled and enabled.

## Theory

**Comparator with Enable:**
An enable input (en) controls whether the comparator is active. When en = 0, the outputs are forced to a known state (all zero). When en = 1, normal comparison occurs.

**Behavioral Implementation:**
Using `always @(*)` with `if-else` statements makes the code easy to read and modify. The comparison can use either bit-wise logic or relational operators (`>`, `<`, `==`).

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity comp_8bit_en is
  port (
    en     : in  std_logic;
    a, b   : in  std_logic_vector(7 downto 0);
    a_gt_b : out std_logic;
    a_eq_b : out std_logic;
    a_lt_b : out std_logic
  );
end entity;

architecture behavioral of comp_8bit_en is
begin
  process (en, a, b) begin
    if en = '0' then
      a_gt_b <= '0';
      a_eq_b <= '0';
      a_lt_b <= '0';
    else
      if unsigned(a) > unsigned(b) then
        a_gt_b <= '1';
        a_eq_b <= '0';
        a_lt_b <= '0';
      elsif unsigned(a) = unsigned(b) then
        a_gt_b <= '0';
        a_eq_b <= '1';
        a_lt_b <= '0';
      else
        a_gt_b <= '0';
        a_eq_b <= '0';
        a_lt_b <= '1';
      end if;
    end if;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_comp_8bit_en is
end entity;

architecture sim of tb_comp_8bit_en is
  signal en     : std_logic;
  signal a, b   : std_logic_vector(7 downto 0);
  signal a_gt_b, a_eq_b, a_lt_b : std_logic;
begin
  uut: entity work.comp_8bit_en port map (en => en, a => a, b => b, a_gt_b => a_gt_b, a_eq_b => a_eq_b, a_lt_b => a_lt_b);

  process begin
    en <= '0';
    a <= "01100100"; b <= "00110010"; wait for 10 ns;
    a <= "00110010"; b <= "01100100"; wait for 10 ns;

    en <= '1';
    a <= "01100100"; b <= "00110010"; wait for 10 ns;
    a <= "00110010"; b <= "01100100"; wait for 10 ns;
    a <= "01001011"; b <= "01001011"; wait for 10 ns;
    a <= "11001000"; b <= "01100100"; wait for 10 ns;
    a <= "00000000"; b <= "11111111"; wait for 10 ns;

    en <= '0';
    a <= "11001000"; b <= "01100100"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
en=0 A=100 B=50 | A>B=0 A=B=0 A<B=0
en=0 A=50 B=100 | A>B=0 A=B=0 A<B=0
en=1 A=100 B=50 | A>B=1 A=B=0 A<B=0
en=1 A=50 B=100 | A>B=0 A=B=0 A<B=1
en=1 A=75 B=75 | A>B=0 A=B=1 A<B=0
en=1 A=200 B=100 | A>B=1 A=B=0 A<B=0
en=1 A=0 B=255 | A>B=0 A=B=0 A<B=1
en=0 A=200 B=100 | A>B=0 A=B=0 A<B=0
```

## Conclusion

Designed an 8-bit comparator with enable control using behavioral `if-else` statements. When enable is low, all outputs are zero. When enable is high, the comparator correctly identifies the relationship between the two 8-bit inputs.
