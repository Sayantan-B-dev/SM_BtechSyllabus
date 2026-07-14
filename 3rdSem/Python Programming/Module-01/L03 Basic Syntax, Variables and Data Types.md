# Basic Syntax, Variables and Data Types

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 3  
**Date:** 13-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

### 1. Python Syntax Basics

#### 1.1 Case Sensitivity

Python is **case-sensitive**. This means `name`, `Name`, and `NAME` are three different identifiers.

```python
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)   # Alice
print(Name)   # Bob
print(NAME)   # Charlie
```

#### 1.2 Indentation

Python uses **indentation** (whitespace at the beginning of a line) to define blocks of code. Unlike C, Java, or JavaScript (which use curly braces `{}`), Python requires consistent indentation -- typically 4 spaces per level.

```python
# Correct indentation
if 5 > 2:
    print("Five is greater than two!")  # This line is indented

# Incorrect indentation -- this will cause an IndentationError
if 5 > 2:
print("This line is not indented")
```

**Output of incorrect code:**

```
  File "example.py", line 3
    print("This line is not indented")
    ^
IndentationError: expected an indented block
```

**Rules:**
- Use spaces or tabs, but **do not mix them** (Python 3 disallows mixing).
- The standard convention is **4 spaces per indentation level**.
- All statements in a block must have the same indentation.

#### 1.3 Comments

Comments are lines of code that Python ignores. They are used to explain code to human readers.

**Single-line comments** start with `#`:

```python
# This is a comment
print("Hello")  # This is also a comment (inline comment)
```

**Multi-line comments** use triple quotes (single or double). These are technically string literals, but when not assigned to a variable, they act as comments:

```python
'''
This is a multi-line comment.
It can span multiple lines.
Python will ignore it.
'''

print("After the comment")
```

Or with double quotes:

```python
"""
Another way to write
multi-line comments.
"""
```

---

### 2. Variables in Python

A **variable** is a named location in memory that stores a value. In Python, you create a variable by assigning a value to a name using the `=` operator.

```python
message = "Hello, Python!"   # string variable
age = 20                     # integer variable
price = 99.99                # float variable
is_student = True            # boolean variable
```

#### 2.1 Dynamic Typing

Python is **dynamically typed** -- you do not need to declare the type of a variable. The interpreter infers the type from the value you assign. Moreover, a variable can change its type during execution:

```python
x = 10        # x is an integer
print(type(x))  # <class 'int'>

x = "hello"   # now x is a string (same variable, different type)
print(type(x))  # <class 'str'>
```

This is different from statically typed languages like Java:

```java
// Java -- you must declare the type
int x = 10;       // x can only hold integers
x = "hello";      // ERROR: incompatible types
```

#### 2.2 Variable Naming Rules

Python has specific rules for valid variable names:

1. Must start with a **letter** (a-z, A-Z) or an **underscore** (`_`).
2. The rest can contain letters, digits (0-9), or underscores.
3. **Cannot** start with a digit.
4. **Cannot** contain spaces or special characters (`@`, `#`, `$`, `%`, etc.).
5. **Cannot** be a **reserved keyword** (like `if`, `else`, `for`, `while`, `class`, `def`, etc.).

**Valid names:**
```python
name = "John"
_age = 25
student1 = "Alice"
my_variable = 100
camelCaseExample = "okay"
```

**Invalid names:**
```python
123abc = "error"    # starts with a digit
my var = "error"    # contains a space
if = 10             # 'if' is a keyword
$money = "error"    # contains special character
```

**Conventions (PEP 8):**
- Use **snake_case** for variable names: `first_name`, `total_count`.
- Use **UPPER_CASE** for constants: `PI = 3.14159`, `MAX_SIZE = 100`.
- Leading underscore `_var` means "internal use" (by convention).
- Double leading underscore `__var` triggers name mangling (for classes).

#### 2.3 Multiple Assignment

Python allows you to assign values to multiple variables in one line:

