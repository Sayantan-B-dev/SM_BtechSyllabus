# String Functions and Methods

**Course:** Python Programming  
**Module:** 2 | **Lecture:** 6  
**Date:** 10-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 105-142

## expandtabs(tabsize)

Replaces tab characters (`\t`) with spaces. The `tabsize` parameter specifies the number of spaces per tab (default is 8).

```python
text = "Col1\tCol2\tCol3"
print(text)
# Output: Col1    Col2    Col3 (with default 8-space tabs)

# Custom tab size
print(text.expandtabs(4))
# Output: Col1 Col2 Col3 (with 4-space tabs)

print(text.expandtabs(10))
# Output: Col1      Col2      Col3 (with 10-space tabs)

# Practical: normalizing tab-separated data
data = "Name\tAge\tCity\nAlice\t25\tNYC\nBob\t30\tLA"
print(data.expandtabs(15))
# Output:
# Name          Age           City
# Alice         25            NYC
# Bob           30            LA
```

### Tab Expansion with Different Widths

```python
lines = [
    "a\tb\tc",
    "aa\tbb\tcc",
    "aaa\tbbb\tccc"
]
for line in lines:
    expanded = line.expandtabs(8)
    print(f"'{expanded}'")
# Output:
# 'a       b       c'
# 'aa      bb      cc'
# 'aaa     bbb     ccc'
```

## casefold()

Similar to `lower()`, but more aggressive. Designed for case-insensitive matching, especially for Unicode characters where `lower()` may not be sufficient.

```python
# German sharp s (eszett)
text = "STRASSE"
print(text.lower())          # Output: strasse
print(text.casefold())       # Output: strasse

# Greek letters
greek = "ΜΆΡΚΟΣ"
print(greek.lower())         # Output: μάρκοσ
print(greek.casefold())      # Output: μαρκοσ (removes accents)

# Comparison example
s1 = "straße"
s2 = "STRASSE"
print(s1.lower() == s2.lower())          # Output: False
print(s1.casefold() == s2.casefold())    # Output: True

# When to use casefold() vs lower()
text1 = "Hello"
text2 = "HELLO"
print(text1.lower() == text2.lower())          # Output: True
print(text1.casefold() == text2.casefold())    # Output: True
# For most English text, they work the same
```

## format_map()

Similar to `format(**dict)`, but takes a single mapping object (like a dictionary) directly.

```python
# Using format_map with a dictionary
data = {"name": "Alice", "age": 25, "city": "NYC"}
template = "{name} is {age} years old and lives in {city}"
print(template.format_map(data))
# Output: Alice is 25 years old and lives in NYC

# format_map vs format
print(template.format(**data))       # Same output

# format_map with missing keys (raises KeyError)
# print("{name} {country}".format_map(data))  # KeyError: 'country'
```

### Using format_map with DefaultDict

```python
from collections import defaultdict

# Safely handle missing keys
class DefaultDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"

data = DefaultDict(name="Alice", age=25)
template = "{name} is {age} years old from {city}"
print(template.format_map(data))
# Output: Alice is 25 years old from {city}
```

### Practical: Template Engine

```python
email_template = """
Dear {name},

Thank you for your interest in {product}.
Your order #{order_id} has been confirmed.
Expected delivery: {delivery_date}.

Best regards,
{company}
"""

customer_data = {
    "name": "John Doe",
    "product": "Python Programming Course",
    "order_id": "ORD-2026-0842",
    "delivery_date": "August 15, 2026",
    "company": "TechEd Inc."
}
print(email_template.format_map(customer_data))
```

## f-Strings (Formatted String Literals)

Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions inside string literals.

### Basic f-String Syntax

```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")
# Output: Alice is 25 years old

# Expressions inside f-strings
print(f"{name.upper()} will be {age + 5} in 5 years")
# Output: ALICE will be 30 in 5 years
```

### Format Specifiers in f-Strings

