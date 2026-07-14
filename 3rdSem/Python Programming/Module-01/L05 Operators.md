# Operators

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 5  
**Date:** 15-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

An **operator** is a symbol that performs an operation on one or more **operands** (values). For example, in `5 + 3`, `+` is the operator and `5` and `3` are operands.

Python has seven categories of operators.

---

### 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division (float) | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `10 ** 3` | `1000` |

```python
# Arithmetic operators in action
a = 15
b = 4

print(f"a + b = {a + b}")   # 19
print(f"a - b = {a - b}")   # 11
print(f"a * b = {a * b}")   # 60
print(f"a / b = {a / b}")   # 3.75
print(f"a // b = {a // b}")  # 3 (floor division)
print(f"a % b = {a % b}")    # 3 (remainder)
print(f"a ** b = {a ** b}")  # 50625 (15^4)
```

**Important details about division:**

```python
# Division always returns a float
print(10 / 5)      # 2.0 (not 2!)
print(10 // 5)     # 2 (integer division)

# Floor division with negative numbers
print(10 // 3)     # 3
print(-10 // 3)    # -4 (floors down, rounds towards negative infinity)
print(10 // -3)    # -4

# Modulus with negative numbers
print(10 % 3)      # 1
print(-10 % 3)     # 2  (result has same sign as divisor)
print(10 % -3)     # -2
```

**Operator with strings:**

```python
# + concatenates strings
print("Hello" + " " + "World")  # Hello World

# * repeats strings
print("Ha" * 3)  # HaHaHa
print(3 * "Ha")  # HaHaHa (order doesn't matter)
```

---

### 2. Comparison (Relational) Operators

Used to compare two values. Always return a boolean (`True` or `False`).

| Operator | Name | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

**Examples:**

```python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 10)  # True
print(a <= 10)  # True

# Comparison works with strings (lexicographic order)
print("apple" < "banana")  # True (a comes before b)
print("apple" > "Apple")   # True (lowercase > uppercase in ASCII)

# Chained comparisons
print(5 < 10 < 15)   # True (equivalent to: 5 < 10 and 10 < 15)
print(5 < 10 > 15)   # False (5 < 10 is True, but 10 > 15 is False)
```

**Common mistake: `=` vs `==`**

```python
# = is assignment
x = 10

# == is comparison
if x == 10:   # Correct
    print("x is 10")

# if x = 10:  # SyntaxError (cannot use assignment in condition)
```

---

### 3. Logical Operators

Used to combine conditional statements. Return boolean values.

| Operator | Description | Example | Result |
|---|---|---|---|
| `and` | True if both operands are true | `True and False` | `False` |
| `or` | True if at least one operand is true | `True or False` | `True` |
| `not` | Inverts the boolean value | `not True` | `False` |

**Truth tables:**

| A | B | A and B | A or B | not A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

**Examples:**

```python
age = 20
has_license = True

# and: both conditions must be true
if age >= 18 and has_license:
    print("You can drive")  # This prints

# or: at least one condition must be true
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No work today!")  # This prints

# not: reverses the condition
is_raining = False
if not is_raining:
    print("No umbrella needed")  # This prints
```

**Short-circuit evaluation:**

Python evaluates `and` and `or` using short-circuit logic:
- For `and`: if the first operand is `False`, Python does **not** evaluate the second operand (because the result is already known to be `False`).
- For `or`: if the first operand is `True`, Python does **not** evaluate the second operand.

```python
def get_true():
    print("get_true() called")
    return True

def get_false():
    print("get_false() called")
    return False

print(get_false() and get_true())  # Only get_false() is called
print(get_true() or get_false())   # Only get_true() is called
```

---

### 4. Assignment Operators

Used to assign values to variables. Compound assignment operators combine assignment with another operation.

| Operator | Example | Equivalent to |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `\|=` | `x \|= 3` | `x = x \| 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `<<=` | `x <<= 3` | `x = x << 3` |
| `>>=` | `x >>= 3` | `x = x >> 3` |

```python
x = 10
print(x)   # 10

x += 5     # x = x + 5
print(x)   # 15

x -= 3     # x = x - 3
print(x)   # 12

