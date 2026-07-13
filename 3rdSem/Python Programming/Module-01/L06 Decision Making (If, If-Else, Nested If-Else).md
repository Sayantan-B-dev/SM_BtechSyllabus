# Decision Making (If, If-Else, Nested If-Else)

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 6  
**Date:** 20-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

Decision-making statements allow a program to execute different code paths based on conditions. Python uses `if`, `elif`, and `else` to implement conditional logic.

---

### 1. The `if` Statement

The `if` statement evaluates a condition. If the condition is `True`, the indented block of code runs. If it is `False`, the block is skipped.

**Syntax:**

```python
if condition:
    # code to execute if condition is True
    statement1
    statement2
```

**IMPORTANT:** The colon (`:`) is required after the condition. The indented block must be consistent (typically 4 spaces).

**Example 1: Basic if**

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
    print("Please register to vote.")

print("This line always runs.")
```

**Output:**

```
You are eligible to vote.
Please register to vote.
This line always runs.
```

**Example 2: If with False condition**

```python
age = 16

if age >= 18:
    print("You are eligible to vote.")  # This will NOT print

print("This line always runs.")
```

**Output:**

```
This line always runs.
```

---

### 2. The `if-else` Statement

The `if-else` statement provides an alternative block that executes when the condition is `False`.

**Syntax:**

```python
if condition:
    # code if condition is True
    statements
else:
    # code if condition is False
    statements
```

**Example 1: Even or Odd**

```python
number = 7

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

**Output:**

```
7 is odd.
```

**Example 2: Positive or Negative**

```python
num = -5

if num >= 0:
    print(f"{num} is positive or zero.")
else:
    print(f"{num} is negative.")
```

**Output:**

```
-5 is negative.
```

---

### 3. The `elif` Clause

`elif` (short for "else if") allows you to check multiple conditions. Python evaluates conditions from top to bottom. The first `True` condition executes its block, and the rest are skipped.

**Syntax:**

```python
if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
elif condition3:
    # code if condition3 is True
else:
    # code if none of the above are True
```

**Example 1: Grade Classifier**

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
```

**Output:**

```
Score: 85, Grade: B
```

**How it works for `score = 85`:**
1. `85 >= 90`? False -- skip.
2. `85 >= 80`? True -- execute this block, set grade to "B".
3. Skip the remaining `elif` and `else` blocks.

**Example 2: Day of the Week**

```python
day_num = 3

if day_num == 1:
    day_name = "Monday"
elif day_num == 2:
    day_name = "Tuesday"
elif day_num == 3:
    day_name = "Wednesday"
elif day_num == 4:
    day_name = "Thursday"
elif day_num == 5:
    day_name = "Friday"
elif day_num == 6:
    day_name = "Saturday"
elif day_num == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid day number"

print(f"Day {day_num} is {day_name}.")
```

**Output:**

```
Day 3 is Wednesday.
```

---

### 4. Nested if-else Statements

You can place one `if` (or `if-else`) inside another `if` (or `if-else`). This is called **nesting**.

**Syntax:**

```python
if outer_condition:
    if inner_condition:
        # code when both are True
    else:
        # code when outer is True but inner is False
else:
    # code when outer is False
```

**Example 1: Number Category**

```python
num = 15

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print(f"{num} is positive.")
        
        if num % 2 == 0:
            print("It is also even.")
        else:
            print("It is also odd.")
else:
    print(f"{num} is negative.")
```

**Output:**

```
15 is positive.
It is also odd.
```

**Example 2: Login System**

```python
username = "admin"
password = "pass123"

