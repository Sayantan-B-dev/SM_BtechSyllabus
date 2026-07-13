# Classes and Objects

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 4  
**Date:** 12-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## Introduction to Object-Oriented Programming (OOP)

OOP is a programming paradigm that organizes code around "objects" rather than functions and logic. An object contains both data (attributes) and behavior (methods).

### Key OOP Concepts
- **Class** -- Blueprint or template for creating objects
- **Object** -- An instance of a class (a concrete entity)
- **Attribute** -- Data stored in an object
- **Method** -- Function defined inside a class that operates on the object

### Procedural vs Object-Oriented

| Procedural | Object-Oriented |
|---|---|
| Focuses on functions | Focuses on objects |
| Data is separate from functions | Data and methods are bundled |
| Less reusable | More reusable (inheritance) |
| Harder to model real world | Natural real-world mapping |

## Defining a Class

Use the `class` keyword followed by the class name (PascalCase convention).

```python
class ClassName:
    """Optional docstring describing the class."""
    # Class body: attributes and methods
    pass
```

### Simple Class Example

```python
class Student:
    """A simple Student class."""
    pass

# Create objects (instances)
s1 = Student()
s2 = Student()

print(type(s1))
print(s1)
print(s2)
```

Output:
```
<class '__main__.Student'>
<__main__.Student object at 0x0000021A3B4D0FD0>
<__main__.Student object at 0x0000021A3B4D0FA0>
```

Each object has a unique memory address (`0x...`).

## The `__init__` Method (Constructor)

`__init__` is a special method that runs automatically when an object is created. It initializes the object's attributes.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
        self.grade = grade    # Instance attribute

# Creating objects with __init__
s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 19, "B")

print(f"{s1.name}: age {s1.age}, grade {s1.grade}")
print(f"{s2.name}: age {s2.age}, grade {s2.grade}")
```

Output:
```
Alice: age 20, grade A
Bob: age 19, grade B
```

## The `self` Parameter

`self` refers to the current instance of the class. It must be the first parameter of every instance method.

- `self` is automatically passed by Python -- you do not provide it when calling methods
- The name `self` is a convention, not a keyword (but always use `self`)

```python
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        # self refers to the specific object calling this method
        print(f"{self.model} ({self.year})")

    def age(self, current_year):
        return current_year - self.year

c1 = Car("Toyota Camry", 2022)
c2 = Car("Honda Civic", 2020)

c1.display_info()       # self = c1
c2.display_info()       # self = c2
print(f"C1 age: {c1.age(2026)} years")
print(f"C2 age: {c2.age(2026)} years")
```

Output:
```
Toyota Camry (2022)
Honda Civic (2020)
C1 age: 4 years
C2 age: 6 years
```

## Instance Attributes vs Class Attributes

### Instance Attributes
- Defined inside `__init__` with `self.attribute = value`
- Each object has its own copy
- Can vary between objects

### Class Attributes
- Defined directly in the class body (outside any method)
- Shared by all instances of the class
- Accessed via `ClassName.attribute` or `self.attribute`

```python
class Student:
    # Class attribute (shared by all students)
    school_name = "Springfield High School"
    total_students = 0

    def __init__(self, name, grade):
        # Instance attributes (unique to each student)
        self.name = name
        self.grade = grade
        Student.total_students += 1

    def display(self):
        print(f"{self.name} ({self.grade}) - {self.school_name}")

# Create students
s1 = Student("Alice", "A")
s2 = Student("Bob", "B")
s3 = Student("Charlie", "A")

s1.display()
s2.display()
s3.display()
print(f"\nTotal students: {Student.total_students}")
print(f"School: {Student.school_name}")

# Class attribute is shared -- change affects all
Student.school_name = "New School"
s1.display()  # Reflects the change
s3.display()
```

Output:
```
Alice (A) - Springfield High School
Bob (B) - Springfield High School
Charlie (A) - Springfield High School

Total students: 3
School: Springfield High School
Alice (A) - New School
Charlie (A) - New School
```

### Instance Attribute Overrides Class Attribute

If you assign to `self.attribute`, you create an instance attribute that shadows the class attribute:

```python
class Employee:
    company = "TechCorp"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # TechCorp (from class)
print(e2.company)  # TechCorp (from class)

e1.company = "Startup"  # Creates instance attribute
print(e1.company)       # Startup (instance shadows class)
print(e2.company)       # TechCorp (still class)
print(Employee.company) # TechCorp (class unchanged)
```

Output:
```
TechCorp
TechCorp
Startup
TechCorp
TechCorp
```

## Creating Objects (Instances)

Creating an object is called "instantiation." Syntax: `variable_name = ClassName(arguments)`

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        print(f"Read {pages} pages. Now at page {self.current_page}.")

    def bookmark(self):
        return self.current_page

# Creating objects
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

book1.read(50)
book1.read(100)
print(f"Bookmark at page: {book1.bookmark()}")
book2.read(30)
```

Output:
```
Read 50 pages. Now at page 50.
Read 100 pages. Now at page 150.
Bookmark at page: 150
Read 30 pages. Now at page 30.
```

## The `__str__` Method

`__str__` defines the string representation of an object (what `print()` shows). Without it, `print` shows `<__main__.ClassName object at 0x...>`.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student({self.name}, age={self.age}, grade={self.grade})"

