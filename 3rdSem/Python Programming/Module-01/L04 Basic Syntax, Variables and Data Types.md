# Basic Syntax, Variables and Data Types

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 4  
**Date:** 15-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

### 1. Type Conversion (Type Casting)

Type conversion is the process of converting a value from one data type to another. Python provides built-in functions for explicit type conversion.

#### 1.1 Implicit Type Conversion

Python sometimes converts types automatically (implicit conversion). This happens when you mix data types in an operation where one type can be safely promoted.

```python
# Integer + Float -> Float (int is promoted to float)
result = 10 + 3.5
print(result)       # 13.5
print(type(result)) # <class 'float'>

# Integer / Integer -> Float (division always returns float)
result = 10 / 3
print(result)       # 3.3333333333333335
```

#### 1.2 Explicit Type Conversion

You use built-in functions to explicitly convert between types.

**`int()` -- Convert to Integer**

Converts a float (truncates decimal part), a string (must be a valid integer literal), or a boolean to an integer.

```python
# Float to int (truncation, not rounding)
print(int(3.14))    # 3
print(int(3.99))    # 3 (truncated, not rounded!)

# String to int (must be a valid integer)
print(int("42"))    # 42
print(int("  100  "))  # 100 (leading/trailing spaces are okay)

# Bool to int
print(int(True))    # 1
print(int(False))   # 0

# Invalid conversion -- will raise ValueError
# int("3.14")    # ValueError: invalid literal for int() with base 10: '3.14'
# int("hello")   # ValueError
```

**`float()` -- Convert to Float**

```python
# Int to float
print(float(10))        # 10.0

# String to float
print(float("3.14"))    # 3.14
print(float("100"))     # 100.0

# Bool to float
print(float(True))      # 1.0
print(float(False))     # 0.0
```

**`str()` -- Convert to String**

```python
# Any type to string
print(str(42))          # "42"
print(str(3.14))        # "3.14"
print(str(True))        # "True"
print(str(None))        # "None"

# Useful for concatenation
age = 22
# print("I am " + age + " years old.")  # TypeError: can only concatenate str (not "int") to str
print("I am " + str(age) + " years old.")  # "I am 22 years old."
```

**`bool()` -- Convert to Boolean**

```python
# Falsy values (convert to False)
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False
print(bool(None))       # False
print(bool([]))         # False (empty list)
print(bool({}))         # False (empty dict)

# Truthy values (convert to True) -- everything else
print(bool(1))          # True
print(bool(-1))         # True
print(bool(3.14))       # True
print(bool("hello"))    # True
print(bool(" "))        # True (space is a character!)
```

**Common Conversion Errors:**

```python
# Invalid literal for int()
# int("12.5")  # ValueError: invalid literal for int() with base 10: '12.5'

# First convert to float, then to int
print(int(float("12.5")))  # 12

# Converting a non-numeric string
# int("abc")  # ValueError
```

---

### 2. Taking Input from the User: `input()`

The `input()` function reads a line of text from the user. It **always returns a string**, even if the user types a number.

#### 2.1 Basic Input

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**Run:**

```
Enter your name: Alice
Hello, Alice!
```

#### 2.2 Input Returns a String (Important!)

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'> -- ALWAYS a string

# If you need a number, convert it:
age = int(input("Enter your age: "))
print(type(age))  # <class 'int'>
```

#### 2.3 Complete Example: Simple Calculator

```python
# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2  # Note: can cause ZeroDivisionError

# Display results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Quotient:", quot_result)
```

**Run:**

```
Enter the first number: 10
Enter the second number: 3
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.3333333333333335
```

#### 2.4 Getting Multiple Inputs in One Line

You can use `split()` to read multiple values from a single input line:

```python
# Input: "Alice 22 85.5"
name, age, score = input("Enter name, age, score: ").split()
age = int(age)
score = float(score)

print(f"Name: {name}, Age: {age}, Score: {score}")
```

**Run:**

```
Enter name, age, score: Alice 22 85.5
Name: Alice, Age: 22, Score: 85.5
```

---

### 3. String Formatting

String formatting lets you embed values inside a string in a controlled way. Python offers three main approaches.

#### 3.1 f-Strings (Python 3.6+) -- Recommended

f-strings (formatted string literals) are the modern and most readable way to format strings. Prefix the string with `f` or `F` and use `{expression}` inside.

```python
name = "Rahul"
age = 22
score = 85.5

# Basic f-string
print(f"Name: {name}, Age: {age}, Score: {score}")
# Output: Name: Rahul, Age: 22, Score: 85.5

# Expressions inside {}
print(f"Next year you will be {age + 1} years old.")
# Output: Next year you will be 23 years old.

# Formatting numbers (width and precision)
print(f"Score: {score:.2f}")  # 2 decimal places
# Output: Score: 85.50

pi = 3.1415926535
print(f"Pi to 3 decimals: {pi:.3f}")
# Output: Pi to 3 decimals: 3.142

