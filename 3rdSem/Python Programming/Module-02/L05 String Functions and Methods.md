# String Functions and Methods

**Course:** Python Programming  
**Module:** 2 | **Lecture:** 5  
**Date:** 10-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 105-142

## Alignment Methods

These methods align a string within a specified width by padding it with a fill character (default is space).

### center(width, fillchar)

Returns a centered string of the specified width.

```python
text = "Python"
print(text.center(20))         # Output:       Python
print(text.center(20, "-"))    # Output: -------Python-------

# If width is less than or equal to string length, returns original string
print(text.center(3))          # Output: Python

# Practical: Creating a heading
heading = "Chapter 1: Introduction"
print(heading.center(50, "="))
# Output: ===========Chapter 1: Introduction===========
```

### ljust(width, fillchar)

Returns a left-justified string of the specified width. The string is padded on the right.

```python
text = "Python"
print(text.ljust(15))          # Output: Python       
print(text.ljust(15, "."))     # Output: Python........

# Practical: Creating a left-aligned table
items = [("Apple", 1.50), ("Banana", 0.75), ("Cherry", 2.25)]
for name, price in items:
    print(name.ljust(10, ".") + "$" + str(price).ljust(5))
# Output:
# Apple......$1.5
# Banana.....$0.75
# Cherry.....$2.25
```

### rjust(width, fillchar)

Returns a right-justified string of the specified width. The string is padded on the left.

```python
text = "Python"
print(text.rjust(15))          # Output:        Python
print(text.rjust(15, "."))     # Output: ........Python

# Practical: Right-aligning numbers
numbers = [1, 12, 123, 1234, 12345]
for n in numbers:
    print(str(n).rjust(5))
# Output:
#     1
#    12
#   123
#  1234
# 12345
```

### Combined Alignment Example

```python
# Creating a formatted report
print("=" * 50)
print("SALES REPORT".center(50))
print("=" * 50)
print("Item".ljust(20) + "Qty".rjust(10) + "Price".rjust(10) + "Total".rjust(10))
print("-" * 50)
items = [("Laptop", 2, 45000), ("Mouse", 5, 500), ("Keyboard", 3, 1200)]
for item, qty, price in items:
    total = qty * price
    print(
        item.ljust(20) +
        str(qty).rjust(10) +
        str(price).rjust(10) +
        str(total).rjust(10)
    )
```

## zfill(width)

Pads the string on the left with zeros (`0`) to reach the specified width. Particularly useful for numeric strings.

```python
number = "42"
print(number.zfill(5))         # Output: 00042

# Works with negative numbers (zero goes after the minus sign)
print("-42".zfill(5))          # Output: -0042

# Works with decimal numbers
print("3.14".zfill(8))         # Output: 00003.14

# If width is less than or equal, returns original
print("12345".zfill(3))        # Output: 12345
```

### Practical Uses of zfill()

```python
# Padding invoice numbers
invoice_no = "1234"
print("INV-" + invoice_no.zfill(8))    # Output: INV-00001234

# Formatting time components
hours = 9
minutes = 5
seconds = 3
time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(time_str)                        # Output: 09:05:03

# Creating sequential filenames
for i in range(1, 11):
    filename = f"image_{str(i).zfill(3)}.jpg"
    print(filename)
# Output:
# image_001.jpg
# image_002.jpg
# ...
# image_010.jpg
```

## maketrans() and translate()

These methods work together for character-level substitution.

### maketrans(x, y, z)

Creates a translation table that maps one set of characters to another.

- `x`: string of characters to be replaced
- `y`: string of replacement characters (same length as x)
- `z` (optional): string of characters to be deleted

### translate(table)

Applies the translation table to the string.

```python
# Simple character mapping
text = "Hello World"
trans_table = str.maketrans("Hd", "hD")
print(text.translate(trans_table))     # Output: hello WorlD

# Vowel replacement
text = "Python Programming"
trans_table = str.maketrans("aeiou", "AEIOU")
print(text.translate(trans_table))     # Output: PYthOn PrOgrAmmIng

# Removing characters (using third argument)
text = "Hello, World! How are you?"
trans_table = str.maketrans("", "", ",!?")
print(text.translate(trans_table))     # Output: Hello World How are you

# Combining replacement and deletion
text = "Hello123World456"
trans_table = str.maketrans("Helo", "hELO", "123456")
print(text.translate(trans_table))     # Output: hELLOWOrld
```

