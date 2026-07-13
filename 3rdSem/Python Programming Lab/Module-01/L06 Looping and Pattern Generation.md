# Looping and Pattern Generation

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 6  
**Date:** 24-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Implement iterative logic using while loops.
- Use loop control variables to manage repetition.
- Write programs to generate the Fibonacci series, implement a number guessing game, and compute GCD using Euclid's algorithm.

## Theory

A while loop repeatedly executes a block of code as long as a given condition remains True. The syntax is:
```python
while condition:
    # loop body
```
The condition is evaluated before each iteration. If the condition becomes False, the loop exits. If the condition never becomes False, the loop runs forever (infinite loop). Care must be taken to update variables within the loop body to eventually make the condition False.

The Fibonacci series starts with 0 and 1, where each subsequent term is the sum of the two preceding terms: 0, 1, 1, 2, 3, 5, 8, 13, ... The GCD (Greatest Common Divisor) of two numbers can be found using Euclid's algorithm: repeatedly replace the larger number with the remainder of dividing the larger by the smaller, until the remainder is 0. The last non-zero remainder is the GCD.

A number guessing game demonstrates interactive while loops: the program picks a random number, and the user repeatedly guesses. After each guess, the program gives feedback (too high/too low) until the correct number is found. A flag variable (boolean) controls the loop.

## Procedure

1. Create a new Python file named lab06.py.
2. Write a program using a while loop to print numbers 1 to 10.
3. Write a program to generate the Fibonacci series up to n terms using a while loop.
4. Write a number guessing game where the secret number is 42 (hardcoded) and the user guesses until correct.
5. Write a program to compute the GCD of two numbers using Euclid's algorithm with a while loop.
6. Test each program.

## Source Code

```python
# Lab 06: While Loop, Fibonacci, Number Guessing, GCD

# Program 1: Print 1 to 10 using while
print("Numbers 1 to 10:")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# Program 2: Fibonacci series up to n terms
n = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
count = 0
print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

# Program 3: Number Guessing Game
secret = 42
guess = None
attempts = 0
print("Guess the number (between 1 and 100):")
while guess != secret:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")

# Program 4: GCD using Euclid's algorithm
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y != 0:
    x, y = y, x % y
print(f"GCD of {a} and {b} is {x}")
```

## Sample Output

```
Numbers 1 to 10:
1 2 3 4 5 6 7 8 9 10
Enter number of Fibonacci terms: 8
Fibonacci Series:
0 1 1 2 3 5 8 13
Guess the number (between 1 and 100):
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 42
Correct! You guessed it in 3 attempts.
Enter first number: 48
Enter second number: 18
GCD of 48 and 18 is 6
```

## Homework

1. Write a program using a while loop to find the sum of digits of a given integer (e.g., 123 -> 1+2+3 = 6).
2. Write a program that keeps asking the user for numbers until they enter 0, then prints the sum and average.
3. Write a program to reverse a given integer using a while loop (e.g., 1234 -> 4321).
