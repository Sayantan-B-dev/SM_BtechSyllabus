# String Operations

**Course:** Python Programming  
**Module:** 2 | **Lecture:** 3  
**Date:** 03-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 105-142

## Case Conversion Methods

These methods return a new string with the case of characters changed. The original string remains unchanged.

### upper()

Converts all lowercase characters to uppercase.

```python
text = "Hello World"
print(text.upper())        # Output: HELLO WORLD

text2 = "python 3.10"
print(text2.upper())       # Output: PYTHON 3.10
```

### lower()

Converts all uppercase characters to lowercase.

```python
text = "Hello World"
print(text.lower())        # Output: hello world

text2 = "PYTHON 3.10"
print(text2.lower())       # Output: python 3.10
```

### title()

Converts the first character of each word to uppercase and the rest to lowercase.

```python
text = "hello world from python"
print(text.title())        # Output: Hello World From Python

text2 = "hELLO wORLD"
print(text2.title())       # Output: Hello World
```

### capitalize()

Converts the first character of the string to uppercase and the rest to lowercase.

```python
text = "hello WORLD"
print(text.capitalize())   # Output: Hello world

text2 = "python is FUN"
print(text2.capitalize())  # Output: Python is fun
```

### swapcase()

Swaps uppercase characters to lowercase and vice versa.

```python
text = "Hello World"
print(text.swapcase())     # Output: hELLO wORLD

text2 = "Python 3.10"
print(text2.swapcase())    # Output: pYTHON 3.10
```

### Practical Case-Insensitive Comparison

```python
user_input = "Yes"
if user_input.lower() == "yes":
    print("User confirmed")

# Sorting case-insensitively
names = ["alice", "Bob", "Charlie", "david"]
names.sort(key=str.lower)
print(names)               # Output: ['alice', 'Bob', 'Charlie', 'david']
```

## Stripping Whitespace Methods

These methods remove whitespace characters (spaces, tabs, newlines) from strings.

### strip()

Removes leading and trailing whitespace.

```python
text = "   Hello World   "
print(f"'{text.strip()}'")        # Output: 'Hello World'

text2 = "\t\n  Python  \n\t"
print(text2.strip())             # Output: Python
```

### lstrip()

Removes leading (left) whitespace only.

```python
text = "   Hello World   "
print(f"'{text.lstrip()}'")      # Output: 'Hello World   '
```

### rstrip()

Removes trailing (right) whitespace only.

```python
text = "   Hello World   "
print(f"'{text.rstrip()}'")      # Output: '   Hello World'
```

### Stripping Specific Characters

All three methods accept an optional argument to specify which characters to remove.

```python
# Removing specific characters
url = "www.python.org"
print(url.strip("w"))            # Output: .python.org
print(url.strip("w."))           # Output: python.org

# Stripping punctuation
text = "...Hello..."
print(text.strip("."))           # Output: Hello

# Stripping from both sides
phone = "+1-555-1234"
print(phone.strip("+1-"))        # Output: 555-1234
```

### Practical Data Cleaning

```python
# Cleaning user input
user_name = "  John  Doe  \n"
cleaned = user_name.strip()
print(f"'{cleaned}'")            # Output: 'John  Doe'

# Cleaning CSV-like data
data = "  apple , banana , cherry "
items = [item.strip() for item in data.split(",")]
print(items)                     # Output: ['apple', 'banana', 'cherry']
```

## split() and join() Methods

### split()

Splits a string into a list of substrings based on a delimiter.

```python
# Default split (whitespace)
text = "Python is fun"
words = text.split()
print(words)                     # Output: ['Python', 'is', 'fun']

# Split with specific delimiter
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)                    # Output: ['apple', 'banana', 'cherry']

# Split with limit (maxsplit)
text = "one two three four"
print(text.split(" ", 2))        # Output: ['one', 'two', 'three four']

# Splitting on newlines
multiline = "Line1\nLine2\nLine3"
print(multiline.split("\n"))     # Output: ['Line1', 'Line2', 'Line3']

# Splitting on multiple spaces
text = "Python    is    fun"
print(text.split())              # Output: ['Python', 'is', 'fun']
```

