# HDL introduction

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 2  
**Date:** 09-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Computer Organization and Design: The Hardware/Software Interface, David A. Patterson and John L. Hennessy, 5th edition, Elsevier. & Lab Manual

## Lab Objectives

- Implement and simulate NAND, NOR, XOR, and XNOR gates using dataflow Verilog.
- Understand the concept of universal gates (NAND and NOR) and their ability to implement any Boolean function.
- Verify all gates through simulation testbench.

## Theory

**Universal Gates:**
- NAND gate: `y = ~(a & b)` -- A NAND gate alone can implement AND, OR, NOT, and any other logic function.
- NOR gate: `y = ~(a | b)` -- Similarly universal; any Boolean expression can be realized using only NOR gates.

**XOR and XNOR:**
- XOR (exclusive-OR): `y = a ^ b` -- Output is 1 when inputs differ.
- XNOR (exclusive-NOR): `y = ~(a ^ b)` -- Output is 1 when inputs are equal.

## Truth Table

| a | b | NAND | NOR | XOR | XNOR |
|---|---|------|-----|-----|------|
| 0 | 0 |  1   |  1  |  0  |  1   |
| 0 | 1 |  1   |  0  |  1  |  0   |
| 1 | 0 |  1   |  0  |  1  |  0   |
| 1 | 1 |  0   |  0  |  0  |  1   |

**NAND as Universal Gate -- Basic Equivalents:**
- NOT: `NAND(a, a)` = NOT a
- AND: `NAND(NAND(a,b), NAND(a,b))` = a AND b
- OR:  `NAND(NAND(a,a), NAND(b,b))` = a OR b

## Verilog Code

```verilog
// NAND gate
module nand_gate (
    input  wire a, b,
    output wire y
);
    assign y = ~(a & b);
endmodule

// NOR gate
module nor_gate (
    input  wire a, b,
    output wire y
);
    assign y = ~(a | b);
endmodule

// XOR gate
module xor_gate (
    input  wire a, b,
    output wire y
);
    assign y = a ^ b;
endmodule

// XNOR gate
module xnor_gate (
    input  wire a, b,
    output wire y
);
    assign y = ~(a ^ b);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_gates2;
    reg  a, b;
    wire y_nand, y_nor, y_xor, y_xnor;

    nand_gate u1 (.a(a), .b(b), .y(y_nand));
    nor_gate  u2 (.a(a), .b(b), .y(y_nor));
    xor_gate  u3 (.a(a), .b(b), .y(y_xor));
    xnor_gate u4 (.a(a), .b(b), .y(y_xnor));

    initial begin
        $monitor("a=%b b=%b | NAND=%b NOR=%b XOR=%b XNOR=%b",
                 a, b, y_nand, y_nor, y_xor, y_xnor);

        a = 0; b = 0; #10;
        a = 0; b = 1; #10;
        a = 1; b = 0; #10;
        a = 1; b = 1; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
a=0 b=0 | NAND=1 NOR=1 XOR=0 XNOR=1
a=0 b=1 | NAND=1 NOR=0 XOR=1 XNOR=0
a=1 b=0 | NAND=1 NOR=0 XOR=1 XNOR=0
a=1 b=1 | NAND=0 NOR=0 XOR=0 XNOR=1
```

## Conclusion

Successfully implemented NAND, NOR, XOR, and XNOR gates. The universal nature of NAND and NOR gates was discussed -- any logic circuit can be built using only these gates.
