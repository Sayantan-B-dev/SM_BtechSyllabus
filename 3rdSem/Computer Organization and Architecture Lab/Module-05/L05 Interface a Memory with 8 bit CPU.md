# Interface a Meomory with 8 bit CPU

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 5  
**Date:** 15-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Connect the CPU module to a RAM module via address bus, data bus, and read/write control.
- Create a top-level module integrating CPU and memory.
- Simulate the integrated system.

## Theory

**CPU-Memory Interface:**
The CPU and memory communicate through:
- **Address Bus:** CPU sends the address of the memory location to access.
- **Data Bus:** Bidirectional pathway for data transfer between CPU and memory.
- **Read/Write Control:** CPU asserts read or write signals to control the direction of data transfer.

**Memory-Mapped CPU:**
The CPU's program counter (PC) provides the address for instruction fetch. For data access, the CPU generates the address from the instruction operands.

**Top-Level Block Diagram:**
```
         +-------+                    +--------+
         |       |-- addr_bus[7:0] -->|        |
         |       |-- data_bus[7:0] <->|  RAM   |
         | CPU   |-- mem_read ------->|  256x8 |
         |       |-- mem_write ------>|        |
         |       |<-- clk ------------|        |
         |       |<-- rst ------------|        |
         +-------+                    +--------+
```

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ram_256x8 is
  port (
    clk  : in  std_logic;
    we   : in  std_logic;
    addr : in  std_logic_vector(7 downto 0);
    din  : in  std_logic_vector(7 downto 0);
    dout : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of ram_256x8 is
  type mem_array is array (0 to 255) of std_logic_vector(7 downto 0);
  signal mem : mem_array;
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

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity cpu_core is
  port (
    clk, rst  : in  std_logic;
    data_in   : in  std_logic_vector(7 downto 0);
    addr_out  : out std_logic_vector(7 downto 0);
    data_out  : out std_logic_vector(7 downto 0);
    mem_read  : out std_logic;
    mem_write : out std_logic
  );
end entity;

architecture behavioral of cpu_core is
  type state_type is (FETCH, DECODE, EXEC);
  signal state : state_type;
  signal pc, ir, acc : std_logic_vector(7 downto 0) := (others => '0');
begin
  addr_out <= pc when state = FETCH else (others => '0');
  data_out <= acc;

  process (clk, rst) begin
    if rst = '1' then
      state <= FETCH;
      pc <= (others => '0');
      ir <= (others => '0');
      acc <= (others => '0');
    elsif rising_edge(clk) then
      case state is
        when FETCH =>
          ir <= data_in;
          state <= DECODE;
        when DECODE =>
          state <= EXEC;
        when EXEC =>
          pc <= std_logic_vector(unsigned(pc) + 1);
          case ir(7 downto 5) is
            when "000" => acc <= std_logic_vector(unsigned(acc) + unsigned(data_in));
            when "001" => acc <= std_logic_vector(unsigned(acc) - unsigned(data_in));
            when "010" => acc <= data_in;
            when "011" => acc <= acc;
            when "100" => acc <= acc AND data_in;
            when "101" => acc <= acc OR data_in;
            when others => acc <= acc;
          end case;
          state <= FETCH;
      end case;
    end if;
  end process;

  mem_read  <= '1' when (state = FETCH) or (state = EXEC and ir(7 downto 5) /= "011") else '0';
  mem_write <= '0';
end architecture;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity cpu_with_memory is
  port (
    clk, rst : in std_logic
  );
end entity;

architecture structural of cpu_with_memory is
  signal addr, data_to_mem, data_from_mem : std_logic_vector(7 downto 0);
  signal mem_read, mem_write : std_logic;
begin
  cpu: entity work.cpu_core
    port map (clk => clk, rst => rst, data_in => data_from_mem,
              addr_out => addr, data_out => data_to_mem,
              mem_read => mem_read, mem_write => mem_write);

  ram: entity work.ram_256x8
    port map (clk => clk, we => mem_write, addr => addr,
              din => data_to_mem, dout => data_from_mem);
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_cpu_memory is
end entity;

architecture sim of tb_cpu_memory is
  signal clk, rst : std_logic := '0';
begin
  uut: entity work.cpu_with_memory
    port map (clk => clk, rst => rst);

  clk <= NOT clk after 5 ns;

  process begin
    clk <= '0'; rst <= '0';
    wait for 10 ns; rst <= '1';
    wait for 10 ns; rst <= '0';
    wait for 100 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 rst=0
clk=1 rst=1    (reset active)
clk=0 rst=0    (reset released, CPU starts fetching)
clk=1 rst=0    (fetch cycle: reads instruction from PC address)
clk=0 rst=0    (decode)
clk=1 rst=0    (execute: increment PC, perform ALU op)
... (continues fetch-decode-execute cycle)
```

## Conclusion

Successfully integrated a simple CPU core with a RAM module. The top-level module connects the CPU and memory through address, data, and control buses, forming a complete minimal computing system.
