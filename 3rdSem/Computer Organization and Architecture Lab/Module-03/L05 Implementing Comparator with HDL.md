# Implementing Comparator with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 5  
**Date:** 03-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 1-bit comparator with three outputs: A > B, A = B, A < B.
- Design a 4-bit comparator using hierarchical design.
- Simulate and verify the comparator functionality.

## Theory

**Comparator:**
A digital comparator compares two binary numbers and produces outputs indicating their relative magnitude.

**1-bit Comparator:**
For two single-bit inputs A and B:
- A_gt_B = A & ~B
- A_eq_B = ~(A ^ B) = A xnor B
- A_lt_B = ~A & B

**4-bit Comparator (Hierarchical):**
A 4-bit comparator compares two 4-bit numbers A[3:0] and B[3:0]. The comparison starts from the most significant bit (MSB). If the MSBs differ, the result is determined immediately. If they are equal, the next lower bits are compared.

## Truth Table (1-bit)

| A | B | A>B | A=B | A<B |
|---|---|-----|-----|-----|
| 0 | 0 |  0  |  1  |  0  |
| 0 | 1 |  0  |  0  |  1  |
| 1 | 0 |  1  |  0  |  0  |
| 1 | 1 |  0  |  1  |  0  |

## Verilog Code

```verilog
// 1-bit Comparator
module comp_1bit (
    input  wire a, b,
    output wire a_gt_b,
    output wire a_eq_b,
    output wire a_lt_b
);
    assign a_gt_b = a & ~b;
    assign a_eq_b = ~(a ^ b);
    assign a_lt_b = ~a & b;
endmodule

// 4-bit Comparator using hierarchical design
module comp_4bit (
    input  wire [3:0] a, b,
    output wire       a_gt_b,
    output wire       a_eq_b,
    output wire       a_lt_b
);
    wire [3:0] gt, eq, lt;

    // Instantiate 1-bit comparators for each bit
    comp_1bit c0 (.a(a[0]), .b(b[0]), .a_gt_b(gt[0]), .a_eq_b(eq[0]), .a_lt_b(lt[0]));
    comp_1bit c1 (.a(a[1]), .b(b[1]), .a_gt_b(gt[1]), .a_eq_b(eq[1]), .a_lt_b(lt[1]));
    comp_1bit c2 (.a(a[2]), .b(b[2]), .a_gt_b(gt[2]), .a_eq_b(eq[2]), .a_lt_b(lt[2]));
    comp_1bit c3 (.a(a[3]), .b(b[3]), .a_gt_b(gt[3]), .a_eq_b(eq[3]), .a_lt_b(lt[3]));

    // Combine results: check from MSB to LSB
    assign a_gt_b = gt[3] | (eq[3] & gt[2]) | (eq[3] & eq[2] & gt[1]) | (eq[3] & eq[2] & eq[1] & gt[0]);
    assign a_lt_b = lt[3] | (eq[3] & lt[2]) | (eq[3] & eq[2] & lt[1]) | (eq[3] & eq[2] & eq[1] & lt[0]);
    assign a_eq_b = eq[3] & eq[2] & eq[1] & eq[0];
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_comp_4bit;
    reg  [3:0] a, b;
    wire       a_gt_b, a_eq_b, a_lt_b;

    comp_4bit uut (.a(a), .b(b), .a_gt_b(a_gt_b), .a_eq_b(a_eq_b), .a_lt_b(a_lt_b));

    initial begin
        $monitor("A=%d B=%d | A>B=%b A=B=%b A<B=%b", a, b, a_gt_b, a_eq_b, a_lt_b);

        a = 4'd10; b = 4'd5;  #10;  // A > B
        a = 4'd5;  b = 4'd10; #10;  // A < B
        a = 4'd7;  b = 4'd7;  #10;  // A = B
        a = 4'd15; b = 4'd0;  #10;  // A > B
        a = 4'd0;  b = 4'd15; #10;  // A < B
        a = 4'd8;  b = 4'd9;  #10;  // A < B

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=10 B=5 | A>B=1 A=B=0 A<B=0
A=5 B=10 | A>B=0 A=B=0 A<B=1
A=7 B=7 | A>B=0 A=B=1 A<B=0
A=15 B=0 | A>B=1 A=B=0 A<B=0
A=0 B=15 | A>B=0 A=B=0 A<B=1
A=8 B=9 | A>B=0 A=B=0 A<B=1
```

## Conclusion

Designed a 1-bit comparator and extended it to a 4-bit comparator using hierarchical design. The comparator correctly determines the relationship between two 4-bit numbers by checking bits from MSB to LSB.
