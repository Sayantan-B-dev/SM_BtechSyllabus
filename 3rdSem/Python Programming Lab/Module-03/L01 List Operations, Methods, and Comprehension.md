# List Operations, Methods, and Comprehension

**Course:** Python Programming Lab  
**Module:** 3 | **Lecture:** 1  
**Date:** 21-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Create lists and access elements using indexing and slicing.
- Use list methods: append(), extend(), insert(), remove(), pop().
- Write a list operations menu program and a duplicate removal program.

## Theory

A list in Python is an ordered, mutable collection of elements enclosed in square brackets []. Lists can contain elements of different types, including other lists. Lists are mutable, meaning elements can be added, removed, or modified after creation. Indexing and slicing work the same way as with strings.

Key list methods: append(item) adds an item to the end. extend(iterable) adds all elements of an iterable. insert(index, item) inserts at a specific position. remove(item) removes the first occurrence of the item (raises ValueError if not found). pop(index) removes and returns the item at the given index (or the last item if no index given). del list[index] deletes by index without returning.

List operations use the + operator for concatenation and * for repetition. The len() function returns the number of elements. The in operator checks membership. Removing duplicates can be done by converting to a set and back, or by iterating and building a new list.

## Procedure

1. Create a new Python file named lab13.py.
2. Create a list with mixed data types. Demonstrate indexing and slicing.
3. Demonstrate append(), extend(), insert(), remove(), and pop().
4. Write an interactive menu-driven program that lets the user perform list operations.
5. Write a program that removes duplicates from a list while preserving order.
6. Test all programs.

## Source Code

```python
# Module 03 Lab 01: List Creation, Indexing, Methods

# Basic list creation and indexing
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Sliced [1:4]: {numbers[1:4]}")
print(f"Length: {len(numbers)}")

# List methods
fruits = ["apple", "banana"]
print(f"\nInitial fruits: {fruits}")

fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

fruits.extend(["date", "elderberry"])
print(f"After extend(): {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert(1, 'blueberry'): {fruits}")

fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

popped = fruits.pop()
print(f"After pop(): {fruits}, popped: {popped}")

popped_at = fruits.pop(2)
print(f"After pop(2): {fruits}, popped: {popped_at}")

# Menu-driven list operations
print("\n--- List Operations Menu ---")
my_list = []
while True:
    print("\n1. Append  2. Insert  3. Remove  4. Pop  5. Display  6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        val = input("Enter value: ")
        my_list.append(val)
    elif choice == 2:
        val = input("Enter value: ")
        idx = int(input("Enter index: "))
        my_list.insert(idx, val)
    elif choice == 3:
        val = input("Enter value to remove: ")
        if val in my_list:
            my_list.remove(val)
        else:
            print("Not found.")
    elif choice == 4:
        if my_list:
            print(f"Popped: {my_list.pop()}")
        else:
            print("List is empty.")
    elif choice == 5:
        print(f"List: {my_list}")
    elif choice == 6:
        break

# Removing duplicates preserving order
original = [1, 2, 3, 2, 4, 1, 5, 3, 6]
unique = []
for item in original:
    if item not in unique:
        unique.append(item)
print(f"\nOriginal: {original}")
print(f"Without duplicates: {unique}")
```

## Sample Output

```
List: [10, 20, 30, 40, 50]
First element: 10
Last element: 50
Sliced [1:4]: [20, 30, 40]
Length: 5

Initial fruits: ['apple', 'banana']
After append('cherry'): ['apple', 'banana', 'cherry']
After extend(): ['apple', 'banana', 'cherry', 'date', 'elderberry']
After insert(1, 'blueberry'): ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
After remove('banana'): ['apple', 'blueberry', 'cherry', 'date', 'elderberry']
After pop(): ['apple', 'blueberry', 'cherry', 'date'], popped: elderberry
After pop(2): ['apple', 'blueberry', 'date'], popped: cherry

--- List Operations Menu ---

1. Append  2. Insert  3. Remove  4. Pop  5. Display  6. Exit
Enter choice: 1
Enter value: hello

1. Append  2. Insert  3. Remove  4. Pop  5. Display  6. Exit
Enter choice: 5
List: ['hello']

1. Append  2. Insert  3. Remove  4. Pop  5. Display  6. Exit
Enter choice: 6

Original: [1, 2, 3, 2, 4, 1, 5, 3, 6]
Without duplicates: [1, 2, 3, 4, 5, 6]
```

## Homework

1. Write a program that takes 5 numbers from the user and stores them in a list, then prints the sum, maximum, and minimum.
2. Write a program that rotates a list to the left by one position (e.g., [1,2,3,4] -> [2,3,4,1]).
3. Write a program that takes two lists and prints their intersection (common elements) without using sets.
