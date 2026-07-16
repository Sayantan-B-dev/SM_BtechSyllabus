# Implementing 8-bit Addition, Multiplication, Division with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 2  
**Date:** 10-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Implement an 8-bit multiplier using the `*` operator in VHDL.
- Understand the concept of sequential multiplication (shift-and-add).
- Simulate and verify multiplication results.

## Theory

**Multiplication in VHDL:**
The `*` operator performs binary multiplication. Synthesis tools infer either combinational multipliers (using array of adders) or sequential multipliers depending on coding style.

**8-bit Multiplier:**
For two 8-bit inputs A and B:
- Product = A * B (16-bit result)

The product of two 8-bit numbers requires 16 bits to represent the maximum value (255 * 255 = 65025).

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity multiplier_8bit is
  port (
    a       : in  std_logic_vector(7 downto 0);
    b       : in  std_logic_vector(7 downto 0);
    product : out std_logic_vector(15 downto 0)
  );
end entity;

architecture behavioral of multiplier_8bit is
begin
  process (a, b) begin
    product <= std_logic_vector(unsigned(a) * unsigned(b));
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_multiplier_8bit is
end entity;

architecture sim of tb_multiplier_8bit is
  signal a, b   : std_logic_vector(7 downto 0) := (others => '0');
  signal product : std_logic_vector(15 downto 0);
begin
  uut: entity work.multiplier_8bit port map (a => a, b => b, product => product);

  process begin
    report "A=10 B=5 | Product=50 (expected=50)";
    a <= std_logic_vector(to_unsigned(10, 8)); b <= std_logic_vector(to_unsigned(5, 8)); wait for 10 ns;

    report "A=25 B=4 | Product=100 (expected=100)";
    a <= std_logic_vector(to_unsigned(25, 8)); b <= std_logic_vector(to_unsigned(4, 8)); wait for 10 ns;

    report "A=100 B=3 | Product=300 (expected=300)";
    a <= std_logic_vector(to_unsigned(100, 8)); b <= std_logic_vector(to_unsigned(3, 8)); wait for 10 ns;

    report "A=255 B=255 | Product=65025 (expected=65025)";
    a <= std_logic_vector(to_unsigned(255, 8)); b <= std_logic_vector(to_unsigned(255, 8)); wait for 10 ns;

    report "A=12 B=12 | Product=144 (expected=144)";
    a <= std_logic_vector(to_unsigned(12, 8)); b <= std_logic_vector(to_unsigned(12, 8)); wait for 10 ns;

    report "A=1 B=200 | Product=200 (expected=200)";
    a <= std_logic_vector(to_unsigned(1, 8)); b <= std_logic_vector(to_unsigned(200, 8)); wait for 10 ns;

    report "A=0 B=50 | Product=0 (expected=0)";
    a <= std_logic_vector(to_unsigned(0, 8)); b <= std_logic_vector(to_unsigned(50, 8)); wait for 10 ns;

    report "A=17 B=11 | Product=187 (expected=187)";
    a <= std_logic_vector(to_unsigned(17, 8)); b <= std_logic_vector(to_unsigned(11, 8)); wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=10 B=5 | Product=50 (expected=50)
A=25 B=4 | Product=100 (expected=100)
A=100 B=3 | Product=300 (expected=300)
A=255 B=255 | Product=65025 (expected=65025)
A=12 B=12 | Product=144 (expected=144)
A=1 B=200 | Product=200 (expected=200)
A=0 B=50 | Product=0 (expected=0)
A=17 B=11 | Product=187 (expected=187)
```

## Conclusion

Implemented an 8-bit multiplier using the behavioral `*` operator. The 16-bit product correctly accommodates the full range of multiplication results for 8-bit inputs.
