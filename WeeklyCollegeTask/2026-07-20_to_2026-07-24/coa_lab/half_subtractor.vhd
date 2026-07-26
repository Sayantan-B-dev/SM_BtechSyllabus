-- ==========================================================
-- Program    : Design and Implementation of Half Subtractor Using VHDL
-- File Name  : half_subtractor.vhd
-- Inputs     : A, B
-- Outputs    : D (Difference), Borrow
--
-- Truth Table
-- A  B | D  Borrow
-- 0  0 | 0     0
-- 0  1 | 1     1
-- 1  0 | 1     0
-- 1  1 | 0     0
-- ==========================================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity half_subtractor is
    Port (
        A      : in STD_LOGIC;
        B      : in STD_LOGIC;
        D      : out STD_LOGIC;
        Borrow : out STD_LOGIC
    );
end half_subtractor;

architecture Behavioral of half_subtractor is
begin

    D      <= A XOR B;
    Borrow <= (NOT A) AND B;

end Behavioral;