```python
# Assigning different values to different variables
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Assigning the same value to multiple variables
x = y = z = 0
print(x)  # 0
print(y)  # 0
print(z)  # 0

# Swapping values (very Pythonic!)
a, b = 5, 10
print(a, b)  # 5 10
a, b = b, a  # swap
print(a, b)  # 10 5
```

The swapping trick works because Python evaluates the right-hand side first (creating a tuple `(b, a)` = `(10, 5)`) and then unpacks it into `a, b`.

---

### 3. Basic Data Types

Python has several built-in data types. The most fundamental ones are:

#### 3.1 `int` -- Integer

Whole numbers, positive or negative, without a decimal point.

```python
a = 10
b = -5
c = 0
d = 12345678901234567890  # Python handles arbitrarily large integers

print(type(a))  # <class 'int'>

# Operations with integers
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 ** 3)  # 1000 (exponentiation)
print(10 // 3)  # 3 (integer/floor division)
print(10 % 3)   # 1 (modulus/remainder)
```

#### 3.2 `float` -- Floating-Point Number

Numbers with a decimal point. Also used for scientific notation.

```python
pi = 3.14159
temperature = -2.5
speed_of_light = 3.0e8  # 3.0 * 10^8 = 300,000,000.0

print(type(pi))  # <class 'float'>

# Operations with floats
print(3.5 + 2.1)  # 5.6
print(10.0 / 3.0) # 3.3333333333333335 (floating-point precision)
```

**Important:** Floating-point arithmetic is not always exact due to the way computers represent real numbers. This is normal and happens in all languages.

```python
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3)
```

#### 3.3 `str` -- String

A sequence of characters enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).

```python
name = "Alice"
city = 'New York'
multiline = """This is a
multi-line string."""
quote = '''She said, "Hello!"'''

print(type(name))  # <class 'str'>

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
print(greeting)  # Hello World

repeat = "Ha" * 3
print(repeat)  # HaHaHa

# Accessing characters (indexing -- starts at 0)
message = "Python"
print(message[0])  # P
print(message[2])  # t
print(message[-1]) # n (negative index counts from the end)

# Slicing: string[start:end:step]
print(message[0:3])   # Pyt (characters from index 0 to 2)
print(message[::2])   # Pto (every 2nd character)
print(message[::-1])  # nohtyP (reversed)
```

**String methods (some common ones):**

```python
text = "  Hello, World!  "

print(text.lower())       # "  hello, world!  "
print(text.upper())       # "  HELLO, WORLD!  "
print(text.strip())       # "Hello, World!" (removes leading/trailing spaces)
print(text.replace("World", "Python"))  # "  Hello, Python!  "
print(text.split(","))    # ['  Hello', ' World!  ']
print(len(text))          # 18 (length of the string includes spaces)
```

#### 3.4 `bool` -- Boolean

Represents one of two values: `True` or `False`. Used for logical operations and conditional statements.

```python
is_raining = True
is_sunny = False

print(type(is_raining))  # <class 'bool'>

# Boolean operations
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Comparison results are booleans
print(10 > 5)   # True
print(10 == 5)  # False
print(10 != 5)  # True
```

**Truthiness:** In Python, certain values behave like `False` in boolean contexts:
- `None`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict)

Everything else behaves like `True`.

```python
if "":
    print("This won't print")  # Empty string is falsy
if "hello":
    print("This will print")   # Non-empty string is truthy
```

#### 3.5 `NoneType` -- None

`None` is a special value that represents the **absence of a value** or a **null value**. It is the only value of type `NoneType`.

```python
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>

# Common use: as a placeholder
user_input = None  # We don't have input yet
```

`None` is falsy in boolean contexts:

```python
if None:
    print("This won't print")
else:
    print("None is falsy")  # This will print
```

---

### 4. The `type()` Function

The built-in `type()` function returns the type of any object. This is very useful for debugging and understanding your code.

