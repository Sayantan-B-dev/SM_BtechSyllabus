# Multiple Objects and Attributes

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 7  
**Date:** 26-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## Creating Multiple Objects from the Same Class

A class is a blueprint. You can create as many objects (instances) as needed, each with its own separate data.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name}, age {self.age}.")

# Create multiple objects
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
s3 = Student("Charlie", 21)

s1.introduce()
s2.introduce()
s3.introduce()

print(f"s1 memory address: {id(s1)}")
print(f"s2 memory address: {id(s2)}")
print(f"Are s1 and s2 the same? {s1 is s2}")
```

Output:
```
Hi, I am Alice, age 20.
Hi, I am Bob, age 22.
Hi, I am Charlie, age 21.
s1 memory address: 2653847592832
s2 memory address: 2653847592896
Are s1 and s2 the same? False
```

### Objects Are Independent

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

# Each counter operates independently
c1 = Counter(10)
c2 = Counter(100)

c1.increment()
c1.increment()
c2.increment()

print(f"c1: {c1.count}")  # 12
print(f"c2: {c2.count}")  # 101

c1.decrement()
print(f"c1 after decrement: {c1.count}")  # 11
print(f"c2 unchanged: {c2.count}")  # 101
```

## Modifying Attributes

Object attributes can be modified directly or through methods.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0
        self.color = "White"

    def __str__(self):
        return f"{self.color} {self.make} {self.model} ({self.speed} km/h)"

car = Car("Toyota", "Camry")
print(car)

car.color = "Blue"
print(car)

car.speed = 50
print(car)

car.year = 2022
print(f"Year: {car.year}")
```

Output:
```
White Toyota Camry (0 km/h)
Blue Toyota Camry (0 km/h)
Blue Toyota Camry (50 km/h)
Year: 2022
```

### Adding Attributes Dynamically

Python allows adding attributes to individual objects that are not defined in the class:

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")

p1.age = 25

print(p1.name, p1.age)
print(p2.name)
```

Output:
```
Alice 25
Bob
```

## The `__dict__` Attribute

Every object has a `__dict__` dictionary that stores its writable attributes.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self, percent):
        return self.salary * percent / 100

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print("e1.__dict__:", e1.__dict__)
print("e2.__dict__:", e2.__dict__)

e1.__dict__["salary"] = 55000
print("After dict modification:")
print("e1.__dict__:", e1.__dict__)
print(f"e1.salary: {e1.salary}")
```

Output:
```
e1.__dict__: {'name': 'Alice', 'salary': 50000}
e2.__dict__: {'name': 'Bob', 'salary': 60000}
After dict modification:
e1.__dict__: {'name': 'Alice', 'salary': 55000}
e1.salary: 55000
```

### Class `__dict__` vs Instance `__dict__`

```python
class Sample:
    class_var = "shared"

    def __init__(self, value):
        self.instance_var = value

    def method(self):
        pass

print("Class __dict__:")
for key, value in Sample.__dict__.items():
    if not key.startswith("__"):
        print(f"  {key}: {value}")

obj = Sample(42)
print("\nInstance __dict__:")
print(f"  {obj.__dict__}")
```

Output:
```
Class __dict__:
  class_var: shared
  method: <function Sample.method at 0x...>

Instance __dict__:
  {'instance_var': 42}
```

## Attribute Access Functions

Python provides four built-in functions for dynamic attribute access.

### hasattr() -- Check if Attribute Exists

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)

print(hasattr(p, "name"))
print(hasattr(p, "age"))
print(hasattr(p, "salary"))

if hasattr(p, "salary"):
    print(p.salary)
else:
    print("No salary attribute.")
```

### getattr() -- Get Attribute Value

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)

print(getattr(p, "name"))
print(getattr(p, "age"))
print(getattr(p, "salary", "N/A"))
print(getattr(p, "name", "Unknown"))

try:
    print(getattr(p, "salary"))