x *= 2     # x = x * 2
print(x)   # 24

x //= 5    # x = x // 5
print(x)   # 4

x **= 3    # x = x ** 3
print(x)   # 64
```

---

### 5. Bitwise Operators

Operate on integers at the binary (bit) level. Rarely used in day-to-day programming but important for systems programming, cryptography, and performance optimization.

| Operator | Name | Description |
|---|---|---|
| `&` | AND | Sets each bit to 1 if both bits are 1 |
| `|` | OR | Sets each bit to 1 if at least one bit is 1 |
| `^` | XOR | Sets each bit to 1 if exactly one bit is 1 |
| `~` | NOT | Inverts all bits (unary) |
| `<<` | Left shift | Shifts bits left by specified positions |
| `>>` | Right shift | Shifts bits right by specified positions |

**Example with `a = 5` (binary `0101`) and `b = 3` (binary `0011`):**

```python
a = 5   # 0101 in binary
b = 3   # 0011 in binary

print(f"a & b = {a & b}")   # 1  (0001)
print(f"a | b = {a | b}")   # 7  (0111)
print(f"a ^ b = {a ^ b}")   # 6  (0110)
print(f"~a = {~a}")         # -6 (inverts all bits)
print(f"a << 1 = {a << 1}") # 10 (1010) -- multiply by 2
print(f"a >> 1 = {a >> 1}") # 2  (0010) -- integer divide by 2
```

**Step-by-step binary calculation for `a & b`:**

```
  0101  (5)
& 0011  (3)
  ----
  0001  (1)  -- only the LSB is 1 in both numbers
```

**Step-by-step for `a << 1`:**

```
  0101  (5)   original
 1010  (10)  shift left by 1 (add a 0 at the end)
```

Left shift by `n` is equivalent to multiplying by `2^n`. Right shift by `n` is equivalent to floor division by `2^n`.

---

### 6. Membership Operators

Used to test whether a value is present in a sequence (string, list, tuple, set, dictionary).

| Operator | Description | Example | Result |
|---|---|---|---|
| `in` | True if value is found | `'a' in 'apple'` | `True` |
| `not in` | True if value is not found | `'z' not in 'apple'` | `True` |

```python
# With strings
text = "Hello, World!"
print("Hello" in text)      # True
print("hello" in text)      # False (case-sensitive)
print("xyz" not in text)    # True

# With lists
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("mango" in fruits)    # False

# With dictionaries (checks keys by default)
student = {"name": "Alice", "age": 22}
print("name" in student)    # True (checks keys)
print("Alice" in student)   # False (values are not checked)

# Check values in dictionary
print("Alice" in student.values())  # True
```

---

### 7. Identity Operators

Used to compare the memory locations (identities) of two objects.

| Operator | Description | Example |
|---|---|---|
| `is` | True if both variables refer to the same object | `x is y` |
| `is not` | True if variables refer to different objects | `x is not y` |

```python
# is vs ==
# == compares VALUES
# is compares IDENTITIES (memory addresses)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same values)
print(a is b)   # False (different objects in memory)
print(a is c)   # True (c references the same object as a)

# Integer caching (small integers are reused)
x = 256
y = 256
print(x is y)   # True (Python caches small integers -5 to 256)

x = 257
y = 257
print(x is y)   # False (large integers are not cached)
```

**IMPORTANT:** Always use `==` to compare values. Use `is` only when you specifically need to check if two variables point to the same object (e.g., checking for `None`).

```python
# Correct way to check for None
if result is None:
    print("No result")

# Also works but not idiomatic
if result == None:
    print("No result")
```

---

### 8. Operator Precedence

When an expression has multiple operators, Python evaluates them in a specific order. The table below lists operators from highest precedence (evaluated first) to lowest.

| Precedence | Operator | Description |
|---|---|---|
| 1 (highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shift |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, identity, membership |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

**Examples demonstrating precedence:**

```python
# Without parentheses -- follows precedence
result = 5 + 3 * 2
print(result)  # 11 (multiplication first: 5 + 6)

# With parentheses -- explicit
result = (5 + 3) * 2
print(result)  # 16 (addition first: 8 * 2)

