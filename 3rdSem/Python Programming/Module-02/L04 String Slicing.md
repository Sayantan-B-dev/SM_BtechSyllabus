# String Slicing

**Course:** Python Programming  
**Module:** 2 | **Lecture:** 4  
**Date:** 05-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 105-142

## Introduction to Slicing

Slicing is a powerful feature in Python that extracts a portion (substring) from a string. The slicing syntax is:

```
string[start:stop:step]
```

- **start**: The index where the slice begins (inclusive). Defaults to 0.
- **stop**: The index where the slice ends (exclusive). Defaults to the end of the string.
- **step**: The increment between each index in the slice. Defaults to 1.

### Basic Slice

```python
text = "PYTHON PROGRAMMING"
#       0123456789...

# Slice from index 0 to 6 (exclusive)
print(text[0:6])         # Output: PYTHON

# Slice from index 7 to 18 (exclusive)
print(text[7:18])        # Output: PROGRAMMING
```

### Visualizing String Indexes

```
String:  P  Y  T  H  O  N     P  R  O  G  R  A  M  M  I  N  G
Index:   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
NegIdx: -18 ...

Slice text[0:6] -> P Y T H O N
Slice text[7:18] -> P R O G R A M M I N G
```

## Omitting Indices

One or more of the three parameters can be omitted, and Python uses sensible defaults.

### Omitting start (defaults to 0)

```python
text = "Hello World"
print(text[:5])          # Output: Hello (equivalent to text[0:5])
```

### Omitting stop (defaults to end of string)

```python
text = "Hello World"
print(text[6:])          # Output: World (from index 6 to end)
```

### Omitting both start and stop (full copy)

```python
text = "Hello World"
print(text[:])           # Output: Hello World (copies the entire string)
```

### Omitting step (defaults to 1)

```python
text = "Hello"
print(text[0:5:1])       # Output: Hello (every character, step 1)
print(text[0:5])         # Output: Hello (step defaults to 1)
```

### Step with Other Parameters

```python
text = "PYTHON PROGRAMMING"

# Every 2nd character from start to end
print(text[::2])         # Output: PTO POMIG

# Every 3rd character from start to end
print(text[::3])         # Output: PN RMN

# Step of 1 (all characters)
print(text[::1])         # Output: PYTHON PROGRAMMING
```

## Using Positive and Negative Indices in Slicing

You can mix positive and negative indices in the same slice.

```python
text = "Python Programming"

# From index 2 to second-last character
print(text[2:-2])        # Output: thon Programmi

# From start to third-last character
print(text[:-3])         # Output: Python Programmi

# From third character to end
print(text[2:])          # Output: thon Programming

# Using all negative indices
print(text[-7:-1])       # Output: amming
```

### Negative Indices in Detail

```python
text = "PYTHON"
#       012345  (positive)
#      -6-5-4-3-2-1  (negative)

print(text[-5:-2])       # Output: YTH (from -5 to -2 exclusive)
print(text[-5:])         # Output: YTHON (from -5 to end)
print(text[:-2])         # Output: PYT (from start to -2 exclusive)
```

## Negative Step (Reversing)

When `step` is negative, Python traverses the string from right to left. The `start` and `stop` semantics flip: `start` should be greater than `stop` for meaningful output.

### Reversing a String

```python
text = "Python"
print(text[::-1])        # Output: nohtyP

# Step -2 (reverse, every 2nd character)
print(text[::-2])        # Output: nhy

# Step -3 (reverse, every 3rd character)
print(text[::-3])        # Output: nh
```

### Negative Step with Start and Stop

When step is negative:
- `start` defaults to the last character (-1)
- `stop` defaults to the beginning (exclusive), so it goes to index 0 inclusive

```python
text = "PYTHON"

# From index 4 to 1 with step -1
print(text[4:1:-1])      # Output: OHT (indexes 4,3,2)

# From index 5 to 0 with step -2
print(text[5:0:-2])      # Output: NTO (indexes 5,3,1)

# From end to index 2 (exclusive) with step -1
print(text[:2:-1])       # Output: NOHT (from -1 to index 2 exclusive)
```

### Understanding Negative Step Behavior

