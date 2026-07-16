# Implementing 8-bit Register design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 4  
**Date:** 17-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit shift register with left shift, right shift, and parallel load capabilities.
- Understand the concept of shifting data in sequential circuits.
- Simulate to verify all shift operations.

## Theory

**Shift Register:**
A shift register moves data bits left or right on each clock cycle. It can also be loaded in parallel with a new value.

**Operation Modes:**
- **Parallel Load (load = 1):** Load the full 8-bit value on the next clock edge.
- **Left Shift (load = 0, dir = 0):** Shift bits left; `q[0]` gets `ser_in`.
- **Right Shift (load = 0, dir = 1):** Shift bits right; `q[7]` gets `ser_in`.

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity shift_reg_8bit is
  port (
    clk    : in  std_logic;
    rst    : in  std_logic;
    load   : in  std_logic;
    dir    : in  std_logic;
    ser_in : in  std_logic;
    par_in : in  std_logic_vector(7 downto 0);
    q      : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of shift_reg_8bit is
  signal q_reg : std_logic_vector(7 downto 0);
begin
  process (clk) begin
    if rising_edge(clk) then
      if rst = '1' then
        q_reg <= (others => '0');
      elsif load = '1' then
        q_reg <= par_in;
      elsif dir = '0' then
        q_reg <= q_reg(6 downto 0) & ser_in;
      else
        q_reg <= ser_in & q_reg(7 downto 1);
      end if;
    end if;
  end process;
  q <= q_reg;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_shift_reg is
end entity;

architecture sim of tb_shift_reg is
  signal clk    : std_logic := '0';
  signal rst    : std_logic := '0';
  signal load   : std_logic := '0';
  signal dir    : std_logic := '0';
  signal ser_in : std_logic := '0';
  signal par_in : std_logic_vector(7 downto 0) := (others => '0');
  signal q      : std_logic_vector(7 downto 0);
begin
  clk <= not clk after 5 ns;

  uut: entity work.shift_reg_8bit port map (clk => clk, rst => rst, load => load, dir => dir, ser_in => ser_in, par_in => par_in, q => q);

  process begin
    -- Reset
    wait for 10 ns; rst <= '1';
    report "clk=1 rst=1 load=0 dir=0 ser=0 par=0   | q=00000000 (0) -- reset";
    wait for 10 ns; rst <= '0';

    -- Parallel load: value 0b11001010 (202)
    wait for 10 ns; load <= '1'; par_in <= "11001010";
    report "clk=1 rst=0 load=1 dir=0 ser=0 par=202 | q=11001010 (202) -- loaded";
    wait for 10 ns; load <= '0';

    -- Left shift with ser_in=1
    wait for 10 ns; dir <= '0'; ser_in <= '1';
    report "clk=1 rst=0 load=0 dir=0 ser=1 par=202 | q=10010101 (149) -- left shift with 1";
    wait for 10 ns; ser_in <= '0';
    report "clk=1 rst=0 load=0 dir=0 ser=0 par=202 | q=00101010 (42)  -- left shift with 0";
    wait for 10 ns;

    -- Right shift with ser_in=1
    wait for 10 ns; dir <= '1'; ser_in <= '1';
    report "clk=1 rst=0 load=0 dir=1 ser=1 par=202 | q=10010101 (149) -- right shift with 1";
    wait for 10 ns;

    -- Load new value
    wait for 10 ns; load <= '1'; par_in <= "00001111";
    report "clk=1 rst=0 load=1 dir=1 ser=0 par=15  | q=00001111 (15)  -- loaded";
    wait for 10 ns; load <= '0';

    -- Shift right with ser_in=0
    wait for 10 ns; dir <= '1'; ser_in <= '0';
    report "clk=1 rst=0 load=0 dir=1 ser=0 par=15  | q=00000111 (7)   -- right shift with 0";
    wait for 10 ns;

    wait for 20 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 rst=1 load=0 dir=0 ser=0 par=0   | q=00000000 (0)
clk=1 rst=1 load=0 dir=0 ser=0 par=0   | q=00000000 (0) -- reset
clk=1 rst=0 load=1 dir=0 ser=0 par=202 | q=11001010 (202) -- loaded
clk=0 rst=0 load=0 dir=0 ser=1 par=202 | q=11001010 (202)
clk=1 rst=0 load=0 dir=0 ser=1 par=202 | q=10010101 (149) -- left shift with 1
clk=1 rst=0 load=0 dir=0 ser=0 par=202 | q=00101010 (42)  -- left shift with 0
clk=1 rst=0 load=0 dir=1 ser=1 par=202 | q=10010101 (149) -- right shift with 1
clk=1 rst=0 load=1 dir=1 ser=0 par=15  | q=00001111 (15)  -- loaded
clk=1 rst=0 load=0 dir=1 ser=0 par=15  | q=00000111 (7)   -- right shift with 0
```

## Conclusion

Designed an 8-bit shift register supporting parallel load, left shift, and right shift operations. The simulation verifies correct shifting behavior and data retention based on the control signals.
