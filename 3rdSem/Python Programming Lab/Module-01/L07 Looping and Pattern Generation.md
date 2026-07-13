# Looping and Pattern Generation

**Course:** Python Programming Lab  
**Module:** 1 | **Lecture:** 7  
**Date:** 31-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:**   
**Reference:** Lab Manual

## Lab Objectives

- Use nested loops to generate 2D patterns.
- Print right triangle, pyramid, and diamond patterns using stars (*) and numbers.
- Understand how the inner loop controls columns and the outer loop controls rows.

## Theory

Nested loops are loops placed inside other loops. For pattern printing, the outer loop typically controls the number of rows, while the inner loop controls the number of elements printed per row. The range() values for the inner loop may depend on the outer loop's variable to create triangular or symmetrical shapes.

Pattern logic follows these principles:
- Right triangle (star): row i prints i stars.
- Pyramid: row i prints (n - i - 1) spaces followed by (2*i + 1) stars.
- Diamond: the top half is a pyramid, the bottom half is an inverted pyramid.

Number patterns work similarly: instead of printing stars, print the row number, column number, or a calculated value. The print() function's end parameter controls whether output goes to the next line (end=" " keeps on same line). A plain print() without arguments moves to the next line.

## Procedure

1. Create a new Python file named lab07.py.
2. Write a nested loop to print a right triangle of stars (5 rows).
3. Write a nested loop to print a pyramid pattern (5 rows).
4. Write a nested loop to print a diamond pattern (5 rows for top half).
5. Write a number pattern program: right triangle with row numbers.
6. Write a number pattern: Floyd's triangle (consecutive numbers).
7. Test all patterns.

## Source Code

```python
# Lab 07: Pattern Generation using Nested Loops

n = 5

# Pattern 1: Right Triangle (stars)
print("Right Triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Pattern 2: Pyramid (stars)
print("Pyramid:")
for i in range(n):
    # print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    # print stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
print()

# Pattern 3: Diamond (stars)
print("Diamond:")
# Top half (including middle)
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
# Bottom half
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
print()

# Pattern 4: Number Triangle (row numbers)
print("Number Triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
print()

# Pattern 5: Floyd's Triangle
print("Floyd's Triangle:")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

## Sample Output

```
Right Triangle:
*
* *
* * *
* * * *
* * * * *

Pyramid:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

Diamond:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

Number Triangle:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Floyd's Triangle:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

## Homework

1. Print an inverted right triangle pattern (5 rows, decreasing stars).
2. Print a number pyramid where each row contains numbers from 1 to i.
3. Print a hollow square pattern of stars (side length 5) where only the border is filled with stars.
