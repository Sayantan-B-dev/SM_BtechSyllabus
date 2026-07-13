# Implementing 8-bit Addition, Multiplication, Division with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 2  
**Date:** 10-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Implement an 8-bit multiplier using the `*` operator in Verilog.
- Understand the concept of sequential multiplication (shift-and-add).
- Simulate and verify multiplication results.

## Theory

**Multiplication in Verilog:**
The `*` operator performs binary multiplication. Synthesis tools infer either combinational multipliers (using array of adders) or sequential multipliers depending on coding style.

**8-bit Multiplier:**
For two 8-bit inputs A and B:
- Product = A * B (16-bit result)

The product of two 8-bit numbers requires 16 bits to represent the maximum value (255 * 255 = 65025).

## Verilog Code

```verilog
// 8-bit Multiplier using behavioral '*' operator
module multiplier_8bit (
    input  wire [7:0] a, b,
    output reg  [15:0] product
);
    always @(*) begin
        product = a * b;
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_multiplier_8bit;
    reg  [7:0] a, b;
    wire [15:0] product;

    multiplier_8bit uut (.a(a), .b(b), .product(product));

    initial begin
        $monitor("A=%d B=%d | Product=%d (expected=%d)", a, b, product, a * b);

        a = 8'd10;  b = 8'd5;   #10;
        a = 8'd25;  b = 8'd4;   #10;
        a = 8'd100; b = 8'd3;   #10;
        a = 8'd255; b = 8'd255; #10;
        a = 8'd12;  b = 8'd12;  #10;
        a = 8'd1;   b = 8'd200; #10;
        a = 8'd0;   b = 8'd50;  #10;
        a = 8'd17;  b = 8'd11;  #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=10 B=5 | Product=50 (expected=50)
A=25 B=4 | Product=100 (expected=100)
A=100 B=3 | Product=300 (expected=300)
A=255 B=255 | Product=65025 (expected=65025)
A=12 B=12 | Product=144 (expected=144)
A=1 B=200 | Product=200 (expected=200)
A=0 B=50 | Product=0 (expected=0)
A=17 B=11 | Product=187 (expected=187)
```

## Conclusion

Implemented an 8-bit multiplier using the behavioral `*` operator. The 16-bit product correctly accommodates the full range of multiplication results for 8-bit inputs.
