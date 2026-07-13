# String Operations

**Course:** Python Programming  
**Module:** 2 | **Lecture:** 2  
**Date:** 03-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 105-142

## Concatenation (+)

The `+` operator joins two or more strings together to form a new string.

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)          # Output: John Doe

# Concatenating multiple strings
result = "Python" + " " + "Programming" + " " + "Language"
print(result)             # Output: Python Programming Language

# Concatenation creates a new string (immutability)
a = "Hello"
b = "World"
c = a + b
print(c)                  # Output: HelloWorld
print(id(a))              # Different memory address
print(id(b))              # Different memory address
print(id(c))              # Different memory address
```

### Concatenating Different Types (Causes Error)

```python
# print("Age: " + 25)     # TypeError: can only concatenate str (not "int") to str
# Fix: convert to string first
print("Age: " + str(25))  # Output: Age: 25
```

### Using += Operator

The `+=` operator appends to an existing string (actually creates a new string and reassigns).

```python
msg = "Hello"
msg += " World"
print(msg)                # Output: Hello World

msg += "!"
print(msg)                # Output: Hello World!
```

## Repetition (*)

The `*` operator repeats a string a specified number of times.

```python
star = "*"
print(star * 10)          # Output: **********

word = "Hi "
print(word * 3)           # Output: Hi Hi Hi

# Creating patterns
line = "-" * 40
print(line)               # Output: ----------------------------------------

# Repetition with concatenation
pattern = ("*" * 5) + " " + ("-" * 5)
print(pattern)            # Output: ***** -----

# Repeating a multi-character string
print("AB" * 4)           # Output: ABABABAB
```

### Repetition with Variables

```python
n = 5
symbol = "#"
print(symbol * n)         # Output: #####

# Building a simple bar chart
values = [3, 7, 2, 9]
for v in values:
    print("#" * v)
# Output:
# ###
# #######
# ##
# #########
```

## Membership Test (in, not in)

The `in` operator checks whether a substring exists within a string. It returns `True` or `False`. The `not in` operator is the logical opposite.

```python
text = "Python Programming is Fun"

# Using 'in'
print("Python" in text)       # Output: True
print("Java" in text)         # Output: False
print("gram" in text)         # Output: True
print(" " in text)            # Output: True (space is a character)

# Using 'not in'
print("Java" not in text)     # Output: True
print("Python" not in text)   # Output: False
```

### Practical Uses of Membership Test

```python
# Checking user input
password = "SecurePass123"
if " " in password:
    print("Password cannot contain spaces")

# Validating email
email = "user@example.com"
if "@" in email and "." in email:
    print("Valid email format")

# Filtering words
words = ["apple", "banana", "grape", "avocado"]
a_words = [w for w in words if "a" in w]
print(a_words)                # Output: ['apple', 'banana', 'grape', 'avocado']
```

### Single Character Check

```python
char = input("Enter a character: ")
if char in "aeiouAEIOU":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")
```

## Comparison Operators on Strings (Lexicographic Comparison)

Python compares strings lexicographically (dictionary order) based on the **Unicode code point** of each character.

### How Comparison Works

- Compare the first character of each string.
- If they differ, that comparison determines the result.
- If they are equal, move to the next character.
- If all characters match, the strings are equal.
- If one string is a prefix of the other, the shorter string is "less than" the longer one.

```python
# Basic comparisons
print("apple" == "apple")     # Output: True
print("apple" != "banana")    # Output: True
print("apple" < "banana")     # Output: True (a comes before b)
print("apple" > "banana")     # Output: False
print("apple" <= "apple")     # Output: True

# Case sensitivity (uppercase letters have lower Unicode values)
print("Apple" < "apple")      # Output: True (A=65, a=97)
print("Z" < "a")              # Output: True (Z=90, a=97)

