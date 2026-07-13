# Importing Modules, Math and Random Modules

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 5  
**Date:** 28-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## What is a Module?

A module is a file containing Python definitions and statements. Modules help organize code into reusable files. The file name is the module name with the `.py` extension.

## The `import` Statement

The `import` statement loads a module and makes its contents available.

```python
import math

# Use functions from the math module with module_name.function_name
print(math.sqrt(16))
print(math.pi)
```

**Output:**
```
4.0
3.141592653589793
```

### Importing Multiple Modules

```python
import math
import random

print(math.floor(3.7))
print(random.randint(1, 10))
```

## The `from...import` Statement

This imports specific items from a module directly into the current namespace, so you can use them without the module prefix.

```python
from math import sqrt, pi

# Use directly without 'math.'
print(sqrt(25))
print(pi)
```

**Output:**
```
5.0
3.141592653589793
```

### Importing All Names with `*`

```python
from math import *

print(sin(0))
print(cos(0))
print(e)
```

**Output:**
```
0.0
1.0
2.718281828459045
```

**Warning:** Using `*` can cause name conflicts if imported names override existing ones. It is better to import only what you need.

## The `import...as` Statement (Alias)

This imports a module or item with a shorter alias.

```python
import math as m
import random as r

print(m.sqrt(144))
print(r.randint(1, 6))
```

**Output:**
```
12.0
3
```

```python
from math import pi as PI_VALUE, sqrt as square_root

print(PI_VALUE)
print(square_root(100))
```

**Output:**
```
3.141592653589793
10.0
```

## Creating Your Own Module

Any `.py` file can be a module. Save the file and import it.

**File: `my_utils.py`**

```python
"""My custom utility functions."""

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_palindrome(s):
    return s == s[::-1]

PI = 3.14159
```

**Using the module:**

```python
import my_utils

print(my_utils.add(10, 5))
print(my_utils.multiply(3, 4))
print(my_utils.is_palindrome("radar"))
print(my_utils.PI)
```

**Output:**
```
15
12
True
3.14159
```

## The `if __name__ == "__main__"` Idiom

When a Python file is run directly, its `__name__` variable is set to `"__main__"`. When it is imported as a module, `__name__` is set to the module's name.

This idiom allows a file to be both used as a module and run as a standalone script.

**File: `calculator.py`**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    # This code runs only when the file is executed directly
    print("Calculator running as standalone script...")
    print("3 + 4 =", add(3, 4))
    print("10 - 7 =", subtract(10, 7))
```

**Running directly:**

```
> python calculator.py
Calculator running as standalone script...
3 + 4 = 7
10 - 7 = 3
```

**Importing as a module:**

```python
import calculator

print(calculator.add(5, 6))
print(calculator.multiply(2, 8))
```

**Output (only import behavior, no test code runs):**
```
11
16
```

The test code inside `if __name__ == "__main__":` does not execute because the file is imported, not run directly.

## The `math` Module

The `math` module provides mathematical functions and constants.

### Common Math Constants

```python
import math

print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
print(math.tau)  # 6.283185307179586
print(math.inf)  # inf
print(math.nan)  # nan
```

### Common Math Functions

| Function          | Description                            | Example                     |
|-------------------|----------------------------------------|-----------------------------|
| `sqrt(x)`         | Square root of x                       | `sqrt(16)` -> 4.0           |
| `ceil(x)`         | Smallest integer >= x                  | `ceil(3.2)` -> 4            |
| `floor(x)`        | Largest integer <= x                   | `floor(3.8)` -> 3           |
| `pow(x, y)`       | x raised to power y                    | `pow(2, 3)` -> 8.0          |
| `fabs(x)`         | Absolute value (float)                 | `fabs(-5)` -> 5.0           |
| `factorial(x)`    | Factorial of x                         | `factorial(5)` -> 120       |
| `gcd(a, b)`       | Greatest common divisor                | `gcd(12, 18)` -> 6          |
| `sin(x)`          | Sine of x (radians)                    | `sin(0)` -> 0.0             |
| `cos(x)`          | Cosine of x (radians)                  | `cos(0)` -> 1.0             |
| `tan(x)`          | Tangent of x (radians)                 | `tan(pi/4)` -> 1.0          |
| `log(x)`          | Natural logarithm of x                 | `log(2.718)` -> 1.0         |
| `log10(x)`        | Base-10 logarithm of x                 | `log10(100)` -> 2.0         |
| `log2(x)`         | Base-2 logarithm of x                  | `log2(8)` -> 3.0            |
| `degrees(x)`      | Convert radians to degrees             | `degrees(pi)` -> 180.0      |
| `radians(x)`      | Convert degrees to radians             | `radians(180)` -> pi        |

### Code Examples

```python
import math

