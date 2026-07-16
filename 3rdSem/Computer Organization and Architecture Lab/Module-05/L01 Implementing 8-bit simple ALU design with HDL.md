# Implementing 8-bit simple ALU design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 1  
**Date:** 01-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit ALU (Arithmetic Logic Unit) supporting multiple operations via select lines.
- Implement add, subtract, AND, OR, XOR, NOT, shift left, and shift right operations.
- Simulate and verify all ALU operations.

## Theory

**ALU (Arithmetic Logic Unit):**
The ALU is the core computational unit of a CPU. It performs arithmetic and logic operations on input data based on a set of select/control lines.

**8-bit ALU with 3 select lines (8 operations):**
| Sel[2:0] | Operation     | Description         |
|----------|---------------|---------------------|
| 000      | A + B         | Addition            |
| 001      | A - B         | Subtraction         |
| 010      | A & B         | Bitwise AND         |
| 011      | A | B         | Bitwise OR          |
| 100      | A ^ B         | Bitwise XOR         |
| 101      | ~A            | Bitwise NOT (A)     |
| 110      | A << 1        | Left shift by 1     |
| 111      | A >> 1        | Right shift by 1    |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_8bit is
  port (
    a, b   : in  std_logic_vector(7 downto 0);
    sel    : in  std_logic_vector(2 downto 0);
    result : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of alu_8bit is
begin
  process (a, b, sel) begin
    case sel is
      when "000" => result <= std_logic_vector(unsigned(a) + unsigned(b));
      when "001" => result <= std_logic_vector(unsigned(a) - unsigned(b));
      when "010" => result <= a AND b;
      when "011" => result <= a OR b;
      when "100" => result <= a XOR b;
      when "101" => result <= NOT a;
      when "110" => result <= std_logic_vector(unsigned(a) sll 1);
      when "111" => result <= std_logic_vector(unsigned(a) srl 1);
      when others => result <= (others => '0');
    end case;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_alu_8bit is
end entity;

architecture sim of tb_alu_8bit is
  signal a, b   : std_logic_vector(7 downto 0) := (others => '0');
  signal sel    : std_logic_vector(2 downto 0) := (others => '0');
  signal result : std_logic_vector(7 downto 0);
begin
  uut: entity work.alu_8bit
    port map (a => a, b => b, sel => sel, result => result);

  process begin
    a <= std_logic_vector(to_unsigned(20, 8));
    b <= std_logic_vector(to_unsigned(10, 8));
    sel <= "000"; wait for 10 ns;
    sel <= "001"; wait for 10 ns;
    sel <= "010"; wait for 10 ns;
    sel <= "011"; wait for 10 ns;
    sel <= "100"; wait for 10 ns;
    sel <= "101"; wait for 10 ns;
    sel <= "110"; wait for 10 ns;
    sel <= "111"; wait for 10 ns;

    a <= std_logic_vector(to_unsigned(240, 8));
    b <= std_logic_vector(to_unsigned(15, 8));
    sel <= "000"; wait for 10 ns;
    sel <= "010"; wait for 10 ns;
    sel <= "110"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=20 B=10 sel=000 | result=30
A=20 B=10 sel=001 | result=10
A=20 B=10 sel=010 | result=0
A=20 B=10 sel=011 | result=30
A=20 B=10 sel=100 | result=30
A=20 B=10 sel=101 | result=235
A=20 B=10 sel=110 | result=40
A=20 B=10 sel=111 | result=10
A=240 B=15 sel=000 | result=255
A=240 B=15 sel=010 | result=0
A=240 B=15 sel=110 | result=224
```

## Conclusion

Designed an 8-bit ALU supporting 8 operations including addition, subtraction, bitwise operations, and shifts. The `case` statement selects the appropriate operation based on the 3-bit select signal.
