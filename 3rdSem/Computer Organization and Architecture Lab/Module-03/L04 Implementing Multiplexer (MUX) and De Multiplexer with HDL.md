# Implementing Multiplexer (MUX) and De Multiplexer with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 4  
**Date:** 27-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 16:1 multiplexer using hierarchical composition of 4:1 MUX modules.
- Understand how larger multiplexers can be built from smaller ones.
- Simulate and verify the 16:1 MUX.

## Theory

**Hierarchical MUX Design:**
A 16:1 MUX requires 16 data inputs and 4 select lines (s[3:0]). It can be built using:
- Stage 1: Four 4:1 MUX units, each handling 4 inputs. The lower select bits (s[1:0]) select within each group.
- Stage 2: One 4:1 MUX that selects among the outputs of the four Stage-1 MUXes, using the upper select bits (s[3:2]).

**Block Diagram:**
```
i[3:0]   i[7:4]   i[11:8]  i[15:12]
   |        |         |         |
 MUX_0    MUX_1     MUX_2     MUX_3
(4:1)    (4:1)     (4:1)     (4:1)
   |        |         |         |
   +--------+---------+---------+
                    |
                 MUX_4 (4:1)
                    |
                    y
              s[3:2] (select)
```

## Verilog Code

```verilog
// 4:1 MUX building block
module mux_4to1 (
    input  wire [3:0] i,
    input  wire [1:0] sel,
    output reg        y
);
    always @(*) begin
        case (sel)
            2'b00: y = i[0];
            2'b01: y = i[1];
            2'b10: y = i[2];
            2'b11: y = i[3];
            default: y = 1'b0;
        endcase
    end
endmodule

// 16:1 MUX using hierarchical design
module mux_16to1 (
    input  wire [15:0] i,
    input  wire [3:0]  sel,
    output wire        y
);
    wire [3:0] mux_out;

    // Stage 1: Four 4:1 MUXes
    mux_4to1 m0 (.i(i[3:0]),    .sel(sel[1:0]), .y(mux_out[0]));
    mux_4to1 m1 (.i(i[7:4]),    .sel(sel[1:0]), .y(mux_out[1]));
    mux_4to1 m2 (.i(i[11:8]),   .sel(sel[1:0]), .y(mux_out[2]));
    mux_4to1 m3 (.i(i[15:12]),  .sel(sel[1:0]), .y(mux_out[3]));

    // Stage 2: Final 4:1 MUX
    mux_4to1 m_final (.i(mux_out), .sel(sel[3:2]), .y(y));
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_mux_16to1;
    reg  [15:0] i;
    reg  [3:0]  sel;
    wire        y;

    mux_16to1 uut (.i(i), .sel(sel), .y(y));

    initial begin
        $monitor("sel=%b i=%b | y=%b", sel, i, y);

        // Assign a pattern: each group has a unique bit high
        i = 16'b0001_0010_0100_1000; // group pattern

        // Test all select combinations
        sel = 4'b0000; #10;  // expect i[0] = 0
        sel = 4'b0001; #10;  // expect i[1] = 0
        sel = 4'b0010; #10;  // expect i[2] = 1
        sel = 4'b0011; #10;  // expect i[3] = 0
        sel = 4'b0100; #10;  // expect i[4] = 0
        sel = 4'b0101; #10;  // expect i[5] = 1
        sel = 4'b0110; #10;  // expect i[6] = 0
        sel = 4'b0111; #10;  // expect i[7] = 0
        sel = 4'b1000; #10;  // expect i[8] = 0
        sel = 4'b1001; #10;  // expect i[9] = 0
        sel = 4'b1010; #10;  // expect i[10] = 1
        sel = 4'b1011; #10;  // expect i[11] = 0
        sel = 4'b1100; #10;  // expect i[12] = 0
        sel = 4'b1101; #10;  // expect i[13] = 0
        sel = 4'b1110; #10;  // expect i[14] = 0
        sel = 4'b1111; #10;  // expect i[15] = 1

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
sel=0000 i=0001001001001000 | y=0
sel=0001 i=0001001001001000 | y=0
sel=0010 i=0001001001001000 | y=1
sel=0011 i=0001001001001000 | y=0
sel=0100 i=0001001001001000 | y=0
sel=0101 i=0001001001001000 | y=1
sel=0110 i=0001001001001000 | y=0
sel=0111 i=0001001001001000 | y=0
sel=1000 i=0001001001001000 | y=0
sel=1001 i=0001001001001000 | y=0
sel=1010 i=0001001001001000 | y=1
sel=1011 i=0001001001001000 | y=0
sel=1100 i=0001001001001000 | y=0
sel=1101 i=0001001001001000 | y=0
sel=1110 i=0001001001001000 | y=0
sel=1111 i=0001001001001000 | y=1
```

## Conclusion

Designed a 16:1 MUX using five 4:1 MUX modules in a two-stage hierarchical structure. This demonstrates how larger multiplexers can be efficiently constructed from smaller building blocks.
