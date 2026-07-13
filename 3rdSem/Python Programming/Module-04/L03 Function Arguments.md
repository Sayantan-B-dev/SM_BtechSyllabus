# Function Arguments

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 3  
**Date:** 14-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## Introduction to Function Arguments

Arguments are values passed to a function when it is called. Python provides several flexible ways to pass arguments.

## 1. Positional Arguments

Positional arguments are passed in the same order as the function's parameters. The first argument maps to the first parameter, the second to the second, and so on.

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Positional arguments: order matters
describe_person("Alice", 30, "New York")
```

**Output:**
```
Alice is 30 years old and lives in New York.
```

If you swap the arguments, the result changes:

```python
describe_person("New York", "Alice", 30)  # Wrong order!
```

**Output:**
```
New York is Alice years old and lives in 30.
```

## 2. Keyword Arguments

Keyword arguments are passed using the parameter name. The order does not matter when using keywords.

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Keyword arguments: order does not matter
describe_person(age=25, city="London", name="Bob")
```

**Output:**
```
Bob is 25 years old and lives in London.
```

You can mix positional and keyword arguments, but positional arguments must come first:

```python
# Valid: positional first, then keyword
describe_person("Charlie", city="Paris", age=35)

# Invalid: keyword before positional (this will cause an error)
# describe_person(name="Diana", 40, "Berlin")  # SyntaxError
```

**Output:**
```
Charlie is 35 years old and lives in Paris.
```

## 3. Default Arguments

Default arguments have a predefined value. If the caller does not provide a value, the default is used.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Using the default greeting
greet("Alice")

# Providing a custom greeting
greet("Bob", "Hi")
greet("Charlie", greeting="Good morning")
```

**Output:**
```
Hello, Alice!
Hi, Bob!
Good morning, Charlie!
```

### Important Rule for Default Arguments

Default arguments must be placed after non-default arguments.

```python
# Correct
def create_profile(name, age=18, city="Unknown"):
    print(f"{name}, {age}, {city}")

# Incorrect (SyntaxError)
# def create_profile(name="Guest", age, city):
#     pass
```

### Mutable Default Arguments -- A Common Pitfall

Avoid using mutable objects (lists, dictionaries) as default arguments.

```python
def add_item(item, items=[]):  # Problem: default list is shared across calls
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))
```

**Output:**
```
['apple']
['apple', 'banana']
['apple', 'banana', 'cherry']
```

The default list is created once when the function is defined, not each time the function is called. To fix this, use `None` and create a new list inside the function:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))
```

**Output:**
```
['apple']
['banana']
['cherry']
```

## 4. Variable-Length Arguments

Sometimes you do not know how many arguments will be passed to a function.

### `*args` -- Arbitrary Positional Arguments

The `*args` parameter collects any number of positional arguments into a tuple.

```python
def sum_all(*args):
    """Sum any number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2))           # 3
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all())               # 0 (empty tuple)
```

You can mix regular parameters with `*args`:

```python
def display_info(title, *tags):
    print("Title:", title)
    print("Tags:", tags)

display_info("Python Basics", "programming", "python", "tutorial")
```

**Output:**
```
Title: Python Basics
Tags: ('programming', 'python', 'tutorial')
```

### `**kwargs` -- Arbitrary Keyword Arguments

The `**kwargs` parameter collects any number of keyword arguments into a dictionary.

```python
def create_profile(**kwargs):
    """Create a profile from keyword arguments."""
    print("Profile Details:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_profile(name="Alice", age=30, job="Engineer", city="Boston")
```

**Output:**
```
Profile Details:
  name: Alice
  age: 30
  job: Engineer
  city: Boston
```

You can combine `*args` and `**kwargs`:

```python
def func(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

func(1, 2, 3, 4, 5, x=10, y=20)
```

**Output:**
```
a = 1, b = 2
args = (3, 4, 5)
kwargs = {'x': 10, 'y': 20}
```

## 5. Keyword-Only Arguments (After `*`)

Arguments placed after a bare `*` must be passed as keyword arguments.

```python
def connect(host, port, *, timeout=30, ssl=True):
    print(f"Connecting to {host}:{port}")
    print(f"Timeout: {timeout}s, SSL: {ssl}")

# Keyword-only arguments must use the keyword
connect("localhost", 8080, timeout=60, ssl=False)

# This will cause an error:
# connect("localhost", 8080, 60, False)  # TypeError
```

**Output:**
```
Connecting to localhost:8080
Timeout: 60s, SSL: False
```

## 6. Positional-Only Arguments (Before `/`, Python 3.8+)

Arguments placed before a `/` can only be passed positionally, not by keyword.

```python
def divide(a, b, /):
    """Divide a by b. Both arguments must be positional."""
    return a / b

# Valid - positional arguments
print(divide(10, 3))

# Invalid - keyword arguments not allowed
# print(divide(a=10, b=3))  # TypeError
```

**Output:**
```
3.3333333333333335
```

You can combine all argument types:

```python
def example(pos_only, /, pos_or_keyword, *, keyword_only):
    print(f"Positional-only: {pos_only}")
    print(f"Positional or keyword: {pos_or_keyword}")
    print(f"Keyword-only: {keyword_only}")

example(1, 2, keyword_only=3)          # Valid
example(1, pos_or_keyword=2, keyword_only=3)  # Valid
# example(pos_only=1, pos_or_keyword=2, keyword_only=3)  # Error (pos_only is positional-only)
```

