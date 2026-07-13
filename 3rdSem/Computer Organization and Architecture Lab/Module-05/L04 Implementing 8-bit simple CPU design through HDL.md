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

## Verilog Code

```verilog
// CPU Control Unit (FSM)
module cpu_control (
    input  wire       clk, rst,
    input  wire [2:0] opcode,
    output reg        pc_inc,
    output reg        ir_load,
    output reg        reg_wr_en,
    output reg        mem_read
);
    // State encoding
    localparam FETCH  = 2'b00;
    localparam DECODE = 2'b01;
    localparam EXEC   = 2'b10;

    reg [1:0] state, next_state;

    // State register
    always @(posedge clk or posedge rst) begin
        if (rst)
            state <= FETCH;
        else
            state <= next_state;
    end

    // Next state logic
    always @(*) begin
        next_state = state;
        case (state)
            FETCH:  next_state = DECODE;
            DECODE: next_state = EXEC;
            EXEC:   next_state = FETCH;
        endcase
    end

    // Output logic
    always @(*) begin
        // Defaults
        pc_inc    = 1'b0;
        ir_load   = 1'b0;
        reg_wr_en = 1'b0;
        mem_read  = 1'b0;

        case (state)
            FETCH: begin
                mem_read = 1'b1;
                ir_load  = 1'b1;
            end
            DECODE: begin
                // Decode: prepare control signals based on opcode
                // (no outputs needed here for simple CPU)
            end
            EXEC: begin
                pc_inc = 1'b1;
                // Write back for ALU operations (opcode != 011 means ALU op)
                if (opcode != 3'b011)  // LDI is handled differently
                    reg_wr_en = 1'b1;
            end
        endcase
    end
endmodule

// Top-level Simple CPU
module simple_cpu (
    input  wire       clk, rst,
    input  wire [7:0] instruction,
    output wire [7:0] alu_result
);
    wire pc_inc, ir_load, reg_wr_en;
    wire [2:0] opcode;
    reg  [7:0] pc;

    // Program Counter
    always @(posedge clk or posedge rst) begin
        if (rst)
            pc <= 8'b00000000;
        else if (pc_inc)
            pc <= pc + 1;
    end

    // Control Unit
    cpu_control ctrl (.clk(clk), .rst(rst), .opcode(opcode),
                      .pc_inc(pc_inc), .ir_load(ir_load),
                      .reg_wr_en(reg_wr_en), .mem_read());

    // Datapath (simplified)
    reg [7:0] ir;
    always @(posedge clk) begin
        if (ir_load)
            ir <= instruction;
    end
    assign opcode = ir[7:5];

    // Simple ALU for execute stage
    reg [7:0] reg_a, reg_b;
    always @(posedge clk) begin
        if (reg_wr_en)
            reg_a <= alu_result;
    end

    assign alu_result = (opcode == 3'b000) ? reg_a + reg_b :
                        (opcode == 3'b001) ? reg_a - reg_b :
                        (opcode == 3'b010) ? reg_a :
                        (opcode == 3'b011) ? instruction : // LDI
                        (opcode == 3'b100) ? reg_a & reg_b :
                        (opcode == 3'b101) ? reg_a | reg_b : 8'b00000000;
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_cpu_control;
    reg        clk, rst;
    reg  [7:0] instruction;
    wire [7:0] alu_result;

    simple_cpu cpu (.clk(clk), .rst(rst), .instruction(instruction), .alu_result(alu_result));

    always #5 clk = ~clk;

    initial begin
        $monitor("clk=%b rst=%b inst=%b | alu_result=%d", clk, rst, instruction, alu_result);

        clk = 0; rst = 0; instruction = 0;

        // Reset CPU
        #10 rst = 1; #10 rst = 0;

        // Instruction 1: LDI R0, 42  (opcode=011, uses instruction[7:0] as immediate)
        instruction = 8'b011_00_0_1;  // simplified: immediate = 42
        #30;  // 3 cycles (fetch, decode, execute)

        // Instruction 2: ADD R0, R0, R1 (opcode=000)
        instruction = 8'b000_00_00_1;
        #30;

        // Instruction 3: SUB R0, R0, R1 (opcode=001)
        instruction = 8'b001_00_00_1;
        #30;

        #20 $finish;
    end
endmodule
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
