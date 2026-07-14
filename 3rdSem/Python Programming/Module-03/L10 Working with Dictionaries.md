# Working with Dictionaries

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 10  
**Date:** 02-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Dictionary View Methods: `keys()`, `values()`, `items()`

These methods return **view objects** that dynamically reflect changes to the dictionary.

### `keys()` -- Get All Keys

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

keys = student.keys()
print(keys)  # dict_keys(['name', 'age', 'grade'])

# Convert to a list if needed
print(list(keys))  # ['name', 'age', 'grade']

# Iterate over keys
for key in student.keys():
    print(key, end=" ")  # name age grade
```

### `values()` -- Get All Values

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

values = student.values()
print(list(values))  # ['Alice', 20, 'A']

for val in student.values():
    print(val, end=" ")  # Alice 20 A
```

### `items()` -- Get All Key-Value Pairs as Tuples

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

items = student.items()
print(list(items))
# [('name', 'Alice'), ('age', 20), ('grade', 'A')]

# Iterate with unpacking
for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 20
# grade: A
```

## Iterating Dictionaries

By default, iterating over a dictionary iterates over its keys.

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Iterate over keys (default)
for key in student:
    print(key, end=" ")  # name age grade

print()

# Iterate over values
for val in student.values():
    print(val, end=" ")  # Alice 20 A

print()

# Iterate over key-value pairs
for key, val in student.items():
    print(f"{key} = {val}")
# name = Alice
# age = 20
# grade = A
```

## Removing Items

### `pop(key)` -- Remove by Key and Return Value

```python
student = {"name": "Alice", "age": 20, "grade": "A", "city": "NYC"}

age = student.pop("age")
print(age)     # 20
print(student) # {'name': 'Alice', 'grade': 'A', 'city': 'NYC'}

# pop with default (avoids KeyError)
result = student.pop("major", "Not Found")
print(result)  # Not Found
```

### `popitem()` -- Remove and Return Last Inserted Item

In Python 3.7+, `popitem()` removes and returns the **last inserted** item as a tuple `(key, value)`.

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

item = student.popitem()
print(item)    # ('grade', 'A')
print(student) # {'name': 'Alice', 'age': 20}
```

### `clear()` -- Remove All Items

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
student.clear()
print(student)  # {}
```

### `update()` -- Merge Another Dictionary

`update()` adds key-value pairs from another dictionary (or an iterable of key-value pairs). Existing keys are overwritten.

```python
student = {"name": "Alice", "age": 20}

# Update with another dictionary
student.update({"grade": "A", "city": "New York"})
print(student)
# {'name': 'Alice', 'age': 20, 'grade': 'A', 'city': 'New York'}

# Update with keyword arguments
student.update(major="CS", year=2)
print(student)
# {'name': 'Alice', 'age': 20, 'grade': 'A', 'city': 'New York', 'major': 'CS', 'year': 2}

# Overwrite existing keys
student.update(age=21)
print(student["age"])  # 21
```

## Dictionary Comprehension

Dictionary comprehension creates dictionaries using a concise syntax:

```python
{k: v for k, v in iterable}
```

```python
# Square numbers as dictionary
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
gradebook = {name: score for name, score in zip(names, scores)}
print(gradebook)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# With condition
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transform keys/values
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'hello': 5, 'world': 5, 'python': 6}
```

## Merging Dictionaries (Python 3.9+)

The `|` operator merges two dictionaries. If there are duplicate keys, the right-hand dictionary's value wins.

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = d1 | d2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Overlapping keys -- right side wins
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 99, 'c': 3}

# In-place merge (Python 3.9+)
d1 |= d2
print(d1)  # {'a': 1, 'b': 99, 'c': 3}
```

### Merging in Older Python Versions

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}

# Using update()
merged = {}
merged.update(d1)
merged.update(d2)
print(merged)  # {'a': 1, 'b': 99, 'c': 3}

# Using {**d1, **d2} unpacking (Python 3.5+)
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 99, 'c': 3}
```

## Checking Key Existence with `in`

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

print("name" in student)    # True
print("city" in student)    # False
print("name" not in student) # False

# Always use 'in' to check existence before accessing
if "city" in student:
    print(student["city"])
else:
    print("City not found")  # This runs
```

---

## Practice Problems

**Problem 1:** Given `student = {"name": "Alice", "age": 20, "grade": "A"}`, use `keys()`, `values()`, and `items()` to print all keys, all values, and all key-value pairs.

<details>
<summary>Show Answer</summary>

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))
# Keys: ['name', 'age', 'grade']
# Values: ['Alice', 20, 'A']
# Items: [('name', 'Alice'), ('age', 20), ('grade', 'A')]
```
</details>

**Problem 2:** Use dictionary comprehension to create a dictionary mapping numbers 1 to 10 to their cubes.

<details>
<summary>Show Answer</summary>

```python
cubes = {x: x ** 3 for x in range(1, 11)}
print(cubes)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
```
</details>

**Problem 3:** Given `d1 = {"a": 1, "b": 2}` and `d2 = {"c": 3, "d": 4}`, merge them using the `|` operator and using `update()`.

<details>
<summary>Show Answer</summary>

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# Using | operator
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using update()
d1_copy = {"a": 1, "b": 2}
d1_copy.update(d2)
print(d1_copy)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
</details>

**Problem 3:** Use `pop()` to remove the key `"age"` from `student = {"name": "Alice", "age": 20, "grade": "A"}` and store the removed value. Then use `popitem()` to remove the last item.

<details>
<summary>Show Answer</summary>

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
removed_age = student.pop("age")
print(removed_age)  # 20
print(student)      # {'name': 'Alice', 'grade': 'A'}

last_item = student.popitem()
print(last_item)  # ('grade', 'A')
print(student)    # {'name': 'Alice'}
```
</details>

**Problem 3:** Use dictionary comprehension to create a dictionary that maps each character in the string "hello" to its ASCII code (use `ord()`).

<details>
<summary>Show Answer</summary>

```python
ascii_map = {ch: ord(ch) for ch in "hello"}
print(ascii_map)  # {'h': 104, 'e': 101, 'l': 108, 'o': 111}
```
</details>

**Problem 4:** Write a program that checks if the key `"email"` exists in `user = {"name": "Alice", "age": 20}`. If it does not, add it with value `"alice@example.com"`.

<details>
<summary>Show Answer</summary>

```python
user = {"name": "Alice", "age": 20}
if "email" not in user:
    user["email"] = "alice@example.com"
print(user)
# {'name': 'Alice', 'age': 20, 'email': 'alice@example.com'}
```
</details>

**Problem 5:** Use `clear()` to empty a dictionary, then verify its length is 0.

<details>
<summary>Show Answer</summary>

```python
d = {"a": 1, "b": 2, "c": 3}
d.clear()
print(len(d))  # 0
print(d)       # {}
```
</details>