# Exponentiation is right-associative
print(2 ** 3 ** 2)  # 512 (evaluated as 2 ** (3 ** 2) = 2 ** 9)

# Mixed logical operators
print(True or False and False)   # True (and has higher precedence: True or False -> True)
print((True or False) and False) # False (or evaluated first: True and False -> False)
```

**Best practice:** When in doubt, use parentheses to make your intention clear. It improves readability even when the precedence is correct.

```python
# Unclear
if age >= 18 and has_license or is_approved:
    pass

# Clear
if (age >= 18 and has_license) or is_approved:
    pass
```

---

### 9. Complete Example: Using Multiple Operators

```python
# A program that demonstrates various operators

a = 10
b = 3

print("=== Arithmetic Operators ===")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

print("\n=== Comparison Operators ===")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")

print("\n=== Logical Operators ===")
x, y = True, False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

print("\n=== Membership Operators ===")
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'mango' not in fruits: {'mango' not in fruits}")

print("\n=== Identity Operators ===")
p = [1, 2]
q = [1, 2]
r = p
print(f"p is q: {p is q}")
print(f"p is r: {p is r}")
```

**Output:**

```
=== Arithmetic Operators ===
a + b = 13
a - b = 7
a * b = 30
a / b = 3.3333333333333335
a // b = 3
a % b = 1
a ** b = 1000

=== Comparison Operators ===
a == b: False
a != b: True
a > b: True
a < b: False

=== Logical Operators ===
x and y: False
x or y: True
not x: False

=== Membership Operators ===
'banana' in fruits: True
'mango' not in fruits: True

=== Identity Operators ===
p is q: False
p is r: True
```

---

## Practice Problems

1. **Operator Challenge:** Evaluate the following expressions manually, then verify with Python:
   - `10 + 5 * 2`
   - `(10 + 5) * 2`
   - `17 % 3 + 4`
   - `2 ** 3 ** 2`
   - `True or False and not False`
   <details>
   <summary>Show Answer</summary>
   - `10 + 5 * 2` → `10 + 10` → `20`
   - `(10 + 5) * 2` → `15 * 2` → `30`
   - `17 % 3 + 4` → `2 + 4` → `6`
   - `2 ** 3 ** 2` → `2 ** 9` → `512` (right-associative)
   - `True or False and not False` → `True or (False and True)` → `True or False` → `True`
   </details>

2. **Even or Odd (bitwise):** Use the bitwise AND operator `&` to check if a number is even or odd. (Hint: `x & 1` is `1` for odd numbers, `0` for even numbers.)
   <details>
   <summary>Show Answer</summary>
   ```python
   x = int(input("Enter a number: "))
   if x & 1:
       print(f"{x} is odd")
   else:
       print(f"{x} is even")
   ```
   </details>

3. **Leap Year Logic:** Write an expression that checks if a year is a leap year:
   - Divisible by 4, but not by 100, unless also divisible by 400.
   - Use logical operators (`and`, `or`, `not`).
   <details>
   <summary>Show Answer</summary>
   ```python
   year = int(input("Enter year: "))
   is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
   print(f"{year} is{' ' if is_leap else ' not '}a leap year")
   ```
   </details>

4. **Identity vs Equality:** Create two lists `a = [1, 2, 3]` and `b = [1, 2, 3]`. Check `a == b` and `a is b`. Now set `c = a`. Check `c is a`. Explain the difference.
   <details>
   <summary>Show Answer</summary>
   ```python
   a = [1, 2, 3]
   b = [1, 2, 3]
   c = a
   print(a == b)   # True - same values
   print(a is b)   # False - different objects in memory
   print(c is a)   # True - c references the same object as a
   ```
   `==` checks **value equality** (do they contain the same data?). `is` checks **identity** (do they refer to the same object in memory?).
   </details>

5. **Assignment Chain:** Using compound assignment operators, start with `x = 100`. Apply `//=` by 3, then `**=` by 2, then `-=` by 5. What is the final value of `x`?
   <details>
   <summary>Show Answer</summary>
   ```python
   x = 100
   x //= 3   # x = 33
   x **= 2   # x = 1089
   x -= 5    # x = 1084
   print(x)  # 1084
   ```
   </details>
