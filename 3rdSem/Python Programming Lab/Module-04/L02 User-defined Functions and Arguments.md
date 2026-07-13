# User-defined Functions and Arguments

**Course:** Python Programming Lab  
**Module:** 4 | **Lecture:** 2  
**Date:** 11-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Understand positional and keyword arguments in function calls.
- Use default parameter values in function definitions.
- Write a power function with a default exponent and a student info function with varying parameters.

## Theory

Python functions accept arguments in two ways: positional arguments are matched by order, and keyword arguments are matched by name. Positional arguments must be provided in the same order as the parameters. Keyword arguments use the `param=value` syntax and can be specified in any order after positional arguments.

Default parameter values are assigned in the function definition: `def func(param=default)`. If the caller does not provide a value for that parameter, the default is used. Defaults are evaluated once at function definition time (not each call). Parameters with defaults must come after parameters without defaults in the function signature.

Combining positional and keyword arguments follows the rule: all positional arguments must come before any keyword arguments in a function call. For example, `student_info("Alice", 20, course="CS")` is valid, but `student_info(name="Alice", 20)` is not. These features give callers flexibility and make functions easier to use with sensible defaults.

## Procedure

1. Create a new Python file named lab20.py.
2. Define a function power(base, exponent=2) that returns base^exponent (default exponent is 2).
3. Call power with one argument (uses default) and with two arguments.
4. Define a function student_info(name, age, course="Python", grade="Not graded") that prints student details.
5. Call student_info with different combinations of positional and keyword arguments.
6. Write a function create_profile(name, **kwargs) that accepts any number of keyword arguments.
7. Test all functions.

## Source Code

```python
# Module 04 Lab 02: Positional, Keyword, and Default Arguments

# Function with default argument
def power(base, exponent=2):
    """Compute base raised to the exponent power (default exponent=2)."""
    return base ** exponent

print("--- Power Function ---")
print(f"power(5) = {power(5)}")           # uses default exponent=2
print(f"power(5, 3) = {power(5, 3)}")     # positional: base=5, exponent=3
print(f"power(exponent=4, base=3) = {power(exponent=4, base=3)}")  # keyword args, order doesn't matter

# Function with multiple default parameters
def student_info(name, age, course="Python", grade="Not graded"):
    """Display student information."""
    print("\n--- Student Info ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Grade: {grade}")

print("\n--- Student Info Function ---")
# Positional only
student_info("Alice", 20)

# Positional + keyword
student_info("Bob", 22, course="Data Science")

# All keyword arguments
student_info(name="Charlie", age=21, grade="A", course="Web Dev")

# Default used for grade
student_info("Diana", 23, "AI/ML")

# Function accepting arbitrary keyword arguments (**kwargs)
def create_profile(name, **kwargs):
    """Create a profile dictionary with name and any additional info."""
    profile = {"name": name}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

print("\n--- Profile Builder ---")
profile1 = create_profile("Alice", age=20, city="NYC", hobby="Reading")
print(f"Profile 1: {profile1}")

profile2 = create_profile("Bob", occupation="Engineer", skills=["Python", "Java"])
print(f"Profile 2: {profile2}")
```

## Sample Output

```
--- Power Function ---
power(5) = 25
power(5, 3) = 125
power(exponent=4, base=3) = 81

--- Student Info Function ---

--- Student Info ---
Name: Alice
Age: 20
Course: Python
Grade: Not graded

--- Student Info ---
Name: Bob
Age: 22
Course: Data Science
Grade: Not graded

--- Student Info ---
Name: Charlie
Age: 21
Course: Web Dev
Grade: A

--- Student Info ---
Name: Diana
Age: 23
Course: AI/ML
Grade: Not graded

--- Profile Builder ---
Profile 1: {'name': 'Alice', 'age': 20, 'city': 'NYC', 'hobby': 'Reading'}
Profile 2: {'name': 'Bob', 'occupation': 'Engineer', 'skills': ['Python', 'Java']}
```

## Homework

1. Write a function `greet(name, greeting="Hello")` that prints a greeting message. Test it with and without the greeting parameter.
2. Write a function `rectangle_area(length, width=None)` that calculates area. If only one argument is given, treat it as a square (length == width).
3. Write a function `order_summary(item, quantity=1, price=0.0, discount=0)` that prints a summary and returns the total cost after discount.
