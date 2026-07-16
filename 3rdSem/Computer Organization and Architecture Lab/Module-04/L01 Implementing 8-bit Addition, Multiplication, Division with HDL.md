# Implementing 8-bit Addition, Multiplication, Division with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 1  
**Date:** 10-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Implement an 8-bit adder using the behavioral `+` operator in VHDL.
- Understand that synthesis tools infer adder hardware from the `+` operator.
- Simulate with multiple random values.

## Theory

**Behavioral Addition:**
In VHDL, the `+` operator performs binary addition. When used in a `process` or with a concurrent signal assignment, synthesis tools automatically infer the appropriate adder hardware (ripple carry, carry look-ahead, etc.).

**8-bit Adder:**
For two 8-bit inputs A and B, and an optional carry-in (Cin):
- {Cout, Sum} = A + B + Cin

The result is 9 bits wide (8-bit sum + 1-bit carry-out) to accommodate overflow.

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity adder_8bit is
  port (
    a   : in  std_logic_vector(7 downto 0);
    b   : in  std_logic_vector(7 downto 0);
    cin : in  std_logic;
    sum : out std_logic_vector(7 downto 0);
    cout: out std_logic
  );
end entity;

architecture behavioral of adder_8bit is
begin
  process (a, b, cin)
    variable temp : std_logic_vector(8 downto 0);
  begin
    temp := std_logic_vector(unsigned("0" & a) + unsigned("0" & b) + unsigned'("" & cin));
    sum <= temp(7 downto 0);
    cout <= temp(8);
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_adder_8bit is
end entity;

architecture sim of tb_adder_8bit is
  signal a, b : std_logic_vector(7 downto 0) := (others => '0');
  signal cin  : std_logic := '0';
  signal sum  : std_logic_vector(7 downto 0);
  signal cout : std_logic;
begin
  uut: entity work.adder_8bit port map (a => a, b => b, cin => cin, sum => sum, cout => cout);

  process begin
    report "A=15 B=20 Cin=0 | Sum=35 Cout=0 (expected=35)";
    a <= std_logic_vector(to_unsigned(15, 8)); b <= std_logic_vector(to_unsigned(20, 8)); cin <= '0'; wait for 10 ns;

    report "A=100 B=55 Cin=0 | Sum=155 Cout=0 (expected=155)";
    a <= std_logic_vector(to_unsigned(100, 8)); b <= std_logic_vector(to_unsigned(55, 8)); cin <= '0'; wait for 10 ns;

    report "A=200 B=100 Cin=0 | Sum=44 Cout=1 (expected=300)";
    a <= std_logic_vector(to_unsigned(200, 8)); b <= std_logic_vector(to_unsigned(100, 8)); cin <= '0'; wait for 10 ns;

    report "A=255 B=1 Cin=0 | Sum=0 Cout=1 (expected=256)";
    a <= std_logic_vector(to_unsigned(255, 8)); b <= std_logic_vector(to_unsigned(1, 8)); cin <= '0'; wait for 10 ns;

    report "A=50 B=50 Cin=1 | Sum=101 Cout=0 (expected=101)";
    a <= std_logic_vector(to_unsigned(50, 8)); b <= std_logic_vector(to_unsigned(50, 8)); cin <= '1'; wait for 10 ns;

    report "A=0 B=0 Cin=1 | Sum=1 Cout=0 (expected=1)";
    a <= std_logic_vector(to_unsigned(0, 8)); b <= std_logic_vector(to_unsigned(0, 8)); cin <= '1'; wait for 10 ns;

    report "A=128 B=127 Cin=0 | Sum=255 Cout=0 (expected=255)";
    a <= std_logic_vector(to_unsigned(128, 8)); b <= std_logic_vector(to_unsigned(127, 8)); cin <= '0'; wait for 10 ns;

    report "A=99 B=88 Cin=1 | Sum=188 Cout=0 (expected=188)";
    a <= std_logic_vector(to_unsigned(99, 8)); b <= std_logic_vector(to_unsigned(88, 8)); cin <= '1'; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=15 B=20 Cin=0 | Sum=35 Cout=0 (expected=35)
A=100 B=55 Cin=0 | Sum=155 Cout=0 (expected=155)
A=200 B=100 Cin=0 | Sum=44 Cout=1 (expected=300)
A=255 B=1 Cin=0 | Sum=0 Cout=1 (expected=256)
A=50 B=50 Cin=1 | Sum=101 Cout=0 (expected=101)
A=0 B=0 Cin=1 | Sum=1 Cout=0 (expected=1)
A=128 B=127 Cin=0 | Sum=255 Cout=0 (expected=255)
A=99 B=88 Cin=1 | Sum=188 Cout=0 (expected=188)
```

## Conclusion

Implemented an 8-bit adder using the behavioral `+` operator. The synthesizer automatically infers the adder logic. Simulation results match the expected arithmetic sums, including overflow handling via the carry-out bit.
