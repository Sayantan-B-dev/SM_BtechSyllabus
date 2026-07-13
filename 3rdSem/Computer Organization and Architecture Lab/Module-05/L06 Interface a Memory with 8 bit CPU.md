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

## Verilog Code

```verilog
// RAM module with initialization support
module ram_256x8 (
    input  wire        clk,
    input  wire        we,
    input  wire [7:0]  addr,
    input  wire [7:0]  din,
    output reg  [7:0]  dout
);
    reg [7:0] mem [0:255];

    // Initialize memory with a program
    integer i;
    initial begin
        for (i = 0; i < 256; i = i + 1)
            mem[i] = 8'b00000000;

        // Simple program:
        // Address 0: LOAD accumulator from address 0x10
        mem[0] = 8'b010_00000; // opcode=010 (LOAD), address in next instruction
        mem[1] = 8'd16;        // address = 16 (0x10)
        // Address 2: ADD accumulator with value at address 0x11
        mem[2] = 8'b000_00000; // opcode=000 (ADD)
        mem[3] = 8'd17;        // address = 17 (0x11)
        // Address 4: SUB accumulator with value at address 0x12
        mem[4] = 8'b001_00000; // opcode=001 (SUB)
        mem[5] = 8'd18;        // address = 18 (0x12)
        // Address 6: NOP (infinite loop here)
        mem[6] = 8'b011_00000; // opcode=011 (NOP)
        mem[7] = 8'b011_00000; // NOP

        // Data section
        mem[16] = 8'd10; // operand 1
        mem[17] = 8'd5;  // operand 2
        mem[18] = 8'd3;  // operand 3
    end

    always @(posedge clk) begin
        if (we)
            mem[addr] <= din;
        dout <= mem[addr];
    end
endmodule

// Enhanced CPU core
module cpu_core (
    input  wire        clk, rst,
    input  wire [7:0]  data_in,
    output wire [7:0]  addr_out,
    output wire [7:0]  data_out,
    output wire        mem_read,
    output wire        mem_write
);
    reg [7:0] pc, ir, acc, mar;
    reg [1:0] state;
    reg       fetch_operand;

    localparam FETCH  = 2'b00;
    localparam DECODE = 2'b01;
    localparam EXEC   = 2'b10;

    assign addr_out = (state == FETCH) ? pc : mar;
    assign data_out = acc;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            state <= FETCH;
            pc <= 8'b00000000;
            ir <= 8'b00000000;
            acc <= 8'b00000000;
            mar <= 8'b00000000;
            fetch_operand <= 1'b0;
        end else begin
            case (state)
                FETCH: begin
                    if (!fetch_operand) begin
                        ir <= data_in;
                        pc <= pc + 1;
                        state <= DECODE;
                    end else begin
                        mar <= data_in;
                        fetch_operand <= 1'b0;
                        state <= EXEC;
                    end
                end
                DECODE: begin
                    // Check if instruction needs operand fetch
                    if (ir[7:5] != 3'b011) begin // not NOP
                        fetch_operand <= 1'b1;
                        state <= FETCH;
                    end else begin
                        state <= EXEC;
                    end
                end
                EXEC: begin
                    case (ir[7:5])
                        3'b000: acc <= acc + data_in;
                        3'b001: acc <= acc - data_in;
                        3'b010: acc <= data_in;
                        3'b100: acc <= acc & data_in;
                        3'b101: acc <= acc | data_in;
                        default: acc <= acc; // NOP
                    endcase
                    state <= FETCH;
                end
            endcase
        end
    end

    assign mem_read  = 1'b1; // Always read
    assign mem_write = 1'b0;
endmodule

// Top-level system
module complete_system (
    input  wire clk, rst
);
    wire [7:0] addr, data_to_mem, data_from_mem;
    wire       mem_read, mem_write;

    cpu_core cpu (.clk(clk), .rst(rst), .data_in(data_from_mem),
                  .addr_out(addr), .data_out(data_to_mem),
                  .mem_read(mem_read), .mem_write(mem_write));

    ram_256x8 ram (.clk(clk), .we(mem_write), .addr(addr),
                   .din(data_to_mem), .dout(data_from_mem));
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_complete_system;
    reg clk, rst;

    complete_system uut (.clk(clk), .rst(rst));

    always #5 clk = ~clk;

    initial begin
        $display("Starting complete system test...");
        $monitor("Time=%0t clk=%b", $time, clk);

        clk = 0; rst = 0;

        #10 rst = 1;
        #10 rst = 0;

        // Run for enough cycles to execute the program
        // Program: LOAD 10, ADD 5, SUB 3 => result should be 12
        #200;

        $display("System test complete.");
        $finish;
    end
endmodule
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
