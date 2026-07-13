# Packages and Composition

**Course:** Python Programming  
**Module:** 4 | **Lecture:** 6  
**Date:** 28-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 344-554

## What is a Package?

A package is a way of organizing related modules into a directory hierarchy. A package is simply a directory that contains a special file named `__init__.py` (which can be empty) and one or more module files (`.py` files).

### Package vs Module

- **Module**: A single `.py` file containing Python code.
- **Package**: A directory containing multiple modules and an `__init__.py` file.

```
project/
    main.py              # main script
    shapes/              # package directory
        __init__.py      # makes 'shapes' a package
        circle.py        # module
        rectangle.py     # module
        triangle.py      # module
```

## Creating a Package

### Step 1: Create the Directory Structure

```
shapes/
    __init__.py
    circle.py
    rectangle.py
    triangle.py
```

### Step 2: Create the Modules

**File: `shapes/__init__.py`**

The `__init__.py` file can be empty or contain package initialization code. It is executed when the package is imported.

```python
# shapes/__init__.py
# This file marks the directory as a Python package
# It can be empty, or contain package-level imports and variables

__version__ = "1.0"
print("Initializing shapes package...")
```

**File: `shapes/circle.py`**

```python
"""Module for circle operations."""
import math

def area(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2

def circumference(radius):
    """Calculate circumference of a circle."""
    return 2 * math.pi * radius
```

**File: `shapes/rectangle.py`**

```python
"""Module for rectangle operations."""

def area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def perimeter(length, width):
    """Calculate perimeter of a rectangle."""
    return 2 * (length + width)
```

**File: `shapes/triangle.py`**

```python
"""Module for triangle operations."""

def area(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

def is_valid(a, b, c):
    """Check if three sides can form a valid triangle."""
    return (a + b > c) and (a + c > b) and (b + c > a)
```

### Step 3: Using the Package

```python
# Import the package
import shapes

# Access modules through the package
print("Circle area (r=5):", shapes.circle.area(5))
print("Rectangle area (4x7):", shapes.rectangle.area(4, 7))
```

**Output:**
```
Initializing shapes package...
Circle area (r=5): 78.53981633974483
Rectangle area (4x7): 28
```

## Importing from Packages

### Explicit Module Import

```python
from shapes import circle, rectangle

print(circle.area(3))
print(rectangle.perimeter(4, 5))
```

### Importing Specific Functions

```python
from shapes.circle import area as circle_area
from shapes.rectangle import area as rect_area

print(circle_area(5))
print(rect_area(10, 20))
```

### Importing All from a Module

```python
from shapes.circle import *

print(area(3))
print(circumference(3))
```

### Using `__init__.py` to Simplify Imports

You can import key functions in `__init__.py` so they are available directly from the package.

**File: `shapes/__init__.py`**

```python
"""Shapes package - geometric shape calculations."""

__version__ = "1.0"

from .circle import area as circle_area, circumference
from .rectangle import area as rect_area, perimeter as rect_perimeter
from .triangle import area as triangle_area, is_valid as valid_triangle
```

Now users can do:

```python
import shapes

# Direct access to functions without specifying the submodule
print(shapes.circle_area(5))
print(shapes.rect_area(10, 5))
print(shapes.valid_triangle(3, 4, 5))
```

## Absolute vs Relative Imports

### Absolute Imports

Absolute imports specify the full path from the project root.

```python
from shapes.circle import area
from shapes.rectangle import perimeter
```

### Relative Imports

Relative imports use dots (`.`) to refer to the current and parent packages.

- `.` -- Current package.
- `..` -- Parent package.
- `...` -- Grandparent package.

```python
# Inside shapes/circle.py

# Import from the same package (shapes)
from . import rectangle  # relative import
from .rectangle import perimeter  # import specific function

# Import from parent package
from .. import main  # if main.py is the parent

# Import from sibling subpackage
from ..utils import helpers
```

**Note:** Relative imports only work inside packages and cannot be used in scripts run directly.

### Example of Relative Import

```python
# Inside shapes/circle.py
from .rectangle import area as rect_area

def compare_areas(circle_r, rect_l, rect_w):
    """Compare area of a circle with area of a rectangle."""
    return area(circle_r) - rect_area(rect_l, rect_w)
```

## Using `__all__` to Control What Gets Exported

The `__all__` variable in a module or `__init__.py` defines what is imported when `from module import *` is used.

