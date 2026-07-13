# Looping Statements (For, While, Nested Loops)

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 9  
**Date:** 27-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

### 1. Nested Loops

A **nested loop** is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

**Syntax:**

```python
for outer_var in outer_sequence:
    for inner_var in inner_sequence:
        # Code runs (outer * inner) times
        statements
```

**How nested loops work -- trace the execution:**

```python
for i in range(3):       # Outer loop: runs 3 times
    print(f"Outer: i={i}")
    for j in range(2):   # Inner loop: runs 2 times for EACH outer iteration
        print(f"  Inner: j={j}")
    print("---")
```

**Output:**

```
Outer: i=0
  Inner: j=0
  Inner: j=1
---
Outer: i=1
  Inner: j=0
  Inner: j=1
---
Outer: i=2
  Inner: j=0
  Inner: j=1
---
```

The inner loop body executes `outer_count * inner_count` times = `3 * 2 = 6` times.

#### Example 1: Multiplication Table (1 to 5)

```python
# Program: Multiplication tables from 1 to 5

for i in range(1, 6):       # Outer loop: table for numbers 1 to 5
    print(f"Table of {i}:")
    for j in range(1, 11):  # Inner loop: multiply by 1 to 10
        print(f"{i:2d} x {j:2d} = {i*j:3d}")
    print()  # Blank line between tables
```

**Output (partial):**

```
Table of 1:
 1 x  1 =   1
 1 x  2 =   2
 ... (1 x 3 through 1 x 10)
 1 x 10 =  10

Table of 2:
 2 x  1 =   2
 2 x  2 =   4
 ...
```

#### Example 2: Print a Rectangle of Stars

```python
# Program: Print a rectangle of stars

rows = 4
cols = 10

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()  # New line after each row
```

**Output:**

```
**********
**********
**********
**********
```

#### Example 3: Number Pattern

```python
# Program: Print a right-angle triangle pattern

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Output:**

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### 2. The `else` Clause with Loops

Python loops can have an `else` clause. The `else` block executes when the loop completes normally (i.e., it was **not** terminated by a `break` statement).

**Syntax:**

```python
for variable in sequence:
    # loop body
    if condition:
        break
else:
    # executes only if the loop did NOT encounter a break
```

**Example 1: Search for an item (with and without break)**

```python
# Without break -- else always runs
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    print(f"Checking {num}")
else:
    print("Loop completed (no break was used)")
```

**Output:**

```
Checking 1
Checking 3
Checking 5
Checking 7
Checking 9
Loop completed (no break was used)
```

**Example 2: Search with break -- else does NOT run**

```python
# With break -- else does NOT run
numbers = [1, 3, 5, 7, 9]
target = 5

for num in numbers:
    print(f"Checking {num}")
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")
```

**Output:**

```
Checking 1
Checking 3
Checking 5
Found 5!
```

**Example 3: Prime number checker using for-else**

```python
# Program: Check if a number is prime using for-else

num = int(input("Enter a positive integer: "))

if num < 2:
    print(f"{num} is not prime.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime. Divisible by {i}.")
            break
    else:
        print(f"{num} is prime!")
```

**Run 1:**

```
Enter a positive integer: 17
17 is prime!
```

**Run 2:**

```
Enter a positive integer: 21
21 is not prime. Divisible by 3.
```

**Without for-else, you would need a flag variable:**

```python
# Traditional approach (without for-else)
is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is prime!")
else:
    print(f"{num} is not prime.")
```

---

### 3. The `enumerate()` Function

`enumerate()` adds a counter to an iterable. It returns pairs of `(index, value)`.

**Syntax:**

```python
for index, value in enumerate(iterable, start=0):
    statements
