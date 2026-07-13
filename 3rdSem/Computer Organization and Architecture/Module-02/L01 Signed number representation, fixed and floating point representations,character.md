# Signed number representation, fixed and floating point representations,character representation

**Course:** Computer Organization and Architecture  
**Module:** 2 | **Lecture:** 1  
**Date:** 28-Jul-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Signed Number Representation

Binary numbers can represent both positive and negative values. Three common schemes exist.

#### 1.1 Signed Magnitude

- The most significant bit (MSB) is the **sign bit** (0 = positive, 1 = negative).
- The remaining bits represent the **magnitude** (absolute value).
- Example with 4 bits:

| Binary   | Signed Magnitude Value |
|----------|------------------------|
| 0000     | +0                     |
| 0001     | +1                     |
| ...      | ...                    |
| 0111     | +7                     |
| 1000     | -0                     |
| 1001     | -1                     |
| ...      | ...                    |
| 1111     | -7                     |

- Range with n bits: -(2^(n-1) - 1) to +(2^(n-1) - 1) for 4 bits: -7 to +7.
- Disadvantage: two representations for zero (+0 and -0), making arithmetic circuits more complex.

#### 1.2 Ones Complement

- Positive numbers are represented as in signed magnitude.
- Negative numbers are obtained by **complementing all bits** of the positive number.
- Example (4 bits): +5 = 0101, then -5 = 1010.
- Range: -(2^(n-1) - 1) to +(2^(n-1) - 1). Still has two zeros: 0000 (+0) and 1111 (-0).
- Addition requires an **end-around carry** (if a carry out of the MSB occurs, add it back to the LSB).

#### 1.3 Twos Complement

- Positive numbers same as binary.
- Negative numbers: take ones complement and add 1.
- Example (4 bits): +5 = 0101. Ones complement = 1010. Add 1 => 1011 = -5.
- Only one representation for zero: 0000.
- Range: -2^(n-1) to +(2^(n-1) - 1). For 4 bits: -8 to +7.
- Most widely used due to simple arithmetic: **A - B = A + (twos complement of B)**.

| 4-bit Pattern | Signed Magnitude | Ones Complement | Twos Complement |
|---------------|------------------|-----------------|-----------------|
| 0000          | +0               | +0              | 0               |
| 0001          | +1               | +1              | +1              |
| 0010          | +2               | +2              | +2              |
| 0111          | +7               | +7              | +7              |
| 1000          | -0               | -7              | -8              |
| 1001          | -1               | -6              | -7              |
| 1010          | -2               | -5              | -6              |
| 1111          | -7               | -0              | -1              |

**Twos complement extension rule**: To extend an n-bit twos complement number to m bits (m > n), copy the sign bit into all new leftmost positions (sign extension). Example: 1011 (-5 in 4 bits) -> 11111011 (-5 in 8 bits).

---

### 2. Fixed-Point Representation

- The **binary point** (radix point) is assumed at a fixed position.
- Example: for an 8-bit fixed-point representation with 4 integer bits and 4 fractional bits:
  - Bits: b7 b6 b5 b4 . b3 b2 b1 b0
  - Value = b7*2^3 + b6*2^2 + b5*2^1 + b4*2^0 + b3*2^(-1) + b2*2^(-2) + b1*2^(-3) + b0*2^(-4)
  - Example: 0110.1010 = 4 + 2 + 0.5 + 0.125 = 6.625
- Also called Q-format. Qm.n means m integer bits, n fractional bits.
- Limitation: fixed range and precision; cannot represent very large and very small numbers simultaneously.

---

### 3. Floating-Point Representation (IEEE 754 Standard)

Floating-point representation overcomes fixed-point limitations by using a **significand (mantissa)** and an **exponent**.

#### 3.1 General Form
   Value = (-1)^S x M x 2^E

Where:
- S = sign bit (0 positive, 1 negative)
- M = mantissa (significand), usually normalized to 1.xxx...
- E = exponent (biased)

#### 3.2 IEEE 754 Single Precision (32-bit)

| Field   | Bits     | Description                                    |
|---------|----------|------------------------------------------------|
| Sign    | 1 (bit 31) | 0 = positive, 1 = negative                    |
| Exponent| 8 (bits 30-23) | Biased by 127: actual E = stored - 127     |
| Mantissa| 23 (bits 22-0) | Fractional part; implied leading 1 is hidden |

- Biased exponent range: 1 to 254 (actual exponent -126 to +127).
- Special values:
  - Exponent = 0, Mantissa = 0 => zero (+0 and -0).
  - Exponent = 255, Mantissa = 0 => Infinity.
  - Exponent = 255, Mantissa != 0 => NaN (Not a Number).
  - Exponent = 0, Mantissa != 0 => Denormalized numbers (implied leading 0).

**Example 1**: Convert decimal 5.75 to IEEE 754 single precision.

Step 1: Convert to binary.
- Integer part: 5 = 101 (binary)
- Fractional part: 0.75 = 0.11 (binary) because 0.75 * 2 = 1.5 (write 1), 0.5 * 2 = 1.0 (write 1)
- So 5.75 = 101.11 (binary)

Step 2: Normalize.
- Shift binary point left until only one 1 remains to the left: 1.0111 x 2^2
- Mantissa = 0111 (fractional part), exponent = 2.

Step 3: Bias the exponent.
- Bias for single precision = 127. Stored exponent = 2 + 127 = 129 = 10000001 (binary).

Step 4: Assemble.
- Sign = 0 (positive)
- Exponent = 10000001
- Mantissa = 01110000000000000000000 (23 bits, pad with zeros)

