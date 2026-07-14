# Accessing Lists and Operations

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 2  
**Date:** 17-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Accessing Elements with Indexing

### Positive Indexing

Elements are accessed using their position number, starting from 0.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry
print(fruits[3])  # date
print(fruits[4])  # elderberry
```

### Negative Indexing

Negative indices count from the end of the list. `-1` is the last element, `-2` is the second last, and so on.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[-1])  # elderberry
print(fruits[-2])  # date
print(fruits[-3])  # cherry
print(fruits[-4])  # banana
print(fruits[-5])  # apple
```

### IndexError

Accessing an index that does not exist raises an `IndexError`.

```python
fruits = ["apple", "banana", "cherry"]
# print(fruits[10])  # IndexError: list index out of range
# print(fruits[-10]) # IndexError: list index out of range
```

## List Slicing

Slicing extracts a portion of a list as a new list. The syntax is `list[start:stop:step]`.

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slice
print(nums[2:6])     # [2, 3, 4, 5]

# Omitting start (defaults to 0)
print(nums[:5])      # [0, 1, 2, 3, 4]

# Omitting stop (defaults to end)
print(nums[7:])      # [7, 8, 9]

# Omitting both gives a full copy
print(nums[:])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using step
print(nums[0:9:3])   # [0, 3, 6]

# Negative step (reverse)
print(nums[::-2])    # [9, 7, 5, 3, 1]

# Negative indices in slice
print(nums[-5:-1])   # [5, 6, 7, 8]
```

## Concatenation (`+`)

The `+` operator joins two or more lists into a new list.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Concatenating multiple lists
result = [0] + list1 + list2 + [7]
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7]
```

## Repetition (`*`)

The `*` operator repeats the list elements a given number of times.

```python
base = [1, 2, 3]
repeated = base * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Also works in reverse order
print(2 * ["a", "b"])  # ['a', 'b', 'a', 'b']
```

## Membership (`in` and `not in`)

The `in` operator checks whether an element exists in a list. It returns `True` or `False`.

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)   # True
print("grape" in fruits)    # False
print("grape" not in fruits) # True
```

## Comparison of Lists

Lists are compared element-by-element using lexicographic (dictionary-style) comparison.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 4]
d = [1, 2, 3, 4]

print(a == b)   # True (same elements)
print(a == c)   # False (3 != 4)
print(a < c)    # True (3 < 4)
print(a < d)    # True (a is shorter, and all elements match up to len(a))
print([1, 2, 3] < [1, 2, 3, 0])  # True (shorter list is considered smaller)
```

## Iterating with a `for` Loop

The `for` loop lets you visit each element of a list one by one.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

### Using `range()` and `len()` for Index-Based Iteration

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry
```

## Summary Table

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| Positive index | `lst[i]` | `[10,20,30][1]` | `20` |
| Negative index | `lst[-i]` | `[10,20,30][-1]` | `30` |
| Slice | `lst[i:j]` | `[1,2,3,4][1:3]` | `[2, 3]` |
| Concatenation | `lst1 + lst2` | `[1,2]+[3,4]` | `[1,2,3,4]` |
| Repetition | `lst * n` | `[1,2]*3` | `[1,2,1,2,1,2]` |
| Membership | `x in lst` | `2 in [1,2,3]` | `True` |
| Comparison | `lst1 == lst2` | `[1,2]==[1,2]` | `True` |
| Iteration | `for x in lst` | -- | visits each element |

---

## Practice Problems

**Problem 1:** Given `nums = [5, 10, 15, 20, 25, 30, 35, 40]`, use slicing to extract:
- Elements from index 2 to 5 (inclusive of 2, exclusive of 5)
- The last 4 elements
- All elements at even indices
- The list in reverse order

<details>
<summary>Show Answer</summary>

```python
nums = [5, 10, 15, 20, 25, 30, 35, 40]
print(nums[2:5])   # [15, 20, 25]
print(nums[-4:])   # [25, 30, 35, 40]
print(nums[::2])   # [5, 15, 25, 35]
print(nums[::-1])  # [40, 35, 30, 25, 20, 15, 10, 5]
```
</details>

**Problem 2:** Write a program that takes two lists `a = [1, 2, 3]` and `b = [4, 5, 6]` and produces `[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]` using concatenation and repetition.

<details>
<summary>Show Answer</summary>

```python
a = [1, 2, 3]
b = [4, 5, 6]
result = (a + b) * 2
print(result)  # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
```
</details>

**Problem 3:** Use a `for` loop to iterate over `colors = ["red", "green", "blue"]` and print each color in uppercase.

<details>
<summary>Show Answer</summary>

```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color.upper())

# Output:
# RED
# GREEN
# BLUE
```
</details>

**Problem 4:** Check whether `"cherry"` is in the list `fruits = ["apple", "banana", "cherry", "date"]` using the `in` operator. Also check if `"grape"` is NOT in the list.

<details>
<summary>Show Answer</summary>

```python
fruits = ["apple", "banana", "cherry", "date"]
print("cherry" in fruits)   # True
print("grape" not in fruits) # True
```
</details>

**Problem 5:** Compare the lists `[1, 2, 100]` and `[1, 2, 3, 4]` using `<` and explain the result.

<details>
<summary>Show Answer</summary>

```python
print([1, 2, 100] < [1, 2, 3, 4])  # False
# Explanation: At index 2, 100 is compared to 3. Since 100 > 3, the result is False.
```
</details>
