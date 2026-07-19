-- ============================================
-- XOR Gate
-- Description: XOR (exclusive-OR) gate outputs 1
--              when inputs are DIFFERENT.
-- Truth Table:
--   A | B | C
--   0 | 0 | 0
--   0 | 1 | 1
--   1 | 0 | 1
--   1 | 1 | 0
-- ============================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity xor_gate is
    Port (
        A : in STD_LOGIC;   -- Input A
        B : in STD_LOGIC;   -- Input B
        C : out STD_LOGIC   -- Output C = A XOR B
    );
end xor_gate;

architecture Behavioral of xor_gate is
begin
    -- Concurrent signal assignment:
    -- C gets the logical XOR of A and B
    C <= A XOR B;
end Behavioral;
