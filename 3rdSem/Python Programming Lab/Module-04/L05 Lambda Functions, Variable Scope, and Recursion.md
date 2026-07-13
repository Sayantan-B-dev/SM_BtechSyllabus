# Lambda Functions, Variable Scope, and Recursion

**Course:** Python Programming Lab  
**Module:** 4 | **Lecture:** 5  
**Date:** 25-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Define anonymous functions using the lambda keyword.
- Use lambda with map() to transform sequences.
- Use lambda with filter() to select elements.
- Use lambda as the key function for sorted().

## Theory

A lambda function is a small, anonymous function defined using the lambda keyword. The syntax is `lambda arguments: expression`. Lambda functions can take any number of arguments but can only contain a single expression (which is evaluated and returned). They are useful where a short function is needed temporarily, especially as arguments to higher-order functions.

The map() function applies a given function to each item of an iterable and returns a map object. `map(function, iterable)` returns an iterator of results. Typically used with lambda: `map(lambda x: x**2, numbers)`. The result can be converted to a list with list().

The filter() function selects items from an iterable for which the function returns True. `filter(function, iterable)` returns an iterator. The sorted() function accepts a key parameter for custom sorting: `sorted(iterable, key=lambda)`. Both map and filter can often be replaced by list comprehensions, but using them with lambda is a common functional programming style.

## Procedure

1. Create a new Python file named lab23.py.
2. Write lambda functions for simple operations: add, square, max of two numbers.
3. Use map() with lambda to square all numbers in a list.
4. Use filter() with lambda to keep only even numbers.
5. Use sorted() with a lambda key to sort strings by length, by last character, and by a custom criterion.
6. Compare lambda + map with list comprehension for the same task.
7. Test all programs.

## Source Code

```python
# Module 04 Lab 05: Lambda Functions with map, filter, sorted

# Basic lambda functions
add = lambda a, b: a + b
square = lambda x: x ** 2
max_of_two = lambda a, b: a if a > b else b

print("--- Basic Lambdas ---")
print(f"add(5, 3) = {add(5, 3)}")
print(f"square(7) = {square(7)}")
print(f"max_of_two(10, 20) = {max_of_two(10, 20)}")

# Using lambda with map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nOriginal: {numbers}")

squared = list(map(lambda x: x ** 2, numbers))
print(f"map(lambda x: x**2, numbers): {squared}")

cubed = list(map(lambda x: x ** 3, numbers))
print(f"map(lambda x: x**3, numbers): {cubed}")

# Equivalent list comprehension
squared_comp = [x ** 2 for x in numbers]
print(f"List comprehension (squares): {squared_comp}")

# Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nfilter(lambda x: x%2==0): {evens}")

odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"filter(lambda x: x%2!=0): {odds}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"filter(lambda x: x>5): {greater_than_5}")

# Using lambda with sorted()
words = ["python", "java", "c", "javascript", "go", "rust", "zig"]
print(f"\nOriginal words: {words}")

sorted_default = sorted(words)
print(f"sorted(): {sorted_default}")

sorted_by_len = sorted(words, key=lambda w: len(w))
print(f"sorted(by length): {sorted_by_len}")

sorted_by_last_char = sorted(words, key=lambda w: w[-1])
print(f"sorted(by last char): {sorted_by_last_char}")

sorted_by_len_desc = sorted(words, key=lambda w: len(w), reverse=True)
print(f"sorted(by length desc): {sorted_by_len_desc}")

# Custom sorting: sort by the number of vowels in each word
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

sorted_by_vowels = sorted(words, key=lambda w: count_vowels(w))
print(f"sorted(by vowel count): {sorted_by_vowels}")

# map with multiple iterables
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, a, b))
print(f"\nmap with two lists: {a} + {b} = {sums}")
```

## Sample Output

```
--- Basic Lambdas ---
add(5, 3) = 8
square(7) = 49
max_of_two(10, 20) = 20

Original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
map(lambda x: x**2, numbers): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
map(lambda x: x**3, numbers): [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
List comprehension (squares): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

filter(lambda x: x%2==0): [2, 4, 6, 8, 10]
filter(lambda x: x%2!=0): [1, 3, 5, 7, 9]
filter(lambda x: x>5): [6, 7, 8, 9, 10]

Original words: ['python', 'java', 'c', 'javascript', 'go', 'rust', 'zig']
sorted(): ['c', 'go', 'java', 'javascript', 'python', 'rust', 'zig']
sorted(by length): ['c', 'go', 'zig', 'java', 'rust', 'python', 'javascript']
sorted(by last char): ['java', 'c', 'go', 'python', 'rust', 'zig', 'javascript']
sorted(by length desc): ['javascript', 'python', 'rust', 'java', 'zig', 'go', 'c']
sorted(by vowel count): ['c', 'go', 'zig', 'rust', 'java', 'python', 'javascript']

map with two lists: [1, 2, 3, 4] + [10, 20, 30, 40] = [11, 22, 33, 44]
```

## Homework

1. Use map() with lambda to convert a list of temperatures in Celsius to Fahrenheit: [0, 10, 20, 30, 40].
2. Use filter() with lambda to extract all strings from a list that have length >= 5: ["hi", "hello", "python", "code", "programming"].
3. Use sorted() with a lambda key to sort a list of tuples (name, age, score) by score in descending order: [("Alice", 20, 85), ("Bob", 22, 92), ("Charlie", 21, 78)].