### Practical Text Transformation

```python
# ROT13 cipher (simple letter substitution)
def rot13(text):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_lower = lowercase[13:] + lowercase[:13]
    shifted_upper = uppercase[13:] + uppercase[:13]
    trans_table = str.maketrans(
        lowercase + uppercase,
        shifted_lower + shifted_upper
    )
    return text.translate(trans_table)

print(rot13("Hello World"))            # Output: Uryyb Jbeyq
print(rot13("Uryyb Jbeyq"))            # Output: Hello World

# Removing all vowels
text = "Python Programming is Fun"
vowels = "aeiouAEIOU"
trans_table = str.maketrans("", "", vowels)
print(text.translate(trans_table))     # Output: Pythn Prgrmmng s Fn
```

## format() Method

The `format()` method provides powerful string formatting capabilities.

### Positional Arguments

```python
# Basic positional formatting
print("{} is {} years old".format("Alice", 25))
# Output: Alice is 25 years old

# Using index numbers
print("{0} is {1} years old. {0} lives in {2}".format("Alice", 25, "NYC"))
# Output: Alice is 25 years old. Alice lives in NYC

# Repeating arguments
print("{0} {0} {1} {1}".format("Hi", "Bye"))
# Output: Hi Hi Bye Bye
```

### Keyword Arguments

```python
print("{name} is {age} years old and lives in {city}".format(
    name="Bob", age=30, city="London"
))
# Output: Bob is 30 years old and lives in London
```

### Format Specifiers

```python
# Width and alignment
print("{:<10}".format("left"))     # Output: left       (left align)
print("{:>10}".format("right"))    # Output:      right (right align)
print("{:^10}".format("center"))   # Output:   center   (center)
print("{:*^10}".format("fill"))    # Output: **fill****

# Numeric formatting
print("{:.2f}".format(3.14159))    # Output: 3.14
print("{:,.2f}".format(1234567.89)) # Output: 1,234,567.89
print("{:d}".format(42))           # Output: 42
print("{:b}".format(42))           # Output: 101010 (binary)
print("{:x}".format(255))          # Output: ff (hex)
print("{:o}".format(255))          # Output: 377 (octal)

# Percentage
print("{:.2%}".format(0.25))       # Output: 25.00%

# Sign display
print("{:+d}".format(42))          # Output: +42
print("{:+d}".format(-42))         # Output: -42
print("{: d}".format(42))          # Output:  42 (space for positive)
print("{: d}".format(-42))         # Output: -42
```

### Combining format() with Strings

```python
# Formatting a table
header = "{:<20} {:<10} {:>10}".format("Name", "Department", "Salary")
print(header)
print("-" * 40)
employees = [
    ("Alice Johnson", "Engineering", 85000),
    ("Bob Smith", "Marketing", 62000),
    ("Charlie Brown", "Sales", 72000)
]
for name, dept, salary in employees:
    print("{:<20} {:<10} {:>10,.2f}".format(name, dept, salary))
```

### Padding and Truncating Strings

```python
# Padding strings
print("{:10}".format("Hi"))              # Output: Hi        
print("{:<10}".format("Hi"))             # Output: Hi        
print("{:>10}".format("Hi"))             # Output:         Hi

# Truncating strings
print("{:.5}".format("Hello World"))     # Output: Hello
print("{:>10.5}".format("Hello World"))  # Output:      Hello
```

### Using format() with Dictionaries

```python
data = {"name": "Alice", "age": 25, "city": "NYC"}
print("{name} lives in {city}".format(**data))
# Output: Alice lives in NYC

# With format specifiers
print("{name:10} {age:3d} {city:10}".format(**data))
# Output: Alice         25 NYC
```

## partition() and rpartition()

These methods split a string into three parts: the part before the separator, the separator itself, and the part after the separator.

### partition(sep)

Splits at the **first** occurrence of the separator. Returns a tuple of 3 elements.

