# List Functions and Methods

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 5  
**Date:** 24-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Built-in Functions for Lists

Python provides several built-in functions that work with lists (and other iterables).

### `len()` -- Number of Elements

```python
print(len([1, 2, 3, 4, 5]))  # 5
print(len([]))                # 0
print(len([[1,2], [3,4]]))    # 2 (counts outer elements only)
```

### `max()` and `min()` -- Largest and Smallest

```python
numbers = [45, 12, 89, 3, 67]
print(max(numbers))  # 89
print(min(numbers))  # 3

# Works with strings (alphabetical order)
words = ["apple", "Zebra", "banana"]
print(max(words))  # Zebra (uppercase comes before lowercase in ASCII)
print(min(words))  # apple

# For case-insensitive comparison, use the key parameter
print(max(words, key=str.lower))  # banana
print(min(words, key=str.lower))  # apple
```

### `sum()` -- Total of All Elements

`sum()` works on lists of numbers. An optional second argument specifies a starting value (default 0).

```python
numbers = [10, 20, 30, 40]
print(sum(numbers))       # 100
print(sum(numbers, 100))  # 200 (starts from 100)

# sum() does NOT work on non-numeric lists
# print(sum(["a", "b"]))  # TypeError
```

### `any()` and `all()`

- `any(iterable)` returns `True` if **at least one** element is truthy.
- `all(iterable)` returns `True` if **all** elements are truthy.

```python
# Truthy and falsy values: 0, None, False, empty sequences are falsy
print(any([0, 0, 1]))     # True (1 is truthy)
print(any([0, 0, 0]))     # False (all falsy)
print(any([]))            # False (empty iterable)

print(all([1, 2, 3]))     # True (all truthy)
print(all([1, 0, 3]))     # False (0 is falsy)
print(all([]))            # True (empty iterable -- vacuous truth)

# Practical use: check if all numbers are positive
nums = [10, 20, 30, 40]
print(all(x > 0 for x in nums))  # True

# Check if any number is negative
nums = [10, -5, 30]
print(any(x < 0 for x in nums))  # True
```

## `map()` and `filter()` with Lists

### `map()` -- Apply a Function to Every Element

`map(function, iterable)` applies a function to each element and returns a **map object** (an iterator). Convert it to a list with `list()`.

```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Using lambda (anonymous function)
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert strings to integers
str_nums = ["10", "20", "30"]
int_nums = list(map(int, str_nums))
print(int_nums)  # [10, 20, 30]
```

### `filter()` -- Keep Elements That Satisfy a Condition

`filter(function, iterable)` keeps only elements for which the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Using lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter out None values
values = [1, None, 2, None, 3]
clean = list(filter(lambda x: x is not None, values))
print(clean)  # [1, 2, 3]
```

### Combining `map()` and `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16, 36, 64, 100]

# Equivalent list comprehension (more readable)
result = [x ** 2 for x in numbers if x % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]
```

## `reduce()` from `functools`

`reduce(function, iterable)` cumulatively applies a function to the elements, reducing the sequence to a single value. It is not a built-in; it must be imported from `functools`.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers using reduce
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 15

# Find the maximum using reduce
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)  # 5

# Factorial using reduce
factorial = reduce(lambda a, b: a * b, range(1, 6))
print(factorial)  # 120 (1*2*3*4*5)
```

## `zip()` with Lists

`zip(*iterables)` pairs up elements from multiple iterables into tuples. It stops at the shortest iterable.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Pair names with scores
pairs = list(zip(names, scores))
print(pairs)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Unpacking zipped pairs
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78

# zip with three lists
subjects = ["Math", "Science", "English"]
grades = [90, 85, 88]
semesters = [1, 1, 2]
combined = list(zip(names, subjects, grades, semesters))
print(combined)
# [('Alice', 'Math', 90, 1), ('Bob', 'Science', 85, 1), ('Charlie', 'English', 88, 2)]

# Uneven lengths -- stops at shortest
a = [1, 2, 3]
b = [10, 20]
print(list(zip(a, b)))  # [(1, 10), (2, 20)]
```

---

## Practice Problems

**Problem 1:** Given `nums = [15, 8, 22, 3, 10, 7]`, use built-in functions to find the length, maximum, minimum, and sum.

<details>
<summary>Answer</summary>

```python
nums = [15, 8, 22, 3, 10, 7]
print(len(nums))  # 6
print(max(nums))  # 22
print(min(nums))  # 3
print(sum(nums))  # 65
```
</details>

**Problem 2:** Use `map()` and `filter()` together to get the squares of odd numbers from 1 to 20. Then write the equivalent list comprehension.

<details>
<summary>Answer</summary>

```python
# Using map and filter
result = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, range(1, 21))))
print(result)

# Equivalent list comprehension
result = [x**2 for x in range(1, 21) if x % 2 != 0]
print(result)
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
```
</details>

**Problem 3:** Use `reduce()` to find the product of all numbers in `[2, 3, 4, 5]`.

<details>
<summary>Answer</summary>

```python
from functools import reduce
product = reduce(lambda a, b: a * b, [2, 3, 4, 5])
print(product)  # 120
```
</details>

**Problem 4:** Given `names = ["Alice", "Bob", "Charlie"]` and `ages = [25, 30, 35]`, use `zip()` to create a list of tuples and then print each name with its age.

<details>
<summary>Answer</summary>

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```
</details>

**Problem 5:** Use `any()` and `all()` to check if a list `[10, 20, 30, 40, 50]` contains any number greater than 45, and if all numbers are positive.

<details>
<summary>Answer</summary>

```python
nums = [10, 20, 30, 40, 50]
print(any(x > 45 for x in nums))  # True (50 > 45)
print(all(x > 0 for x in nums))   # True
```
</details>
