# Input-Output Operations and File Handling

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 7  
**Date:** 30-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## Console I/O: `input()` and `print()`

### The `input()` Function

The `input()` function reads a line from the user (keyboard) as a string.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Output:**
```
Enter your name: Alice
Hello, Alice
```

**Important:** `input()` always returns a string. You must convert it to the desired type.

```python
age = input("Enter your age: ")       # returns "25" (string)
age = int(age)                         # convert to int

# Or do it in one step
age = int(input("Enter your age: "))
```

```python
# Numeric input examples
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
```

**Output:**
```
Enter first number: 10.5
Enter second number: 3.2
Sum: 13.7
```

### The `print()` Function

The `print()` function outputs data to the console.

```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

#### The `sep` Parameter

The `sep` parameter specifies the separator between multiple arguments (default is a space).

```python
print("apple", "banana", "cherry")
print("apple", "banana", "cherry", sep=", ")
print("apple", "banana", "cherry", sep=" | ")
print("apple", "banana", "cherry", sep="")
```

**Output:**
```
apple banana cherry
apple, banana, cherry
apple | banana | cherry
applebananacherry
```

#### The `end` Parameter

The `end` parameter specifies what to print at the end (default is `\n` newline).

```python
print("Hello", end=" ")
print("World")

print("Line 1", end=" --- ")
print("Line 2", end="\n\n")
print("Line 3")
```

**Output:**
```
Hello World
Line 1 --- Line 2

Line 3
```

#### The `file` Parameter

The `file` parameter redirects output to a file or other file-like object.

```python
with open("output.txt", "w") as f:
    print("This goes to the file", file=f)
    print("This also goes to the file", file=f)

print("This goes to the console")
```

**Content of `output.txt`:**
```
This goes to the file
This also goes to the file
```

#### Combining `sep`, `end`, and `file`

```python
data = [1, 2, 3, 4, 5]

# Print list items separated by commas
print(*data, sep=", ")

# Print to file with custom separator and end
with open("data.txt", "w") as f:
    print(*data, sep=", ", end="!", file=f)
```

## File Handling

File handling allows you to read from and write to files on disk.

### Opening a File: `open()`

The `open()` function returns a file object.

```python
file_object = open(filename, mode)
```

### File Modes

| Mode | Description                                  |
|------|----------------------------------------------|
| `'r'` | Read mode (default). File must exist.        |
| `'w'` | Write mode. Creates file or truncates if exists. |
| `'a'` | Append mode. Creates file if not exists.     |
| `'x'` | Exclusive creation. Fails if file exists.    |
| `'r+'`| Read and write. File must exist.             |
| `'w+'`| Read and write. Creates or truncates.        |
| `'a+'`| Read and append. Creates if not exists.      |
| `'b'` | Binary mode (add to another mode, e.g., `'rb'`, `'wb'`). |
| `'t'` | Text mode (default, e.g., `'rt'`).           |

```python
# Different ways to open a file
f1 = open("file.txt", "r")    # read text (default)
f2 = open("file.txt", "w")    # write text
f3 = open("file.txt", "a")    # append text
f4 = open("file.txt", "rb")   # read binary
f5 = open("file.txt", "r+")   # read and write
```

### Reading Files

#### `read()` -- Read Entire Content

```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

**Content of `sample.txt`:**
```
First line
Second line
Third line
```

**Output:**
```
First line
Second line
Third line
```

You can also read a specific number of characters:

```python
file = open("sample.txt", "r")
first_10 = file.read(10)
print(first_10)
file.close()
```

#### `readline()` -- Read One Line

```python
file = open("sample.txt", "r")
line1 = file.readline()
line2 = file.readline()
print("Line 1:", line1, end="")
print("Line 2:", line2, end="")
file.close()
```

**Output:**
```
Line 1: First line
Line 2: Second line
```

#### `readlines()` -- Read All Lines into a List

```python
file = open("sample.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

**Output:**
```
['First line\n', 'Second line\n', 'Third line\n']
```

#### Reading Line by Line (Recommended)

```python
file = open("sample.txt", "r")
for line in file:
    print(line, end="")
file.close()
```

**Output:**
```
First line
Second line
Third line
```

### Writing Files

#### `write()` -- Write a String

```python
file = open("output.txt", "w")
file.write("Hello, World!\n")
file.write("This is the second line.\n")
file.close()

# Verify
file = open("output.txt", "r")
print(file.read())
file.close()
```

**Output:**
```
Hello, World!
This is the second line.
```

**Note:** `write()` does not add a newline automatically. You must include `\n` if needed.

#### `writelines()` -- Write a List of Strings

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

file = open("output.txt", "w")
file.writelines(lines)
file.close()

# Verify
with open("output.txt", "r") as f:
    print(f.read())
```

