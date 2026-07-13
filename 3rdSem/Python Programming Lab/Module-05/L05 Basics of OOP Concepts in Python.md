# Basics of OOP Concepts in Python

**Course:** Python Programming Lab  
**Module:** 5 | **Lecture:** 5  
**Date:** 30-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Define classes and create objects in Python.
- Use the __init__() constructor to initialize object attributes.
- Use the __str__() method for string representation.
- Implement a Student class and a Book class with attributes and methods.

## Theory

Object-Oriented Programming (OOP) is a paradigm that organizes code into classes (blueprints) and objects (instances). A class defines the attributes (data) and methods (functions) that its objects will have. In Python, classes are defined using the `class` keyword: `class ClassName:`. By convention, class names use PascalCase.

The __init__() method is the constructor, automatically called when an object is created. It initializes the object's attributes using the `self` parameter, which refers to the current instance. For example: `def __init__(self, name, age): self.name = name`. The __str__() method returns a human-readable string representation of the object, used by print() and str().

Instance methods are functions defined inside a class that take `self` as the first parameter. They can access and modify the object's attributes. Classes allow bundling related data and behavior together, making code more organized, reusable, and easier to maintain compared to procedural programming.

## Procedure

1. Create a new Python file named lab29.py.
2. Define a Student class with __init__() that accepts name, roll_number, and marks.
3. Add instance methods: display_info(), calculate_percentage(), is_passed().
4. Override __str__() to return a formatted string.
5. Create multiple Student objects and call their methods.
6. Define a Book class with attributes: title, author, isbn, price.
7. Add methods: apply_discount(), display_book().
8. Create Book objects and test the methods.

## Source Code

```python
# Module 05 Lab 05: Class and Object, __init__, __str__
# Student class and Book class

class Student:
    """Represents a student with name, roll number, and marks."""

    def __init__(self, name, roll_number, marks):
        """Initialize a new Student object."""
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # list of marks in subjects

    def display_info(self):
        """Display student details."""
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def calculate_percentage(self):
        """Calculate and return the average percentage."""
        if len(self.marks) == 0:
            return 0.0
        total = sum(self.marks)
        return total / len(self.marks)

    def is_passed(self, passing_marks=40):
        """Check if student passed all subjects."""
        return all(mark >= passing_marks for mark in self.marks)

    def __str__(self):
        """Return a string representation of the Student."""
        percentage = self.calculate_percentage()
        return f"Student({self.name}, Roll: {self.roll_number}, Percentage: {percentage:.1f}%)"


print("--- Student Class Demo ---")
# Create Student objects
s1 = Student("Alice", 101, [85, 90, 78, 92, 88])
s2 = Student("Bob", 102, [45, 38, 52, 60, 55])
s3 = Student("Charlie", 103, [95, 93, 97, 89, 91])

# Display and test methods
for student in [s1, s2, s3]:
    print()
    student.display_info()
    print(f"Percentage: {student.calculate_percentage():.1f}%")
    print(f"Passed All: {student.is_passed()}")
    print(str(student))


class Book:
    """Represents a book with title, author, isbn, and price."""

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def apply_discount(self, discount_percent):
        """Apply a percentage discount to the price."""
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount
        return self.price

    def display_book(self):
        """Display book details."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Price: ${self.price:.2f}")

    def __str__(self):
        return f"Book('{self.title}' by {self.author}, ${self.price:.2f})"


print("\n\n--- Book Class Demo ---")
b1 = Book("Python Programming", "John Doe", "978-3-16-148410-0", 49.99)
b2 = Book("Data Science 101", "Jane Smith", "978-0-12-345678-9", 59.99)

b1.display_book()
print()
b2.display_book()

print("\nAfter 20% discount on Book 1:")
b1.apply_discount(20)
print(f"New price: ${b1.price:.2f}")
print(str(b1))
```

## Sample Output

```
--- Student Class Demo ---

Name: Alice
Roll Number: 101
Marks: [85, 90, 78, 92, 88]
Percentage: 86.6%
Passed All: True
Student(Alice, Roll: 101, Percentage: 86.6%)

Name: Bob
Roll Number: 102
Marks: [45, 38, 52, 60, 55]
Percentage: 50.0%
Passed All: False
Student(Bob, Roll: 102, Percentage: 50.0%)

Name: Charlie
Roll Number: 103
Marks: [95, 93, 97, 89, 91]
Percentage: 93.0%
Passed All: True
Student(Charlie, Roll: 103, Percentage: 93.0%)


--- Book Class Demo ---
Title: Python Programming
Author: John Doe
ISBN: 978-3-16-148410-0
Price: $49.99

Title: Data Science 101
Author: Jane Smith
ISBN: 978-0-12-345678-9
Price: $59.99

After 20% discount on Book 1:
New price: $39.99
Book('Python Programming' by John Doe, $39.99)
```

## Homework

1. Create a BankAccount class with attributes: account_number, holder_name, balance. Methods: deposit(amount), withdraw(amount), display_balance(). Ensure withdrawal does not allow balance to go negative.
2. Create a Rectangle class with length and width attributes. Methods: area(), perimeter(), is_square(). The __str__() should return dimensions and area.
3. Create a Library class that maintains a list of Book objects. Methods: add_book(book), remove_book(isbn), search_by_author(author), display_all().
