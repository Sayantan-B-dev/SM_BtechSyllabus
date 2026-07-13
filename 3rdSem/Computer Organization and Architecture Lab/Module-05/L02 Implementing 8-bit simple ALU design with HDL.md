# Implementing 8-bit simple ALU design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 5 | **Lecture:** 2  
**Date:** 01-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Enhance the 8-bit ALU with status flags: zero, carry, overflow, and negative.
- Understand how flags are used for conditional operations in CPUs.
- Simulate and verify flag generation for various operations.

## Theory

**ALU Status Flags:**
- **Zero (Z):** Set to 1 when the result is all zeros.
- **Carry (C):** Set to 1 when the operation produces a carry-out (for addition) or borrow (for subtraction).
- **Overflow (V):** Set to 1 when signed overflow occurs (result exceeds the signed 8-bit range -128 to 127).
- **Negative (N):** Set to 1 when the MSB of the result is 1 (result is negative in signed interpretation).

## Verilog Code

```verilog
// Enhanced 8-bit ALU with status flags
module alu_8bit_flags (
    input  wire [7:0] a, b,
    input  wire [2:0] sel,
    output reg  [7:0] result,
    output reg        zero,
    output reg        carry,
    output reg        overflow,
    output reg        negative
);
    wire [8:0] add_result, sub_result;

    assign add_result = a + b;
    assign sub_result = a - b;

    always @(*) begin
        // Default values
        zero = 1'b0;
        carry = 1'b0;
        overflow = 1'b0;
        negative = 1'b0;

        case (sel)
            3'b000: begin  // Addition
                result = add_result[7:0];
                carry = add_result[8];
                overflow = (a[7] == b[7]) && (result[7] != a[7]);
                negative = result[7];
            end
            3'b001: begin  // Subtraction
                result = sub_result[7:0];
                carry = sub_result[8];
                overflow = (a[7] != b[7]) && (result[7] != a[7]);
                negative = result[7];
            end
            3'b010: result = a & b;           // AND
            3'b011: result = a | b;           // OR
            3'b100: result = a ^ b;           // XOR
            3'b101: result = ~a;              // NOT
            3'b110: begin                     // Left shift
                result = a << 1;
                carry = a[7];
            end
            3'b111: begin                     // Right shift
                result = a >> 1;
                carry = a[0];
            end
            default: result = 8'b00000000;
        endcase

        // Zero flag (check after result is computed)
        if (result == 8'b00000000)
            zero = 1'b1;
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_alu_flags;
    reg  [7:0] a, b;
    reg  [2:0] sel;
    wire [7:0] result;
    wire       zero, carry, overflow, negative;

    alu_8bit_flags uut (.a(a), .b(b), .sel(sel), .result(result),
                        .zero(zero), .carry(carry), .overflow(overflow),
                        .negative(negative));

    initial begin
        $monitor("A=%d B=%d sel=%b | result=%d Z=%b C=%b V=%b N=%b",
                 a, b, sel, result, zero, carry, overflow, negative);

        // Test addition: 50 + 50 = 100 (no flags)
        a = 8'd50; b = 8'd50; sel = 3'b000; #10;

        // Test addition: 200 + 100 = 44 (carry, overflow)
        a = 8'd200; b = 8'd100; sel = 3'b000; #10;

        // Test subtraction: 100 - 100 = 0 (zero)
        a = 8'd100; b = 8'd100; sel = 3'b001; #10;

        // Test subtraction: 50 - 100 = -56 (negative)
        a = 8'd50; b = 8'd100; sel = 3'b001; #10;

        // Test AND: 0xFF & 0x00 = 0x00 (zero)
        a = 8'd255; b = 8'd0; sel = 3'b010; #10;

        // Test left shift of 0x80 (carry flag)
        a = 8'd128; b = 8'd0; sel = 3'b110; #10;

        // Test addition: 127 + 1 = 128 (overflow for signed)
        a = 8'd127; b = 8'd1; sel = 3'b000; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
A=50 B=50 sel=000 | result=100 Z=0 C=0 V=0 N=0
A=200 B=100 sel=000 | result=44 Z=0 C=1 V=1 N=0
A=100 B=100 sel=001 | result=0 Z=1 C=0 V=0 N=0
A=50 B=100 sel=001 | result=206 Z=0 C=1 V=0 N=1
A=255 B=0 sel=010 | result=0 Z=1 C=0 V=0 N=0
A=128 B=0 sel=110 | result=0 Z=1 C=1 V=0 N=0
A=127 B=1 sel=000 | result=128 Z=0 C=0 V=1 N=1
```

## Conclusion

Enhanced the 8-bit ALU with zero, carry, overflow, and negative status flags. These flags provide essential status information for conditional branching and program flow control in CPU design.
