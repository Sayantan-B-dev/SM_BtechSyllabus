# Basic digital logic base programming with HDL through structural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 3  
**Date:** 16-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Understand structural modeling in Verilog by instantiating primitive gates.
- Design a half adder using structural modeling with XOR and AND primitive gates.
- Simulate and verify the half adder circuit.

## Theory

**Structural Modeling:**
In structural modeling, a digital circuit is described by interconnecting predefined primitive gates (and, or, not, xor, etc.). This resembles building a circuit on a breadboard by wiring components.

**Half Adder:**
A half adder adds two single-bit binary numbers (A and B) and produces:
- Sum (S) = A xor B
- Carry (C) = A and B

**Primitive Gate Instantiation:**
```verilog
gate_type instance_name (output, input1, input2, ...);
// Example:
xor u1 (sum, a, b);
and u2 (carry, a, b);
```

## Truth Table

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 |    0    |     0     |
| 0 | 1 |    1    |     0     |
| 1 | 0 |    1    |     0     |
| 1 | 1 |    0    |     1     |

**Block Diagram:**
```
         _________
A ------>|       |
         |  XOR  |-----> Sum (S)
B ------>|_______|

A ------>|       |
         |  AND  |-----> Carry (C)
B ------>|_______|
```

## Verilog Code

```verilog
// Half Adder using structural modeling
module half_adder (
    input  wire a,
    input  wire b,
    output wire sum,
    output wire carry
);
    // Instantiate primitive gates
    xor u1 (sum, a, b);
    and u2 (carry, a, b);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_half_adder;
    reg  a, b;
    wire sum, carry;

    half_adder uut (.a(a), .b(b), .sum(sum), .carry(carry));

    initial begin
        $monitor("A=%b B=%b | Sum=%b Carry=%b", a, b, sum, carry);

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
A=0 B=0 | Sum=0 Carry=0
A=0 B=1 | Sum=1 Carry=0
A=1 B=0 | Sum=1 Carry=0
A=1 B=1 | Sum=0 Carry=1
```

## Conclusion

Designed a half adder using structural modeling in Verilog by instantiating primitive XOR and AND gates. The simulation results match the expected half adder truth table.
