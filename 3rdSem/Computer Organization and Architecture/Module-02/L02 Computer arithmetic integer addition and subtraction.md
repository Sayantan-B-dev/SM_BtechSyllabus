# Computer arithmetic integer addition and subtraction

**Course:** Computer Organization and Architecture  
**Module:** 2 | **Lecture:** 2  
**Date:** 29-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Binary Addition Rules

Binary addition follows the same principles as decimal addition but with only two digits (0 and 1). The four basic rules are:

| A | B | Sum (A XOR B) | Carry (A AND B) |
|---|---|----------------|------------------|
| 0 | 0 | 0              | 0                |
| 0 | 1 | 1              | 0                |
| 1 | 0 | 1              | 0                |
| 1 | 1 | 0              | 1                |

When a carry-in is included (as in multi-bit addition):

| A | B | Carry-in | Sum   | Carry-out |
|---|---|----------|-------|-----------|
| 0 | 0 | 0        | 0     | 0         |
| 0 | 0 | 1        | 1     | 0         |
| 0 | 1 | 0        | 1     | 0         |
| 0 | 1 | 1        | 0     | 1         |
| 1 | 0 | 0        | 1     | 0         |
| 1 | 0 | 1        | 0     | 1         |
| 1 | 1 | 0        | 0     | 1         |
| 1 | 1 | 1        | 1     | 1         |

**Binary addition example** (4-bit, unsigned):
```
   Carry: 1 1 1 0
      A:   0 1 1 0   (6)
      B:   0 1 0 1   (5)
      ----------
      Sum:  1 0 1 1   (11)
```

### 2. Half Adder

A **half adder** adds two single-bit inputs (A and B) and produces a sum (S) and a carry-out (C).

- S = A XOR B
- C = A AND B

```
   A -----|       |
          | HA    |----- S = A XOR B
   B -----|       |
          |       |----- C = A AND B
          |       |
```

### 3. Full Adder

A **full adder** adds three single-bit inputs (A, B, and Carry-in Ci) and produces a sum (S) and a carry-out (Co).

Logic expressions:
- S = A XOR B XOR Ci
- Co = (A AND B) OR (Ci AND (A XOR B)) = AB + Ci(A XOR B)

```
   A -----|       |
   B -----| FA    |----- S = A XOR B XOR Ci
   Ci ----|       |
          |       |----- Co = AB + Ci(A XOR B)
          |       |
```

### 4. Subtraction Using Twos Complement

In twos complement arithmetic, subtraction is performed by adding the negative of the subtrahend:

**A - B = A + (twos complement of B)**

To compute the twos complement of B:
1. Invert all bits of B (ones complement).
2. Add 1 to the result.

**Example**: Compute 7 - 3 using 4-bit twos complement.

7 = 0111, 3 = 0011
Twos complement of 3: invert 0011 -> 1100, add 1 -> 1101.

Now add:
```
   Carry: 1 1 1 0
      A:   0 1 1 1   (+7)
   (-B):   1 1 0 1   (-3)
   ----------
   Sum:   1 0 1 0 0
```

Discard the final carry-out (since we are using 4 bits): Result = 0100 = +4.

**Example**: Compute 3 - 7 using 4-bit twos complement.

3 = 0011, 7 = 0111
Twos complement of 7: invert 0111 -> 1000, add 1 -> 1001.

```
   Carry: 0 0 1 1
      A:   0 0 1 1   (+3)
   (-B):   1 0 0 1   (-7)
   ----------
   Sum:   1 1 0 0
```

Result = 1100 = -4 (in twos complement). Check: invert 1100 -> 0011, add 1 -> 0100 = 4, so 1100 = -4. Correct.

### 5. Overflow Detection

Overflow occurs when the result of an arithmetic operation exceeds the range that can be represented with the given number of bits.

**Rule for twos complement addition**:
Overflow occurs if and only if the carry into the sign bit (MSB) is **different** from the carry out of the sign bit.

Let Cin be the carry into the MSB and Cout be the carry out of the MSB.
- Overflow = Cin XOR Cout

**Example**: Add +7 (0111) and +5 (0101) in 4 bits.

```
   Carry: 0 1 1 1
      A:   0 1 1 1   (+7)
      B:   0 1 0 1   (+5)
   ----------
   Sum:   1 1 0 0
```

Cin to MSB = 1, Cout from MSB = 0. Cin XOR Cout = 1 => Overflow.
Result 1100 = -4, which is incorrect for +12 (range is -8 to +7). Overflow detected.

**Example**: Add -5 (1011) and -4 (1100) in 4 bits.

```
   Carry: 1 0 1 1
      A:   1 0 1 1   (-5)
      B:   1 1 0 0   (-4)
   ----------
   Sum:   0 1 1 1
```

Cin to MSB = 0, Cout from MSB = 1. Cin XOR Cout = 1 => Overflow.
Result 0111 = +7, which is incorrect for -9 (range is -8 to +7). Overflow detected.

**Example**: No overflow case. Add +3 (0011) and +4 (0100) in 4 bits.

```
   Carry: 0 0 0 0
      A:   0 0 1 1   (+3)
      B:   0 1 0 0   (+4)
   ----------
   Sum:   0 1 1 1
```

