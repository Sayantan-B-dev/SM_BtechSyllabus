# List Operations, Methods, and Comprehension

**Course:** Python Programming Lab  
**Module:** 3 | **Lecture:** 3  
**Date:** 28-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Create and manipulate nested lists (lists within lists).
- Implement matrix addition and transpose operations.
- Flatten a nested list into a single-level list.

## Theory

A nested list is a list that contains other lists as its elements. Nested lists represent 2D data structures like matrices, tables, or grids. Accessing elements uses multiple indices: matrix[row][col]. The outer index selects the row, the inner index selects the column within that row.

Matrix addition requires two matrices of the same dimensions. Corresponding elements are added: result[i][j] = A[i][j] + B[i][j]. The transpose of a matrix swaps rows and columns: result[j][i] = matrix[i][j]. For an m x n matrix, the transpose is n x m.

Flattening a nested list converts it into a one-dimensional list containing all elements in order. This can be done with nested loops or using list comprehension with two for clauses: `[item for row in nested for item in row]`. The outer for iterates over rows, the inner for iterates over elements in each row.

## Procedure

1. Create a new Python file named lab15.py.
2. Create a 3x3 nested list (matrix) and print it in matrix form.
3. Access and modify individual elements using double indexing.
4. Write a function to add two matrices of the same dimensions.
5. Write a function to transpose a matrix.
6. Write a program to flatten a nested list.
7. Test all functions with sample data.

## Source Code

```python
# Module 03 Lab 03: Nested Lists and Matrix Operations

# Creating a nested list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nElement at [1][2]: {matrix[1][2]}")  # 6
print(f"Element at [0][0]: {matrix[0][0]}")  # 1

# Modify element
matrix[2][1] = 100
print(f"After modifying [2][1] to 100:")
for row in matrix:
    print(row)

# Matrix Addition
print("\n--- Matrix Addition ---")
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

rows = len(A)
cols = len(A[0])
result = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix A:")
for row in A:
    print(row)
print("Matrix B:")
for row in B:
    print(row)
print("A + B:")
for row in result:
    print(row)

# Matrix Transpose
print("\n--- Matrix Transpose ---")
C = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [[C[j][i] for j in range(len(C))] for i in range(len(C[0]))]

print("Original:")
for row in C:
    print(row)
print("Transpose:")
for row in transpose:
    print(row)

# Flatten a nested list
print("\n--- Flatten Nested List ---")
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flat}")

# Flatten with nested loops (equivalent)
flat_loop = []
for sublist in nested:
    for item in sublist:
        flat_loop.append(item)
print(f"Flattened (loops): {flat_loop}")
```

## Sample Output

```
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Element at [1][2]: 6
Element at [0][0]: 1
After modifying [2][1] to 100:
[1, 2, 3]
[4, 5, 6]
[7, 100, 9]

--- Matrix Addition ---
Matrix A:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
Matrix B:
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]
A + B:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]

--- Matrix Transpose ---
Original:
[1, 2, 3]
[4, 5, 6]
Transpose:
[1, 4]
[2, 5]
[3, 6]

--- Flatten Nested List ---
Nested: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Flattened (loops): [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Homework

1. Write a program to multiply two matrices (3x3) using nested loops.
2. Write a program that takes a nested list and returns the sum of all elements (use nested loops or sum() with comprehension).
3. Write a program to print the diagonal elements (top-left to bottom-right) of a square matrix.
