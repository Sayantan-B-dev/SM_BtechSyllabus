# Decision Making (If, If-Else, Nested If-Else)

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 7  
**Date:** 22-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

### 1. Chained Comparisons

Python allows you to chain comparison operators together, creating concise and readable conditions.

**Syntax:**

```python
a < b < c    # Equivalent to: a < b and b < c
```

Python evaluates chained comparisons efficiently using short-circuit evaluation.

**Examples:**

```python
x = 15

# Check if x is between 10 and 20 (inclusive)
if 10 <= x <= 20:
    print(f"{x} is between 10 and 20.")
else:
    print(f"{x} is outside the range.")

# Output: 15 is between 10 and 20.
```

```python
# Check if three numbers are in strictly increasing order
a, b, c = 5, 10, 15

if a < b < c:
    print("Increasing order")    # Prints this
elif a > b > c:
    print("Decreasing order")
else:
    print("Neither")

# Chained comparison with different operators
age = 25
if 18 <= age < 60:
    print("Working age adult")   # Prints this
```

**Without chained comparison (more verbose):**

```python
# Instead of:
if x >= 10 and x <= 20:
    print("In range")

# Write:
if 10 <= x <= 20:
    print("In range")
```

**All comparison operators can be chained:**

```python
# Check if all three values are equal
if x == y == z:
    print("All equal")

# Mixed operators
if a < b != c:  # a < b AND b != c (but no relation between a and c)
    print("Condition met")
```

---

### 2. The `match-case` Statement (Python 3.10+)

Introduced in Python 3.10, `match-case` provides a powerful pattern matching mechanism, similar to `switch-case` in other languages but much more flexible.

**Basic Syntax:**

```python
match value:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case _:
        # default case (underscore matches anything)
```

**Example 1: Simple value matching**

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
```

**Output:**

```
Wednesday
```

**Example 2: Matching with OR condition (using `|`)**

```python
day = "saturday"

match day.lower():
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
```

**Output:**

```
Weekend
```

**Example 3: Matching with conditions (guards)**

```python
num = 15

match num:
    case n if n > 0:
        print(f"{n} is positive")
    case n if n < 0:
        print(f"{n} is negative")
    case 0:
        print("Zero")
