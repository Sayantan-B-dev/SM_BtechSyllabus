# String Indexing, Operations, and Built-in Functions

**Course:** Python Programming Lab  
**Module:** 2 | **Lecture:** 4  
**Date:** 14-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 2  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Use ord() and chr() functions to work with Unicode code points.
- Build a character frequency counter for a given string.
- Write a word count program that analyzes a text.

## Theory

Every character in Python has a corresponding Unicode code point (an integer). The ord() function takes a single character and returns its integer code point. For example, ord('A') returns 65. The chr() function is the inverse: it takes an integer and returns the corresponding character. These functions are useful for character-level analysis and data encoding tasks.

Character frequency analysis counts how many times each character appears in a string. This is implemented using a dictionary where keys are characters and values are counts. The program iterates through each character in the string, updating the count in the dictionary. This technique is used in cryptography, text analysis, and data compression.

Word counting involves splitting a string into words (using split()), then counting the total number of words, or the frequency of each distinct word. Additional refinements include ignoring case, removing punctuation, and filtering stop words. These programs demonstrate practical text processing that combines strings, dictionaries, and loops.

## Procedure

1. Create a new Python file named lab12.py.
2. Write a program that demonstrates ord() and chr() for a range of characters.
3. Write a character frequency counter that reads a string and prints each character with its count.
4. Write a word count program that reads a paragraph and prints the total word count and frequency of each word.
5. Test all programs with sample text.

## Source Code

```python
# Module 02 Lab 04: ord(), chr(), Character Frequency, Word Count

# Program 1: Demonstrate ord() and chr()
print("ASCII/Unicode values:")
for ch in "ABCabc123":
    print(f"ord('{ch}') = {ord(ch)}")

print()
# chr() demo: print characters from 65 to 75
print("Characters from code points 65 to 75:")
for code in range(65, 76):
    print(f"chr({code}) = '{chr(code)}'")

print()

# Program 2: Character Frequency Counter
text = input("Enter a string for character frequency: ")
freq = {}
for ch in text:
    if ch != ' ':  # skip spaces
        freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequency:")
for ch, count in freq.items():
    print(f"'{ch}': {count}")

print()

# Program 3: Word Count from Text
paragraph = input("Enter a paragraph of text:\n")

# Normalize: lowercase and split
words = paragraph.lower().split()
total_words = len(words)
print(f"\nTotal words: {total_words}")

# Word frequency
word_freq = {}
# Remove punctuation from each word
import string
for word in words:
    clean_word = word.strip(string.punctuation)
    if clean_word:
        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

print("\nWord Frequency:")
# Sort by frequency (descending)
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"'{word}': {count}")
```

## Sample Output

```
ASCII/Unicode values:
ord('A') = 65
ord('B') = 66
ord('C') = 67
ord('a') = 97
ord('b') = 98
ord('c') = 99
ord('1') = 49
ord('2') = 50
ord('3') = 51

Characters from code points 65 to 75:
chr(65) = 'A'
chr(66) = 'B'
chr(67) = 'C'
chr(68) = 'D'
chr(69) = 'E'
chr(70) = 'F'
chr(71) = 'G'
chr(72) = 'H'
chr(73) = 'I'
chr(74) = 'J'
chr(75) = 'K'

Enter a string for character frequency: hello world

Character Frequency:
'h': 1
'e': 1
'l': 3
'o': 2
'w': 1
'r': 1
'd': 1

Enter a paragraph of text:
Python is great. Python is powerful and easy to learn.

Total words: 9

Word Frequency:
'python': 2
'is': 2
'great': 1
'powerful': 1
'and': 1
'easy': 1
'to': 1
'learn': 1
```

## Homework

1. Write a program using ord() to encrypt a string by shifting each character by 3 positions (Caesar cipher). Print both the original and encrypted strings.
2. Write a program that finds and prints the most frequent character in a user-given string (excluding spaces).
3. Write a program that counts the number of lines, words, and characters in a multi-line paragraph (use splitlines() to split into lines).
