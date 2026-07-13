# HDL introduction

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 1  
**Date:** 09-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Computer Organization and Design: The Hardware/Software Interface, David A. Patterson and John L. Hennessy, 5th edition, Elsevier. & Lab Manual

## Lab Objectives

- Understand the fundamental structure of a Verilog module (ports, inputs, outputs, body).
- Learn basic Verilog data types: `wire` (combinational) and `reg` (sequential/stored).
- Implement and simulate basic logic gates (AND, OR, NOT) using dataflow modeling.

## Theory

**HDL (Hardware Description Language)** allows designers to describe digital circuits textually. Verilog is one of the most widely used HDLs.

**Module Structure:**
```verilog
module module_name (port_list);
  input  [width-1:0] input_port;
  output [width-1:0] output_port;
  // internal logic
endmodule
```

**Data Types:**
- `wire` -- Represents a physical wire; holds a value only when driven continuously. Used in combinational logic.
- `reg` -- Represents a storage element; holds a value until a new value is assigned inside an `always` block. Used in sequential and behavioral logic.

**Basic Gates (Dataflow operators):**
- AND:  `assign y = a & b;`
- OR:   `assign y = a | b;`
- NOT:  `assign y = ~a;`

## Truth Table

**AND Gate:**
| a | b | y = a & b |
|---|---|-----------|
| 0 | 0 |     0     |
| 0 | 1 |     0     |
| 1 | 0 |     0     |
| 1 | 1 |     1     |

**OR Gate:**
| a | b | y = a | b |
|---|---|-----------|
| 0 | 0 |     0     |
| 0 | 1 |     1     |
| 1 | 0 |     1     |
| 1 | 1 |     1     |

**NOT Gate:**
| a | y = ~a |
|---|--------|
| 0 |   1    |
| 1 |   0    |

## Verilog Code

```verilog
// AND gate module
module and_gate (
    input  wire a,
    input  wire b,
    output wire y
);
    assign y = a & b;
endmodule

// OR gate module
module or_gate (
    input  wire a,
    input  wire b,
    output wire y
);
    assign y = a | b;
endmodule

// NOT gate module
module not_gate (
    input  wire a,
    output wire y
);
    assign y = ~a;
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_gates;
    reg  a, b;
    wire y_and, y_or, y_not;

    // Instantiate the gates
    and_gate u1 (.a(a), .b(b), .y(y_and));
    or_gate  u2 (.a(a), .b(b), .y(y_or));
    not_gate u3 (.a(a),       .y(y_not));

    initial begin
        $monitor("a=%b b=%b  AND=%b OR=%b NOT(a)=%b", a, b, y_and, y_or, y_not);

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
a=0 b=0  AND=0 OR=0 NOT(a)=1
a=0 b=1  AND=0 OR=1 NOT(a)=1
a=1 b=0  AND=0 OR=1 NOT(a)=0
a=1 b=1  AND=1 OR=1 NOT(a)=0
```

## Conclusion

Successfully implemented AND, OR, and NOT gates using dataflow modeling in Verilog. The simulation results match the expected truth tables, confirming correct functionality.
