-- ============================================
-- XNOR Gate
-- Description: XNOR (exclusive-NOR) gate outputs 1
--              when inputs are SAME.
-- Truth Table:
--   A | B | C
--   0 | 0 | 1
--   0 | 1 | 0
--   1 | 0 | 0
--   1 | 1 | 1
-- ============================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity xnor_gate is
    Port (
        A : in STD_LOGIC;   -- Input A
        B : in STD_LOGIC;   -- Input B
        C : out STD_LOGIC   -- Output C = A XNOR B
    );
end xnor_gate;

architecture Behavioral of xnor_gate is
begin
    -- Concurrent signal assignment:
    -- C gets the logical XNOR of A and B
    C <= A XNOR B;
end Behavioral;
