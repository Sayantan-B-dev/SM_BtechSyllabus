# Accessing Strings

**Course:** Python Programming  
**Module:** 2 | **Lecture:** 1  
**Date:** 29-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 105-142

## Creating Strings

A string is a sequence of characters enclosed within quotes. Python treats single quotes, double quotes, and triple quotes as valid string delimiters.

### Single Quotes

Use single quotes for simple strings.

```python
str1 = 'Hello'
print(str1)          # Output: Hello
print(type(str1))    # Output: <class 'str'>
```

### Double Quotes

Double quotes work identically to single quotes. Useful when the string itself contains a single quote.

```python
str2 = "Python Programming"
print(str2)          # Output: Python Programming

# Embedding a single quote inside double quotes
str3 = "It's a sunny day"
print(str3)          # Output: It's a sunny day
```

### Triple Quotes

Triple quotes (''' or """) allow multi-line strings. They are also used as docstrings for functions and classes.

```python
str4 = '''This is a
multi-line
string.'''
print(str4)
# Output:
# This is a
# multi-line
# string.

str5 = """Another way
to write multi-line
strings."""
print(str5)
# Output:
# Another way
# to write multi-line
# strings.
```

### Using str() Constructor

The `str()` function converts other data types into strings.

```python
num = 100
s = str(num)
print(s)             # Output: 100
print(type(s))       # Output: <class 'str'>

pi = 3.14159
s2 = str(pi)
print(s2)            # Output: 3.14159
```

## Immutability of Strings

Strings in Python are **immutable**, meaning once created, their contents cannot be changed. Any operation that appears to modify a string creates a new string in memory.

```python
message = "Hello"
# Trying to change a character raises an error
# message[0] = 'J'   # TypeError: 'str' object does not support item assignment

# Concatenation creates a new string
new_message = message + " World"
print(message)        # Output: Hello (original unchanged)
print(new_message)    # Output: Hello World (new string created)

# Check memory addresses
print(id(message))       # e.g. 238472938472
print(id(new_message))   # different address
```

### Why Immutability?

- **Security**: Strings used as keys in dictionaries remain hashable.
- **Performance**: Python can reuse string objects (interning) for efficiency.
- **Predictability**: Functions receiving strings cannot accidentally modify the caller's data.

```python
# Python interns short strings automatically
a = "hello"
b = "hello"
print(a is b)        # Output: True (same object, interned)

c = "hello world"
d = "hello world"
print(c is d)        # Output: True (Python may intern these too)
```

## String Indexing

Every character in a string has an index position. Python supports two indexing systems.

### Positive Indexing

Indexes start at 0 for the first character and go up to `n-1` (where n is the string length).

```python
text = "PYTHON"
#       012345   (positive indexes)

print(text[0])   # Output: P
print(text[1])   # Output: Y
print(text[2])   # Output: T
print(text[3])   # Output: H
print(text[4])   # Output: O
print(text[5])   # Output: N
```

### Negative Indexing

Indexes start at -1 for the last character and go backward.

```python
text = "PYTHON"
#       012345   (positive)
#       -6-5-4-3-2-1   (negative)

print(text[-1])   # Output: N (last character)
print(text[-2])   # Output: O
print(text[-3])   # Output: H
print(text[-4])   # Output: T
print(text[-5])   # Output: Y
print(text[-6])   # Output: P (first character)
```

### IndexError

Accessing an index outside the valid range raises an IndexError.

```python
text = "Hello"
# print(text[10])   # IndexError: string index out of range
# print(text[-10])  # IndexError: string index out of range
```

## The len() Function

`len()` returns the number of characters in a string (including spaces and punctuation).

```python
word = "Python"
print(len(word))       # Output: 6

sentence = "Hello World"
print(len(sentence))   # Output: 11 (space counts as a character)

empty = ""
print(len(empty))      # Output: 0
```

Using `len()` to safely access the last character:

```python
text = "Programming"
last_index = len(text) - 1
print(text[last_index])   # Output: g
print(text[-1])           # Output: g (simpler)
```

## String Slicing

Slicing extracts a portion (substring) of a string. The syntax is `string[start:stop:step]`.

- `start`: starting index (inclusive), defaults to 0
- `stop`: ending index (exclusive), defaults to end of string
- `step`: increment between indexes, defaults to 1

```python
text = "PYTHON PROGRAMMING"

# Basic slice from index 0 to 5 (exclusive)
print(text[0:6])       # Output: PYTHON

# Slice from index 7 to 18 (exclusive)
print(text[7:18])      # Output: PROGRAMMING

# Slice with step
print(text[0:18:2])    # Output: PTO POMIG (every 2nd character)

# Omitting start (defaults to 0)
print(text[:6])        # Output: PYTHON

# Omitting stop (defaults to end)
print(text[7:])        # Output: PROGRAMMING

# Omitting both
print(text[:])         # Output: PYTHON PROGRAMMING (full copy)

# Negative step (reverse)
print(text[::-1])      # Output: GNIMARGORP NOHTYP
```

### Common Slicing Patterns

```python
s = "Hello World"

# First 5 characters
print(s[:5])           # Output: Hello

# Last 5 characters
print(s[-5:])          # Output: World

# Middle characters
print(s[1:9])          # Output: ello Wor

# Everything except first and last
print(s[1:-1])         # Output: ello Worl

# Reverse a string
print(s[::-1])         # Output: dlroW olleH
```

## Accessing Characters

Characters can be accessed individually using indexing or iterated using loops.

### Using Index

```python
word = "Python"
print(word[0])   # P
print(word[-1])  # n
```

### Using a Loop

```python
word = "Python"
for ch in word:
    print(ch, end=" ")   # Output: P y t h o n
```

### While Loop with Index

```python
word = "Python"
i = 0
while i < len(word):
    print(f"Index {i}: {word[i]}")
    i += 1
# Output:
# Index 0: P
# Index 1: y
# Index 2: t
# Index 3: h
# Index 4: o
# Index 5: n
```

## String Iteration

### Iterating Over Characters

```python
text = "CODE"
for ch in text:
    print(ch)
# Output:
# C
# O
# D
# E
```

### Iterating with Index (enumerate)

```python
text = "CODE"
for index, ch in enumerate(text):
    print(f"Character at position {index}: {ch}")
# Output:
# Character at position 0: C
# Character at position 1: O
# Character at position 2: D
# Character at position 3: E
```

### Iterating in Reverse

```python
text = "CODE"
for ch in reversed(text):
    print(ch)
# Output:
# E
# D
# O
# C
```

### List Comprehension on Strings

```python
text = "Hello"
chars = [ch.upper() for ch in text]
print(chars)             # Output: ['H', 'E', 'L', 'L', 'O']

vowels = [ch for ch in text if ch in "aeiouAEIOU"]
print(vowels)            # Output: ['e', 'o']
```

## Practice Problems

1. **Character Counter**: Write a program that takes a string from the user and prints each character with its positive and negative index.

   **Hint**: Use a `for` loop with `enumerate()`. The negative index is `index - len(string)`.

   **Answer**:
   ```python
   s = input("Enter a string: ")
   for i, ch in enumerate(s):
       neg = i - len(s)
       print(f"Index {i} ({neg}): {ch}")
   ```

2. **First and Last**: Write a program that prints the first and last character of a given string using both positive and negative indexing.

   **Answer**:
   ```python
   s = input("Enter a string: ")
   print(f"First: {s[0]} (positive), {s[-len(s)]} (negative)")
   print(f"Last: {s[len(s)-1]} (positive), {s[-1]} (negative)")
   ```

3. **Middle Character**: Given a string, print the middle character(s). If the string length is even, print the two middle characters.

   **Hint**: Use `len(s) // 2` to find the middle.

   **Answer**:
   ```python
   s = input("Enter a string: ")
   n = len(s)
   mid = n // 2
   if n % 2 == 0:
       print(s[mid-1:mid+1])
   else:
       print(s[mid])
   ```

4. **String Immutability Demonstration**: Write code that shows strings are immutable by attempting to change a character and catching the error, then showing how to correctly "modify" by creating a new string.

   **Answer**:
   ```python
   s = "Python"
   try:
       s[0] = "J"
   except TypeError as e:
       print(f"Error: {e}")
   # Correct way
   s = "J" + s[1:]
   print(s)   # Output: Jython
   ```

5. **Extract Domain**: Given an email address like "user@example.com", use slicing to extract just the username and just the domain.

   **Hint**: Find the `@` position first.

   **Answer**:
   ```python
   email = "john.doe@university.edu"
   at_pos = email.index("@")
   username = email[:at_pos]
   domain = email[at_pos+1:]
   print(f"Username: {username}")
   print(f"Domain: {domain}")
   ```
