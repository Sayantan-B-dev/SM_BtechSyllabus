# Basic digital logic base programming with HDL through Behavioural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 6  
**Date:** 23-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 3:8 decoder using behavioral modeling.
- Design an 8:3 encoder using behavioral modeling.
- Verify both circuits through exhaustive simulation.

## Theory

**Decoder:**
A decoder converts n-bit input to 2^n-bit output. For a 3:8 decoder:
- Input: A[2:0] (3-bit binary)
- Output: Y[7:0] (one-hot -- exactly one output is 1)
- For input "000", Y(0)='1'; for "001", Y(1)='1'; ...; for "111", Y(7)='1'.

**Encoder:**
An encoder performs the reverse operation. For an 8:3 encoder:
- Input: D[7:0] (one-hot)
- Output: Q[2:0] (3-bit binary)
- For D(0)='1', Q="000"; for D(1)='1', Q="001"; ...; for D(7)='1', Q="111".

## Truth Table

**3:8 Decoder:**
| A2 | A1 | A0 | Y7 | Y6 | Y5 | Y4 | Y3 | Y2 | Y1 | Y0 |
|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 1  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1  | 0  | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 1  | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |

**8:3 Encoder:**
| D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Q2 | Q1 | Q0 |
|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 1  |
| 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  |

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity decoder_3to8 is
  port (
    a : in  std_logic_vector(2 downto 0);
    y : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of decoder_3to8 is
begin
  process (a) begin
    case a is
      when "000" => y <= "00000001";
      when "001" => y <= "00000010";
      when "010" => y <= "00000100";
      when "011" => y <= "00001000";
      when "100" => y <= "00010000";
      when "101" => y <= "00100000";
      when "110" => y <= "01000000";
      when "111" => y <= "10000000";
      when others => y <= "00000000";
    end case;
  end process;
end architecture;

library ieee;
use ieee.std_logic_1164.all;

entity encoder_8to3 is
  port (
    d : in  std_logic_vector(7 downto 0);
    q : out std_logic_vector(2 downto 0)
  );
end entity;

architecture behavioral of encoder_8to3 is
begin
  process (d) begin
    case d is
      when "00000001" => q <= "000";
      when "00000010" => q <= "001";
      when "00000100" => q <= "010";
      when "00001000" => q <= "011";
      when "00010000" => q <= "100";
      when "00100000" => q <= "101";
      when "01000000" => q <= "110";
      when "10000000" => q <= "111";
      when others => q <= "000";
    end case;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_dec_enc is
end entity;

architecture sim of tb_dec_enc is
  signal a : std_logic_vector(2 downto 0);
  signal y : std_logic_vector(7 downto 0);
  signal d : std_logic_vector(7 downto 0);
  signal q : std_logic_vector(2 downto 0);
begin
  dec: entity work.decoder_3to8 port map (a => a, y => y);
  enc: entity work.encoder_8to3 port map (d => d, q => q);

  process begin
    report "=== 3:8 Decoder ===";
    a <= "000"; wait for 10 ns;
    a <= "001"; wait for 10 ns;
    a <= "010"; wait for 10 ns;
    a <= "011"; wait for 10 ns;
    a <= "100"; wait for 10 ns;
    a <= "101"; wait for 10 ns;
    a <= "110"; wait for 10 ns;
    a <= "111"; wait for 10 ns;

    wait for 20 ns;

    report "=== 8:3 Encoder ===";
    d <= "00000001"; wait for 10 ns;
    d <= "00000010"; wait for 10 ns;
    d <= "00000100"; wait for 10 ns;
    d <= "00001000"; wait for 10 ns;
    d <= "00010000"; wait for 10 ns;
    d <= "00100000"; wait for 10 ns;
    d <= "01000000"; wait for 10 ns;
    d <= "10000000"; wait for 10 ns;

    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
=== 3:8 Decoder ===
a=000 | y=00000001
a=001 | y=00000010
a=010 | y=00000100
a=011 | y=00001000
a=100 | y=00010000
a=101 | y=00100000
a=110 | y=01000000
a=111 | y=10000000

=== 8:3 Encoder ===
d=00000001 | q=000
d=00000010 | q=001
d=00000100 | q=010
d=00001000 | q=011
d=00010000 | q=100
d=00100000 | q=101
d=01000000 | q=110
d=10000000 | q=111
```

## Conclusion

Successfully implemented a 3:8 decoder and an 8:3 encoder using behavioral modeling with the `case` statement in VHDL. The decoder produces a one-hot output, while the encoder generates the corresponding binary code from a one-hot input.