```python
print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type(None))        # <class 'NoneType'>
print(type([1, 2, 3]))   # <class 'list'>
print(type((1, 2, 3)))   # <class 'tuple'>
print(type({1, 2, 3}))   # <class 'set'>
print(type({"a": 1}))    # <class 'dict'>
```

You can also use `isinstance()` to check if a value is of a specific type:

```python
print(isinstance(10, int))          # True
print(isinstance("Hi", str))        # True
print(isinstance("Hi", int))        # False
```

---

### 5. Complete Example with All Data Types

```python
# A program demonstrating Python's basic data types

# Integer
age = 22
print(f"Age: {age}, Type: {type(age)}")

# Float
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String
name = "Rahul"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_student = True
print(f"Student: {is_student}, Type: {type(is_student)}")

# NoneType
middle_name = None
print(f"Middle Name: {middle_name}, Type: {type(middle_name)}")
```

**Output:**

```
Age: 22, Type: <class 'int'>
Height: 5.9, Type: <class 'float'>
Name: Rahul, Type: <class 'str'>
Student: True, Type: <class 'bool'>
Middle Name: None, Type: <class 'NoneType'>
```

---

### 6. The `id()` Function

Every object in Python has a unique identity (memory address). The `id()` function returns this identity as an integer.

```python
x = 10
y = 10
z = 20

print(id(x))  # e.g., 140734982674944
print(id(y))  # Same as x (Python reuses small integers for efficiency)
print(id(z))  # Different from x
```

This is useful for understanding when variables refer to the same object vs. different objects.

---

## Practice Problems

1. **Variable Naming:** Which of the following are valid Python variable names? Fix the invalid ones.
   - `2nd_place`
   - `my_name`
   - `_count`
   - `class`
   - `total$`
   <details>
   <summary>Show Answer</summary>
   - `2nd_place` — Invalid (starts with digit). Fix: `second_place`
   - `my_name` — Valid
   - `_count` — Valid
   - `class` — Invalid (reserved keyword). Fix: `class_` or `my_class`
   - `total$` — Invalid (`$` is not allowed). Fix: `total`
   </details>

2. **Multiple Assignment:** Use multiple assignment to swap the values of `a = 15` and `b = 30` so that `a` becomes 30 and `b` becomes 15. Print the result.
   <details>
   <summary>Show Answer</summary>
   ```python
   a, b = 15, 30
   a, b = b, a
   print(a, b)  # Output: 30 15
   ```
   </details>

3. **Type Inspection:** For each of the following values, determine the type without running code, then verify with `type()`:
   - `42`
   - `3.0`
   - `"42"`
   - `"True"`
   - `True`
   - `None`
   <details>
   <summary>Show Answer</summary>
   - `42` → `int`
   - `3.0` → `float`
   - `"42"` → `str`
   - `"True"` → `str` (it's a string because of the quotes)
   - `True` → `bool`
   - `None` → `NoneType`
   </details>

4. **String Slicing:** Given `s = "Python Programming"`, write slicing expressions to get:
   - `"Python"`
   - `"Programming"`
   - `"Pto rgamn"` (every 2nd character)
   - The string reversed
   <details>
   <summary>Show Answer</summary>
   ```python
   s = "Python Programming"
   s[:6]        # "Python"
   s[7:]        # "Programming"
   s[::2]       # "Pto rgamn"
   s[::-1]      # "gnimmargorP nohtyP"
   ```
   </details>

5. **Truthiness:** Predict the output of this code without running it:
   ```python
   if 0:
       print("Zero is truthy")
   else:
       print("Zero is falsy")
   
   if "False":
       print("Non-empty string is truthy")
   else:
       print("Non-empty string is falsy")
   ```
   <details>
   <summary>Show Answer</summary>
   Output:
   ```
   Zero is falsy
   Non-empty string is truthy
   ```
   `0` is falsy in Python. `"False"` is a non-empty string, which is truthy.
   </details>