except AttributeError as e:
    print(f"Error: {e}")
```

### setattr() -- Set Attribute Value

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(f"Before: {p.name}")

setattr(p, "name", "Bob")
print(f"After setattr: {p.name}")

setattr(p, "age", 30)
print(f"New attribute: {p.age}")

attr_name = "city"
attr_value = "New York"
setattr(p, attr_name, attr_value)
print(f"Dynamic attr: {p.city}")
```

### delattr() -- Delete Attribute

```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

p = Person("Alice", 25, "NYC")
print(f"Before: {p.__dict__}")

delattr(p, "city")
print(f"After delattr city: {p.__dict__}")

del p.age
print(f"After del age: {p.__dict__}")

try:
    print(p.city)
except AttributeError as e:
    print(f"Error: {e}")
```

### Practical Example: Config Object Using Attribute Functions

```python
class Config:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def has(self, key):
        return hasattr(self, key)

    def remove(self, key):
        if hasattr(self, key):
            delattr(self, key)
            return True
        return False

    def __str__(self):
        items = [f"{k}={v}" for k, v in self.__dict__.items()]
        return ", ".join(items)

config = Config(host="localhost", port=8080, debug=True, max_users=100)
print(f"Host: {config.get('host')}")
print(f"Has 'debug': {config.has('debug')}")
print(f"Has 'password': {config.has('password')}")
print(f"Config: {config}")

config.remove("max_users")
print(f"After remove: {config}")
```

## Comparing Objects

### Default Behavior (Identity Comparison)

By default, `==` compares object identity (memory address), not content.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = p1

print(f"p1 is p3: {p1 is p3}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 is p2: {p1 is p2}")
print(f"p1 == p2: {p1 == p2}")
```

### Implementing `__eq__` (Equality)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(5, 6)

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 == 'hello': {p1 == 'hello'}")

point_set = {p1, p2, p3}
print(f"Set size: {len(point_set)}")
```

### Implementing `__lt__` and `__gt__` (Ordering)

```python
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade == other.grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade > other.grade

    def __str__(self):
        return f"{self.name} (grade={self.grade}, age={self.age})"

students = [
    Student("Alice", 85, 20),
    Student("Bob", 92, 22),
    Student("Charlie", 78, 21),
    Student("Diana", 95, 19),
]

print(f"Alice < Bob: {students[0] < students[1]}")
print(f"Alice > Charlie: {students[0] > students[2]}")
print(f"Alice == Diana: {students[0] == students[3]}")

sorted_students = sorted(students)
print("\nSorted by grade:")
for s in sorted_students:
    print(f"  {s}")
```

### Using `functools.total_ordering`

```python
from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __str__(self):
        return f"Rectangle({self.width}x{self.height}, area={self.area()})"

r1 = Rectangle(10, 5)
r2 = Rectangle(7, 8)
r3 = Rectangle(5, 10)

print(f"r1 == r3: {r1 == r3}")
print(f"r1 != r2: {r1 != r2}")
print(f"r1 < r2: {r1 < r2}")
print(f"r1 <= r2: {r1 <= r2}")
print(f"r1 >= r3: {r1 >= r3}")
```

## Complete Example: Library Book Management