Result: 0 10000001 01110000000000000000000 = 0x40B80000 (hex)

**Example 2**: Convert decimal -0.3125 to IEEE 754 single precision.

Step 1: Convert to binary.
- 0.3125 * 2 = 0.625 (write 0)
- 0.625 * 2 = 1.25 (write 1)
- 0.25 * 2 = 0.5 (write 0)
- 0.5 * 2 = 1.0 (write 1)
- So 0.3125 = 0.0101 (binary)

Step 2: Normalize.
- 1.01 x 2^(-2)

Step 3: Bias exponent.
- Stored exponent = -2 + 127 = 125 = 01111101 (binary)

Step 4: Assemble.
- Sign = 1 (negative)
- Exponent = 01111101
- Mantissa = 01000000000000000000000

Result: 1 01111101 01000000000000000000000 = 0xBEA00000 (hex)

#### 3.3 IEEE 754 Double Precision (64-bit)

| Field   | Bits      | Description                                      |
|---------|-----------|--------------------------------------------------|
| Sign    | 1 (bit 63)  | 0 = positive, 1 = negative                     |
| Exponent| 11 (bits 62-52) | Biased by 1023: actual E = stored - 1023     |
| Mantissa| 52 (bits 51-0)  | Fractional part; implied leading 1 is hidden   |

- Actual exponent range: -1022 to +1023.
- Same special value conventions (exponent all 0s or all 1s).

**Example 3**: Convert decimal 3.14159265 to IEEE 754 double precision (approximate).

Step 1: Convert integer part: 3 = 11 (binary).
Step 2: Convert fractional part (repeating approximately):
  0.14159265 * 2 = 0.2831853 -> 0
  0.2831853 * 2 = 0.5663706 -> 0
  0.5663706 * 2 = 1.1327412 -> 1
  0.1327412 * 2 = 0.2654824 -> 0
  0.2654824 * 2 = 0.5309648 -> 0
  ... continues
Approximation: 0.14159265 ~ 0.001001000011111...
So 3.14159265 ~ 11.001001000011111... (binary)

Step 3: Normalize: 1.1001001000011111... x 2^1

Step 4: Mantissa = 1001001000011111... (52 bits)
  Exponent = 1 + 1023 = 1024 = 10000000000 (binary)

Sign = 0
Result: 0 10000000000 1001001000011111101101010100010001000010110100011000

---

### 4. Character Representation

#### 4.1 ASCII (American Standard Code for Information Interchange)

- 7-bit encoding (0-127), often stored in 8-bit byte (MSB = 0).
- Represents English letters (A-Z, a-z), digits (0-9), punctuation, control characters.
- Example: 'A' = 65 = 0x41 = 01000001, 'a' = 97 = 0x61, '0' = 48 = 0x30.
- Extended ASCII: 8-bit (0-255) adds special symbols, but not standardized.

| Char | ASCII (Dec) | Binary (7-bit) |
|------|-------------|----------------|
| A    | 65          | 1000001        |
| B    | 66          | 1000010        |
| Z    | 90          | 1011010        |
| a    | 97          | 1100001        |
| 0    | 48          | 0110000        |
| 9    | 57          | 0111001        |
| LF   | 10          | 0001010        |

#### 4.2 Unicode

- Universal character encoding supporting all world scripts and symbols.
- Common encodings:
  - **UTF-8**: Variable length (1-4 bytes per character). ASCII characters use 1 byte. Backward compatible with ASCII.
  - **UTF-16**: 2 or 4 bytes per character.
  - **UTF-32**: Fixed 4 bytes per character.
- Unicode code points: U+0000 to U+10FFFF.
- Example: 'A' = U+0041 (UTF-8: 0x41), 'Omega' = U+03A9 (UTF-8: 0xCE 0xA9).

---

### Key Takeaways

- Twos complement is the standard for signed integers due to single zero and simple subtraction.
- IEEE 754 standardizes floating-point with sign, biased exponent, and normalized mantissa with hidden bit.
- ASCII (7-bit) and Unicode (variable-length) represent characters; Unicode is the modern standard for multilingual text.

---

## Practice Problems

1. **Signed representation**: Represent the decimal number -27 using 8-bit signed magnitude, ones complement, and twos complement.
   - **Answer**: Signed magnitude: 10011011. Ones complement: 11100100. Twos complement: 11100101.

2. **IEEE 754 conversion**: Convert decimal 13.625 to IEEE 754 single precision (32-bit). Express as hex.
   - **Answer**: 13 = 1101, 0.625 = 0.101. So 13.625 = 1101.101 = 1.101101 x 2^3. Exponent = 3+127=130=10000010. Mantissa = 101101000... Sign=0. Result: 0x415A0000.

3. **ASCII encoding**: What is the binary ASCII representation of the string "COA"?
   - **Answer**: C=67=1000011, O=79=1001111, A=65=1000001. Stored as bytes: 01000011 01001111 01000001.

4. **Fixed-point**: An 8-bit Q4.4 fixed-point number has bits 1101.0110. What is its decimal value (signed, twos complement)?
   - **Answer**: Signed number 1101.0110. The integer part is 1101 = -3 (in 4-bit twos complement). Fractional 0.0110 = 0.375. Total = -3.0 + 0.375 = -2.625.

5. **Floating-point range**: What is the largest normalized positive number in IEEE 754 single precision?
   - **Answer**: Exponent = 254 (bias 127 gives actual +127). Mantissa = all 1s = 1.111... (23 ones) = 2 - 2^(-23). Value = (2 - 2^(-23)) x 2^127 ~ 3.403 x 10^38.
