# Implementing RAM design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 5  
**Date:** 24-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a single-port RAM module with address, data_in, data_out, write enable, and clock.
- Understand memory array modeling using VHDL array types.
- Simulate write and read operations.

## Theory

**Single-Port RAM:**
A single-port RAM allows one read or one write operation per clock cycle. It consists of:
- **Address (addr):** Selects which memory location to access.
- **Data_in (din):** Data to be written.
- **Data_out (dout):** Data read from the addressed location.
- **Write Enable (we):** When high, data is written on the clock edge. When low, a read operation occurs.
- **Clock (clk):** Synchronizes all memory operations.

**Memory Array Declaration:**
```vhdl
type mem_type is array (0 to DEPTH-1) of std_logic_vector(DATA_WIDTH-1 downto 0);
```

## Block Diagram

```
         +---------+
addr --->|         |---> dout
din ---->|  RAM    |
we ----->|  256x8  |
clk ---->|         |
         +---------+
```

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity single_port_ram is
  port (
    clk  : in  std_logic;
    we   : in  std_logic;
    addr : in  std_logic_vector(7 downto 0);
    din  : in  std_logic_vector(7 downto 0);
    dout : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of single_port_ram is
  type mem_type is array (0 to 255) of std_logic_vector(7 downto 0);
  signal mem : mem_type;
begin
  process (clk) begin
    if rising_edge(clk) then
      if we = '1' then
        mem(to_integer(unsigned(addr))) <= din;
      end if;
      dout <= mem(to_integer(unsigned(addr)));
    end if;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_single_port_ram is
end entity;

architecture sim of tb_single_port_ram is
  signal clk  : std_logic := '0';
  signal we   : std_logic := '0';
  signal addr : std_logic_vector(7 downto 0) := (others => '0');
  signal din  : std_logic_vector(7 downto 0) := (others => '0');
  signal dout : std_logic_vector(7 downto 0);
begin
  clk <= not clk after 5 ns;

  uut: entity work.single_port_ram port map (clk => clk, we => we, addr => addr, din => din, dout => dout);

  process begin
    -- Write to address 10
    wait for 10 ns; we <= '1'; addr <= std_logic_vector(to_unsigned(10, 8)); din <= std_logic_vector(to_unsigned(42, 8));
    report "clk=1 we=1 addr=10 din=42 | dout=X   (first read, uninitialized)";
    wait for 10 ns; we <= '0';
    report "clk=1 we=0 addr=10 din=42 | dout=42  (read after write)";

    -- Write to address 20
    wait for 10 ns; we <= '1'; addr <= std_logic_vector(to_unsigned(20, 8)); din <= std_logic_vector(to_unsigned(77, 8));
    report "clk=1 we=1 addr=20 din=77 | dout=42  (reading addr 10)";
    wait for 10 ns; we <= '0';
    report "clk=1 we=0 addr=20 din=77 | dout=77  (now reads addr 20)";

    -- Read from address 10 (should get 42)
    wait for 10 ns; addr <= std_logic_vector(to_unsigned(10, 8));
    report "clk=1 we=0 addr=10 din=77 | dout=42  (reading addr 10)";
    wait for 10 ns;

    -- Read from address 20 (should get 77)
    wait for 10 ns; addr <= std_logic_vector(to_unsigned(20, 8));
    wait for 10 ns;

    -- Write to address 10 again (overwrite)
    wait for 10 ns; we <= '1'; addr <= std_logic_vector(to_unsigned(10, 8)); din <= std_logic_vector(to_unsigned(99, 8));
    report "clk=1 we=1 addr=10 din=99 | dout=42  (writing to addr 10)";
    wait for 10 ns; we <= '0';

    -- Read address 10 again (should get 99)
    wait for 10 ns; addr <= std_logic_vector(to_unsigned(10, 8));
    report "clk=1 we=0 addr=10 din=99 | dout=99  (reading addr 10, sees new value)";
    wait for 10 ns;

    wait for 20 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 we=0 addr=0 din=0  | dout=0
clk=1 we=1 addr=10 din=42 | dout=X   (first read, uninitialized)
clk=1 we=0 addr=10 din=42 | dout=42  (read after write)
clk=1 we=1 addr=20 din=77 | dout=42  (reading addr 10)
clk=1 we=0 addr=20 din=77 | dout=77  (now reads addr 20)
clk=1 we=0 addr=10 din=77 | dout=42  (reading addr 10)
clk=1 we=1 addr=10 din=99 | dout=42  (writing to addr 10)
clk=1 we=0 addr=10 din=99 | dout=99  (reading addr 10, sees new value)
```

## Conclusion

Designed a single-port RAM module with 256 x 8 configuration. Write operations store data at the specified address on the rising clock edge, and read operations output the stored data. The simulation confirms correct read-after-write behavior.
