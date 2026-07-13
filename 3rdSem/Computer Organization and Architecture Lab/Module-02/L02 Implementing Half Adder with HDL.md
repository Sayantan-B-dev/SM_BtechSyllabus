# Implementing Half Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 2  
**Date:** 30-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a half subtractor using Verilog.
- Understand the difference between half adder and half subtractor.
- Verify the half subtractor truth table through simulation.

## Theory

**Half Subtractor:**
A half subtractor subtracts one single-bit binary number (B) from another (A). It produces two outputs:
- Difference (D) = A xor B
- Borrow-out (B_out) = (not A) and B

When A < B, a borrow is needed, so B_out = 1.

## Truth Table

| A | B | Difference (D) | Borrow-out (B_out) |
|---|---|----------------|--------------------|
| 0 | 0 |       0        |         0          |
| 0 | 1 |       1        |         1          |
| 1 | 0 |       1        |         0          |
| 1 | 1 |       0        |         0          |

## Verilog Code

```verilog
// Half Subtractor -- Dataflow
module half_subtractor_df (
    input  wire a, b,
    output wire diff, borrow
);
    assign diff  = a ^ b;
    assign borrow = ~a & b;
endmodule

// Half Subtractor -- Structural
module half_subtractor_st (
    input  wire a, b,
    output wire diff, borrow
);
    xor u1 (diff, a, b);
    and u2 (borrow_int, ~a, b); // not supported directly; use dataflow for structural with NOT
    // Structural version needs a NOT gate:
endmodule

// Alternative structural with NOT gate primitive
module half_subtractor_st2 (
    input  wire a, b,
    output wire diff, borrow
);
    wire not_a;
    not u1 (not_a, a);
    xor u2 (diff, a, b);
    and u3 (borrow, not_a, b);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_half_subtractor;
    reg  a, b;
    wire diff, borrow;

    half_subtractor_df uut (.a(a), .b(b), .diff(diff), .borrow(borrow));

    initial begin
        $monitor("A=%b B=%b | Diff=%b Borrow=%b", a, b, diff, borrow);

        a = 0; b = 0; #10;
        a = 0; b = 1; #10;
        a = 1; b = 0; #10;
        a = 1; b = 1; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=0 B=0 | Diff=0 Borrow=0
A=0 B=1 | Diff=1 Borrow=1
A=1 B=0 | Diff=1 Borrow=0
A=1 B=1 | Diff=0 Borrow=0
```

## Conclusion

Implemented a half subtractor using dataflow and structural modeling. The borrow output is 1 only when A=0 and B=1, correctly indicating that a borrow is needed.
