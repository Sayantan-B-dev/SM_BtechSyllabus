-- ============================================
-- AND Gate
-- Description: AND gate outputs 1 only when
--              ALL inputs are 1.
-- Truth Table:
--   A | B | C
--   0 | 0 | 0
--   0 | 1 | 0
--   1 | 0 | 0
--   1 | 1 | 1
-- ============================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity and_gate is
    Port (
        A : in STD_LOGIC;   -- Input A
        B : in STD_LOGIC;   -- Input B
        C : out STD_LOGIC   -- Output C = A AND B
    );
end and_gate;

architecture Behavioral of and_gate is
begin
    -- Concurrent signal assignment:
    -- C gets the logical AND of A and B
    C <= A AND B;
end Behavioral;
