# Using Modules and File Input/Output

**Course:** Python Programming Lab  
**Module:** 5 | **Lecture:** 1  
**Date:** 09-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Import and use built-in modules: math and random.
- Create and import a custom module.
- Build a math operations menu using the math module and a random number game using the random module.

## Theory

Modules are Python files (.py) containing functions, classes, and variables that can be imported into other programs. The import statement loads a module: `import math` gives access to math.pi, math.sqrt(), etc. Selective imports: `from math import pi, sqrt` brings specific names into the current namespace. The `import ... as` syntax creates an alias: `import numpy as np`.

The math module provides mathematical functions: sqrt(), pow(), ceil(), floor(), sin(), cos(), log(), and constants like pi and e. The random module is used for generating pseudo-random numbers: random() returns a float in [0,1), randint(a,b) returns a random int between a and b inclusive, choice(seq) picks a random element, shuffle(list) shuffles in-place.

Creating a custom module is straightforward: write functions in a .py file and import it from another script. The custom module file should be in the same directory as the importing script (or in Python's module search path). The `__name__` variable is `"__main__"` when a script is run directly, and the module's filename when imported.

## Procedure

1. Create a new Python file named lab25.py.
2. Import the math module and demonstrate: sqrt(), ceil(), floor(), pi, sin(), cos().
3. Build an interactive math operations menu using math functions.
4. Import the random module and demonstrate: random(), randint(), choice(), shuffle().
5. Build a random number guessing game where the computer picks a number between 1 and 100.
6. Create a custom module named `my_utils.py` with a few helper functions.
7. Import and use my_utils.py in the main program.

## Source Code

```python
# Module 05 Lab 01: Using Modules (math, random) and Custom Module

# Importing math module
import math

print("--- Math Module ---")
num = float(input("Enter a number: "))
print(f"sqrt({num}) = {math.sqrt(num):.2f}")
print(f"ceil({num}) = {math.ceil(num)}")
print(f"floor({num}) = {math.floor(num)}")
print(f"pi = {math.pi:.6f}")
print(f"sin(pi/2) = {math.sin(math.pi/2):.2f}")
print(f"cos(0) = {math.cos(0):.2f}")

# Math operations menu
print("\n--- Math Operations Menu ---")
while True:
    print("\n1. Square root  2. Power  3. Sine  4. Cosine  5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        x = float(input("Enter number: "))
        print(f"sqrt({x}) = {math.sqrt(x):.2f}")
    elif choice == 2:
        b = float(input("Enter base: "))
        e = float(input("Enter exponent: "))
        print(f"{b}^{e} = {math.pow(b, e):.2f}")
    elif choice == 3:
        deg = float(input("Enter angle in degrees: "))
        print(f"sin({deg}) = {math.sin(math.radians(deg)):.4f}")
    elif choice == 4:
        deg = float(input("Enter angle in degrees: "))
        print(f"cos({deg}) = {math.cos(math.radians(deg)):.4f}")
    elif choice == 5:
        break

# Importing random module
import random

print("\n--- Random Module ---")
print(f"random() float: {random.random()}")
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"choice(['red','green','blue']): {random.choice(['red', 'green', 'blue'])}")

cards = ["Ace", "King", "Queen", "Jack", "10"]
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# Random number guessing game
print("\n--- Number Guessing Game ---")
secret = random.randint(1, 100)
guess = None
attempts = 0
while guess != secret:
    guess = int(input("Guess (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct in {attempts} attempts!")
```

Contents of custom module `my_utils.py` (save in same folder):

```python
# my_utils.py - Custom module with helper functions

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def rectangle_area(length, width):
    return length * width
```

Import and use in main:

```python
# Using the custom module
import my_utils

print("\n--- Custom Module (my_utils) ---")
print(f"is_even(7): {my_utils.is_even(7)}")
print(f"is_even(42): {my_utils.is_even(42)}")
print(f"celsius_to_fahrenheit(100): {my_utils.celsius_to_fahrenheit(100):.1f}F")
print(f"rectangle_area(5, 3): {my_utils.rectangle_area(5, 3)}")
```

## Sample Output

```
--- Math Module ---
Enter a number: 9.7
sqrt(9.7) = 3.11
ceil(9.7) = 10
floor(9.7) = 9
pi = 3.141593
sin(pi/2) = 1.00
cos(0) = 1.00

--- Math Operations Menu ---

1. Square root  2. Power  3. Sine  4. Cosine  5. Exit
Enter choice: 2
Enter base: 2
Enter exponent: 10
2.0^10.0 = 1024.00

1. Square root  2. Power  3. Sine  4. Cosine  5. Exit
Enter choice: 5

--- Random Module ---
random() float: 0.3748251793426973
randint(1, 10): 7
choice(['red','green','blue']): green
Shuffled cards: ['King', '10', 'Queen', 'Jack', 'Ace']

--- Number Guessing Game ---
Guess (1-100): 50
Too low!
Guess (1-100): 75
Too high!
Guess (1-100): 62
Correct in 3 attempts!

--- Custom Module (my_utils) ---
is_even(7): False
is_even(42): True
celsius_to_fahrenheit(100): 212.0F
rectangle_area(5, 3): 15
```

## Homework

1. Create a custom module `string_utils.py` with functions: reverse(s), count_vowels(s), and is_palindrome(s). Import and use it in another script.
2. Use the random module to simulate rolling two dice 100 times and print the frequency of each sum (2 to 12).
3. Use the math module to compute the area and circumference of a circle given the radius (use math.pi).
