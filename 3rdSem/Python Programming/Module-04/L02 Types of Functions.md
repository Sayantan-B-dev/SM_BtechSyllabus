# Types of Functions

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 2  
**Date:** 14-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## Classification of Functions in Python

Python functions can be classified into several categories based on how they are defined and used.

## 1. Built-in Functions vs User-Defined Functions

### Built-in Functions

These are functions that come pre-installed with Python. They are always available for use without importing any module.

Common built-in functions:

| Function     | Description                              | Example                     |
|-------------|------------------------------------------|-----------------------------|
| `print()`   | Outputs data to the console              | `print("Hello")`            |
| `len()`     | Returns length of a sequence             | `len([1, 2, 3])` -> 3       |
| `type()`    | Returns the data type of a value         | `type(42)` -> `<class 'int'>` |
| `int()`     | Converts value to integer                | `int("5")` -> 5             |
| `str()`     | Converts value to string                 | `str(100)` -> "100"         |
| `list()`    | Creates a list from an iterable          | `list("abc")` -> ['a','b','c'] |
| `max()`     | Returns the largest item                 | `max(3, 7, 1)` -> 7         |
| `min()`     | Returns the smallest item                | `min(3, 7, 1)` -> 1         |
| `sum()`     | Sums all items in an iterable            | `sum([1, 2, 3])` -> 6       |
| `input()`   | Reads input from the user                | `input("Enter name: ")`     |

```python
# Examples of built-in functions
numbers = [5, 2, 8, 1, 9]
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
```

**Output:**
```
Length: 5
Maximum: 9
Minimum: 1
Sum: 25
Sorted: [1, 2, 5, 8, 9]
```

### User-Defined Functions

These are functions created by the programmer to perform specific tasks. They are defined using the `def` keyword.

```python
def cube(x):
    return x ** 3

def is_positive(x):
    return x > 0

# Using user-defined functions
print(cube(3))
print(is_positive(-5))
```

**Output:**
```
27
False
```

## 2. Functions Based on Arguments and Return Values

### Function with No Arguments and No Return Value

```python
def welcome():
    print("Welcome to Python Programming!")

welcome()
```

**Output:**
```
Welcome to Python Programming!
```

### Function with Arguments but No Return Value

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

**Output:**
```
Hello, Alice!
```

### Function with No Arguments but a Return Value

```python
import random

def get_pi():
    return 3.14159

def random_dice():
    return random.randint(1, 6)

print(get_pi())
print(random_dice())
```

**Output:**
```
3.14159
4
```

### Function with Arguments and a Return Value

```python
def power(base, exponent):
    return base ** exponent

result = power(2, 5)
print(result)
```

**Output:**
```
32
```

## 3. Void Functions (Returning `None`)

A void function is one that does not return a meaningful value. In Python, such functions return `None` implicitly.

```python
def display_table(number):
    """Prints the multiplication table for a number."""
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    # No return statement -- returns None

result = display_table(5)
print("Return value:", result)
```

**Output:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Return value: None
```

The `return None` is implicit in void functions, but you can also write it explicitly:

```python
def log_message(msg):
    print(f"[LOG]: {msg}")
    return None  # explicit, but unnecessary
```

## 4. Lambda Functions (Brief Introduction)

Lambda functions are small, anonymous functions defined with the `lambda` keyword. They can have any number of arguments but only one expression.

```python
# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(square(5))  # 25

add = lambda a, b: a + b
print(add(10, 20))  # 30
```

Lambda functions are covered in detail in Lecture 4.

## 5. Recursive Functions

A recursive function is a function that calls itself. Every recursive function must have:

1. **Base case** -- A condition that stops the recursion.
2. **Recursive case** -- The function calls itself with a smaller or simpler input.

### Factorial Example

```python
def factorial(n):
    """Calculate n! using recursion."""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of 7:", factorial(7))
```

**Output:**
```
Factorial of 5: 120
Factorial of 0: 1
Factorial of 7: 5040
```

**How recursion works for `factorial(5)`:**

```
factorial(5) = 5 * factorial(4)
            = 5 * 4 * factorial(3)
            = 5 * 4 * 3 * factorial(2)
            = 5 * 4 * 3 * 2 * factorial(1)
            = 5 * 4 * 3 * 2 * 1
            = 120
```

### Fibonacci Sequence Example

```python
def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed)."""
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")
```

**Output:**
```
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
fib(8) = 21
fib(9) = 34
```

### Recursion vs Iteration

```python
# Recursive approach
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_recursive(6))  # 720
print(factorial_iterative(6))  # 720
```

**Note:** Recursion is elegant but can be less efficient due to function call overhead. Python has a recursion limit (default 1000). For very deep recursion, iterative solutions are safer.

## Summary Table

| Type                    | Has Arguments | Has Return | Example                    |
|-------------------------|:------------:|:----------:|----------------------------|
| No args, no return      | No           | No         | `def greet(): print("Hi")` |
| With args, no return    | Yes          | No         | `def show(x): print(x)`    |
| No args, with return    | No           | Yes        | `def pi(): return 3.14`    |
| With args, with return  | Yes          | Yes        | `def add(a,b): return a+b` |
| Void                    | Either       | Returns None| `def log(msg): print(msg)`|
| Recursive               | Yes          | Yes        | `def fact(n): ...`         |

---

## Practice Problems

**Problem 1:** Write a recursive function `sum_digits(n)` that returns the sum of digits of a positive integer.

<details>
<summary>Hint</summary>

Base case: if n == 0, return 0. Recursive case: return (n % 10) + sum_digits(n // 10).
</details>

<details>
<summary>Solution</summary>

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  # 1+2+3+4 = 10
print(sum_digits(9876))  # 9+8+7+6 = 30
```
</details>

**Problem 2:** Write a function `is_prime(n)` that returns `True` if n is prime, `False` otherwise. Use only built-in functions.

<details>
<summary>Hint</summary>

A number is prime if it is greater than 1 and divisible only by 1 and itself. Check divisibility from 2 to sqrt(n) using `n % i == 0`.
</details>

<details>
<summary>Solution</summary>

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
print(is_prime(25))  # False
```
</details>

**Problem 3:** Write a recursive function `reverse_string(s)` that returns the reverse of a string.

<details>
<summary>Hint</summary>

Base case: if string length is 0 or 1, return the string. Recursive case: return `reverse_string(s[1:]) + s[0]`.
</details>

<details>
<summary>Solution</summary>

```python
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```
</details>

**Problem 4:** Write a void function `print_triangle(n)` that prints a right-angled triangle pattern of stars with n rows. It should return `None` (implicitly).

<details>
<summary>Hint</summary>

Use nested loops: outer loop for rows, inner loop for stars in each row.
</details>

<details>
<summary>Solution</summary>

```python
def print_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

result = print_triangle(5)
print("Returned:", result)
```

**Output:**
```
*
**
***
****
*****
Returned: None
```
</details>
