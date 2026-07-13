# Implementing Full Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 3  
**Date:** 06-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a full adder using structural and behavioral modeling in Verilog.
- Derive and verify the logical expressions for Sum and Carry-out.
- Test exhaustively for all 8 input combinations.

## Theory

**Full Adder:**
A full adder adds three single-bit inputs: A, B, and Carry-in (Cin). It produces:
- Sum = A xor B xor Cin
- Cout = (A & B) | (Cin & (A xor B))

**Behavioral Modeling:**
Using `always @(*)` with `case` or `if-else` to describe the circuit functionally.

**Structural Modeling:**
Building the full adder using two half adders and an OR gate (as in Module-1, Lab 4).

## Truth Table

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0  |
| 0 | 0 |  1  |  1  |  0  |
| 0 | 1 |  0  |  1  |  0  |
| 0 | 1 |  1  |  0  |  1  |
| 1 | 0 |  0  |  1  |  0  |
| 1 | 0 |  1  |  0  |  1  |
| 1 | 1 |  0  |  0  |  1  |
| 1 | 1 |  1  |  1  |  1  |

## Verilog Code

```verilog
// Full Adder -- Behavioral using always block
module full_adder_beh (
    input  wire a, b, cin,
    output reg  sum, cout
);
    always @(*) begin
        {cout, sum} = a + b + cin; // using '+' operator
    end
endmodule

// Full Adder -- Structural using XOR, AND, OR primitives
module full_adder_str (
    input  wire a, b, cin,
    output wire sum, cout
);
    wire s1, c1, c2;
    xor u1 (s1, a, b);
    xor u2 (sum, s1, cin);
    and u3 (c1, a, b);
    and u4 (c2, s1, cin);
    or  u5 (cout, c1, c2);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_full_adder;
    reg  a, b, cin;
    wire sum_beh, cout_beh;
    wire sum_str, cout_str;

    full_adder_beh uut_beh (.a(a), .b(b), .cin(cin), .sum(sum_beh), .cout(cout_beh));
    full_adder_str uut_str (.a(a), .b(b), .cin(cin), .sum(sum_str), .cout(cout_str));

    initial begin
        $monitor("A=%b B=%b Cin=%b | Sum_beh=%b Cout_beh=%b | Sum_str=%b Cout_str=%b",
                 a, b, cin, sum_beh, cout_beh, sum_str, cout_str);

        {a, b, cin} = 3'b000; #10;
        {a, b, cin} = 3'b001; #10;
        {a, b, cin} = 3'b010; #10;
        {a, b, cin} = 3'b011; #10;
        {a, b, cin} = 3'b100; #10;
        {a, b, cin} = 3'b101; #10;
        {a, b, cin} = 3'b110; #10;
        {a, b, cin} = 3'b111; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=0 B=0 Cin=0 | Sum_beh=0 Cout_beh=0 | Sum_str=0 Cout_str=0
A=0 B=0 Cin=1 | Sum_beh=1 Cout_beh=0 | Sum_str=1 Cout_str=0
A=0 B=1 Cin=0 | Sum_beh=1 Cout_beh=0 | Sum_str=1 Cout_str=0
A=0 B=1 Cin=1 | Sum_beh=0 Cout_beh=1 | Sum_str=0 Cout_str=1
A=1 B=0 Cin=0 | Sum_beh=1 Cout_beh=0 | Sum_str=1 Cout_str=0
A=1 B=0 Cin=1 | Sum_beh=0 Cout_beh=1 | Sum_str=0 Cout_str=1
A=1 B=1 Cin=0 | Sum_beh=0 Cout_beh=1 | Sum_str=0 Cout_str=1
A=1 B=1 Cin=1 | Sum_beh=1 Cout_beh=1 | Sum_str=1 Cout_str=1
```

## Conclusion

Designed a full adder using both behavioral and structural modeling. Both approaches produce identical results matching the full adder truth table.