**Output:**
```
Line 1
Line 2
Line 3
```

### Append Mode

```python
file = open("log.txt", "a")
file.write("New log entry\n")
file.write("Another entry\n")
file.close()

# Read to verify
with open("log.txt", "r") as f:
    print(f.read())
```

Each run adds more lines without deleting the existing content.

### Read and Write Mode (`'r+'`)

```python
with open("data.txt", "w") as f:
    f.write("ABCDEFGHIJ")

with open("data.txt", "r+") as f:
    content = f.read()       # read entire content
    print("Before:", content)
    f.seek(0)                # go back to beginning
    f.write("123")           # overwrite first 3 characters
    f.seek(0)
    print("After:", f.read())
```

**Output:**
```
Before: ABCDEFGHIJ
After: 123DEFGHIJ
```

## The `with` Statement (Context Manager)

The `with` statement automatically closes the file when the block is exited, even if an exception occurs.

### Without `with` (Manual Close Required)

```python
file = open("sample.txt", "r")
content = file.read()
file.close()  # must close manually
```

### With `with` (Automatic Close)

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

### Benefits of `with`

1. Automatic resource cleanup.
2. No need to remember `file.close()`.
3. File is closed even if an exception occurs.

```python
try:
    with open("sample.txt", "r") as f:
        data = f.read()
        result = int(data)  # might raise ValueError
except ValueError as e:
    print("Error:", e)
# File is still closed properly
```

## Handling File Exceptions

Common file-related exceptions:

| Exception       | When It Occurs                                   |
|-----------------|--------------------------------------------------|
| `FileNotFoundError` | File does not exist when opening in read mode. |
| `PermissionError`   | No permission to read/write the file.           |
| `IsADirectoryError` | Attempting to open a directory as a file.       |
| `IOError`           | General I/O error (base class).                 |

```python
import os

filename = "nonexistent.txt"

try:
    with open(filename, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except PermissionError:
    print(f"Error: No permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Output:**
```
Error: File 'nonexistent.txt' not found.
```

### Checking if a File Exists Before Opening

```python
import os

filename = "sample.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"File '{filename}' does not exist.")
```

## File Pointer Methods: `seek()` and `tell()`

```python
with open("sample.txt", "r") as f:
    print("Position:", f.tell())  # 0 (beginning)

    data = f.read(5)
    print("Read:", data)
    print("Position:", f.tell())  # 5

    f.seek(0)  # go back to beginning
    print("After seek(0):", f.tell())

    f.seek(10)  # move to byte 10
    data = f.read(5)
    print("At position 10, read 5:", data)
```

## Working with Binary Files

Binary files store data in binary format (images, videos, executables, etc.).

### Reading a Binary File

```python
with open("image.jpg", "rb") as f:
    data = f.read()
    print(f"Read {len(data)} bytes")
```

### Writing a Binary File

```python
# Copy a binary file
with open("source.jpg", "rb") as src:
    data = src.read()

with open("copy.jpg", "wb") as dest:
    dest.write(data)

print("File copied successfully")
```

### Working with Binary Data

```python
# Write binary data (bytes)
with open("binary.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03")
    f.write(bytes([10, 20, 30, 40]))

# Read binary data
with open("binary.bin", "rb") as f:
    content = f.read()
    print("Bytes:", content)
    print("As list:", list(content))
```

**Output:**
```
Bytes: b'\x00\x01\x02\x03\n\x14\x1e('
As list: [0, 1, 2, 3, 10, 20, 30, 40]
```

## Complete Examples

### Example 1: Student Grades File

```python
# Write student data
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95),
]

with open("grades.txt", "w") as f:
    f.write("Student Grades\n")
    f.write("=" * 20 + "\n")
    for name, grade in students:
        f.write(f"{name}: {grade}\n")

# Read and display
with open("grades.txt", "r") as f:
    print(f.read())
```

**Output:**
```
Student Grades
====================
Alice: 85
Bob: 92
Charlie: 78
Diana: 95
```

### Example 2: Number Analysis

```python
# Generate numbers file
with open("numbers.txt", "w") as f:
    for i in range(1, 101):
        f.write(f"{i}\n")

# Analyze numbers file
total = 0
count = 0
even_count = 0

with open("numbers.txt", "r") as f:
    for line in f:
        num = int(line.strip())
        total += num
        count += 1
        if num % 2 == 0:
            even_count += 1

print(f"Sum: {total}")
print(f"Count: {count}")
print(f"Average: {total / count:.2f}")
print(f"Even numbers: {even_count}")
```

**Output:**
```
Sum: 5050
Count: 100
Average: 50.50
Even numbers: 50
```

### Example 3: CSV-like File Handling

```python
# Write CSV-like data
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"],
    ["Charlie", "35", "Paris"],
]

