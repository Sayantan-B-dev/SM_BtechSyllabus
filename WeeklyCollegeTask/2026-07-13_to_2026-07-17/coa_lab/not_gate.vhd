-- ============================================
-- NOT Gate
-- Description: A NOT gate (inverter) outputs
--              the logical complement of input.
-- Truth Table:
--   A | C
--   0 | 1
--   1 | 0
-- ============================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity not_gate is
    Port (
        A : in STD_LOGIC;   -- Input signal
        C : out STD_LOGIC   -- Output signal (inverted)
    );
end not_gate;

architecture Behavioral of not_gate is
begin
    -- Concurrent signal assignment:
    -- C gets the logical NOT of A
    C <= NOT A;
end Behavioral;
