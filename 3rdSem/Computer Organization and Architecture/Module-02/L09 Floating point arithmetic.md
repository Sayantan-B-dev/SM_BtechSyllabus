# Floating point arithmetic

**Course:** Computer Organization and Architecture  
**Module:** 2 | **Lecture:** 9  
**Date:** 12-Aug-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. IEEE 754 Floating-Point Review

IEEE 754 single precision (32-bit) format:

| S (1) | Exponent E (8) | Mantissa M (23) |
|-------|----------------|-----------------|

- Value = (-1)^S x (1.M) x 2^(E - 127)
- Bias = 127 for single, 1023 for double.

#### Special Values

| Exponent | Mantissa | Value               |
|----------|----------|---------------------|
| 0        | 0        | Zero (+0 / -0)      |
| 0        | non-zero | Denormalized number |
| 1-254    | any      | Normalized number   |
| 255      | 0        | Infinity            |
| 255      | non-zero | NaN (Not a Number)  |

---

### 2. Floating-Point Addition and Subtraction

Floating-point addition/subtraction is more complex than integer addition because the operands may have different exponents.

#### Algorithm Steps

Given two IEEE 754 floating-point numbers X and Y:

**Step 1: Check for zero.**
   If either operand is zero, the result is the other operand (with appropriate sign handling).

**Step 2: Align mantissas (equalize exponents).**
   - Subtract exponents: d = |Ex - Ey|.
   - Shift the mantissa of the number with the smaller exponent right by d bits.
   - Increase the smaller exponent by d.

**Step 3: Add or subtract the mantissas.**
   - If signs are the same, add the mantissas.
   - If signs differ, subtract the smaller mantissa from the larger.
   - The result sign is the sign of the larger operand.

**Step 4: Normalize the result.**
   - If the mantissa sum >= 2 (carry out), shift mantissa right by 1 and increment exponent.
   - If the mantissa sum < 1 (leading zero), shift mantissa left and decrement exponent until the leading 1 is in the correct position.
   - Check for exponent overflow/underflow.

**Step 5: Round the mantissa.**
   - Apply rounding (round to nearest, round toward zero, etc.).
   - If rounding causes carry-out, re-normalize.

**Step 6: Assemble the result.**
   - Combine sign, exponent, and mantissa into IEEE 754 format.
   - Check for overflow/underflow and return special values if needed.

#### ASCII Flowchart

```
    X (Sx, Ex, Mx)      Y (Sy, Ey, My)
         |                    |
         +--+-------+--------+
            |       |
            v       v
     +-----------------+
     | Check for zero  |
     +-----------------+
            |
            v
     +-----------------+
     | Align mantissas |
     | (shift smaller  |
     | exponent right) |
     +-----------------+
            |
            v
     +-----------------+
     | Add/Subtract    |
     | Mantissas       |
     +-----------------+
            |
            v
     +-----------------+
     | Normalize       |
     | (shift left or  |
     | right)          |
     +-----------------+
            |
            v
     +-----------------+
     | Round           |
     +-----------------+
            |
            v
     +-----------------+
     | Assemble result |
     +-----------------+
            |
            v
         Result
```

#### Worked Example: Add Two Single-Precision Floats

Add X = 12.5 and Y = 7.375 using IEEE 754 single precision.

**Step 1: Convert to IEEE 754.**

X = 12.5:
- 12 = 1100, 0.5 = 0.1 => 1100.1 = 1.1001 x 2^3
- S = 0, E = 3 + 127 = 130 = 10000010, M = 10010000000000000000000

Y = 7.375:
- 7 = 111, 0.375 = 0.011 => 111.011 = 1.11011 x 2^2
- S = 0, E = 2 + 127 = 129 = 10000001, M = 11011000000000000000000

**Step 2: Align mantissas.**

Ex = 3, Ey = 2, d = |3 - 2| = 1.
Y has the smaller exponent. Shift Y's mantissa right by 1:
- My (original) = 1.11011
- My (aligned) = 0.111011 (exponent becomes 3)

Now both have exponent 3:
- X: 1.1001 x 2^3
- Y: 0.111011 x 2^3

