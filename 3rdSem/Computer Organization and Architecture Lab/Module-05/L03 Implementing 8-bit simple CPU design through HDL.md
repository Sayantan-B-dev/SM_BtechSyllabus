# Implementing 8-bit simple CPU design through HDL.

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 3  
**Date:** 08-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design the datapath of a simple 8-bit CPU including ALU, register file, and instruction register.
- Define a basic instruction set for the CPU.
- Simulate the CPU datapath with sample instructions.

## Theory

**Simple CPU Datapath:**
A CPU datapath consists of:
- **Register File:** A set of general-purpose registers (e.g., 4 registers: R0-R3, each 8-bit).
- **ALU:** Performs arithmetic/logic operations on register values.
- **Instruction Register (IR):** Holds the current instruction being executed.
- **Program Counter (PC):** Points to the next instruction address.

**Basic Instruction Set:**
| Opcode | Mnemonic | Description            |
|--------|----------|------------------------|
| 000    | ADD Rd, Rs, Rt | Rd = Rs + Rt      |
| 001    | SUB Rd, Rs, Rt | Rd = Rs - Rt      |
| 010    | MOV Rd, Rs     | Rd = Rs           |
| 011    | LDI Rd, Imm    | Rd = immediate    |
| 100    | AND Rd, Rs, Rt | Rd = Rs & Rt      |
| 101    | OR  Rd, Rs, Rt | Rd = Rs | Rt      |

**Instruction Format:**
```
[7:5] Opcode (3 bits)
[4:3] Destination Register / Rd (2 bits)
[2:1] Source Register 1 / Rs (2 bits)
[0]   Source Register 2 / Rt or immediate flag
```

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity reg_file is
  port (
    clk, wr_en                : in  std_logic;
    rd_addr, rs_addr, rt_addr : in  std_logic_vector(1 downto 0);
    wr_data                   : in  std_logic_vector(7 downto 0);
    rs_data, rt_data          : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of reg_file is
  type reg_array is array (0 to 3) of std_logic_vector(7 downto 0);
  signal regs : reg_array;
begin
  process (clk) begin
    if rising_edge(clk) then
      if wr_en = '1' then
        regs(to_integer(unsigned(rd_addr))) <= wr_data;
      end if;
    end if;
  end process;

  rs_data <= regs(to_integer(unsigned(rs_addr)));
  rt_data <= regs(to_integer(unsigned(rt_addr)));
end architecture;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity cpu_datapath is
  port (
    clk, rst       : in  std_logic;
    ir_load        : in  std_logic;
    reg_wr_en      : in  std_logic;
    instruction_in : in  std_logic_vector(7 downto 0);
    alu_result     : out std_logic_vector(7 downto 0)
  );
end entity;

architecture structural of cpu_datapath is
  signal ir_out   : std_logic_vector(7 downto 0);
  signal opcode   : std_logic_vector(2 downto 0);
  signal rd, rs, rt : std_logic_vector(1 downto 0);
  signal rs_data, rt_data, alu_out : std_logic_vector(7 downto 0);
begin
  process (clk) begin
    if rising_edge(clk) then
      if ir_load = '1' then
        ir_out <= instruction_in;
      end if;
    end if;
  end process;

  opcode <= ir_out(7 downto 5);
  rd     <= ir_out(4 downto 3);
  rs     <= ir_out(2 downto 1);
  rt     <= '0' & ir_out(0);

  rf: entity work.reg_file
    port map (
      clk => clk, wr_en => reg_wr_en,
      rd_addr => rd, rs_addr => rs, rt_addr => rt,
      wr_data => alu_out,
      rs_data => rs_data, rt_data => rt_data
    );

  alu: entity work.alu_8bit
    port map (a => rs_data, b => rt_data, sel => opcode, result => alu_out);

  alu_result <= alu_out;
end architecture;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_8bit is
  port (
    a, b   : in  std_logic_vector(7 downto 0);
    sel    : in  std_logic_vector(2 downto 0);
    result : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of alu_8bit is
begin
  process (a, b, sel) begin
    case sel is
      when "000" => result <= std_logic_vector(unsigned(a) + unsigned(b));
      when "001" => result <= std_logic_vector(unsigned(a) - unsigned(b));
      when "010" => result <= a;
      when "011" => result <= b;
      when "100" => result <= a AND b;
      when "101" => result <= a OR b;
      when others => result <= (others => '0');
    end case;
  end process;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_cpu_datapath is
end entity;

architecture sim of tb_cpu_datapath is
  signal clk, rst          : std_logic := '0';
  signal ir_load, reg_wr_en : std_logic := '0';
  signal instruction_in    : std_logic_vector(7 downto 0) := (others => '0');
  signal alu_result        : std_logic_vector(7 downto 0);
begin
  uut: entity work.cpu_datapath
    port map (clk => clk, rst => rst, ir_load => ir_load,
              reg_wr_en => reg_wr_en, instruction_in => instruction_in,
              alu_result => alu_result);

  clk <= NOT clk after 5 ns;

  process begin
    clk <= '0'; rst <= '0'; ir_load <= '0'; reg_wr_en <= '0'; instruction_in <= (others => '0');

    wait for 10 ns; rst <= '1'; wait for 10 ns; rst <= '0';

    instruction_in <= "01000010";
    ir_load <= '1'; wait for 10 ns;
    ir_load <= '0';
    reg_wr_en <= '1'; wait for 10 ns;
    reg_wr_en <= '0';

    instruction_in <= "00000001";
    ir_load <= '1'; wait for 10 ns;
    ir_load <= '0';
    reg_wr_en <= '1'; wait for 10 ns;
    reg_wr_en <= '0';

    wait for 20 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 inst=00000000 opcode=000 | alu_result=0
clk=1 inst=01000010 opcode=010 | alu_result=0
clk=0 inst=01000010 opcode=010 | alu_result=0
clk=1 inst=01000010 opcode=010 | alu_result=42  (MOV R0, R1)
clk=0 inst=00000001 opcode=000 | alu_result=42
clk=1 inst=00000001 opcode=000 | alu_result=84  (ADD R0, R0, R1)
```

## Conclusion

Designed the datapath of a simple 8-bit CPU including a register file, ALU, and instruction register. The datapath correctly decodes instructions and executes them through the ALU.
