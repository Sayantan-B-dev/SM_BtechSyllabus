# Advanced File Handling and Keyboard Input

**Course:** Python Programming Lab  
**Module:** 5 | **Lecture:** 3  
**Date:** 16-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Write data to files using write() and writelines() methods.
- Append new content to an existing file.
- Write a program that copies the contents of one file to another.

## Theory

File writing uses the open() function with modes: "w" (write -- overwrites existing content), "a" (append -- adds to the end), and "x" (exclusive creation -- fails if file exists). If the file does not exist, "w" and "a" create it. Writing is done with write(string) which writes a single string, or writelines(list_of_strings) which writes multiple strings (no newlines are added automatically).

When writing, you must include newline characters (\n) explicitly if you want line breaks. The write() method returns the number of characters written. For structured output, build strings with f-strings or format() and write the complete string. Always close the file after writing to ensure data is flushed to disk.

File copying involves opening the source file in read mode, reading its content, and writing it to the destination file opened in write mode. For large files, use buffered reading: read and write in chunks rather than loading the entire file into memory. The shutil module provides a high-level copy function, but implementing it manually demonstrates file I/O concepts.

## Procedure

1. Create a new Python file named lab27.py.
2. Write a program that takes user input and writes it to a file using write().
3. Write a program that appends a timestamped log entry to a log file.
4. Use writelines() to write multiple lines at once.
5. Write a file copy program that reads from a source file and writes to a destination file.
6. Verify the output by reading the written files.

## Source Code

```python
# Module 05 Lab 03: File Writing - write(), writelines(), append, copy

# Program 1: Write user input to a file
print("--- Write User Input to File ---")
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

file = open("user_info.txt", "w")
file.write(f"Name: {name}\n")
file.write(f"Age: {age}\n")
file.write(f"City: {city}\n")
file.close()
print("Data written to 'user_info.txt'.\n")

# Verify
file = open("user_info.txt", "r")
print("File contents:")
print(file.read())
file.close()

# Program 2: Append timestamped log entries
print("--- Append to Log File ---")
import datetime

log_file = open("app.log", "a")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = input("Enter log message: ")
log_file.write(f"[{timestamp}] {log_entry}\n")
log_file.close()
print("Log entry appended.\n")

# Program 3: writelines() example
print("--- writelines() Example ---")
lines_to_write = [
    "First line\n",
    "Second line\n",
    "Third line\n",
    "Fourth line\n",
]

file = open("writelines_demo.txt", "w")
file.writelines(lines_to_write)
file.close()
print("Multiple lines written using writelines().\n")

# Program 4: File copy
print("--- File Copy ---")
source_name = input("Enter source filename: ")
dest_name = input("Enter destination filename: ")

try:
    source = open(source_name, "r")
    dest = open(dest_name, "w")

    # Method 1: Copy entire content
    content = source.read()
    dest.write(content)
    print(f"Copied '{source_name}' to '{dest_name}' successfully.")

    source.close()
    dest.close()
except FileNotFoundError:
    print(f"Error: Source file '{source_name}' not found.")

# Program 5: Chunk-based copy for large files
print("\n--- Chunk-based Copy ---")
try:
    with open("writelines_demo.txt", "r") as src:
        with open("chunk_copy.txt", "w") as dst:
            while True:
                chunk = src.read(1024)  # read 1KB at a time
                if not chunk:
                    break
                dst.write(chunk)
    print("Chunk-based copy complete.")
except FileNotFoundError:
    print("Source file not found.")
```

## Sample Output

```
--- Write User Input to File ---
Enter your name: Alice
Enter your age: 20
Enter your city: New York
Data written to 'user_info.txt'.

File contents:
Name: Alice
Age: 20
City: New York

--- Append to Log File ---
Enter log message: Application started successfully.
Log entry appended.

--- writelines() Example ---
Multiple lines written using writelines().

--- File Copy ---
Enter source filename: user_info.txt
Enter destination filename: user_backup.txt
Copied 'user_info.txt' to 'user_backup.txt' successfully.

--- Chunk-based Copy ---
Chunk-based copy complete.
```

## Homework

1. Write a program that asks the user for 5 favorite movies and writes them to a file named `movies.txt`, one per line.
2. Write a program that appends the current date and time to a file `visits.log` each time it is run. After 5 runs, the file should have 5 timestamps.
3. Write a program that merges the contents of two files (`file1.txt` and `file2.txt`) into a third file (`merged.txt`), preserving the order (file1 content first, then file2 content).
