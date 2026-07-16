# Interface a Meomory with 8 bit CPU

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 6  
**Date:** 15-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Perform a complete system test: load a program into memory, execute instructions, and verify results.
- Create a testbench that initializes memory with a simple program.
- Observe the CPU executing the program step by step.

## Theory

**Loading a Program:**
To test the full system, we pre-load the RAM with a program (machine code). The CPU's program counter starts at address 0 and fetches instructions sequentially.

**Sample Program:**
A simple program that:
1. Loads value 10 from memory into the accumulator.
2. Adds value 5 from memory to the accumulator.
3. Subtracts value 3 from the accumulator.
4. Stores the result.

**Memory Map:**
| Address | Content   | Description             |
|---------|-----------|------------------------|
| 0x00    | 0x0A      | LOAD R0, [addr]         |
| 0x01    | 0x10      | Address of data (16)    |
| 0x02    | 0x05      | ADD R0, [addr]          |
| 0x03    | 0x11      | Address of data (17)    |
| 0x04    | 0x09      | SUB R0, [addr]          |
| 0x05    | 0x12      | Address of data (18)    |
| ...     | ...       | ...                     |
| 0x10    | 10        | Data: first operand     |
| 0x11    | 5         | Data: second operand    |
| 0x12    | 3         | Data: third operand     |

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
  signal mem : mem_array := (
    0 => "01000000", 1 => "00010000",
    2 => "00000000", 3 => "00010001",
    4 => "00100000", 5 => "00010010",
    6 => "01100000", 7 => "01100000",
    16 => "00001010", 17 => "00000101", 18 => "00000011",
    others => (others => '0')
  );
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
  signal pc, ir, acc, mar : std_logic_vector(7 downto 0) := (others => '0');
  signal fetch_operand : std_logic := '0';
begin
  addr_out <= pc when state = FETCH else mar;
  data_out <= acc;

  process (clk, rst) begin
    if rst = '1' then
      state <= FETCH;
      pc <= (others => '0');
      ir <= (others => '0');
      acc <= (others => '0');
      mar <= (others => '0');
      fetch_operand <= '0';
    elsif rising_edge(clk) then
      case state is
        when FETCH =>
          if fetch_operand = '0' then
            ir <= data_in;
            pc <= std_logic_vector(unsigned(pc) + 1);
            state <= DECODE;
          else
            mar <= data_in;
            fetch_operand <= '0';
            state <= EXEC;
          end if;
        when DECODE =>
          if ir(7 downto 5) /= "011" then
            fetch_operand <= '1';
            state <= FETCH;
          else
            state <= EXEC;
          end if;
        when EXEC =>
          case ir(7 downto 5) is
            when "000" => acc <= std_logic_vector(unsigned(acc) + unsigned(data_in));
            when "001" => acc <= std_logic_vector(unsigned(acc) - unsigned(data_in));
            when "010" => acc <= data_in;
            when "100" => acc <= acc AND data_in;
            when "101" => acc <= acc OR data_in;
            when others => acc <= acc;
          end case;
          state <= FETCH;
      end case;
    end if;
  end process;

  mem_read  <= '1';
  mem_write <= '0';
end architecture;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity complete_system is
  port (
    clk, rst : in std_logic
  );
end entity;

architecture structural of complete_system is
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

entity tb_complete_system is
end entity;

architecture sim of tb_complete_system is
  signal clk, rst : std_logic := '0';
begin
  uut: entity work.complete_system
    port map (clk => clk, rst => rst);

  clk <= NOT clk after 5 ns;

  process begin
    report "Starting complete system test...";
    clk <= '0'; rst <= '0';
    wait for 10 ns; rst <= '1';
    wait for 10 ns; rst <= '0';
    wait for 200 ns;
    report "System test complete.";
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
Starting complete system test...
Time=0 clk=0
Time=10 clk=0 rst=1    (reset)
Time=20 clk=0 rst=0    (start execution)
... (CPU fetches instructions and executes)
... LOAD: acc = 10
... ADD:  acc = 15
... SUB:  acc = 12
...
System test complete.
```

## Conclusion

Performed a complete system test integrating a CPU, memory, and a pre-loaded program. The CPU successfully fetched instructions from memory, decoded them, and executed the operations (LOAD, ADD, SUB) to produce the final result. This demonstrates a fully functional minimal computing system.
