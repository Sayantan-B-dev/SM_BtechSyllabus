# Defining and Calling Functions

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 1  
**Date:** 09-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## What is a Function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, you write it once inside a function and call that function whenever needed.

## Why Use Functions?

- **Reusability**: Write once, use many times.
- **Modularity**: Break complex programs into smaller, manageable pieces.
- **Readability**: Code becomes cleaner and easier to understand.
- **Debugging**: Easier to find and fix errors in isolated function blocks.
- **Maintainability**: Changes are made in one place.

## Defining a Function: The `def` Keyword

Python uses the `def` keyword to define a function. The general syntax is:

```python
def function_name(parameters):
    """docstring (optional)"""
    # function body
    # indented block of code
    return value  # optional
```

### Components Explained

1. **`def`** - Keyword that starts the function definition.
2. **`function_name`** - A valid identifier (follows variable naming rules).
3. **`parameters`** - Inputs the function accepts (optional, can be empty).
4. **Colon (`:`)** - Marks the end of the function header.
5. **Function body** - Indented block of code beneath the `def` line.
6. **`return`** - Statement that sends a result back to the caller (optional).

## Function Body and Indentation

The function body must be indented. Python uses indentation (typically 4 spaces) to define the block of code belonging to the function.

```python
def greet():
print("Hello!")  # This will cause an IndentationError
```

Correct version:

```python
def greet():
    print("Hello!")  # 4 spaces indentation
```

## The `return` Statement

The `return` statement exits a function and optionally sends a value back to the caller.

### Returning a Single Value

```python
def square(number):
    return number * number

result = square(5)
print(result)
```

**Output:**
```
25
```

### Returning Multiple Values

Python functions can return multiple values as a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([4, 7, 2, 9, 1])
print("Lowest:", lowest)
print("Highest:", highest)
```

**Output:**
```
Lowest: 1
Highest: 9
```

When you return multiple values separated by commas, Python packs them into a tuple. You can unpack them directly into variables.

### Function Without `return`

If a function does not have a `return` statement, it returns `None` by default:

```python
def show_message(msg):
    print("Message:", msg)

result = show_message("Hello")
print("Returned:", result)
```

**Output:**
```
Message: Hello
Returned: None
```

## Calling a Function

To call (execute) a function, write its name followed by parentheses with any required arguments:

```python
# Definition
def add(a, b):
    return a + b

# Call
sum_result = add(10, 20)
print(sum_result)
```

**Output:**
```
30
```

## Docstrings (`"""`)

A docstring is a string literal that appears right after the function header. It documents what the function does. Docstrings are written inside triple quotes.

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width
```

You can view a function's docstring using `help()` or `.__doc__`:

```python
help(calculate_area)
# or
print(calculate_area.__doc__)
```

**Output:**
```
Help on function calculate_area in module __main__:

calculate_area(length, width)
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
```

## Complete Example: Putting It All Together

```python
def is_even(number):
    """Check if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if even, False otherwise.
    """
    return number % 2 == 0

def factorial(n):
    """Calculate factorial of n (n!)."""
    if n < 0:
        return None  # factorial undefined for negative numbers
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Calling the functions
num = 6
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

print(f"Factorial of {num} is {factorial(num)}.")
```

**Output:**
```
6 is even.
Factorial of 6 is 720.
```

## Key Points to Remember

- Function names must be unique within a scope.
- A function must be defined before it is called.
- Indentation is part of Python's syntax -- use consistent spacing (4 spaces recommended).
- `return` immediately exits the function; any code after `return` inside the function is not executed.
- Functions without `return` implicitly return `None`.
- Docstrings are not mandatory but are considered a best practice.

---

## Practice Problems

**Problem 1:** Write a function `is_palindrome(s)` that checks whether a given string is a palindrome (reads the same forwards and backwards). Return `True` or `False`.

<details>
<summary>Show Answer</summary>

Compare the string with its reverse: `s == s[::-1]`.
</details>

<details>
<summary>Show Answer</summary>

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
```
</details>

**Problem 2:** Write a function `count_vowels(text)` that returns the number of vowels (a, e, i, o, u) in a given string.

<details>
<summary>Show Answer</summary>

Loop through each character and check if it is in `"aeiouAEIOU"`.
</details>

<details>
<summary>Show Answer</summary>

```python
def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))  # 3
```
</details>

**Problem 3:** Write a function `stats(numbers)` that takes a list of numbers and returns the sum, average, minimum, and maximum as four separate values.

<details>
<summary>Show Answer</summary>

Use `sum()`, `len()`, `min()`, `max()` built-in functions.
</details>

<details>
<summary>Show Answer</summary>

```python
def stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, avg, minimum, maximum

s, a, mi, ma = stats([10, 20, 30, 40, 50])
print(f"Sum: {s}, Avg: {a}, Min: {mi}, Max: {ma}")
```
</details>

**Problem 4:** Write a function `temperature_converter(value, to_celsius=True)` that converts between Celsius and Fahrenheit. If `to_celsius` is `True`, convert Fahrenheit to Celsius; otherwise, convert Celsius to Fahrenheit.

<details>
<summary>Show Answer</summary>

C = (F - 32) * 5/9, F = C * 9/5 + 32
</details>

<details>
<summary>Show Answer</summary>

```python
def temperature_converter(value, to_celsius=True):
    if to_celsius:
        return (value - 32) * 5 / 9
    else:
        return value * 9 / 5 + 32

print(temperature_converter(98.6, True))    # 37.0
print(temperature_converter(37, False))     # 98.6
```
</details>