if username == "admin":
    if password == "pass123":
        print("Login successful. Welcome, admin!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
```

**Output:**

```
Login successful. Welcome, admin!
```

**Important:** Deep nesting (more than 3 levels) can make code hard to read. In such cases, consider using logical operators (`and`, `or`) to flatten the structure.

---

### 5. Conditional Expressions (Ternary Operator)

Python supports a one-line conditional expression, often called the **ternary operator**.

**Syntax:**

```python
value_if_true if condition else value_if_false
```

**Example 1: Find the maximum of two numbers**

```python
a, b = 10, 20
max_num = a if a > b else b
print(f"The maximum is {max_num}")  # The maximum is 20
```

**Example 2: Check adult status**

```python
age = 17
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")  # Status: Minor
```

**Example 3: Nested ternary (use sparingly)**

```python
num = 0
result = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
print(f"{num} is {result}")  # 0 is Zero
```

**Comparison: Ternary vs. if-else**

```python
# Using if-else (5 lines)
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Using ternary (1 line, same result)
status = "Adult" if age >= 18 else "Minor"
```

---

### 6. Multiple Conditions with `and` / `or`

You can combine multiple conditions in a single `if` statement using logical operators.

**Example 1: Driving eligibility (all conditions must be True)**

```python
age = 18
has_license = True
passed_eye_test = True

if age >= 18 and has_license and passed_eye_test:
    print("You are legally allowed to drive.")
else:
    print("You cannot drive yet.")
```

**Output:**

```
You are legally allowed to drive.
```

**Example 2: Weekend or holiday (at least one condition must be True)**

```python
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("No work today!")
else:
    print("Time to work.")
```

**Output:**

```
No work today!
```

**Example 3: Complex condition (combined and/or)**

```python
age = 65
is_retired = False
is_veteran = True

# Check eligibility for senior discount
if (age >= 60 or is_retired) and is_veteran:
    print("You are eligible for the special discount.")
else:
    print("Not eligible.")
```

**Output:**

```
You are eligible for the special discount.
```

---

### 7. Complete Code Examples

#### Example 1: Even/Odd Checker

```python
# Program: Check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```

**Run:**

```
Enter a number: 7
7 is odd.
```

#### Example 2: Grade Calculator

```python
# Program: Calculate letter grade based on percentage

percentage = float(input("Enter your percentage: "))

if percentage > 100 or percentage < 0:
    print("Invalid percentage. Enter a value between 0 and 100.")
elif percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
```

**Run:**

```
Enter your percentage: 85.5
Percentage: 85.50%
Grade: B
```

#### Example 3: Leap Year Checker

A year is a leap year if:
- It is divisible by 400, OR
- It is divisible by 4 but NOT by 100.

```python
# Program: Check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

**Run:**

```
Enter a year: 2024
2024 is a leap year.
```

**Test cases:**

| Year | Divisible by 400? | Divisible by 4? | Divisible by 100? | Leap? |
|---|---|---|---|---|
| 1900 | No | Yes | Yes | No |
| 2000 | Yes | Yes | Yes | Yes |
| 2024 | No | Yes | No | Yes |
| 2023 | No | No | - | No |

#### Example 4: Largest of Three Numbers

```python
# Program: Find the largest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}")
```

**Run:**

```
Enter first number: 10
Enter second number: 25
Enter third number: 7
The largest number is 25.0
```

---

### 8. Common Mistakes

| Mistake | Wrong Code | Correct Code |
|---|---|---|
| Missing colon | `if x > 5` | `if x > 5:` |
| Inconsistent indentation | mixed tabs and spaces | Use 4 spaces consistently |
| Using `=` instead of `==` | `if x = 5:` | `if x == 5:` |
| Empty if block | `if x > 5:` (nothing indented) | `if x > 5: pass` or add code |
| Forgetting `elif` chain stops | Adding `else if` (no such keyword) | Use `elif` |

---

## Practice Problems

1. **Positive, Negative, or Zero:** Write a program that takes a number as input and prints whether it is positive, negative, or zero.

2. **Vowel or Consonant:** Write a program that takes a single character as input and determines if it is a vowel (a, e, i, o, u) or a consonant. Handle both uppercase and lowercase.

3. **Ticket Price Calculator:** Write a program that calculates movie ticket price based on age:
   - Age < 5: Free (Rs. 0)
   - Age 5-12: Rs. 50
   - Age 13-59: Rs. 100
   - Age 60+: Rs. 60

4. **Triangle Type:** Write a program that takes three side lengths and determines if they form:
   - An equilateral triangle (all sides equal)
   - An isosceles triangle (two sides equal)
   - A scalene triangle (all sides different)
   - Or no triangle (sum of any two sides <= third)

5. **ATM Withdrawal:** Write a program that asks for account balance and withdrawal amount. Check:
   - If withdrawal amount is positive
   - If account has sufficient balance
   - If withdrawal amount is a multiple of 100 (ATMs typically only dispense 100s)
   Display appropriate messages for each condition.
