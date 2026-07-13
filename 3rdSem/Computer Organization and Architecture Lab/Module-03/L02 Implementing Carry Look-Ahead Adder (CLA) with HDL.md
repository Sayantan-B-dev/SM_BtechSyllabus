# Implementing Carry Look-Ahead Adder (CLA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 2  
**Date:** 20-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit CLA using two 4-bit CLA blocks in hierarchical fashion.
- Understand hierarchical design methodology for scalable adders.
- Simulate and verify the 8-bit CLA.

## Theory

**Hierarchical CLA Design:**
An 8-bit CLA can be constructed by cascading two 4-bit CLA blocks. The carry-out from the lower 4-bit CLA becomes the carry-in for the upper 4-bit CLA.

**Group Generate and Propagate:**
For hierarchical CLA, we compute group-level generate (GG) and propagate (GP) signals:
- GGrp = G3 | (P3 & G2) | (P3 & P2 & G1) | (P3 & P2 & P1 & G0)
- PGrp = P3 & P2 & P1 & P0

These allow building wider adders without sacrificing the look-ahead benefit across groups.

## Block Diagram

```
A[7:4] B[7:4]              A[3:0] B[3:0]
   |      |                    |      |
   +------+                    +------+
   |      |                    |      |
  CLA_High                  CLA_Low
   (4-bit)                   (4-bit)
   |      |                    |      |
   +------+------+------+------+------+
                  |             |
                Sum[7:4]     Sum[3:0]
                  |             |
              Cout <--- c3[high]   c3[low] ----> Cin
```

## Verilog Code

```verilog
// 4-bit CLA block with group generate and propagate
module cla_4bit (
    input  wire [3:0] a, b,
    input  wire       cin,
    output wire [3:0] sum,
    output wire       cout,
    output wire       gg, pg         // group generate and propagate
);
    wire [3:0] g, p, c;

    assign g = a & b;
    assign p = a ^ b;

    assign c[0] = cin;
    assign c[1] = g[0] | (p[0] & cin);
    assign c[2] = g[1] | (p[1] & g[0]) | (p[1] & p[0] & cin);
    assign c[3] = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) | (p[2] & p[1] & p[0] & cin);
    assign cout = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) | (p[3] & p[2] & p[1] & g[0]) |
                  (p[3] & p[2] & p[1] & p[0] & cin);

    assign sum = p ^ {c[2:0], cin};

    // Group generate and propagate
    assign gg = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) | (p[3] & p[2] & p[1] & g[0]);
    assign pg = p[3] & p[2] & p[1] & p[0];
endmodule

// 8-bit CLA using two 4-bit CLA blocks
module cla_8bit (
    input  wire [7:0] a, b,
    input  wire       cin,
    output wire [7:0] sum,
    output wire       cout
);
    wire c4;

    cla_4bit low  (.a(a[3:0]), .b(b[3:0]), .cin(cin),  .sum(sum[3:0]), .cout(c4));
    cla_4bit high (.a(a[7:4]), .b(b[7:4]), .cin(c4),   .sum(sum[7:4]), .cout(cout));
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_cla_8bit;
    reg  [7:0] a, b;
    reg        cin;
    wire [7:0] sum;
    wire       cout;

    cla_8bit uut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        $monitor("A=%d B=%d Cin=%b | Sum=%d Cout=%b", a, b, cin, sum, cout);

        a = 8'd15;  b = 8'd20;  cin = 0; #10;
        a = 8'd100; b = 8'd55;  cin = 0; #10;
        a = 8'd200; b = 8'd100; cin = 0; #10;
        a = 8'd255; b = 8'd1;   cin = 0; #10;
        a = 8'd50;  b = 8'd50;  cin = 1; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=15 B=20 Cin=0 | Sum=35 Cout=0
A=100 B=55 Cin=0 | Sum=155 Cout=0
A=200 B=100 Cin=0 | Sum=44 Cout=1
A=255 B=1 Cin=0 | Sum=0 Cout=1
A=50 B=50 Cin=1 | Sum=101 Cout=0
```

## Conclusion

Designed an 8-bit CLA by hierarchically connecting two 4-bit CLA blocks. The hierarchical approach allows scalable adder designs while maintaining the speed advantage of carry look-ahead.
