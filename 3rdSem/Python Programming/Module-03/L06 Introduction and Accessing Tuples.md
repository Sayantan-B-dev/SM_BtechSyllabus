# Introduction and Accessing Tuples

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 6  
**Date:** 24-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## What is a Tuple?

A tuple is an **ordered**, **immutable** collection of elements. Once created, you cannot change, add, or remove elements. Tuples are:

- **Ordered** -- elements have a defined position.
- **Immutable** -- cannot be modified after creation.
- **Heterogeneous** -- can hold different data types.
- **Hashable** -- can be used as dictionary keys (unlike lists).

## Creating Tuples

### Using Parentheses `()`

```python
# Empty tuple
empty = ()
print(empty)       # ()
print(type(empty)) # <class 'tuple'>

# Tuple of integers
numbers = (1, 2, 3, 4, 5)
print(numbers)  # (1, 2, 3, 4, 5)

# Heterogeneous tuple
mixed = (42, "hello", 3.14, True)
print(mixed)  # (42, 'hello', 3.14, True)
```

### Using the `tuple()` Constructor

```python
# Empty tuple
empty = tuple()
print(empty)  # ()

# Convert a list to a tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)  # (1, 2, 3)

# Convert a string to a tuple of characters
tup = tuple("abc")
print(tup)  # ('a', 'b', 'c')

# Convert a range to a tuple
tup = tuple(range(5))
print(tup)  # (0, 1, 2, 3, 4)
```

### Single-Element Tuple

A single-element tuple requires a trailing comma. Without the comma, Python treats the parentheses as grouping operators.

```python
# This is NOT a tuple -- it is just an integer in parentheses
not_a_tuple = (5)
print(type(not_a_tuple))  # <class 'int'>

# This IS a tuple
a_tuple = (5,)
print(type(a_tuple))  # <class 'tuple'>
print(a_tuple)        # (5,)

# The comma is what makes it a tuple, not the parentheses
another = 5,
print(type(another))  # <class 'tuple'>
print(another)       # (5,)
```

## Tuple Immutability

Once a tuple is created, you cannot change, add, or remove elements.

```python
tup = (1, 2, 3)

# tup[0] = 99  # TypeError: 'tuple' object does not support item assignment
# tup.append(4)  # AttributeError: 'tuple' object has no attribute 'append'
# tup.remove(1)  # AttributeError: 'tuple' object has no attribute 'remove'
# del tup[0]     # TypeError: 'tuple' object doesn't support item deletion

# You CAN delete the entire tuple variable
del tup
# print(tup)  # NameError: name 'tup' is not defined
```

## Indexing and Slicing

Indexing and slicing work exactly the same as with lists.

```python
tup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Positive indexing
print(tup[0])   # 10
print(tup[3])   # 40

# Negative indexing
print(tup[-1])  # 100
print(tup[-3])  # 80

# Slicing
print(tup[2:6])     # (30, 40, 50, 60)
print(tup[:4])      # (10, 20, 30, 40)
print(tup[5:])      # (60, 70, 80, 90, 100)
print(tup[1:8:2])   # (20, 40, 60, 80)
print(tup[::-1])    # (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)
```

## Packing and Unpacking

**Packing** is creating a tuple by grouping values. **Unpacking** is extracting those values back into variables.

```python
# Packing
point = 3, 7  # Parentheses are optional
print(point)  # (3, 7)

# Unpacking
x, y = point
print(x)  # 3
print(y)  # 7

# Unpacking with multiple values
person = ("Alice", 30, "Engineer")
name, age, profession = person
print(name)        # Alice
print(age)         # 30
print(profession)  # Engineer
```

### Using `*` for Extended Unpacking

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]  (always a list)
print(last)    # 5

first, second, *rest = numbers
print(first)   # 1
print(second)  # 2
print(rest)    # [3, 4, 5]
```

## Swapping Variables with Tuple Unpacking

Tuple unpacking provides an elegant way to swap two (or more) variables without a temporary variable.

```python
# Traditional swap (requires a temp variable)
a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)  # 10 5

# Pythonic swap using tuple unpacking
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5

# Swapping multiple variables
x, y, z = 1, 2, 3
x, y, z = z, x, y
print(x, y, z)  # 3, 1, 2
```

## Summary

| Concept | Syntax | Example | Result |
|---------|--------|---------|--------|
| Create tuple | `(a, b)` or `tuple()` | `(1, 2, 3)` | `(1, 2, 3)` |
| Single element | `(x,)` | `(5,)` | `(5,)` |
| Index | `t[i]` | `(10,20)[0]` | `10` |
| Slice | `t[i:j]` | `(1,2,3)[1:]` | `(2, 3)` |
| Packing | `t = 1, 2` | `t = 1, 2` | `(1, 2)` |
| Unpacking | `a, b = t` | `a, b = (1,2)` | `a=1, b=2` |
| Swap | `a, b = b, a` | `a,b=1,2; a,b=b,a` | `a=2, b=1` |

---

## Practice Problems

**Problem 1:** Create a tuple `person` containing your name, age, and favorite programming language. Then unpack it into three variables and print each one.

<details>
<summary>Show Answer</summary>

```python
person = ("Alice", 25, "Python")
name, age, lang = person
print(name)  # Alice
print(age)   # 25
print(lang)  # Python
```
</details>

**Problem 2:** Create a single-element tuple containing the number `100`. Verify its type.

<details>
<summary>Show Answer</summary>

```python
t = (100,)
print(type(t))  # <class 'tuple'>
print(t)        # (100,)
```
</details>

**Problem 3:** Given `tup = (5, 10, 15, 20, 25, 30)`, use slicing to extract:
- Elements from index 1 to 4
- The last 3 elements
- Every second element
- The tuple in reverse

<details>
<summary>Show Answer</summary>

```python
tup = (5, 10, 15, 20, 25, 30)
print(tup[1:5])   # (10, 15, 20, 25)
print(tup[-3:])   # (20, 25, 30)
print(tup[::2])   # (5, 15, 25)
print(tup[::-1])  # (30, 25, 20, 15, 10, 5)
```
</details>

**Problem 4:** Use tuple unpacking to swap the values of `a = 100` and `b = 200` in a single line.

<details>
<summary>Show Answer</summary>

```python
a, b = 100, 200
a, b = b, a
print(a, b)  # 200 100
```
</details>

**Problem 5:** Demonstrate that tuples are immutable by attempting to change an element. Show the error message.

<details>
<summary>Show Answer</summary>

```python
t = (1, 2, 3)
# t[0] = 99  # Uncommenting this line produces:
# TypeError: 'tuple' object does not support item assignment
```
</details>