# Square root
print(math.sqrt(25))      # 5.0
print(math.sqrt(2))       # 1.4142135623730951

# Ceil and Floor
print(math.ceil(4.1))     # 5
print(math.floor(4.9))    # 4
print(math.ceil(-3.2))    # -3
print(math.floor(-3.2))   # -4

# Power
print(math.pow(2, 10))    # 1024.0
print(math.pow(5, 3))     # 125.0

# Trigonometric
angle = math.radians(45)  # Convert 45 degrees to radians
print(math.sin(angle))    # 0.7071067811865475
print(math.cos(angle))    # 0.7071067811865476
print(math.tan(angle))    # 0.9999999999999999

# Logarithms
print(math.log(100))      # 4.605170185988092 (natural log)
print(math.log10(100))    # 2.0
print(math.log2(16))      # 4.0

# GCD
print(math.gcd(24, 36))   # 12
```

## The `random` Module

The `random` module is used for generating pseudo-random numbers.

### Common Random Functions

| Function             | Description                                      | Example                          |
|----------------------|--------------------------------------------------|----------------------------------|
| `random()`           | Random float in [0.0, 1.0)                       | `random()` -> 0.4567             |
| `randint(a, b)`      | Random integer in [a, b] (inclusive)             | `randint(1, 6)` -> 4             |
| `randrange(start, stop[, step])` | Random element from range        | `randrange(0, 10, 2)` -> 6       |
| `choice(seq)`        | Random element from a non-empty sequence         | `choice(['a','b','c'])` -> 'b'   |
| `choices(pop, k)`    | Pick k items with replacement                    | `choices([1,2,3], k=2)` -> [1,3] |
| `sample(pop, k)`     | Pick k unique items without replacement          | `sample([1..10], 3)` -> [7,2,9]  |
| `shuffle(lst)`       | Shuffle a list in place                          | `shuffle(cards)`                 |
| `uniform(a, b)`      | Random float in [a, b]                           | `uniform(0, 10)` -> 5.67         |
| `seed(n)`            | Initialize the random generator                  | `seed(42)`                       |

### Code Examples

```python
import random

# Seed for reproducible results
random.seed(42)
print(random.random())  # 0.6394267984578838 (deterministic with seed)

# Random float between 0 and 1
print(random.random())  # 0.025010755222666936

# Random integer
dice = random.randint(1, 6)
print("Dice roll:", dice)

# Random float in a range
temp = random.uniform(95.0, 104.0)
print("Temperature:", round(temp, 1))

# Random choice from a list
colors = ["red", "blue", "green", "yellow", "purple"]
print("Random color:", random.choice(colors))

# Multiple random choices (with replacement - could repeat)
print("3 choices (with replacement):", random.choices(colors, k=3))

# Random sample (without replacement - no repeats)
print("3 unique colors:", random.sample(colors, 3))
```

**Sample Output:**
```
0.6394267984578838
0.025010755222666936
Dice roll: 3
Temperature: 98.6
Random color: green
3 choices (with replacement): ['blue', 'yellow', 'blue']
3 unique colors: ['green', 'purple', 'red']
```

### Shuffling a List

```python
import random

cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7"]
print("Original:", cards)

random.shuffle(cards)
print("Shuffled:", cards)

random.shuffle(cards)
print("Shuffled again:", cards)
```

**Sample Output:**
```
Original: ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7']
Shuffled: ['Jack', '10', '7', 'Queen', 'Ace', '9', 'King', '8']
Shuffled again: ['Queen', '8', '9', '10', 'Ace', '7', 'Jack', 'King']
```

### Practical Examples

```python
import random
import math

