# Decision Making Using Conditional Statements

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 4  
**Date:** 17-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Use nested if statements to handle multiple levels of conditions.
- Apply the ternary (conditional) operator for concise inline decisions.
- Implement pattern matching using the match-case statement (Python 3.10+).

## Theory

Nested if statements place one if-else construct inside another. This is useful when a condition depends on a previous condition being true. For example, checking if a year is a leap year involves multiple conditions: divisible by 400, or divisible by 4 but not by 100. Indentation must be consistent to correctly associate blocks.

The ternary operator (also called conditional expression) evaluates a condition in a single line: `value_if_true if condition else value_if_false`. It is useful for simple assignments that depend on a boolean condition, reducing the need for a full if-else block.

The match-case statement (introduced in Python 3.10) works like a switch statement in other languages. It compares a value against multiple patterns and executes the matching block. Each case can include a literal value, and the underscore _ acts as a default wildcard. match-case improves readability when handling many discrete values.

## Procedure

1. Create a new Python file named lab04.py.
2. Write a leap year checker using nested if conditions.
3. Write a program to find the largest of three numbers using nested if.
4. Write a program that uses the ternary operator to check voting eligibility.
5. Write a program using match-case that displays the day name from a number (1-7).
6. Test each program with multiple inputs.

## Source Code

```python
# Lab 04: Nested if, Ternary Operator, match-case

# Program 1: Leap Year Checker using nested if
year = int(input("Enter a year: "))
if year % 400 == 0:
    print(f"{year} is a Leap Year.")
else:
    if year % 100 == 0:
        print(f"{year} is not a Leap Year.")
    else:
        if year % 4 == 0:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")

print()

# Program 2: Largest of three numbers using nested if
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print(f"The largest number is {largest}")

print()

# Program 3: Ternary operator for voting eligibility
age = int(input("Enter your age: "))
status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(status)

print()

# Program 4: match-case for day name
day_num = int(input("Enter day number (1-7): "))
match day_num:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"
    case 5:
        day_name = "Friday"
    case 6:
        day_name = "Saturday"
    case 7:
        day_name = "Sunday"
    case _:
        day_name = "Invalid day number"
print(day_name)
```

## Sample Output

```
Enter a year: 2024
2024 is a Leap Year.

Enter first number: 45
Enter second number: 78
Enter third number: 23
The largest number is 78.0

Enter your age: 16
Not eligible to vote

Enter day number (1-7): 5
Friday
```

## Homework

1. Write a program using nested if to check if a triangle is valid based on three angles (sum must be 180, each angle > 0).
2. Use the ternary operator to assign "Pass" or "Fail" based on marks >= 40.
3. Write a match-case program that takes a month number (1-12) and prints the number of days in that month. Assume February has 28 days.
