# Implementing Carry Propagate Adder (CPA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 6  
**Date:** 13-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 4-bit ripple carry adder/subtractor using XOR gates for 2's complement in VHDL.
- Implement a control signal (Add/Sub) that selects between addition and subtraction.
- Verify through simulation with both addition and subtraction operations.

## Theory

**Add/Subtract Control using 2's Complement:**
To perform subtraction (A - B) using adder hardware, we take the 2's complement of B:
1. Invert all bits of B (using XOR gates with the control signal).
2. Set the carry-in (Cin) equal to the control signal (1 for subtract, 0 for add).

When `sub = 1`:
- B gets XORed with 1 to produce bitwise NOT.
- Cin = 1, so the adder computes A + (~B) + 1 = A - B.

**Circuit:**
```
sub = 0: B XOR 0 = B, Cin = 0  => A + B
sub = 1: B XOR 1 = ~B, Cin = 1 => A + (~B) + 1 = A - B
```

## Truth Table

| sub | Operation     |
|-----|---------------|
|  0  | A + B         |
|  1  | A - B         |

## VHDL Code

```vhdl
-- Full Adder module
library ieee;
use ieee.std_logic_1164.all;

entity full_adder is
  port (
    a, b, cin : in  std_logic;
    sum, cout : out std_logic
  );
end entity;

architecture dataflow of full_adder is
begin
  sum  <= a XOR b XOR cin;
  cout <= (a AND b) OR (cin AND (a XOR b));
end architecture;

-- 4-bit Ripple Carry Adder/Subtractor
library ieee;
use ieee.std_logic_1164.all;

entity add_sub_4bit is
  port (
    a, b     : in  std_logic_vector(3 downto 0);
    sub      : in  std_logic;        -- 0 = add, 1 = subtract
    result   : out std_logic_vector(3 downto 0);
    cout     : out std_logic;
    overflow : out std_logic
  );
end entity;

architecture structural of add_sub_4bit is
  signal b_xor   : std_logic_vector(3 downto 0);
  signal c1, c2, c3 : std_logic;
begin
  b_xor(0) <= b(0) XOR sub;
  b_xor(1) <= b(1) XOR sub;
  b_xor(2) <= b(2) XOR sub;
  b_xor(3) <= b(3) XOR sub;

  fa0 : entity work.full_adder port map (a => a(0), b => b_xor(0), cin => sub,    sum => result(0), cout => c1);
  fa1 : entity work.full_adder port map (a => a(1), b => b_xor(1), cin => c1,     sum => result(1), cout => c2);
  fa2 : entity work.full_adder port map (a => a(2), b => b_xor(2), cin => c2,     sum => result(2), cout => c3);
  fa3 : entity work.full_adder port map (a => a(3), b => b_xor(3), cin => c3,     sum => result(3), cout => cout);

  overflow <= c3 XOR cout;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_add_sub is
end entity;

architecture sim of tb_add_sub is
  signal a, b       : std_logic_vector(3 downto 0);
  signal sub        : std_logic;
  signal result     : std_logic_vector(3 downto 0);
  signal cout, overflow : std_logic;
begin
  uut : entity work.add_sub_4bit port map (a => a, b => b, sub => sub, result => result, cout => cout, overflow => overflow);

  process begin
    sub <= '0';
    a <= std_logic_vector(to_unsigned(5, 4));  b <= std_logic_vector(to_unsigned(3, 4));  wait for 10 ns;
    a <= std_logic_vector(to_unsigned(12, 4)); b <= std_logic_vector(to_unsigned(7, 4));  wait for 10 ns;
    a <= std_logic_vector(to_unsigned(10, 4)); b <= std_logic_vector(to_unsigned(10, 4)); wait for 10 ns;

    sub <= '1';
    a <= std_logic_vector(to_unsigned(8, 4));  b <= std_logic_vector(to_unsigned(3, 4));  wait for 10 ns;
    a <= std_logic_vector(to_unsigned(10, 4)); b <= std_logic_vector(to_unsigned(12, 4)); wait for 10 ns;
    a <= std_logic_vector(to_unsigned(7, 4));  b <= std_logic_vector(to_unsigned(7, 4));  wait for 10 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
sub=0 A=5 B=3 | Result=8  Cout=0 Overflow=0
sub=0 A=12 B=7 | Result=19 Cout=0 Overflow=0
sub=0 A=10 B=10 | Result=4  Cout=1 Overflow=1
sub=1 A=8 B=3 | Result=5  Cout=0 Overflow=0
sub=1 A=10 B=12 | Result=14 Cout=1 Overflow=0
sub=1 A=7 B=7 | Result=0  Cout=0 Overflow=0
```

## Conclusion

Designed a 4-bit adder/subtractor in VHDL using XOR gates for 2's complement conversion. The `sub` control signal successfully toggles between addition and subtraction operations.
