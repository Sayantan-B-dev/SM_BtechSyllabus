# List Operations, Methods, and Comprehension

**Course:** Python Programming Lab  
**Module:** 3 | **Lecture:** 4  
**Date:** 28-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Create tuples and understand their immutability.
- Use tuple packing and unpacking for multiple assignments.
- Write programs demonstrating tuple methods and their use as immutable lists.

## Theory

A tuple is an ordered, immutable sequence of elements enclosed in parentheses (). Like lists, tuples can hold elements of different types and support indexing and slicing. Unlike lists, tuples cannot be modified after creation: no append, remove, or item assignment. This immutability makes tuples usable as dictionary keys and ensures data integrity.

Tuple packing creates a tuple by assigning multiple values separated by commas: `t = 1, 2, 3`. Unpacking assigns tuple elements to individual variables: `a, b, c = t`. This is commonly used for swapping variables without a temporary variable: `a, b = b, a`. Functions can return multiple values as a tuple, which the caller can unpack.

Tuple methods are limited: count(item) returns the number of occurrences, index(item) returns the first index. Since tuples are immutable, they have fewer methods than lists. Use a tuple when you want to store a collection that should not change. Use a list when you need to modify the collection.

## Procedure

1. Create a new Python file named lab16.py.
2. Create tuples using parentheses, tuple(), and packing (no parentheses).
3. Demonstrate indexing and slicing on tuples.
4. Show that trying to modify a tuple raises TypeError.
5. Demonstrate packing and unpacking, including swapping variables.
6. Write a function that returns multiple values as a tuple.
7. Demonstrate tuple methods: count() and index().
8. Show a tuple used as a dictionary key.

## Source Code

```python
# Module 03 Lab 04: Tuple Basics, Packing/Unpacking, Methods

# Creating tuples
t1 = (1, 2, 3, 4, 5)
t2 = tuple([10, 20, 30])
t3 = 100, 200, 300  # packing without parentheses

print(f"t1: {t1}")
print(f"t2: {t2}")
print(f"t3: {t3}")
print(f"Type of t3: {type(t3)}")

# Indexing and slicing
print(f"\nt1[0]: {t1[0]}")
print(f"t1[-1]: {t1[-1]}")
print(f"t1[1:4]: {t1[1:4]}")

# Immutability demonstration
try:
    t1[0] = 99
except TypeError as e:
    print(f"\nCannot modify tuple: {e}")

# Tuple packing and unpacking
point = (10, 20)
x, y = point  # unpacking
print(f"\nUnpacked point: x = {x}, y = {y}")

# Swapping using tuples
a = 5
b = 10
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Function returning multiple values as tuple
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [45, 12, 78, 34, 90, 23]
minimum, maximum = min_max(nums)
print(f"\nNumbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

# Tuple methods
t = (1, 2, 3, 2, 4, 2, 5)
print(f"\nTuple: {t}")
print(f"count(2): {t.count(2)}")
print(f"index(4): {t.index(4)}")

# Tuple as dictionary key (immutable requirement)
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago"
}
print(f"\nDictionary with tuple keys: {locations}")
print(f"Location at (40.7128, -74.0060): {locations[(40.7128, -74.0060)]}")
```

## Sample Output

```
t1: (1, 2, 3, 4, 5)
t2: (10, 20, 30)
t3: (100, 200, 300)
Type of t3: <class 'tuple'>

t1[0]: 1
t1[-1]: 5
t1[1:4]: (2, 3, 4)

Cannot modify tuple: 'tuple' object does not support item assignment

Unpacked point: x = 10, y = 20

Before swap: a = 5, b = 10
After swap: a = 10, b = 5

Numbers: [45, 12, 78, 34, 90, 23]
Min: 12, Max: 90

Tuple: (1, 2, 3, 2, 4, 2, 5)
count(2): 3
index(4): 4

Dictionary with tuple keys: {(40.7128, -74.0060): 'New York', (34.0522, -118.2437): 'Los Angeles', (41.8781, -87.6298): 'Chicago'}
Location at (40.7128, -74.0060): New York
```

## Homework

1. Write a function that takes three numbers and returns them sorted in ascending order as a tuple.
2. Write a program that creates a list of tuples, where each tuple contains (name, age, grade). Then print each student's details using unpacking in a for loop.
3. Write a program using tuple unpacking to iterate through a dictionary's items() and print key-value pairs in reverse order (value then key).
