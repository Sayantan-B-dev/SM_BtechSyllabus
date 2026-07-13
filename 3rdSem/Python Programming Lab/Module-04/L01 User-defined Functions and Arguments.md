# User-defined Functions and Arguments

**Course:** Python Programming Lab  
**Module:** 4 | **Lecture:** 1  
**Date:** 11-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Define user-defined functions using the def keyword.
- Use the return statement to send values back to the caller.
- Write documentation strings (docstrings) for functions.
- Implement factorial, prime check, and temperature converter functions.

## Theory

A function is a reusable block of code that performs a specific task. Functions help avoid code duplication and improve program organization. A function is defined using the def keyword, followed by the function name, parentheses for parameters, and a colon. The function body is indented. The return statement exits the function and optionally sends a value back.

```python
def function_name(parameters):
    """docstring explaining the function"""
    # function body
    return value
```

A docstring (triple-quoted string right after the def line) documents the function's purpose, parameters, and return value. It is accessible via help(function_name) or function_name.__doc__. Good docstrings are essential for code readability and maintainability.

Functions can call other functions. They can also be composed: the result of one function becomes the argument to another. Common practice is to write small, focused functions that do one thing well. The factorial function (n!) multiplies numbers 1..n. A prime check function tests divisibility up to sqrt(n). A temperature converter applies a conversion formula.

## Procedure

1. Create a new Python file named lab19.py.
2. Define a function factorial(n) that computes n! using a loop and returns the result. Include a docstring.
3. Define a function is_prime(n) that returns True if n is prime, False otherwise.
4. Define functions celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f).
5. Write a main section that calls these functions with user input and prints results.
6. Test each function with at least three different inputs.

## Source Code

```python
# Module 04 Lab 01: User-defined Functions, Return Values, Docstrings

def factorial(n):
    """Compute the factorial of a non-negative integer n.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The factorial of n (n!).
    """
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    """Check if a positive integer n is prime.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit.
    
    Args:
        c (float): Temperature in Celsius.
    
    Returns:
        float: Temperature in Fahrenheit.
    """
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius.
    
    Args:
        f (float): Temperature in Fahrenheit.
    
    Returns:
        float: Temperature in Celsius.
    """
    return (f - 32) * 5/9

# Main section - test all functions
print("--- Factorial ---")
num = int(input("Enter a number: "))
f = factorial(num)
if f is not None:
    print(f"{num}! = {f}")
else:
    print("Factorial not defined for negative numbers.")

print("\n--- Prime Check ---")
num2 = int(input("Enter a number: "))
if is_prime(num2):
    print(f"{num2} is prime.")
else:
    print(f"{num2} is not prime.")

print("\n--- Temperature Converter ---")
c = float(input("Enter Celsius: "))
print(f"{c}C = {celsius_to_fahrenheit(c):.2f}F")

f = float(input("Enter Fahrenheit: "))
print(f"{f}F = {fahrenheit_to_celsius(f):.2f}C")
```

## Sample Output

```
--- Factorial ---
Enter a number: 6
6! = 720

--- Prime Check ---
Enter a number: 29
29 is prime.

--- Temperature Converter ---
Enter Celsius: 100
100C = 212.00F
Enter Fahrenheit: 32
32F = 0.00C
```

## Homework

1. Write a function sum_of_digits(n) that returns the sum of the digits of a positive integer.
2. Write a function reverse_string(s) that returns the reverse of a given string using slicing.
3. Write a function is_palindrome(s) that checks if a string is a palindrome, ignoring case and spaces.