### join()

Joins a list of strings into a single string using a separator.

```python
# Joining with a space
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)                  # Output: Python is fun

# Joining with a comma
fruits = ["apple", "banana", "cherry"]
csv = ",".join(fruits)
print(csv)                       # Output: apple,banana,cherry

# Joining with newlines
lines = ["Line 1", "Line 2", "Line 3"]
output = "\n".join(lines)
print(output)
# Output:
# Line 1
# Line 2
# Line 3

# Joining an empty list
empty = "->".join([])
print(f"'{empty}'")              # Output: ''

# Joining characters of a string
chars = list("Python")
print("|".join(chars))           # Output: P|y|t|h|o|n
```

### Practical split and join

```python
# CSV parsing
csv_line = "John,Doe,30,New York"
fields = csv_line.split(",")
print(fields)                    # Output: ['John', 'Doe', '30', 'New York']

# Removing extra spaces from a sentence
sentence = "Python    is   a   great   language"
cleaned = " ".join(sentence.split())
print(cleaned)                   # Output: Python is a great language

# Reversing words in a sentence
sentence = "Hello World Python"
reversed_words = " ".join(sentence.split()[::-1])
print(reversed_words)            # Output: Python World Hello
```

## replace()

Replaces all occurrences of a substring with another substring.

```python
text = "Hello World"
print(text.replace("World", "Python"))   # Output: Hello Python

# Replacing multiple occurrences
text = "apple apple banana apple"
print(text.replace("apple", "orange"))   # Output: orange orange banana orange

# Limiting replacements (count parameter)
text = "one one one one"
print(text.replace("one", "two", 2))     # Output: two two one one

# Removing characters (replace with empty string)
text = "Hello123World456"
print(text.replace("123", ""))           # Output: HelloWorld456
```

### Chaining replace Calls

```python
# Removing multiple characters
text = "Hello, World! How are you?"
cleaned = text.replace(",", "").replace("!", "").replace("?", "")
print(cleaned)                    # Output: Hello World How are you

# HTML tag removal (simple)
html = "<p>Hello</p><b>World</b>"
clean = html.replace("<p>", "").replace("</p>", "").replace("<b>", "").replace("</b>", "")
print(clean)                      # Output: HelloWorld
```

## find() and index() Methods

Both methods search for a substring and return its starting index. `find()` returns -1 if not found, while `index()` raises a ValueError.

### find()

Returns the lowest index where the substring is found, or -1 if not found.

```python
text = "Python Programming Language"

print(text.find("Programming"))   # Output: 7
print(text.find("Java"))          # Output: -1 (not found)
print(text.find("o"))             # Output: 4 (first occurrence)

# With start and end parameters
print(text.find("o", 5))          # Output: 15 (search from index 5)
print(text.find("o", 5, 10))      # Output: -1 (search between index 5 and 10)
```

### rfind()

Returns the highest index where the substring is found (searching from right).

```python
text = "Python Programming Language"
print(text.rfind("o"))            # Output: 15 (last occurrence)
print(text.rfind("Python"))       # Output: 0
print(text.rfind("Java"))         # Output: -1
```

### index()

Same as `find()`, but raises ValueError if the substring is not found.

```python
text = "Python Programming"

print(text.index("Programming"))  # Output: 7

# print(text.index("Java"))       # ValueError: substring not found

# Safer to use try-except
try:
    pos = text.index("Java")
except ValueError:
    pos = -1
print(pos)                        # Output: -1
```

### rindex()

Same as `rfind()`, but raises ValueError if not found.

```python
text = "Python Programming Language"
print(text.rindex("o"))           # Output: 15
# print(text.rindex("Java"))      # ValueError
```

## startswith() and endswith() Methods

These methods check if a string starts or ends with a specified substring.

### startswith()

Returns `True` if the string starts with the given prefix.