```python
# Numbers
pi = 3.14159265
print(f"Pi rounded: {pi:.2f}")           # Output: Pi rounded: 3.14
print(f"Pi padded: {pi:10.3f}")          # Output: Pi padded:     3.142

# Alignment
name = "Python"
print(f"{name:<15}left")                 # Output: Python         left
print(f"{name:>15}right")                # Output:         Python right
print(f"{name:^15}center")               # Output:    Python     center
print(f"{name:*^15}fill")                # Output: ****Python****

# Numbers formatting
number = 1234567.89
print(f"{number:,.2f}")                  # Output: 1,234,567.89
print(f"{number:,.0f}")                  # Output: 1,234,568
```

### Using Variables and Expressions

```python
# Arithmetic expressions
a, b = 10, 3
print(f"{a} + {b} = {a + b}")            # Output: 10 + 3 = 13
print(f"{a} / {b} = {a / b:.2f}")        # Output: 10 / 3 = 3.33

# Method calls
text = "hello world"
print(f"{text.upper()}")                 # Output: HELLO WORLD
print(f"{text.title()}")                 # Output: Hello World

# Conditional expressions
score = 85
print(f"Grade: {'Pass' if score >= 50 else 'Fail'}")
# Output: Grade: Pass
```

### f-Strings with Strings (String-Specific Examples)

```python
# String methods inside f-strings
word = "python"
print(f"Original: {word}")
print(f"Upper: {word.upper()}")
print(f"Capitalized: {word.capitalize()}")
print(f"Reversed: {word[::-1]}")
print(f"Length: {len(word)}")
print(f"Count of 'p': {word.count('p')}")

# Slicing inside f-strings
text = "Python Programming"
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[-11:]}")
print(f"Reversed: {text[::-1]}")

# Multiple f-strings for table
print(f"{'Name':<10} {'Score':<10}")
print(f"{'Alice':<10} {95:<10}")
print(f"{'Bob':<10} {87:<10}")

# Debug mode (Python 3.8+)
name = "Python"
version = 3.10
print(f"{name=}, {version=}")
# Output: name='Python', version=3.10
```

### f-Strings with Dictionaries

```python
data = {"name": "Bob", "job": "developer"}
print(f"{data['name']} works as a {data['job']}")
# Output: Bob works as a developer

# Note: use single quotes inside the f-string if using double quotes
# Or double quotes inside if using single quotes
```

### Multiline f-Strings

```python
name = "Alice"
age = 25
city = "NYC"

info = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"City: {city}"
)
print(info)
# Output:
# Name: Alice
# Age: 25
# City: NYC

# Alternative with triple quotes
info2 = f"""Name: {name}
Age: {age}
City: {city}"""
```

### Performance Comparison

```python
import time

name = "Alice"
age = 25

# Concatenation
start = time.perf_counter()
for _ in range(100000):
    s = name + " is " + str(age) + " years old"
concat_time = time.perf_counter() - start

# format()
start = time.perf_counter()
for _ in range(100000):
    s = "{} is {} years old".format(name, age)
format_time = time.perf_counter() - start

# f-string
start = time.perf_counter()
for _ in range(100000):
    s = f"{name} is {age} years old"
fstring_time = time.perf_counter() - start

print(f"Concatenation: {concat_time:.4f}s")
print(f"format(): {format_time:.4f}s")
print(f"f-string: {fstring_time:.4f}s")
# f-strings are typically the fastest
```

## ord() and chr() - ASCII and Unicode

### ord(character)

Returns the Unicode code point (integer) of a single character.

```python
print(ord("A"))          # Output: 65
print(ord("a"))          # Output: 97
print(ord("0"))          # Output: 48
print(ord(" "))          # Output: 32
print(ord("$"))          # Output: 36
print(ord("\n"))         # Output: 10

# Unicode characters
print(ord("!"))          # Output: 33
print(ord("~"))          # Output: 126
```

### chr(code_point)

Returns the character corresponding to the given Unicode code point.

