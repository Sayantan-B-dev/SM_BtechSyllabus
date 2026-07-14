# Exception and Exception Handling

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 1  
**Date:** 05-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## What is an Exception?

An exception is an unexpected event that occurs during program execution. It disrupts the normal flow of instructions. When Python encounters an error it cannot handle, it raises an exception, which stops the program unless the exception is caught and handled.

Without exception handling, a single error crashes the entire program. With exception handling, we can anticipate errors and respond gracefully.

```python
# Without exception handling -- program crashes
x = 10
y = 0
result = x / y  # ZeroDivisionError: division by zero
print("This line never executes")
```

Output:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

## Common Built-in Exceptions

Python defines dozens of built-in exceptions. These are the most common ones every programmer must know:

| Exception | Cause | Example |
|---|---|---|
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `ValueError` | Invalid argument value | `int("abc")` |
| `TypeError` | Operation on incompatible type | `"hello" + 5` |
| `IndexError` | Sequence index out of range | `[1, 2][5]` |
| `KeyError` | Dictionary key not found | `{"a": 1}["b"]` |
| `FileNotFoundError` | File does not exist | `open("nope.txt")` |
| `AttributeError` | Attribute does not exist | `"hello".nonexistent` |
| `ImportError` | Module not found | `import nonexistent_module` |

```python
# ZeroDivisionError
print(10 / 0)

# ValueError
print(int("hello"))

# TypeError
print("Age: " + 25)

# IndexError
numbers = [10, 20, 30]
print(numbers[10])

# KeyError
student = {"name": "Alice", "age": 20}
print(student["grade"])

# FileNotFoundError
with open("data.txt", "r") as f:
    content = f.read()
```

## The try-except Block

The `try` block contains code that might raise an exception. The `except` block contains code that runs when an exception occurs.

### Basic Syntax

```python
try:
    # Code that may raise an exception
    risky_operation()
except:
    # Code that runs if an exception occurs
    handle_error()
```

### Example 1: Handling ZeroDivisionError

```python
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("Program continues after error handling.")
```

Output (user enters 10 and 0):
```
Enter numerator: 10
Enter denominator: 0
Error: Cannot divide by zero!
Program continues after error handling.
```

### Example 2: Handling ValueError

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Error: Please enter a valid number.")
```

Output:
```
Enter your age: twenty
Error: Please enter a valid number.
```

## Catching Specific Exceptions

Always catch specific exceptions instead of using a bare `except`. This prevents hiding unexpected bugs.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("That is not a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Accessing the Exception Object

Use `as` to capture the exception object for inspection:

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ZeroDivisionError as e:
    print(f"Error details: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
```

Output:
```
Enter a number: 10
Enter another number: 0
Error details: division by zero
```

## Multiple Except Blocks

When multiple exceptions are possible, list each `except` block separately. Python checks them in order and executes the first matching block.

```python
try:
    data = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    divisor = int(input("Enter divisor: "))
    result = data[index] / divisor
    print(f"Result: {result}")
except IndexError:
    print("Index out of range. Use 0, 1, or 2.")
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Catching Multiple Exceptions in One Block

```python
try:
    value = input("Enter a number: ")
    num = int(value)
    print(100 / num)
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
```

## The Bare except -- Why to Avoid It

A bare `except:` catches every exception including `KeyboardInterrupt` (Ctrl+C), `SystemExit`, and `MemoryError`. This makes debugging difficult and can lock up programs.

```python
# BAD PRACTICE -- bare except hides everything
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(10 / number)
except:
    print("Something went wrong.")  # Hides all errors!
```

**Better approach:** Always specify the exception type:

```python
# GOOD PRACTICE
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(10 / number)
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Exception Hierarchy

All Python exceptions inherit from `BaseException`. The most important subclass is `Exception`, which all practical exceptions inherit from.

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- NameError
      +-- OSError
      |    +-- FileNotFoundError
      +-- TypeError
      +-- ValueError
```

## Complete File Handling Example

```python
def read_safe(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except PermissionError:
        return f"Error: Permission denied to read '{filename}'."
    except Exception as e:
        return f"Unexpected error: {e}"

# Test
print(read_safe("existing.txt"))
print(read_safe("nonexistent.txt"))
```

## Practice Problems

1. **Safe Division Calculator** -- Write a program that asks the user for two numbers and divides them. Handle `ZeroDivisionError`, `ValueError`, and any other unexpected errors. The program should keep asking until the user types "quit".
   <details>
   <summary>Show Answer</summary>

   ```python
   while True:
       user_input = input("Enter two numbers separated by space (or 'quit'): ")
       if user_input.lower() == "quit":
           break
       try:
           a, b = map(int, user_input.split())
           print(f"{a} / {b} = {a / b}")
       except ValueError:
           print("Enter two integers separated by a space.")
       except ZeroDivisionError:
           print("Cannot divide by zero.")
       except Exception as e:
           print(f"Unexpected error: {e}")
   ```
   </details>

2. **List Access with Error Handling** -- Create a list of 5 fruits. Ask the user for an index and print the fruit at that index. Catch `IndexError` and `ValueError`. If the index is out of range, show available indices.
   <details>
   <summary>Show Answer</summary>

   ```python
   fruits = ["apple", "banana", "cherry", "date", "elderberry"]
   try:
       idx = int(input(f"Enter index (0 to {len(fruits)-1}): "))
       print(f"Fruit at index {idx}: {fruits[idx]}")
   except IndexError:
       print(f"Index out of range. Valid indices: 0 to {len(fruits)-1}")
   except ValueError:
       print("Please enter a valid integer.")
   ```
   </details>

3. **Dictionary Lookup** -- Create a dictionary of student names and grades. Ask the user for a name and print the grade. Handle `KeyError` gracefully. Also handle the case where the user enters a non-string value.
   <details>
   <summary>Show Answer</summary>

   ```python
   grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
   name = input("Enter student name: ")
   try:
       print(f"{name}'s grade: {grades[name]}")
   except KeyError:
       print(f"Student '{name}' not found.")
       print(f"Available students: {', '.join(grades.keys())}")
   ```
   </details>

4. **Multiple Exception Catcher** -- Write a function `process_input(data, index, divisor)` that takes a list, an index, and a divisor. It returns `data[index] / divisor`. Catch `IndexError`, `ZeroDivisionError`, and `TypeError` in separate blocks. Test with various inputs.
   <details>
   <summary>Show Answer</summary>

   ```python
   def process_input(data, index, divisor):
       try:
           return data[index] / divisor
       except IndexError:
           return f"Index {index} out of range (max {len(data)-1})"
       except ZeroDivisionError:
           return "Cannot divide by zero"
       except TypeError:
           return "Invalid type for division"

   print(process_input([10, 20, 30], 1, 5))   # 4.0
   print(process_input([10, 20, 30], 5, 2))   # Index error
   print(process_input([10, 20, 30], 1, 0))   # Zero division
   print(process_input([10, 20, 30], 1, "a")) # TypeError
   ```
   </details>

5. **File Read with Fallback** -- Write a program that tries to read from `config.txt`. If the file is not found, create it with default content `{"theme": "dark", "language": "en"}` and then read it again. Use appropriate exception handling.
   <details>
   <summary>Show Answer</summary>

   ```python
   try:
       with open("config.txt", "r") as f:
           print("Config:", f.read())
   except FileNotFoundError:
       print("Config file not found. Creating default config...")
       with open("config.txt", "w") as f:
           f.write('{"theme": "dark", "language": "en"}')
       with open("config.txt", "r") as f:
           print("New config:", f.read())
   ```
   </details>
