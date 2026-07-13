# Basic digital logic base programming with HDL through Behavioural model

**Course:** Computer Organization and Architecture Lab  
**Module:** 1 | **Lecture:** 5  
**Date:** 23-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 1  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Understand behavioral modeling in Verilog using the `always` block.
- Use `if-else` and `case` statements for decision-based hardware description.
- Design and simulate a 4:1 multiplexer using behavioral modeling.

## Theory

**Behavioral Modeling:**
Behavioral modeling describes a circuit's functionality at a high level of abstraction, without explicitly specifying gate-level interconnections. It uses constructs like `always`, `if-else`, `case`, and `for` loops.

**always block:**
```verilog
always @(sensitivity_list) begin
    // sequential or combinational logic
end
```
For combinational logic, all input signals are listed in the sensitivity list, or `@(*)` (automatic sensitivity) is used.

**4:1 Multiplexer:**
A multiplexer selects one of several input signals and forwards it to the output. A 4:1 MUX has 4 data inputs (i0, i1, i2, i3), 2 select lines (s1, s0), and 1 output (y).

## Truth Table

| s1 | s0 |  y   |
|----|----|------|
| 0  | 0  |  i0  |
| 0  | 1  |  i1  |
| 1  | 0  |  i2  |
| 1  | 1  |  i3  |

## Verilog Code

```verilog
// 4:1 Multiplexer using behavioral modeling (case statement)
module mux_4to1 (
    input  wire [3:0] i,    // packed inputs: i[0]=i0, i[1]=i1, etc.
    input  wire [1:0] sel,  // select lines: sel[1]=s1, sel[0]=s0
    output reg        y
);
    always @(*) begin
        case (sel)
            2'b00: y = i[0];
            2'b01: y = i[1];
            2'b10: y = i[2];
            2'b11: y = i[3];
            default: y = 1'b0;
        endcase
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_mux_4to1;
    reg  [3:0] i;
    reg  [1:0] sel;
    wire       y;

    mux_4to1 uut (.i(i), .sel(sel), .y(y));

    initial begin
        $monitor("sel=%b i=%b | y=%b", sel, i, y);

        // Set inputs to known pattern
        i = 4'b1010;

        sel = 2'b00; #10;  // expect y = i[0] = 0
        sel = 2'b01; #10;  // expect y = i[1] = 1
        sel = 2'b10; #10;  // expect y = i[2] = 0
        sel = 2'b11; #10;  // expect y = i[3] = 1

        // Try another pattern
        i = 4'b0110;
        sel = 2'b00; #10;
        sel = 2'b01; #10;
        sel = 2'b10; #10;
        sel = 2'b11; #10;

        $finish;
    end
endmodule
```

## Expected Output / Waveform

```
sel=00 i=1010 | y=0
sel=01 i=1010 | y=1
sel=10 i=1010 | y=0
sel=11 i=1010 | y=1
sel=00 i=0110 | y=0
sel=01 i=0110 | y=1
sel=10 i=0110 | y=1
sel=11 i=0110 | y=0
```

## Conclusion

Designed a 4:1 multiplexer using behavioral modeling with the `case` statement. The simulation confirms that the correct input is routed to the output based on the select line combination.
