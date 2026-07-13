# Polymorphism

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 10  
**Date:** 28-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## What is Polymorphism?

Polymorphism means "many forms." In programming, it is the ability of different objects to respond to the same method call in their own way. The same interface can be used with different underlying data types.

### Types of Polymorphism in Python

1. **Method Overriding** (Runtime Polymorphism) -- Subclass redefines a parent method
2. **Duck Typing** -- "If it walks like a duck and quacks like a duck, it is a duck"
3. **Operator Overloading** -- Same operator behaves differently with different types
4. **Abstract Base Classes** -- Enforcing interface contracts

## Method Overriding (Runtime Polymorphism)

Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"Shape with area {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Polymorphic function -- works with any Shape
def print_area(shape):
    print(f"{type(shape).__name__} area: {shape.area():.2f}")
    print(f"  {shape.describe()}")

shapes = [Circle(5), Rectangle(4, 6), Shape()]

for shape in shapes:
    print_area(shape)
```

Output:
```
Circle area: 78.54
  Shape with area 78.54
Rectangle area: 24.00
  Shape with area 24.00
Shape area: 0.00
  Shape with area 0.00
```

### Why This is Polymorphism

The function `print_area` does not care about the specific type of shape. It only cares that the object has an `area()` method. Each object provides its own implementation.

## Duck Typing

Duck typing is a concept where the suitability of an object is determined by the presence of certain methods and properties, rather than by the type of the object itself.

"If it walks like a duck and quacks like a duck, then it is a duck."

```python
class Duck:
    def quack(self):
        return "Duck quacks: Quack!"

    def walk(self):
        return "Duck waddles."

class Person:
    def quack(self):
        return "Person imitates: Quack quack!"

    def walk(self):
        return "Person walks like a duck."

class Robot:
    def quack(self):
        return "Robot says: QUACK (synthesized)"

    def walk(self):
        return "Robot moves on wheels."

# Duck-typed function -- no type checking
def interact_with_duck(entity):
    print(entity.quack())
    print(entity.walk())

# All three classes work because they all have quack() and walk()
entities = [Duck(), Person(), Robot()]
for e in entities:
    interact_with_duck(e)
    print()
```

Output:
```
Duck quacks: Quack!
Duck waddles.

Person imitates: Quack quack!
Person walks like a duck.

Robot says: QUACK (synthesized)
Robot moves on wheels.
```

### Duck Typing with Built-in Types

```python
class ListLike:
    def __init__(self, items):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __contains__(self, item):
        return item in self._items

# Works with len(), for loops, 'in' operator
my_list = ListLike([10, 20, 30, 40, 50])

print(f"Length: {len(my_list)}")
print(f"Third item: {my_list[2]}")
print(f"30 in list: {30 in my_list}")

for item in my_list:
    print(f"  Item: {item}")
```

### EAFP vs LBYL

Duck typing is often used with the EAFP (Easier to Ask Forgiveness than Permission) principle:

```python
# LBYL (Look Before You Leap) -- less Pythonic
def make_sound_lbyl(animal):
    if hasattr(animal, 'quack'):
        animal.quack()
    else:
        print("This animal cannot quack.")

# EAFP (Easier to Ask Forgiveness than Permission) -- Pythonic
def make_sound_eafp(animal):
    try:
        animal.quack()
    except AttributeError:
        print("This animal cannot quack.")
```

## Operator Overloading

Operator overloading allows the same operator (like `+`, `-`, `*`, `==`) to behave differently with different types. Python achieves this through special methods (dunder methods).

### Common Operator Overloading Methods

| Category | Operators | Methods |
|---|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` | `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__` |
| Unary | `-`, `+`, `~` | `__neg__`, `__pos__`, `__invert__` |
| Augmented | `+=`, `-=`, `*=` | `__iadd__`, `__isub__`, `__imul__` |
| Container | `[]`, `in`, `len()` | `__getitem__`, `__setitem__`, `__contains__`, `__len__` |
| String | `str()`, `repr()` | `__str__`, `__repr__` |
| Callable | `()` | `__call__` |

