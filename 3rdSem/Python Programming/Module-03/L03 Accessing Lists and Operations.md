# Accessing Lists and Operations

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 3  
**Date:** 17-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Nested List Indexing

Nested lists are lists within lists. To access elements, chain the index operators.

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access an entire row
print(matrix[0])  # [1, 2, 3]
print(matrix[1])  # [4, 5, 6]

# Access a specific element: matrix[row][col]
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
print(matrix[2][1])  # 8

# Modify an element in a nested list
matrix[1][1] = 99
print(matrix)
# [[1, 2, 3], [4, 99, 6], [7, 8, 9]]
```

### Deeper Nesting

```python
# 3D list (list of matrices)
data = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(data[0])       # [[1, 2], [3, 4]]
print(data[0][1])    # [3, 4]
print(data[0][1][0]) # 3
```

## List Comprehension Basics

List comprehension provides a concise way to create lists. The basic syntax is:

```python
[expression for item in iterable]
```

```python
# Traditional for loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Same thing with list comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

### With Conditional Filtering

```python
# Traditional approach
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)  # [0, 2, 4, 6, 8]

# List comprehension with if
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Transform and filter together
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

## The `enumerate()` Function

`enumerate()` returns both the index and the value when iterating over a list.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry

# You can specify a starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. cherry
```

## List Aliasing and Copying

### Aliasing (Reference Copy)

When you assign a list to a new variable, both variables refer to the same list object in memory. Changes through one variable affect the other.

```python
original = [1, 2, 3]
alias = original  # alias points to the SAME list

alias[0] = 99
print(original)  # [99, 2, 3]  -- original changed too!
print(alias)     # [99, 2, 3]

# Check if they are the same object
print(original is alias)  # True
```

### Shallow Copy with `copy()`

A shallow copy creates a new list object, but the elements inside are still references to the same objects. For simple lists (no nested lists), this is usually sufficient.

```python
original = [1, 2, 3]
shallow = original.copy()  # or original[:]

shallow[0] = 99
print(original)  # [1, 2, 3]  -- unchanged
print(shallow)   # [99, 2, 3]

print(original is shallow)  # False (different objects)
```

### Shallow Copy with Nested Lists -- The Problem

A shallow copy only copies the outer list. Nested lists are still shared.

```python
original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]]  -- changed!
print(shallow)   # [[99, 2], [3, 4]]

# The inner lists are the same objects
print(original[0] is shallow[0])  # True
```

### Deep Copy with `copy.deepcopy()`

A deep copy creates an entirely independent copy, including all nested objects. You must import the `copy` module.

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]]  -- unchanged
print(deep)      # [[99, 2], [3, 4]]

print(original[0] is deep[0])  # False (completely independent)
```

### Comparison of Copy Methods

| Method | Syntax | Copies nested objects? | Use case |
|--------|--------|----------------------|----------|
| Alias | `b = a` | No (same object) | When you want two names for one list |
| Shallow copy | `b = a.copy()` or `b = a[:]` | No | Simple lists without nesting |
| Deep copy | `b = copy.deepcopy(a)` | Yes | Nested lists that must be independent |

---

## Practice Problems

**Problem 1:** Given `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, write code to:
- Print the second row
- Print the element in row 3, column 2 (value 8)
- Change the element at row 1, column 1 to 50

<details>
<summary>Show Answer</summary>

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])      # [4, 5, 6]
print(matrix[2][1])   # 8
matrix[0][0] = 50
print(matrix)         # [[50, 2, 3], [4, 5, 6], [7, 8, 9]]
```
</details>

**Problem 2:** Use a list comprehension to create a list of cubes of numbers from 1 to 10.

<details>
<summary>Show Answer</summary>

```python
cubes = [x ** 3 for x in range(1, 11)]
print(cubes)  # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
</details>

**Problem 3:** Use `enumerate()` to print the index and value of each element in `colors = ["red", "green", "blue"]` starting from index 1.

<details>
<summary>Show Answer</summary>

```python
colors = ["red", "green", "blue"]
for i, color in enumerate(colors, start=1):
    print(f"{i}: {color}")

# Output:
# 1: red
# 2: green
# 3: blue
```
</details>

**Problem 4:** Demonstrate the difference between shallow copy and deep copy using a nested list `[[1, 2], [3, 4]]`. Show that modifying a nested element in the shallow copy affects the original, but modifying it in the deep copy does not.

<details>
<summary>Show Answer</summary>

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy
shallow = original.copy()
shallow[0][0] = 99
print("Original after shallow edit:", original)  # [[99, 2], [3, 4]]

# Reset original
original = [[1, 2], [3, 4]]

# Deep copy
deep = copy.deepcopy(original)
deep[0][0] = 99
print("Original after deep edit:", original)  # [[1, 2], [3, 4]]
print("Deep copy:", deep)                     # [[99, 2], [3, 4]]
```
</details>

**Problem 5:** Use a list comprehension to create a list of all even numbers between 1 and 20 (inclusive).

<details>
<summary>Show Answer</summary>

```python
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
</details>
