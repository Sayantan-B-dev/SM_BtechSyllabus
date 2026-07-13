# String Indexing, Operations, and Built-in Functions

**Course:** Python Programming Lab  
**Module:** 2 | **Lecture:** 3  
**Date:** 14-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Use f-strings and the format() method with format specifiers.
- Create formatted tables with aligned columns.
- Format numbers with decimal places, padding, and alignment.

## Theory

String formatting allows embedding variable values into strings with precise control over appearance. Python offers three approaches: %-formatting (old style), str.format() method, and f-strings (Python 3.6+). f-strings are the most modern and preferred: prefix the string with 'f' or 'F' and embed expressions in curly braces {}.

Format specifiers within curly braces control alignment and width. The syntax is `{value:format_spec}`. Format specifiers include: `<` for left align, `>` for right align, `^` for center. A number after the alignment character specifies minimum width. For numbers, `.Nf` controls decimal places (e.g., `.2f` for 2 decimal places). Integers use `d`, floats use `f`, and strings use `s`.

The format() method uses the same specifiers but is invoked on the string: `"{}".format(value)`. Positional and keyword arguments can be used. For table formatting, combining alignment specifiers with fixed widths creates professional-looking columnar output.

## Procedure

1. Create a new Python file named lab11.py.
2. Demonstrate basic f-string usage with variables and expressions.
3. Format numbers: integers with leading zeros, floats with decimal places, percentages.
4. Create a table of student marks with aligned columns using format specifiers.
5. Demonstrate the format() method with positional and keyword arguments.
6. Test all formatting.

## Source Code

```python
# Module 02 Lab 03: String Formatting, f-strings, Format Specifiers

# Basic f-strings
name = "Alice"
age = 20
score = 87.5
print(f"Student: {name}, Age: {age}, Score: {score}")

# Expressions inside f-strings
a, b = 15, 7
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")

# Number formatting
pi = 3.14159265359
print(f"\nPi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")

value = 1234.5678
print(f"\nValue: {value}")
print(f"Width 10, right aligned: |{value:>10.2f}|")
print(f"Width 10, left aligned:  |{value:<10.2f}|")
print(f"Width 10, center:        |{value:^10.2f}|")

# Integer formatting with leading zeros
num = 42
print(f"\nLeading zeros: {num:05d}")
print(f"Width 8 right:  {num:8d}")
print(f"Width 8 left:   {num:<8d}")

# Percentage formatting
rate = 0.875
print(f"\nRate as percentage: {rate:.1%}")

# Table formatting
print("\n--- Student Marks Table ---")
print(f"{'Name':<10} {'Math':>6} {'Sci':>6} {'Eng':>6} {'Total':>6}")
print("-" * 34)
students = [
    ("Alice", 85, 90, 78),
    ("Bob", 72, 88, 91),
    ("Charlie", 95, 93, 89),
    ("Diana", 68, 75, 82)
]
for sname, math, sci, eng in students:
    total = math + sci + eng
    print(f"{sname:<10} {math:>6} {sci:>6} {eng:>6} {total:>6}")

# format() method with positional and keyword args
print("\nUsing format() method:")
print("Name: {}, Age: {}".format("Alice", 20))
print("Name: {0}, Age: {1}, Score: {1}".format("Alice", 20))
print("Name: {n}, Age: {a}".format(n="Bob", a=22))
```

## Sample Output

```
Student: Alice, Age: 20, Score: 87.5
15 + 7 = 22
15 * 7 = 105

Pi to 2 decimals: 3.14
Pi to 4 decimals: 3.1416

Value: 1234.5678
Width 10, right aligned: |   1234.57|
Width 10, left aligned:  |1234.57   |
Width 10, center:        | 1234.57  |

Leading zeros: 00042
Width 8 right:        42
Width 8 left:  42

Rate as percentage: 87.5%

--- Student Marks Table ---
Name        Math   Sci   Eng  Total
----------------------------------
Alice        85    90    78    253
Bob          72    88    91    251
Charlie      95    93    89    277
Diana        68    75    82    225

Using format() method:
Name: Alice, Age: 20
Name: Alice, Age: 20, Score: 20
Name: Bob, Age: 22
```

## Homework

1. Write a program that prints a multiplication table (1 to 10) in aligned columns using f-strings.
2. Write a program that takes a temperature in Celsius and prints it in Fahrenheit formatted to 2 decimal places with a width of 8 and right-aligned.
3. Create a product price catalog with columns for Product Name (left aligned, width 15), Quantity (right aligned, width 5), and Price (right aligned, width 8, 2 decimals). Add at least 4 products.
