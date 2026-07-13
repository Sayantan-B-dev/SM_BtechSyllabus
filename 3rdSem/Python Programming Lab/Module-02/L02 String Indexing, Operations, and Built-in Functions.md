# String Indexing, Operations, and Built-in Functions

**Course:** Python Programming Lab  
**Module:** 2 | **Lecture:** 2  
**Date:** 07-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Use built-in string methods: upper(), lower(), split(), join(), replace(), strip().
- Write a program to capitalize sentences properly.
- Parse comma-separated values (CSV) using split() and strip().

## Theory

Python strings have numerous built-in methods that return new strings (since strings are immutable). Common case conversion methods: upper() converts to uppercase, lower() converts to lowercase, capitalize() capitalizes the first character, title() capitalizes the first letter of each word, and swapcase() swaps case.

The split() method breaks a string into a list of substrings based on a delimiter. By default, it splits on whitespace. The join() method is the inverse: it concatenates a list of strings using a specified separator. The replace() method replaces all occurrences of a substring with another. The strip() method removes leading and trailing whitespace (or specified characters); lstrip() and rstrip() remove from the left or right only.

These methods are essential for text processing tasks like cleaning user input, parsing data files, and formatting text output. For CSV parsing, split(",") separates fields, and strip() can remove extra whitespace around each field.

## Procedure

1. Create a new Python file named lab10.py.
2. Demonstrate upper(), lower(), title(), and swapcase() on a sample string.
3. Use split() to break a sentence into words and join() to rebuild with hyphens.
4. Use replace() to substitute a word in a sentence.
5. Use strip() to clean messy input with extra spaces.
6. Write a program that takes a sentence and capitalizes the first letter of each word.
7. Write a CSV parsing program that splits on commas and strips whitespace from each field.
8. Test all programs.

## Source Code

```python
# Module 02 Lab 02: String Methods - upper, lower, split, join, replace, strip

text = "  hello World! Python is Fun.  "

# Case conversion methods
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"swapcase(): '{text.swapcase()}'")

# strip whitespace
clean = text.strip()
print(f"\nstrip(): '{clean}'")

# split and join
sentence = "Python is a powerful language"
words = sentence.split()
print(f"\nOriginal: '{sentence}'")
print(f"split(): {words}")

hyphenated = "-".join(words)
print(f"join() with '-': '{hyphenated}'")

# replace
original = "I like apples. Apples are tasty."
replaced = original.replace("apples", "oranges")
print(f"\nOriginal: '{original}'")
print(f"replace('apples','oranges'): '{replaced}'")
print(f"case-sensitive replace: '{original.replace('Apples', 'Oranges')}'")

# Sentence capitalizer: capitalize first letter of each word
s = input("\nEnter a sentence: ")
capitalized = s.title()
print(f"Title-cased: {capitalized}")

# CSV parsing
csv_line = "  Alice , 25 , New York , Student "
fields = csv_line.split(",")
print(f"\nRaw CSV split: {fields}")
cleaned_fields = [f.strip() for f in fields]
print(f"Cleaned fields: {cleaned_fields}")
```

## Sample Output

```
Original: '  hello World! Python is Fun.  '
upper(): '  HELLO WORLD! PYTHON IS FUN.  '
lower(): '  hello world! python is fun.  '
title(): '  Hello World! Python Is Fun.  '
swapcase(): '  HELLO wORLD! pYTHON IS fUN.  '

strip(): 'hello World! Python is Fun.'

Original: 'Python is a powerful language'
split(): ['Python', 'is', 'a', 'powerful', 'language']
join() with '-': 'Python-is-a-powerful-language'

Original: 'I like apples. Apples are tasty.'
replace('apples','oranges'): 'I like oranges. Apples are tasty.'
case-sensitive replace: 'I like apples. Oranges are tasty.'

Enter a sentence: hello world! python programming.
Title-cased: Hello World! Python Programming.

Raw CSV split: ['  Alice ', ' 25 ', ' New York ', ' Student ']
Cleaned fields: ['Alice', '25', 'New York', 'Student']
```

## Homework

1. Write a program that takes a full name (first middle last) and prints the initials in uppercase with dots (e.g., "john fitzgerald kennedy" -> "J.F.K").
2. Write a program that replaces all spaces in a sentence with underscores and converts the result to lowercase (for creating URL slugs).
3. Write a program that takes a paragraph of text and counts how many sentences it contains (split on '.' and count non-empty parts).