# Width and alignment
print(f"|{name:10}|")   # right-aligned in width 10
# Output: |Rahul     |
print(f"|{name:<10}|")  # left-aligned
# Output: |Rahul     |
print(f"|{name:^10}|")  # centered
# Output: |  Rahul   |
```

**Practical example:**

```python
item = "Apple"
quantity = 5
price = 0.75

print(f"{'Item':<10}{'Qty':<5}{'Price':>8}")
print(f"{item:<10}{quantity:<5}${price:>6.2f}")
```

**Output:**

```
Item      Qty       Price
Apple     5        $0.75
```

#### 3.2 `.format()` Method (Python 2.7+, 3.0+)

The `str.format()` method uses curly braces `{}` as placeholders.

```python
name = "Rahul"
age = 22

# Positional arguments
print("Name: {}, Age: {}".format(name, age))
# Output: Name: Rahul, Age: 22

# Indexed placeholders (reusable)
print("Name: {0}, Age: {1}, Again name: {0}".format(name, age))
# Output: Name: Rahul, Age: 22, Again name: Rahul

# Named placeholders
print("Name: {n}, Age: {a}".format(n=name, a=age))
# Output: Name: Rahul, Age: 22

# Format specifiers
print("Score: {:.2f}".format(85.5))
# Output: Score: 85.50

# Width and alignment
print("|{:<10}|{:>10}|".format("left", "right"))
# Output: |left      |     right|
```

#### 3.3 %-Formatting (Old Style, Legacy)

Inspired by C's `printf`. Still works but not recommended for new code.

```python
name = "Rahul"
age = 22
score = 85.5

# %s for strings, %d for integers, %f for floats
print("Name: %s, Age: %d, Score: %.2f" % (name, age, score))
# Output: Name: Rahul, Age: 22, Score: 85.50

# Named placeholders using a dictionary
print("Name: %(name)s, Age: %(age)d" % {"name": "Rahul", "age": 22})
```

**Summary -- Which one to use?**

| Method | When to Use |
|---|---|
| f-strings | Always preferred (Python 3.6+). Most readable. |
| `.format()` | When you need to store a template separately from values. |
| `%-formatting` | Only when maintaining legacy code. |

---

### 4. Working Examples with Input/Output

#### Example 1: Temperature Converter (Celsius to Fahrenheit)

```python
# Program: Celsius to Fahrenheit Converter

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.1f}C = {fahrenheit:.1f}F")
```

**Run:**

```
Enter temperature in Celsius: 25
25.0C = 77.0F
```

#### Example 2: Simple Interest Calculator

```python
# Program: Simple Interest Calculator

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (per year): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("\n--- Results ---")
print(f"Principal: Rs.{principal:.2f}")
print(f"Rate: {rate:.2f}% per year")
print(f"Time: {time} years")
print(f"Simple Interest: Rs.{simple_interest:.2f}")
print(f"Total Amount: Rs.{total_amount:.2f}")
```

**Run:**

```
Enter principal amount: 10000
Enter rate of interest (per year): 5.5
Enter time (in years): 3

--- Results ---
Principal: Rs.10000.00
Rate: 5.50% per year
Time: 3.0 years
Simple Interest: Rs.1650.00
Total Amount: Rs.11650.00
```

#### Example 3: Area of a Circle

```python
# Program: Area of a Circle

import math  # import the math module for pi

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Radius: {radius}")
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")
```

**Run:**

```
Enter the radius of the circle: 7
Radius: 7.0
Area: 153.94 square units
Circumference: 43.98 units
```

---

### 5. Common Mistakes and Best Practices

| Mistake | Wrong | Correct |
|---|---|---|
| Forgetting to convert input | `age = input("Age: ")` then `age + 1` | `age = int(input("Age: "))` |
| Mixing types in concatenation | `"Age: " + 22` | `"Age: " + str(22)` or f-string |
| Using `input()` with conversion in the same line | `age = int(input("Age: "))` if user might type a float | Use `float()` and then convert later if needed |
| Rounding with `int()` | `int(3.9)` gives `3`, not `4` | Use `round(3.9)` for proper rounding |

---

## Practice Problems

1. **Addition Quiz:** Write a program that asks the user for two numbers, adds them, and prints the result using an f-string. Example: `"The sum of 10 and 20 is 30"`.

2. **Type Converter:** Write a program that asks the user for an integer, a float, and a string. Then print the type of each using `type()` both before and after conversion.

3. **Rectangle Calculator:** Ask the user for the length and width of a rectangle. Calculate and display the area and perimeter. Format the output to 2 decimal places.

4. **Student Grade Input:** Ask the user for their name, subject, and score (out of 100). Display a formatted report like:
   ```
   Student: Alice
   Subject: Math
   Score: 87.50 / 100
   Percentage: 87.50%
   ```

5. **Currency Converter:** Ask the user for an amount in USD. Convert it to INR using a conversion rate (assume 1 USD = 83.50 INR). Display the result formatted with 2 decimal places and the currency symbol.
