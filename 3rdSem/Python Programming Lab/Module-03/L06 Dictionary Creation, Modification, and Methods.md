# Dictionary Creation, Modification, and Methods

**Course:** Python Programming Lab  
**Module:** 3 | **Lecture:** 6  
**Date:** 04-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Use dictionary methods: keys(), values(), items(), update(), setdefault().
- Create dictionaries using dictionary comprehension.
- Work with nested dictionaries for structured data like student records.
- Merge dictionaries and invert a dictionary.

## Theory

Dictionary methods provide powerful ways to manipulate data. keys() returns a view of all keys, values() returns a view of all values, items() returns (key, value) pairs. The update() method merges another dictionary into the current one, overwriting existing keys. setdefault(key, default) returns the value for key if it exists; otherwise inserts key with default and returns default.

Dictionary comprehension follows the pattern: `{key_expr: value_expr for item in iterable if condition}`. This is useful for creating dictionaries from lists, transforming existing dictionaries, or filtering. For example, `{x: x**2 for x in range(5)}` creates {0:0, 1:1, 2:4, 3:9, 4:16}.

Nested dictionaries store dictionaries as values, allowing hierarchical data representation. For example, a student record might have keys like "personal" (containing name, age) and "grades" (containing subject: score pairs). Accessing nested data uses chained keys: `records[student_id]["grades"]["math"]`.

## Procedure

1. Create a new Python file named lab18.py.
2. Demonstrate keys(), values(), items() on a sample dictionary.
3. Use update() to merge two dictionaries and setdefault() for safe initialization.
4. Create a dictionary using dictionary comprehension (squares, even-filtered).
5. Create nested dictionaries for student records with personal info and grades.
6. Write a program to merge two dictionaries (handle key conflicts).
7. Write a program to invert a dictionary (swap keys and values), handling duplicate values.

## Source Code

```python
# Module 03 Lab 06: Dictionary Methods, Comprehension, Nested Dicts

# Dictionary methods
student = {"name": "Alice", "age": 20, "grade": "A", "city": "NYC"}
print(f"Dictionary: {student}")
print(f"keys(): {list(student.keys())}")
print(f"values(): {list(student.values())}")
print(f"items(): {list(student.items())}")

# update() to merge
extra_info = {"email": "alice@example.com", "grade": "A+"}
student_copy = student.copy()
student_copy.update(extra_info)
print(f"\nAfter update(): {student_copy}")

# setdefault()
marks = {"math": 85, "science": 90}
marks.setdefault("english", 75)  # adds english: 75
marks.setdefault("math", 99)     # does nothing, math already exists
print(f"setdefault example: {marks}")

# Dictionary comprehension
print("\n--- Dictionary Comprehension ---")

# Squares
sq_dict = {x: x**2 for x in range(1, 11)}
print(f"Squares: {sq_dict}")

# Filter even numbers
even_sq = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_sq}")

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"\nOriginal: {original}")
print(f"Inverted: {inverted}")

# Handling duplicate values when inverting
grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "Diana": "C"}
inverted_grades = {}
for name, grade in grades.items():
    if grade not in inverted_grades:
        inverted_grades[grade] = []
    inverted_grades[grade].append(name)
print(f"\nGrades: {grades}")
print(f"Students by grade: {inverted_grades}")

# Nested dictionaries for student records
print("\n--- Nested Student Records ---")
students = {
    101: {"name": "Alice", "age": 20, "grades": {"math": 85, "science": 90, "eng": 78}},
    102: {"name": "Bob", "age": 22, "grades": {"math": 72, "science": 88, "eng": 91}},
    103: {"name": "Charlie", "age": 21, "grades": {"math": 95, "science": 93, "eng": 89}}
}

for sid, info in students.items():
    g = info["grades"]
    avg = sum(g.values()) / len(g)
    print(f"ID {sid}: {info['name']}, Age {info['age']}, Avg Grade: {avg:.1f}")

# Merge two dictionaries with conflict resolution
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4, "e": 5}

merged = dict1.copy()
for key, value in dict2.items():
    if key in merged:
        print(f"Conflict on '{key}': {merged[key]} vs {value}, keeping from dict2")
    merged[key] = value

print(f"\nMerged dictionary: {merged}")
```

## Sample Output

```
Dictionary: {'name': 'Alice', 'age': 20, 'grade': 'A', 'city': 'NYC'}
keys(): ['name', 'age', 'grade', 'city']
values(): ['Alice', 20, 'A', 'NYC']
items(): [('name', 'Alice'), ('age', 20), ('grade', 'A'), ('city', 'NYC')]

After update(): {'name': 'Alice', 'age': 20, 'grade': 'A+', 'city': 'NYC', 'email': 'alice@example.com'}
setdefault example: {'math': 85, 'science': 90, 'english': 75}

--- Dictionary Comprehension ---
Squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
Even squares: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

Original: {'a': 1, 'b': 2, 'c': 3}
Inverted: {1: 'a', 2: 'b', 3: 'c'}

Grades: {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A', 'Diana': 'C'}
Students by grade: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['Diana']}

--- Nested Student Records ---
ID 101: Alice, Age 20, Avg Grade: 84.3
ID 102: Bob, Age 22, Avg Grade: 83.7
ID 103: Charlie, Age 21, Avg Grade: 92.3

Conflict on 'b': 2 vs 20, keeping from dict2
Merged dictionary: {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5}
```

## Homework

1. Use dictionary comprehension to create a mapping of numbers 1 to 15 to their cubes, but only for numbers divisible by 3.
2. Write a program that takes a list of (name, age) tuples and creates a nested dictionary grouping people by age range (e.g., "10-19", "20-29").
3. Write a program that merges three dictionaries using a loop and the update() method, printing any key conflicts as they occur.