**Step 3: Add mantissas.**
Since both signs are positive, add the mantissas:

```
   1.10010000000000000000000
+  0.11101100000000000000000
----------------------------
  10.01111100000000000000000
```

Result: 10.011111 x 2^3

**Step 4: Normalize.**
Mantissa >= 2 (carry out), so shift right by 1 and increment exponent:
- Mantissa = 1.001111100000000000000000
- Exponent = 3 + 1 = 4

**Step 5: Round.**
Assume round-to-nearest. The mantissa fits in 23 bits with no extra bits set, so no rounding needed.

**Step 6: Assemble.**
- S = 0
- E = 4 + 127 = 131 = 10000011
- M = 00111110000000000000000

Result: 0 10000011 00111110000000000000000 = 0x419F0000

Check: 1.0011111 x 2^4 = 10011.111 = 16 + 2 + 1 + 0.5 + 0.25 + 0.125 + 0.0625 = 19.875 + 0.9375? Let me compute: 10011.111 = 16 + 0 + 0 + 2 + 1 + 0.5 + 0.25 + 0.125 = 19.875. And 12.5 + 7.375 = 19.875. Correct!

#### Example 2: Subtraction (X - Y where signs differ)

Compute X = 8.5 - 3.25.

X = 8.5:
- 8.5 = 1000.1 = 1.0001 x 2^3
- S=0, E=130, M=00010000000000000000000

Y = 3.25:
- 3.25 = 11.01 = 1.101 x 2^1
- S=0, E=128, M=10100000000000000000000

We compute X + (-Y). So effectively X - Y.

Step 2: Align.
Ex=3, Ey=1, d=2. Shift Y mantissa right by 2:
- My = 0.01101 x 2^3

Step 3: Subtract (since X is positive, Y is treated as negative, so we compute X - Y):
```
   1.00010000000000000000000
-  0.01101000000000000000000
----------------------------
   0.10101000000000000000000
```

Step 4: Normalize.
Leading bit is at position 0 (result < 1). Shift left by 1:
- Mantissa = 1.0101000000000000000000
- Exponent = 3 - 1 = 2

Step 5: Round. No rounding needed.

Step 6: Assemble.
- S = 0
- E = 2 + 127 = 129 = 10000001
- M = 01010000000000000000000

Result: 0 10000001 01010000000000000000000

Check: 1.0101 x 2^2 = 101.01 = 5.25. And 8.5 - 3.25 = 5.25. Correct.

---

### 3. Floating-Point Multiplication

Multiplication is simpler than addition: exponents are added and mantissas are multiplied.

#### Algorithm Steps

Given X = (-1)^Sx x Mx x 2^Ex, Y = (-1)^Sy x My x 2^Ey:

**Step 1: Check for zero.**
   If either operand is zero, result is zero.

**Step 2: Add exponents.**
   - E_result = Ex + Ey - bias (since both are biased).
   - For single precision: E_result = (Ex - 127) + (Ey - 127) + 127 = Ex + Ey - 127.
   - Check for exponent overflow/underflow.

**Step 3: Multiply mantissas.**
   - Mx x My (both in the range 1 to 2, so product is in range 1 to 4).
   - Use integer multiplication of 24-bit numbers (including the hidden 1).
   - Result: up to 48 bits.

**Step 4: Normalize.**
   - If product >= 2 (carry into bit 48), shift right by 1 and increment exponent.
   - If product < 1 (should not happen for normalized inputs), shift left.

**Step 5: Round.**
   - Round the mantissa to 23 (or 52) bits.
   - Re-normalize if carry occurs from rounding.

**Step 6: Determine sign.**
   - S_result = Sx XOR Sy.

**Step 7: Assemble result.**

#### Worked Example: Multiply Two Single-Precision Floats

Compute X x Y where X = 4.5 and Y = 2.0.

**Step 1: Convert to IEEE 754.**

X = 4.5 = 100.1 = 1.001 x 2^2
- Sx = 0, Ex = 2 + 127 = 129 = 10000001, Mx = 00100000000000000000000

Y = 2.0 = 10.0 = 1.0 x 2^1
- Sy = 0, Ey = 1 + 127 = 128 = 10000000, My = 00000000000000000000000