```python
text = "Python Programming"

print(text.startswith("Python"))      # Output: True
print(text.startswith("Java"))        # Output: False
print(text.startswith("Prog"))        # Output: False

# Using a tuple of prefixes
print(text.startswith(("Py", "Ja")))  # Output: True
print(text.startswith(("Java", "C"))) # Output: False

# With start and end parameters
print(text.startswith("Prog", 7))     # Output: True (check from index 7)
```

### endswith()

Returns `True` if the string ends with the given suffix.

```python
text = "python.txt"

print(text.endswith(".txt"))          # Output: True
print(text.endswith(".py"))           # Output: False

# Using a tuple of suffixes
print(text.endswith((".txt", ".md")))    # Output: True
print(text.endswith((".py", ".java")))   # Output: False

# Practical file checking
filename = "report.csv"
if filename.endswith(".csv"):
    print("CSV file detected")

# Checking multiple file extensions
if filename.endswith((".csv", ".xlsx", ".json")):
    print("Data file detected")
```

### Practical Uses

```python
# URL validation
url = "https://example.com"
if url.startswith(("http://", "https://")):
    print("Valid URL scheme")

# File extension filtering
files = ["doc.txt", "image.png", "script.py", "data.csv"]
text_files = [f for f in files if f.endswith(".txt")]
print(text_files)                   # Output: ['doc.txt']

# String prefix check in data processing
sentence = "The quick brown fox"
if sentence.startswith("The"):
    print("Starts with 'The'")
```

## isalpha(), isdigit(), isalnum(), isspace() Methods

These methods check the character content of a string and return boolean values.

### isalpha()

Returns `True` if all characters are alphabetic (a-z, A-Z) and the string is not empty.

```python
print("Hello".isalpha())        # Output: True
print("Hello123".isalpha())     # Output: False
print("".isalpha())             # Output: False (empty string)
print("Hello World".isalpha())  # Output: False (space is not alphabetic)
```

### isdigit()

Returns `True` if all characters are digits (0-9) and the string is not empty.

```python
print("12345".isdigit())        # Output: True
print("123abc".isdigit())       # Output: False
print("12.34".isdigit())        # Output: False (dot is not a digit)
print("".isdigit())             # Output: False
print("  123".isdigit())        # Output: False
```

### isalnum()

Returns `True` if all characters are alphanumeric (letters or digits) and the string is not empty.

```python
print("Hello123".isalnum())     # Output: True
print("Hello".isalnum())        # Output: True
print("123".isalnum())          # Output: True
print("Hello 123".isalnum())    # Output: False (space)
print("Hello!".isalnum())       # Output: False (exclamation)
```

### isspace()

Returns `True` if all characters are whitespace characters.

```python
print("   ".isspace())          # Output: True
print("".isspace())             # Output: False (empty string)
print(" \t\n".isspace())        # Output: True (space, tab, newline)
print(" a ".isspace())          # Output: False ('a' is not whitespace)
```

### Additional is* Methods

```python
print("Hello".isupper())        # Output: False
print("HELLO".isupper())        # Output: True
print("hello".islower())        # Output: True
print("Hello World".istitle())  # Output: True
print("hello world".istitle())  # Output: False
print("123".isnumeric())        # Output: True
print("IIX".isdecimal())        # Output: False
print("abc".isascii())          # Output: True
```

### Practical Validation Examples

```python
# Password validation
password = "Pass123"
if password.isalnum() and len(password) >= 6:
    print("Valid password")

# Input type detection
user_input = input("Enter something: ")
if user_input.isdigit():
    print(f"You entered a number: {user_input}")
elif user_input.isalpha():
    print(f"You entered a word: {user_input}")
elif user_input.isalnum():
    print("You entered alphanumeric text")
else:
    print("Input contains special characters")

# Data cleaning
data = ["123", "abc", "456def", "!@#"]
numbers = [x for x in data if x.isdigit()]
words = [x for x in data if x.isalpha()]
print(numbers)    # Output: ['123']
print(words)      # Output: ['abc']
```

## count()

Returns the number of non-overlapping occurrences of a substring in a string.