```python
print(chr(65))           # Output: A
print(chr(97))           # Output: a
print(chr(48))           # Output: 0
print(chr(32))           # Output: ' '
print(chr(36))           # Output: $
```

### Practical Uses of ord() and chr()

```python
# Generating the alphabet
uppercase = [chr(i) for i in range(65, 91)]
print(uppercase)
# Output: ['A', 'B', 'C', ..., 'X', 'Y', 'Z']

lowercase = [chr(i) for i in range(97, 123)]
print(lowercase)
# Output: ['a', 'b', 'c', ..., 'x', 'y', 'z']

# Caesar cipher using ord() and chr()
def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result

print(caesar_cipher("Hello World", 3))    # Output: Khoor Zruog
print(caesar_cipher("Khoor Zruog", -3))   # Output: Hello World

# Shift characters
def shift_char(ch, n):
    """Shift a single character by n positions in ASCII"""
    return chr(ord(ch) + n)

print(shift_char("A", 2))        # Output: C
print(shift_char("z", -1))       # Output: y

# Character to binary
char = "A"
print(f"'{char}' = {ord(char)} = {ord(char):08b}")
# Output: 'A' = 65 = 01000001
```

### Unicode Beyond ASCII

```python
# Unicode code points
print(ord("!"))               # Output: 8377 (Indian Rupee sign)
print(chr(8377))              # Output: !
print(chr(0x03A9))            # Output: (Omega, hex 0x03A9 = decimal 937)
print(chr(0x1F600))           # Output: (grinning face, emoji)

# Unicode range example
for code in range(0x4E00, 0x4E10):
    char = chr(code)
    print(f"U+{code:04X}: {char}")
# Output: (CJK Unified Ideographs block sample)
```

## Regular Expressions Introduction (re module)

Regular expressions provide a powerful way to search, match, and manipulate strings based on patterns.

### Importing and Basic Matching

```python
import re

# re.search() - searches for a pattern anywhere in the string
text = "The quick brown fox jumps over the lazy dog"
match = re.search(r"fox", text)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")
    # Output: Found 'fox' at position 16

# re.match() - matches pattern at the beginning of the string
match = re.match(r"The", text)
if match:
    print(f"Starts with '{match.group()}'")
    # Output: Starts with 'The'

# re.findall() - finds all occurrences
text = "My numbers are 123, 456, and 789"
numbers = re.findall(r"\d+", text)
print(numbers)                     # Output: ['123', '456', '789']
```

### Common Regex Patterns

| Pattern  | Meaning                                  | Example                    | Matches            |
|----------|------------------------------------------|----------------------------|--------------------|
| `.`      | Any character except newline             | `h.llo`                    | hello, hxllo       |
| `\d`     | Digit (0-9)                              | `\d\d\d`                   | 123, 456           |
| `\D`     | Non-digit                                | `\D\D`                     | ab, A#             |
| `\w`     | Word character (alphanumeric + underscore) | `\w+`                    | hello, abc123      |
| `\W`     | Non-word character                      | `\W`                       | !, @, #, space     |
| `\s`     | Whitespace (space, tab, newline)         | `\s`                       | ' ', '\t', '\n'    |
| `\S`     | Non-whitespace                           | `\S+`                      | hello, 123         |
| `^`      | Start of string                          | `^Hello`                   | Hello...           |
| `$`      | End of string                            | `world$`                   | ...world           |
| `*`      | 0 or more repetitions                   | `ab*c`                     | ac, abc, abbc      |
| `+`      | 1 or more repetitions                   | `ab+c`                     | abc, abbc          |
| `?`      | 0 or 1 repetition                       | `ab?c`                     | ac, abc            |
| `{n}`    | Exactly n repetitions                   | `\d{3}`                    | 123, 456           |
| `{n,m}`  | Between n and m repetitions             | `\d{2,4}`                  | 12, 123, 1234      |
| `[abc]`  | Any character in the set                | `[aeiou]`                  | a, e, i, o, u      |
| `[a-z]`  | Range of characters                     | `[a-z]`                    | any lowercase      |
| `[^abc]` | Any character NOT in the set            | `[^0-9]`                   | any non-digit      |
| `|`      | OR                                      | `cat|dog`                  | cat, dog           |
| `()`     | Grouping                                 | `(ab)+`                    | ab, abab           |

