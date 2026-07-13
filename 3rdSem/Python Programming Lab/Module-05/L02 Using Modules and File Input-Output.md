# Using Modules and File Input/Output

**Course:** Python Programming Lab  
**Module:** 5 | **Lecture:** 2  
**Date:** 09-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Open and read text files using Python's built-in open() function.
- Use read(), readline(), and readlines() methods to read file content.
- Write programs to read a file, count lines, and count words in a file.

## Theory

File handling in Python begins with the open() function: `file = open("filename", "r")`. The "r" mode opens for reading (text mode). Other modes include "w" (write), "a" (append), and "r+" (read and write). By default, files are opened in text mode. Adding "b" opens in binary mode (e.g., "rb", "wb").

Three methods are used for reading:
- read(size) reads the entire file (or size bytes/chars if specified) as a single string.
- readline() reads one line (including the newline character).
- readlines() reads all lines into a list of strings.

After reading, the file must be closed with file.close() to free system resources. Files are iterable: `for line in file:` processes the file line by line without loading it entirely into memory. This is memory-efficient for large files.

Word counting involves reading the file content, splitting into words, and counting them. Line counting can be done by iterating over the file object or using len(file.readlines()). Always handle the case where the file does not exist (FileNotFoundError) or other I/O errors.

## Procedure

1. Create a sample text file named `sample.txt` with some content.
2. Create a new Python file named lab26.py.
3. Open `sample.txt` in read mode and display all content using read().
4. Open the same file and use readline() to read one line at a time.
5. Use readlines() to get all lines as a list, then print them with line numbers.
6. Write a program that counts the number of lines in a file.
7. Write a program that counts the number of words in a file.
8. Test all programs.

## Source Code

```python
# Module 05 Lab 02: File Reading - read(), readline(), readlines()

# First, create a sample file to work with
sample_content = """Python is a powerful programming language.
It is widely used in data science and web development.
File handling is an important skill for any programmer.
This is the fourth line of the sample file.
The fifth and final line ends here."""

with open("sample.txt", "w") as f:
    f.write(sample_content)

print("Sample file 'sample.txt' created.")

# Method 1: read() - read entire file at once
print("\n--- Using read() ---")
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# Method 2: readline() - read one line at a time
print("\n--- Using readline() ---")
file = open("sample.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(f"Line 1: {line1.strip()}")
print(f"Line 2: {line2.strip()}")
file.close()

# readline() in a loop
print("\n--- readline() in a loop ---")
file = open("sample.txt", "r")
line = file.readline()
line_num = 1
while line:
    print(f"{line_num}: {line.strip()}")
    line = file.readline()
    line_num += 1
file.close()

# Method 3: readlines() - read all lines into a list
print("\n--- Using readlines() ---")
file = open("sample.txt", "r")
lines = file.readlines()
print(f"Number of lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"{i}: {line.strip()}")
file.close()

# Iterate over file object directly (most efficient)
print("\n--- Iterating over file object ---")
file = open("sample.txt", "r")
for line_num, line in enumerate(file, 1):
    print(f"{line_num}: {line.strip()}")
file.close()

# Line count program
print("\n--- Line Count ---")
file = open("sample.txt", "r")
line_count = 0
for _ in file:
    line_count += 1
file.close()
print(f"Total lines: {line_count}")

# Word count program
print("\n--- Word Count ---")
file = open("sample.txt", "r")
text = file.read()
words = text.split()
word_count = len(words)
file.close()
print(f"Total words: {word_count}")

# Combined: line, word, character count
print("\n--- File Statistics ---")
file = open("sample.txt", "r")
data = file.read()
file.close()

lines = data.count("\n") + 1  # count newlines + 1
words = len(data.split())
chars = len(data)

print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {chars}")
```

## Sample Output

```
Sample file 'sample.txt' created.

--- Using read() ---
Python is a powerful programming language.
It is widely used in data science and web development.
File handling is an important skill for any programmer.
This is the fourth line of the sample file.
The fifth and final line ends here.

--- Using readline() ---
Line 1: Python is a powerful programming language.
Line 2: It is widely used in data science and web development.

--- readline() in a loop ---
1: Python is a powerful programming language.
2: It is widely used in data science and web development.
3: File handling is an important skill for any programmer.
4: This is the fourth line of the sample file.
5: The fifth and final line ends here.

--- Using readlines() ---
Number of lines: 5
1: Python is a powerful programming language.
2: It is widely used in data science and web development.
3: File handling is an important skill for any programmer.
4: This is the fourth line of the sample file.
5: The fifth and final line ends here.

--- Iterating over file object ---
1: Python is a powerful programming language.
2: It is widely used in data science and web development.
3: File handling is an important skill for any programmer.
4: This is the fourth line of the sample file.
5: The fifth and final line ends here.

--- Line Count ---
Total lines: 5

--- Word Count ---
Total words: 30

--- File Statistics ---
Lines: 5
Words: 30
Characters: 161
```

## Homework

1. Create a file `poem.txt` with a short poem (4 lines). Write a program that reads and displays the poem with line numbers.
2. Write a program that reads a file and prints only the lines that contain the word "Python" (case-insensitive).
3. Write a program that reads a file and finds the longest line (by character count), printing its line number and length.
