# Tuple Functions and Methods

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 8  
**Date:** 31-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Built-in Functions with Tuples

All the built-in functions that work on iterables also work with tuples.

### `len()` -- Number of Elements

```python
tup = (10, 20, 30, 40, 50)
print(len(tup))  # 5
print(len(()))   # 0
```

### `max()` and `min()` -- Largest and Smallest

```python
numbers = (45, 12, 89, 3, 67)
print(max(numbers))  # 89
print(min(numbers))  # 3

# With strings
words = ("apple", "Zebra", "banana")
print(max(words))  # Zebra (ASCII order)
print(min(words))  # apple
```

### `sum()` -- Total of All Elements

```python
numbers = (10, 20, 30, 40)
print(sum(numbers))       # 100
print(sum(numbers, 50))   # 150 (starts from 50)
```

### `any()` and `all()`

```python
tup = (0, 1, 0, 1)
print(any(tup))  # True (at least one truthy value)
print(all(tup))  # False (0 is falsy)

# Practical examples
scores = (85, 92, 78, 95)
print(all(s >= 40 for s in scores))  # True (all passed)
print(any(s >= 90 for s in scores))  # True (at least one A-grade)
```

## `sorted()` with Tuples

`sorted()` returns a **list** (not a tuple) because it needs to return a mutable collection.

```python
tup = (4, 2, 9, 1, 5)
sorted_list = sorted(tup)
print(sorted_list)  # [1, 2, 4, 5, 9]  (list, not tuple)
print(type(sorted_list))  # <class 'list'>

# To get a tuple back, use tuple()
sorted_tup = tuple(sorted(tup))
print(sorted_tup)  # (1, 2, 4, 5, 9)

# Descending order
print(sorted(tup, reverse=True))  # [9, 5, 4, 2, 1]
```

## Tuple Comprehension? (Generator Expressions)

There is no tuple comprehension in Python. Using parentheses around a comprehension creates a **generator expression**, not a tuple.

```python
# This is a generator expression, NOT a tuple comprehension
gen = (x ** 2 for x in range(5))
print(gen)  # <generator object <genexpr> at 0x...>
print(type(gen))  # <class 'generator'>

# To create a tuple, pass the generator to tuple()
tup = tuple(x ** 2 for x in range(5))
print(tup)  # (0, 1, 4, 9, 16)

# Generator expressions are memory-efficient (lazy evaluation)
# They produce values one at a time
for val in (x ** 2 for x in range(5)):
    print(val, end=" ")  # 0 1 4 9 16
```

## `namedtuple` from `collections`

`namedtuple` creates tuple subclasses with named fields. This makes code more readable by accessing elements by name instead of index.

```python
from collections import namedtuple

# Define a named tuple type
Point = namedtuple("Point", ["x", "y"])

# Create instances
p1 = Point(3, 7)
p2 = Point(x=10, y=20)

# Access by name (readable)
print(p1.x)  # 3
print(p1.y)  # 7

# Access by index (still works)
print(p1[0])  # 3
print(p1[1])  # 7

# Unpacking works too
x, y = p1
print(x, y)  # 3 7

# Named tuples are still tuples
print(isinstance(p1, tuple))  # True
```

### Practical Examples of `namedtuple`

```python
from collections import namedtuple

# Student record
Student = namedtuple("Student", ["name", "age", "grade"])

s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 22, "B")

print(s1.name)   # Alice
print(s2.grade)  # B

# More readable than regular tuples
# Compare:
student_tuple = ("Alice", 20, "A")
print(student_tuple[0])  # Alice (what does index 0 mean?)

# vs namedtuple
print(s1.name)  # Alice (clear meaning)
```

### `_asdict()` and `_replace()` Methods

Named tuples also provide useful helper methods.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)

# Convert to dictionary
print(p._asdict())  # {'x': 3, 'y': 7}

# Create a new instance with one field changed
p2 = p._replace(x=10)
print(p)   # Point(x=3, y=7)  -- original unchanged
print(p2)  # Point(x=10, y=7) -- new instance
```

## Summary Table

| Function/Method | Description | Works on tuples? | Returns |
|----------------|-------------|-----------------|---------|
| `len(t)` | Number of elements | Yes | Integer |
| `max(t)` | Largest element | Yes | Element |
| `min(t)` | Smallest element | Yes | Element |
| `sum(t)` | Sum of elements | Yes (numeric) | Number |
| `any(t)` | Any truthy element? | Yes | Boolean |
| `all(t)` | All truthy elements? | Yes | Boolean |
| `sorted(t)` | Return sorted list | Yes | List |
| `t.count(x)` | Count occurrences | Yes | Integer |
| `t.index(x)` | Find first index | Yes | Integer |

---

## Practice Problems

**Problem 1:** Given `scores = (78, 92, 85, 67, 95, 88)`, use built-in functions to find the highest score, lowest score, total score, and average score.

<details>
<summary>Answer</summary>

```python
scores = (78, 92, 85, 67, 95, 88)
print("Max:", max(scores))       # 95
print("Min:", min(scores))       # 67
print("Sum:", sum(scores))       # 505
print("Avg:", sum(scores) / len(scores))  # 84.17
```
</details>

**Problem 2:** Use `sorted()` to sort the tuple `(9, 3, 7, 1, 5)` in descending order. What type does `sorted()` return? Convert it back to a tuple.

<details>
<summary>Answer</summary>

```python
tup = (9, 3, 7, 1, 5)
sorted_list = sorted(tup, reverse=True)
print(sorted_list)       # [9, 7, 5, 3, 1]
print(type(sorted_list)) # <class 'list'>

sorted_tup = tuple(sorted_list)
print(sorted_tup)  # (9, 7, 5, 3, 1)
```
</details>

**Problem 3:** Use `any()` and `all()` to check if the tuple `(10, 20, 30, 40, 50)` contains any number less than 15, and if all numbers are multiples of 5.

<details>
<summary>Answer</summary>

```python
tup = (10, 20, 30, 40, 50)
print(any(x < 15 for x in tup))  # True (10 < 15)
print(all(x % 5 == 0 for x in tup))  # True
```
</details>

**Problem 4:** Create a `namedtuple` called `Student` with fields `name`, `age`, and `grade`. Create two instances and print their names.

<details>
<summary>Answer</summary>

```python
from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "grade"])
s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 22, "B")
print(s1.name)  # Alice
print(s2.name)  # Bob
```
</details>

**Problem 5:** Use a generator expression to create a generator that yields squares of numbers from 1 to 5. Convert it to a tuple and print the result.

<details>
<summary>Answer</summary>

```python
gen = (x ** 2 for x in range(1, 6))
result = tuple(gen)
print(result)  # (1, 4, 9, 16, 25)
```
</details>
