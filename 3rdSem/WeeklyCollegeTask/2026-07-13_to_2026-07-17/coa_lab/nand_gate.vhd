-- ============================================
-- NAND Gate
-- Description: NAND gate outputs 0 only when
--              ALL inputs are 1 (inverse of AND).
-- Truth Table:
--   A | B | C
--   0 | 0 | 1
--   0 | 1 | 1
--   1 | 0 | 1
--   1 | 1 | 0
-- ============================================

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity nand_gate is
    Port (
        A : in STD_LOGIC;   -- Input A
        B : in STD_LOGIC;   -- Input B
        C : out STD_LOGIC   -- Output C = A NAND B
    );
end nand_gate;

architecture Behavioral of nand_gate is
begin
    -- Concurrent signal assignment:
    -- C gets the logical NAND of A and B
    C <= A NAND B;
end Behavioral;
