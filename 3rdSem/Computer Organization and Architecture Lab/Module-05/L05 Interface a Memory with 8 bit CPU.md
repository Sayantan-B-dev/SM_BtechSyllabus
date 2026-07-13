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

## Verilog Code

```verilog
// RAM module
module ram_256x8 (
    input  wire        clk,
    input  wire        we,
    input  wire [7:0]  addr,
    input  wire [7:0]  din,
    output reg  [7:0]  dout
);
    reg [7:0] mem [0:255];

    always @(posedge clk) begin
        if (we)
            mem[addr] <= din;
        dout <= mem[addr];
    end
endmodule

// CPU core with memory interface
module cpu_core (
    input  wire        clk, rst,
    input  wire [7:0]  data_in,
    output wire [7:0]  addr_out,
    output wire [7:0]  data_out,
    output wire        mem_read,
    output wire        mem_write
);
    reg [7:0] pc, ir, acc;
    reg [1:0] state;

    localparam FETCH  = 2'b00;
    localparam DECODE = 2'b01;
    localparam EXEC   = 2'b10;

    assign addr_out = (state == FETCH) ? pc : 8'b00000000;
    assign data_out = acc;

    // FSM
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            state <= FETCH;
            pc <= 8'b00000000;
            ir <= 8'b00000000;
            acc <= 8'b00000000;
        end else begin
            case (state)
                FETCH: begin
                    ir <= data_in;
                    state <= DECODE;
                end
                DECODE: begin
                    state <= EXEC;
                end
                EXEC: begin
                    pc <= pc + 1;
                    // Simple execution
                    case (ir[7:5])
                        3'b000: acc <= acc + data_in;  // ADD
                        3'b001: acc <= acc - data_in;  // SUB
                        3'b010: acc <= data_in;        // LOAD
                        3'b011: acc <= acc;            // NOP
                        3'b100: acc <= acc & data_in;  // AND
                        3'b101: acc <= acc | data_in;  // OR
                        default: acc <= acc;
                    endcase
                    state <= FETCH;
                end
            endcase
        end
    end

    assign mem_read  = (state == FETCH) || (state == EXEC && ir[7:5] != 3'b011);
    assign mem_write = 1'b0; // No write in this simple core
endmodule

// Top-level CPU + Memory
module cpu_with_memory (
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

module tb_cpu_memory;
    reg  clk, rst;

    cpu_with_memory uut (.clk(clk), .rst(rst));

    always #5 clk = ~clk;

    initial begin
        $monitor("clk=%b rst=%b", clk, rst);

        clk = 0; rst = 0;

        #10 rst = 1;  // Reset CPU
        #10 rst = 0;

        // Run for several clock cycles
        #100;

        $finish;
    end
endmodule
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
