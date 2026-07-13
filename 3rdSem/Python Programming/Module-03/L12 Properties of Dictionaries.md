# Properties of Dictionaries

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 12  
**Date:** 07-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Hash Table Concept

A dictionary in Python is implemented using a **hash table**. A hash table is a data structure that stores key-value pairs and provides very fast lookup.

### How Hashing Works

1. When you insert a key-value pair, Python computes a **hash value** of the key using the `hash()` function.
2. The hash value determines the **bucket** (storage location) where the key-value pair is stored.
3. When you look up a key, Python computes its hash again and goes directly to the bucket -- no searching needed.

```python
# The hash() function returns an integer for hashable objects
print(hash("hello"))   # 123456789 (value varies by run)
print(hash(42))        # 42
print(hash((1, 2, 3))) # some integer

# Unhashable types raise TypeError
# print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'
```

## Key Requirements (Immutable and Hashable)

For an object to be used as a dictionary key, it must be:

1. **Hashable** -- must have a `__hash__()` method that returns an integer.
2. **Immutable** -- the hash value must never change during the object's lifetime.

```python
# Hashable (valid keys)
d = {
    "string": 1,      # strings are hashable
    42: 2,            # integers are hashable
    3.14: 3,          # floats are hashable
    True: 4,          # booleans are hashable
    (1, 2): 5,        # tuples are hashable (if all elements are hashable)
}

# Unhashable (invalid keys)
# d[[1, 2]] = "list"     # TypeError: unhashable type: 'list'
# d[{"a": 1}] = "dict"   # TypeError: unhashable type: 'dict'
# d[{1, 2}] = "set"      # TypeError: unhashable type: 'set'

# Tuple with mutable element is also unhashable
# d[([1, 2], 3)] = "bad"  # TypeError: unhashable type: 'list'
```

## Dictionary vs List Performance

The key advantage of dictionaries over lists is **lookup speed**.

| Operation | List | Dictionary |
|-----------|------|------------|
| Lookup by index/key | O(1) by index | O(1) by key |
| Search for value | O(n) -- must scan | O(1) -- direct hash |
| Insert at end | O(1) amortized | O(1) |
| Insert at beginning | O(n) | O(1) |
| Delete by value | O(n) | O(1) by key |
| Memory | Less | More (hash table overhead) |

```python
import time

# List search is O(n) -- slow for large data
n = 1000000
large_list = list(range(n))
large_dict = {i: i for i in range(n)}

# Search in list
start = time.time()
found = 999999 in large_list
end = time.time()
print(f"List search: {end - start:.6f} seconds")

# Search in dict
start = time.time()
found = 999999 in large_dict
end = time.time()
print(f"Dict search: {end - start:.6f} seconds")

# Dict is dramatically faster for large datasets
```

## `OrderedDict` from `collections`

`OrderedDict` is a dictionary subclass that remembers the insertion order. In Python 3.7+, regular dictionaries also maintain insertion order, but `OrderedDict` provides additional methods.

```python
from collections import OrderedDict

# Creating an OrderedDict
od = OrderedDict()
od["z"] = 1
od["a"] = 2
od["m"] = 3
print(od)
# OrderedDict([('z', 1), ('a', 2), ('m', 3)])

# move_to_end() -- move a key to the end
od.move_to_end("z")
print(od)
# OrderedDict([('a', 2), ('m', 3), ('z', 1)])

# move_to_end with last=False moves to the beginning
od.move_to_end("m", last=False)
print(od)
# OrderedDict([('m', 3), ('a', 2), ('z', 1)])

# popitem() with last=False removes from the beginning
first = od.popitem(last=False)
print(first)  # ('m', 3)
print(od)     # OrderedDict([('a', 2), ('z', 1)])
```

## Practical Applications

### 1. Counting Word Frequency

```python
text = "the quick brown fox jumps over the lazy dog the dog barks"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1,
#  'over': 1, 'lazy': 1, 'dog': 2, 'barks': 1}
```

### 2. Grouping Data

```python
students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "C"),
    ("Eve", "B"),
]

# Group students by grade
from collections import defaultdict
by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)

print(dict(by_grade))
# {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Eve'], 'C': ['Diana']}
```

### 3. Memoization (Caching)

Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again.

```python
# Fibonacci without memoization (slow)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Fibonacci with memoization (fast)
def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    cache[n] = result
    return result

import time

start = time.time()
print(fib(35))       # 9227465 (slow)
end = time.time()
print(f"Without memo: {end - start:.4f} seconds")

start = time.time()
print(fib_memo(35))  # 9227465 (fast)
end = time.time()
print(f"With memo: {end - start:.4f} seconds")
```

## Complete Method Reference

| Method | Description | Returns |
|--------|-------------|---------|
| `d.keys()` | View of all keys | `dict_keys` |
| `d.values()` | View of all values | `dict_values` |
| `d.items()` | View of all (key, value) pairs | `dict_items` |
| `d.get(k, default)` | Safe access | Value or default |
| `d.pop(k, default)` | Remove and return value | Value or default |
| `d.popitem()` | Remove and return last item | (key, value) tuple |
| `d.clear()` | Remove all items | None |
| `d.update(other)` | Merge from another dict | None |
| `d1 \| d2` | Merge (Python 3.9+) | New dict |
| `k in d` | Check key existence | Boolean |

---

## Practice Problems

**Problem 1:** Write a function `count_words(text)` that returns a dictionary with word frequencies. Test with `"apple banana apple cherry banana apple"`.

<details>
<summary>Answer</summary>

```python
def count_words(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(count_words("apple banana apple cherry banana apple"))
# {'apple': 3, 'banana': 2, 'cherry': 1}
```
</details>

