# Except Clause and Try-Finally Clause

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 2  
**Date:** 05-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## The try-except-else Clause

The `else` block runs only when no exception occurs in the `try` block. This separates "success code" from "error handling code".

### Syntax

```python
try:
    risky_code()
except SomeException:
    handle_error()
else:
    # Runs only if no exception was raised
    success_code()
```

### Why Use else?

Putting code in `else` instead of directly in `try` avoids accidentally catching exceptions from code that was not intended to be protected.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Not a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    # This runs only if both int() and division succeeded
    print(f"Success! 100 / {number} = {result}")
```

### Practical Example: File Processing

```python
def process_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return
    else:
        # Only runs if file opened successfully
        word_count = len(content.split())
        print(f"File '{filename}' has {word_count} words.")
        print("First 100 characters:")
        print(content[:100])
    finally:
        # We will cover finally next
        try:
            file.close()
        except NameError:
            pass

process_file("sample.txt")
process_file("nonexistent.txt")
```

Output (when sample.txt exists):
```
File 'sample.txt' has 47 words.
First 100 characters:
This is a sample file for demonstrating the else clause in exception handling...
```

Output (when file does not exist):
```
Error: nonexistent.txt not found.
```

## The try-finally Clause

The `finally` block executes **always** -- whether an exception occurs or not. It is used for cleanup operations: closing files, releasing network connections, freeing resources.

### Syntax

```python
try:
    risky_code()
finally:
    # Always executes
    cleanup_code()
```

### Key Behavior of finally

- Runs after `try` completes normally
- Runs after `except` completes (if present)
- Runs even if `return`, `break`, or `continue` is executed in `try`
- Runs even if an unhandled exception propagates upward

```python
def demonstrate_finally():
    try:
        print("Inside try block.")
        return "Returning from try"
    finally:
        print("Finally block always runs.")

result = demonstrate_finally()
print(f"Result: {result}")
```

Output:
```
Inside try block.
Finally block always runs.
Result: Returning from try
```

Notice that `finally` ran even though `try` had a `return` statement!

### Finally with Unhandled Exceptions

```python
try:
    print("Opening resource...")
    result = 10 / 0  # Unhandled exception
finally:
    print("Closing resource...")  # This still runs

