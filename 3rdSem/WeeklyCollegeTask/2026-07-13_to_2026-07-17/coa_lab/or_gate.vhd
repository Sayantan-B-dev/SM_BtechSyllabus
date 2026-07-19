-- ============================================
-- OR Gate
-- Description: OR gate outputs 1 when AT LEAST
--              ONE input is 1.
-- Truth Table:
--   A | B | C
--   0 | 0 | 0
--   0 | 1 | 1
--   1 | 0 | 1
--   1 | 1 | 1
-- ============================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity or_gate is
    Port (
        A : in STD_LOGIC;   -- Input A
        B : in STD_LOGIC;   -- Input B
        C : out STD_LOGIC   -- Output C = A OR B
    );
end or_gate;

architecture Behavioral of or_gate is
begin
    -- Concurrent signal assignment:
    -- C gets the logical OR of A and B
    C <= A OR B;
end Behavioral;
