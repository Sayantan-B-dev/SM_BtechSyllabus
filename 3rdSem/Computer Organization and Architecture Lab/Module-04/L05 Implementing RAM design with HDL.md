# Implementing RAM design with HDL

**Course:** Computer Organization and Architecture Lab  
**Module:** 4 | **Lecture:** 5  
**Date:** 24-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Book & Lab Manual

## Lab Objectives

- Design a single-port RAM module with address, data_in, data_out, write enable, and clock.
- Understand memory array modeling using Verilog reg arrays.
- Simulate write and read operations.

## Theory

**Single-Port RAM:**
A single-port RAM allows one read or one write operation per clock cycle. It consists of:
- **Address (addr):** Selects which memory location to access.
- **Data_in (din):** Data to be written.
- **Data_out (dout):** Data read from the addressed location.
- **Write Enable (we):** When high, data is written on the clock edge. When low, a read operation occurs.
- **Clock (clk):** Synchronizes all memory operations.

**Memory Array Declaration:**
```verilog
reg [DATA_WIDTH-1:0] mem [0:DEPTH-1];
```

## Block Diagram

```
         +---------+
addr --->|         |---> dout
din ---->|  RAM    |
we ----->|  256x8  |
clk ---->|         |
         +---------+
```

## Verilog Code

```verilog
// Single-port RAM: 256 x 8
module single_port_ram (
    input  wire        clk,
    input  wire        we,         // write enable (1 = write, 0 = read)
    input  wire [7:0]  addr,       // 8-bit address = 256 locations
    input  wire [7:0]  din,        // data input
    output reg  [7:0]  dout        // data output
);
    // Memory array: 256 locations, each 8 bits
    reg [7:0] mem [0:255];

    // Write operation (synchronous)
    always @(posedge clk) begin
        if (we)
            mem[addr] <= din;
        dout <= mem[addr];  // Read operation (always reads)
    end
endmodule
```

## Testbench Code

```verilog
`timescale 1ns / 1ps

module tb_single_port_ram;
    reg        clk, we;
    reg  [7:0] addr, din;
    wire [7:0] dout;

    single_port_ram uut (.clk(clk), .we(we), .addr(addr), .din(din), .dout(dout));

    always #5 clk = ~clk;

    initial begin
        $monitor("clk=%b we=%b addr=%d din=%d | dout=%d", clk, we, addr, din, dout);

        clk = 0; we = 0; addr = 0; din = 0;

        // Write to address 10
        #10 we = 1; addr = 10; din = 8'd42;
        #10 we = 0;

        // Write to address 20
        #10 we = 1; addr = 20; din = 8'd77;
        #10 we = 0;

        // Read from address 10 (should get 42)
        #10 addr = 10;
        #10;

        // Read from address 20 (should get 77)
        #10 addr = 20;
        #10;

        // Write to address 10 again (overwrite)
        #10 we = 1; addr = 10; din = 8'd99;
        #10 we = 0;

        // Read address 10 again (should get 99)
        #10 addr = 10;
        #10;

        #20 $finish;
    end
endmodule
```

## Expected Output / Waveform

```
clk=0 we=0 addr=0 din=0  | dout=0
clk=1 we=1 addr=10 din=42 | dout=X   (first read, uninitialized)
clk=1 we=0 addr=10 din=42 | dout=42  (read after write)
clk=1 we=1 addr=20 din=77 | dout=42  (reading addr 10)
clk=1 we=0 addr=20 din=77 | dout=77  (now reads addr 20)
clk=1 we=0 addr=10 din=77 | dout=42  (reading addr 10)
clk=1 we=1 addr=10 din=99 | dout=42  (writing to addr 10)
clk=1 we=0 addr=10 din=99 | dout=99  (reading addr 10, sees new value)
```

## Conclusion

Designed a single-port RAM module with 256 x 8 configuration. Write operations store data at the specified address on the rising clock edge, and read operations output the stored data. The simulation confirms correct read-after-write behavior.
