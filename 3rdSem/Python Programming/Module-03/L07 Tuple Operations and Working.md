# Tuple Operations and Working

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 7  
**Date:** 26-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Concatenation (`+`)

The `+` operator joins two or more tuples into a new tuple. Since tuples are immutable, a new tuple is always created.

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print(result)  # (1, 2, 3, 4, 5, 6)

# Concatenating multiple tuples
result = (0,) + t1 + t2 + (7, 8)
print(result)  # (0, 1, 2, 3, 4, 5, 6, 7, 8)
```

## Repetition (`*`)

```python
base = ("ha",)
repeated = base * 3
print(repeated)  # ('ha', 'ha', 'ha')

numbers = (1, 2, 3)
print(numbers * 4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## Membership (`in` and `not in`)

```python
tup = ("apple", "banana", "cherry")

print("banana" in tup)   # True
print("grape" in tup)    # False
print("grape" not in tup) # True
```

## Tuple Methods: `count()` and `index()`

Tuples have only two methods because they are immutable.

```python
tup = (1, 2, 3, 2, 4, 2, 5, 2)

# count(x) -- how many times x appears
print(tup.count(2))  # 4
print(tup.count(1))  # 1
print(tup.count(9))  # 0

# index(x) -- position of first occurrence
print(tup.index(2))     # 1
print(tup.index(2, 2))  # 3 (search from index 2)
print(tup.index(5))     # 6
```

## Nested Tuples

```python
# Tuple of tuples (like a 2D grid)
grid = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(grid[0])      # (1, 2, 3)
print(grid[1][2])   # 6

# Iterating over nested tuples
for row in grid:
    for val in row:
        print(val, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## When to Use Tuples vs Lists

| Scenario | Use Tuple | Use List |
|----------|-----------|----------|
| Data should not change | Yes | No |
| Dictionary keys | Yes | No |
| Function arguments (fixed) | Yes | No |
| Return multiple values | Yes | No |
| Data that grows/shrinks | No | Yes |
| Need to sort/reverse in-place | No | Yes |
| Large collection of homogeneous data | No | Yes |
| Represent a fixed record (e.g., coordinates) | Yes | No |

## Returning Multiple Values from Functions

Functions that return multiple values actually return a tuple. The parentheses are optional.

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # returns a tuple

result = divide(17, 5)
print(result)       # (3, 2)
print(type(result)) # <class 'tuple'>

# Unpack the result
q, r = divide(17, 5)
print(f"Quotient: {q}, Remainder: {r}")  # Quotient: 3, Remainder: 2
```

---

## Practice Problems

**Problem 1:** Given `t1 = (1, 2, 3)` and `t2 = (4, 5, 6)`, create `t3` that is the concatenation of `t1` and `t2` repeated twice. Print `t3`.

<details>
<summary>Show Answer</summary>

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = (t1 + t2) * 2
print(t3)  # (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
```
</details>

**Problem 2:** Given `tup = (5, 10, 15, 10, 20, 10, 25)`, use `count()` and `index()` to find how many times `10` appears and the index of its first occurrence.

<details>
<summary>Show Answer</summary>

```python
tup = (5, 10, 15, 10, 20, 10, 25)
print(tup.count(10))  # 3
print(tup.index(10))  # 1
```
</details>

**Problem 3:** Create a nested tuple representing a 2x3 matrix:
```
1 2 3
4 5 6
```
Access and print the element at row 2, column 3 (value 6).

<details>
<summary>Show Answer</summary>

```python
matrix = ((1, 2, 3), (4, 5, 6))
print(matrix[1][2])  # 6
```
</details>

**Problem 4:** Write a function `split(number)` that takes an integer and returns a tuple of its digits. For example, `split(1234)` should return `(1, 2, 3, 4)`.

<details>
<summary>Show Answer</summary>

Convert the number to a string, then to a tuple of characters, then map each character to an integer.

```python
def split(number):
    return tuple(int(d) for d in str(number))

print(split(1234))  # (1, 2, 3, 4)
```
</details>

**Problem 5:** Given `data = ((1, 2), (3, 4, 5), (6,))`, write a loop that prints the length of each inner tuple.

<details>
<summary>Show Answer</summary>

```python
data = ((1, 2), (3, 4, 5), (6,))
for t in data:
    print(len(t))

# Output:
# 2
# 3
# 1
```
</details>
