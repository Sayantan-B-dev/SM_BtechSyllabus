# Implementing Comparator with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 3 | **Lecture:** 6  
**Date:** 03-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit comparator with an enable input using behavioral modeling.
- Use `if-else` statements for the comparator logic.
- Simulate with the enable signal disabled and enabled.

## Theory

**Comparator with Enable:**
An enable input (en) controls whether the comparator is active. When en = 0, the outputs are forced to a known state (all zero). When en = 1, normal comparison occurs.

**Behavioral Implementation:**
Using `always @(*)` with `if-else` statements makes the code easy to read and modify. The comparison can use either bit-wise logic or relational operators (`>`, `<`, `==`).

## Verilog Code

```verilog
// 8-bit Comparator with Enable
module comp_8bit_en (
    input  wire       en,
    input  wire [7:0] a, b,
    output reg        a_gt_b,
    output reg        a_eq_b,
    output reg        a_lt_b
);
    always @(*) begin
        if (!en) begin
            a_gt_b = 1'b0;
            a_eq_b = 1'b0;
            a_lt_b = 1'b0;
        end else begin
            if (a > b) begin
                a_gt_b = 1'b1;
                a_eq_b = 1'b0;
                a_lt_b = 1'b0;
            end else if (a == b) begin
                a_gt_b = 1'b0;
                a_eq_b = 1'b1;
                a_lt_b = 1'b0;
            end else begin
                a_gt_b = 1'b0;
                a_eq_b = 1'b0;
                a_lt_b = 1'b1;
            end
        end
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_comp_8bit_en;
    reg        en;
    reg  [7:0] a, b;
    wire       a_gt_b, a_eq_b, a_lt_b;

    comp_8bit_en uut (.en(en), .a(a), .b(b), .a_gt_b(a_gt_b), .a_eq_b(a_eq_b), .a_lt_b(a_lt_b));

    initial begin
        $monitor("en=%b A=%d B=%d | A>B=%b A=B=%b A<B=%b",
                 en, a, b, a_gt_b, a_eq_b, a_lt_b);

        // Enable disabled -- outputs should be 0
        en = 0;
        a = 8'd100; b = 8'd50;  #10;
        a = 8'd50;  b = 8'd100; #10;

        // Enable enabled
        en = 1;
        a = 8'd100; b = 8'd50;  #10;  // A > B
        a = 8'd50;  b = 8'd100; #10;  // A < B
        a = 8'd75;  b = 8'd75;  #10;  // A = B
        a = 8'd200; b = 8'd100; #10;  // A > B
        a = 8'd0;   b = 8'd255; #10;  // A < B

        // Disable again
        en = 0;
        a = 8'd200; b = 8'd100; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
en=0 A=100 B=50 | A>B=0 A=B=0 A<B=0
en=0 A=50 B=100 | A>B=0 A=B=0 A<B=0
en=1 A=100 B=50 | A>B=1 A=B=0 A<B=0
en=1 A=50 B=100 | A>B=0 A=B=0 A<B=1
en=1 A=75 B=75 | A>B=0 A=B=1 A<B=0
en=1 A=200 B=100 | A>B=1 A=B=0 A<B=0
en=1 A=0 B=255 | A>B=0 A=B=0 A<B=1
en=0 A=200 B=100 | A>B=0 A=B=0 A<B=0
```

## Conclusion

Designed an 8-bit comparator with enable control using behavioral `if-else` statements. When enable is low, all outputs are zero. When enable is high, the comparator correctly identifies the relationship between the two 8-bit inputs.