```python
from functools import total_ordering

@total_ordering
class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        self.is_borrowed = False

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year < other.year

    def __hash__(self):
        return hash(self.isbn)

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} ({self.year}) - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if book in self.books:
            print(f"Book '{book.title}' already in library.")
            return False
        self.books.append(book)
        print(f"Added: {book.title}")
        return True

    def find_by_author(self, author):
        return [b for b in self.books if b.author.lower() == author.lower()]

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrow():
                    print(f"Borrowed: {book.title}")
                    return True
                else:
                    print(f"'{book.title}' is already borrowed.")
                    return False
        print(f"Book with ISBN {isbn} not found.")
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                print(f"Returned: {book.title}")
                return True
        return False

    def list_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print(f"\n--- {self.name} ---")
        print(f"{'Title':30s} {'Year':6s} {'Status':12s}")
        print("-" * 48)
        for book in sorted(self.books):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title:30s} {book.year:6d} {status:12s}")

    def __len__(self):
        return len(self.books)

    def __contains__(self, book):
        return book in self.books


lib = Library("City Library")
b1 = Book("1984", "George Orwell", "9780451524935", 1949)
b2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960)
b3 = Book("Brave New World", "Aldous Huxley", "9780060850524", 1932)
b4 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
b5 = Book("1984", "George Orwell", "9780451524935", 1949)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)
lib.add_book(b5)

lib.list_books()

print("\nBorrowing and returning:")
lib.borrow_book("9780451524935")
lib.borrow_book("9780451524935")
lib.return_book("9780451524935")
lib.list_books()

print(f"\nLibrary has {len(lib)} books.")
print(f"Has '1984'? {b1 in lib}")
```

## Practice Problems

1. **Employee Directory** -- Create an `Employee` class with name, emp_id, department, salary. Create multiple employees. Implement `__eq__` (same emp_id), `__lt__` (by salary). Use `hasattr`, `getattr`, `setattr`, `delattr` for dynamic attribute management.
   <details>
   <summary>Show Answer</summary>

   ```python
   class Employee:
       def __init__(self, name, emp_id, department, salary):
           self.name = name
           self.emp_id = emp_id
           self.department = department
           self.salary = salary

       def __eq__(self, other):
           if not isinstance(other, Employee):
               return NotImplemented
           return self.emp_id == other.emp_id

       def __lt__(self, other):
           if not isinstance(other, Employee):
               return NotImplemented
           return self.salary < other.salary

       def __str__(self):
           return f"{self.name} ({self.emp_id}) - {self.department}: ${self.salary}"

   e1 = Employee("Alice", "E001", "Eng", 75000)
   e2 = Employee("Bob", "E002", "Mkt", 65000)
   e3 = Employee("Charlie", "E001", "Eng", 80000)

   print(f"e1 == e3: {e1 == e3}")
   print(f"e1 < e2: {e1 < e2}")

   setattr(e1, "bonus", 5000)
   print(f"Has bonus? {hasattr(e1, 'bonus')}: {getattr(e1, 'bonus')}")
   delattr(e1, "bonus")
   print(f"Has bonus? {hasattr(e1, 'bonus')}")
   ```
   </details>

2. **Shopping Cart System** -- Create a `CartItem` class (product, price, quantity) and a `ShoppingCart` class that holds multiple items. Implement `add_item`, `remove_item`, `total`. Implement `__eq__` for CartItem (same product name). Allow sorting items by price.
   <details>
   <summary>Show Answer</summary>

   ```python
   class CartItem:
       def __init__(self, product, price, quantity=1):
           self.product = product
           self.price = price
           self.quantity = quantity

       def total(self):
           return self.price * self.quantity

       def __eq__(self, other):
           if not isinstance(other, CartItem):
               return NotImplemented
           return self.product == other.product

       def __lt__(self, other):
           if not isinstance(other, CartItem):
               return NotImplemented
           return self.price < other.price

       def __str__(self):
           return f"{self.product} x{self.quantity} @ ${self.price}"

   class ShoppingCart:
       def __init__(self):
           self.items = []

       def add_item(self, product, price, quantity=1):
           item = CartItem(product, price, quantity)
           if item in self.items:
               idx = self.items.index(item)
               self.items[idx].quantity += quantity
           else:
               self.items.append(item)

       def remove_item(self, product):
           self.items = [i for i in self.items if i.product != product]

       def total(self):
           return sum(item.total() for item in self.items)

       def sort_by_price(self):
           self.items.sort()

       def __str__(self):
           result = "\n".join(str(item) for item in self.items)
           return f"{result}\nTotal: ${self.total():.2f}"

   cart = ShoppingCart()
   cart.add_item("Laptop", 1000, 1)
   cart.add_item("Mouse", 25, 2)
   cart.add_item("Laptop", 1000, 1)
   print(cart)
   ```
   </details>

