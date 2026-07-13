# Looping Statements (For, While, Nested Loops)

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 8  
**Date:** 22-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

Loops allow you to execute a block of code repeatedly. Python provides two primary loop structures: `for` and `while`.

---

### 1. The `for` Loop

The `for` loop in Python is used to iterate over a sequence (such as a list, string, tuple, or range). It is not a traditional C-style `for (i=0; i<10; i++)` loop; instead, it is a **for-each** loop.

**Syntax:**

```python
for variable in sequence:
    # code to execute for each item
    statements
```

#### 1.1 Iterating over a `range()`

The `range()` function generates a sequence of numbers and is commonly used with `for` loops.

```python
# Print numbers 0 to 4
for i in range(5):
    print(i)
```

**Output:**

```
0
1
2
3
4
```

**`range(start, stop, step)`:**

```python
# range(start, stop) -- from start to stop-1
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5

print()

# range(start, stop, step) -- with step size
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8

print()

# Negative step (counting backward)
for i in range(10, 0, -2):
    print(i, end=" ")  # 10 8 6 4 2
```

**Output:**

```
2 3 4 5
0 2 4 6 8
10 8 6 4 2
```

**Understanding `range()`:**

| Call | Sequence Generated |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |
| `range(5, 1)` | (empty -- start < stop but step is positive) |

#### 1.2 Iterating over a String

```python
for char in "Python":
    print(char, end=" ")
```

**Output:**

```
P y t h o n
```

#### 1.3 Iterating over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
```

**Output:**

```
I like apple
I like banana
I like cherry
```

#### 1.4 Iterating over a Tuple and Dictionary

```python
# Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# Dictionary (iterates over keys by default)
student = {"name": "Alice", "age": 22, "grade": "A"}
for key in student:
    print(f"{key}: {student[key]}")

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key} = {value}")
```

---

### 2. The `while` Loop

The `while` loop executes a block of code as long as a condition remains `True`.

**Syntax:**

```python
while condition:
    # code to execute repeatedly
    statements
```

**Example 1: Print 1 to 5**

```python
i = 1
while i <= 5:
    print(i)
    i += 1  # IMPORTANT: update the variable, or the loop runs forever!
```

**Output:**

```
1
2
3
4
5
```

**Example 2: Sum of numbers until user enters 0**

```python
total = 0
num = float(input("Enter a number (0 to stop): "))

while num != 0:
    total += num
    num = float(input("Enter a number (0 to stop): "))

print(f"Total sum: {total}")
```

**Run:**

```
Enter a number (0 to stop): 10
Enter a number (0 to stop): 25
Enter a number (0 to stop): -5
Enter a number (0 to stop): 0
Total sum: 30.0
```

**Example 3: Count digits in a number**

```python
num = 12345
count = 0

while num > 0:
    num //= 10  # Remove the last digit
    count += 1

print(f"Number of digits: {count}")  # 5
```

---

### 3. Infinite Loops

An **infinite loop** is a loop that never terminates. This happens when the condition never becomes `False`.

```python
# DANGER: This will run forever!
# i = 1
# while i > 0:
#     print(i)
#     i += 1  # i keeps increasing, condition never False
```

To stop an infinite loop, press `Ctrl + C` in the terminal.

**Common causes of infinite loops:**

1. Forgetting to update the loop variable:

```python
i = 1
while i <= 10:
    print(i)
    # Missing: i += 1
```

2. Wrong condition logic:

```python
x = 5
while x > 0:
    print(x)
    x += 1  # Oops: x increases, so it's always > 0
```

3. Using `=` instead of `!=` or `==`:

```python
# Suppose we want to stop when input is "quit"
choice = ""
while choice != "quit":
    choice = input("Enter command: ")  # Works correctly
```

---

### 4. The `break` Statement (Introduction)

The `break` statement immediately exits the loop, regardless of the loop condition. Execution continues with the first statement after the loop.

**Example: Find the first number divisible by 7 and 11**

```python
for i in range(1, 200):
    if i % 7 == 0 and i % 11 == 0:
        print(f"Found: {i}")
        break  # Exit the loop once found
