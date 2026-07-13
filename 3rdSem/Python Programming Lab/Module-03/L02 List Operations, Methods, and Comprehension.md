# List Operations, Methods, and Comprehension

**Course:** Python Programming Lab  
**Module:** 3 | **Lecture:** 2  
**Date:** 21-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Sort lists of numbers and strings using sorted() and list.sort().
- Search for elements in a list using index(), in operator, and linear search.
- Use list comprehensions to create lists concisely.

## Theory

List sorting: the sorted() function returns a new sorted list without modifying the original. The list.sort() method sorts the list in-place (modifies the original). Both accept a reverse=True parameter for descending order and a key parameter for custom sorting (e.g., key=len for sorting by string length).

List searching: the in operator checks membership (returns boolean). The index(item) method returns the first index of the item (raises ValueError if not found). The count(item) method counts occurrences. For unsorted lists, linear search (iterating through all elements) is used.

List comprehensions provide a concise syntax for creating lists: `[expression for item in iterable if condition]`. They replace for-loop + append patterns. For example, `[x**2 for x in range(10)]` creates a list of squares. The optional if clause filters elements. Comprehensions are more readable and faster than equivalent loop code.

## Procedure

1. Create a new Python file named lab14.py.
2. Create a list of numbers and sort it using both sorted() and list.sort().
3. Sort a list of strings by length using the key parameter.
4. Demonstrate searching with in, index(), and linear search.
5. Use list comprehension to generate squares, filter even numbers, and create modified lists.
6. Compare comprehension with equivalent loop code.

## Source Code

```python
# Module 03 Lab 02: Sorting, Searching, List Comprehension

# Sorting numbers
numbers = [42, 15, 8, 23, 16, 4]
print(f"Original: {numbers}")
print(f"sorted() ascending: {sorted(numbers)}")
print(f"sorted() descending: {sorted(numbers, reverse=True)}")

numbers.sort()
print(f"After sort() in-place: {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sorting strings by length
words = ["python", "java", "c", "javascript", "go", "rust"]
print(f"\nOriginal words: {words}")
print(f"Sorted by length: {sorted(words, key=len)}")
print(f"Sorted by length desc: {sorted(words, key=len, reverse=True)}")

# Searching in lists
fruits = ["apple", "banana", "cherry", "date", "apple"]
print(f"\nFruits: {fruits}")
print(f"'banana' in list: {'banana' in fruits}")
print(f"'grape' in list: {'grape' in fruits}")
print(f"Index of 'cherry': {fruits.index('cherry')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# Linear search
def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

target = "date"
result = linear_search(fruits, target)
print(f"Linear search for '{target}': index {result}")

# List comprehension examples
print("\n--- List Comprehensions ---")

# Squares
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares 1-10: {squares}")

# Filter even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in nums if n % 2 == 0]
print(f"Evens: {evens}")

# Filter even numbers (equivalent for loop)
evens_loop = []
for n in nums:
    if n % 2 == 0:
        evens_loop.append(n)
print(f"Evens (loop): {evens_loop}")

# Modified list
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5 + 32) for c in celsius]
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Nested comprehension: multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(f"\nMultiplication table (1-5):")
for row in table:
    print(row)
```

## Sample Output

```
Original: [42, 15, 8, 23, 16, 4]
sorted() ascending: [4, 8, 15, 16, 23, 42]
sorted() descending: [42, 23, 16, 15, 8, 4]
After sort() in-place: [4, 8, 15, 16, 23, 42]
After sort(reverse=True): [42, 23, 16, 15, 8, 4]

Original words: ['python', 'java', 'c', 'javascript', 'go', 'rust']
Sorted by length: ['c', 'go', 'java', 'rust', 'python', 'javascript']
Sorted by length desc: ['javascript', 'python', 'rust', 'java', 'go', 'c']

Fruits: ['apple', 'banana', 'cherry', 'date', 'apple']
'banana' in list: True
'grape' in list: False
Index of 'cherry': 2
Count of 'apple': 2
Linear search for 'date': index 3

--- List Comprehensions ---
Squares 1-10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens: [2, 4, 6, 8, 10]
Evens (loop): [2, 4, 6, 8, 10]
Celsius: [0, 10, 20, 30, 40]
Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]

Multiplication table (1-5):
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25]
```

## Homework

1. Use list comprehension to create a list of all even numbers between 1 and 50 that are also divisible by 6.
2. Write a program that sorts a list of strings by their last character (use key=lambda).
3. Given a list of words, use list comprehension to create a new list containing only words that start with a vowel (a, e, i, o, u), ignoring case.
