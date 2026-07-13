# User-defined Functions and Arguments

**Course:** Python Programming Lab  
**Module:** 4 | **Lecture:** 3  
**Date:** 18-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Use *args to accept a variable number of positional arguments.
- Use **kwargs to accept a variable number of keyword arguments.
- Write a variable-sum function and a flexible student details function.

## Theory

The *args parameter collects extra positional arguments into a tuple. The name "args" is conventional but not required; the asterisk (*) is the special syntax. Inside the function, args is a tuple that can be iterated or indexed. This is useful when you don't know how many arguments will be passed.

The **kwargs parameter collects extra keyword arguments into a dictionary. The name "kwargs" is conventional, and the double asterisk (**) is the special syntax. Inside the function, kwargs is a dictionary mapping parameter names to values. This is useful for functions that need to handle many optional parameters.

Functions can use both *args and **kwargs simultaneously. The order must be: normal parameters, *args, then **kwargs. These features are widely used in decorators, wrapper functions, and APIs where flexibility is needed. The terms "args" and "kwargs" come from "arguments" and "keyword arguments."

## Procedure

1. Create a new Python file named lab21.py.
2. Write a function sum_all(*args) that returns the sum of all numeric arguments passed.
3. Write a function concatenate(*args, sep=" ") that joins all string arguments with a separator.
4. Write a function student_details(name, **kwargs) that prints a student's name and all other details.
5. Write a function flexible_display(*args, **kwargs) that prints positional args and keyword args.
6. Test all functions with different numbers of arguments.

## Source Code

```python
# Module 04 Lab 03: *args and **kwargs

# Variable number of positional arguments with *args
def sum_all(*args):
    """Return the sum of all provided numeric arguments."""
    total = 0
    for num in args:
        total += num
    return total

print("--- Sum All ---")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50) = {sum_all(10, 20, 30, 40, 50)}")
print(f"sum_all(5) = {sum_all(5)}")
print(f"sum_all() = {sum_all()}")

# *args with strings
def concatenate(*args, sep=" "):
    """Concatenate all string arguments with a separator."""
    return sep.join(args)

print("\n--- Concatenate ---")
print(f"concatenate('Hello', 'World') = '{concatenate('Hello', 'World')}'")
print(f"concatenate('a', 'b', 'c', sep='-') = '{concatenate('a', 'b', 'c', sep='-')}'")
print(f"concatenate('Python', 'is', 'fun', sep=' | ') = '{concatenate('Python', 'is', 'fun', sep=' | ')}'")

# **kwargs for flexible keyword arguments
def student_details(name, **kwargs):
    """Print student name and any additional details."""
    print(f"\n--- Student: {name} ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n--- Student Details ---")
student_details("Alice", age=20, course="CS", grade="A")
student_details("Bob", age=22, major="Physics", minor="Math", year=3)
student_details("Charlie")  # no additional kwargs

# Function with both *args and **kwargs
def flexible_display(*args, **kwargs):
    """Display positional args and keyword args."""
    print("\n--- Flexible Display ---")
    print("Positional arguments (args):")
    for i, arg in enumerate(args):
        print(f"  [{i}]: {arg}")

    print("Keyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

flexible_display(1, 2, 3, name="Alice", age=20, city="NYC")
flexible_display("hello", count=5)
```

## Sample Output

```
--- Sum All ---
sum_all(1, 2, 3) = 6
sum_all(10, 20, 30, 40, 50) = 150
sum_all(5) = 5
sum_all() = 0

--- Concatenate ---
concatenate('Hello', 'World') = 'Hello World'
concatenate('a', 'b', 'c', sep='-') = 'a-b-c'
concatenate('Python', 'is', 'fun', sep=' | ') = 'Python | is | fun'

--- Student Details ---

--- Student: Alice ---
age: 20
course: CS
grade: A

--- Student: Bob ---
age: 22
major: Physics
minor: Math
year: 3

--- Student: Charlie ---

--- Flexible Display ---
Positional arguments (args):
  [0]: 1
  [1]: 2
  [2]: 3
Keyword arguments (kwargs):
  name: Alice
  age: 20
  city: NYC

--- Flexible Display ---
Positional arguments (args):
  [0]: hello
Keyword arguments (kwargs):
  count: 5
```

## Homework

1. Write a function multiply_all(*args) that returns the product of all arguments. Return 1 if no arguments are given.
2. Write a function build_profile(first_name, last_name, **kwargs) that creates a dictionary with first_name, last_name, and all additional keyword arguments.
3. Write a function average_and_details(*args) that prints the average, minimum, and maximum of the provided numbers. Handle the empty case gracefully.
