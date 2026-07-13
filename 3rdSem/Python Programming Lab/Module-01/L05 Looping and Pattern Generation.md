# Looping and Pattern Generation

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 5  
**Date:** 24-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Use the for loop with the range() function for iteration.
- Write programs to print sequences of numbers and compute sums of series.
- Implement a factorial calculator using a for loop.

## Theory

A for loop in Python iterates over a sequence (list, tuple, string, or range). The range() function generates a sequence of numbers. range(stop) produces numbers from 0 to stop-1. range(start, stop) produces from start to stop-1. range(start, stop, step) increments by step. The default step is 1.

For loops follow the syntax:
```python
for variable in sequence:
    # loop body
```

The variable takes each value in the sequence one by one. The loop body (indented) executes once per value. Common uses include iterating a fixed number of times, processing each element of a collection, and accumulating results like sums or products.

The factorial of a non-negative integer n (written n!) is the product of all positive integers from 1 to n. By convention, 0! = 1. Factorial can be calculated iteratively using a for loop: start with result = 1, then multiply by each integer from 1 to n.

## Procedure

1. Create a new Python file named lab05.py.
2. Write a for loop using range() to print numbers from 1 to 10.
3. Write a loop to print even numbers from 2 to 20 using range() with a step of 2.
4. Write a program that takes a number n and computes the sum of the series 1 + 2 + 3 + ... + n.
5. Write a program that takes an integer n and computes the sum of squares: 1^2 + 2^2 + ... + n^2.
6. Write a factorial calculator that reads n and computes n! using a for loop.
7. Test all programs.

## Source Code

```python
# Lab 05: For Loop with range()

# Program 1: Print numbers 1 to 10
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Program 2: Even numbers 2 to 20
print("Even numbers 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Program 3: Sum of first n natural numbers
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n} is {total}")

# Program 4: Sum of squares
n2 = int(input("Enter n for sum of squares: "))
sum_sq = 0
for i in range(1, n2 + 1):
    sum_sq += i * i
print(f"Sum of squares 1^2 to {n2}^2 is {sum_sq}")

# Program 5: Factorial
num = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")
```

## Sample Output

```
Numbers 1 to 10:
1 2 3 4 5 6 7 8 9 10
Even numbers 2 to 20:
2 4 6 8 10 12 14 16 18 20
Enter n: 10
Sum of 1 to 10 is 55
Enter n for sum of squares: 5
Sum of squares 1^2 to 5^2 is 55
Enter a number for factorial: 6
6! = 720
```

## Homework

1. Write a program that prints the multiplication table of a number entered by the user (up to 10).
2. Write a program to compute the sum of all odd numbers between 1 and a given n.
3. Write a program to compute n raised to the power m (n^m) without using the ** operator, using a for loop.
