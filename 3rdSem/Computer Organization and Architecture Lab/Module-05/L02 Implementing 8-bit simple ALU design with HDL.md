# Implementing 8-bit simple ALU design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 2  
**Date:** 01-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Enhance the 8-bit ALU with status flags: zero, carry, overflow, and negative.
- Understand how flags are used for conditional operations in CPUs.
- Simulate and verify flag generation for various operations.

## Theory

**ALU Status Flags:**
- **Zero (Z):** Set to 1 when the result is all zeros.
- **Carry (C):** Set to 1 when the operation produces a carry-out (for addition) or borrow (for subtraction).
- **Overflow (V):** Set to 1 when signed overflow occurs (result exceeds the signed 8-bit range -128 to 127).
- **Negative (N):** Set to 1 when the MSB of the result is 1 (result is negative in signed interpretation).

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_8bit_flags is
  port (
    a, b     : in  std_logic_vector(7 downto 0);
    sel      : in  std_logic_vector(2 downto 0);
    result   : out std_logic_vector(7 downto 0);
    zero     : out std_logic;
    carry    : out std_logic;
    overflow : out std_logic;
    negative : out std_logic
  );
end entity;

architecture behavioral of alu_8bit_flags is
  signal add_result : std_logic_vector(8 downto 0);
  signal sub_result : std_logic_vector(8 downto 0);
  signal res_int    : std_logic_vector(7 downto 0);
begin
  add_result <= std_logic_vector(unsigned("0" & a) + unsigned("0" & b));
  sub_result <= std_logic_vector(unsigned("0" & a) - unsigned("0" & b));

  process (a, b, sel, add_result, sub_result) begin
    zero <= '0'; carry <= '0'; overflow <= '0'; negative <= '0';
    res_int <= (others => '0');

    case sel is
      when "000" =>
        res_int <= add_result(7 downto 0);
        carry <= add_result(8);
        overflow <= (a(7) XNOR b(7)) AND (a(7) XOR add_result(7));
      when "001" =>
        res_int <= sub_result(7 downto 0);
        carry <= sub_result(8);
        overflow <= (a(7) XNOR b(7)) AND (a(7) XOR sub_result(7));
      when "010" => res_int <= a AND b;
      when "011" => res_int <= a OR b;
      when "100" => res_int <= a XOR b;
      when "101" => res_int <= NOT a;
      when "110" =>
        res_int <= std_logic_vector(unsigned(a) sll 1);
        carry <= a(7);
      when "111" =>
        res_int <= std_logic_vector(unsigned(a) srl 1);
        carry <= a(0);
      when others => res_int <= (others => '0');
    end case;

    result <= res_int;
    negative <= res_int(7);
    if res_int = "00000000" then
      zero <= '1';
    end if;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_alu_flags is
end entity;

architecture sim of tb_alu_flags is
  signal a, b     : std_logic_vector(7 downto 0) := (others => '0');
  signal sel      : std_logic_vector(2 downto 0) := (others => '0');
  signal result   : std_logic_vector(7 downto 0);
  signal zero, carry, overflow, negative : std_logic;
begin
  uut: entity work.alu_8bit_flags
    port map (a => a, b => b, sel => sel, result => result,
              zero => zero, carry => carry, overflow => overflow,
              negative => negative);

  process begin
    a <= std_logic_vector(to_unsigned(50, 8));
    b <= std_logic_vector(to_unsigned(50, 8));
    sel <= "000"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(200, 8));
    b <= std_logic_vector(to_unsigned(100, 8));
    sel <= "000"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(100, 8));
    b <= std_logic_vector(to_unsigned(100, 8));
    sel <= "001"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(50, 8));
    b <= std_logic_vector(to_unsigned(100, 8));
    sel <= "001"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(255, 8));
    b <= std_logic_vector(to_unsigned(0, 8));
    sel <= "010"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(128, 8));
    b <= std_logic_vector(to_unsigned(0, 8));
    sel <= "110"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(127, 8));
    b <= std_logic_vector(to_unsigned(1, 8));
    sel <= "000"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=50 B=50 sel=000 | result=100 Z=0 C=0 V=0 N=0
A=200 B=100 sel=000 | result=44 Z=0 C=1 V=1 N=0
A=100 B=100 sel=001 | result=0 Z=1 C=0 V=0 N=0
A=50 B=100 sel=001 | result=206 Z=0 C=1 V=0 N=1
A=255 B=0 sel=010 | result=0 Z=1 C=0 V=0 N=0
A=128 B=0 sel=110 | result=0 Z=1 C=1 V=0 N=0
A=127 B=1 sel=000 | result=128 Z=0 C=0 V=1 N=1
```

## Conclusion

Enhanced the 8-bit ALU with zero, carry, overflow, and negative status flags. These flags provide essential status information for conditional branching and program flow control in CPU design.