```python
text = "Python-Programming-Language"
result = text.partition("-")
print(result)              # Output: ('Python', '-', 'Programming-Language')

# Accessing individual parts
before, sep, after = text.partition("-")
print(before)              # Output: Python
print(sep)                 # Output: -
print(after)               # Output: Programming-Language

# If separator is not found, the original string is the first element
text2 = "Hello World"
result2 = text2.partition("-")
print(result2)             # Output: ('Hello World', '', '')
```

### rpartition(sep)

Splits at the **last** occurrence of the separator. Returns a tuple of 3 elements.

```python
text = "Python-Programming-Language"
result = text.rpartition("-")
print(result)              # Output: ('Python-Programming', '-', 'Language')

# Accessing parts
before, sep, after = text.rpartition("-")
print(before)              # Output: Python-Programming
print(sep)                 # Output: -
print(after)               # Output: Language
```

### Practical Uses of partition()

```python
# Extracting file name and extension
filename = "document.pdf"
name, dot, ext = filename.rpartition(".")
print(f"Name: {name}, Extension: {ext}")
# Output: Name: document, Extension: pdf

# Parsing email
email = "user@example.com"
local, at, domain = email.partition("@")
print(f"Local part: {local}")
print(f"Domain: {domain}")

# Parsing URL
url = "https://www.example.com/page"
protocol, _, rest = url.partition("://")
print(f"Protocol: {protocol}")
print(f"Rest: {rest}")

# Splitting path
path = r"C:\Users\John\Documents\file.txt"
drive, _, rest = path.partition(":")
print(f"Drive: {drive}")
print(f"Path: {rest}")
```

### partition() vs rpartition() Comparison

```python
text = "one-two-three-four"

# partition finds first separator
print(text.partition("-"))      # Output: ('one', '-', 'two-three-four')

# rpartition finds last separator
print(text.rpartition("-"))     # Output: ('one-two-three', '-', 'four')
```

## encode() and decode()

Strings in Python are Unicode. The `encode()` method converts a string to bytes using a specified encoding. The `decode()` method converts bytes back to a string.

### encode(encoding, errors)

Converts a string to bytes using the specified encoding (default is UTF-8).

```python
text = "Python Programming"

# Encode to bytes using UTF-8
bytes_data = text.encode()
print(bytes_data)              # Output: b'Python Programming'
print(type(bytes_data))        # Output: <class 'bytes'>

# Encode with different encodings
utf8_data = text.encode("utf-8")
ascii_data = text.encode("ascii")
print(utf8_data)               # Output: b'Python Programming'
print(ascii_data)              # Output: b'Python Programming'

# Encoding with error handling
text2 = "Python Programmation"
# ascii_data = text2.encode("ascii")  # UnicodeEncodeError
ascii_data = text2.encode("ascii", errors="ignore")
print(ascii_data)              # Output: b'Python Programmation'
ascii_data = text2.encode("ascii", errors="replace")
print(ascii_data)              # Output: b'Python Programm??tion'
```

### decode(encoding, errors)

Converts bytes back to a string.

```python
# Decode bytes to string
bytes_data = b"Python Programming"
text = bytes_data.decode("utf-8")
print(text)                    # Output: Python Programming

# Full encode-decode cycle
original = "Hello World"
encoded = original.encode("utf-8")
decoded = encoded.decode("utf-8")
print(original == decoded)     # Output: True
```

### Common Encodings

```python
text = "Hello World"

# UTF-8 (most common)
print(text.encode("utf-8"))        # Output: b'Hello World'

# UTF-16
print(text.encode("utf-16"))       # Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00W\x00o\x00r\x00l\x00d\x00'

# ASCII
print(text.encode("ascii"))        # Output: b'Hello World'

# Latin-1 / ISO-8859-1
print(text.encode("latin-1"))      # Output: b'Hello World'
```

### Handling Unicode Characters with encode/decode

```python
# Unicode text
text = "Cafe au lait"

# UTF-8 can encode any Unicode character
utf8 = text.encode("utf-8")
print(utf8)                        # Output: b'Caf\xc3\xa9 au lait'
print(utf8.decode("utf-8"))        # Output: Cafe au lait

# Error handling modes
text = "Python Programming"
modes = ["strict", "ignore", "replace", "xmlcharrefreplace"]
for mode in modes:
    try:
        result = text.encode("ascii", errors=mode)
        print(f"{mode:20}: {result}")
    except UnicodeEncodeError as e:
        print(f"{mode:20}: ERROR - {e}")
```