**File: `shapes/circle.py`**

```python
__all__ = ["area", "circumference"]  # only these are exported with *

import math

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

def _helper_function(radius):  # private (by convention)
    return radius * 2
```

By convention, names starting with underscore (`_`) are considered private.

## Third-Party Packages and PyPI

PyPI (Python Package Index) is the official repository for third-party Python packages.

### Using `pip` to Install Packages

```bash
# Install a package
pip install requests

# Install a specific version
pip install numpy==1.21.0

# Install multiple packages
pip install requests pandas matplotlib

# Install from requirements file
pip install -r requirements.txt

# List installed packages
pip list

# Uninstall a package
pip uninstall requests
```

### Example: Using the `requests` Package (Third-Party)

```python
import requests

# Make an HTTP GET request
response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
print("Content type:", response.headers["content-type"])
print("JSON data:", response.json())
```

### Example: Using `numpy` and `matplotlib`

```python
import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
```

## Creating a `requirements.txt` File

This file lists all dependencies for a project.

```
# requirements.txt
requests==2.28.1
numpy>=1.21.0
matplotlib>=3.5.0
pandas==1.4.3
```

```bash
pip install -r requirements.txt
```

## Virtual Environments (`venv`)

A virtual environment creates an isolated Python environment for each project, preventing conflicts between package versions.

### Creating and Using a Virtual Environment

```bash
# Create a virtual environment (Python 3.3+)
python -m venv myproject_env

# Activate the environment
# On Windows:
myproject_env\Scripts\activate

# On macOS/Linux:
source myproject_env/bin/activate

# The prompt changes to show the environment name
# Now install packages inside this environment
pip install requests pandas

# Deactivate the environment
deactivate
```

### Why Virtual Environments?

- Different projects can use different versions of the same package.
- Avoids polluting the global Python installation.
- Makes it easy to list and manage project dependencies.
- Enables reproducible builds.

### Example Workflow

```bash
# Create project
mkdir my_project
cd my_project

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install packages
pip install flask requests

# Freeze dependencies to requirements.txt
pip freeze > requirements.txt

# Later, someone else can recreate the environment
# pip install -r requirements.txt

# Deactivate when done
deactivate
```

## Complete Example: Building and Using a Simple Package

### Step 1: Create the Package Structure

```
text_utils/
    __init__.py
    formatting.py
    analysis.py
```

**File: `text_utils/__init__.py`**

```python
"""Text utilities package."""

__version__ = "0.1.0"

from .formatting import capitalize_words, reverse_text, strip_punctuation
from .analysis import word_count, char_count, average_word_length
```

**File: `text_utils/formatting.py`**

```python
"""Text formatting functions."""

def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return text.title()

def reverse_text(text):
    """Reverse the entire text."""
    return text[::-1]

def strip_punctuation(text):
    """Remove common punctuation marks from text."""
    import string
    return text.translate(str.maketrans("", "", string.punctuation))
```

**File: `text_utils/analysis.py`**

```python
"""Text analysis functions."""

def word_count(text):
    """Count the number of words in text."""
    return len(text.split())

def char_count(text):
    """Count the number of characters (excluding spaces)."""
    return len(text.replace(" ", ""))

def average_word_length(text):
    """Calculate the average length of words."""
    words = text.split()
    if not words:
        return 0
    total_chars = sum(len(word) for word in words)
    return total_chars / len(words)
```

### Step 2: Use the Package

```python
import text_utils

sample = "Hello, world! Welcome to Python programming."

print("Original:", sample)
print("Capitalized:", text_utils.capitalize_words(sample))
print("Reversed:", text_utils.reverse_text(sample))
print("No punctuation:", text_utils.strip_punctuation(sample))
print("Word count:", text_utils.word_count(sample))
print("Char count:", text_utils.char_count(sample))
print("Avg word length:", round(text_utils.average_word_length(sample), 2))
```

**Output:**
```
Original: Hello, world! Welcome to Python programming.
Capitalized: Hello, World! Welcome To Python Programming.
Reversed: .gnimmargorp nohtyP ot emocleW !dlrow ,olleH
No punctuation: Hello world Welcome to Python programming
Word count: 6
Char count: 32
Avg word length: 5.33
```

### Step 3: Add Package Metadata (Optional)