**Step 2: Add exponents.**
E_result = Ex + Ey - 127 = 129 + 128 - 127 = 130 = 10000010

**Step 3: Multiply mantissas.**
Mx = 1.001, My = 1.000
1.001 x 1.000 = 1.001000 (product = 1.001 x 2^0 = 1.001)
Let me do the multiplication:
  1.001 (9/8)
x 1.000 (1)
= 1.001000 (9/8 = 1.125)

Actually 4.5 x 2 = 9. So the result should represent 9.

**Step 4: Normalize.**
Product = 1.001 (between 1 and 2), so no normalization needed.
E_result = 130 (no change).

**Step 5: Round.** No rounding needed.

**Step 6: Sign.** 0 XOR 0 = 0 (positive).

**Step 7: Assemble.**
- S = 0
- E = 130 = 10000010
- M = 00100000000000000000000

Result: 0 10000010 00100000000000000000000

Check: 1.001 x 2^(130-127) = 1.001 x 2^3 = 1001.0 = 9.0. And 4.5 x 2.0 = 9.0. Correct.

#### Worked Example: Multiplication with Normalization

Compute 3.0 x 5.0.

X = 3.0 = 11.0 = 1.1 x 2^1
- Sx=0, Ex=128, Mx=10000000000000000000000

Y = 5.0 = 101.0 = 1.01 x 2^2
- Sy=0, Ey=129, My=01000000000000000000000

Step 2: E_result = 128 + 129 - 127 = 130 = 10000010

Step 3: Multiply mantissas.
Mx = 1.1, My = 1.01
   1.1
x  1.01
-------
   1.1
  0.00
 1.1
-------
 1.111

Product = 1.111 = 15/8 = 1.875

Step 4: Normalize. Product < 2, so no shift needed.

Step 6: Sign = 0.

Step 7: S=0, E=130=10000010, M=11100000000000000000000

Result: 1.111 x 2^(130-127) = 1.111 x 2^3 = 1111.0 = 15.0. 3 x 5 = 15. Correct.

---

### 4. Special Values in Floating-Point Arithmetic

#### NaN (Not a Number)

- Representation: Exponent = all 1s, Mantissa != 0.
- Produced by: 0/0, infinity - infinity, sqrt(-1), etc.
- NaN propagates through operations: any operation with NaN produces NaN.
- Two types:
  - **Quiet NaN (QNaN)**: MSB of mantissa = 1. Does not raise exception.
  - **Signaling NaN (SNaN)**: MSB of mantissa = 0. Raises exception when used.

#### Infinity

- Representation: Exponent = all 1s, Mantissa = 0.
- Produced by: overflow, division by zero.
- Rules:
  - infinity + infinity = infinity
  - infinity - infinity = NaN
  - infinity * infinity = infinity
  - infinity / infinity = NaN
  - Any finite number / infinity = 0
  - infinity + finite = infinity

#### Denormalized Numbers

- Representation: Exponent = 0, Mantissa != 0.
- Hidden bit is 0 instead of 1: value = (-1)^S x 0.M x 2^(-126)
- Purpose: Allow **gradual underflow**. When the exponent goes below the minimum, the mantissa is denormalized (leading zeros are allowed) instead of going to zero abruptly.
- Example: The smallest positive normalized single-precision number is 1.0 x 2^(-126) ~ 1.18 x 10^(-38). The smallest positive denormal is 2^(-149) ~ 1.4 x 10^(-45).

| Value Type      | Binary (Single Precision)          | Decimal (approx)                  |
|-----------------|------------------------------------|-----------------------------------|
| Largest normal  | 0 11111110 111...111 (23 ones)     | 3.403 x 10^38                    |
| Smallest normal | 0 00000001 000...000 (23 zeros)    | 1.175 x 10^(-38)                 |
| Smallest denorm | 0 00000000 000...001 (22 zeros, 1) | 1.401 x 10^(-45)                 |
| Zero            | 0 00000000 000...000 (23 zeros)    | 0.0                              |

#### IEEE 754 Special Value Handling Table

