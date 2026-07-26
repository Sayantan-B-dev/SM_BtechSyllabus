-- ==========================================================
-- Program    : Design and Implementation of Half Adder Using VHDL
-- File Name  : half_adder.vhd
-- Inputs     : A, B
-- Outputs    : S (Sum), C (Carry)
--
-- Truth Table
-- A  B | S  C
-- 0  0 | 0  0
-- 0  1 | 1  0
-- 1  0 | 1  0
-- 1  1 | 0  1
-- ==========================================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity half_adder is
    Port (
        A : in STD_LOGIC;
        B : in STD_LOGIC;
        S : out STD_LOGIC;
        C : out STD_LOGIC
    );
end half_adder;

architecture Behavioral of half_adder is
begin

    S <= A XOR B;
    C <= A AND B;

end Behavioral;