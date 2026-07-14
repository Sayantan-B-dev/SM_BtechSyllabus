# Setting up Path and Working with Python

**Course:** Python Programming  
**Module:** 1 | **Lecture:** 2  
**Date:** 08-Jul-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 2-98

## Notes

### 1. Downloading and Installing Python

**Step 1: Download Python**

1. Open your web browser and go to [python.org](https://www.python.org).
2. Hover over the **Downloads** tab. The website will automatically suggest the latest version for your operating system.
3. Click the download button (e.g., "Download Python 3.12.x").
4. The installer file (`.exe` on Windows) will begin downloading.

**Step 2: Install Python (Windows)**

1. Locate the downloaded installer (usually in your `Downloads` folder).
2. **CRITICAL:** On the first screen of the installer, check the box that says **"Add Python to PATH"** at the bottom. This is very important -- it allows you to run `python` from the command prompt.
3. Click **"Install Now"** (recommended) or choose **"Customize installation"** if you want to change the install location.
4. Wait for the installation to complete, then click **"Close"**.

**Step 3: Verify Installation -- Command Prompt Method**

Open a **Command Prompt** (press `Win + R`, type `cmd`, press Enter) and run:

```cmd
python --version
```

Expected output (your version may differ):

```
Python 3.12.2
```

Also verify that `pip` (Python's package manager) is installed:

```cmd
pip --version
```

Expected output:

```
pip 24.0 from C:\Python312\Lib\site-packages\pip (python 3.12)
```

If you see version numbers, Python and pip are installed correctly.

---

### 2. What is PATH and Why Does It Matter?

The **PATH** is an environment variable that tells the operating system where to look for executable programs.

When you type `python` in the Command Prompt, Windows searches every directory listed in the PATH variable for an executable named `python.exe`. If Python's installation folder (e.g., `C:\Python312\`) is in PATH, Windows finds and runs it. If not, you get an error like:

```
'python' is not recognized as an internal or external command,
operable program or batch file.
```

**If you forgot to check "Add Python to PATH" during installation:**

1. Open **System Properties** (press `Win + Pause/Break` or right-click "This PC" -> Properties).
2. Click **"Advanced system settings"** on the left.
3. Click **"Environment Variables..."** at the bottom.
4. In the "System variables" section, scroll and select the **Path** variable, then click **"Edit..."**.
5. Click **"New"** and add these two paths (adjust version number if different):
   - `C:\Python312`
   - `C:\Python312\Scripts`
6. Click OK on all dialogs.
7. Restart Command Prompt and run `python --version` again.

---

### 3. Running Python: Two Modes

Python offers two ways to run code:

#### 3.1 Interactive Mode (REPL)

REPL stands for **Read-Eval-Print Loop**. It lets you type Python code one line at a time and see the result immediately.

To start the interactive shell, open Command Prompt and type:

```cmd
python
```

You will see something like:

```
Python 3.12.2 (tags/v3.12.2:12345678, Feb  6 2026, 14:23:15) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the **prompt**. You can type Python code here:

```python
>>> 2 + 3
5
>>> print("Hello from REPL")
Hello from REPL
>>> x = 10
>>> x * 2
20
```

To exit the REPL, type `exit()` or press `Ctrl + Z` then Enter (on Windows), or `Ctrl + D` (on Linux/Mac).

**Use case:** Quick testing, experimenting with small code snippets, learning new features.

#### 3.2 Script Mode

In script mode, you write Python code in a file (with `.py` extension) and run the entire file at once.

1. Create a file named `hello.py` using any text editor.
2. Write your code:

```python
print("Hello, World!")
print("This is a Python script.")
```

3. Run it from Command Prompt:

```cmd
python hello.py
```

Output:

```
Hello, World!
This is a Python script.
```

**Use case:** Building complete programs, reusable code, projects.

---

### 4. Writing Your First Program: "Hello, World!"

Every programming course starts with a program that prints "Hello, World!" to the screen. Here is the Python version:

```python
print("Hello, World!")
```

**Explanation:**
- `print()` is a built-in Python function that displays text on the screen.
- The text `"Hello, World!"` is a **string literal** (a sequence of characters enclosed in double quotes).
- The parentheses `()` are required. In Python 3, `print` is a function, not a statement.

Run this program and you should see:

```
Hello, World!
```

---

### 5. Using IDLE

**IDLE** (Integrated Development and Learning Environment) is Python's built-in IDE. It comes bundled with the standard Python installation.

**To start IDLE:**
- Search for "IDLE" in the Start Menu and click it.
- Or navigate to `C:\Python312\Lib\idlelib\idle.pyw` and double-click.

**Features of IDLE:**
- **Python Shell:** An interactive REPL window (same as the command-line REPL but with syntax highlighting).
- **File Editor:** Click `File -> New File` to open an editor window. Write your script there.
- **Run Script:** Press `F5` (or click `Run -> Run Module`) to execute the script in the shell window.
- **Syntax Highlighting:** Code is color-coded (keywords in orange, strings in green, etc.).
- **Auto-indentation:** IDLE automatically indents your code after a colon (`:`).

**Example in IDLE:**
1. Open IDLE.
2. Click `File -> New File`.
3. Type: `print("Hello from IDLE!")`
4. Press `F5`. You will be prompted to save the file. Save it as `idle_demo.py`.
5. The output appears in the Python Shell window.

---

### 6. Using VS Code with the Python Extension

VS Code is a free, powerful code editor from Microsoft. With the Python extension, it becomes an excellent Python IDE.

**Step 1: Install VS Code**
- Download from [code.visualstudio.com](https://code.visualstudio.com).
- Run the installer (accept default options).

**Step 2: Install the Python Extension**
1. Open VS Code.
2. Click the **Extensions** icon on the left sidebar (or press `Ctrl + Shift + X`).
3. Search for "Python".
4. Click "Install" on the extension published by Microsoft (the one with the blue icon).

**Step 3: Create and Run a Python File**
1. Click `File -> New File` (or `Ctrl + N`).
2. Save the file as `hello.py` (`Ctrl + S`).
3. Type your code:

```python
print("Hello from VS Code!")
```

4. Right-click anywhere in the editor and select **"Run Python File in Terminal"**.
5. The output appears in the terminal panel at the bottom:

```
Hello from VS Code!
```

**Alternative: Using the Integrated Terminal**
1. Open the terminal: `View -> Terminal` (or `Ctrl + ``).
2. Type: `python hello.py` and press Enter.

**Useful VS Code features for Python:**
- **IntelliSense:** Automatic code completion as you type.
- **Syntax highlighting:** Color-coded code.
- **Linting:** Catches errors (e.g., missing parentheses) before you run the code.
- **Debugger:** Step through your code line by line to find bugs.
- **Run button:** A play button appears in the top right of the editor for `.py` files.

---

### 7. Common Installation Issues and Solutions

| Problem | Solution |
|---|---|
| `'python' is not recognized` | Python not in PATH. Reinstall with "Add to PATH" checked, or manually add to PATH. |
| `'pip' is not recognized` | Pip not in PATH. Add `C:\Python312\Scripts` to PATH. |
| `python` opens Microsoft Store | This happens if Python is not installed and Windows redirects. Install Python properly. |
| VS Code says "Python interpreter not selected" | Press `Ctrl + Shift + P`, type "Python: Select Interpreter", and choose your Python installation. |

---

## Practice Problems

1. **Installation Check:** Open Command Prompt and run `python --version` and `pip --version`. Write down the output you see.
   <details>
   <summary>Show Answer</summary>
   Sample output: `Python 3.12.5` and `pip 24.2 from C:\...\site-packages\pip (python 3.12)`. Your actual versions may differ.
   </details>

2. **REPL Practice:** Open the Python interactive shell and evaluate the following expressions one by one:
   - `15 + 7`
   - `10 * 3`
   - `"Hello" + " " + "World"`
   - `2 ** 10`
   <details>
   <summary>Show Answer</summary>
   Results: `22`, `30`, `"Hello World"`, `1024`.
   </details>

3. **Script Practice:** Create a file `myname.py` that prints your name, your age, and your favorite color on three separate lines. Run it and note the output.
   <details>
   <summary>Show Answer</summary>
   ```python
   # myname.py
   print("Alice")
   print(20)
   print("Blue")
   ```
   Output:
   ```
   Alice
   20
   Blue
   ```
   </details>

4. **Error Exploration:** In the REPL, type `print("Hello"` (intentionally missing the closing parenthesis). What error do you get?
   <details>
   <summary>Show Answer</summary>
   You get a `SyntaxError: '(' was never closed` (or `unexpected EOF while parsing`). The REPL may also show a continuation prompt `...` because it expects the rest of the expression.
   </details>

5. **IDLE vs VS Code:** Open `myname.py` in both IDLE and VS Code. Run it in both environments. Which do you prefer and why?
   <details>
   <summary>Show Answer</summary>
   Sample preference: VS Code is preferred because it offers syntax highlighting, integrated terminal, linting, debugging, and extensions. IDLE is simpler and lighter but lacks advanced features. (Your answer will depend on personal experience.)
   </details>
