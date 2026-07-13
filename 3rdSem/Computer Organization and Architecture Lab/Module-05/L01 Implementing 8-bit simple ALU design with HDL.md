# Implementing 8-bit simple ALU design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 1  
**Date:** 01-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit ALU (Arithmetic Logic Unit) supporting multiple operations via select lines.
- Implement add, subtract, AND, OR, XOR, NOT, shift left, and shift right operations.
- Simulate and verify all ALU operations.

## Theory

**ALU (Arithmetic Logic Unit):**
The ALU is the core computational unit of a CPU. It performs arithmetic and logic operations on input data based on a set of select/control lines.

**8-bit ALU with 3 select lines (8 operations):**
| Sel[2:0] | Operation     | Description         |
|----------|---------------|---------------------|
| 000      | A + B         | Addition            |
| 001      | A - B         | Subtraction         |
| 010      | A & B         | Bitwise AND         |
| 011      | A | B         | Bitwise OR          |
| 100      | A ^ B         | Bitwise XOR         |
| 101      | ~A            | Bitwise NOT (A)     |
| 110      | A << 1        | Left shift by 1     |
| 111      | A >> 1        | Right shift by 1    |

## Verilog Code

```verilog
// 8-bit ALU with 8 operations
module alu_8bit (
    input  wire [7:0] a, b,
    input  wire [2:0] sel,
    output reg  [7:0] result
);
    always @(*) begin
        case (sel)
            3'b000: result = a + b;        // Addition
            3'b001: result = a - b;        // Subtraction
            3'b010: result = a & b;        // AND
            3'b011: result = a | b;        // OR
            3'b100: result = a ^ b;        // XOR
            3'b101: result = ~a;           // NOT
            3'b110: result = a << 1;       // Left shift
            3'b111: result = a >> 1;       // Right shift
            default: result = 8'b00000000;
        endcase
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_alu_8bit;
    reg  [7:0] a, b;
    reg  [2:0] sel;
    wire [7:0] result;

    alu_8bit uut (.a(a), .b(b), .sel(sel), .result(result));

    initial begin
        $monitor("A=%d B=%d sel=%b | result=%d", a, b, sel, result);

        a = 8'd20; b = 8'd10;

        sel = 3'b000; #10;  // 20 + 10 = 30
        sel = 3'b001; #10;  // 20 - 10 = 10
        sel = 3'b010; #10;  // 20 & 10 = 0 (10100 & 01010 = 00000)
        sel = 3'b011; #10;  // 20 | 10 = 30 (10100 | 01010 = 11110)
        sel = 3'b100; #10;  // 20 ^ 10 = 30 (10100 ^ 01010 = 11110)
        sel = 3'b101; #10;  // ~20 = 235
        sel = 3'b110; #10;  // 20 << 1 = 40
        sel = 3'b111; #10;  // 20 >> 1 = 10

        a = 8'd240; b = 8'd15;
        sel = 3'b000; #10;  // 240 + 15 = 255
        sel = 3'b010; #10;  // 240 & 15 = 0
        sel = 3'b110; #10;  // 240 << 1 = 224 (overflow)

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=20 B=10 sel=000 | result=30
A=20 B=10 sel=001 | result=10
A=20 B=10 sel=010 | result=0
A=20 B=10 sel=011 | result=30
A=20 B=10 sel=100 | result=30
A=20 B=10 sel=101 | result=235
A=20 B=10 sel=110 | result=40
A=20 B=10 sel=111 | result=10
A=240 B=15 sel=000 | result=255
A=240 B=15 sel=010 | result=0
A=240 B=15 sel=110 | result=224
```

## Conclusion

Designed an 8-bit ALU supporting 8 operations including addition, subtraction, bitwise operations, and shifts. The `case` statement selects the appropriate operation based on the 3-bit select signal.
