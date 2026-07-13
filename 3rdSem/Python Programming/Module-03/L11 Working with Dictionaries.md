# Working with Dictionaries

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 11  
**Date:** 07-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Nested Dictionaries

A dictionary can contain other dictionaries as values. This is useful for representing structured or hierarchical data.

```python
# Nested dictionary representing students
students = {
    "S001": {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 90, "science": 85, "english": 88}
    },
    "S002": {
        "name": "Bob",
        "age": 22,
        "grades": {"math": 75, "science": 80, "english": 72}
    },
    "S003": {
        "name": "Charlie",
        "age": 21,
        "grades": {"math": 95, "science": 92, "english": 90}
    }
}

# Accessing nested values
print(students["S001"]["name"])              # Alice
print(students["S001"]["grades"]["math"])    # 90
print(students["S003"]["grades"]["english"]) # 90

# Modifying nested values
students["S002"]["grades"]["science"] = 88
print(students["S002"]["grades"]["science"])  # 88

# Adding a new nested key
students["S001"]["grades"]["history"] = 91
print(students["S001"]["grades"])
# {'math': 90, 'science': 85, 'english': 88, 'history': 91}
```

### Iterating Over Nested Dictionaries

```python
for student_id, info in students.items():
    print(f"ID: {student_id}")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print(f"  Grades:")
    for subject, score in info["grades"].items():
        print(f"    {subject}: {score}")

# Output:
# ID: S001
#   Name: Alice
#   Age: 20
#   Grades:
#     math: 90
#     science: 85
#     english: 88
# ID: S002
#   Name: Bob
#   Age: 22
#   Grades:
#     math: 75
#     science: 88
#     english: 72
# ID: S003
#   Name: Charlie
#   Age: 21
#   Grades:
#     math: 95
#     science: 92
#     english: 90
```

## `defaultdict` from `collections`

`defaultdict` is a dictionary that provides a default value for missing keys. This eliminates the need to check for key existence before accessing.

```python
from collections import defaultdict

# Regular dictionary -- requires checking
word_counts = {}
text = "apple banana apple cherry banana apple"
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)
# {'apple': 3, 'banana': 2, 'cherry': 1}

# Using defaultdict -- no need to check
word_counts = defaultdict(int)  # default value is 0
for word in text.split():
    word_counts[word] += 1
print(dict(word_counts))
# {'apple': 3, 'banana': 2, 'cherry': 1}
```

### Common Default Factories

```python
from collections import defaultdict

# int -- default is 0
counter = defaultdict(int)
counter["a"] += 1
print(counter["a"])  # 1
print(counter["b"])  # 0 (no KeyError)

# list -- default is empty list
groups = defaultdict(list)
groups["even"].append(2)
groups["even"].append(4)
groups["odd"].append(1)
print(dict(groups))  # {'even': [2, 4], 'odd': [1]}

# set -- default is empty set
sets = defaultdict(set)
sets["a"].add(1)
sets["a"].add(2)
sets["b"].add(1)
print(dict(sets))  # {'a': {1, 2}, 'b': {1}}

# str -- default is empty string
strings = defaultdict(str)
print(strings["missing"])  # '' (empty string)
```

## `Counter` from `collections`

`Counter` is a dictionary subclass for counting hashable objects. It maps elements to their count.

```python
from collections import Counter

# Count elements in a list
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(fruits)
print(counter)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Access count (returns 0 for missing items, no KeyError)
print(counter["apple"])   # 3
print(counter["grape"])   # 0 (no error)

# Most common elements
print(counter.most_common(2))
# [('apple', 3), ('banana', 2)]

# Count characters in a string
char_count = Counter("mississippi")
print(char_count)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(char_count.most_common(1))  # [('i', 4)]
```

## Dictionary View Objects

`keys()`, `values()`, and `items()` return **view objects** that dynamically reflect changes to the dictionary.

```python
student = {"name": "Alice", "age": 20}

keys = student.keys()
values = student.values()
items = student.items()

print(list(keys))   # ['name', 'age']
print(list(values)) # ['Alice', 20]

# Modify the dictionary
student["grade"] = "A"
student["age"] = 21

# Views automatically reflect the changes
print(list(keys))   # ['name', 'age', 'grade']
print(list(values)) # ['Alice', 21, 'A']
print(list(items))  # [('name', 'Alice'), ('age', 21), ('grade', 'A')]
```

