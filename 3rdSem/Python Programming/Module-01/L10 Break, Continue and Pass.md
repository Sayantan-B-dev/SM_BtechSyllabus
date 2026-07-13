# Break, Continue and Pass

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 10  
**Date:** 27-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

`break`, `continue`, and `pass` are three control statements that affect the flow of loops and code execution. Each serves a distinct purpose.

---

### 1. The `break` Statement

`break` immediately terminates the innermost loop. Execution resumes at the first statement after the loop body.

**Effect on different loop types:**
- In a `for` loop: exits the loop entirely.
- In a `while` loop: exits the loop entirely.
- In nested loops: exits only the innermost loop where it appears.

**Syntax:**

```python
for variable in sequence:
    if condition:
        break
    # code here runs until break is triggered
# code here runs after break (or after loop ends naturally)
```

#### Example 1: Search for an element

```python
# Find the first occurrence of 7 in a list
numbers = [3, 5, 2, 7, 9, 7, 1]

for i, num in enumerate(numbers):
    if num == 7:
        print(f"Found 7 at index {i}")
        break
else:
    print("7 not found in the list")
```

**Output:**

```
Found 7 at index 3
```

Without `break`, the loop would continue to check `9`, `7`, `1` unnecessarily.

#### Example 2: Prime number checker (using break)

```python
# Check if a number is prime
num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not prime.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            print(f"{num} is divisible by {i}. Not prime.")
            break

    if is_prime:
        print(f"{num} is prime!")
```

**Run 1:**

```
Enter a number: 29
29 is prime!
```

**Run 2:**

```
Enter a number: 35
35 is divisible by 5. Not prime.
```

**Explanation:** Once we find a divisor, we know the number is not prime. There is no need to check further divisors, so we `break` out of the loop. This optimization reduces the number of iterations significantly for large numbers.

#### Example 3: Input validation with break

```python
# Keep asking until user enters a valid number
while True:
    user_input = input("Enter a positive number (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if user_input.isdigit() and int(user_input) > 0:
        num = int(user_input)
        print(f"You entered {num}. Square is {num ** 2}.")
        break
    else:
        print("Invalid input. Try again.")
```

**Run:**

```
Enter a positive number (or 'quit' to exit): -5
Invalid input. Try again.
Enter a positive number (or 'quit' to exit): abc
Invalid input. Try again.
Enter a positive number (or 'quit' to exit): 12
You entered 12. Square is 144.
```

---

### 2. The `continue` Statement

`continue` skips the rest of the current iteration and moves to the next iteration of the loop.

- In a `for` loop: goes to the next item in the sequence.
- In a `while` loop: goes back to check the condition again.

**Syntax:**

```python
for variable in sequence:
    if condition:
        continue
    # code here runs only if continue was NOT triggered
```

#### Example 1: Skip even numbers, process odd numbers

```python
# Process only odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"{i} is odd")
```

**Output:**

```
1 is odd
3 is odd
5 is odd
7 is odd
9 is odd
```

#### Example 2: Skip invalid data in a list

```python
# Calculate average of only valid positive numbers
data = [10, -5, 25, -8, 15, 0, 30, "invalid", 20]

total = 0
count = 0

for value in data:
    # Skip non-numeric values
    if not isinstance(value, (int, float)):
        print(f"Skipping non-numeric: {value}")
        continue

    # Skip non-positive numbers
    if value <= 0:
        print(f"Skipping non-positive: {value}")
        continue

    total += value
    count += 1

if count > 0:
    print(f"Average of {count} valid numbers: {total / count:.2f}")
else:
    print("No valid numbers to average.")
```

**Output:**

```
Skipping non-positive: -5
Skipping non-positive: -8
Skipping non-positive: 0
Skipping non-numeric: invalid
Average of 4 valid numbers: 20.00
```

#### Example 3: Continue in a while loop

