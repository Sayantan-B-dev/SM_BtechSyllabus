# Implementing Carry Look-Ahead Adder (CLA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 2  
**Date:** 20-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit CLA using two 4-bit CLA blocks in hierarchical fashion.
- Understand hierarchical design methodology for scalable adders.
- Simulate and verify the 8-bit CLA.

## Theory

**Hierarchical CLA Design:**
An 8-bit CLA can be constructed by cascading two 4-bit CLA blocks. The carry-out from the lower 4-bit CLA becomes the carry-in for the upper 4-bit CLA.

**Group Generate and Propagate:**
For hierarchical CLA, we compute group-level generate (GG) and propagate (GP) signals:
- GGrp = G3 | (P3 & G2) | (P3 & P2 & G1) | (P3 & P2 & P1 & G0)
- PGrp = P3 & P2 & P1 & P0

These allow building wider adders without sacrificing the look-ahead benefit across groups.

## Block Diagram

```
A[7:4] B[7:4]              A[3:0] B[3:0]
   |      |                    |      |
   +------+                    +------+
   |      |                    |      |
  CLA_High                  CLA_Low
   (4-bit)                   (4-bit)
   |      |                    |      |
   +------+------+------+------+------+
                  |             |
                Sum[7:4]     Sum[3:0]
                  |             |
              Cout <--- c3[high]   c3[low] ----> Cin
```

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity cla_4bit is
  port (
    a, b : in  std_logic_vector(3 downto 0);
    cin  : in  std_logic;
    sum  : out std_logic_vector(3 downto 0);
    cout : out std_logic;
    gg   : out std_logic;
    pg   : out std_logic
  );
end entity;

architecture behavioral of cla_4bit is
  signal g, p, c : std_logic_vector(3 downto 0);
begin
  g <= a and b;
  p <= a xor b;

  c(0) <= cin;
  c(1) <= g(0) or (p(0) and cin);
  c(2) <= g(1) or (p(1) and g(0)) or (p(1) and p(0) and cin);
  c(3) <= g(2) or (p(2) and g(1)) or (p(2) and p(1) and g(0)) or (p(2) and p(1) and p(0) and cin);
  cout <= g(3) or (p(3) and g(2)) or (p(3) and p(2) and g(1)) or (p(3) and p(2) and p(1) and g(0)) or
          (p(3) and p(2) and p(1) and p(0) and cin);

  sum <= p xor (c(2 downto 0) & cin);

  gg <= g(3) or (p(3) and g(2)) or (p(3) and p(2) and g(1)) or (p(3) and p(2) and p(1) and g(0));
  pg <= p(3) and p(2) and p(1) and p(0);
end architecture;

library ieee;
use ieee.std_logic_1164.all;

entity cla_8bit is
  port (
    a, b : in  std_logic_vector(7 downto 0);
    cin  : in  std_logic;
    sum  : out std_logic_vector(7 downto 0);
    cout : out std_logic
  );
end entity;

architecture structural of cla_8bit is
  signal c4 : std_logic;
begin
  low: entity work.cla_4bit port map (a => a(3 downto 0), b => b(3 downto 0), cin => cin, sum => sum(3 downto 0), cout => c4);
  high: entity work.cla_4bit port map (a => a(7 downto 4), b => b(7 downto 4), cin => c4, sum => sum(7 downto 4), cout => cout);
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_cla_8bit is
end entity;

architecture sim of tb_cla_8bit is
  signal a, b : std_logic_vector(7 downto 0);
  signal cin  : std_logic;
  signal sum  : std_logic_vector(7 downto 0);
  signal cout : std_logic;
begin
  uut: entity work.cla_8bit port map (a => a, b => b, cin => cin, sum => sum, cout => cout);

  process begin
    a <= "00001111"; b <= "00010100"; cin <= '0'; wait for 10 ns;
    a <= "01100100"; b <= "00110111"; cin <= '0'; wait for 10 ns;
    a <= "11001000"; b <= "01100100"; cin <= '0'; wait for 10 ns;
    a <= "11111111"; b <= "00000001"; cin <= '0'; wait for 10 ns;
    a <= "00110010"; b <= "00110010"; cin <= '1'; wait for 10 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=15 B=20 Cin=0 | Sum=35 Cout=0
A=100 B=55 Cin=0 | Sum=155 Cout=0
A=200 B=100 Cin=0 | Sum=44 Cout=1
A=255 B=1 Cin=0 | Sum=0 Cout=1
A=50 B=50 Cin=1 | Sum=101 Cout=0
```

## Conclusion

Designed an 8-bit CLA by hierarchically connecting two 4-bit CLA blocks. The hierarchical approach allows scalable adder designs while maintaining the speed advantage of carry look-ahead.