### Set-Like Operations on `keys()`

The `keys()` view supports set operations (union, intersection, difference).

```python
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

# Keys in both dictionaries (intersection)
common = d1.keys() & d2.keys()
print(common)  # {'b', 'c'}

# Keys in d1 but not in d2 (difference)
only_d1 = d1.keys() - d2.keys()
print(only_d1)  # {'a'}

# Keys in either dictionary (union)
all_keys = d1.keys() | d2.keys()
print(all_keys)  # {'a', 'b', 'c', 'd'}
```

## Performance Considerations

- **Lookup by key**: O(1) average time (hash table).
- **Insertion**: O(1) average time.
- **Deletion**: O(1) average time.
- **Iteration**: O(n) where n is the number of items.
- **Memory**: Dictionaries use more memory than lists due to the hash table overhead.

```python
import time

# Dictionary lookup is O(1) -- fast even for large dictionaries
large_dict = {i: i ** 2 for i in range(1000000)}
start = time.time()
val = large_dict[999999]
end = time.time()
print(f"Dict lookup: {end - start:.6f} seconds")  # Very fast

# List lookup is O(n) -- slow for large lists
large_list = list(range(1000000))
start = time.time()
found = 999999 in large_list
end = time.time()
print(f"List membership: {end - start:.6f} seconds")  # Slower
```

---

## Practice Problems

**Problem 1:** Create a nested dictionary `company` with departments as keys and each department containing a list of employee names. For example: `"Engineering": ["Alice", "Bob"]`, `"Sales": ["Charlie"]`. Add a new employee to Engineering and print the structure.

<details>
<summary>Answer</summary>

```python
company = {
    "Engineering": ["Alice", "Bob"],
    "Sales": ["Charlie"],
    "HR": ["Diana"]
}
company["Engineering"].append("Eve")
print(company)
# {'Engineering': ['Alice', 'Bob', 'Eve'], 'Sales': ['Charlie'], 'HR': ['Diana']}
```
</details>

**Problem 2:** Use `defaultdict` to group a list of words by their first letter. Test with `words = ["apple", "banana", "avocado", "blueberry", "cherry"]`.

<details>
<summary>Answer</summary>

```python
from collections import defaultdict

words = ["apple", "banana", "avocado", "blueberry", "cherry"]
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
print(dict(groups))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```
</details>

**Problem 2:** Use `Counter` to find the most common character in the string "mississippi".

<details>
<summary>Answer</summary>

```python
from collections import Counter
c = Counter("mississippi")
print(c.most_common(1))  # [('i', 4)]
```
</details>

**Problem 3:** Demonstrate that dictionary view objects are dynamic by modifying the dictionary after creating a view and showing the view reflects the change.

<details>
<summary>Answer</summary>

```python
d = {"a": 1, "b": 2}
keys = d.keys()
print(list(keys))  # ['a', 'b']
d["c"] = 3
print(list(keys))  # ['a', 'b', 'c']  -- view updated automatically
```
</details>

**Problem 4:** Use `defaultdict` with `list` to build a dictionary that maps each word length to a list of words of that length. Test with `["hi", "hello", "hey", "python", "go"]`.

<details>
<summary>Answer</summary>

```python
from collections import defaultdict

words = ["hi", "hello", "hey", "python", "go"]
by_length = defaultdict(list)
for word in words:
    by_length[len(word)].append(word)
print(dict(by_length))
# {2: ['hi', 'go'], 5: ['hello'], 3: ['hey'], 6: ['python']}
```
</details>

**Problem 4:** Use `Counter` to count the frequency of each word in the sentence "the quick brown fox jumps over the lazy dog". Print the 3 most common words.

<details>
<summary>Answer</summary>

```python
from collections import Counter
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
counter = Counter(words)
print(counter.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]
```
</details>

**Problem 5:** Create a nested dictionary representing a library with two books. Each book has `title`, `author`, and `year`. Print the author of the second book.

<details>
<summary>Answer</summary>

```python
library = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}
print(library["book2"]["author"])  # Harper Lee
```
</details>