3. **Student Grade Tracker** -- Create a `Student` class with name and marks (list). Implement `__eq__` (same average marks), `__lt__` (by average). Create a `Classroom` class that holds multiple students and can find top performer, sort by grade, etc.
   <details>
   <summary>Show Answer</summary>

   ```python
   class Student:
       def __init__(self, name, marks):
           self.name = name
           self.marks = marks

       @property
       def average(self):
           return sum(self.marks) / len(self.marks) if self.marks else 0

       def __eq__(self, other):
           if not isinstance(other, Student):
               return NotImplemented
           return self.average == other.average

       def __lt__(self, other):
           if not isinstance(other, Student):
               return NotImplemented
           return self.average < other.average

       def __str__(self):
           return f"{self.name}: avg={self.average:.1f}"

   class Classroom:
       def __init__(self):
           self.students = []

       def add(self, student):
           self.students.append(student)

       def top_performer(self):
           return max(self.students) if self.students else None

       def sorted_by_grade(self):
           return sorted(self.students, reverse=True)

       def __len__(self):
           return len(self.students)

   room = Classroom()
   room.add(Student("Alice", [85, 90, 78]))
   room.add(Student("Bob", [92, 88, 95]))
   room.add(Student("Charlie", [70, 75, 72]))
   print(f"Top: {room.top_performer()}")
   print("Sorted:")
   for s in room.sorted_by_grade():
       print(f"  {s}")
   ```
   </details>

4. **Dynamic Form Builder** -- Create a `Form` class that uses `hasattr`, `getattr`, `setattr`, `delattr` to manage form fields dynamically. Allow adding fields like `add_field(name, value)`, `get_field(name)`, `remove_field(name)`, `has_field(name)`.
   <details>
   <summary>Show Answer</summary>

   ```python
   class DynamicForm:
       def __init__(self, name):
           self._form_name = name

       def add_field(self, name, value):
           setattr(self, name, value)
           print(f"Added field '{name}' = {value!r}")

       def get_field(self, name, default=None):
           return getattr(self, name, default)

       def has_field(self, name):
           return hasattr(self, name)

       def remove_field(self, name):
           if self.has_field(name):
               delattr(self, name)
               print(f"Removed field '{name}'")
               return True
           return False

       def list_fields(self):
           fields = {k: v for k, v in self.__dict__.items()
                     if not k.startswith("_")}
           print(f"Form '{self._form_name}': {fields}")

   form = DynamicForm("Registration")
   form.add_field("username", "alice")
   form.add_field("email", "alice@example.com")
   form.add_field("age", 25)
   form.list_fields()
   print(f"Has 'email': {form.has_field('email')}")
   form.remove_field("age")
   form.list_fields()
   ```
   </details>

5. **Object Counter with `__dict__`** -- Create a class `TrackedObject` that logs every attribute change in `__dict__`. Use `setattr` in `__init__` to store a history log. Track all attribute modifications.
   <details>
   <summary>Show Answer</summary>

   ```python
   class TrackedObject:
       def __init__(self, **kwargs):
           self._changes = []
           for key, value in kwargs.items():
               setattr(self, key, value)
               self._changes.append(f"INIT: {key} = {value!r}")

       def __setattr__(self, name, value):
           if name != "_changes":
               self._changes.append(f"SET: {name} = {value!r}")
           super().__setattr__(name, value)

       def __delattr__(self, name):
           if name != "_changes":
               self._changes.append(f"DEL: {name}")
           super().__delattr__(name)

       def history(self):
           return self._changes.copy()

   obj = TrackedObject(name="Alice", age=25)
   obj.city = "NYC"
   obj.age = 26
   del obj.city

   for entry in obj.history():
       print(entry)
   print(f"Final __dict__: {obj.__dict__}")
   ```
   </details>
