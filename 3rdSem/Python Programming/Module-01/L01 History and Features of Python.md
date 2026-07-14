# History and Features of Python

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 1  
**Date:** 08-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

### 1. History of Python

Python was created by **Guido van Rossum**, a Dutch programmer. Work on Python began in the late 1980s, and the first public release (Python 0.9.0) came out in **1991**. The name "Python" was inspired by the British comedy series "Monty Python's Flying Circus" -- Guido was reading the published scripts from the show and wanted a name that was short, unique, and slightly mysterious.

**Key milestones:**

- **1991:** Python 0.9.0 released. It already had classes with inheritance, exception handling, functions, and the core data types (list, dict, str, etc.).
- **1994:** Python 1.0 released. Included functional programming tools like `lambda`, `map`, `filter`, and `reduce`.
- **2000:** Python 2.0 released. Major new features included list comprehensions, garbage collection, and Unicode support.
- **2008:** Python 3.0 (also called Python 3000 or Py3K) released. This was a deliberate **backward-incompatible** release. Python 3 cleaned up many design flaws in Python 2.
- **2020:** Python 2 was officially end-of-lifed (2.7.18 was the final release). All developers were urged to migrate to Python 3.

**Python 2 vs Python 3 -- Major Differences:**

| Feature | Python 2 | Python 3 |
|---|---|---|
| `print` is a statement | `print "Hello"` | `print("Hello")` |
| Integer division | `3 / 2` gives `1` | `3 / 2` gives `1.5` |
| `input()` function | `input()` evaluates input as code; `raw_input()` for strings | `input()` always returns a string |
| Unicode | Strings are ASCII by default; `u"..."` for Unicode | Strings are Unicode by default |
| `range()` | returns a list | returns a range object (memory-efficient) |
| `xrange()` | existed for efficient iteration | removed (use `range()`) |
| Exception syntax | `except Exception, e:` | `except Exception as e:` |

Today, **Python 3.x** is the standard. You should always install Python 3.

---

### 2. Key Features of Python

#### 2.1 Interpreted Language
Python is an **interpreted** (not compiled) language. The Python interpreter reads your code line by line and executes it immediately. This makes development faster because there is no separate compile step. You can also run Python code interactively.

#### 2.2 Dynamically Typed
You do not need to declare the type of a variable. Python infers the type at runtime.

```python
x = 10        # x is an integer
x = "hello"   # now x is a string -- no error
```

This is different from statically typed languages like Java or C++ where the type of a variable is fixed at declaration.

#### 2.3 Object-Oriented
Python supports object-oriented programming. Everything in Python is an object -- even integers, strings, and functions. You can define classes, create objects, use inheritance, polymorphism, and encapsulation.

```python
class Dog:
    def bark(self):
        return "Woof!"
```

#### 2.4 Batteries Included
Python comes with a **large standard library** that includes modules for:
- File I/O (`os`, `shutil`, `pathlib`)
- Networking (`socket`, `http`, `urllib`)
- Data processing (`json`, `csv`, `xml`)
- Mathematics (`math`, `random`, `statistics`)
- Web development (`http.server`)
- Testing (`unittest`)
- And many more

This "batteries included" philosophy means you can do a lot without installing third-party packages.

#### 2.5 Cross-Platform
Python runs on Windows, macOS, Linux, and many other platforms. Python code written on one operating system typically runs unchanged on another (as long as you avoid platform-specific features).

#### 2.6 Easy to Read and Write
Python's syntax emphasizes readability. It uses indentation (whitespace) to define code blocks instead of curly braces `{}` or keywords like `begin`/`end`. This makes Python code clean and easy to understand.

#### 2.7 High-Level Language
Python handles memory management (garbage collection), low-level data structures, and other complex details automatically. Programmers can focus on solving problems rather than managing memory.

---

### 3. Applications of Python

Python is a **general-purpose** language used in many fields:

#### 3.1 Web Development
Frameworks like **Django** and **Flask** make it easy to build web applications. Django is a full-featured framework (includes an ORM, admin panel, authentication). Flask is a lightweight micro-framework.

