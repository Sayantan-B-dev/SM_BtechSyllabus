# Lambda Functions, Variable Scope, and Recursion

**Course:** Python Programming Lab  
**Module:** 4 | **Lecture:** 6  
**Date:** 25-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Understand global and local variable scope in Python.
- Use the global keyword to modify global variables inside functions.
- Create closures: inner functions that remember their enclosing scope.
- Build a counter closure function.

## Theory

Scope refers to the region of a program where a variable is accessible. Variables defined inside a function are local to that function and cannot be accessed outside it. Variables defined at the top level of a module are global and accessible throughout the module. When a variable is referenced, Python searches in the order: local, enclosing, global, built-in (LEGB rule).

The global keyword allows a function to modify a global variable. Without it, assigning to a variable inside a function creates a new local variable that shadows the global one. Using global should be done sparingly as it makes code harder to debug. The nonlocal keyword is used in nested functions to refer to variables in the enclosing (but non-global) scope.

A closure is a function that remembers variables from its enclosing scope even after that scope has finished executing. Closures are created when a nested function references a variable from its enclosing function. The counter function pattern is a classic closure: an outer function initializes a counter and returns an inner function that increments and returns it. Each call to the outer function creates an independent counter.

## Procedure

1. Create a new Python file named lab24.py.
2. Demonstrate local vs global scope: define a global variable and try to access/modify it inside a function.
3. Use the global keyword to modify a global variable from within a function.
4. Write a closure for a counter: a function make_counter() that returns an inner function incrementing a count.
5. Demonstrate that each closure has its own independent state by creating two counters.
6. Write a closure that multiplies numbers by a given factor (multiplier factory).
7. Test all programs.

## Source Code

```python
# Module 04 Lab 06: Global/Local Scope and Closures

# Global vs Local scope
x = 10  # global variable

def show_scope():
    y = 20  # local variable
    print(f"Inside function: x = {x} (global), y = {y} (local)")

show_scope()
# print(y)  # Error: NameError if uncommented (y is local)
print(f"Outside function: x = {x} (global)")

# Modifying global variable (without global keyword)
count = 0

def increment_wrong():
    count = count + 1  # Error: UnboundLocalError

def increment_correct():
    global count
    count += 1
    print(f"count inside: {count}")

# increment_wrong()  # Uncomment to see: UnboundLocalError
increment_correct()
increment_correct()
print(f"count outside: {count}")

# Closures: Counter
print("\n--- Counter Closure ---")
def make_counter():
    """Return a counter function that increments on each call."""
    count = 0  # enclosed variable

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# Create two independent counters
counter1 = make_counter()
counter2 = make_counter()

print("Counter 1:")
print(f"  {counter1()}")  # 1
print(f"  {counter1()}")  # 2
print(f"  {counter1()}")  # 3

print("Counter 2 (independent):")
print(f"  {counter2()}")  # 1
print(f"  {counter2()}")  # 2

print("Counter 1 again:")
print(f"  {counter1()}")  # 4 (continues from where it left off)

# Closure: Multiplier Factory
print("\n--- Multiplier Factory ---")
def make_multiplier(factor):
    """Return a function that multiplies its argument by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")
print(f"double(10) = {double(10)}")
print(f"triple(5) = {triple(5)}")
print(f"triple(10) = {triple(10)}")
```

## Sample Output

```
Inside function: x = 10 (global), y = 20 (local)
Outside function: x = 10 (global)
count inside: 1
count inside: 2
count outside: 2

--- Counter Closure ---
Counter 1:
  1
  2
  3
Counter 2 (independent):
  1
  2
Counter 1 again:
  4

--- Multiplier Factory ---
double(5) = 10
double(10) = 20
triple(5) = 15
triple(10) = 30
```

## Homework

1. Write a closure `make_power(n)` that returns a function that raises its argument to the nth power. Create square = make_power(2) and cube = make_power(3).
2. Write a closure `make_password_checker(password)` that returns a function that takes a guess and returns True if it matches. The password should be hidden in the closure, not accessible globally.
3. Write a program that demonstrates the difference between local and global scope: create a global list, a function that appends to it using the list's append() method (no global keyword needed for mutation), and another function that reassigns it (needs global keyword).
