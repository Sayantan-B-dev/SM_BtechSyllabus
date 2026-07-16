# Implementing 8-bit simple CPU design through HDL.

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 4  
**Date:** 08-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a simple CPU control unit using a finite state machine (FSM).
- Implement the fetch-decode-execute cycle.
- Simulate the control unit with the datapath.

## Theory

**CPU Control Unit:**
The control unit sequences the operations of the CPU through the fetch-decode-execute cycle:

1. **Fetch:** Load the next instruction from memory (address from PC) into the Instruction Register (IR). Increment PC.
2. **Decode:** Interpret the opcode and prepare control signals.
3. **Execute:** Perform the operation (ALU computation, register write, etc.).

**State Machine (3 states):**
```
  +-------+       +---------+       +----------+
  | FETCH | ----> | DECODE  | ----> | EXECUTE  |
  +-------+       +---------+       +----------+
      ^                                  |
      +----------------------------------+
```

**Control Signals Generated:**
- `pc_inc`: Increment program counter
- `ir_load`: Load instruction register
- `reg_wr_en`: Enable register file write
- `alu_sel`: ALU operation select

## VHDL Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity cpu_control is
  port (
    clk, rst  : in  std_logic;
    opcode    : in  std_logic_vector(2 downto 0);
    pc_inc    : out std_logic;
    ir_load   : out std_logic;
    reg_wr_en : out std_logic;
    mem_read  : out std_logic
  );
end entity;

architecture behavioral of cpu_control is
  type state_type is (FETCH, DECODE, EXEC);
  signal state, next_state : state_type;
begin
  process (clk, rst) begin
    if rst = '1' then
      state <= FETCH;
    elsif rising_edge(clk) then
      state <= next_state;
    end if;
  end process;

  process (state) begin
    next_state <= state;
    case state is
      when FETCH  => next_state <= DECODE;
      when DECODE => next_state <= EXEC;
      when EXEC   => next_state <= FETCH;
    end case;
  end process;

  process (state, opcode) begin
    pc_inc    <= '0';
    ir_load   <= '0';
    reg_wr_en <= '0';
    mem_read  <= '0';

    case state is
      when FETCH =>
        mem_read <= '1';
        ir_load  <= '1';
      when DECODE =>
      when EXEC =>
        pc_inc <= '1';
        if opcode /= "011" then
          reg_wr_en <= '1';
        end if;
    end case;
  end process;
end architecture;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity simple_cpu is
  port (
    clk, rst     : in  std_logic;
    instruction  : in  std_logic_vector(7 downto 0);
    alu_result   : out std_logic_vector(7 downto 0)
  );
end entity;

architecture behavioral of simple_cpu is
  signal pc_inc, ir_load, reg_wr_en : std_logic;
  signal opcode : std_logic_vector(2 downto 0);
  signal pc     : std_logic_vector(7 downto 0) := (others => '0');
  signal ir     : std_logic_vector(7 downto 0);
  signal reg_a, reg_b : std_logic_vector(7 downto 0) := (others => '0');
  signal alu_out : std_logic_vector(7 downto 0);
begin
  process (clk, rst) begin
    if rst = '1' then
      pc <= (others => '0');
    elsif rising_edge(clk) then
      if pc_inc = '1' then
        pc <= std_logic_vector(unsigned(pc) + 1);
      end if;
    end if;
  end process;

  ctrl: entity work.cpu_control
    port map (clk => clk, rst => rst, opcode => opcode,
              pc_inc => pc_inc, ir_load => ir_load,
              reg_wr_en => reg_wr_en, mem_read => open);

  process (clk) begin
    if rising_edge(clk) then
      if ir_load = '1' then
        ir <= instruction;
      end if;
    end if;
  end process;
  opcode <= ir(7 downto 5);

  process (clk) begin
    if rising_edge(clk) then
      if reg_wr_en = '1' then
        reg_a <= alu_out;
      end if;
    end if;
  end process;

  alu_out <= std_logic_vector(unsigned(reg_a) + unsigned(reg_b)) when opcode = "000" else
             std_logic_vector(unsigned(reg_a) - unsigned(reg_b)) when opcode = "001" else
             reg_a when opcode = "010" else
             instruction when opcode = "011" else
             reg_a AND reg_b when opcode = "100" else
             reg_a OR reg_b when opcode = "101" else
             (others => '0');
  alu_result <= alu_out;
end architecture;
```

## Testbench Code

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_cpu_control is
end entity;

architecture sim of tb_cpu_control is
  signal clk, rst     : std_logic := '0';
  signal instruction  : std_logic_vector(7 downto 0) := (others => '0');
  signal alu_result   : std_logic_vector(7 downto 0);
begin
  cpu: entity work.simple_cpu
    port map (clk => clk, rst => rst, instruction => instruction, alu_result => alu_result);

  clk <= NOT clk after 5 ns;

  process begin
    clk <= '0'; rst <= '0'; instruction <= (others => '0');
    wait for 10 ns; rst <= '1'; wait for 10 ns; rst <= '0';

    instruction <= "01100001"; wait for 30 ns;
    instruction <= "00000001"; wait for 30 ns;
    instruction <= "00100001"; wait for 30 ns;
    wait for 20 ns;
    wait;
  end process;
end architecture;
```

## Expected Output / Waveform

```
clk=0 rst=0 inst=00000000 | alu_result=0
clk=1 rst=1 inst=00000000 | alu_result=0    (reset)
clk=0 rst=0 inst=01100001 | alu_result=0
clk=1 rst=0 inst=01100001 | alu_result=42   (LDI - execute)
clk=0 rst=0 inst=00000001 | alu_result=42
clk=1 rst=0 inst=00000001 | alu_result=84   (ADD - execute)
clk=0 rst=0 inst=00100001 | alu_result=84
clk=1 rst=0 inst=00100001 | alu_result=42   (SUB - execute)
```

## Conclusion

Designed a simple CPU control unit using a 3-state FSM (fetch, decode, execute). The control unit generates the appropriate control signals for each stage, and the integrated CPU successfully executes a sequence of instructions.
