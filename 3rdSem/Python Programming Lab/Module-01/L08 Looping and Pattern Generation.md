# Looping and Pattern Generation

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 8  
**Date:** 31-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Use break to exit loops prematurely.
- Use continue to skip the current iteration.
- Use pass as a placeholder in loops and conditionals.
- Use the else clause with loops (executes when no break occurs).

## Theory

Loop control statements alter the normal flow of loop execution. The break statement immediately terminates the loop and transfers control to the statement after the loop. It is useful for searching: once an element is found, there is no need to continue iterating.

The continue statement skips the rest of the current iteration and moves to the next iteration. It is used to skip unwanted values without exiting the loop entirely. The pass statement does nothing; it serves as a syntactic placeholder where a statement is required but no action is needed.

The else clause on a for or while loop executes only if the loop completes normally (i.e., was not terminated by a break). This is a unique Python feature. It is commonly used in search loops: if the loop finishes without finding a target, the else block indicates the item was not found. Prime number checking is a classic example: if no divisor is found (no break), the else block confirms the number is prime.

## Procedure

1. Create a new Python file named lab08.py.
2. Write a prime number checker using a for loop with break and else.
3. Write a program that prints numbers from 1 to 20 but skips multiples of 3 using continue.
4. Write a program that finds the first number divisible by both 7 and 5 in a given range using break.
5. Demonstrate pass inside an empty loop body.
6. Test all programs.

## Source Code

```python
# Lab 08: break, continue, pass, and loop else

# Program 1: Prime Number Checker using for-else
num = int(input("Enter a positive integer: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is divisible by {i}.")
            is_prime = False
            break
    else:
        # This else runs only if no break occurred
        print("No divisors found.")

if is_prime:
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")

print()

# Program 2: Skip multiples of 3 using continue
print("Numbers 1 to 20 skipping multiples of 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
print()

# Program 3: Find first number divisible by both 7 and 5
print("First number divisible by both 7 and 5 in 1-200:")
for i in range(1, 201):
    if i % 7 == 0 and i % 5 == 0:
        print(f"Found: {i}")
        break
else:
    print("Not found in range.")
print()

# Program 4: Using pass (placeholder)
print("Even numbers:")
for i in range(1, 11):
    if i % 2 != 0:
        pass  # placeholder, do nothing for odd
    else:
        print(i, end=" ")
print()
```

## Sample Output

```
Enter a positive integer: 29
No divisors found.
29 is a Prime Number.

Numbers 1 to 20 skipping multiples of 3:
1 2 4 5 7 8 10 11 13 14 16 17 19 20

First number divisible by both 7 and 5 in 1-200:
Found: 35

Even numbers:
2 4 6 8 10
```

## Homework

1. Write a program that accepts numbers from the user until they enter -1. Use break to stop. Print the sum of all entered numbers (excluding -1).
2. Write a program that prints all numbers from 1 to 50 except those divisible by both 4 and 6 (use continue).
3. Write a program to check if a given string contains any digit. Use a for loop with break and else. Print "Contains digit" or "No digits found".