```

**Output:**

```
Found: 77
```

Without `break`, the loop would continue through all 199 numbers. With `break`, it stops as soon as it finds the answer.

**Example: Input validation with break**

```python
while True:  # Infinite loop (intentional)
    password = input("Enter password: ")
    if password == "python123":
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")
```

**Run:**

```
Enter password: hello
Wrong password. Try again.
Enter password: python123
Access granted!
```

---

### 5. The `continue` Statement (Introduction)

The `continue` statement skips the rest of the current iteration and moves to the next iteration of the loop.

**Example: Print odd numbers between 1 and 10**

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
```

**Output:**

```
1 3 5 7 9
```

**Example: Process only valid inputs**

```python
numbers = [10, -5, 25, -8, 15, 0, 30]

for num in numbers:
    if num <= 0:
        continue  # Skip non-positive numbers
    print(f"Processing: {num}")
```

**Output:**

```
Processing: 10
Processing: 25
Processing: 15
Processing: 30
```

---

### 6. `break` vs `continue` (First Look)

| Statement | Effect |
|---|---|
| `break` | Exits the loop entirely. |
| `continue` | Skips the rest of the current iteration, goes to the next iteration. |

```python
# Demonstration: break vs continue
print("With break:")
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")  # 1 2

print("\nWith continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")  # 1 2 4 5
```

**Output:**

```
With break:
1 2
With continue:
1 2 4 5
```

---

### 7. Complete Code Examples

#### Example 1: Print 1 to N

```python
# Program: Print numbers from 1 to N

n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print(f"Numbers from 1 to {n}:")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()  # New line at the end
```

**Run:**

```
Enter a positive number: 7
Numbers from 1 to 7:
1 2 3 4 5 6 7
```

#### Example 2: Sum of Numbers from 1 to N

```python
# Program: Sum of numbers from 1 to N

n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"Sum of numbers from 1 to {n} is {total}")

    # Verify using formula: n(n+1)/2
    formula_result = n * (n + 1) // 2
    print(f"Using formula (n(n+1)/2): {formula_result}")
```

**Run:**

```
Enter a positive number: 100
Sum of numbers from 1 to 100 is 5050
Using formula (n(n+1)/2): 5050
```

#### Example 3: Multiplication Table of a Number

```python
# Program: Print multiplication table

num = int(input("Enter a number: "))

print(f"Multiplication table for {num}:")
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i:2d} = {product:3d}")
```

**Run:**

```
Enter a number: 7
Multiplication table for 7:
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
7 x  4 =  28
7 x  5 =  35
7 x  6 =  42
7 x  7 =  49
7 x  8 =  56
7 x  9 =  63
7 x 10 =  70
```

#### Example 4: Factorial Calculation

```python
# Program: Calculate factorial of a number

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print(f"0! = 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"{n}! = {factorial}")
```

**Run:**

```
Enter a non-negative integer: 6
6! = 720
```

#### Example 5: Fibonacci Sequence (While Loop)

```python
# Program: Print Fibonacci sequence up to N terms

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    a, b = 0, 1
    count = 0

    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

    print()
```

**Run:**

```
Enter the number of terms: 10
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34
```

**Explanation of `a, b = b, a + b`:** This updates both variables simultaneously. Python evaluates the right side first (creating a tuple `(b, a+b)`) before assigning to `a` and `b`.

---

### 8. Loop Control Summary

```python
# for loop example with all control statements
for i in range(1, 11):
    if i == 3:
        continue  # Skip 3
    if i == 8:
        break     # Stop at 8
    print(i, end=" ")
else:
    print("\nLoop completed normally")  # This won't execute because break was used

# Output: 1 2 4 5 6 7
```

---

## Practice Problems

1. **Sum of Even Numbers:** Write a program that takes a number N and calculates the sum of all even numbers from 1 to N using a `for` loop.

2. **Countdown Timer:** Write a program that takes a number N and counts down from N to 1 using a `while` loop, then prints "Blast off!". Ensure the program handles negative input.

3. **Find the First:** Write a program that finds the first number between 1 and 1000 that is divisible by 13 and 17. Use a `for` loop with `break`.

4. **Skip Multiples:** Write a program that prints numbers from 1 to 30, but skips numbers that are multiples of 3. Use `continue`.

5. **Average Calculator:** Write a program that keeps taking numbers from the user until they enter -1. Then calculate and print the average of all numbers entered (excluding -1). Use a `while` loop.

6. **Palindrome Checker:** Write a program that checks if a given number is a palindrome (reads the same forward and backward, e.g., 121, 12321). Use a `while` loop to reverse the number and compare.