```python
text = "ABCDEFGH"
#       01234567

# From index 7 to 2 (exclusive), moving left
print(text[7:2:-1])      # Output: HGFED (indexes 7,6,5,4,3)

# From index 5 to 1 (exclusive), moving left
print(text[5:1:-1])      # Output: FED (indexes 5,4,3,2)

# From index 3 to -4 (exclusive), moving left
print(text[3:-4:-1])     # Output: (empty) - cannot go left from index 3 to -4
# Correct: from index -4 to 3 with step -1
print(text[-4:3:-1])     # Output: (empty) - 3 and -4 are same, stop is exclusive
```

## Common Slicing Idioms

```python
s = "Hello World Python"

# First n characters
print(s[:5])              # Output: Hello

# Last n characters
print(s[-6:])             # Output: Python

# Characters from position 3 to 8 (exclusive)
print(s[3:8])             # Output: lo Wo

# Everything except first 3 characters
print(s[3:])              # Output: lo World Python

# Everything except last 4 characters
print(s[:-4])             # Output: Hello World Py

# First and last characters
first = s[:1]
last = s[-1:]
print(first, last)        # Output: H n

# Reversing a string
print(s[::-1])            # Output: nohtyP dlroW olleH
```

## Extracting Substrings

### Extracting the Middle

```python
s = "PythonProgramming"

# Extract 'Program'
print(s[6:13])            # Output: Program

# Extract 'thon'
print(s[2:6])             # Output: thon
```

### Extracting Domain from Email

```python
email = "user@example.com"
at_pos = email.index("@")

# Extract username
username = email[:at_pos]
print(username)              # Output: user

# Extract domain
domain = email[at_pos+1:]
print(domain)                # Output: example.com
```

### Extracting File Extension

```python
filename = "document.pdf"
dot_pos = filename.index(".")

# Extract extension
ext = filename[dot_pos+1:]
print(ext)                   # Output: pdf

# Extract name without extension
name = filename[:dot_pos]
print(name)                  # Output: document
```

## Palindrome Check Using Slicing

A palindrome is a string that reads the same forward and backward (e.g., "radar", "madam").

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))      # Output: True
print(is_palindrome("hello"))      # Output: False
print(is_palindrome("madam"))      # Output: True
print(is_palindrome("racecar"))    # Output: True
print(is_palindrome("Python"))     # Output: False
```

### Case-Insensitive Palindrome Check

```python
def is_palindrome_ci(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome_ci("A man a plan a canal Panama"))   # Output: True
print(is_palindrome_ci("No lemon no melon"))             # Output: True
```

## Reversing Strings

### Using Slicing

```python
text = "Python"
reversed_text = text[::-1]
print(reversed_text)       # Output: nohtyP
```

### Using reversed() Function (returns iterator)

```python
text = "Python"
reversed_chars = reversed(text)
print(''.join(reversed_chars))   # Output: nohtyP
```

### Reversing Words in a Sentence

```python
sentence = "Python is fun"
# Reverse the entire string character by character
print(sentence[::-1])            # Output: nuf si nohtyP

# Reverse the order of words
words = sentence.split()
reversed_words = " ".join(words[::-1])
print(reversed_words)            # Output: fun is Python
```

## Extracting Every nth Character

### Every 2nd Character

```python
text = "ABCDEFGHIJ"
print(text[::2])         # Output: ACEGI
print(text[1::2])        # Output: BDFHJ (starting from index 1)
```

### Every 3rd Character

```python
text = "ABCDEFGHIJKLMN"
print(text[::3])         # Output: ADGJM
print(text[1::3])        # Output: BEHKN
print(text[2::3])        # Output: CFIL
```

### Practical: Extract Only Letters at Even Positions

```python
text = "Python Programming"
even_chars = text[::2]
print(even_chars)        # Output: Pto rgamn

odd_chars = text[1::2]
print(odd_chars)         # Output: yhnPormig
```

## Slicing with Variables

```python
text = "Hello World Python"
start = 6
stop = 11
step = 1
print(text[start:stop:step])   # Output: World

# Dynamic slicing
n = 3
print(text[:n])                # Output: Hel
print(text[-n:])               # Output: hon
```

## Edge Cases in Slicing

### Empty Slices

```python
text = "Python"

# Start equals stop
print(text[3:3])         # Output: (empty string)

# Start greater than stop with positive step
print(text[5:2])         # Output: (empty string)

