# Implementing Full Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 3  
**Date:** 06-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a full adder using structural and behavioral modeling in VHDL.
- Derive and verify the logical expressions for Sum and Carry-out.
- Test exhaustively for all 8 input combinations.

## Theory

**Full Adder:**
A full adder adds three single-bit inputs: A, B, and Carry-in (Cin). It produces:
- Sum = A xor B xor Cin
- Cout = (A & B) | (Cin & (A xor B))

**Behavioral Modeling:**
Using `process` with `case` or `if-else` to describe the circuit functionally.

**Structural Modeling:**
Building the full adder using two half adders and an OR gate (as in Module-1, Lab 4).

## Truth Table

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0  |
| 0 | 0 |  1  |  1  |  0  |
| 0 | 1 |  0  |  1  |  0  |
| 0 | 1 |  1  |  0  |  1  |
| 1 | 0 |  0  |  1  |  0  |
| 1 | 0 |  1  |  0  |  1  |
| 1 | 1 |  0  |  0  |  1  |
| 1 | 1 |  1  |  1  |  1  |

## VHDL Code

```vhdl
-- Full Adder -- Behavioral using process
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity full_adder_beh is
  port (
    a, b, cin : in  std_logic;
    sum, cout : out std_logic
  );
end entity;

architecture behavioral of full_adder_beh is
begin
  process (a, b, cin) begin
    cout <= (a AND b) OR (cin AND (a XOR b));
    sum  <= a XOR b XOR cin;
  end process;
end architecture;

-- Full Adder -- Structural using concurrent assignments
library ieee;
use ieee.std_logic_1164.all;

entity full_adder_str is
  port (
    a, b, cin : in  std_logic;
    sum, cout : out std_logic
  );
end entity;

architecture structural of full_adder_str is
  signal s1, c1, c2 : std_logic;
begin
  s1   <= a XOR b;
  sum  <= s1 XOR cin;
  c1   <= a AND b;
  c2   <= s1 AND cin;
  cout <= c1 OR c2;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_full_adder is
end entity;

architecture sim of tb_full_adder is
  signal a, b, cin             : std_logic;
  signal sum_beh, cout_beh     : std_logic;
  signal sum_str, cout_str     : std_logic;
begin
  uut_beh : entity work.full_adder_beh port map (a => a, b => b, cin => cin, sum => sum_beh, cout => cout_beh);
  uut_str : entity work.full_adder_str port map (a => a, b => b, cin => cin, sum => sum_str, cout => cout_str);

  process begin
    (a, b, cin) <= std_logic_vector'("000"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("001"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("010"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("011"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("100"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("101"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("110"); wait for 10 ns;
    (a, b, cin) <= std_logic_vector'("111"); wait for 10 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=0 B=0 Cin=0 | Sum_beh=0 Cout_beh=0 | Sum_str=0 Cout_str=0
A=0 B=0 Cin=1 | Sum_beh=1 Cout_beh=0 | Sum_str=1 Cout_str=0
A=0 B=1 Cin=0 | Sum_beh=1 Cout_beh=0 | Sum_str=1 Cout_str=0
A=0 B=1 Cin=1 | Sum_beh=0 Cout_beh=1 | Sum_str=0 Cout_str=1
A=1 B=0 Cin=0 | Sum_beh=1 Cout_beh=0 | Sum_str=1 Cout_str=0
A=1 B=0 Cin=1 | Sum_beh=0 Cout_beh=1 | Sum_str=0 Cout_str=1
A=1 B=1 Cin=0 | Sum_beh=0 Cout_beh=1 | Sum_str=0 Cout_str=1
A=1 B=1 Cin=1 | Sum_beh=1 Cout_beh=1 | Sum_str=1 Cout_str=1
```

## Conclusion

Designed a full adder using both behavioral and structural modeling in VHDL. Both approaches produce identical results matching the full adder truth table.
