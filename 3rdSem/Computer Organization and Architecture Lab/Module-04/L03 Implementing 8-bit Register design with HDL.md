# Implementing 8-bit Register design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 3  
**Date:** 17-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit D flip-flop register with synchronous reset and enable.
- Understand the behavior of sequential circuits with clock, reset, and enable.
- Simulate to verify load, hold, and reset operations.

## Theory

**D Flip-Flop Register:**
An n-bit register stores n bits of data on the rising (or falling) edge of a clock signal. It consists of n D flip-flops sharing a common clock.

**Control Signals:**
- **Clock (clk):** Triggers the storage operation on the active edge.
- **Reset (rst):** Forces all bits to 0 (synchronous: on clock edge; asynchronous: immediately).
- **Enable (en):** When high, new data is loaded on the clock edge. When low, the register retains its current value.

**Timing Diagram (Synchronous):**
```
clk   : _|-|_|-|_|-|_|-|_|-|
rst   : ___|---|___________
en    : ___|-------|_______
d     : XX< A >< B >< C >XX
q     : XX< 0 >< A >< B >XX (rst clears, en loads)
```

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity reg_8bit is
  port (
    clk : in  std_logic;
    rst : in  std_logic;
    en  : in  std_logic;
    d   : in  std_logic_vector(7 downto 0);
    q   : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of reg_8bit is
begin
  process (clk) begin
    if rising_edge(clk) then
      if rst = '1' then
        q <= (others => '0');
      elsif en = '1' then
        q <= d;
      end if;
    end if;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_reg_8bit is
end entity;

architecture sim of tb_reg_8bit is
  signal clk : std_logic := '0';
  signal rst : std_logic := '0';
  signal en  : std_logic := '0';
  signal d   : std_logic_vector(7 downto 0) := (others => '0');
  signal q   : std_logic_vector(7 downto 0);
begin
  clk <= not clk after 5 ns;

  uut: entity work.reg_8bit port map (clk => clk, rst => rst, en => en, d => d, q => q);

  process begin
    report "clk=0 rst=0 en=0 d=0 | q=0";

    -- Reset the register
    wait for 10 ns; rst <= '1';
    report "clk=1 rst=1 en=0 d=0 | q=0  (reset active)";
    wait for 10 ns; rst <= '0';

    -- Load value A
    wait for 10 ns; en <= '1'; d <= std_logic_vector(to_unsigned(42, 8));
    report "clk=1 rst=0 en=1 d=42 | q=42 (loaded on posedge)";
    wait for 10 ns; en <= '0';

    -- Load value B (should not load because en = 0)
    wait for 10 ns; d <= std_logic_vector(to_unsigned(99, 8));
    report "clk=1 rst=0 en=0 d=99 | q=42 (hold, en=0)";
    wait for 10 ns;

    -- Enable and load C
    wait for 10 ns; en <= '1'; d <= std_logic_vector(to_unsigned(77, 8));
    report "clk=1 rst=0 en=1 d=77 | q=77 (loaded)";
    wait for 10 ns; en <= '0';

    -- Reset again
    wait for 10 ns; rst <= '1';
    report "clk=1 rst=1 en=0 d=77 | q=0  (reset)";
    wait for 10 ns; rst <= '0';

    wait for 20 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 rst=0 en=0 d=0   | q=0
clk=1 rst=0 en=0 d=0   | q=0
clk=0 rst=1 en=0 d=0   | q=0
clk=1 rst=1 en=0 d=0   | q=0  (reset active)
clk=0 rst=0 en=0 d=0   | q=0
clk=1 rst=0 en=0 d=0   | q=0
clk=0 rst=0 en=1 d=42  | q=0
clk=1 rst=0 en=1 d=42  | q=42 (loaded on posedge)
clk=0 rst=0 en=0 d=42  | q=42
clk=1 rst=0 en=0 d=99  | q=42 (hold, en=0)
clk=0 rst=0 en=1 d=77  | q=42
clk=1 rst=0 en=1 d=77  | q=77 (loaded)
clk=0 rst=1 en=0 d=77  | q=77
clk=1 rst=1 en=0 d=77  | q=0  (reset)
```

## Conclusion

Designed an 8-bit register with synchronous reset and enable control. The register correctly loads data only when enabled on the rising clock edge, holds its value when disabled, and resets to zero when reset is asserted.
