# Implementing Carry Look-Ahead Adder (CLA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 1  
**Date:** 20-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Understand the theory of Carry Look-Ahead Adder (CLA) -- generate (G) and propagate (P) signals.
- Design a 4-bit CLA in VHDL.
- Compare CLA performance with ripple carry adder.

## Theory

**Carry Look-Ahead Adder (CLA):**
The CLA reduces propagation delay by computing the carry signals in parallel using generate (G) and propagate (P) signals.

For each bit position i:
- Generate:  Gi = Ai & Bi  (carry is generated when both inputs are 1)
- Propagate: Pi = Ai ^ Bi  (carry propagates when exactly one input is 1)

The carry signals are computed as:
- C0 = Cin
- C1 = G0 | (P0 & Cin)
- C2 = G1 | (P1 & G0) | (P1 & P0 & Cin)
- C3 = G2 | (P2 & G1) | (P2 & P1 & G0) | (P2 & P1 & P0 & Cin)
- C4 = G3 | (P3 & G2) | (P3 & P2 & G1) | (P3 & P2 & P1 & G0) | (P3 & P2 & P1 & P0 & Cin)

Sum = Pi ^ Ci-1 (for each bit)

## Block Diagram

```
Ai Bi
|  |
+--+--+
|     |
AND   XOR
|     |
Gi    Pi
|     |
+-----+-----+
      |     |
      |     +-----> Si = Pi XOR Ci-1
      |
      +-----> Carry Logic (parallel)
                  |
                  Ci
```

## Truth Table (per bit)

| Ai | Bi | Gi | Pi |
|----|----|----|----|
| 0  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  |
| 1  | 0  | 0  | 1  |
| 1  | 1  | 1  | 0  |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity cla_4bit is
  port (
    a, b : in  std_logic_vector(3 downto 0);
    cin  : in  std_logic;
    sum  : out std_logic_vector(3 downto 0);
    cout : out std_logic
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
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_cla is
end entity;

architecture sim of tb_cla is
  signal a, b : std_logic_vector(3 downto 0);
  signal cin  : std_logic;
  signal sum  : std_logic_vector(3 downto 0);
  signal cout : std_logic;
begin
  uut: entity work.cla_4bit port map (a => a, b => b, cin => cin, sum => sum, cout => cout);

  process begin
    a <= "0011"; b <= "0101"; cin <= '0'; wait for 10 ns;
    a <= "0110"; b <= "0011"; cin <= '0'; wait for 10 ns;
    a <= "1111"; b <= "0001"; cin <= '0'; wait for 10 ns;
    a <= "1010"; b <= "1010"; cin <= '0'; wait for 10 ns;
    a <= "1111"; b <= "1111"; cin <= '0'; wait for 10 ns;
    a <= "0000"; b <= "0000"; cin <= '1'; wait for 10 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
A=0011 B=0101 Cin=0 | Sum=1000 Cout=0
A=0110 B=0011 Cin=0 | Sum=1001 Cout=0
A=1111 B=0001 Cin=0 | Sum=0000 Cout=1
A=1010 B=1010 Cin=0 | Sum=0100 Cout=1
A=1111 B=1111 Cin=0 | Sum=1110 Cout=1
A=0000 B=0000 Cin=1 | Sum=0001 Cout=0
```

## Conclusion

Designed a 4-bit Carry Look-Ahead Adder. The CLA computes all carry signals in parallel using generate/propagate logic, significantly reducing the propagation delay compared to a ripple carry adder.
