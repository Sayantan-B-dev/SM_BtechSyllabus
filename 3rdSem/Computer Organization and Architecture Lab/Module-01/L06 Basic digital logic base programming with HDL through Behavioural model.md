# Basic digital logic base programming with HDL through Behavioural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 6  
**Date:** 23-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 3:8 decoder using behavioral modeling.
- Design an 8:3 encoder using behavioral modeling.
- Verify both circuits through exhaustive simulation.

## Theory

**Decoder:**
A decoder converts n-bit input to 2^n-bit output. For a 3:8 decoder:
- Input: A[2:0] (3-bit binary)
- Output: Y[7:0] (one-hot -- exactly one output is 1)
- For input 3'b000, Y[0]=1; for 3'b001, Y[1]=1; ...; for 3'b111, Y[7]=1.

**Encoder:**
An encoder performs the reverse operation. For an 8:3 encoder:
- Input: D[7:0] (one-hot)
- Output: Q[2:0] (3-bit binary)
- For D[0]=1, Q=000; for D[1]=1, Q=001; ...; for D[7]=1, Q=111.

## Truth Table

**3:8 Decoder:**
| A2 | A1 | A0 | Y7 | Y6 | Y5 | Y4 | Y3 | Y2 | Y1 | Y0 |
|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 1  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1  | 0  | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 1  | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |

**8:3 Encoder:**
| D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | Q2 | Q1 | Q0 |
|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 1  |
| 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  |

## Verilog Code

```verilog
// 3:8 Decoder using behavioral modeling
module decoder_3to8 (
    input  wire [2:0] a,
    output reg  [7:0] y
);
    always @(*) begin
        case (a)
            3'b000: y = 8'b00000001;
            3'b001: y = 8'b00000010;
            3'b010: y = 8'b00000100;
            3'b011: y = 8'b00001000;
            3'b100: y = 8'b00010000;
            3'b101: y = 8'b00100000;
            3'b110: y = 8'b01000000;
            3'b111: y = 8'b10000000;
            default: y = 8'b00000000;
        endcase
    end
endmodule

// 8:3 Encoder using behavioral modeling
module encoder_8to3 (
    input  wire [7:0] d,
    output reg  [2:0] q
);
    always @(*) begin
        case (d)
            8'b00000001: q = 3'b000;
            8'b00000010: q = 3'b001;
            8'b00000100: q = 3'b010;
            8'b00001000: q = 3'b011;
            8'b00010000: q = 3'b100;
            8'b00100000: q = 3'b101;
            8'b01000000: q = 3'b110;
            8'b10000000: q = 3'b111;
            default:     q = 3'b000;
        endcase
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_dec_enc;
    reg  [2:0] a;
    wire [7:0] y;
    reg  [7:0] d;
    wire [2:0] q;

    decoder_3to8 dec (.a(a), .y(y));
    encoder_8to3 enc (.d(d), .q(q));

    initial begin
        $display("=== 3:8 Decoder ===");
        $monitor("a=%b | y=%b", a, y);

        a = 3'b000; #10;
        a = 3'b001; #10;
        a = 3'b010; #10;
        a = 3'b011; #10;
        a = 3'b100; #10;
        a = 3'b101; #10;
        a = 3'b110; #10;
        a = 3'b111; #10;

        #20;

        $display("=== 8:3 Encoder ===");
        d = 8'b00000001; #10;
        d = 8'b00000010; #10;
        d = 8'b00000100; #10;
        d = 8'b00001000; #10;
        d = 8'b00010000; #10;
        d = 8'b00100000; #10;
        d = 8'b01000000; #10;
        d = 8'b10000000; #10;

        $finish;
    end

    // Separate monitor for encoder
    always @(d) begin
        #1 $display("d=%b | q=%b", d, q);
    end
endmodule
```

## Expected Output / Waveform

```
=== 3:8 Decoder ===
a=000 | y=00000001
a=001 | y=00000010
a=010 | y=00000100
a=011 | y=00001000
a=100 | y=00010000
a=101 | y=00100000
a=110 | y=01000000
a=111 | y=10000000

=== 8:3 Encoder ===
d=00000001 | q=000
d=00000010 | q=001
d=00000100 | q=010
d=00001000 | q=011
d=00010000 | q=100
d=00100000 | q=101
d=01000000 | q=110
d=10000000 | q=111
```

## Conclusion

Successfully implemented a 3:8 decoder and an 8:3 encoder using behavioral modeling with the `case` statement. The decoder produces a one-hot output, while the encoder generates the corresponding binary code from a one-hot input.
