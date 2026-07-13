# Implementing Carry Propagate Adder (CPA) with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 5  
**Date:** 13-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a 4-bit ripple carry adder (carry propagate adder) using structural Verilog.
- Understand how carry propagates through cascaded full adders.
- Simulate with multiple input combinations.

## Theory

**Ripple Carry Adder (RCA):**
A 4-bit ripple carry adder adds two 4-bit numbers (A[3:0] and B[3:0]) along with a carry-in (Cin) to produce a 4-bit sum (S[3:0]) and carry-out (Cout).

It consists of 4 full adders connected in series. The carry-out of each full adder feeds into the carry-in of the next higher stage.

**Delay:**
The main disadvantage is propagation delay -- the carry must "ripple" through all stages. The worst-case delay is proportional to the number of bits.

**Block Diagram:**
```
A3 B3    A2 B2    A1 B1    A0 B0
|  |     |  |     |  |     |  |
FA3      FA2      FA1      FA0
|  |     |  |     |  |     |  |
S3 C3--> S2 C2--> S1 C1--> S0 Cin
                    |
                   Cout
```

## Truth Table (4-bit addition example)

| A    | B    | Cin | S    | Cout |
|------|------|-----|------|------|
| 0011 | 0101 |  0  | 1000 |   0  |
| 0110 | 0011 |  0  | 1001 |   0  |
| 1111 | 0001 |  0  | 0000 |   1  |
| 1010 | 1010 |  0  | 0100 |   1  |

## Verilog Code

```verilog
// Full Adder module (building block)
module full_adder (
    input  wire a, b, cin,
    output wire sum, cout
);
    assign {cout, sum} = a + b + cin;
endmodule

// 4-bit Ripple Carry Adder
module ripple_carry_adder (
    input  wire [3:0] a, b,
    input  wire       cin,
    output wire [3:0] sum,
    output wire       cout
);
    wire c1, c2, c3;

    full_adder fa0 (.a(a[0]), .b(b[0]), .cin(cin),  .sum(sum[0]), .cout(c1));
    full_adder fa1 (.a(a[1]), .b(b[1]), .cin(c1),   .sum(sum[1]), .cout(c2));
    full_adder fa2 (.a(a[2]), .b(b[2]), .cin(c2),   .sum(sum[2]), .cout(c3));
    full_adder fa3 (.a(a[3]), .b(b[3]), .cin(c3),   .sum(sum[3]), .cout(cout));
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_rca;
    reg  [3:0] a, b;
    reg        cin;
    wire [3:0] sum;
    wire       cout;

    ripple_carry_adder uut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        $monitor("A=%b B=%b Cin=%b | Sum=%b Cout=%b (decimal: %d + %d + %d = %d)",
                 a, b, cin, sum, cout, a, b, cin, {cout, sum});

        a = 4'b0011; b = 4'b0101; cin = 0; #10;
        a = 4'b0110; b = 4'b0011; cin = 0; #10;
        a = 4'b1111; b = 4'b0001; cin = 0; #10;  // 15 + 1 = 16 (overflow)
        a = 4'b1010; b = 4'b1010; cin = 0; #10;  // 10 + 10 = 20
        a = 4'b0111; b = 4'b1000; cin = 0; #10;  // 7 + 8 = 15
        a = 4'b0001; b = 4'b0010; cin = 1; #10;  // 1 + 2 + 1 = 4

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=0011 B=0101 Cin=0 | Sum=1000 Cout=0 (decimal: 3 + 5 + 0 = 8)
A=0110 B=0011 Cin=0 | Sum=1001 Cout=0 (decimal: 6 + 3 + 0 = 9)
A=1111 B=0001 Cin=0 | Sum=0000 Cout=1 (decimal: 15 + 1 + 0 = 16)
A=1010 B=1010 Cin=0 | Sum=0100 Cout=1 (decimal: 10 + 10 + 0 = 20)
A=0111 B=1000 Cin=0 | Sum=1111 Cout=0 (decimal: 7 + 8 + 0 = 15)
A=0001 B=0010 Cin=1 | Sum=0100 Cout=0 (decimal: 1 + 2 + 1 = 4)
```

## Conclusion

Successfully designed a 4-bit ripple carry adder by cascading four full adders. The carry propagates through each stage, and the simulation results confirm correct addition for multiple input combinations.
