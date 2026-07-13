# Implementing RAM design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 6  
**Date:** 24-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a dual-port RAM module with separate read and write ports.
- Understand simultaneous access capabilities of dual-port RAM.
- Simulate concurrent read and write operations.

## Theory

**Dual-Port RAM:**
A dual-port RAM has two independent ports (Port A and Port B), allowing simultaneous access to different memory locations. Each port has its own address, data, and control signals.

**Common Configurations:**
- Two read/write ports (2RW)
- One read/write port + one read-only port (1RW + 1R)
- One read/write port + one write-only port (1RW + 1W)

In this lab, we implement a true dual-port RAM where both ports can read or write independently.

## Block Diagram

```
         +---------+
addr_a-->|         |---> dout_a
din_a--->| DUAL    |
we_a---->| PORT    |
         |  RAM    |
addr_b-->| 256x8   |---> dout_b
din_b--->|         |
we_b---->|         |
clk------>|         |
         +---------+
```

## Verilog Code

```verilog
// Dual-port RAM: 256 x 8
module dual_port_ram (
    input  wire        clk,
    // Port A
    input  wire        we_a,
    input  wire [7:0]  addr_a,
    input  wire [7:0]  din_a,
    output reg  [7:0]  dout_a,
    // Port B
    input  wire        we_b,
    input  wire [7:0]  addr_b,
    input  wire [7:0]  din_b,
    output reg  [7:0]  dout_b
);
    // Shared memory array
    reg [7:0] mem [0:255];

    // Port A operations
    always @(posedge clk) begin
        if (we_a)
            mem[addr_a] <= din_a;
        dout_a <= mem[addr_a];
    end

    // Port B operations
    always @(posedge clk) begin
        if (we_b)
            mem[addr_b] <= din_b;
        dout_b <= mem[addr_b];
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_dual_port_ram;
    reg        clk;
    reg        we_a, we_b;
    reg  [7:0] addr_a, addr_b;
    reg  [7:0] din_a, din_b;
    wire [7:0] dout_a, dout_b;

    dual_port_ram uut (.clk(clk), .we_a(we_a), .addr_a(addr_a), .din_a(din_a),
                       .dout_a(dout_a), .we_b(we_b), .addr_b(addr_b),
                       .din_b(din_b), .dout_b(dout_b));

    always #5 clk = ~clk;

    initial begin
        $monitor("clk=%b | PortA: we=%b addr=%d din=%d dout=%d | PortB: we=%b addr=%d din=%d dout=%d",
                 clk, we_a, addr_a, din_a, dout_a, we_b, addr_b, din_b, dout_b);

        clk = 0; we_a = 0; we_b = 0; addr_a = 0; addr_b = 0;
        din_a = 0; din_b = 0;

        // Port A writes to address 10, Port B writes to address 20 simultaneously
        #10 we_a = 1; addr_a = 10; din_a = 8'd100;
            we_b = 1; addr_b = 20; din_b = 8'd200;
        #10 we_a = 0; we_b = 0;

        // Port A reads address 10, Port B reads address 20 simultaneously
        #10 addr_a = 10; addr_b = 20;
        #10;

        // Port A writes to address 10 while Port B reads address 10 simultaneously
        #10 we_a = 1; addr_a = 10; din_a = 8'd150;
            we_b = 0; addr_b = 10;
        #10 we_a = 0;

        // Both read address 10
        #10 addr_a = 10; addr_b = 10;
        #10;

        #20 $finish;
    end
endmodule
```

## Expected Output / Waveform

```
clk=0 | PortA: we=0 addr=0 din=0 dout=0 | PortB: we=0 addr=0 din=0 dout=0
clk=1 | PortA: we=1 addr=10 din=100 dout=X | PortB: we=1 addr=20 din=200 dout=X
clk=1 | PortA: we=0 addr=10 din=100 dout=100 | PortB: we=0 addr=20 din=200 dout=200
clk=1 | PortA: we=0 addr=10 din=100 dout=100 | PortB: we=0 addr=20 din=200 dout=200
clk=1 | PortA: we=1 addr=10 din=150 dout=100 | PortB: we=0 addr=10 din=200 dout=100
clk=1 | PortA: we=0 addr=10 din=150 dout=150 | PortB: we=0 addr=10 din=200 dout=150
clk=1 | PortA: we=0 addr=10 din=150 dout=150 | PortB: we=0 addr=10 din=200 dout=150
```

## Conclusion

Designed a dual-port RAM module with independent read/write ports. The simulation demonstrates simultaneous write operations at different addresses, concurrent reads, and read-write to the same address through different ports.