Cin = 0, Cout = 0. Cin XOR Cout = 0 => No overflow. Result 0111 = +7. Correct.

### 6. Summary of Conditions

| Operation | Operand A | Operand B | Result valid when...                |
|-----------|-----------|-----------|--------------------------------------|
| A + B     | positive  | positive  | Result sign bit = 0                  |
| A + B     | negative  | negative  | Result sign bit = 1                  |
| A - B     | positive  | negative  | Result sign bit = 0                  |
| A - B     | negative  | positive  | Result sign bit = 1                  |

### 7. Hardware Implementation (ASCII Diagram)

A basic n-bit adder/subtractor unit:

```
                              B register (n bits)
                                    |
                              [Complementer]  (XOR gates controlled by Add/Sub)
                                    |
                    A register     |
                    (n bits)       |
                         |         |
                         v         v
                    +------------------+
                    |    n-bit          |
                    |    Adder          |
                    |                   |
                    +------------------+
                         |
                    +----------+
                    | Overflow |
                    | Detection|
                    +----------+
                         |
                        Sum
```

The Add/Sub control line:
- 0 = Add (B passes through unchanged).
- 1 = Subtract (all bits of B inverted, and carry-in to LSB = 1 to complete twos complement).

The XOR gates act as programmable inverters. When Subtract = 1, each bit of B is flipped (B XOR 1 = NOT B). Together with the 1 carry-in to the LSB, this computes the twos complement.

---

## Practice Problems

1. **Binary addition**: Add 101101 (45) and 011011 (27) using 6-bit binary addition.
<details>
<summary>Show Answer</summary>
     ```
     1111
     101101
     011011
     -------
    1001000  -> Discard carry = 001000 (8). Wait: 45+27=72, 6-bit max 63, so overflow. 001000=8 but real sum 72. Overflow detected.
     ```
</details>

2. **Subtraction**: Compute 12 - 19 using 6-bit twos complement. Check for overflow.
<details>
<summary>Show Answer</summary>
12=001100, 19=001100, complement of 19=110101. Add: 001100+110101=000001 (discard carry). 12-19=-7, result 000001+? Let me recalc: -19 in 6-bit twos complement = 101101. 001100+101101=111001 = -7. No overflow (Cin=Cout=0).
</details>

3. **Overflow detection**: Add 1001 (-7) and 1010 (-6) in 4-bit twos complement. Detect overflow.
<details>
<summary>Show Answer</summary>
     ```
     1 001
     1001
     1010
     -----
    10011
     ```
     Cin=1, Cout=1 => No overflow. Result 0011 = +3? -7 + -6 = -13, out of range for 4 bits (-8 to +7). Wait, Cin into sign bit = 1 (carry from bit 2 to bit 3), Cout from sign bit = 1. 1 XOR 1 = 0 => no overflow detected? But this is wrong because -13 is out of range. Actually, -13 cannot be represented in 4 bits. The carry discard gives 0011 = 3. Let me check: Cin=Cout=1 is the correct overflow condition. Wait, the rule is Cin XOR Cout, which gives 0 (no overflow detected). However, this result is wrong. The correct answer: in 4-bit twos complement, -8 to +7. -7 + -6 = -13 is not representable. But Cin=Cout=1 means no overflow according to the textbook. Actually, I need to re-examine: 1001+1010 = 10011. The MSB (sign bit) addition: 1+1+carry_in=1+1+1=3 = 11, so carry_out=1, sum bit=1. So result is 0011. Cin XOR Cout = 1 XOR 1 = 0 -> no overflow flag. But -13 truly is out of range. The issue: note that -7 and -6 are both negative, and result should be negative, but 0011 is positive. The rule works: when two negative numbers add to a positive, overflow detected by examining sign bits. Cin XOR Cout says no overflow, but we can also check sign(A)=sign(B)=1, sign(result)=0 => overflow. The overflow flag is often set using both rules. Let me verify with standard textbook: In twos complement, overflow = (carry_in_to_MSB XOR carry_out_from_MSB). For 1001+1010: carry bits are: 1+0=1 (bit0), 0+1+carry1=10 (bit1 carry1), 0+0+carry1=01 (bit2 carry0), 1+1+carry0=10 (bit3 carry1). So carry_in_to_MSB = 0, carry_out_from_MSB = 1. Cin XOR Cout = 1 => OVERFLOW. I made an error earlier. Cin (bit2 to bit3) = 0, Cout (bit3 out) = 1. So cin XOR cout = 1 => overflow detected. Correct!
</details>

4. **Twos complement subtraction**: Show step-by-step: 0101 - 0011 using twos complement.
<details>
<summary>Show Answer</summary>
0101 - 0011 = 0101 + (1100+1) = 0101 + 1101 = 0010 (carry 1 discarded) = 2. Correct.
</details>

5. **Hardware**: In the adder/subtractor circuit, why are XOR gates used on the B input?
<details>
<summary>Show Answer</summary>
XOR gates act as controlled inverters. When Subtract=1, each XOR outputs NOT B. Combined with carry-in=1 to the LSB, this produces the twos complement of B, enabling A + (-B) = A - B with the same adder hardware.
</details>