### Using re.findall()

```python
import re

text = "Contact us: john@example.com, jane@test.org, or admin@site.com"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)
# Output: ['john@example.com', 'jane@test.org', 'admin@site.com']

# Extracting all words
words = re.findall(r"\w+", "Hello, World! How are you?")
print(words)                     # Output: ['Hello', 'World', 'How', 'are', 'you']

# Extracting all numbers
prices = "Items cost $12.50, $5.00, and $100.00"
amounts = re.findall(r"\d+\.\d{2}", prices)
print(amounts)                   # Output: ['12.50', '5.00', '100.00']
```

### Using re.search() and re.match()

```python
import re

text = "Python 3.10 was released in 2021"

# search() finds anywhere
m = re.search(r"\d+\.\d+", text)
if m:
    print(f"Version: {m.group()}")       # Output: Version: 3.10

# match() only at start
m = re.match(r"Python", text)
if m:
    print(f"Starts with: {m.group()}")   # Output: Starts with: Python

# match() returns None if not at start
m = re.match(r"\d+", text)
print(m)                                  # Output: None
```

### Using re.sub() (Substitution)

```python
import re

text = "My phone number is 123-456-7890"
masked = re.sub(r"\d", "*", text)
print(masked)                          # Output: My phone number is ***-***-****

# Replace pattern with formatted text
text = "Date: 2026-08-10"
formatted = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", text)
print(formatted)                       # Output: Date: 10/08/2026

# Remove HTML tags
html = "<p>Hello <b>World</b></p>"
clean = re.sub(r"<[^>]+>", "", html)
print(clean)                           # Output: Hello World
```

### Using re.split()

```python
import re

text = "apple,banana;cherry grape"
parts = re.split(r"[,; ]", text)
print(parts)                          # Output: ['apple', 'banana', 'cherry', 'grape']

# Split on multiple whitespace
text = "one   two\tthree\nfour"
parts = re.split(r"\s+", text)
print(parts)                          # Output: ['one', 'two', 'three', 'four']
```

### Using re.compile() for Performance

```python
import re

# Compile once, use many times for better performance
pattern = re.compile(r"\d{3}-\d{4}")

texts = ["Call 555-1234", "Fax 555-5678", "No number here"]
for text in texts:
    m = pattern.search(text)
    if m:
        print(f"Found: {m.group()}")
    else:
        print("No match")
```

### Practical Regex Examples

#### Email Validation

```python
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

emails = ["user@example.com", "invalid-email", "user@.com", "user@example.co.uk"]
for e in emails:
    print(f"{e:25} -> {'Valid' if is_valid_email(e) else 'Invalid'}")
```

#### Phone Number Extraction

```python
import re

text = "Contact: John (555) 123-4567 or Jane 555-987-6543"
phones = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
print(phones)                         # Output: ['(555) 123-4567', '555-987-6543']
```

#### Data Extraction from Logs

```python
import re

log = """2026-08-10 10:15:30 INFO  User login successful
2026-08-10 10:16:45 ERROR Connection timeout
2026-08-10 10:17:12 INFO  File uploaded
2026-08-10 10:18:00 WARN  Disk space low"""

# Extract all ERROR lines
errors = re.findall(r"^.*ERROR.*$", log, re.MULTILINE)
for error in errors:
    print(error)
# Output: 2026-08-10 10:16:45 ERROR Connection timeout

# Extract timestamps
timestamps = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", log)
print(timestamps)
# Output: ['2026-08-10 10:15:30', '2026-08-10 10:16:45', '2026-08-10 10:17:12', '2026-08-10 10:18:00']
```

## Practice Problems

