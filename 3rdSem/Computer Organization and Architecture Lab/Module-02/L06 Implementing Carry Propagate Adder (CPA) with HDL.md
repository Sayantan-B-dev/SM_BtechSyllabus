# Implementing Carry Propagate Adder (CPA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 6  
**Date:** 13-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 4-bit ripple carry adder/subtractor using XOR gates for 2's complement.
- Implement a control signal (Add/Sub) that selects between addition and subtraction.
- Verify through simulation with both addition and subtraction operations.

## Theory

**Add/Subtract Control using 2's Complement:**
To perform subtraction (A - B) using adder hardware, we take the 2's complement of B:
1. Invert all bits of B (using XOR gates with the control signal).
2. Set the carry-in (Cin) equal to the control signal (1 for subtract, 0 for add).

When `sub = 1`:
- B gets XORed with 1 to produce bitwise NOT.
- Cin = 1, so the adder computes A + (~B) + 1 = A - B.

**Circuit:**
```
sub = 0: B XOR 0 = B, Cin = 0  => A + B
sub = 1: B XOR 1 = ~B, Cin = 1 => A + (~B) + 1 = A - B
```

## Truth Table

| sub | Operation     |
|-----|---------------|
|  0  | A + B         |
|  1  | A - B         |

## Verilog Code

```verilog
// Full Adder module
module full_adder (
    input  wire a, b, cin,
    output wire sum, cout
);
    assign {cout, sum} = a + b + cin;
endmodule

// 4-bit Ripple Carry Adder/Subtractor
module add_sub_4bit (
    input  wire [3:0] a, b,
    input  wire       sub,        // 0 = add, 1 = subtract
    output wire [3:0] result,
    output wire       cout,
    output wire       overflow
);
    wire [3:0] b_xor;
    wire c1, c2, c3;

    // XOR gates to conditionally invert B
    assign b_xor[0] = b[0] ^ sub;
    assign b_xor[1] = b[1] ^ sub;
    assign b_xor[2] = b[2] ^ sub;
    assign b_xor[3] = b[3] ^ sub;

    full_adder fa0 (.a(a[0]), .b(b_xor[0]), .cin(sub),    .sum(result[0]), .cout(c1));
    full_adder fa1 (.a(a[1]), .b(b_xor[1]), .cin(c1),     .sum(result[1]), .cout(c2));
    full_adder fa2 (.a(a[2]), .b(b_xor[2]), .cin(c2),     .sum(result[2]), .cout(c3));
    full_adder fa3 (.a(a[3]), .b(b_xor[3]), .cin(c3),     .sum(result[3]), .cout(cout));

    // Overflow detection: XOR of carry-in and carry-out of MSB
    assign overflow = c3 ^ cout;
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_add_sub;
    reg  [3:0] a, b;
    reg        sub;
    wire [3:0] result;
    wire       cout, overflow;

    add_sub_4bit uut (.a(a), .b(b), .sub(sub), .result(result),
                      .cout(cout), .overflow(overflow));

    initial begin
        $monitor("sub=%b A=%d B=%d | Result=%d Cout=%b Overflow=%b",
                 sub, a, b, result, cout, overflow);

        // Addition tests
        sub = 0;
        a = 4'd5;  b = 4'd3;  #10;  // 5 + 3 = 8
        a = 4'd12; b = 4'd7;  #10;  // 12 + 7 = 19
        a = 4'd10; b = 4'd10; #10;  // 10 + 10 = 20 (overflow in 4-bit signed)

        // Subtraction tests
        sub = 1;
        a = 4'd8;  b = 4'd3;  #10;  // 8 - 3 = 5
        a = 4'd10; b = 4'd12; #10;  // 10 - 12 = -2 (2's complement)
        a = 4'd7;  b = 4'd7;  #10;  // 7 - 7 = 0

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
sub=0 A=5 B=3 | Result=8  Cout=0 Overflow=0
sub=0 A=12 B=7 | Result=19 Cout=0 Overflow=0
sub=0 A=10 B=10 | Result=4  Cout=1 Overflow=1
sub=1 A=8 B=3 | Result=5  Cout=0 Overflow=0
sub=1 A=10 B=12 | Result=14 Cout=1 Overflow=0
sub=1 A=7 B=7 | Result=0  Cout=0 Overflow=0
```

## Conclusion

Designed a 4-bit adder/subtractor using XOR gates for 2's complement conversion. The `sub` control signal successfully toggles between addition and subtraction operations.
