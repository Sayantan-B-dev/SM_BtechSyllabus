# Implementing 8-bit Register design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 3  
**Date:** 17-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design an 8-bit D flip-flop register with synchronous reset and enable.
- Understand the behavior of sequential circuits with clock, reset, and enable.
- Simulate to verify load, hold, and reset operations.

## Theory

**D Flip-Flop Register:**
An n-bit register stores n bits of data on the rising (or falling) edge of a clock signal. It consists of n D flip-flops sharing a common clock.

**Control Signals:**
- **Clock (clk):** Triggers the storage operation on the active edge.
- **Reset (rst):** Forces all bits to 0 (synchronous: on clock edge; asynchronous: immediately).
- **Enable (en):** When high, new data is loaded on the clock edge. When low, the register retains its current value.

**Timing Diagram (Synchronous):**
```
clk   : _|-|_|-|_|-|_|-|_|-|
rst   : ___|---|___________
en    : ___|-------|_______
d     : XX< A >< B >< C >XX
q     : XX< 0 >< A >< B >XX (rst clears, en loads)
```

## Verilog Code

```verilog
// 8-bit Register with synchronous reset and enable
module reg_8bit (
    input  wire       clk,
    input  wire       rst,
    input  wire       en,
    input  wire [7:0] d,
    output reg  [7:0] q
);
    always @(posedge clk) begin
        if (rst)
            q <= 8'b00000000;
        else if (en)
            q <= d;
        // else: q holds its value (implied latch)
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_reg_8bit;
    reg        clk, rst, en;
    reg  [7:0] d;
    wire [7:0] q;

    reg_8bit uut (.clk(clk), .rst(rst), .en(en), .d(d), .q(q));

    // Clock generation: 10ns period
    always #5 clk = ~clk;

    initial begin
        $monitor("clk=%b rst=%b en=%b d=%d | q=%d", clk, rst, en, d, q);

        // Initialize
        clk = 0; rst = 0; en = 0; d = 8'd0;

        // Reset the register
        #10 rst = 1;
        #10 rst = 0;

        // Load value A
        #10 en = 1; d = 8'd42;
        #10 en = 0;

        // Load value B (should not load because en = 0)
        #10 d = 8'd99;
        #10;

        // Enable and load C
        #10 en = 1; d = 8'd77;
        #10 en = 0;

        // Reset again
        #10 rst = 1;
        #10 rst = 0;

        #20 $finish;
    end
endmodule
```

## Expected Output / Waveform

```
clk=0 rst=0 en=0 d=0   | q=0
clk=1 rst=0 en=0 d=0   | q=0
clk=0 rst=1 en=0 d=0   | q=0
clk=1 rst=1 en=0 d=0   | q=0  (reset active)
clk=0 rst=0 en=0 d=0   | q=0
clk=1 rst=0 en=0 d=0   | q=0
clk=0 rst=0 en=1 d=42  | q=0
clk=1 rst=0 en=1 d=42  | q=42 (loaded on posedge)
clk=0 rst=0 en=0 d=42  | q=42
clk=1 rst=0 en=0 d=99  | q=42 (hold, en=0)
clk=0 rst=0 en=1 d=77  | q=42
clk=1 rst=0 en=1 d=77  | q=77 (loaded)
clk=0 rst=1 en=0 d=77  | q=77
clk=1 rst=1 en=0 d=77  | q=0  (reset)
```

## Conclusion

Designed an 8-bit register with synchronous reset and enable control. The register correctly loads data only when enabled on the rising clock edge, holds its value when disabled, and resets to zero when reset is asserted.
