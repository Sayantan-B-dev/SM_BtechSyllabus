# Implementing 8-bit Register design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 4  
**Date:** 17-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit shift register with left shift, right shift, and parallel load capabilities.
- Understand the concept of shifting data in sequential circuits.
- Simulate to verify all shift operations.

## Theory

**Shift Register:**
A shift register moves data bits left or right on each clock cycle. It can also be loaded in parallel with a new value.

**Operation Modes:**
- **Parallel Load (load = 1):** Load the full 8-bit value on the next clock edge.
- **Left Shift (load = 0, dir = 0):** Shift bits left; `q[0]` gets `ser_in`.
- **Right Shift (load = 0, dir = 1):** Shift bits right; `q[7]` gets `ser_in`.

## Verilog Code

```verilog
// 8-bit Shift Register with parallel load, left/right shift
module shift_reg_8bit (
    input  wire       clk,
    input  wire       rst,
    input  wire       load,        // 1 = parallel load, 0 = shift
    input  wire       dir,         // 0 = left shift, 1 = right shift
    input  wire       ser_in,      // serial input for shift
    input  wire [7:0] par_in,      // parallel input
    output reg  [7:0] q
);
    always @(posedge clk) begin
        if (rst)
            q <= 8'b00000000;
        else if (load)
            q <= par_in;
        else if (!dir) begin
            // Left shift
            q <= {q[6:0], ser_in};
        end else begin
            // Right shift
            q <= {ser_in, q[7:1]};
        end
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_shift_reg;
    reg        clk, rst, load, dir, ser_in;
    reg  [7:0] par_in;
    wire [7:0] q;

    shift_reg_8bit uut (.clk(clk), .rst(rst), .load(load), .dir(dir),
                        .ser_in(ser_in), .par_in(par_in), .q(q));

    always #5 clk = ~clk;

    initial begin
        $monitor("clk=%b rst=%b load=%b dir=%b ser=%b par=%d | q=%b ( %d )",
                 clk, rst, load, dir, ser_in, par_in, q, q);

        clk = 0; rst = 0; load = 0; dir = 0; ser_in = 0; par_in = 8'd0;

        // Reset
        #10 rst = 1; #10 rst = 0;

        // Parallel load: value 0b11001010 (202)
        #10 load = 1; par_in = 8'b11001010;
        #10 load = 0;

        // Left shift with ser_in=1
        #10 dir = 0; ser_in = 1; // shift left, LSB gets 1
        #10;
        #10 ser_in = 0;          // shift left, LSB gets 0
        #10;

        // Right shift with ser_in=1
        #10 dir = 1; ser_in = 1; // shift right, MSB gets 1
        #10;

        // Load new value
        #10 load = 1; par_in = 8'b00001111;
        #10 load = 0;

        // Shift right with ser_in=0
        #10 dir = 1; ser_in = 0;
        #10;

        #20 $finish;
    end
endmodule
```

## Expected Output / Waveform

```
clk=0 rst=1 load=0 dir=0 ser=0 par=0   | q=00000000 (0)
clk=1 rst=1 load=0 dir=0 ser=0 par=0   | q=00000000 (0) -- reset
clk=1 rst=0 load=1 dir=0 ser=0 par=202 | q=11001010 (202) -- loaded
clk=0 rst=0 load=0 dir=0 ser=1 par=202 | q=11001010 (202)
clk=1 rst=0 load=0 dir=0 ser=1 par=202 | q=10010101 (149) -- left shift with 1
clk=1 rst=0 load=0 dir=0 ser=0 par=202 | q=00101010 (42)  -- left shift with 0
clk=1 rst=0 load=0 dir=1 ser=1 par=202 | q=10010101 (149) -- right shift with 1
clk=1 rst=0 load=1 dir=1 ser=0 par=15  | q=00001111 (15)  -- loaded
clk=1 rst=0 load=0 dir=1 ser=0 par=15  | q=00000111 (7)   -- right shift with 0
```

## Conclusion

Designed an 8-bit shift register supporting parallel load, left shift, and right shift operations. The simulation verifies correct shifting behavior and data retention based on the control signals.