# Comparing character by character
print("abc" < "abd")          # Output: True (c < d)
print("abc" < "abcd")         # Output: True (shorter is less)
print("abcd" > "abc")         # Output: True (longer is greater)
```

### Unicode Code Point Values

```python
print(ord("A"))   # Output: 65
print(ord("a"))   # Output: 97
print(ord("0"))   # Output: 48
print(ord(" "))   # Output: 32
```

### Sorting Strings (Uses Lexicographic Comparison)

```python
fruits = ["banana", "Apple", "cherry", "apple"]
fruits.sort()
print(fruits)      # Output: ['Apple', 'apple', 'banana', 'cherry']
# 'A' (65) comes before 'a' (97)
```

To sort case-insensitively:

```python
fruits = ["banana", "Apple", "cherry", "apple"]
fruits.sort(key=str.lower)
print(fruits)      # Output: ['Apple', 'apple', 'banana', 'cherry']
```

### Practical Comparisons

```python
# Version comparison
v1 = "2.10.3"
v2 = "2.9.1"
print(v1 > v2)     # Output: False (because '1' < '9' at position 2)

# String comparison in conditions
name = "Alice"
if name < "Bob":
    print(f"{name} comes before Bob")
```

## Raw Strings (r"...")

Raw strings treat backslashes as literal characters rather than escape sequences. They are prefixed with `r` or `R`.

```python
# Without raw string (backslash is interpreted)
path = "C:\Users\Name"
print(path)              # Output: C:\Users\Name (but \U and \N may cause errors)

# Raw string (backslash is literal)
path = r"C:\Users\Name"
print(path)              # Output: C:\Users\Name

# Useful for regular expressions
import re
pattern = r"\d{3}-\d{4}"   # Raw string prevents escaping issues
print(pattern)             # Output: \d{3}-\d{4}
```

### Raw Strings vs Normal Strings

```python
# Normal string - escape sequences are processed
s1 = "Hello\nWorld"
print(s1)
# Output:
# Hello
# World

# Raw string - backslash is literal
s2 = r"Hello\nWorld"
print(s2)                # Output: Hello\nWorld
```

### Common Use Cases for Raw Strings

```python
# File paths on Windows
file_path = r"C:\Users\John\Documents\file.txt"

# Regular expressions (avoid double escaping)
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# LaTeX strings
latex = r"\frac{1}{2}"

# Any string with many backslashes
error_msg = r"Don't use \n or \t in raw strings - they are literal"
```

### Limitation of Raw Strings

A raw string cannot end with an odd number of backslashes because the backslash would escape the closing quote.

```python
# This causes an error
# s = r"Hello\"     # SyntaxError

# Workaround: concatenate
s = r"Hello" "\\"
print(s)                # Output: Hello\
```

## Escape Sequences

Escape sequences allow inserting special characters into strings. They start with a backslash (`\`).

### Common Escape Sequences

| Escape Sequence | Description        | Example                          | Output                      |
|-----------------|--------------------|----------------------------------|-----------------------------|
| `\n`            | Newline            | `print("Line1\nLine2")`          | Line1 (newline) Line2       |
| `\t`            | Tab                | `print("Col1\tCol2")`            | Col1    Col2                |
| `\'`            | Single quote       | `print('It\'s fine')`            | It's fine                   |
| `\"`            | Double quote       | `print("She said \"Hi\"")`       | She said "Hi"               |
| `\\`            | Backslash          | `print("Path: C:\\Users")`       | Path: C:\Users              |
| `\r`            | Carriage return    | `print("Hello\rWorld")`          | World                       |
| `\b`            | Backspace          | `print("Hello\bWorld")`          | HellWorld                   |
| `\a`            | Bell (alert)       | `print("\a")`                    | (system bell sound)         |
| `\0`            | Null character     | `print("Null\0char")`            | Null char                   |

### Examples of Each Escape Sequence

```python
# Newline
print("First Line\nSecond Line\nThird Line")
# Output:
# First Line
# Second Line
# Third Line