```

**Example 1: Basic enumeration**

```python
fruits = ["apple", "banana", "cherry", "date"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**Output:**

```
0: apple
1: banana
2: cherry
3: date
```

**Example 2: Using `start` parameter**

```python
# Start counting from 1 (more intuitive for humans)
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Output:**

```
1. apple
2. banana
3. cherry
4. date
```

**Example 3: Practical use -- finding positions of a substring**

```python
# Find all positions of 'l' in a string
text = "hello world"
for i, char in enumerate(text):
    if char == 'l':
        print(f"Found 'l' at position {i}")
```

**Output:**

```
Found 'l' at position 2
Found 'l' at position 3
Found 'l' at position 9
```

---

### 4. The `zip()` Function

`zip()` combines multiple iterables element-wise into tuples. It stops when the shortest iterable is exhausted.

**Syntax:**

```python
for item1, item2, ... in zip(iterable1, iterable2, ...):
    statements
```

**Example 1: Parallel iteration**

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Output:**

```
Alice: 85
Bob: 92
Charlie: 78
```

**Example 2: Three iterables**

```python
subjects = ["Math", "Physics", "Chemistry"]
marks = [90, 85, 88]
grades = ["A", "B+", "A"]

for sub, mark, grade in zip(subjects, marks, grades):
    print(f"{sub}: {mark} ({grade})")
```

**Output:**

```
Math: 90 (A)
Physics: 85 (B+)
Chemistry: 88 (A)
```

**Example 3: zip stops at the shortest iterable**

```python
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

for a, b in zip(list1, list2):
    print(a, b)
```

**Output:**

```
1 a
2 b
3 c
```

Note: `4` and `5` are ignored because `list2` only has 3 elements.

**Example 4: Unzipping with zip**

```python
# zip can also unzip using the * operator
pairs = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
names, scores = zip(*pairs)

print(names)   # ('Alice', 'Bob', 'Charlie')
print(scores)  # (85, 92, 78)
```

---

### 5. Practical Examples

#### Example 1: Pyramid Pattern

```python
# Program: Print a pyramid of stars

n = 5

for i in range(1, n + 1):
    # Print spaces (left side)
    for s in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()  # New line
```

**Output:**

```
    *
   ***
  *****
 *******
*********
```

#### Example 2: Diamond Pattern

```python
# Program: Print a diamond pattern

n = 5

# Upper half (including middle)
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

**Output:**

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

#### Example 3: Multiplication Table (Full Grid)

```python
# Program: Print a formatted multiplication table (1 to 10)

print("Multiplication Table")
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4d}", end="")
print()
print("    " + "----" * 10)

for i in range(1, 11):
    print(f"{i:2d} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()
```

**Output:**

```
Multiplication Table
        1   2   3   4   5   6   7   8   9  10
    --------------------------------------------
 1 |   1   2   3   4   5   6   7   8   9  10
 2 |   2   4   6   8  10  12  14  16  18  20
 3 |   3   6   9  12  15  18  21  24  27  30
 4 |   4   8  12  16  20  24  28  32  36  40
 5 |   5  10  15  20  25  30  35  40  45  50
 6 |   6  12  18  24  30  36  42  48  54  60
 7 |   7  14  21  28  35  42  49  56  63  70
 8 |   8  16  24  32  40  48  56  64  72  80
 9 |   9  18  27  36  45  54  63  72  81  90
10 |  10  20  30  40  50  60  70  80  90 100
```

#### Example 4: Student Report Card System

```python
# Program: Student report card (using enumerate and zip)

students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]

# Store marks in a 2D structure
marks = [
    [85, 90, 78],  # Alice
    [92, 88, 84],  # Bob
    [70, 75, 80]   # Charlie
]

print("=== Report Card ===")
print(f"{'Student':<10}", end="")
for subject in subjects:
    print(f"{subject:<10}", end="")
print(f"{'Average':<10}")

for i, student in enumerate(students):
    print(f"{student:<10}", end="")
    total = 0
    for mark in marks[i]:
        print(f"{mark:<10}", end="")
        total += mark
    avg = total / len(subjects)
    print(f"{avg:<10.2f}")

print()

# Find subject toppers
for sub_idx, subject in enumerate(subjects):
    max_mark = 0
    topper = ""
    for stu_idx, student in enumerate(students):
        if marks[stu_idx][sub_idx] > max_mark:
            max_mark = marks[stu_idx][sub_idx]
            topper = student
    print(f"{subject} Topper: {topper} ({max_mark})")
```

**Output:**

```
=== Report Card ===
Student   Math      Science   English   Average
Alice     85        90        78        84.33
Bob       92        88        84        88.00
Charlie   70        75        80        75.00

Math Topper: Bob (92)
Science Topper: Alice (90)
English Topper: Bob (84)
```

---

### 6. Loop Performance: Nested Loop Executions

Understanding how many times code in nested loops executes:

```python
# How many times does "Hello" print?
count = 0
for i in range(3):
    for j in range(4):
        print("Hello", end=" ")
        count += 1
print(f"\nTotal: {count} times")

# Output: Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello
# Total: 12 times (3 * 4 = 12)
```

**Common patterns:**

| Outer | Inner | Total Executions |
|---|---|---|
| `range(m)` | `range(n)` | `m * n` |
| `range(n)` | `range(i)` | `n(n+1)/2` |
| `range(n)` | `range(n-i)` | `n(n+1)/2` |

---

## Practice Problems

1. **Pattern: Inverted Triangle:** Write a program to print the following pattern for n = 5:
   ```
   *****
    ****
     ***
      **
       *
   ```

2. **Student Marks Analysis:** Given two lists `names = ["Ram", "Shyam", "Hari"]` and `marks = [[80, 85, 90], [70, 65, 75], [95, 92, 88]]` (3 subjects each), use `enumerate()` and `zip()` to print each student's name, their marks, total, and percentage.

3. **Prime Numbers in Range:** Write a program that prints all prime numbers between 2 and 100. Use the `for-else` pattern for prime checking.

4. **Pattern: Number Pyramid:** Write a program to print:
   ```
       1
      121
     12321
    1234321
   123454321
   ```

5. **Matrix Addition:** Write a program to add two 3x3 matrices. Use nested loops to iterate through rows and columns. Display all three matrices (A, B, A+B).

6. **FizzBuzz with Loop:** Write a program that prints numbers 1 to 100, but:
   - For multiples of 3, print "Fizz" instead of the number.
   - For multiples of 5, print "Buzz" instead.
   - For multiples of both 3 and 5, print "FizzBuzz".