1. **Advanced Password Validator with Regex**: Write a program that validates a password with the following rules using regex:
   - At least 8 characters
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one digit
   - At least one special character (@, #, $, %, etc.)
   <details>
   <summary>Show Answer</summary>

   ```python
   import re
   password = input("Enter password: ")
   pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$"
   if re.match(pattern, password):
       print("Strong password!")
   else:
       print("Weak password. Must be 8+ chars with upper, lower, digit, and special char.")
   ```
   </details>

2. **URL Parser with Regex**: Write a function that extracts protocol, domain, and path from a URL using regex groups.
   <details>
   <summary>Show Answer</summary>

   ```python
   import re
   def parse_url(url):
       pattern = r"(\w+)://([^/]+)(/.*)?"
       m = re.match(pattern, url)
       if m:
           return {"protocol": m.group(1), "domain": m.group(2), "path": m.group(3) or "/"}
       return None

   url = "https://www.example.com/python/course"
   parsed = parse_url(url)
   if parsed:
       for key, value in parsed.items():
           print(f"{key}: {value}")
   ```
   </details>

3. **Word Scrambler Using f-strings and ord()/chr()**: Write a program that takes a word and shifts each character by a random amount between 1-5, displaying the original and scrambled versions.
   <details>
   <summary>Show Answer</summary>

   ```python
   import random
   word = input("Enter a word: ")
   scrambled = ""
   for ch in word:
       if ch.isalpha():
           shift = random.randint(1, 5)
           if ch.islower():
               new_ch = chr((ord(ch) - 97 + shift) % 26 + 97)
           else:
               new_ch = chr((ord(ch) - 65 + shift) % 26 + 65)
           scrambled += new_ch
       else:
           scrambled += ch
   print(f"Original: {word}")
   print(f"Scrambled: {scrambled}")
   ```
   </details>

4. **Text Statistics with f-strings**: Write a program that reads a paragraph and displays statistics using f-strings:
   - Total characters (including and excluding spaces)
   - Total words
   - Total sentences
   - Average word length
   - Uppercase, lowercase, digit, and space counts
   <details>
   <summary>Show Answer</summary>

   ```python
   text = input("Enter a paragraph: ")
   char_count = len(text)
   char_no_space = len(text.replace(" ", ""))
   words = text.split()
   word_count = len(words)
   sentences = text.count(".") + text.count("!") + text.count("?")
   avg_word_len = sum(len(w) for w in words) / word_count if word_count > 0 else 0
   upper = sum(1 for c in text if c.isupper())
   lower = sum(1 for c in text if c.islower())
   digits = sum(1 for c in text if c.isdigit())
   spaces = sum(1 for c in text if c.isspace())

   print(f"{'Statistic':<30} {'Value':<10}")
   print("-" * 40)
   print(f"{'Total characters':<30} {char_count:<10}")
   print(f"{'Characters (no spaces)':<30} {char_no_space:<10}")
   print(f"{'Word count':<30} {word_count:<10}")
   print(f"{'Sentence count':<30} {sentences:<10}")
   print(f"{'Avg word length':<30} {avg_word_len:<10.2f}")
   print(f"{'Uppercase letters':<30} {upper:<10}")
   print(f"{'Lowercase letters':<30} {lower:<10}")
   print(f"{'Digits':<30} {digits:<10}")
   print(f"{'Spaces':<30} {spaces:<10}")
   ```
   </details>

5. **Regex-Based Search and Replace Tool**: Write a program that takes a text and a regex pattern, then finds all matches and offers to replace each with user-provided text.
   <details>
   <summary>Show Answer</summary>

   ```python
   import re
   text = input("Enter text: ")
   pattern = input("Enter regex pattern: ")
   matches = re.findall(pattern, text)
   if not matches:
       print("No matches found.")
   else:
       print(f"Found {len(matches)} match(es): {matches}")
       replace_with = input("Replace with: ")
       result = re.sub(pattern, replace_with, text)
       print("Result:", result)
   ```
   </details>