| Operation          | Result Situation                  | IEEE 754 Result  |
|--------------------|-----------------------------------|------------------|
| n / 0             | n != 0                            | Infinity (signed)|
| 0 / 0             | indeterminate                     | NaN              |
| n / infinity      | finite                            | 0 (signed)       |
| infinity + inf    | same sign                         | Infinity         |
| infinity - inf    | opposite sign                     | NaN              |
| 0 * infinity      | indeterminate                     | NaN              |
| sqrt(x)           | x < 0                             | NaN              |
| Overflow          | exponent too large                | Infinity         |
| Underflow         | exponent too small                | Denormal or 0    |

---

### 5. Guard Bits and Rounding

In floating-point arithmetic, intermediate results have extra bits (guard, round, sticky) to improve accuracy.

#### Guard, Round, Sticky Bits

- **Guard bit (G)**: First bit beyond the LSB of the mantissa (bit 24 for single precision).
- **Round bit (R)**: Second bit beyond the LSB.
- **Sticky bit (S)**: OR of all remaining bits beyond the round bit.

During alignment, the shifted-out bits are captured in these three bits. They determine the rounding.

#### Rounding Modes

IEEE 754 defines four rounding modes:

1. **Round to nearest (ties to even)**: Default. Round to the nearest representable value. If exactly midway, round to even LSB.
2. **Round toward zero (truncate)**: Discard extra bits.
3. **Round toward +infinity (ceil)**: Round up.
4. **Round toward -infinity (floor)**: Round down.

---

## Practice Problems

1. **Floating-point addition**: Add 6.75 and 2.5 in IEEE 754 single precision. Show all steps.
   - **Answer**:
     6.75 = 110.11 = 1.1011 x 2^2. IEEE: S=0, E=129, M=10110000000000000000000.
     2.5 = 10.1 = 1.01 x 2^1. IEEE: S=0, E=128, M=01000000000000000000000.
     Align: shift 2.5 right by 1: 0.101 x 2^2.
     Add: 1.1011 + 0.101 = 10.0101. Normalize: 1.00101 x 2^3.
     Result: S=0, E=130, M=00101000000000000000000 = 0x41140000.
     Check: 6.75+2.5=9.25. 1.00101 x 2^3 = 1001.01 = 9.25. Correct.

2. **Floating-point multiplication**: Multiply 1.5 x 3.5 using IEEE 754 single precision.
   - **Answer**:
     1.5 = 1.1 x 2^0. S=0, E=127, M=10000000000000000000000.
     3.5 = 11.1 = 1.11 x 2^1. S=0, E=128, M=11000000000000000000000.
     E_result = 127+128-127 = 128.
     M_prod = 1.1 x 1.11 = 10.101. Normalize: 1.0101 x 2^1.
     E = 128+1 = 129. M = 01010000000000000000000.
     Result: 0x404A0000. Check: 1.0101 x 2^(129-127) = 1.0101 x 2^2 = 101.01 = 5.25. 1.5x3.5=5.25. Correct.

3. **Special values**: What is the result of 0.0 / 0.0 in IEEE 754?
   - **Answer**: NaN (Not a Number). The operation is indeterminate (0/0 has no well-defined value), so IEEE 754 returns NaN with exponent all 1s and non-zero mantissa. This propagates through subsequent operations.

4. **Denormalized numbers**: What is the value of the IEEE 754 single-precision number 0x00300000?
   - **Answer**: 0x00300000 = 0 00000000 01100000000000000000000.
     Exponent = 0 (denormalized), so hidden bit = 0.
     Mantissa = 0.011 x 2^(-126) = 0.375 x 2^(-126) = 3 x 2^(-128) ~ 8.82 x 10^(-39).

5. **Guard and rounding**: Suppose a single-precision mantissa after alignment is 1.01010101010101010101011 1001 (23 fraction bits + guard=1, round=0, sticky=1). What is the rounded result using round-to-nearest (ties to even)?
   - **Answer**: The guard bits are 101 (G=1, R=0, S=1). Since G=1 and (R OR S) = 1, we round up (add 1 to LSB). The mantissa becomes 1.01010101010101010101100.