```python
# Print the first 10 positive multiples of 3
i = 0
count = 0

while count < 10:
    i += 1
    if i % 3 != 0:
        continue  # Not a multiple of 3, skip
    print(f"{i} is a multiple of 3")
    count += 1
```

**Output:**

```
3 is a multiple of 3
6 is a multiple of 3
9 is a multiple of 3
12 is a multiple of 3
15 is a multiple of 3
18 is a multiple of 3
21 is a multiple of 3
24 is a multiple of 3
27 is a multiple of 3
30 is a multiple of 3
```

**Important note about `continue` in `while` loops:** If the loop variable update is placed after `continue`, it may cause an infinite loop.

```python
# WRONG -- infinite loop
i = 0
while i < 10:
    if i % 2 == 0:
        continue  # Skips i += 1 below, so i never changes
    print(i)
    i += 1  # This line is skipped when continue runs

# CORRECT -- update before continue
i = 0
while i < 10:
    i += 1  # Update first
    if i % 2 == 0:
        continue
    print(i)
```

---

### 3. The `pass` Statement

`pass` is a **null operation** -- it does nothing. It is used as a placeholder where Python syntax requires a statement but you do not want to execute any code.

**Syntax:**

```python
if condition:
    pass  # Do nothing
```

#### Example 1: Placeholder for future code

```python
# I will implement this function later
def calculate_tax(income):
    pass  # TODO: implement tax calculation

# The function exists but does nothing yet
# Without pass, an empty function would cause IndentationError
```

#### Example 2: Placeholder in a class

```python
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass  # Will implement later

    def display_details(self):
        pass  # Will implement later
```

#### Example 3: Placeholder in a loop

```python
# Ignore all even numbers (just a placeholder for future logic)
for i in range(1, 11):
    if i % 2 == 0:
        pass  # Placeholder -- will add logic later
    else:
        print(f"{i} is odd")
```

**Output:**

```
1 is odd
3 is odd
5 is odd
7 is odd
9 is odd
```

(Note: using `continue` would be more appropriate here if the intent is to skip evens. `pass` is only a placeholder.)

#### Example 4: Minimal class with pass

```python
# An empty class -- pass makes it syntactically valid
class PlaceholderConfig:
    pass

# We can still create instances
config = PlaceholderConfig()
print(type(config))  # <class '__main__.PlaceholderConfig'>
```

---

### 4. Difference Between break, continue, and pass

| Statement | What it does | When to use |
|---|---|---|
| `break` | Exits the loop immediately | When you found what you were looking for and want to stop |
| `continue` | Skips the rest of the current iteration, moves to the next | When the current item should be ignored but the loop continues |
| `pass` | Does nothing (placeholder) | When syntax requires a statement but no action needed |

**Visual comparison:**

```python
print("Using break:")
for i in range(1, 6):
    if i == 3:
        break  # Loop ends when i is 3
    print(i, end=" ")  # 1 2

print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3, continue with 4, 5
    print(i, end=" ")  # 1 2 4 5

print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass  # Does nothing, loop continues normally
    print(i, end=" ")  # 1 2 3 4 5
```

**Output:**

```
Using break:
1 2
Using continue:
1 2 4 5
Using pass:
1 2 3 4 5
```

---

### 5. Complete Practical Examples

#### Example 1: Prime Number Checker (Complete)

```python
# Program: Check if a number is prime

num = int(input("Enter a positive integer: "))

if num < 2:
    print(f"{num} is not prime.")
else:
    found_divisor = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            found_divisor = True
            print(f"{num} is not prime. It is divisible by {i}.")
            break

    if not found_divisor:
        print(f"{num} is prime!")

    # Optimization note: checking up to sqrt(num) is sufficient
    # because if num = a * b and both a and b are > sqrt(num),
    # then a * b > num, which is impossible.
```

**Run:**

```
Enter a positive integer: 97
97 is prime!
```

#### Example 2: Print numbers skipping multiples of 3

```python
# Program: Print numbers from 1 to 20, skipping multiples of 3

print("Numbers from 1 to 20 (skipping multiples of 3):")

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")

print()
```