# Start less than stop with negative step
print(text[2:5:-1])      # Output: (empty string)
```

### Out of Bounds Indices

Unlike regular indexing, slicing handles out-of-bounds indices gracefully.

```python
text = "Python"

# Stop beyond string length
print(text[3:100])       # Output: hon

# Start beyond string length
print(text[100:])        # Output: (empty string)

# Negative index beyond string length
print(text[:-100])       # Output: (empty string)
```

### Step of 0 (Error)

```python
text = "Python"
# print(text[::0])       # ValueError: slice step cannot be zero
```

## Practical Examples

### 1. Alternating Characters

```python
text = "Hello World"
alt1 = text[::2]     # Characters at even indexes
alt2 = text[1::2]    # Characters at odd indexes
print(alt1)          # Output: HloWrd
print(alt2)          # Output: el ol
```

### 2. Extracting Initials

```python
full_name = "John Michael Doe"
names = full_name.split()
initials = "".join(name[0] + "." for name in names)
print(initials)       # Output: J.M.D.
```

### 3. URL Parser

```python
url = "https://www.example.com/page"
# Extract protocol
protocol = url[:url.index(":")]
print(protocol)          # Output: https

# Extract domain
domain_start = url.index("//") + 2
domain_end = url.index("/", domain_start)
domain = url[domain_start:domain_end]
print(domain)            # Output: www.example.com
```

### 4. DNA Sequence Analysis

```python
dna = "ATGCGATACGCTTAG"
# Extract every 3rd character starting from index 0
codon_positions = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(codon_positions)   # Output: ['ATG', 'CGA', 'TAC', 'GCT', 'TAG']
```

### 5. Text Wrapping

```python
def wrap_text(text, width):
    return [text[i:i+width] for i in range(0, len(text), width)]

lines = wrap_text("Hello World Python Programming", 5)
print(lines)
# Output: ['Hello', ' Worl', 'd Pyt', 'hon P', 'rogra', 'mming']
```

## Practice Problems

1. **Password Masking**: Write a program that takes a password and shows only the first and last character, replacing the middle with `*`. For example, "Secret123" becomes "S*******3".

   **Hint**: Use slicing to get first, middle, and last parts.

   **Answer**:
   ```python
   password = input("Enter password: ")
   if len(password) <= 2:
       print(password)
   else:
       masked = password[0] + "*" * (len(password) - 2) + password[-1]
       print(masked)
   ```

2. **Every Other Word Reversal**: Write a program that takes a sentence and reverses every other word (2nd, 4th, 6th, ...) using slicing.

   **Hint**: Split the sentence, use slicing with step 2 to select even-indexed words, and reverse them.

   **Answer**:
   ```python
   sentence = input("Enter a sentence: ")
   words = sentence.split()
   for i in range(1, len(words), 2):
       words[i] = words[i][::-1]
   print(" ".join(words))
   ```

3. **Slicing Puzzle**: Given the string `s = "abcdefghij"`, write Python expressions using slicing to produce:
   - "abc"
   - "defg"
   - "jihgfedcba"
   - "acegi"
   - "hfdb"

   **Answer**:
   ```python
   s = "abcdefghij"
   print(s[0:3])       # abc
   print(s[3:7])       # defg
   print(s[::-1])      # jihgfedcba
   print(s[::2])       # acegi
   print(s[-3::-2])    # hfdb
   ```

4. **Binary Palindrome**: Write a program that converts a number to binary and checks if the binary representation is a palindrome using slicing.

   **Answer**:
   ```python
   num = int(input("Enter a number: "))
   binary = bin(num)[2:]  # Remove '0b' prefix
   print(f"Binary: {binary}")
   if binary == binary[::-1]:
       print(f"{num} is a binary palindrome")
   else:
       print(f"{num} is NOT a binary palindrome")
   ```

5. **String Rotation**: Write a function that rotates a string left by `n` positions. For example, rotating "Hello" by 2 gives "lloHe".

   **Hint**: Use slicing: `s[n:] + s[:n]`.

   **Answer**:
   ```python
   def rotate_left(s, n):
       n = n % len(s)
       return s[n:] + s[:n]

   def rotate_right(s, n):
       n = n % len(s)
       return s[-n:] + s[:-n]

   text = input("Enter a string: ")
   n = int(input("Rotate by: "))
   print(f"Left: {rotate_left(text, n)}")
   print(f"Right: {rotate_right(text, n)}")
   ```