s = Student("Alice", 20, "A")
print(s)           # Calls __str__
print(str(s))      # Same
print(repr(s))     # Falls back to default (or __repr__)
```

Output:
```
Student(Alice, age=20, grade=A)
Student(Alice, age=20, grade=A)
<__main__.Student object at 0x0000021A3B4D0FD0>
```

### `__str__` vs `__repr__`

| Method | Purpose | Used by |
|---|---|---|
| `__str__` | Readable, user-friendly output | `print()`, `str()` |
| `__repr__` | Unambiguous, developer-friendly | `repr()`, debugging |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(str(p))    # (3, 4)
print(repr(p))   # Point(3, 4)
print(p)         # prints __str__
```

## Complete Example: Car Class

```python
class Car:
    """A simple Car class."""

    # Class attributes
    wheels = 4
    vehicle_type = "Automobile"

    def __init__(self, make, model, year, color="White"):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
        self.speed = 0
        self.odometer = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} started.")
        else:
            print("Car is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.make} {self.model} stopped.")
        else:
            print("Car is already off.")

    def accelerate(self, amount):
        if not self.is_running:
            print("Start the car first!")
            return
        self.speed += amount
        if self.speed > 180:
            self.speed = 180
        print(f"Speed: {self.speed} km/h")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Speed: {self.speed} km/h")

    def drive(self, distance_km):
        if not self.is_running:
            print("Start the car first!")
            return
        self.odometer += distance_km
        print(f"Drove {distance_km} km. Total: {self.odometer} km")

    def __str__(self):
        status = "running" if self.is_running else "off"
        return (f"{self.year} {self.color} {self.make} {self.model} "
                f"[{status}, {self.speed} km/h, {self.odometer} km]")

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.year}, '{self.color}')"


# Create and use Car objects
my_car = Car("Toyota", "Camry", 2022, "Blue")
print(my_car)
print()

my_car.start()
my_car.accelerate(50)
my_car.drive(100)
my_car.accelerate(30)
my_car.brake(20)
print(my_car)
print()

my_car.stop()
print()
print(repr(my_car))
print(f"All cars have {Car.wheels} wheels.")
```

Output:
```
2022 Blue Toyota Camry [off, 0 km/h, 0 km]

Toyota Camry started.
Speed: 50 km/h
Drove 100 km. Total: 100 km
Speed: 80 km/h
Speed: 60 km/h
2022 Blue Toyota Camry [running, 60 km/h, 100 km]

Toyota Camry stopped.

Car('Toyota', 'Camry', 2022, 'Blue')
All cars have 4 wheels.
```

## Summary Table: Special Methods

| Method | Purpose | Called When |
|---|---|---|
| `__init__(self, ...)` | Constructor / initializer | `ClassName()` |
| `__str__(self)` | String representation | `print(obj)`, `str(obj)` |
| `__repr__(self)` | Developer representation | `repr(obj)`, debugging |
| `__del__(self)` | Destructor (cleanup) | `del obj` |

## Practice Problems

1. **Rectangle Class** -- Create a `Rectangle` class with attributes `length` and `width`. Include methods: `area()` returns length * width; `perimeter()` returns 2*(l+w); `is_square()` returns True if l==w. Add `__str__` to display "Rectangle(l, w)".

2. **BankAccount Class** -- Create a `BankAccount` class with attributes `account_holder`, `account_number`, `balance`. Include methods: `deposit(amount)`, `withdraw(amount)`, and `__str__` showing masked account number and balance.

3. **Employee Class with Class Counter** -- Create an `Employee` class with instance attributes `name` and `salary`. Use a class attribute `employee_count` to track total employees. Create a class method `display_count()`.

4. **LibraryBook Class** -- Create a `LibraryBook` class with title, author, isbn, is_borrowed (default False). Methods: `borrow()` (marks as borrowed), `return_book()` (marks as returned). Prevent borrowing an already-borrowed book.

5. **Student Class with Methods** -- Create a `Student` class with name, marks (list of 3 subjects). Methods: `total()` returns sum; `average()` returns mean; `grade()` returns 'A' if avg>=85, 'B' if avg>=70, 'C' if avg>=50, else 'F'. Use `__str__`.

---

## Practice Problems

1. **Rectangle Class**

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

    def __str__(self):
        return f"Rectangle({self.length}, {self.width})"

r = Rectangle(5, 5)
print(r)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")
print(f"Is square? {r.is_square()}")
```

2. **BankAccount Class**

```python
import random

class BankAccount:
    def __init__(self, holder, initial_balance=0):
        self.account_holder = holder
        self.account_number = str(random.randint(10000000, 99999999))
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Balance: ${self.balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        masked = "XXXX" + self.account_number[-4:]
        return f"Account[{masked}] Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

acc = BankAccount("Alice", 1000)
print(acc)
acc.deposit(500)
acc.withdraw(200)
```

3. **Employee Class with Class Counter**

```python
class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def display_count(cls):
        print(f"Total employees: {cls.employee_count}")

    def __str__(self):
        return f"{self.name}: ${self.salary}"

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e3 = Employee("Charlie", 55000)
Employee.display_count()
print(e1)
print(e3)
```

4. **LibraryBook Class**

```python
class LibraryBook:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
            return False
        self.is_borrowed = True
        print(f"'{self.title}' borrowed successfully.")
        return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
            return False
        self.is_borrowed = False
        print(f"'{self.title}' returned.")
        return True

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} [{status}]"

book = LibraryBook("1984", "George Orwell", "9780451524935")
print(book)
book.borrow()
book.borrow()
book.return_book()
print(book)
```

5. **Student Class with Methods**

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of 3 marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    def __str__(self):
        return (f"Student: {self.name}\n"
                f"Marks: {self.marks}\n"
                f"Total: {self.total()}, Avg: {self.average():.1f}, "
                f"Grade: {self.grade()}")

s = Student("Alice", [85, 90, 78])
print(s)
```
