# Implementing Multiplexer (MUX) and De Multiplexer with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 3  
**Date:** 27-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 4:1 multiplexer and 8:1 multiplexer using behavioral modeling.
- Design a 1:4 demultiplexer using behavioral modeling.
- Simulate and verify all circuits.

## Theory

**Multiplexer (MUX):**
A multiplexer selects one of many input signals and forwards it to a single output line based on select lines.
- 4:1 MUX: 4 data inputs, 2 select lines, 1 output
- 8:1 MUX: 8 data inputs, 3 select lines, 1 output

**Demultiplexer (DEMUX):**
A demultiplexer takes a single input and routes it to one of several output lines based on select lines.
- 1:4 DEMUX: 1 data input, 2 select lines, 4 outputs

## Truth Table

**4:1 MUX:**
| s1 | s0 |  y  |
|----|----|-----|
| 0  | 0  | i0  |
| 0  | 1  | i1  |
| 1  | 0  | i2  |
| 1  | 1  | i3  |

**8:1 MUX:**
| s2 | s1 | s0 |  y  |
|----|----|----|-----|
| 0  | 0  | 0  | i0  |
| 0  | 0  | 1  | i1  |
| 0  | 1  | 0  | i2  |
| 0  | 1  | 1  | i3  |
| 1  | 0  | 0  | i4  |
| 1  | 0  | 1  | i5  |
| 1  | 1  | 0  | i6  |
| 1  | 1  | 1  | i7  |

**1:4 DEMUX:**
| s1 | s0 | y3 | y2 | y1 | y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | d  |
| 0  | 1  | 0  | 0  | d  | 0  |
| 1  | 0  | 0  | d  | 0  | 0  |
| 1  | 1  | d  | 0  | 0  | 0  |

## Verilog Code

```verilog
// 4:1 Multiplexer using case
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

// 8:1 Multiplexer using case
module mux_8to1 (
    input  wire [7:0] i,
    input  wire [2:0] sel,
    output reg        y
);
    always @(*) begin
        case (sel)
            3'b000: y = i[0];
            3'b001: y = i[1];
            3'b010: y = i[2];
            3'b011: y = i[3];
            3'b100: y = i[4];
            3'b101: y = i[5];
            3'b110: y = i[6];
            3'b111: y = i[7];
            default: y = 1'b0;
        endcase
    end
endmodule

// 1:4 Demultiplexer
module demux_1to4 (
    input  wire       d,
    input  wire [1:0] sel,
    output reg  [3:0] y
);
    always @(*) begin
        y = 4'b0000;
        case (sel)
            2'b00: y[0] = d;
            2'b01: y[1] = d;
            2'b10: y[2] = d;
            2'b11: y[3] = d;
        endcase
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_mux_demux;
    reg  [3:0] i4;
    reg  [1:0] sel4;
    wire       y4;

    reg  [7:0] i8;
    reg  [2:0] sel8;
    wire       y8;

    reg        d;
    reg  [1:0] sel_d;
    wire [3:0] y_d;

    mux_4to1   mux4 (.i(i4),   .sel(sel4), .y(y4));
    mux_8to1   mux8 (.i(i8),   .sel(sel8), .y(y8));
    demux_1to4 demux (.d(d), .sel(sel_d), .y(y_d));

    initial begin
        $display("=== 4:1 MUX ===");
        i4 = 4'b1010;
        sel4 = 2'b00; #10 $display("sel=%b i=%b | y=%b", sel4, i4, y4);
        sel4 = 2'b01; #10 $display("sel=%b i=%b | y=%b", sel4, i4, y4);
        sel4 = 2'b10; #10 $display("sel=%b i=%b | y=%b", sel4, i4, y4);
        sel4 = 2'b11; #10 $display("sel=%b i=%b | y=%b", sel4, i4, y4);

        $display("=== 8:1 MUX ===");
        i8 = 8'b10101010;
        for (sel8 = 0; sel8 < 8; sel8 = sel8 + 1) begin
            #10 $display("sel=%b i=%b | y=%b", sel8, i8, y8);
        end

        $display("=== 1:4 DEMUX ===");
        d = 1'b1;
        sel_d = 2'b00; #10 $display("sel=%b d=%b | y=%b", sel_d, d, y_d);
        sel_d = 2'b01; #10 $display("sel=%b d=%b | y=%b", sel_d, d, y_d);
        sel_d = 2'b10; #10 $display("sel=%b d=%b | y=%b", sel_d, d, y_d);
        sel_d = 2'b11; #10 $display("sel=%b d=%b | y=%b", sel_d, d, y_d);

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
=== 4:1 MUX ===
sel=00 i=1010 | y=0
sel=01 i=1010 | y=1
sel=10 i=1010 | y=0
sel=11 i=1010 | y=1
=== 8:1 MUX ===
sel=000 i=10101010 | y=0
sel=001 i=10101010 | y=1
sel=010 i=10101010 | y=0
sel=011 i=10101010 | y=1
sel=100 i=10101010 | y=0
sel=101 i=10101010 | y=1
sel=110 i=10101010 | y=0
sel=111 i=10101010 | y=1
=== 1:4 DEMUX ===
sel=00 d=1 | y=0001
sel=01 d=1 | y=0010
sel=10 d=1 | y=0100
sel=11 d=1 | y=1000
```

## Conclusion

Successfully implemented 4:1 MUX, 8:1 MUX, and 1:4 DEMUX using behavioral modeling. The MUX correctly selects inputs based on select lines, and the DEMUX routes the input to the correct output.
