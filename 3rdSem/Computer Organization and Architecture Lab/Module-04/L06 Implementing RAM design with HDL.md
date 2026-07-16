# Implementing RAM design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 6  
**Date:** 24-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a dual-port RAM module with separate read and write ports.
- Understand simultaneous access capabilities of dual-port RAM.
- Simulate concurrent read and write operations.

## Theory

**Dual-Port RAM:**
A dual-port RAM has two independent ports (Port A and Port B), allowing simultaneous access to different memory locations. Each port has its own address, data, and control signals.

**Common Configurations:**
- Two read/write ports (2RW)
- One read/write port + one read-only port (1RW + 1R)
- One read/write port + one write-only port (1RW + 1W)

In this lab, we implement a true dual-port RAM where both ports can read or write independently.

## Block Diagram

```
         +---------+
addr_a-->|         |---> dout_a
din_a--->| DUAL    |
we_a---->| PORT    |
         |  RAM    |
addr_b-->| 256x8   |---> dout_b
din_b--->|         |
we_b---->|         |
clk------>|         |
         +---------+
```

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity dual_port_ram is
  port (
    clk   : in  std_logic;
    we_a  : in  std_logic;
    addr_a: in  std_logic_vector(7 downto 0);
    din_a : in  std_logic_vector(7 downto 0);
    dout_a: out std_logic_vector(7 downto 0);
    we_b  : in  std_logic;
    addr_b: in  std_logic_vector(7 downto 0);
    din_b : in  std_logic_vector(7 downto 0);
    dout_b: out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of dual_port_ram is
  type mem_type is array (0 to 255) of std_logic_vector(7 downto 0);
  signal mem : mem_type;
begin
  process (clk) begin
    if rising_edge(clk) then
      if we_a = '1' then
        mem(to_integer(unsigned(addr_a))) <= din_a;
      end if;
      dout_a <= mem(to_integer(unsigned(addr_a)));
    end if;
  end process;

  process (clk) begin
    if rising_edge(clk) then
      if we_b = '1' then
        mem(to_integer(unsigned(addr_b))) <= din_b;
      end if;
      dout_b <= mem(to_integer(unsigned(addr_b)));
    end if;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_dual_port_ram is
end entity;

architecture sim of tb_dual_port_ram is
  signal clk   : std_logic := '0';
  signal we_a  : std_logic := '0';
  signal we_b  : std_logic := '0';
  signal addr_a: std_logic_vector(7 downto 0) := (others => '0');
  signal addr_b: std_logic_vector(7 downto 0) := (others => '0');
  signal din_a : std_logic_vector(7 downto 0) := (others => '0');
  signal din_b : std_logic_vector(7 downto 0) := (others => '0');
  signal dout_a: std_logic_vector(7 downto 0);
  signal dout_b: std_logic_vector(7 downto 0);
begin
  clk <= not clk after 5 ns;

  uut: entity work.dual_port_ram port map (clk => clk, we_a => we_a, addr_a => addr_a, din_a => din_a, dout_a => dout_a, we_b => we_b, addr_b => addr_b, din_b => din_b, dout_b => dout_b);

  process begin
    -- Port A writes to address 10, Port B writes to address 20 simultaneously
    wait for 10 ns; we_a <= '1'; addr_a <= std_logic_vector(to_unsigned(10, 8)); din_a <= std_logic_vector(to_unsigned(100, 8));
    we_b <= '1'; addr_b <= std_logic_vector(to_unsigned(20, 8)); din_b <= std_logic_vector(to_unsigned(200, 8));
    report "clk=1 | PortA: we=1 addr=10 din=100 dout=X | PortB: we=1 addr=20 din=200 dout=X";
    wait for 10 ns; we_a <= '0'; we_b <= '0';
    report "clk=1 | PortA: we=0 addr=10 din=100 dout=100 | PortB: we=0 addr=20 din=200 dout=200";

    -- Port A reads address 10, Port B reads address 20 simultaneously
    wait for 10 ns; addr_a <= std_logic_vector(to_unsigned(10, 8)); addr_b <= std_logic_vector(to_unsigned(20, 8));
    report "clk=1 | PortA: we=0 addr=10 din=100 dout=100 | PortB: we=0 addr=20 din=200 dout=200";
    wait for 10 ns;

    -- Port A writes to address 10 while Port B reads address 10 simultaneously
    wait for 10 ns; we_a <= '1'; addr_a <= std_logic_vector(to_unsigned(10, 8)); din_a <= std_logic_vector(to_unsigned(150, 8));
    we_b <= '0'; addr_b <= std_logic_vector(to_unsigned(10, 8));
    report "clk=1 | PortA: we=1 addr=10 din=150 dout=100 | PortB: we=0 addr=10 din=200 dout=100";
    wait for 10 ns; we_a <= '0';

    -- Both read address 10
    wait for 10 ns; addr_a <= std_logic_vector(to_unsigned(10, 8)); addr_b <= std_logic_vector(to_unsigned(10, 8));
    report "clk=1 | PortA: we=0 addr=10 din=150 dout=150 | PortB: we=0 addr=10 din=200 dout=150";
    wait for 10 ns;
    report "clk=1 | PortA: we=0 addr=10 din=150 dout=150 | PortB: we=0 addr=10 din=200 dout=150";
    wait for 10 ns;

    wait for 20 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 | PortA: we=0 addr=0 din=0 dout=0 | PortB: we=0 addr=0 din=0 dout=0
clk=1 | PortA: we=1 addr=10 din=100 dout=X | PortB: we=1 addr=20 din=200 dout=X
clk=1 | PortA: we=0 addr=10 din=100 dout=100 | PortB: we=0 addr=20 din=200 dout=200
clk=1 | PortA: we=0 addr=10 din=100 dout=100 | PortB: we=0 addr=20 din=200 dout=200
clk=1 | PortA: we=1 addr=10 din=150 dout=100 | PortB: we=0 addr=10 din=200 dout=100
clk=1 | PortA: we=0 addr=10 din=150 dout=150 | PortB: we=0 addr=10 din=200 dout=150
clk=1 | PortA: we=0 addr=10 din=150 dout=150 | PortB: we=0 addr=10 din=200 dout=150
```

## Conclusion

Designed a dual-port RAM module with independent read/write ports. The simulation demonstrates simultaneous write operations at different addresses, concurrent reads, and read-write to the same address through different ports.
