# User-defined Functions and Arguments

**Course:** Python Programming Lab  
**Module:** 4 | **Lecture:** 4  
**Date:** 18-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Understand recursion: a function calling itself.
- Implement factorial and Fibonacci using recursion.
- Solve the Tower of Hanoi problem using recursion.

## Theory

Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem. Every recursive function must have at least one base case (a condition that stops the recursion) and a recursive case that moves toward the base case. Without a base case, the function would call itself infinitely, causing a stack overflow.

The factorial function is a classic recursive example: n! = n * (n-1)!, with base case 0! = 1. The Fibonacci sequence: fib(n) = fib(n-1) + fib(n-2), with base cases fib(0) = 0 and fib(1) = 1. Recursive solutions are often elegant but may be less efficient than iterative ones due to function call overhead.

The Tower of Hanoi is a mathematical puzzle where three rods and n disks must be moved from source to destination using an auxiliary rod. The recursive solution: move n-1 disks from source to auxiliary, move the nth disk from source to destination, then move n-1 disks from auxiliary to destination. The minimum number of moves is 2^n - 1.

## Procedure

1. Create a new Python file named lab22.py.
2. Write a recursive function factorial_recursive(n) with proper base case.
3. Write a recursive function fibonacci_recursive(n) that returns the nth Fibonacci number.
4. Write a recursive function tower_of_hanoi(n, source, auxiliary, destination) that prints each move.
5. Test all functions with small inputs and trace the recursion.
6. Compare recursive and iterative factorial for the same input.

## Source Code

```python
# Module 04 Lab 04: Recursive Functions

# Recursive factorial
def factorial_recursive(n):
    """Compute n! using recursion."""
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Recursive Fibonacci
def fibonacci_recursive(n):
    """Return the nth Fibonacci number (0-indexed)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, destination):
    """Solve Tower of Hanoi and print moves."""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Test factorial
print("--- Recursive Factorial ---")
for n in range(0, 8):
    print(f"{n}! = {factorial_recursive(n)}")

print("\n--- Recursive Fibonacci ---")
for n in range(0, 11):
    print(f"fib({n}) = {fibonacci_recursive(n)}")

print("\n--- Tower of Hanoi (3 disks) ---")
tower_of_hanoi(3, 'A', 'B', 'C')

# Comparison: Iterative vs Recursive factorial
print("\n--- Comparison: factorial(10) ---")
import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 10
print(f"Iterative: {factorial_iterative(n)}")
print(f"Recursive: {factorial_recursive(n)}")
```

## Sample Output

```
--- Recursive Factorial ---
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040

--- Recursive Fibonacci ---
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
fib(10) = 55

--- Tower of Hanoi (3 disks) ---
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

--- Comparison: factorial(10) ---
Iterative: 3628800
Recursive: 3628800
```

## Homework

1. Write a recursive function sum_recursive(n) that returns the sum of the first n natural numbers.
2. Write a recursive function power_recursive(base, exp) that computes base^exp (exp >= 0).
3. Write a recursive function count_digits(n) that returns the number of digits in a positive integer.