```python
text = "banana"
print(text.count("a"))      # Output: 3
print(text.count("an"))     # Output: 2
print(text.count("ana"))    # Output: 1 (non-overlapping)
print(text.count("x"))      # Output: 0

# With start and end parameters
text = "Hello World Hello"
print(text.count("Hello"))                # Output: 2
print(text.count("Hello", 6))             # Output: 1 (search from index 6)
print(text.count("Hello", 0, 5))          # Output: 1 (search within first 5 chars)
```

### Practical Uses of count()

```python
# Counting words in a sentence
sentence = "the cat and the dog and the bird"
print(sentence.count("the"))    # Output: 3

# Counting vowels
text = "Python Programming"
vowels = sum(1 for ch in text.lower() if ch in "aeiou")
print(vowels)                   # Output: 4

# Character frequency analysis
text = "mississippi"
for ch in set(text):
    print(f"{ch}: {text.count(ch)}")
# Output:
# m: 1
# p: 2
# s: 4
# i: 4
```

## Practice Problems

1. **Password Validator**: Write a program that checks if a password is valid:
   - At least 8 characters long
   - Contains at least one uppercase letter
   - Contains at least one lowercase letter
   - Contains at least one digit
   - Contains at least one special character (non-alphanumeric)

   **Hint**: Use `isupper()`, `islower()`, `isdigit()`, `isalnum()` methods.

   **Answer**:
   ```python
   password = input("Enter password: ")
   has_upper = any(c.isupper() for c in password)
   has_lower = any(c.islower() for c in password)
   has_digit = any(c.isdigit() for c in password)
   has_special = any(not c.isalnum() for c in password)
   if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
       print("Strong password!")
   else:
       print("Weak password. Improve it.")
   ```

2. **Word Frequency Counter**: Write a program that takes a sentence and counts how many times each word appears using `split()` and `count()`.

   **Answer**:
   ```python
   sentence = input("Enter a sentence: ")
   words = sentence.split()
   seen = []
   for word in words:
       if word.lower() not in seen:
           seen.append(word.lower())
           print(f"'{word}': {words.count(word)}")
   ```

3. **Data Cleaner**: Write a program that takes a string with extra spaces, punctuation, and inconsistent casing, and normalizes it: lowercase, remove leading/trailing spaces, replace multiple spaces with one, and remove punctuation.

   **Hint**: Use `strip()`, `lower()`, `replace()` for punctuation, and `split()`/`join()` for extra spaces.

   **Answer**:
   ```python
   text = input("Enter messy text: ")
   text = text.strip().lower()
   for p in ".,!?;:-":
       text = text.replace(p, "")
   cleaned = " ".join(text.split())
   print("Cleaned:", cleaned)
   ```

4. **File Extension Checker**: Write a program that takes a filename and determines its type (image, document, video, or unknown) using `endswith()`.

   **Answer**:
   ```python
   filename = input("Enter filename: ").lower()
   if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
       print("Image file")
   elif filename.endswith((".pdf", ".doc", ".docx", ".txt")):
       print("Document file")
   elif filename.endswith((".mp4", ".avi", ".mkv", ".mov")):
       print("Video file")
   else:
       print("Unknown file type")
   ```

5. **String Analyzer**: Write a program that analyzes a string and prints:
   - Number of uppercase letters
   - Number of lowercase letters
   - Number of digits
   - Number of whitespace characters
   - Number of special characters

   **Hint**: Use `isupper()`, `islower()`, `isdigit()`, `isspace()` in a loop.

   **Answer**:
   ```python
   text = input("Enter a string: ")
   upper = lower = digit = space = special = 0
   for ch in text:
       if ch.isupper():
           upper += 1
       elif ch.islower():
           lower += 1
       elif ch.isdigit():
           digit += 1
       elif ch.isspace():
           space += 1
       else:
           special += 1
   print(f"Uppercase: {upper}")
   print(f"Lowercase: {lower}")
   print(f"Digits: {digit}")
   print(f"Spaces: {space}")
   print(f"Special: {special}")
   ```
