# Implementing 8-bit Addition, Multiplication, Division with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 1  
**Date:** 10-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Implement an 8-bit adder using the behavioral `+` operator in Verilog.
- Understand that synthesis tools infer adder hardware from the `+` operator.
- Simulate with multiple random values.

## Theory

**Behavioral Addition:**
In Verilog, the `+` operator performs binary addition. When used in an `always` block or with `assign`, synthesis tools automatically infer the appropriate adder hardware (ripple carry, carry look-ahead, etc.).

**8-bit Adder:**
For two 8-bit inputs A and B, and an optional carry-in (Cin):
- {Cout, Sum} = A + B + Cin

The result is 9 bits wide (8-bit sum + 1-bit carry-out) to accommodate overflow.

## Verilog Code

```verilog
// 8-bit Adder using behavioral '+' operator
module adder_8bit (
    input  wire [7:0] a, b,
    input  wire       cin,
    output reg  [7:0] sum,
    output reg        cout
);
    always @(*) begin
        {cout, sum} = a + b + cin;
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_adder_8bit;
    reg  [7:0] a, b;
    reg        cin;
    wire [7:0] sum;
    wire       cout;

    adder_8bit uut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        $monitor("A=%d B=%d Cin=%b | Sum=%d Cout=%b (expected=%d)",
                 a, b, cin, sum, cout, a + b + cin);

        // Test with various values
        a = 8'd15;  b = 8'd20;  cin = 0; #10;
        a = 8'd100; b = 8'd55;  cin = 0; #10;
        a = 8'd200; b = 8'd100; cin = 0; #10;
        a = 8'd255; b = 8'd1;   cin = 0; #10;
        a = 8'd50;  b = 8'd50;  cin = 1; #10;
        a = 8'd0;   b = 8'd0;   cin = 1; #10;
        a = 8'd128; b = 8'd127; cin = 0; #10;
        a = 8'd99;  b = 8'd88;  cin = 1; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=15 B=20 Cin=0 | Sum=35 Cout=0 (expected=35)
A=100 B=55 Cin=0 | Sum=155 Cout=0 (expected=155)
A=200 B=100 Cin=0 | Sum=44 Cout=1 (expected=300)
A=255 B=1 Cin=0 | Sum=0 Cout=1 (expected=256)
A=50 B=50 Cin=1 | Sum=101 Cout=0 (expected=101)
A=0 B=0 Cin=1 | Sum=1 Cout=0 (expected=1)
A=128 B=127 Cin=0 | Sum=255 Cout=0 (expected=255)
A=99 B=88 Cin=1 | Sum=188 Cout=0 (expected=188)
```

## Conclusion

Implemented an 8-bit adder using the behavioral `+` operator. The synthesizer automatically infers the adder logic. Simulation results match the expected arithmetic sums, including overflow handling via the carry-out bit.
