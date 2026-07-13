# Advanced File Handling and Keyboard Input

**Course:** Python Programming Lab  
**Module:** 5 | **Lecture:** 4  
**Date:** 16-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Use the with statement (context manager) for automatic file closing.
- Handle file I/O exceptions using try-except blocks.
- Write robust programs for safe file reading and writing.

## Theory

The with statement provides a clean way to manage resources like files. When used with open(), the file is automatically closed when the block exits, even if an exception occurs. The syntax is: `with open("file.txt", "r") as f:`. No explicit f.close() is needed. This is the recommended way to handle files in Python as it prevents resource leaks.

Exception handling with try-except allows the program to gracefully handle errors instead of crashing. Common file I/O exceptions: FileNotFoundError (file doesn't exist), PermissionError (no read/write permission), IsADirectoryError (trying to open a directory as a file), and IOError/OSError (general I/O errors).

A robust file handler should: attempt to open the file, perform the operation, catch specific exceptions with informative messages, and optionally use a finally block for cleanup (though with statement handles this). Exception handling can be combined with loops to give the user multiple attempts to enter a valid filename.

## Procedure

1. Create a new Python file named lab28.py.
2. Write a program that safely reads a file using with statement and try-except.
3. Write a program that asks the user for a filename and keeps trying until a valid file is provided.
4. Write a program that writes data using a context manager.
5. Handle multiple exception types (FileNotFoundError, PermissionError, IsADirectoryError).
6. Test by trying to open non-existent files, directories, and read-only files.

## Source Code

```python
# Module 05 Lab 04: with Statement and Exception Handling in File Ops

# Program 1: Safe file read using with statement
print("--- Safe File Read with Context Manager ---")
filename = input("Enter filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print(f"\nFile '{filename}' read successfully.")
        print("Content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except IsADirectoryError:
    print(f"Error: '{filename}' is a directory, not a file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print()  # blank line

# Program 2: Keep trying until a valid file is provided
print("--- Retry Until Valid File ---")
while True:
    try:
        fname = input("Enter a valid filename: ")
        with open(fname, "r") as f:
            print(f"File opened successfully. First line: {f.readline().strip()}")
        break  # exit loop if successful
    except FileNotFoundError:
        print("File not found. Try again.")
    except Exception as e:
        print(f"Error: {e}. Try again.")

print()

# Program 3: Safe file writing using context manager
print("--- Safe File Write ---")
try:
    with open("output.txt", "w") as f:
        f.write("This is line 1.\n")
        f.write("This is line 2.\n")
        f.write("This is line 3.\n")
    print("Data written to 'output.txt' successfully.")

    # Verify by reading
    with open("output.txt", "r") as f:
        print("Verification - file contents:")
        print(f.read())
except Exception as e:
    print(f"Error during write operation: {e}")

print()

# Program 4: Copy file with exception handling
print("--- Safe File Copy ---")
source = input("Enter source filename: ")
dest = input("Enter destination filename: ")

try:
    with open(source, "r") as src, open(dest, "w") as dst:
        for line in src:
            dst.write(line)
    print(f"Successfully copied '{source}' to '{dest}'.")
except FileNotFoundError:
    print(f"Error: Source file '{source}' not found.")
except PermissionError:
    print(f"Error: Permission denied for file operation.")
except Exception as e:
    print(f"An error occurred during copy: {e}")
```

## Sample Output

```
--- Safe File Read with Context Manager ---
Enter filename to read: nonexistent.txt
Error: The file 'nonexistent.txt' does not exist.

--- Retry Until Valid File ---
Enter a valid filename: missing.txt
File not found. Try again.
Enter a valid filename: sample.txt
File opened successfully. First line: Python is a powerful programming language.

--- Safe File Write ---
Data written to 'output.txt' successfully.
Verification - file contents:
This is line 1.
This is line 2.
This is line 3.

--- Safe File Copy ---
Enter source filename: output.txt
Enter destination filename: output_copy.txt
Successfully copied 'output.txt' to 'output_copy.txt'.
```

## Homework

1. Write a program that asks the user for a filename and reads it. If the file does not exist, create it with some default content ("Empty file created.") and inform the user.
2. Write a program that safely appends user input to a file. Handle the case where the directory does not exist (use os.makedirs or catch FileNotFoundError).
3. Write a program that reads an integer from a file named `number.txt`. If the file doesn't exist, create it with the value 0. If the file contains invalid data, handle the ValueError. Increment the number and write it back.
