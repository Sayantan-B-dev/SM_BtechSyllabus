# Implementing Half Adder with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 2 | **Lecture:** 1  
**Date:** 30-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a half adder using structural and dataflow modeling in Verilog.
- Understand the truth table and logical expressions for half adder.
- Verify the design through simulation.

## Theory

**Half Adder:**
A half adder is a combinational circuit that adds two single-bit binary numbers (A and B). It produces two outputs:
- Sum (S) = A xor B
- Carry (C) = A and B

**Modeling Styles:**
1. **Dataflow:** Uses `assign` statements with operators like `^` and `&`.
2. **Structural:** Instantiates primitive gates like `xor` and `and`.

## Truth Table

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 |    0    |     0     |
| 0 | 1 |    1    |     0     |
| 1 | 0 |    1    |     0     |
| 1 | 1 |    0    |     1     |

## Verilog Code

```verilog
// Half Adder -- Dataflow modeling
module half_adder_df (
    input  wire a, b,
    output wire sum, carry
);
    assign sum   = a ^ b;
    assign carry = a & b;
endmodule

// Half Adder -- Structural modeling
module half_adder_st (
    input  wire a, b,
    output wire sum, carry
);
    xor u1 (sum, a, b);
    and u2 (carry, a, b);
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_half_adder;
    reg  a, b;
    wire sum_df, carry_df;
    wire sum_st, carry_st;

    half_adder_df uut_df (.a(a), .b(b), .sum(sum_df), .carry(carry_df));
    half_adder_st uut_st (.a(a), .b(b), .sum(sum_st), .carry(carry_st));

    initial begin
        $monitor("A=%b B=%b | Sum_df=%b Carry_df=%b | Sum_st=%b Carry_st=%b",
                 a, b, sum_df, carry_df, sum_st, carry_st);

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
A=0 B=0 | Sum_df=0 Carry_df=0 | Sum_st=0 Carry_st=0
A=0 B=1 | Sum_df=1 Carry_df=0 | Sum_st=1 Carry_st=0
A=1 B=0 | Sum_df=1 Carry_df=0 | Sum_st=1 Carry_st=0
A=1 B=1 | Sum_df=0 Carry_df=1 | Sum_st=0 Carry_st=1
```

## Conclusion

Designed a half adder using both dataflow and structural modeling styles. Both implementations produce identical results matching the expected truth table.
