# Introduction and Accessing Values

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 9  
**Date:** 31-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## What is a Dictionary?

A dictionary is an **unordered** collection of **key-value pairs**. Each key is unique and maps to a value. Dictionaries are:

- **Mutable** -- you can add, modify, or remove key-value pairs.
- **Unordered** (before Python 3.7) / **Insertion-ordered** (Python 3.7+).
- **Key-value mapping** -- each key maps to exactly one value.
- **Keys must be immutable** (strings, numbers, tuples) and **hashable**.

## Creating Dictionaries

### Using Curly Braces `{}`

```python
# Empty dictionary
empty = {}
print(empty)  # {}
print(type(empty))  # <class 'dict'>

# Dictionary with initial values
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student)
# {'name': 'Alice', 'age': 20, 'grade': 'A'}
```

### Using the `dict()` Constructor

```python
# Using keyword arguments
person = dict(name="Bob", age=25, city="New York")
print(person)
# {'name': 'Bob', 'age': 25, 'city': 'New York'}

# From a list of tuples (key-value pairs)
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# From two zipped lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "London"]
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London'}
```

## Keys Must Be Immutable

Dictionary keys must be **hashable** (immutable). Lists, dictionaries, and sets cannot be keys.

```python
# Valid keys: strings, numbers, tuples (of immutable elements)
valid = {
    "name": "Alice",    # string key
    42: "answer",       # integer key
    3.14: "pi",         # float key
    (1, 2): "point"     # tuple key (immutable)
}
print(valid)
# {'name': 'Alice', 42: 'answer', 3.14: 'pi', (1, 2): 'point'}

# Invalid keys
# invalid = {[1, 2]: "list"}  # TypeError: unhashable type: 'list'
# invalid = {{"a": 1}: "dict"}  # TypeError: unhashable type: 'dict'
```

## Accessing Values

### Using Square Brackets `dict[key]`

If the key exists, it returns the value. If the key does not exist, it raises a `KeyError`.

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

print(student["name"])   # Alice
print(student["age"])    # 20

# print(student["city"])  # KeyError: 'city'
```

### Using `dict.get(key, default)`

`get()` returns the value if the key exists, otherwise it returns `None` (or a default value you provide). It never raises a `KeyError`.

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

print(student.get("name"))        # Alice
print(student.get("city"))        # None (no error)
print(student.get("city", "Unknown"))  # Unknown (default value)
print(student.get("age", 0))      # 20 (key exists, default ignored)
```

## Adding and Modifying Key-Value Pairs

```python
student = {"name": "Alice", "age": 20}

# Adding a new key-value pair
student["grade"] = "A"
print(student)  # {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Modifying an existing key
student["age"] = 21
print(student)  # {'name': 'Alice', 'age': 21, 'grade': 'A'}

# Adding multiple new keys
student["city"] = "New York"
student["major"] = "Computer Science"
print(student)
# {'name': 'Alice', 'age': 21, 'grade': 'A', 'city': 'New York', 'major': 'Computer Science'}
```

## Dictionary Length

`len(dict)` returns the number of key-value pairs.

```python
empty = {}
print(len(empty))  # 0

student = {"name": "Alice", "age": 20, "grade": "A"}
print(len(student))  # 3

# Adding more pairs increases the length
student["city"] = "New York"
print(len(student))  # 4
```

## Summary

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| Create dict | `{}` or `dict()` | `{"a": 1}` | `{'a': 1}` |
| Access value | `d[key]` | `d["name"]` | Value or KeyError |
| Safe access | `d.get(key)` | `d.get("x")` | Value or None |
| Add/Modify | `d[key] = val` | `d["x"] = 5` | Updates dict |
| Length | `len(d)` | `len({"a":1})` | `1` |

---

## Practice Problems

**Problem 1:** Create a dictionary `car` with keys `brand`, `model`, `year`, and `color`. Assign appropriate values. Print the dictionary and its length.

<details>
<summary>Show Answer</summary>

```python
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "Blue"
}
print(car)
print(len(car))  # 4
```
</details>

**Problem 2:** Given `student = {"name": "Bob", "age": 22}`, add a new key `"grade"` with value `"B"`, then change `"age"` to `23`. Print the updated dictionary.

<details>
<summary>Show Answer</summary>

```python
student = {"name": "Bob", "age": 22}
student["grade"] = "B"
student["age"] = 23
print(student)  # {'name': 'Bob', 'age': 23, 'grade': 'B'}
```
</details>

**Problem 3:** Use `dict.get()` to safely access a key that does not exist. Provide a default value of `"Not Found"`.

<details>
<summary>Show Answer</summary>

```python
d = {"a": 1, "b": 2}
print(d.get("c"))              # None
print(d.get("c", "Not Found")) # Not Found
print(d.get("a", "Not Found")) # 1 (key exists, default ignored)
```
</details>

**Problem 4:** Create a dictionary using the `dict()` constructor with keyword arguments for `title`, `author`, and `year`. Print the dictionary.

<details>
<summary>Show Answer</summary>

```python
book = dict(title="1984", author="George Orwell", year=1949)
print(book)
# {'title': '1984', 'author': 'George Orwell', 'year': 1949}
```
</details>

**Problem 5:** Try to use a list as a dictionary key. What error do you get? Explain why.

<details>
<summary>Show Answer</summary>

```python
# d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
# Lists are mutable and therefore unhashable. Dictionary keys must be immutable (hashable).
```
</details>
