# Basic Syntax, Variables, and Operators

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 2  
**Date:** 10-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Accept user input from the keyboard using the input() function.
- Convert string input to int and float types using type casting.
- Display formatted output using f-strings and the format() method.

## Theory

The input() function is used to take user input in Python. By default, input() always returns a string, even if the user types a number. To perform arithmetic operations on numeric input, you must first convert the string to an int (using int()) or a float (using float()). If you attempt arithmetic on string values, Python will raise a TypeError or concatenate strings instead.

Type conversion functions include int() for converting to integer, float() for converting to float, str() for converting to string, and bool() for converting to boolean. Not all conversions are valid -- for example, int("hello") will raise a ValueError because "hello" is not a valid integer literal.

Formatted output can be achieved using f-strings (f"...{variable}...") introduced in Python 3.6, the format() method ("...{}...".format(variable)), or the older %-formatting. f-strings are the most readable and recommended approach for new Python code. Format specifiers can control decimal places, padding, alignment, and number formatting.

## Procedure

1. Create a new Python file named lab02.py.
2. Use the input() function to prompt the user for their name and store it in a variable.
3. Use input() to ask for their age. Convert the input to an int using int().
4. Use input() to ask for their height in meters. Convert to float using float().
5. Use input() to ask for two numbers, convert both to float, and compute their sum, difference, product, and quotient.
6. Display results using f-strings with appropriate formatting (e.g., height to 2 decimal places).
7. Run the program and test with sample inputs.

## Source Code

```python
# Lab 02: User Input, Type Conversion, and Formatted Output

# Taking string input
name = input("Enter your name: ")

# Taking integer input with type conversion
age = int(input("Enter your age: "))

# Taking float input with type conversion
height = float(input("Enter your height in meters: "))

# Formatted output using f-string
print(f"Hello {name}, you are {age} years old and {height:.2f} meters tall.")

# Arithmetic with user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2

# Display results using f-strings with formatting
print(f"Sum: {sum_result:.2f}")
print(f"Difference: {diff_result:.2f}")
print(f"Product: {prod_result:.2f}")
print(f"Quotient: {quot_result:.2f}")

# Using format() method for comparison
print("Using format(): Sum = {}".format(sum_result))
```

## Sample Output

```
Enter your name: Bob
Enter your age: 22
Enter your height in meters: 1.75
Hello Bob, you are 22 years old and 1.75 meters tall.
Enter first number: 15.5
Enter second number: 3.2
Sum: 18.70
Difference: 12.30
Product: 49.60
Quotient: 4.84
Using format(): Sum = 18.7
```

## Homework

1. Write a program that asks the user for the radius of a circle (float), then computes and prints the area (pi * r^2) to 3 decimal places. Use 3.14159 for pi.
2. Write a program that asks for three test scores (integers), calculates the average, and prints it formatted to 2 decimal places.
3. Write a program that asks for the user's birth year, calculates their approximate age, and prints "You are approximately X years old."
