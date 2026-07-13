# Basic digital logic base programming with HDL through structural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 4  
**Date:** 16-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a full adder using structural modeling by cascading two half adders.
- Understand hierarchical design -- using one module inside another.
- Verify functionality through exhaustive simulation.

## Theory

**Full Adder:**
A full adder adds three single-bit inputs: A, B, and Carry-in (Cin). It produces:
- Sum (S) = A xor B xor Cin
- Carry-out (Cout) = (A & B) | (Cin & (A xor B))

**Structural Implementation using two Half Adders:**
A full adder can be built with two half adders and one OR gate:
1. First half adder: sum1 = A xor B, carry1 = A & B
2. Second half adder: Sum = sum1 xor Cin, carry2 = sum1 & Cin
3. Cout = carry1 | carry2

**Block Diagram:**
```
         +-----------+
A ------>| Half      |-- sum1 ----> +-----------+
B ------>| Adder 1   |-- carry1    | Half      |-- Sum
         +-----------+      |----->| Adder 2   |
                     |      |      +-----------+
         +-----------+      |           |
Cin ------------------------+      carry2
         +-----------+      |           |
         |    OR     |<-----+-----------+
         +-----------+-------> Cout
```

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
// Half Adder module (used as building block)
module half_adder (
    input  wire a, b,
    output wire sum, carry
);
    xor u1 (sum, a, b);
    and u2 (carry, a, b);
endmodule

// Full Adder using two half adders
module full_adder (
    input  wire a, b, cin,
    output wire sum, cout
);
    wire sum1, carry1, carry2;

    half_adder ha1 (.a(a), .b(b),       .sum(sum1),  .carry(carry1));
    half_adder ha2 (.a(sum1), .b(cin),  .sum(sum),   .carry(carry2));

    or u3 (cout, carry1, carry2);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_full_adder;
    reg  a, b, cin;
    wire sum, cout;

    full_adder uut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        $monitor("A=%b B=%b Cin=%b | Sum=%b Cout=%b", a, b, cin, sum, cout);

        // Exhaustive test: 8 combinations
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
A=0 B=0 Cin=0 | Sum=0 Cout=0
A=0 B=0 Cin=1 | Sum=1 Cout=0
A=0 B=1 Cin=0 | Sum=1 Cout=0
A=0 B=1 Cin=1 | Sum=0 Cout=1
A=1 B=0 Cin=0 | Sum=1 Cout=0
A=1 B=0 Cin=1 | Sum=0 Cout=1
A=1 B=1 Cin=0 | Sum=0 Cout=1
A=1 B=1 Cin=1 | Sum=1 Cout=1
```

## Conclusion

Successfully designed a full adder using structural modeling by instantiating two half adders and an OR gate. The hierarchical design approach was demonstrated and verified against the full adder truth table.