**Output:**
```
Positional-only: 1
Positional or keyword: 2
Keyword-only: 3
```

## 7. Order of Parameters

The complete parameter order is:

```
def func(pos_only, /, pos_or_keyword, *args, keyword_only, **kwargs):
```

1. **Positional-only** parameters (before `/`)
2. **Positional-or-keyword** parameters (between `/` and `*`)
3. **Variable-length positional** `*args`
4. **Keyword-only** parameters (after `*` or `*args`)
5. **Variable-length keyword** `**kwargs`

```python
def complete_example(a, b, /, c, d, *args, e, f, **kwargs):
    print(f"Positional-only: a={a}, b={b}")
    print(f"Positional or keyword: c={c}, d={d}")
    print(f"Extra positional(args): {args}")
    print(f"Keyword-only: e={e}, f={f}")
    print(f"Extra keyword(kwargs): {kwargs}")

complete_example(1, 2, 3, 4, 5, 6, e=7, f=8, g=9, h=10)
```

**Output:**
```
Positional-only: a=1, b=2
Positional or keyword: c=3, d=4
Extra positional(args): (5, 6)
Keyword-only: e=7, f=8
Extra keyword(kwargs): {'g': 9, 'h': 10}
```

## Summary Table

| Argument Type         | Syntax           | How to Pass                     | Example                          |
|----------------------|------------------|--------------------------------|----------------------------------|
| Positional           | `def f(a, b)`    | `f(1, 2)`                      | Standard matching by order       |
| Keyword              | `def f(a, b)`    | `f(b=2, a=1)`                  | Match by parameter name          |
| Default              | `def f(a=0)`     | `f()` or `f(5)`                | Uses default if not provided     |
| Variable positional  | `def f(*args)`   | `f(1, 2, 3)`                   | Collects extra args into tuple   |
| Variable keyword     | `def f(**kwargs)`| `f(x=1, y=2)`                  | Collects extra kwargs into dict  |
| Keyword-only         | `def f(*, a)`    | `f(a=1)`                       | Must be passed as keyword        |
| Positional-only      | `def f(a, /)`    | `f(1)`                         | Must be passed positionally      |

---

## Practice Problems

**Problem 1:** Write a function `calculate_average(*args)` that computes the average of any number of numeric arguments. Return `None` if no arguments are passed.

<details>
<summary>Hint</summary>

Use `len(args)` to check for zero arguments. Use `sum(args) / len(args)` for the average.
</details>

<details>
<summary>Solution</summary>

```python
def calculate_average(*args):
    if len(args) == 0:
        return None
    return sum(args) / len(args)

print(calculate_average(10, 20, 30))  # 20.0
print(calculate_average(5))           # 5.0
print(calculate_average())            # None
```
</details>

**Problem 2:** Write a function `create_student_report(name, *scores, grade_scale="A-F")` that prints a student's name, their scores, average, and the grading scale used.

<details>
<summary>Hint</summary>

Use `*scores` for variable-length scores. The `grade_scale` is a keyword-only argument (place it after `*scores`).
</details>

<details>
<summary>Solution</summary>

```python
def create_student_report(name, *scores, grade_scale="A-F"):
    avg = sum(scores) / len(scores) if scores else 0
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.1f}")
    print(f"Grade Scale: {grade_scale}")

create_student_report("Alice", 85, 90, 78, grade_scale="A-F")
```
</details>

**Problem 3:** Write a function `tag_builder(tag, /, content, **attributes)` where `tag` is positional-only, `content` is positional-or-keyword, and `attributes` are variable keyword arguments. The function returns an HTML-style string like `<a href="link" class="btn">Click</a>`.

<details>
<summary>Hint</summary>

Iterate over `attributes.items()` and build the attribute string. Format: `<{tag} {attrs}>{content}</{tag}>`.
</details>

<details>
<summary>Solution</summary>

```python
def tag_builder(tag, /, content, **attributes):
    attrs = ""
    for key, value in attributes.items():
        attrs += f' {key}="{value}"'
    return f"<{tag}{attrs}>{content}</{tag}>"

print(tag_builder("a", "Click here", href="https://example.com", class_="btn"))
# <a href="https://example.com" class="btn">Click here</a>

print(tag_builder("img", "", src="photo.jpg", alt="Photo", width="300"))
# <img src="photo.jpg" alt="Photo" width="300"></img>
```
</details>

**Problem 4:** Write a function `safe_divide(a, b, /, precision=2)` that divides `a` by `b` and returns the result rounded to `precision` decimal places. If `b` is zero, return `"Error: Division by zero"`. Both `a` and `b` must be positional-only.

<details>
<summary>Hint</summary>

Use a `try-except` block or check `if b == 0` before dividing. Use `round(result, precision)`.
</details>

<details>
<summary>Solution</summary>

```python
def safe_divide(a, b, /, precision=2):
    if b == 0:
        return "Error: Division by zero"
    return round(a / b, precision)

print(safe_divide(10, 3))      # 3.33
print(safe_divide(10, 3, precision=4))  # 3.3333
print(safe_divide(5, 0))       # Error: Division by zero
```
</details>
