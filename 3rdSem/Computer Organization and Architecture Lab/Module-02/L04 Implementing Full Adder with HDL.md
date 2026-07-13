# Implementing Full Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 4  
**Date:** 06-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a full subtractor using Verilog.
- Understand the borrow logic in multi-bit subtraction.
- Verify the full subtractor truth table through exhaustive simulation.

## Theory

**Full Subtractor:**
A full subtractor performs subtraction of three single-bit inputs: A (minuend), B (subtrahend), and Bin (borrow-in). It produces:
- Difference (D) = A xor B xor Bin
- Borrow-out (Bout) = (~A & B) | (~A & Bin) | (B & Bin)
- Simplified: Bout = (~A & (B | Bin)) | (B & Bin)

The borrow-out indicates whether the subtraction of the current bit position requires a borrow from the next higher bit.

## Truth Table

| A | B | Bin | Diff | Bout |
|---|---|-----|------|------|
| 0 | 0 |  0  |  0   |  0   |
| 0 | 0 |  1  |  1   |  1   |
| 0 | 1 |  0  |  1   |  1   |
| 0 | 1 |  1  |  0   |  1   |
| 1 | 0 |  0  |  1   |  0   |
| 1 | 0 |  1  |  0   |  0   |
| 1 | 1 |  0  |  0   |  0   |
| 1 | 1 |  1  |  1   |  1   |

## Verilog Code

```verilog
// Full Subtractor -- Behavioral
module full_subtractor_beh (
    input  wire a, b, bin,
    output reg  diff, bout
);
    always @(*) begin
        diff = a ^ b ^ bin;
        bout = (~a & b) | (~a & bin) | (b & bin);
    end
endmodule

// Full Subtractor -- Structural using half subtractors
module half_subtractor (
    input  wire a, b,
    output wire diff, borrow
);
    assign diff  = a ^ b;
    assign borrow = ~a & b;
endmodule

module full_subtractor_str (
    input  wire a, b, bin,
    output wire diff, bout
);
    wire d1, b1, b2;
    half_subtractor hs1 (.a(a), .b(b),       .diff(d1), .borrow(b1));
    half_subtractor hs2 (.a(d1), .b(bin),    .diff(diff), .borrow(b2));
    or u1 (bout, b1, b2);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_full_subtractor;
    reg  a, b, bin;
    wire diff, bout;

    full_subtractor_beh uut (.a(a), .b(b), .bin(bin), .diff(diff), .bout(bout));

    initial begin
        $monitor("A=%b B=%b Bin=%b | Diff=%b Bout=%b", a, b, bin, diff, bout);

        {a, b, bin} = 3'b000; #10;
        {a, b, bin} = 3'b001; #10;
        {a, b, bin} = 3'b010; #10;
        {a, b, bin} = 3'b011; #10;
        {a, b, bin} = 3'b100; #10;
        {a, b, bin} = 3'b101; #10;
        {a, b, bin} = 3'b110; #10;
        {a, b, bin} = 3'b111; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=0 B=0 Bin=0 | Diff=0 Bout=0
A=0 B=0 Bin=1 | Diff=1 Bout=1
A=0 B=1 Bin=0 | Diff=1 Bout=1
A=0 B=1 Bin=1 | Diff=0 Bout=1
A=1 B=0 Bin=0 | Diff=1 Bout=0
A=1 B=0 Bin=1 | Diff=0 Bout=0
A=1 B=1 Bin=0 | Diff=0 Bout=0
A=1 B=1 Bin=1 | Diff=1 Bout=1
```

## Conclusion

Implemented a full subtractor using both behavioral and structural modeling. The borrow-out logic correctly handles the cases where A < (B + Bin).