```

**Output:**

```
15 is positive
```

**Example 4: Matching data structures**

```python
point = (3, 4)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On y-axis at y={y}")
    case (x, 0):
        print(f"On x-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
        print("Not a point")
```

**Output:**

```
Point at (3, 4)
```

**Comparison: if-elif-else vs match-case:**

```python
# Using if-elif-else
status_code = 404

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code == 500:
    print("Server Error")
else:
    print("Unknown")

# Using match-case
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")
```

**When to use match-case:**
- When you have many discrete cases
- When matching against patterns (not just values)
- When pattern destructuring would be helpful

**When to use if-elif-else:**
- For simple conditions (True/False)
- When conditions involve comparisons (>, <, >=)
- When you need complex boolean logic (and, or, not)

---

### 3. Short-Circuit Evaluation

Python uses **short-circuit evaluation** for `and` and `or` operators. This means the second operand is evaluated only when necessary.

**AND short-circuit:**
- If the first operand is `False`, Python knows the result must be `False`, so it does NOT evaluate the second operand.

```python
def get_value():
    print("get_value() called")
    return 10

# Short-circuit: first operand is False, so get_value() is never called
if False and get_value() > 5:
    print("This won't print")

# No output from get_value() because it was never called
```

**OR short-circuit:**
- If the first operand is `True`, Python knows the result must be `True`, so it does NOT evaluate the second operand.

```python
def get_value():
    print("get_value() called")
    return 10

# Short-circuit: first operand is True, so get_value() is never called
if True or get_value() > 5:
    print("This will print")

# Output:
# This will print
# Notice: get_value() was never called
```

**Practical uses of short-circuit evaluation:**

1. **Avoiding errors (guard pattern):**

```python
# Avoid ZeroDivisionError by checking first
b = 0
if b != 0 and 10 / b > 2:
    print("Result > 2")
else:
    print("Can't divide or result <= 2")
# Output: Can't divide or result <= 2
# b != 0 is False, so 10 / b is never evaluated (no error)
```

2. **Providing default values:**

```python
# Use or to provide a default
name = input("Enter name: ") or "Guest"
print(f"Hello, {name}!")
# If user enters nothing, name becomes "Guest"
```

3. **Checking if an attribute exists before using it:**

```python
# Check if an object has an attribute before accessing it
if hasattr(obj, "name") and obj.name:
    print(f"Name is {obj.name}")
```

---

### 4. Common Errors and Best Practices

#### 4.1 Dangling else (not a problem in Python)

Unlike C/Java, Python's indentation-based structure prevents the dangling-else ambiguity:

```python
# Python -- clear which else belongs to which if
if x > 0:
    if x > 10:
        print("x > 10")
else:
    print("x <= 0")  # Belongs to the outer if
```

#### 4.2 Comparing with None

Always use `is` or `is not` to compare with `None`, not `==` or `!=`:

```python
# Correct
if result is None:
    print("No result")

# Also correct
if result is not None:
    print(f"Result is {result}")

# Avoid
if result == None:  # Works but not idiomatic
    print("No result")
```

#### 4.3 Truthiness Pitfalls

```python
# Checking if a list is empty
my_list = []

# Good
if not my_list:
    print("List is empty")

# Avoid
if my_list == []:
    print("List is empty")
```

```python
# Checking if a string is not empty
name = ""

# Good
if name:
    print(f"Hello, {name}")

# Avoid
if len(name) > 0:
    print(f"Hello, {name}")
```

#### 4.4 Avoiding Deep Nesting

Deeply nested code is hard to read. Use logical operators or early returns to flatten:

```python
# Hard to read (3 levels of nesting)
if user.is_active:
    if user.has_permission:
        if user.is_verified:
            print("Access granted")
        else:
            print("Verify your account")
    else:
        print("No permission")
else:
    print("Account inactive")

# Better -- combine conditions
if user.is_active and user.has_permission and user.is_verified:
    print("Access granted")
elif not user.is_active:
    print("Account inactive")
elif not user.has_permission:
    print("No permission")
else:
    print("Verify your account")
```

#### 4.5 Using `elif` vs Multiple `if` Statements

```python
# Using elif -- only ONE block executes
x = 5

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
# Only "Positive" prints

# Using multiple if statements -- ALL matching blocks execute
if x > 0:
    print("Positive")      # This prints
if x < 5:
    print("Less than 5")   # This also prints
if x == 5:
    print("Exactly 5")     # This also prints
```

---

### 5. Truthy and Falsy Values Recap

Values that Python considers `False` in boolean contexts:

```python
# These are ALL falsy:
False
None
0
0.0
0j        # complex zero
""        # empty string
[]        # empty list
()        # empty tuple
{}        # empty dict
set()     # empty set
range(0)  # empty range
```

Everything else is `True`.

```python
# Useful trick: check if a collection is non-empty
items = [1, 2, 3]

if items:  # Instead of: if len(items) > 0:
    print(f"Has {len(items)} items")
```

---

### 6. Practice Problems with Full Solutions

#### Problem 1: Find the maximum of three numbers

Write a program that takes three numbers as input and prints the maximum. Handle the case where two or more are equal.

**Solution:**

```python
# Solution: Maximum of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    if a == b == c:
        print(f"All three numbers are equal to {a}")
    elif a == b:
        print(f"Maximum is {a} (a and b are tied)")
    elif a == c:
        print(f"Maximum is {a} (a and c are tied)")
    else:
        print(f"Maximum is {a}")
elif b >= a and b >= c:
    if b == c:
        print(f"Maximum is {b} (b and c are tied)")
    else:
        print(f"Maximum is {b}")
else:
    print(f"Maximum is {c}")
```

#### Problem 2: ATM Menu System

Write a program that displays a simple ATM menu and processes the user's choice using match-case. Options: 1. Check Balance, 2. Deposit, 3. Withdraw, 4. Exit.

**Solution:**

```python
# Solution: ATM Menu System

balance = 1000.0

print("=== ATM Menu ===")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print(f"Your current balance is Rs.{balance:.2f}")
    case 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{balance:.2f}")
        else:
            print("Invalid deposit amount.")
    case 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount % 100 != 0:
            print("Withdrawal amount must be a multiple of 100.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrew Rs.{amount:.2f}. Remaining balance: Rs.{balance:.2f}")
    case 4:
        print("Thank you for using our ATM. Goodbye!")
    case _:
        print("Invalid choice. Please select 1-4.")
```

#### Problem 3: Character Type Classifier

Write a program that reads a single character and classifies it as:
- Uppercase letter
- Lowercase letter
- Digit
- Special character

**Solution:**

```python
# Solution: Character Type Classifier

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if 'A' <= ch <= 'Z':
        print(f"'{ch}' is an uppercase letter.")
    elif 'a' <= ch <= 'z':
        print(f"'{ch}' is a lowercase letter.")
    elif '0' <= ch <= '9':
        print(f"'{ch}' is a digit.")
    else:
        print(f"'{ch}' is a special character.")
```

#### Problem 4: Discount Calculator

A store offers discounts based on the purchase amount:
- Rs. 0 - 1000: No discount
- Rs. 1001 - 5000: 5% discount
- Rs. 5001 - 10000: 10% discount
- Above Rs. 10000: 15% discount
Additionally, if the customer has a membership card, add 5% extra discount.

**Solution:**

```python
# Solution: Discount Calculator

amount = float(input("Enter purchase amount (Rs.): "))
has_membership = input("Do you have a membership card? (yes/no): ").lower() == "yes"

if amount <= 0:
    print("Invalid amount.")
else:
    # Determine base discount
    if amount <= 1000:
        discount_rate = 0
    elif amount <= 5000:
        discount_rate = 5
    elif amount <= 10000:
        discount_rate = 10
    else:
        discount_rate = 15

    # Add membership bonus
    if has_membership:
        discount_rate += 5

    # Calculate
    discount_amount = amount * discount_rate / 100
    final_amount = amount - discount_amount

    print(f"Original amount: Rs.{amount:.2f}")
    print(f"Discount rate: {discount_rate}%")
    print(f"Discount amount: Rs.{discount_amount:.2f}")
    print(f"Final amount: Rs.{final_amount:.2f}")
```

#### Problem 5: Simple Calculator with Operator

Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation. Handle division by zero and invalid operators.

**Solution:**

```python
# Solution: Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            result = None
        else:
            result = num1 / num2
    case _:
        print(f"Error: '{operator}' is not a valid operator.")
        result = None

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
```

---

## Practice Problems

1. **Number Range:** Write a program that takes a number and prints:
   - "Less than 10" if x < 10
   - "Between 10 and 20" if 10 <= x <= 20
   - "Greater than 20" if x > 20
   Use chained comparisons where appropriate.
   <details>
   <summary>Show Answer</summary>
   ```python
   x = float(input("Enter a number: "))
   if x < 10:
       print("Less than 10")
   elif 10 <= x <= 20:
       print("Between 10 and 20")
   else:
       print("Greater than 20")
   ```
   </details>

2. **Season Finder:** Write a program that takes a month name (e.g., "January") and prints the season:
   - Spring: March, April, May
   - Summer: June, July, August
   - Autumn: September, October, November
   - Winter: December, January, February
   Use match-case with the OR pattern (`|`).
   <details>
   <summary>Show Answer</summary>
   ```python
   month = input("Enter month: ").capitalize()
   match month:
       case "March" | "April" | "May":
           print("Spring")
       case "June" | "July" | "August":
           print("Summer")
       case "September" | "October" | "November":
           print("Autumn")
       case "December" | "January" | "February":
           print("Winter")
       case _:
           print("Invalid month")
   ```
   </details>

3. **Short-Circuit Investigation:** Write a program that demonstrates short-circuit evaluation. Define a function `check()` that prints "checked" and returns True. Use it with `and` and `or` operators to show when it is and is not called.
   <details>
   <summary>Show Answer</summary>
   ```python
   def check():
       print("checked")
       return True
   
   print("Using and:")
   result = False and check()  # check() is NOT called (short-circuit)
   print("Using or:")
   result = True or check()    # check() is NOT called (short-circuit)
   print("Using or with False:")
   result = False or check()   # check() IS called
   ```
   Output: `and` and `or` short-circuit when the left operand already determines the result.
   </details>

4. **Tax Calculator:** Write a program to calculate income tax:
   - Income up to Rs. 2,50,000: No tax
   - Rs. 2,50,001 to Rs. 5,00,000: 5%
   - Rs. 5,00,001 to Rs. 10,00,000: 20%
   - Above Rs. 10,00,000: 30%
   Show the tax amount and the income after tax.
   <details>
   <summary>Show Answer</summary>
   ```python
   income = float(input("Enter your income: "))
   if income <= 250000:
       tax = 0
   elif income <= 500000:
       tax = (income - 250000) * 0.05
   elif income <= 1000000:
       tax = 250000 * 0.05 + (income - 500000) * 0.20
   else:
       tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
   print(f"Tax: Rs. {tax:.2f}")
   print(f"Income after tax: Rs. {income - tax:.2f}")
   ```
   </details>

5. **Rock-Paper-Scissors:** Write a simple two-player Rock-Paper-Scissors game. Take input from two players, determine the winner, and display the result. Handle invalid inputs.
   <details>
   <summary>Show Answer</summary>
   ```python
   p1 = input("Player 1 (rock/paper/scissors): ").lower()
   p2 = input("Player 2 (rock/paper/scissors): ").lower()
   valid = {"rock", "paper", "scissors"}
   if p1 not in valid or p2 not in valid:
       print("Invalid input! Use rock, paper, or scissors.")
   elif p1 == p2:
       print("It's a tie!")
   elif (p1 == "rock" and p2 == "scissors") or \
        (p1 == "scissors" and p2 == "paper") or \
        (p1 == "paper" and p2 == "rock"):
       print("Player 1 wins!")
   else:
       print("Player 2 wins!")
   ```
   </details>
