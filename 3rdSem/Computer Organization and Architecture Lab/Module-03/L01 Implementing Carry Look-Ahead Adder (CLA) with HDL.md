# Implementing Carry Look-Ahead Adder (CLA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 1  
**Date:** 20-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Understand the theory of Carry Look-Ahead Adder (CLA) -- generate (G) and propagate (P) signals.
- Design a 4-bit CLA in Verilog.
- Compare CLA performance with ripple carry adder.

## Theory

**Carry Look-Ahead Adder (CLA):**
The CLA reduces propagation delay by computing the carry signals in parallel using generate (G) and propagate (P) signals.

For each bit position i:
- Generate:  Gi = Ai & Bi  (carry is generated when both inputs are 1)
- Propagate: Pi = Ai ^ Bi  (carry propagates when exactly one input is 1)

The carry signals are computed as:
- C0 = Cin
- C1 = G0 | (P0 & Cin)
- C2 = G1 | (P1 & G0) | (P1 & P0 & Cin)
- C3 = G2 | (P2 & G1) | (P2 & P1 & G0) | (P2 & P1 & P0 & Cin)
- C4 = G3 | (P3 & G2) | (P3 & P2 & G1) | (P3 & P2 & P1 & G0) | (P3 & P2 & P1 & P0 & Cin)

Sum = Pi ^ Ci-1 (for each bit)

## Block Diagram

```
Ai Bi
|  |
+--+--+
|     |
AND   XOR
|     |
Gi    Pi
|     |
+-----+-----+
      |     |
      |     +-----> Si = Pi XOR Ci-1
      |
      +-----> Carry Logic (parallel)
                  |
                  Ci
```

## Truth Table (per bit)

| Ai | Bi | Gi | Pi |
|----|----|----|----|
| 0  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  |
| 1  | 0  | 0  | 1  |
| 1  | 1  | 1  | 0  |

## Verilog Code

```verilog
// 4-bit Carry Look-Ahead Adder
module cla_4bit (
    input  wire [3:0] a, b,
    input  wire       cin,
    output wire [3:0] sum,
    output wire       cout
);
    wire [3:0] g, p, c;

    // Generate and Propagate signals
    assign g = a & b;
    assign p = a ^ b;

    // Carry computation (parallel, look-ahead)
    assign c[0] = cin;
    assign c[1] = g[0] | (p[0] & cin);
    assign c[2] = g[1] | (p[1] & g[0]) | (p[1] & p[0] & cin);
    assign c[3] = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) | (p[2] & p[1] & p[0] & cin);
    assign cout = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) | (p[3] & p[2] & p[1] & g[0]) |
                  (p[3] & p[2] & p[1] & p[0] & cin);

    // Sum computation
    assign sum = p ^ {c[2:0], cin};
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_cla;
    reg  [3:0] a, b;
    reg        cin;
    wire [3:0] sum;
    wire       cout;

    cla_4bit uut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        $monitor("A=%b B=%b Cin=%b | Sum=%b Cout=%b", a, b, cin, sum, cout);

        a = 4'b0011; b = 4'b0101; cin = 0; #10;
        a = 4'b0110; b = 4'b0011; cin = 0; #10;
        a = 4'b1111; b = 4'b0001; cin = 0; #10;
        a = 4'b1010; b = 4'b1010; cin = 0; #10;
        a = 4'b1111; b = 4'b1111; cin = 0; #10;
        a = 4'b0000; b = 4'b0000; cin = 1; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=0011 B=0101 Cin=0 | Sum=1000 Cout=0
A=0110 B=0011 Cin=0 | Sum=1001 Cout=0
A=1111 B=0001 Cin=0 | Sum=0000 Cout=1
A=1010 B=1010 Cin=0 | Sum=0100 Cout=1
A=1111 B=1111 Cin=0 | Sum=1110 Cout=1
A=0000 B=0000 Cin=1 | Sum=0001 Cout=0
```

## Conclusion

Designed a 4-bit Carry Look-Ahead Adder. The CLA computes all carry signals in parallel using generate/propagate logic, significantly reducing the propagation delay compared to a ripple carry adder.