**Problem 2:** Use `defaultdict` to group the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` into "even" and "odd" groups.

<details>
<summary>Answer</summary>

```python
from collections import defaultdict

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
groups = defaultdict(list)
for n in nums:
    groups["even" if n % 2 == 0 else "odd"].append(n)
print(dict(groups))
# {'odd': [1, 3, 5, 7, 9], 'even': [2, 4, 6, 8, 10]}
```
</details>

**Problem 3:** Implement a simple cache using a dictionary. The function `expensive_square(n)` should print "Computing..." and then cache the result for future calls.

<details>
<summary>Answer</summary>

```python
cache = {}
def expensive_square(n):
    if n in cache:
        return cache[n]
    print(f"Computing square of {n}...")
    result = n ** 2
    cache[n] = result
    return result

print(expensive_square(5))  # Computes and caches
print(expensive_square(5))  # Returns from cache (no "Computing..." message)
print(expensive_square(10)) # Computes
print(expensive_square(10)) # Returns from cache
```
</details>

**Problem 4:** Compare the time to check membership of `999999` in a list of 1 million numbers vs a dictionary of 1 million keys. Write code to demonstrate the difference.

<details>
<summary>Answer</summary>

```python
import time

n = 1000000
lst = list(range(n))
d = {i: i for i in range(n)}

start = time.time()
print(999999 in lst)
end = time.time()
print(f"List: {end - start:.6f}s")

start = time.time()
print(999999 in d)
end = time.time()
print(f"Dict: {end - start:.6f}s")
# Dictionary lookup is orders of magnitude faster
```
</details>

**Problem 4:** Use `OrderedDict` to create a dictionary with keys `"z"`, `"a"`, `"m"` in that order. Then move `"z"` to the end and print the order.

<details>
<summary>Answer</summary>

```python
from collections import OrderedDict
od = OrderedDict()
od["z"] = 1
od["a"] = 2
od["m"] = 3
print(list(od.keys()))  # ['z', 'a', 'm']
od.move_to_end("z")
print(list(od.keys()))  # ['a', 'm', 'z']
```
</details>

**Problem 4:** Write a function `invert_dict(d)` that takes a dictionary and returns a new dictionary where keys become values and values become keys. Assume all values are unique and hashable.

<details>
<summary>Answer</summary>

```python
def invert_dict(d):
    return {v: k for k, v in d.items()}

original = {"a": 1, "b": 2, "c": 3}
inverted = invert_dict(original)
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```
</details>

**Problem 5:** Use memoization to optimize a recursive function that computes the nth triangular number (T(n) = n + T(n-1), T(0) = 0).

<details>
<summary>Answer</summary>

```python
cache = {}
def triangular(n):
    if n in cache:
        return cache[n]
    if n == 0:
        result = 0
    else:
        result = n + triangular(n - 1)
    cache[n] = result
    return result

print(triangular(10))  # 55
print(triangular(100)) # 5050
print(triangular(100)) # 5050 (from cache)
```
</details>

## Comprehensive Practice Problems (Covering All 12 Lectures)

**Problem 1 (Lists):** Write a program that takes a list of numbers and returns a new list containing only the even numbers, squared. Use list comprehension.

<details>
<summary>Answer</summary>

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x ** 2 for x in nums if x % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]
```
</details>

**Problem 2 (Tuples):** Write a function `min_max_avg(numbers)` that returns a tuple containing the minimum, maximum, and average of the list.

<details>
<summary>Answer</summary>

```python
def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

result = min_max_avg([10, 20, 30, 40, 50])
print(result)  # (10, 50, 30.0)
```
</details>

**Problem 3 (Dictionaries):** Write a program that takes a string and creates a dictionary mapping each character to its frequency. Ignore spaces.

<details>
<summary>Answer</summary>

```python
text = "hello world"
freq = {}
for ch in text.replace(" ", ""):
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```
</details>

**Problem 4 (Mixed):** Given a list of tuples `[("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]`, create a dictionary mapping names to scores. Then find the student with the highest score.

<details>
<summary>Answer</summary>

```python
data = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]
scores = dict(data)
print(scores)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

top_student = max(scores, key=scores.get)
print(f"Top student: {top_student} with {scores[top_student]}")
# Top student: Diana with 95
```
</details>

**Problem 5 (Comprehensive):** Write a program that reads a paragraph of text and produces:
1. A dictionary of word frequencies.
2. A list of unique words sorted alphabetically.
3. The most frequent word and its count.
4. A dictionary grouping words by their first letter.

<details>
<summary>Answer</summary>

```python
from collections import defaultdict, Counter

text = "the quick brown fox jumps over the lazy dog the dog barks"

# 1. Word frequencies
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequencies:", freq)

# 2. Unique words sorted
unique_sorted = sorted(set(words))
print("Unique sorted:", unique_sorted)

# 3. Most frequent word
counter = Counter(words)
most_common = counter.most_common(1)[0]
print(f"Most frequent: '{most_common[0]}' appears {most_common[1]} times")

# 4. Group by first letter
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print("Grouped by letter:", dict(by_letter))
```
</details>

**Problem 5 (Performance):** Create a list of 100,000 numbers and a dictionary with the same keys. Time how long it takes to find the number `99999` in the list vs the dictionary. Explain the result.

<details>
<summary>Answer</summary>

```python
import time

n = 100000
lst = list(range(n))
d = {i: i for i in range(n)}

start = time.time()
print(99999 in lst)
end = time.time()
print(f"List: {end - start:.6f}s")

start = time.time()
print(99999 in d)
end = time.time()
print(f"Dict: {end - start:.6f}s")

# Dictionary is much faster because it uses O(1) hash table lookup,
# while the list must scan elements sequentially (O(n)).
```
</details>
