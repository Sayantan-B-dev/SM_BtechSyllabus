# Dictionary Creation, Modification, and Methods

**Course:** Python Programming Lab  
**Module:** 3 | **Lecture:** 5  
**Date:** 04-Sep-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Create dictionaries and access values using keys.
- Add, update, and delete key-value pairs in a dictionary.
- Build a phone book application and a word frequency counter.

## Theory

A dictionary in Python is an unordered, mutable collection of key-value pairs. Keys must be unique and immutable (strings, numbers, tuples). Values can be of any type. Dictionaries are created with curly braces: `d = {"key": "value"}` or using the dict() constructor. Access a value via `d[key]` (raises KeyError if missing) or `d.get(key, default)` (returns default if missing).

Dictionaries are mutable: assign `d[key] = value` to add or update, use `del d[key]` to remove a key (raises KeyError if missing), or `d.pop(key)` to remove and return the value. The `in` operator checks if a key exists. The len() function returns the number of key-value pairs.

Common use cases include counting frequencies (where key is the item and value is the count), storing structured records, and fast lookups. The `for key in dict:` loop iterates over keys. The `.items()` method returns (key, value) tuples for simultaneous iteration. The `.keys()` and `.values()` methods return views of keys and values.

## Procedure

1. Create a new Python file named lab17.py.
2. Create a dictionary with student information and access values by key.
3. Add a new key-value pair, update an existing value, and delete a key.
4. Use .get() for safe access and demonstrate the difference from direct indexing.
5. Build a phone book program that lets the user add, search, and delete contacts.
6. Write a word frequency counter that counts how many times each word appears in a sentence.

## Source Code

```python
# Module 03 Lab 05: Dictionary Creation, Modification, Phone Book, Word Frequency

# Creating and accessing dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}

print(f"Student dictionary: {student}")
print(f"Name: {student['name']}")
print(f"Course: {student['course']}")

# Add, update, delete
student["email"] = "alice@example.com"  # add
print(f"\nAfter adding email: {student}")

student["grade"] = "A+"  # update
print(f"After updating grade: {student}")

del student["email"]  # delete
print(f"After deleting email: {student}")

# Safe access with .get()
print(f"\nUsing .get('name'): {student.get('name')}")
print(f"Using .get('phone'): {student.get('phone')}")
print(f"Using .get('phone', 'N/A'): {student.get('phone', 'N/A')}")

# Phone Book Application
print("\n--- Phone Book ---")
phone_book = {}

while True:
    print("\n1. Add  2. Search  3. Delete  4. Display All  5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phone_book[name] = phone
        print(f"Added {name}.")
    elif choice == 2:
        name = input("Enter name to search: ")
        print(f"Phone: {phone_book.get(name, 'Not found')}")
    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Deleted {name}.")
        else:
            print("Not found.")
    elif choice == 4:
        if phone_book:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("Phone book is empty.")
    elif choice == 5:
        break

# Word Frequency Counter
print("\n--- Word Frequency Counter ---")
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("\nWord frequencies:")
for word, count in freq.items():
    print(f"'{word}': {count}")
```

## Sample Output

```
Student dictionary: {'name': 'Alice', 'age': 20, 'course': 'Computer Science', 'grade': 'A'}
Name: Alice
Course: Computer Science

After adding email: {'name': 'Alice', 'age': 20, 'course': 'Computer Science', 'grade': 'A', 'email': 'alice@example.com'}
After updating grade: {'name': 'Alice', 'age': 20, 'course': 'Computer Science', 'grade': 'A+'}
After deleting email: {'name': 'Alice', 'age': 20, 'course': 'Computer Science', 'grade': 'A+'}

Using .get('name'): Alice
Using .get('phone'): None
Using .get('phone', 'N/A'): N/A

--- Phone Book ---

1. Add  2. Search  3. Delete  4. Display All  5. Exit
Enter choice: 1
Enter name: Bob
Enter phone number: 123-456-7890
Added Bob.

1. Add  2. Search  3. Delete  4. Display All  5. Exit
Enter choice: 4
Bob: 123-456-7890

1. Add  2. Search  3. Delete  4. Display All  5. Exit
Enter choice: 5

--- Word Frequency Counter ---
Enter a sentence: the cat and the dog and the bird
Word frequencies:
'the': 3
'cat': 1
'and': 2
'dog': 1
'bird': 1
```

## Homework

1. Write a program that stores student names as keys and their marks in three subjects as values (a list). Print each student's average.
2. Write a program that counts the frequency of each character in a string (including spaces) and prints the results sorted by character.
3. Write a program that takes two dictionaries and prints the keys that are common to both dictionaries.
