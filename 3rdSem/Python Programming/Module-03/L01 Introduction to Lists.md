# Introduction to Lists

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 1  
**Date:** 12-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## What is a List?

A list is a built-in Python data type that stores an ordered collection of items. Lists are:

- **Ordered** -- items have a defined position (index).
- **Mutable** -- you can change, add, or remove items after creation.
- **Heterogeneous** -- can hold items of different data types.
- **Dynamic** -- size can grow or shrink as needed.

Lists are one of the most versatile and commonly used data structures in Python.

## Creating Lists

### Using Square Brackets `[]`

```python
# Empty list
empty_list = []
print(empty_list)  # []

# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']
```

### Using the `list()` Constructor

```python
# Empty list using list()
empty = list()
print(empty)  # []

# Convert a string to a list of characters
chars = list("hello")
print(chars)  # ['h', 'e', 'l', 'l', 'o']

# Convert a tuple to a list
tup = (1, 2, 3)
lst = list(tup)
print(lst)  # [1, 2, 3]

# Convert a range to a list
nums = list(range(5))
print(nums)  # [0, 1, 2, 3, 4]
```

## Heterogeneous Elements

Unlike arrays in many other languages, Python lists can hold items of different data types in the same list.

```python
mixed = [42, "hello", 3.14, True, None]
print(mixed)  # [42, 'hello', 3.14, True, None]

# A list can even contain other lists, dictionaries, etc.
complex_list = [1, "two", [3, 4], {"key": "value"}]
print(complex_list)
# [1, 'two', [3, 4], {'key': 'value'}]
```

## Nested Lists

A list inside another list is called a nested list. This is useful for representing matrices, tables, or grouped data.

```python
# A 2x3 matrix (2 rows, 3 columns)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix)
# [[1, 2, 3], [4, 5, 6]]

# Accessing elements in nested lists
print(matrix[0])     # [1, 2, 3]  -- first row
print(matrix[0][1])  # 2          -- first row, second column
```

## List Indexing

Indexing works exactly like strings. Each element has a position number starting from 0.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0-based, left to right)
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[4])  # elderberry

# Negative indexing (-1 is the last element, right to left)
print(fruits[-1])  # elderberry
print(fruits[-2])  # date
print(fruits[-5])  # apple
```

## List Slicing

Slicing extracts a sublist using the syntax `list[start:stop:step]`. The `stop` index is exclusive.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slice: start:stop
print(numbers[2:6])   # [2, 3, 4, 5]

# Omitting start defaults to 0
print(numbers[:4])    # [0, 1, 2, 3]

# Omitting stop defaults to end
print(numbers[6:])    # [6, 7, 8, 9]

# Step
print(numbers[1:8:2]) # [1, 3, 5, 7]

# Negative step reverses
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Full slice returns a copy
copy_of_numbers = numbers[:]
print(copy_of_numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## List Mutability vs String Immutability

This is a critical difference between lists and strings.

```python
# Lists are MUTABLE -- you can change elements in-place
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Strings are IMMUTABLE -- you cannot change characters in-place
word = "hello"
# word[0] = "H"  # TypeError: 'str' object does not support item assignment

# To "change" a string, you must create a new one
word = "H" + word[1:]
print(word)  # Hello
```

## The `len()` Function

`len()` returns the number of elements in a list.

```python
empty = []
print(len(empty))  # 0

numbers = [10, 20, 30, 40]
print(len(numbers))  # 4

nested = [[1, 2], [3, 4, 5], [6]]
print(len(nested))  # 3 (the outer list has 3 elements)
```

## Summary

| Concept | Syntax | Example |
|---------|--------|---------|
| Create list | `[]` or `list()` | `[1, 2, 3]` |
| Heterogeneous | Mix types | `[1, "a", True]` |
| Nested list | List inside list | `[[1,2], [3,4]]` |
| Index | `lst[i]` | `lst[0]` |
| Slice | `lst[i:j:k]` | `lst[1:4]` |
| Length | `len(lst)` | `len([1,2,3])` -> 3 |

---

## Practice Problems

**Problem 1:** Create a list called `mixed` that contains an integer, a float, a string, a boolean, and another list. Print the list and its length.

<details>
<summary>Show Answer</summary>

```python
mixed = [10, 3.14, "hello", True, [1, 2]]
print(mixed)
print(len(mixed))
```
</details>

**Problem 2:** Given `nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`, use slicing to extract:
- First 4 elements
- Last 3 elements
- Every second element
- The list in reverse order

<details>
<summary>Show Answer</summary>

```python
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums[:4])      # [10, 20, 30, 40]
print(nums[-3:])     # [80, 90, 100]
print(nums[::2])     # [10, 30, 50, 70, 90]
print(nums[::-1])    # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
```
</details>

**Problem 3:** Create a 3x3 matrix (nested list) representing:
```
1 2 3
4 5 6
7 8 9
```
Access and print the element `5`.

<details>
<summary>Show Answer</summary>

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])  # 5
```
</details>

**Problem 4:** Explain with a code example why strings are immutable but lists are mutable.

<details>
<summary>Show Answer</summary>

```python
# List: mutable
lst = [1, 2, 3]
lst[0] = 99  # Works fine
print(lst)   # [99, 2, 3]

# String: immutable
s = "abc"
# s[0] = "X"  # TypeError: 'str' object does not support item assignment
# Must create a new string instead
s = "X" + s[1:]
print(s)  # Xbc
```
</details>

**Problem 5:** Use the `list()` constructor to create a list from the string "Python". Then print the length of the resulting list.

<details>
<summary>Show Answer</summary>

```python
chars = list("Python")
print(chars)  # ['P', 'y', 't', 'h', 'o', 'n']
print(len(chars))  # 6
```
</details>