# Simulate rolling two dice
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

print("Sum of two dice:", roll_dice())

# Generate a random password (alphanumeric)
import string
def random_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

print("Random password:", random_password())
print("Random 12-char password:", random_password(12))

# Estimate pi using Monte Carlo method
def estimate_pi(num_points=100000):
    inside = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) <= 1:
            inside += 1
    return 4 * inside / num_points

print("Estimated pi:", estimate_pi(100000))
```

**Sample Output:**
```
Sum of two dice: 7
Random password: aG7kPq2X
Random 12-char password: X9mKp4LqRtZw
Estimated pi: 3.14148
```

## Module Search Path

When you import a module, Python searches in the following order:

1. Current directory (where the script is running).
2. `PYTHONPATH` environment variable directories.
3. Standard library directories.
4. Site-packages (third-party packages).

You can see the search path:

```python
import sys
print(sys.path)
```

## Built-in Module `sys`

The `sys` module provides system-specific parameters and functions.

```python
import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Command line arguments:", sys.argv)
print("Exit the program:")
sys.exit(0)  # terminates the script
```

---

## Practice Problems

**Problem 1:** Write a program that generates a random multiplication table question (e.g., "What is 7 x 8?"), takes the user's answer, and tells them if they are correct. Use `random.randint()`.

<details>
<summary>Hint</summary>

Generate two random numbers between 1 and 12. Compare the user's input to the product.
</details>

<details>
<summary>Solution</summary>

```python
import random

a = random.randint(1, 12)
b = random.randint(1, 12)
correct = a * b

answer = int(input(f"What is {a} x {b}? "))
if answer == correct:
    print("Correct!")
else:
    print(f"Wrong. The answer is {correct}")
```
</details>

**Problem 2:** Write a function `circle_properties(radius)` that uses the `math` module to return the circumference and area of a circle. Round both to 2 decimal places.

<details>
<summary>Hint</summary>

Circumference = 2 * pi * radius. Area = pi * radius^2.
</details>

<details>
<summary>Solution</summary>

```python
import math

def circle_properties(radius):
    circumference = round(2 * math.pi * radius, 2)
    area = round(math.pi * radius ** 2, 2)
    return circumference, area

c, a = circle_properties(5)
print(f"Circumference: {c}, Area: {a}")
# Circumference: 31.42, Area: 78.54
```
</details>

**Problem 3:** Write a script that generates a list of 10 random integers between 1 and 100, then uses `math` functions to print the maximum, minimum, average (floor), and standard deviation of the list.

<details>
<summary>Hint</summary>

Use `random.randint(1, 100)` for each number. For standard deviation, use: sqrt(sum((x - mean)^2) / n).
</details>

<details>
<summary>Solution</summary>

```python
import random
import math

numbers = [random.randint(1, 100) for _ in range(10)]
print("Numbers:", numbers)

mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std_dev = math.sqrt(variance)

print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Average (floor): {math.floor(mean)}")
print(f"Std Dev: {round(std_dev, 2)}")
```
</details>

**Problem 4:** Create a custom module `temperature.py` that has functions `c_to_f(c)` and `f_to_c(f)`. Then, in a separate script file, import and use this module to convert 100 degrees Celsius to Fahrenheit and 212 degrees Fahrenheit to Celsius.

<details>
<summary>Hint</summary>

Save `temperature.py` in the same directory as your script.
</details>

<details>
<summary>Solution</summary>

**File: `temperature.py`**

```python
def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    # Test code
    print("100 C =", c_to_f(100), "F")
    print("212 F =", f_to_c(212), "C")
```

**File: `main.py`** (separate script)

```python
import temperature

c = 100
f = temperature.c_to_f(c)
print(f"{c}C = {f}F")

f = 212
c = temperature.f_to_c(f)
print(f"{f}F = {c}C")
```

**Output of `main.py`:**
```
100C = 212.0F
212F = 100.0C
```
</details>