with open("people.csv", "w") as f:
    for row in data:
        f.write(",".join(row) + "\n")

# Read and parse CSV-like data
with open("people.csv", "r") as f:
    for line in f:
        fields = line.strip().split(",")
        print(fields)
```

**Output:**
```
['Name', 'Age', 'City']
['Alice', '25', 'New York']
['Bob', '30', 'London']
['Charlie', '35', 'Paris']
```

## Summary: File Methods Reference

| Method            | Description                                     |
|-------------------|-------------------------------------------------|
| `open(file, mode)`| Opens a file and returns a file object          |
| `read(n)`         | Reads `n` characters (or entire file if no `n`) |
| `readline()`      | Reads one line (including newline)              |
| `readlines()`     | Reads all lines into a list                     |
| `write(string)`   | Writes a string to the file                     |
| `writelines(list)`| Writes a list of strings to the file            |
| `seek(offset)`    | Moves file pointer to a given position          |
| `tell()`          | Returns the current file pointer position       |
| `close()`         | Closes the file (automatic with `with`)         |
| `flush()`         | Forces write buffer to be written to disk       |

---

## Practice Problems

**Problem 1:** Write a program that reads a text file named `poem.txt`, counts the number of lines, words, and characters (excluding spaces), and prints the results.

<details>
<summary>Show Answer</summary>

Use a loop over the file object. For each line: increment line count, split to get words, remove spaces for character count.
</details>

<details>
<summary>Show Answer</summary>

```python
lines_count = 0
words_count = 0
chars_count = 0

with open("poem.txt", "r") as f:
    for line in f:
        lines_count += 1
        words_count += len(line.split())
        chars_count += len(line.replace(" ", "").strip())

print(f"Lines: {lines_count}")
print(f"Words: {words_count}")
print(f"Characters (no spaces): {chars_count}")
```
</details>

**Problem 2:** Write a program that appends the current date and time (as a string) to a file `log.txt` every time it is run. Use the `datetime` module.

<details>
<summary>Show Answer</summary>

Open in append mode. Use `import datetime` and `datetime.datetime.now()`.
</details>

<details>
<summary>Show Answer</summary>

```python
from datetime import datetime

with open("log.txt", "a") as f:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"Program run at: {timestamp}\n")

print("Logged successfully")

# Verify by reading
with open("log.txt", "r") as f:
    print(f.read())
```
</details>

**Problem 3:** Write a program that reads a file `data.txt` containing one integer per line, squares each integer, and writes the results to `squared.txt` (one per line). Handle the case where `data.txt` does not exist.

<details>
<summary>Show Answer</summary>

Use `try-except` with `FileNotFoundError`. Use `int(line.strip())` for conversion.
</details>

<details>
<summary>Show Answer</summary>

```python
try:
    with open("data.txt", "r") as infile, open("squared.txt", "w") as outfile:
        for line in infile:
            if line.strip():  # skip empty lines
                num = int(line.strip())
                outfile.write(f"{num ** 2}\n")
    print("Processing complete. Check squared.txt")
except FileNotFoundError:
    print("Error: data.txt not found.")
except ValueError as e:
    print(f"Error: Invalid number in file: {e}")
```
</details>

**Problem 4:** Write a program that reads a binary file `image.jpg`, reverses the byte order, and writes the result to `reversed.jpg`. The reversed file will be corrupted (this is for learning purposes).

<details>
<summary>Show Answer</summary>

Use `'rb'` and `'wb'` modes. Use `data[::-1]` to reverse bytes.
</details>

<details>
<summary>Show Answer</summary>

```python
try:
    with open("image.jpg", "rb") as f:
        data = f.read()

    reversed_data = data[::-1]

    with open("reversed.jpg", "wb") as f:
        f.write(reversed_data)

    print(f"Reversed {len(data)} bytes successfully.")
except FileNotFoundError:
    print("Error: image.jpg not found.")
```
</details>

**Problem 5:** Write a program that asks the user for their name, age, and favorite color, then saves this information to a file `user_info.txt` in a formatted way using `print()` with the `file` parameter.

<details>
<summary>Show Answer</summary>

Use `input()` to collect data. Use `print(f"...", file=f)` to write formatted output.
</details>

<details>
<summary>Show Answer</summary>

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")

with open("user_info.txt", "w") as f:
    print("=" * 30, file=f)
    print("User Information", file=f)
    print("=" * 30, file=f)
    print(f"Name: {name}", file=f)
    print(f"Age: {age}", file=f)
    print(f"Favorite Color: {color}", file=f)
    print("=" * 30, file=f)

print("Information saved to user_info.txt")

# Display the file
print("\nFile contents:")
with open("user_info.txt", "r") as f:
    print(f.read())
```
</details>
