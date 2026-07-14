# Anonymous Functions, Global and Local Variables

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 4  
**Date:** 16-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## Anonymous Functions (Lambda Functions)

An anonymous function is a function defined without a name. In Python, anonymous functions are created using the `lambda` keyword.

### Syntax

```python
lambda arguments: expression
```

- `lambda` is the keyword.
- `arguments` is a comma-separated list of inputs.
- `expression` is a single expression that is evaluated and returned.
- Lambda functions can only contain a single expression, not statements.

### Basic Examples

```python
# Lambda that squares a number
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda that adds two numbers
add = lambda a, b: a + b
print(add(10, 20))  # 30

# Lambda that checks if a number is even
is_even = lambda n: n % 2 == 0
print(is_even(4))   # True
print(is_even(7))   # False
```

The above is equivalent to:

```python
def square(x):
    return x ** 2

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0
```

### When to Use Lambda Functions

Lambdas are most useful when you need a simple function for a short period, typically as an argument to another function.

#### Using Lambda with `map()`

The `map(function, iterable)` applies a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4, 5]

# Square each number using lambda
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 86.0, 104.0]
```

#### Using Lambda with `filter()`

The `filter(function, iterable)` filters items where the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Get numbers greater than 5
greater = list(filter(lambda x: x > 5, numbers))
print(greater)  # [6, 7, 8, 9, 10]
```

#### Using Lambda with `sorted()`

The `sorted()` function accepts a `key` parameter to customize sorting.

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 72},
    {"name": "Charlie", "grade": 90},
    {"name": "Diana", "grade": 68},
]

# Sort by grade (ascending)
sorted_by_grade = sorted(students, key=lambda s: s["grade"])
print(sorted_by_grade)

# Sort by name (alphabetical)
sorted_by_name = sorted(students, key=lambda s: s["name"])
print(sorted_by_name)
```

**Output:**
```
[{'name': 'Diana', 'grade': 68}, {'name': 'Bob', 'grade': 72}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 90}]
[{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 72}, {'name': 'Charlie', 'grade': 90}, {'name': 'Diana', 'grade': 68}]
```

#### Using Lambda with `max()` and `min()`

```python
# Find the student with the highest grade
best_student = max(students, key=lambda s: s["grade"])
print(best_student)  # {'name': 'Charlie', 'grade': 90}

# Find the word with the maximum length
words = ["python", "programming", "code", "function"]
longest = max(words, key=lambda w: len(w))
print(longest)  # programming
```

### Lambda with Multiple Arguments

```python
# Lambda with three arguments
volume = lambda l, w, h: l * w * h
print(volume(3, 4, 5))  # 60

# Lambda as a key for sorting by multiple criteria
points = [(1, 2), (3, 1), (2, 3), (1, 3)]
# Sort by x first, then by y
sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
print(sorted_points)  # [(1, 2), (1, 3), (2, 3), (3, 1)]
```

### Limitations of Lambda

- Can only contain a single expression (no assignments, loops, or statements).
- Cannot use type annotations.
- Less readable for complex operations.

```python
# This will NOT work -- lambda cannot contain statements
# invalid = lambda x: if x > 0: return x; else: return -x

# Use a regular function instead
def abs_value(x):
    if x > 0:
        return x
    else:
        return -x
```

## Global and Local Variables

### Local Variables

A variable declared inside a function is local to that function. It can only be accessed within that function.

```python
def my_function():
    x = 10  # local variable
    print("Inside function, x =", x)

my_function()
# print(x)  # NameError: name 'x' is not defined
```

**Output:**
```
Inside function, x = 10
```

### Global Variables

A variable declared outside any function is global. It can be accessed from anywhere in the module.

```python
y = 100  # global variable

def show_global():
    print("Inside function, y =", y)  # accessing global variable

show_global()
print("Outside function, y =", y)
```

**Output:**
```
Inside function, y = 100
Outside function, y = 100
```

### The `global` Keyword

Inside a function, if you want to modify a global variable (not just read it), you must use the `global` keyword.

```python
counter = 0  # global variable

def increment():
    global counter  # declare that we want to use the global 'counter'
    counter += 1
    print("Counter inside:", counter)

increment()
increment()
print("Counter outside:", counter)
```

**Output:**
```
Counter inside: 1
Counter inside: 2
Counter outside: 2
```

Without `global`, Python creates a new local variable instead:

```python
counter = 0

def increment_wrong():
    counter = counter + 1  # UnboundLocalError
    # This creates a local 'counter' but it is referenced before assignment

# increment_wrong()  # UnboundLocalError
```

### When to Avoid `global`

Global variables should be used sparingly because they:
- Make code harder to debug (any function can change them).
- Break function encapsulation and reusability.
- Create hidden dependencies between functions.

```python
# Better approach: pass values as arguments and return results
def increment_counter(counter):
    return counter + 1

counter = 0
counter = increment_counter(counter)
counter = increment_counter(counter)
print(counter)  # 2
```

## The `nonlocal` Keyword (Nested Functions)

The `nonlocal` keyword is used inside nested functions to modify variables from the enclosing (outer) function's scope.

```python
def outer():
    message = "Hello"  # variable in enclosing scope

    def inner():
        nonlocal message  # refer to the enclosing 'message'
        message = "Modified"
        print("Inside inner:", message)

    inner()
    print("Inside outer:", message)