# Tab
print("Name\tAge\tCity")
print("Alice\t25\tNYC")
print("Bob\t30\tLA")
# Output:
# Name    Age    City
# Alice  25     NYC
# Bob    30     LA

# Single quote inside single-quoted string
print('It\'s a beautiful day')   # Output: It's a beautiful day

# Double quotes inside double-quoted string
print("She said, \"Hello!\"")     # Output: She said, "Hello!"

# Backslash
print("C:\\Users\\John")         # Output: C:\Users\John

# Carriage return (overwrites from beginning of line)
print("12345\rABCDE")            # Output: ABCDE

# Backspace
print("Hello\b\bWorld")          # Output: HelWorld (removes 'l', 'o')
```

### Escape Sequences in Action

```python
# Creating formatted output
print("Item\t\tPrice\t\tQty")
print("----\t\t-----\t\t---")
print("Apple\t\t$1.50\t\t10")
print("Banana\t\t$0.75\t\t20")

# Using triple quotes with escapes
poem = """Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you."""
print(poem)
```

### Unicode Escape Sequences

Python supports Unicode escapes using `\u` (16-bit) and `\U` (32-bit).

```python
# Unicode escapes
print("\u0041")                # Output: A (Latin A)
print("\u03A9")                # Output: Omega symbol
print("\U0001F600")            # Output: (grinning face emoji, 32-bit)

# Named Unicode escape
print("\N{LATIN SMALL LETTER A}")   # Output: a
```

### Combining Escape Sequences

```python
# Multiple escape sequences in one string
output = "Name:\tJohn\nAge:\t25\nCity:\tNYC\n"
print(output)
# Output:
# Name:   John
# Age:    25
# City:   NYC
```

## Practice Problems

1. **String Repetition Pattern**: Write a program that takes a word and a number `n` from the user, and prints the word repeated `n` times, separated by hyphens.

   **Hint**: Use `(word + "-") * (n-1) + word`.

   **Answer**:
   ```python
   word = input("Enter a word: ")
   n = int(input("Enter a number: "))
   result = (word + "-") * (n - 1) + word
   print(result)
   ```

2. **Vowel Checker**: Write a program that takes a character from the user and checks if it is a vowel using the `in` operator.

   **Answer**:
   ```python
   ch = input("Enter a character: ").lower()
   if ch in "aeiou":
       print(f"{ch} is a vowel")
   else:
       print(f"{ch} is not a vowel")
   ```

3. **Lexicographic Sorter**: Write a program that takes three words and prints them in alphabetical order using comparison operators.

   **Hint**: Use a series of `if-elif-else` comparisons.

   **Answer**:
   ```python
   w1 = input("Word 1: ")
   w2 = input("Word 2: ")
   w3 = input("Word 3: ")
   words = [w1, w2, w3]
   words.sort()
   print("Sorted:", words[0], words[1], words[2])
   ```

4. **Escape Sequence Table**: Write a program that uses tab (`\t`) and newline (`\n`) escape sequences to print a formatted table of escape sequences themselves.

   **Answer**:
   ```python
   print("Sequence\tName\t\t\tExample")
   print("--------\t----\t\t\t-------")
   print("\\\\n\t\tNewline\t\t\tprint(\"A\\nB\")")
   print("\\\\t\t\tTab\t\t\tprint(\"A\\tB\")")
   print("\\\\\\\\\t\tBackslash\t\tprint(\"C:\\\\\\\\Users\")")
   ```

5. **File Path Converter**: Write a program that converts a Windows file path entered with forward slashes (e.g., "C:/Users/Name") to a raw string with backslashes.

   **Hint**: Use `replace("/", "\\")` and prepend `r`.

   **Answer**:
   ```python
   path = input("Enter path with forward slashes: ")
   converted = path.replace("/", "\\")
   print(f"Windows path: {converted}")
   print(f"Raw string: r\"{converted}\"")
   ```