# The exception then propagates and crashes the program
```

Output:
```
Opening resource...
Closing resource...
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
ZeroDivisionError: division by zero
```

### Practical Example: File Handling with finally

```python
def read_file_safe(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        return f"File '{filename}' not found."
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed properly.")

result = read_file_safe("hello.txt")
print(result)
```

Output (file exists):
```
File 'hello.txt' closed properly.
(contents of file)
```

Output (file missing):
```
File 'hello.txt' closed properly.
File 'hello.txt' not found.
```

## The Complete Form: try-except-else-finally

The complete form combines all four clauses in order:

```python
try:
    # Code that might raise an exception
    risky_code()
except SomeException:
    # Runs when exception occurs
    error_handler()
else:
    # Runs when NO exception occurs
    success_handler()
finally:
    # ALWAYS runs (cleanup)
    cleanup()
```

### Order Rules

1. `try` is mandatory
2. At least one `except` or `finally` must be present
3. `else` comes after all `except` blocks, before `finally`
4. `finally` is always the last block

### Complete Example: Division with Full Error Handling

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Operation attempted. Cleanup complete.")

print("Test 1:", safe_divide(10, 2))
print("---")
print("Test 2:", safe_divide(10, 0))
print("---")
print("Test 3:", safe_divide(10, "a"))
```

Output:
```
Division successful: 10 / 2 = 5.0
Operation attempted. Cleanup complete.
Test 1: 5.0
---
Error: Division by zero is not allowed.
Operation attempted. Cleanup complete.
Test 2: None
---
Error: Both arguments must be numbers.
Operation attempted. Cleanup complete.
Test 3: None
```

### Real-World Example: Database Connection

```python
import time

class DatabaseConnection:
    def __init__(self, name):
        self.name = name
        self.connected = False

    def connect(self):
        print(f"Connecting to database '{self.name}'...")
        time.sleep(0.5)
        # Simulate random connection failure
        import random
        if random.random() < 0.3:
            raise ConnectionError(f"Cannot connect to '{self.name}'")
        self.connected = True
        print("Connected successfully.")

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected.")
        print(f"Executing: {sql}")
        return ["result1", "result2"]

    def close(self):
        if self.connected:
            print(f"Closing connection to '{self.name}'.")
            self.connected = False

def run_query(db_name, sql):
    db = DatabaseConnection(db_name)
    try:
        db.connect()
        results = db.query(sql)
    except ConnectionError as e:
        print(f"Connection failed: {e}")
        return []
    except RuntimeError as e:
        print(f"Query error: {e}")
        return []
    else:
        print(f"Query returned {len(results)} rows.")
        return results
    finally:
        db.close()
        print("Cleanup completed.")

# Test
data = run_query("testdb", "SELECT * FROM users")
print("Data:", data)
```

## Comparison Table

| Clause | When it runs | Purpose |
|---|---|---|
| `try` | Always | Code that may raise an exception |
| `except` | When matching exception occurs | Error handling |
| `else` | When no exception in `try` | Success path code |
| `finally` | Always (even on return/break) | Cleanup, resource release |

## Pattern: Resource Cleanup Guarantee

The most important use of `finally` is guaranteeing resource cleanup:

```python
# Without finally (unsafe)
def read_config_bad():
    f = open("config.txt", "r")
    try:
        return f.read()
    except:
        return "{}"
    # If an exception occurs after try but before except,
    # the file is never closed!

# With finally (safe)
def read_config_good():
    f = open("config.txt", "r")
    try:
        return f.read()
    except FileNotFoundError:
        return "{}"
    finally:
        f.close()  # Guaranteed to run
```

**Modern alternative:** The `with` statement (context manager) handles `finally` automatically:

```python
def read_config_best():
    try:
        with open("config.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "{}"
    # f.close() is called automatically by the context manager
```

## Practice Problems

1. **File Statistics** -- Write a function `file_stats(filename)` that reads a file and prints line count, word count, and character count. Use `try-except-else-finally`. In `else`, compute and print statistics. In `finally`, close the file. Handle `FileNotFoundError`.
   <details>
   <summary>Show Answer</summary>

   ```python
   def file_stats(filename):
       f = None
       try:
           f = open(filename, "r")
           content = f.read()
       except FileNotFoundError:
           print(f"File '{filename}' not found.")
           return
       else:
           lines = content.count("\n") + 1 if content else 0
           if not content.endswith("\n"):
               lines += 0
           words = len(content.split())
           chars = len(content)
           print(f"File: {filename}")
           print(f"Lines: {lines}")
           print(f"Words: {words}")
           print(f"Characters: {chars}")
       finally:
           if f:
               f.close()
               print("File closed.")

   file_stats("sample.txt")
   ```
   </details>

2. **Calculator with History Logging** -- Create a calculator that performs division. Use `else` to log successful operations to a list. Use `finally` to print "Operation complete." regardless of outcome. Handle `ZeroDivisionError` and `ValueError`.
   <details>
   <summary>Show Answer</summary>

   ```python
   history = []
   while True:
       user_input = input("Enter a / b (or 'quit'): ")
       if user_input.lower() == "quit":
           break
       parts = user_input.split("/")
       if len(parts) != 2:
           print("Format: a / b")
           continue
       try:
           a, b = float(parts[0]), float(parts[1])
           result = a / b
       except ValueError:
           print("Invalid numbers.")
       except ZeroDivisionError:
           print("Cannot divide by zero.")
       else:
           history.append(f"{a}/{b}={result}")
           print(f"Result: {result}")
           print(f"History: {history}")
       finally:
           print("Operation complete.")
   ```
   </details>

3. **Network Request Simulation** -- Simulate connecting to a server. The connection may raise `TimeoutError` or `ConnectionError`. Use `else` to process data, `finally` to always print "Disconnected from server."
   <details>
   <summary>Show Answer</summary>

   ```python
   import random
   def connect_to_server():
       if random.random() < 0.3:
           raise TimeoutError("Connection timed out.")
       if random.random() < 0.3:
           raise ConnectionError("Connection refused.")
       return "Server response: OK"

   try:
       print("Connecting...")
       response = connect_to_server()
   except TimeoutError as e:
       print(f"Timeout: {e}")
   except ConnectionError as e:
       print(f"Connection failed: {e}")
   else:
       print(f"Data received: {response}")
   finally:
       print("Disconnected from server.")
   ```
   </details>

4. **Bank Transaction** -- Write a function `transfer(from_bal, to_bal, amount)` that simulates a transfer. Use `finally` to print a transaction receipt (with current balances) regardless of success. Raise `ValueError` if amount exceeds balance.
   <details>
   <summary>Show Answer</summary>

   ```python
   def transfer(from_bal, to_bal, amount):
       print(f"Transferring ${amount:.2f}...")
       try:
           if amount > from_bal:
               raise ValueError("Insufficient funds.")
           if amount < 0:
               raise ValueError("Amount must be positive.")
           from_bal -= amount
           to_bal += amount
       except ValueError as e:
           print(f"Transfer failed: {e}")
       else:
           print(f"Transfer of ${amount:.2f} successful.")
       finally:
           print(f"Receipt: From=${from_bal:.2f}, To=${to_bal:.2f}")
       return from_bal, to_bal

   transfer(1000, 500, 200)
   print("---")
   transfer(1000, 500, 1500)
   ```
   </details>

5. **Temperature Converter with Logging** -- Create a converter that reads from a file, converts Celsius to Fahrenheit, writes to another file. Use try-except-else-finally at each step.
   <details>
   <summary>Show Answer</summary>

   ```python
   def convert_celsius_to_fahrenheit():
       input_file = "celsius.txt"
       output_file = "fahrenheit.txt"
       fin = None
       fout = None
       try:
           fin = open(input_file, "r")
           celsius_values = fin.readlines()
       except FileNotFoundError:
           print(f"Input file '{input_file}' not found.")
           return
       else:
           try:
               fout = open(output_file, "w")
               for line in celsius_values:
                   line = line.strip()
                   if not line:
                       continue
                   try:
                       c = float(line)
                       f = c * 9/5 + 32
                       fout.write(f"{c}C = {f:.1f}F\n")
                   except ValueError:
                       fout.write(f"Invalid input: {line}\n")
               print(f"Converted {len(celsius_values)} values.")
           except PermissionError:
               print(f"Cannot write to '{output_file}'.")
       finally:
           if fin:
               fin.close()
           if fout:
               fout.close()
           print(f"Files closed. Check '{output_file}' for results.")

   convert_celsius_to_fahrenheit()
   ```
   </details>