### Example 1: Vector Class with Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition: v1 + v2
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction: v1 - v2
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    # Multiplication: v * scalar
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    # Right multiplication: scalar * v
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Negation: -v
    def __neg__(self):
        return Vector(-self.x, -self.y)

    # Equality: v1 == v2
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Length / magnitude
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # Indexing: v[0], v[1]
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector index out of range")

    # Make callable: v()
    def __call__(self):
        return f"Vector call: ({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"3 * v1 = {3 * v1}")
print(f"-v1 = {-v1}")
print(f"abs(v1) = {abs(v1):.2f}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
print(f"v1() = {v1()}")
```

Output:
```
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v1 + v2 = Vector(4, 6)
v1 - v2 = Vector(2, 2)
v1 * 3 = Vector(9, 12)
3 * v1 = Vector(9, 12)
-v1 = Vector(-3, -4)
abs(v1) = 5.00
v1 == Vector(3, 4): True
v1[0] = 3, v1[1] = 4
v1() = Vector call: (3, 4)
```

### Example 2: Time Class with Comparison

```python
from functools import total_ordering

@total_ordering
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def total_minutes(self):
        return self.hours * 60 + self.minutes

    # Addition: t1 + t2
    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        total = self.total_minutes() + other.total_minutes()
        return Time(total // 60, total % 60)

    # Subtraction: t1 - t2
    def __sub__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        total = self.total_minutes() - other.total_minutes()
        if total < 0:
            total = 0
        return Time(total // 60, total % 60)

    # Equality
    def __eq__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self.total_minutes() == other.total_minutes()

    # Less than (for total_ordering)
    def __lt__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self.total_minutes() < other.total_minutes()

    # String
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    # Represent as integer (minutes)
    def __int__(self):
        return self.total_minutes()


t1 = Time(9, 30)
t2 = Time(1, 45)
t3 = Time(9, 30)

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t1 + t2 = {t1 + t2}")
print(f"t1 - t2 = {t1 - t2}")
print(f"t2 - t1 = {t2 - t1}")  # Clamped to 0
print(f"t1 == t3: {t1 == t3}")
print(f"t1 != t2: {t1 != t2}")
print(f"t1 > t2: {t1 > t2}")
print(f"int(t1) = {int(t1)} minutes")
```

### Example 3: Custom Container

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    # Length: len(playlist)
    def __len__(self):
        return len(self._songs)

    # Indexing: playlist[0], playlist[1:3]
    def __getitem__(self, index):
        return self._songs[index]

    # Setting: playlist[0] = "New Song"
    def __setitem__(self, index, song):
        self._songs[index] = song

    # Delete: del playlist[0]
    def __delitem__(self, index):
        del self._songs[index]

    # Contains: "song" in playlist
    def __contains__(self, song):
        return song in self._songs

    # Iteration: for song in playlist
    def __iter__(self):
        return iter(self._songs)

    # String
    def __str__(self):
        return f"Playlist '{self.name}': {len(self)} songs"

    # Addition: playlist1 + playlist2
    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        merged = Playlist(f"{self.name} + {other.name}")
        merged._songs = self._songs + other._songs
        return merged


p1 = Playlist("Rock Classics")
p1.add("Bohemian Rhapsody")
p1.add("Stairway to Heaven")
p1.add("Hotel California")

p2 = Playlist("Pop Hits")
p2.add("Thriller")
p2.add("Billie Jean")

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"First song: {p1[0]}")
print(f"Last song: {p1[-1]}")

print(f"\n'Thriller' in p1? {'Thriller' in p1}")
print(f"'Thriller' in p2? {'Thriller' in p2}")

print("\nAll songs in p1:")
for song in p1:
    print(f"  - {song}")

merged = p1 + p2
print(f"\nMerged: {merged}")
for song in merged:
    print(f"  - {song}")

print(f"\nTotal merged songs: {len(merged)}")
```

## Abstract Base Classes (ABC)

Abstract base classes define a contract that subclasses must fulfill. They cannot be instantiated directly.

### Why Use ABCs?

- Enforce that subclasses implement specific methods
- Provide a clear interface contract
- Enable isinstance checks with abstract types
- Better documentation of class hierarchies

### Syntax with `abc` Module

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Must be implemented by subclasses."""
        pass

    def describe(self):
        """Concrete method -- shared by all shapes."""
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

# Cannot instantiate an ABC
# s = Shape()  # TypeError!

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Now we can create instances
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"{type(shape).__name__}: {shape.describe()}")
```

Output:
```
Circle: Area: 78.54, Perimeter: 31.42
Rectangle: Area: 24.00, Perimeter: 20.00
```

### What Happens if a Subclass Does Not Implement?

```python
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Forgot to implement area() and perimeter()!

try:
    t = Triangle(3, 4, 5)  # This actually works in Python!
    print(f"Triangle area: {t.area()}")  # This fails
except TypeError as e:
    print(f"Error: {e}")
```

Wait -- Python allows creating instances of incomplete ABC subclasses during `__init__`. The error only occurs when the missing abstract method is called. To catch this early, use `ABC` metadata.

### Abstract Properties

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @property
    @abstractmethod
    def pay(self):
        """Monthly pay -- abstract property."""
        pass

    def __str__(self):
        return f"{self.name} ({self.emp_id}): ${self.pay:.2f}"

class SalariedEmployee(Employee):
    def __init__(self, name, emp_id, annual_salary):
        super().__init__(name, emp_id)
        self.annual_salary = annual_salary

    @property
    def pay(self):
        return self.annual_salary / 12

class HourlyEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def pay(self):
        return self.hourly_rate * self.hours_worked

emps = [
    SalariedEmployee("Alice", "E001", 90000),
    HourlyEmployee("Bob", "E002", 45, 160),
]

for emp in emps:
    print(emp)
```

### Abstract Class with Concrete Methods

ABCs can have both abstract and concrete methods:

```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fetch(self):
        """Fetch data from the source."""
        pass

    @abstractmethod
    def parse(self, raw_data):
        """Parse raw data into a standard format."""
        pass

    # Concrete method with shared logic
    def load(self):
        """Template method: fetch + parse."""
        print(f"Loading data from {self.name}...")
        raw = self.fetch()
        parsed = self.parse(raw)
        print(f"Loaded {len(parsed)} records.")
        return parsed

class CSVDataSource(DataSource):
    def __init__(self, filename):
        super().__init__(filename)

    def fetch(self):
        import csv
        with open(self.name, "r") as f:
            return list(csv.reader(f))

    def parse(self, raw_data):
        return [
            {"name": row[0], "age": int(row[1]), "city": row[2]}
            for row in raw_data
        ]

class APIDataSource(DataSource):
    def __init__(self, url):
        super().__init__(url)

    def fetch(self):
        import json
        import urllib.request
        with urllib.request.urlopen(self.name) as response:
            return json.loads(response.read())

    def parse(self, raw_data):
        return raw_data.get("results", [])

print("DataSource ABC defined -- ready for implementation.")
```

## Practical Polymorphism Examples

### Example 1: Payment System

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCard(Payment):
    def __init__(self, card_number, name):
        self.card_number = card_number
        self.name = name

    def pay(self, amount):
        print(f"[CreditCard {self.card_number[-4:]}]: "
              f"Charged ${amount:.2f} to {self.name}")

    def refund(self, amount):
        print(f"[CreditCard {self.card_number[-4:]}]: "
              f"Refunded ${amount:.2f} to {self.name}")

class PayPal(Payment):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"[PayPal {self.email}]: "
              f"Processed ${amount:.2f} payment")

    def refund(self, amount):
        print(f"[PayPal {self.email}]: "
              f"Processed ${amount:.2f} refund")

class Cash(Payment):
    def pay(self, amount):
        print(f"[Cash]: Received ${amount:.2f}")

    def refund(self, amount):
        print(f"[Cash]: Given ${amount:.2f} back")

def checkout(cart_total, payment_method):
    print(f"\nChecking out: ${cart_total:.2f}")
    payment_method.pay(cart_total)

def process_refund(amount, payment_method):
    print(f"\nRefunding: ${amount:.2f}")
    payment_method.refund(amount)

# Polymorphic usage
methods = [
    CreditCard("1234-5678-9012-3456", "Alice"),
    PayPal("alice@example.com"),
    Cash(),
]

for method in methods:
    checkout(150.00, method)
    process_refund(25.00, method)
```

### Example 2: Notification System

```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailNotification(Notification):
    def send(self, message, recipient):
        print(f"[Email] To: {recipient}")
        print(f"  Subject: New Notification")
        print(f"  Body: {message}")
        print()

class SMSNotification(Notification):
    def send(self, message, recipient):
        print(f"[SMS] To: {recipient}")
        print(f"  Message: {message[:50]}...")
        print()

class PushNotification(Notification):
    def send(self, message, recipient):
        print(f"[Push] Device: {recipient}")
        print(f"  Alert: {message}")
        print()

def notify_all(message, recipients, notification_type):
    for recipient in recipients:
        notification_type.send(message, recipient)

users = ["alice@example.com", "+1234567890", "device_token_abc"]
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notify_all("System maintenance tonight at 2 AM.", [users[0]], email)
notify_all("Your OTP is 1234", [users[1]], sms)
notify_all("New message from Bob", [users[2]], push)
```

## Summary

| Polymorphism Type | Mechanism | Example |
|---|---|---|
| Method Overriding | Subclass redefines parent method | `class Dog(Animal): def speak()` |
| Duck Typing | Object must have required methods | `if hasattr(obj, 'quack')` |
| Operator Overloading | Define `__add__`, `__eq__`, etc. | `v1 + v2` with Vector class |
| Abstract Base Classes | `ABC`, `@abstractmethod` | `class Shape(ABC): @abstractmethod def area()` |

## Practice Problems

1. **Shape Hierarchy with ABC** -- Create an abstract `Shape` class with abstract methods `area()` and `perimeter()`. Implement `Circle`, `Rectangle`, `Triangle` subclasses. Create a function `print_shape_info(shape)` that uses polymorphism to print details.

2. **Duck Typing: Media Player** -- Create classes `MP3Player`, `VideoPlayer`, `StreamingPlayer`. Each must have `play()`, `pause()`, `stop()`, `get_info()` methods. Write a duck-typed function `operate_player(player)` that calls all four methods.

3. **Operator Overloading: Fraction** -- Create a `Fraction` class with numerator and denominator. Overload `+`, `-`, `*`, `/`, `==`, `<`, `__str__`. Implement `__float__` to convert to float. Ensure fractions are reduced.

4. **Notification System with ABC** -- Create abstract `Notifier` class with `send(message)`. Implement `EmailNotifier`, `SMSNotifier`, `SlackNotifier`. Create a `NotificationManager` that holds multiple notifiers and broadcasts messages to all.

5. **Polymorphic Database Connection** -- Create abstract `Database` class with `connect()`, `query(sql)`, `close()`. Implement `MySQLDatabase`, `PostgreSQLDatabase`, `SQLiteDatabase`. Write a function `run_migration(db)` that works with any database type.

---

## Practice Problems

1. **Shape Hierarchy with ABC**

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self): return self.a + self.b + self.c

def print_shape_info(shape):
    print(f"{type(shape).__name__}: area={shape.area():.2f}, "
          f"perimeter={shape.perimeter():.2f}")

for s in [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]:
    print_shape_info(s)
```

2. **Duck Typing: Media Player**

```python
class MP3Player:
    def __init__(self, file): self.file = file
    def play(self): print(f"MP3 playing '{self.file}'")
    def pause(self): print("MP3 paused")
    def stop(self): print("MP3 stopped")
    def get_info(self): return f"MP3: {self.file}"

class VideoPlayer:
    def __init__(self, file): self.file = file
    def play(self): print(f"Video playing '{self.file}'")
    def pause(self): print("Video paused")
    def stop(self): print("Video stopped")
    def get_info(self): return f"Video: {self.file}"

class StreamingPlayer:
    def __init__(self, url): self.url = url
    def play(self): print(f"Streaming from '{self.url}'")
    def pause(self): print("Stream paused")
    def stop(self): print("Stream stopped")
    def get_info(self): return f"Stream: {self.url}"

def operate_player(player):
    print(f"Info: {player.get_info()}")
    player.play()
    player.pause()
    player.stop()
    print()

for p in [MP3Player("song.mp3"), VideoPlayer("movie.mp4"),
          StreamingPlayer("https://stream.example.com/live")]:
    operate_player(p)
```

3. **Operator Overloading: Fraction**

```python
from math import gcd

class Fraction:
    def __init__(self, num, den=1):
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        if den < 0:
            num, den = -num, -den
        g = gcd(abs(num), abs(den))
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.num * other.den + other.num * self.den,
            self.den * other.den
        )

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.num * other.den - other.num * self.den,
            self.den * other.den
        )

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.num * other.den < other.num * self.den

    def __float__(self):
        return self.num / self.den

    def __str__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
print(f"{f1} * {f2} = {f1 * f2}")
print(f"{f1} / {f2} = {f1 / f2}")
print(f"{f1} == {Fraction(2, 4)}: {f1 == Fraction(2, 4)}")
print(f"{f1} < {f2}: {f1 < f2}")
print(f"float({f1}) = {float(f1)}")
```

4. **Notification System with ABC**

```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotifier(Notifier):
    def __init__(self, email): self.email = email
    def send(self, message):
        print(f"[Email] To {self.email}: {message}")

class SMSNotifier(Notifier):
    def __init__(self, phone): self.phone = phone
    def send(self, message):
        print(f"[SMS] To {self.phone}: {message[:40]}...")

class SlackNotifier(Notifier):
    def __init__(self, channel): self.channel = channel
    def send(self, message):
        print(f"[Slack] #{self.channel}: {message}")

class NotificationManager:
    def __init__(self):
        self.notifiers = []

    def add(self, notifier):
        self.notifiers.append(notifier)

    def broadcast(self, message):
        print(f"\nBroadcasting: '{message}'")
        for n in self.notifiers:
            n.send(message)

manager = NotificationManager()
manager.add(EmailNotifier("alice@example.com"))
manager.add(SMSNotifier("+1234567890"))
manager.add(SlackNotifier("general"))
manager.broadcast("System will be down for maintenance at 2 AM.")
```

5. **Polymorphic Database Connection**

```python
from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self, name): self.name = name

    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def query(self, sql): pass

    @abstractmethod
    def close(self): pass

class MySQLDatabase(Database):
    def connect(self): print(f"MySQL: Connecting to {self.name}... (port 3306)")
    def query(self, sql): print(f"MySQL: Executing '{sql}' -> 3 rows returned")
    def close(self): print(f"MySQL: Closing connection.")

class PostgreSQLDatabase(Database):
    def connect(self): print(f"PostgreSQL: Connecting to {self.name}... (port 5432)")
    def query(self, sql): print(f"PostgreSQL: Executing '{sql}' -> 5 rows returned")
    def close(self): print(f"PostgreSQL: Closing connection.")

class SQLiteDatabase(Database):
    def connect(self): print(f"SQLite: Opening {self.name}.db")
    def query(self, sql): print(f"SQLite: Executing '{sql}' -> 2 rows returned")
    def close(self): print(f"SQLite: Closing database file.")

def run_migration(db):
    print(f"\nRunning migration on {db.name}...")
    db.connect()
    db.query("CREATE TABLE users (id INT, name TEXT)")
    db.query("INSERT INTO users VALUES (1, 'Alice')")
    db.close()
    print("Migration complete.")

for db in [MySQLDatabase("app_db"), PostgreSQLDatabase("app_db"),
           SQLiteDatabase("app_db")]:
    run_migration(db)
```