#### 3.2 Data Science and Data Analysis
Libraries like **NumPy** (numerical computing), **Pandas** (data manipulation), and **Matplotlib** (visualization) make Python a leading choice for data analysis.

#### 3.3 Artificial Intelligence and Machine Learning
**TensorFlow**, **PyTorch**, **scikit-learn**, and **Keras** are popular Python libraries for building machine learning and deep learning models.

#### 3.4 Automation and Scripting
Python is excellent for writing scripts to automate repetitive tasks: renaming files, scraping websites, sending emails, processing data, and more.

#### 3.5 Desktop GUI Applications
Libraries like **Tkinter** (built-in), **PyQt**, and **Kivy** allow building cross-platform desktop applications.

#### 3.6 Game Development
**Pygame** is a popular library for building 2D games.

#### 3.7 Scientific Computing
**SciPy**, **SymPy**, and **Jupyter Notebooks** are widely used in scientific research and engineering.

---

### 4. The Zen of Python (PEP 20)

To understand Python's design philosophy, open a Python interpreter and type:

```python
import this
```

This prints "The Zen of Python" by Tim Peters -- a collection of guiding principles:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- There should be one -- and preferably only one -- obvious way to do it.
- Now is better than never.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.

These principles guide Python's design and explain why Python looks and behaves the way it does.

---

### 5. Why Python for Beginners?

Python is widely recommended as a first programming language for several reasons:

1. **Gentle Learning Curve:** Python's syntax is close to plain English. A beginner can write useful programs after just a few lessons.
2. **Immediate Feedback:** The interactive REPL (Read-Eval-Print Loop) lets you test code instantly without writing a full program.
3. **Fewer Distractions:** No curly braces, no semicolons, no type declarations. Beginners can focus on logic and problem solving.
4. **Huge Community:** Millions of Python developers worldwide. Abundant tutorials, documentation, Stack Overflow answers, and video courses.
5. **Versatile:** Python is used in web development, data science, AI, automation, and more. A beginner can explore many domains without learning a new language.
6. **Rich Ecosystem:** The Python Package Index (PyPI) has over 400,000 packages. Whatever you want to do, someone has probably built a library for it.

---

## Practice Problems

1. **Research:** Find out which version of Python is currently the latest stable release. Compare it to the version installed on your computer.
   <details>
   <summary>Show Answer</summary>
   As of mid-2026, the latest stable release is Python 3.14. You can check your installed version by running `python --version` in a terminal. Compare the output to the latest on python.org to see if an upgrade is available.
   </details>

2. **Reflection:** Write down two features of Python that seem most interesting to you. Explain why they would help a beginner programmer.
   <details>
   <summary>Show Answer</summary>
   Two key features: (1) **Readable syntax** — Python uses indentation instead of braces, making code clean and easy to read. (2) **Batteries included** — the vast standard library means beginners can do file I/O, web requests, etc. without installing extra packages.
   </details>

3. **Short Answer:** What does "batteries included" mean in the context of Python?
   <details>
   <summary>Show Answer</summary>
   "Batteries included" means Python ships with a large standard library that provides modules and functions for common tasks (file handling, networking, data structures, etc.) out of the box, so you don't need to install third-party packages for basic functionality.
   </details>

4. **Comparison:** List three differences between Python 2 and Python 3.
   <details>
   <summary>Show Answer</summary>
   Three differences: (1) `print` is a statement in Python 2 (`print "Hello"`) but a function in Python 3 (`print("Hello")`). (2) Integer division: `3/2` gives `1` in Python 2 but `1.5` in Python 3. (3) `raw_input()` in Python 2 is renamed to `input()` in Python 3; the old `input()` (which evaluated input as code) was removed.
   </details>

5. **Reading:** Go to python.org and read the "Beginners Guide" section. Note down three things you learned.
   <details>
   <summary>Show Answer</summary>
   Sample answers: (1) Python can be downloaded from python.org and comes with IDLE, a simple IDE. (2) The Beginners Guide links to tutorials, books, and interactive courses. (3) Python is used in web development, data science, automation, and education. (Your actual answers will vary based on what you read.)
   </details>
