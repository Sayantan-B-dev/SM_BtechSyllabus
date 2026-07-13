# String Indexing, Operations, and Built-in Functions

**Course:** Python Programming Lab  
**Module:** 2 | **Lecture:** 1  
**Date:** 07-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Create strings and understand string immutability in Python.
- Use indexing (positive and negative) and slicing to access substrings.
- Write programs to reverse a string, extract substrings, and check for palindromes.

## Theory

A string in Python is a sequence of characters enclosed in single quotes ('...') or double quotes ("..."). Strings are immutable, meaning their contents cannot be changed after creation. Any operation that modifies a string actually creates a new string object.

Each character in a string has an index. Positive indexing starts from 0 (first character) and goes up to length-1 (last character). Negative indexing starts from -1 (last character) and goes backward. For example, in "Hello", H is at index 0 and -5, while o is at index 4 and -1.

Slicing extracts a substring using the syntax `string[start:stop:step]`. start is inclusive, stop is exclusive. Omitting start defaults to 0, omitting stop defaults to the end. A negative step reverses the direction. For example, `s[::-1]` reverses the string. A palindrome is a string that reads the same forward and backward (e.g., "madam", "racecar").

## Procedure

1. Create a new Python file named lab09.py (Module 02, Lab 01).
2. Create strings using single quotes, double quotes, and triple quotes for multiline strings.
3. Demonstrate indexing: print the first character, last character, and a character from the middle.
4. Use slicing to extract a substring from a given string.
5. Write a program to reverse a string using slicing.
6. Write a program to check if a given string is a palindrome.
7. Test with sample strings.

## Source Code

```python
# Module 02 Lab 01: String Creation, Indexing, and Slicing

# Creating strings
str1 = 'Hello'
str2 = "World"
str3 = """This is a
multiline string."""

print(f"str1: {str1}")
print(f"str2: {str2}")
print(f"str3: {str3}")

# String indexing
text = "Python"
print(f"\nString: {text}")
print(f"First character (text[0]): {text[0]}")
print(f"Third character (text[2]): {text[2]}")
print(f"Last character (text[-1]): {text[-1]}")
print(f"Second last (text[-2]): {text[-2]}")

# String slicing
s = "Programming"
print(f"\nString: {s}")
print(f"s[0:4]: {s[0:4]}")     # "Prog"
print(f"s[3:8]: {s[3:8]}")     # "gramm"
print(f"s[:6]: {s[:6]}")       # "Progra"
print(f"s[4:]: {s[4:]}")       # "amming"
print(f"s[::2]: {s[::2]}")     # "Pormig" (every 2nd char)

# Reverse a string using slicing
word = "Python"
reversed_word = word[::-1]
print(f"\nOriginal: {word}")
print(f"Reversed: {reversed_word}")

# Palindrome check
test_str = input("Enter a string to check palindrome: ")
cleaned = test_str.lower()  # case-insensitive
if cleaned == cleaned[::-1]:
    print(f"'{test_str}' is a palindrome.")
else:
    print(f"'{test_str}' is not a palindrome.")
```

## Sample Output

```
str1: Hello
str2: World
str3: This is a
multiline string.

String: Python
First character (text[0]): P
Third character (text[2]): t
Last character (text[-1]): n
Second last (text[-2]): o

String: Programming
s[0:4]: Prog
s[3:8]: gramm
s[:6]: Progra
s[4:]: amming
s[::2]: Pormig

Original: Python
Reversed: nohtyP
Enter a string to check palindrome: racecar
'racecar' is a palindrome.
```

## Homework

1. Write a program that extracts and prints every alternate character from a given string (starting from index 0).
2. Write a program that takes a string and prints the first half and second half separately.
3. Write a program that counts the number of vowels (a, e, i, o, u) in a user-input string using slicing and iteration.