Create a `setup.py` file to make the package installable:

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="text_utils",
    version="0.1.0",
    packages=find_packages(),
    description="A simple text utility package",
    author="Your Name",
    python_requires=">=3.6",
)
```

Then install in development mode:

```bash
pip install -e .
```

## Nested Packages

You can create subpackages within packages:

```
analytics/
    __init__.py
    data/
        __init__.py
        loading.py
        cleaning.py
    models/
        __init__.py
        statistics.py
        visualization.py
```

```python
import analytics.data.loading
from analytics.models.statistics import mean, median
```

## Summary: Package vs Module Comparison

| Feature        | Module                          | Package                          |
|----------------|---------------------------------|----------------------------------|
| Definition     | A single `.py` file             | A directory with `__init__.py`   |
| Purpose        | Groups related functions/classes| Groups related modules           |
| Import         | `import module_name`            | `import package_name`            |
| Access         | `module_name.function()`        | `package.module.function()`      |
| Files          | One `.py` file                  | Directory with `__init__.py`     |

---

## Practice Problems

**Problem 1:** Create a package `calculator` with two modules: `basic.py` (add, subtract, multiply, divide) and `advanced.py` (power, sqrt, factorial_mod). Write a script that imports and uses all functions.

<details>
<summary>Hint</summary>

Create the directory `calculator/` with `__init__.py` that imports from both modules.
</details>

<details>
<summary>Solution</summary>

**Directory structure:**
```
calculator/
    __init__.py
    basic.py
    advanced.py
```

**File: `calculator/basic.py`**

```python
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Error"
    return a / b
```

**File: `calculator/advanced.py`**

```python
def power(a, b): return a ** b
def sqrt(a): return a ** 0.5
def factorial_mod(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**File: `calculator/__init__.py`**

```python
from .basic import add, subtract, multiply, divide
from .advanced import power, sqrt, factorial_mod
```

**Script:**

```python
import calculator

print(calculator.add(10, 5))
print(calculator.power(2, 10))
print(calculator.factorial_mod(5))
```
</details>

**Problem 2:** Install the `requests` package using pip, then write a script to fetch and print the current weather for a city using a free API (e.g., `wttr.in`).

<details>
<summary>Hint</summary>

Use `pip install requests` first. Then use `requests.get("https://wttr.in/London?format=3")`.
</details>

<details>
<summary>Solution</summary>

```bash
pip install requests
```

```python
import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=3"
response = requests.get(url)
print(response.text)
```
</details>

**Problem 3:** Create a virtual environment called `project_env`, activate it, install the `numpy` package, write a Python script that computes the dot product of two vectors using `numpy`, then capture the `pip freeze` output. Provide all shell commands and the script.

<details>
<summary>Hint</summary>

Use `python -m venv project_env`, then activate, then `pip install numpy`, then write the script.
</details>

<details>
<summary>Solution</summary>

```bash
# Create and activate
python -m venv project_env
project_env\Scripts\activate   # Windows
# source project_env/bin/activate  # macOS/Linux

# Install
pip install numpy

# Create script: dot_product.py
```

```python
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
result = np.dot(v1, v2)
print(f"Dot product: {result}")  # 1*4 + 2*5 + 3*6 = 32
```

```bash
# Run
python dot_product.py

# Freeze
pip freeze > requirements.txt

deactivate
```
</details>

**Problem 4:** Using relative imports, create a package `company` with subpackages `hr` and `it`. `hr` has `employees.py` (function `employee_count()`), `it` has `systems.py` (function `server_status()`). In a sibling module, import from the sibling subpackage using relative imports.

<details>
<summary>Hint</summary>

In `hr/employees.py`, use `from ..it.systems import server_status` for a relative import.
</details>

<details>
<summary>Solution</summary>

```
company/
    __init__.py
    hr/
        __init__.py
        employees.py
    it/
        __init__.py
        systems.py
```

**File: `company/__init__.py`** (empty)

**File: `company/hr/__init__.py`** (empty)

**File: `company/it/__init__.py`** (empty)

**File: `company/hr/employees.py`**

```python
from ..it.systems import server_status

def employee_count():
    return 42

def check_server():
    return server_status()
```

**File: `company/it/systems.py`**

```python
def server_status():
    return "All systems operational"
```

**Usage from outside:**

```python
from company.hr.employees import employee_count, check_server

print(employee_count())
print(check_server())
```

**Output:**
```
42
All systems operational
```
</details>
