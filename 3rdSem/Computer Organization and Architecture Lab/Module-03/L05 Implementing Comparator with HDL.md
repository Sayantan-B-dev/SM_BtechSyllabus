# Implementing Comparator with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 5  
**Date:** 03-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 1-bit comparator with three outputs: A > B, A = B, A < B.
- Design a 4-bit comparator using hierarchical design.
- Simulate and verify the comparator functionality.

## Theory

**Comparator:**
A digital comparator compares two binary numbers and produces outputs indicating their relative magnitude.

**1-bit Comparator:**
For two single-bit inputs A and B:
- A_gt_B = A & ~B
- A_eq_B = ~(A ^ B) = A xnor B
- A_lt_B = ~A & B

**4-bit Comparator (Hierarchical):**
A 4-bit comparator compares two 4-bit numbers A[3:0] and B[3:0]. The comparison starts from the most significant bit (MSB). If the MSBs differ, the result is determined immediately. If they are equal, the next lower bits are compared.

## Truth Table (1-bit)

| A | B | A>B | A=B | A<B |
|---|---|-----|-----|-----|
| 0 | 0 |  0  |  1  |  0  |
| 0 | 1 |  0  |  0  |  1  |
| 1 | 0 |  1  |  0  |  0  |
| 1 | 1 |  0  |  1  |  0  |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity comp_1bit is
  port (
    a, b   : in  std_logic;
    a_gt_b : out std_logic;
    a_eq_b : out std_logic;
    a_lt_b : out std_logic
  );
end entity;

architecture behavioral of comp_1bit is
begin
  a_gt_b <= a and not b;
  a_eq_b <= not (a xor b);
  a_lt_b <= not a and b;
end architecture;

library ieee;
use ieee.std_logic_1164.all;

entity comp_4bit is
  port (
    a, b   : in  std_logic_vector(3 downto 0);
    a_gt_b : out std_logic;
    a_eq_b : out std_logic;
    a_lt_b : out std_logic
  );
end entity;

architecture structural of comp_4bit is
  signal gt, eq, lt : std_logic_vector(3 downto 0);
begin
  c0: entity work.comp_1bit port map (a => a(0), b => b(0), a_gt_b => gt(0), a_eq_b => eq(0), a_lt_b => lt(0));
  c1: entity work.comp_1bit port map (a => a(1), b => b(1), a_gt_b => gt(1), a_eq_b => eq(1), a_lt_b => lt(1));
  c2: entity work.comp_1bit port map (a => a(2), b => b(2), a_gt_b => gt(2), a_eq_b => eq(2), a_lt_b => lt(2));
  c3: entity work.comp_1bit port map (a => a(3), b => b(3), a_gt_b => gt(3), a_eq_b => eq(3), a_lt_b => lt(3));

  a_gt_b <= gt(3) or (eq(3) and gt(2)) or (eq(3) and eq(2) and gt(1)) or (eq(3) and eq(2) and eq(1) and gt(0));
  a_lt_b <= lt(3) or (eq(3) and lt(2)) or (eq(3) and eq(2) and lt(1)) or (eq(3) and eq(2) and eq(1) and lt(0));
  a_eq_b <= eq(3) and eq(2) and eq(1) and eq(0);
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_comp_4bit is
end entity;

architecture sim of tb_comp_4bit is
  signal a, b   : std_logic_vector(3 downto 0);
  signal a_gt_b, a_eq_b, a_lt_b : std_logic;
begin
  uut: entity work.comp_4bit port map (a => a, b => b, a_gt_b => a_gt_b, a_eq_b => a_eq_b, a_lt_b => a_lt_b);

  process begin
    a <= "1010"; b <= "0101"; wait for 10 ns;
    a <= "0101"; b <= "1010"; wait for 10 ns;
    a <= "0111"; b <= "0111"; wait for 10 ns;
    a <= "1111"; b <= "0000"; wait for 10 ns;
    a <= "0000"; b <= "1111"; wait for 10 ns;
    a <= "1000"; b <= "1001"; wait for 10 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=10 B=5 | A>B=1 A=B=0 A<B=0
A=5 B=10 | A>B=0 A=B=0 A<B=1
A=7 B=7 | A>B=0 A=B=1 A<B=0
A=15 B=0 | A>B=1 A=B=0 A<B=0
A=0 B=15 | A>B=0 A=B=0 A<B=1
A=8 B=9 | A>B=0 A=B=0 A<B=1
```

## Conclusion

Designed a 1-bit comparator and extended it to a 4-bit comparator using hierarchical design. The comparator correctly determines the relationship between two 4-bit numbers by checking bits from MSB to LSB.
