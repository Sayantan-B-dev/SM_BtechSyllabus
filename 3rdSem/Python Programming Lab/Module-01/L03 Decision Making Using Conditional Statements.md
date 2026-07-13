# Decision Making Using Conditional Statements

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 3  
**Date:** 17-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Implement decision-making logic using if, if-else, and elif statements.
- Write a program to check if a number is even or odd.
- Build a grade calculator that assigns letter grades based on percentage marks.

## Theory

Conditional statements allow a program to execute different code based on specific conditions. The if statement evaluates a boolean expression; if it is True, the indented block under the if is executed. An optional else clause runs when the condition is False. The elif (short for "else if") allows checking multiple conditions sequentially.

The syntax is:
```python
if condition1:
    # block for condition1
elif condition2:
    # block for condition2
else:
    # block if none are true
```

Comparison operators used in conditions include == (equal to), != (not equal to), < (less than), > (greater than), <= (less than or equal), >= (greater than or equal). Logical operators like and, or, not combine multiple conditions. The modulo operator (%) is useful for checking divisibility: if a number % 2 == 0, the number is even.

## Procedure

1. Create a new Python file named lab03.py.
2. Write a program that takes an integer input and checks if it is even or odd using if-else.
3. Write a grade calculator program that asks the user for their marks out of 100.
4. Use elif to assign grades: >= 90 is A, >= 80 is B, >= 70 is C, >= 60 is D, >= 40 is E, and below 40 is F.
5. Write a program that reads a number and prints whether it is positive, negative, or zero.
6. Run all three programs and test with different inputs.

## Source Code

```python
# Lab 03: Decision Making - if, if-else, elif

# Program 1: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

print()  # blank line

# Program 2: Grade Calculator
marks = float(input("Enter your marks (out of 100): "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f"Marks: {marks}, Grade: {grade}")

print()

# Program 3: Positive, Negative, or Zero
value = float(input("Enter a number: "))
if value > 0:
    print(f"{value} is Positive.")
elif value < 0:
    print(f"{value} is Negative.")
else:
    print("The number is Zero.")
```

## Sample Output

```
Enter a number: 7
7 is Odd.

Enter your marks (out of 100): 85.5
Marks: 85.5, Grade: B

Enter a number: -3.2
-3.2 is Negative.
```

## Homework

1. Write a program that asks for a year and checks if it is a century year (divisible by 100).
2. Write a program that reads a character from the user and determines if it is a vowel (a, e, i, o, u) or a consonant. Assume the input is a lowercase letter.
3. Write a program that takes three numbers and prints the smallest among them using if-elif-else.
