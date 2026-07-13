# Basic Syntax, Variables, and Operators

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 1  
**Date:** 10-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Write and execute Python programs using basic syntax rules.
- Declare and initialize variables of types int, float, str, and bool.
- Perform arithmetic operations and use the type() function for type checking.

## Theory

Python is an interpreted, dynamically-typed programming language. Unlike compiled languages, Python code is executed line by line by the Python interpreter. Python's syntax emphasizes readability, using indentation (whitespace) to define blocks of code instead of curly braces or keywords.

Variables in Python do not require explicit type declarations. The interpreter infers the type at runtime based on the value assigned. The primary built-in data types are int (integers), float (decimal numbers), str (strings/text), and bool (True/False). The type() function returns the data type of any value or variable.

Arithmetic operators in Python include + (addition), - (subtraction), * (multiplication), / (division returning float), // (integer/floor division), % (modulus/remainder), and ** (exponentiation). Operator precedence follows standard mathematical rules, where parentheses have the highest precedence.

## Procedure

1. Open IDLE or VS Code and create a new Python file named lab01.py.
2. Write the first program to print "Hello, World!" to the console using the print() function.
3. Declare variables of different types: an integer for age, a float for price, a string for name, and a boolean for is_student.
4. Use print() with f-strings to display the values of each variable.
5. Use the type() function to check and print the data type of each variable.
6. Write arithmetic expressions that use all the operators: +, -, *, /, //, %, **.
7. Print the results of each arithmetic operation.
8. Run the program and verify the output matches the expected results.

## Source Code

```python
# Lab 01: Basic Syntax, Variables, and Operators
# Step 1: Hello World
print("Hello, World!")

# Step 2: Declare variables
age = 20                # int
price = 49.99          # float
name = "Alice"         # str
is_student = True      # bool

# Step 3: Display variables using f-strings
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price: {price}")
print(f"Is Student: {is_student}")

# Step 4: Type checking with type()
print(f"Type of age: {type(age)}")
print(f"Type of price: {type(price)}")
print(f"Type of name: {type(name)}")
print(f"Type of is_student: {type(is_student)}")

# Step 5: Arithmetic operators
a = 15
b = 4

print(f"a + b = {a + b}")    # Addition: 19
print(f"a - b = {a - b}")    # Subtraction: 11
print(f"a * b = {a * b}")    # Multiplication: 60
print(f"a / b = {a / b}")    # Division: 3.75
print(f"a // b = {a // b}")   # Floor division: 3
print(f"a % b = {a % b}")    # Modulus: 3
print(f"a ** b = {a ** b}")   # Exponentiation: 15^4 = 50625
```

## Sample Output

```
Hello, World!
Name: Alice
Age: 20
Price: 49.99
Is Student: True
Type of age: <class 'int'>
Type of price: <class 'float'>
Type of name: <class 'str'>
Type of is_student: <class 'bool'>
a + b = 19
a - b = 11
a * b = 60
a / b = 3.75
a // b = 3
a % b = 3
a ** b = 50625
```

## Homework

1. Write a program that declares variables for your name, roll number, and favorite subject. Print them in a single sentence using an f-string.
2. Compute the area of a rectangle given length = 12.5 and width = 8.3. Print the result with a descriptive message.
3. Given x = 27 and y = 5, print the quotient (using //) and remainder (using %) when x is divided by y.