### Practical File Encoding

```python
# Writing text with specific encoding
text = "UTF-8 is great for Unicode"
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Reading with encoding detection
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)                     # Output: UTF-8 is great for Unicode
```

## Practice Problems

1. **Invoice Generator**: Write a program that uses `center()`, `ljust()`, `rjust()`, and `zfill()` to generate a formatted invoice for a list of items with quantities and prices.

   **Answer**:
   ```python
   print("=".center(50, "="))
   print("INVOICE".center(50))
   print("=".center(50, "="))
   items = [
       ("Widget A", 5, 12.50),
       ("Widget B", 3, 8.75),
       ("Gadget X", 2, 45.00)
   ]
   subtotal = 0
   print("Item".ljust(20) + "Qty".rjust(5) + "Price".rjust(8) + "Total".rjust(8))
   print("-" * 41)
   for name, qty, price in items:
       total = qty * price
       subtotal += total
       print(
           name.ljust(20) +
           str(qty).rjust(5) +
           f"{price:.2f}".rjust(8) +
           f"{total:.2f}".rjust(8)
       )
   print("-" * 41)
   print(f"{'Subtotal:':>33} ${subtotal:.2f}")
   tax = subtotal * 0.08
   print(f"{'Tax (8%):':>33} ${tax:.2f}")
   print(f"{'Total:':>33} ${subtotal + tax:.2f}")
   ```

2. **Character Replacement Tool**: Write a program that uses `maketrans()` and `translate()` to create a simple cipher where each letter is shifted by a given offset.

   **Hint**: Create translation tables for uppercase and lowercase letters separately.

   **Answer**:
   ```python
   def caesar_cipher(text, shift):
       import string
       lower = string.ascii_lowercase
       upper = string.ascii_uppercase
       shifted_lower = lower[shift:] + lower[:shift]
       shifted_upper = upper[shift:] + upper[:shift]
       trans_table = str.maketrans(lower + upper, shifted_lower + shifted_upper)
       return text.translate(trans_table)

   text = "Hello World"
   encrypted = caesar_cipher(text, 3)
   print(f"Original: {text}")
   print(f"Encrypted: {encrypted}")
   decrypted = caesar_cipher(encrypted, -3)
   print(f"Decrypted: {decrypted}")
   ```

3. **Data Parser Using partition()**: Write a program that parses a log entry in the format "timestamp|level|message" using `partition()` and displays formatted output.

   **Answer**:
   ```python
   log_entry = "2026-08-10 14:30:00|ERROR|Connection timeout occurred"
   timestamp, sep1, rest = log_entry.partition("|")
   level, sep2, message = rest.partition("|")
   print(f"[{level}]".ljust(10) + timestamp.ljust(25) + message)
   ```

4. **File Size Formatter**: Write a function that takes a file size in bytes and uses `format()` to display it in human-readable format (KB, MB, GB) with appropriate decimal places.

   **Answer**:
   ```python
   def format_size(bytes_size):
       for unit in ["B", "KB", "MB", "GB", "TB"]:
           if bytes_size < 1024:
               return f"{bytes_size:.2f} {unit}"
           bytes_size /= 1024

   sizes = [500, 2048, 1048576, 1073741824]
   for s in sizes:
       print(f"{s:>12} -> {format_size(s)}")
   ```

5. **Text Alignment Menu**: Write a program that displays a menu of options using `center()`, `ljust()`, and `rjust()` to create a professional-looking menu interface.

   **Answer**:
   ```python
   print("=" * 50)
   print("MAIN MENU".center(50))
   print("=" * 50)
   menu_items = [
       ("1", "New Game"),
       ("2", "Load Game"),
       ("3", "Settings"),
       ("4", "High Scores"),
       ("5", "Exit")
   ]
   for num, item in menu_items:
       print(f"  [{num}]".ljust(8) + item.ljust(30) + "[Enter]".rjust(10))
   print("=" * 50)
   ```