**Output:**

```
Numbers from 1 to 20 (skipping multiples of 3):
1 2 4 5 7 8 10 11 13 14 16 17 19 20
```

#### Example 3: Menu-driven program skeleton

```python
# Program: Skeleton for a menu-driven calculator
# Uses pass as placeholder for unimplemented features

def main():
    while True:
        print("\n=== Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result: {a + b}")
        elif choice == "2":
            print(f"Result: {a - b}")
        elif choice == "3":
            print(f"Result: {a * b}")
        elif choice == "4":
            if b == 0:
                print("Error: Division by zero.")
                continue
            print(f"Result: {a / b}")

if __name__ == "__main__":
    main()
```

**Run (partial):**

```
=== Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

#### Example 4: Find all prime numbers up to N

```python
# Program: Find all prime numbers up to N (using break)

n = int(input("Enter the upper limit: "))

print(f"Prime numbers up to {n}:")

for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break  # Not prime, exit inner loop
    else:
        # This else belongs to the inner for loop
        # It runs only if the loop completed without break
        print(num, end=" ")

print()
```

**Output:**

```
Enter the upper limit: 50
Prime numbers up to 50:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

---

### 6. Common Pitfalls and Best Practices

**Pitfall 1: Forgetting that `break` exits only the innermost loop.**

```python
# This only breaks the inner loop, not the outer one
for i in range(3):
    print(f"Outer: {i}")
    for j in range(5):
        if j == 2:
            break  # Only breaks inner loop
        print(f"  Inner: {j}")
    print("Still in outer loop")
```

**Output:**

```
Outer: 0
  Inner: 0
  Inner: 1
Still in outer loop
Outer: 1
  Inner: 0
  Inner: 1
Still in outer loop
Outer: 2
  Inner: 0
  Inner: 1
Still in outer loop
```

**Pitfall 2: Using `pass` when you meant `continue`.**

`pass` does NOT skip the rest of the iteration. It just does nothing at that point and execution continues.

```python
# The difference between pass and continue
for i in range(1, 6):
    if i == 3:
        pass  # Does nothing -- execution continues
    print(i, end=" ")  # 1 2 3 4 5 -- prints ALL numbers

print()

for i in range(1, 6):
    if i == 3:
        continue  # Skips the rest of this iteration
    print(i, end=" ")  # 1 2 4 5 -- skips 3
```

**Pitfall 3: Infinite loop with `continue` in `while`.**

Always ensure the loop variable is updated BEFORE `continue` in a `while` loop.

**Best Practice: Use `break` to avoid unnecessary computation.**

If you are searching for something and you find it, stop the loop immediately with `break`. Do not keep iterating.

---

## Practice Problems

1. **First Divisor:** Write a program that takes a number N and finds the smallest divisor of N greater than 1. Use `break` to stop once you find the divisor.

2. **Skip Vowels:** Write a program that takes a string and prints it with all vowels (a, e, i, o, u) removed. Use `continue` to skip vowels.

3. **Class Skeleton:** Create a class called `DatabaseConnection` with methods `connect()`, `disconnect()`, and `execute_query()`. Use `pass` for all methods as placeholders for future implementation.

4. **Menu with Break/Continue:** Write a program with a menu that:
   - Option 1: Enter a number and print its square.
   - Option 2: Enter a number and print its cube.
   - Option 3: Exit.
   - If the user enters an invalid option, use `continue` to show the menu again.
   - If the user chooses to exit, use `break` to end the loop.

5. **Password Attempts:** Write a program that gives the user 3 attempts to enter the correct password ("python123"). Use `break` if the password is correct. Use `continue` to prompt again after a wrong attempt (if attempts remain). After 3 failed attempts, print "Account locked."

6. **Sum Until Zero (with break):** Write a program that keeps taking numbers from the user and adding them to a running total. If the user enters 0, break out of the loop and print the total. If the user enters a negative number, use `continue` to skip it (do not add it to the total).