outer()
```

**Output:**
```
Inside inner: Modified
Inside outer: Modified
```

Without `nonlocal`, the assignment would create a new local variable in `inner()`:

```python
def outer():
    message = "Hello"

    def inner():
        message = "Modified"  # creates a new local variable
        print("Inside inner:", message)

    inner()
    print("Inside outer:", message)  # still "Hello"

outer()
```

**Output:**
```
Inside inner: Modified
Inside outer: Hello
```

### Variable Scope Lookup Rule (LEGB Rule)

Python looks up variables in this order:

1. **L**ocal -- Inside the current function.
2. **E**nclosing -- In enclosing functions (outer functions).
3. **G**lobal -- At the module level.
4. **B**uilt-in -- Python's built-in namespace.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # local

    inner()

outer()
print(x)  # global
```

**Output:**
```
local
global
```

## Closure Concept

A closure is a function that remembers the environment in which it was created, even after that environment is gone.

### Creating a Closure

```python
def make_multiplier(factor):
    """Return a function that multiplies its argument by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

# Create closures
double = make_multiplier(2)
triple = make_multiplier(3)

# Use the closures
print(double(5))   # 10
print(triple(5))   # 15
print(double(10))  # 20
```

Here, `double` and `triple` are closures. Each remembers its own `factor` value even after `make_multiplier` has finished executing.

### Requirements for a Closure

1. There must be a nested function.
2. The nested function must refer to a variable from the enclosing function.
3. The enclosing function must return the nested function.

```python
def counter(start=0):
    """Create a counter that increments from start."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Create two independent counters
counter_a = counter(10)
counter_b = counter(100)

print(counter_a())  # 11
print(counter_a())  # 12
print(counter_b())  # 101
print(counter_b())  # 102
```

### Practical Use of Closures

Closures can be used to create function factories and maintain state without using global variables.

```python
def make_power(n):
    """Create a function that raises a number to the nth power."""
    return lambda x: x ** n

square = make_power(2)
cube = make_power(3)
fourth = make_power(4)

print(square(5))   # 25
print(cube(3))     # 27
print(fourth(2))   # 16
```

## Summary Table

| Concept            | Keyword      | Scope                            | Used In               |
|--------------------|-------------|----------------------------------|-----------------------|
| Lambda function    | `lambda`    | Inline expression                | `map`, `filter`, `sorted` |
| Local variable     | (none)      | Inside a function                | Any function          |
| Global variable    | `global`    | Module level (to modify inside fn)| Top-level code        |
| Enclosing variable | `nonlocal`  | Outer function's scope           | Nested functions      |
| Closure            | (pattern)   | Remember enclosing scope         | Factory functions     |

---

## Practice Problems

**Problem 1:** Using a lambda with `filter()`, write a one-liner that extracts all words with length greater than 4 from the list `words = ["cat", "elephant", "dog", "giraffe", "bird", "dolphin"]`.

<details>
<summary>Show Answer</summary>

`filter(lambda w: len(w) > 4, words)`
</details>

<details>
<summary>Show Answer</summary>

```python
words = ["cat", "elephant", "dog", "giraffe", "bird", "dolphin"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)  # ['elephant', 'giraffe', 'dolphin']
```
</details>

**Problem 2:** Write a function `make_discount(percentage)` that returns a closure which applies the given percentage discount to a price. For example, `ten_off = make_discount(10)` and `ten_off(100)` should return `90.0`.

<details>
<summary>Show Answer</summary>

The inner function takes `price` and returns `price * (1 - percentage / 100)`.
</details>

<details>
<summary>Show Answer</summary>

```python
def make_discount(percentage):
    def apply_discount(price):
        return price * (1 - percentage / 100)
    return apply_discount

ten_off = make_discount(10)
twenty_off = make_discount(20)

print(ten_off(100))    # 90.0
print(twenty_off(100))  # 80.0
print(ten_off(250))    # 225.0
```
</details>

**Problem 3:** Write a lambda that sorts a list of tuples `(name, age, score)` by score in descending order. Use the `sorted()` function with a lambda as key.

<details>
<summary>Show Answer</summary>

Use `key=lambda t: t[2]` with `reverse=True`.
</details>

<details>
<summary>Show Answer</summary>

```python
data = [("Alice", 22, 85), ("Bob", 20, 92), ("Charlie", 23, 78), ("Diana", 21, 95)]
sorted_data = sorted(data, key=lambda t: t[2], reverse=True)
print(sorted_data)
# [('Diana', 21, 95), ('Bob', 20, 92), ('Alice', 22, 85), ('Charlie', 23, 78)]
```
</details>

**Problem 4:** Write a function `create_logger(prefix)` that returns a closure. The closure should take a message string and print it as `[prefix] message`. Each call to the returned function should also increment an internal counter and display it, like `[prefix #1] message`, `[prefix #2] message`, ...

<details>
<summary>Show Answer</summary>

Use `nonlocal` for the counter variable inside the nested function.
</details>

<details>
<summary>Show Answer</summary>

```python
def create_logger(prefix):
    counter = 0

    def log(message):
        nonlocal counter
        counter += 1
        print(f"[{prefix} #{counter}] {message}")

    return log

app_log = create_logger("APP")
db_log = create_logger("DB")

app_log("Application started")
app_log("User logged in")
db_log("Database connected")
db_log("Query executed")
app_log("Application shutting down")
```

**Output:**
```
[APP #1] Application started
[APP #2] User logged in
[DB #1] Database connected
[DB #2] Query executed
[APP #3] Application shutting down
```
</details>
