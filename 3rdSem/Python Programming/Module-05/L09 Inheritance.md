# Inheritance

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 9  
**Date:** 28-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## What is Inheritance?

Inheritance is a mechanism where a new class (child/derived class) is created from an existing class (parent/base class). The child class inherits attributes and methods from the parent class and can also add new ones or override existing ones.

### Why Use Inheritance?

- **Code Reuse** -- Common logic is written once in the base class
- **Extensibility** -- Add new functionality without modifying existing code
- **Hierarchical Classification** -- Models real-world "is-a" relationships
- **Polymorphism** -- Enables treating objects of different classes uniformly

### Terminology

| Term | Meaning | Example |
|---|---|---|
| Base class / Parent / Super | Class being inherited from | `Animal` |
| Derived class / Child / Sub | Class that inherits | `Dog` |
| "is-a" relationship | Dog IS-A Animal | -- |

## Single Inheritance

A child class inherits from one parent class.

### Basic Syntax

```python
class Parent:
    # Parent class body
    pass

class Child(Parent):  # Child inherits from Parent
    # Child class body
    pass
```

### Example: Animal-Dog-Cat Hierarchy

```python
class Animal:
    """Base class for all animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100

    def eat(self, food):
        self._energy += 10
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        self._energy = 100
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        """Generic sound -- overridden by subclasses."""
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"{self.name} ({type(self).__name__}, age {self.age})"


class Dog(Animal):
    """Dog inherits from Animal."""

    def make_sound(self):
        """Override the parent's make_sound."""
        print(f"{self.name} barks: Woof! Woof!")

    def fetch(self, item):
        """New method specific to Dog."""
        if self._energy < 20:
            print(f"{self.name} is too tired to fetch.")
            return
        self._energy -= 20
        print(f"{self.name} fetches the {item}.")


class Cat(Animal):
    """Cat inherits from Animal."""

    def make_sound(self):
        """Override the parent's make_sound."""
        print(f"{self.name} meows: Meow!")

    def purr(self):
        """New method specific to Cat."""
        print(f"{self.name} is purring.")


# Create instances
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

# Inherited methods
dog.eat("bone")
cat.eat("fish")
print()

# Overridden methods
dog.make_sound()
cat.make_sound()
print()

# Child-specific methods
dog.fetch("ball")
cat.purr()
print()

# Inherited __str__
print(dog)
print(cat)
```

Output:
```
Buddy is eating bone.
Whiskers is eating fish.

Buddy barks: Woof! Woof!
Whiskers meows: Meow!

Buddy fetches the ball.
Whiskers is purring.

Buddy (Dog, age 3)
Whiskers (Cat, age 2)
```

### Inheritance Tree

```
    Animal
    /    \
  Dog    Cat
```

## Method Overriding

A child class can redefine a method inherited from the parent. This is called overriding.

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model}: Engine started.")

    def stop(self):
        print(f"{self.make} {self.model}: Engine stopped.")

    def fuel_type(self):
        return "Unknown"

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Vehicle):
    def start(self):
        print(f"{self.make} {self.model}: Electric motor activated silently.")

    def fuel_type(self):
        return "Electricity"

vehicles = [
    Car("Toyota", "Camry"),
    ElectricCar("Tesla", "Model 3"),
]

for v in vehicles:
    v.start()
    print(f"  Fuel: {v.fuel_type()}")
    v.stop()
    print()
```

Output:
```
Toyota Camry: Engine started.
  Fuel: Petrol
Toyota Camry: Engine stopped.

Tesla Model 3: Electric motor activated silently.
  Fuel: Electricity
Tesla Model 3: Engine stopped.
```

## The `super()` Function

`super()` returns a temporary proxy object that allows calling methods from the parent class. It is essential when overriding `__init__`.

### Without super()

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent.__init__: name={name}")

class Child(Parent):
    def __init__(self, name, age):
        # Manually calling parent's __init__
        Parent.__init__(self, name)
        self.age = age
        print(f"Child.__init__: age={age}")
```

### With super() (Recommended)

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent.__init__: name={name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent.__init__
        self.age = age
        print(f"Child.__init__: age={age}")

c = Child("Alice", 25)
print(f"Child: name={c.name}, age={c.age}")
```

Output:
```
Parent.__init__: name=Alice
Child.__init__: age=25
Child: name=Alice, age=25
```

### Advantages of super()

1. No need to name the parent class explicitly
2. Handles multiple inheritance correctly (MRO)
3. Makes code more maintainable

### Example: Multi-level Inheritance with super()

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal.__init__: {name}")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
        print(f"Mammal.__init__: {name}, fur={fur_color}")

class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed
        print(f"Dog.__init__: {name}, breed={breed}")

dog = Dog("Buddy", "Golden", "Labrador")
print(f"\nDog: {dog.name}, {dog.fur_color} fur, {dog.breed}")
```

Output:
```
Animal.__init__: Buddy
Mammal.__init__: Buddy, fur=Golden
Dog.__init__: Buddy, breed=Labrador

Dog: Buddy, Golden fur, Labrador
```

## isinstance() and issubclass()

### isinstance() -- Check Object Type

```python
class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass
class GoldenRetriever(Dog): pass

dog = Dog()
cat = Cat()
golden = GoldenRetriever()

print(isinstance(dog, Dog))           # True
print(isinstance(dog, Animal))        # True (Dog is a subclass of Animal)
print(isinstance(cat, Animal))        # True
print(isinstance(cat, Dog))           # False
print(isinstance(golden, Dog))        # True (GoldenRetriever is subclass of Dog)
print(isinstance(golden, Animal))     # True
print(isinstance(dog, (Dog, Cat)))    # True (dog is Dog)
print(isinstance(cat, (Dog, Cat)))    # True (cat is Cat)
```

### issubclass() -- Check Class Relationship

```python
print(issubclass(Dog, Animal))          # True
print(issubclass(Cat, Animal))          # True
print(issubclass(GoldenRetriever, Dog)) # True
print(issubclass(Dog, Cat))             # False
print(issubclass(Dog, object))          # True (all classes inherit from object)
print(issubclass(Animal, Dog))          # False
```

### Practical Example: Polymorphic Function

```python
def animal_sound(animal):
    if isinstance(animal, Animal):
        if isinstance(animal, Dog):
            print("Woof!")
        elif isinstance(animal, Cat):
            print("Meow!")
        else:
            print("Generic animal sound.")
    else:
        print("Not an animal.")

animal_sound(dog)
animal_sound(cat)
animal_sound(golden)
animal_sound("hello")
```

## Multiple Inheritance

A class can inherit from multiple parent classes.

```python
class Flyer:
    def fly(self):
        print("Flying...")

    def move(self):
        print("Moving through air.")

class Swimmer:
    def swim(self):
        print("Swimming...")

    def move(self):
        print("Moving through water.")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.quack()
duck.fly()
duck.swim()
duck.move()  # Which move() is called?
```

Output:
```
Quack!
Flying...
Swimming...
Moving through air.
```

### Method Resolution Order (MRO)

MRO determines the order in which base classes are searched when looking for a method. Python uses C3 linearization algorithm.

Check MRO with `ClassName.__mro__` or `ClassName.mro()`:

```python
print(Duck.__mro__)
print(Duck.mro())
```

Output:
```
(<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>)
[<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>]
```

**Resolution order:** `Duck` -> `Flyer` -> `Swimmer` -> `object`

That is why `duck.move()` called `Flyer.move()` (the first parent in MRO).

### Practical Multiple Inheritance Example

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(f"Vehicle: {make} {model}")

    def start(self):
        print("Vehicle engine started.")

class Radio:
    def __init__(self, brand="Sony"):
        self.radio_brand = brand
        print(f"Radio: {brand}")

    def play_music(self):
        print("Playing music...")

class GPS:
    def __init__(self):
        print("GPS initialized.")

    def navigate(self, destination):
        print(f"Navigating to {destination}.")

class Car(Vehicle, Radio, GPS):
    def __init__(self, make, model, radio_brand="Sony"):
        Vehicle.__init__(self, make, model)
        Radio.__init__(self, radio_brand)
        GPS.__init__(self)

    def start(self):
        super().start()
        print("Car is ready to drive.")

car = Car("Tesla", "Model 3", "Bose")
car.start()
car.play_music()
car.navigate("New York")
print(f"\nMRO: {[c.__name__ for c in Car.__mro__]}")
```

Output:
```
Vehicle: Tesla Model 3
Radio: Bose
GPS initialized.
Vehicle engine started.
Car is ready to drive.
Playing music...
Navigating to New York.

MRO: ['Car', 'Vehicle', 'Radio', 'GPS', 'object']
```

## The Diamond Problem

The diamond problem occurs when a class inherits from two classes that share a common ancestor.

```
    A
   / \
  B   C
   \ /
    D
```

Python's MRO resolves this using the C3 linearization algorithm:

```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass

d = D()
d.method()
print(D.__mro__)
```

Output:
```
B.method
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

**MRO for D:** D -> B -> C -> A -> object

### The `super()` and MRO in Diamond

When `super()` is used in all classes with proper signatures, the MRO ensures each `__init__` is called exactly once:

```python
class A:
    def __init__(self):
        print("A.__init__")
        super().__init__()  # Calls object.__init__

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
print(f"\nMRO: {[c.__name__ for c in D.__mro__]}")
```

Output:
```
D.__init__
B.__init__
C.__init__
A.__init__
```

The `super()` chain follows MRO: D -> B -> C -> A -> object, and each `__init__` is called exactly once.

## Complete Example: Shape Hierarchy

```python
import math

class Shape:
    """Base class for all shapes."""

    def __init__(self, color="black"):
        self.color = color

    def area(self):
        """Must be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement area()")

    def perimeter(self):
        """Must be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement perimeter()")

    def describe(self):
        return f"{self.color} {type(self).__name__}: " \
               f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius, color="black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height, color="black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side, color="black"):
        super().__init__(side, side, color)


class Triangle(Shape):
    def __init__(self, a, b, c, color="black"):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [
    Circle(5, "red"),
    Rectangle(4, 6, "blue"),
    Square(4, "green"),
    Triangle(3, 4, 5, "yellow"),
]

for shape in shapes:
    print(shape.describe())
    print(f"  isinstance(Shape)? {isinstance(shape, Shape)}")
    print()
```

Output:
```
red Circle: area=78.54, perimeter=31.42
  isinstance(Shape)? True

blue Rectangle: area=24.00, perimeter=20.00
  isinstance(Shape)? True

green Square: area=16.00, perimeter=16.00
  isinstance(Shape)? True

yellow Triangle: area=6.00, perimeter=12.00
  isinstance(Shape)? True
```

## Inheritance Summary

```python
# Inheritance hierarchy
#     Shape
#    /  |  \
# Circle Rectangle Triangle
#          |
#        Square


print("*** Inheritance Relationships ***")
print(f"issubclass(Square, Rectangle): {issubclass(Square, Rectangle)}")
print(f"issubclass(Square, Shape): {issubclass(Square, Shape)}")
print(f"issubclass(Rectangle, Shape): {issubclass(Rectangle, Shape)}")
print(f"issubclass(Circle, Shape): {issubclass(Circle, Shape)}")
print(f"issubclass(Triangle, Shape): {issubclass(Triangle, Shape)}")

square = Square(4)
rectangle = Rectangle(4, 6)
print(f"\nisinstance(square, Square): {isinstance(square, Square)}")
print(f"isinstance(square, Rectangle): {isinstance(square, Rectangle)}")
print(f"isinstance(square, Shape): {isinstance(square, Shape)}")
print(f"isinstance(rectangle, Square): {isinstance(rectangle, Square)}")
```

## Practice Problems

1. **Employee Hierarchy** -- Create a base class `Employee` with name, emp_id, salary. Create subclasses `Manager` (with bonus percentage), `Developer` (with programming languages list), `Intern` (with duration). Each should have a `calculate_pay()` method that differs.
   <details>
   <summary>Show Answer</summary>

   ```python
   class Employee:
       def __init__(self, name, emp_id, salary):
           self.name = name
           self.emp_id = emp_id
           self.salary = salary

       def calculate_pay(self):
           return self.salary

       def __str__(self):
           return f"{self.name} ({self.emp_id}): ${self.calculate_pay():.2f}"

   class Manager(Employee):
       def __init__(self, name, emp_id, salary, bonus_pct=0.15):
           super().__init__(name, emp_id, salary)
           self.bonus_pct = bonus_pct

       def calculate_pay(self):
           return self.salary * (1 + self.bonus_pct)

   class Developer(Employee):
       def __init__(self, name, emp_id, salary, languages=None):
           super().__init__(name, emp_id, salary)
           self.languages = languages or []

       def calculate_pay(self):
           bonus = len(self.languages) * 2000
           return self.salary + bonus

   class Intern(Employee):
       def __init__(self, name, emp_id, stipend, duration_months=3):
           super().__init__(name, emp_id, stipend)
           self.duration_months = duration_months

       def calculate_pay(self):
           return self.salary * self.duration_months

   emps = [
       Manager("Alice", "M001", 80000, 0.20),
       Developer("Bob", "D001", 70000, ["Python", "Java", "JS"]),
       Intern("Charlie", "I001", 2000, 6),
   ]
   for e in emps:
       print(e)
   ```
   </details>

2. **Library System** -- Create `LibraryItem` (title, year, is_borrowed). Subclasses: `Book` (author, pages), `DVD` (director, duration), `Magazine` (issue_number, month). Each should override `__str__`. Use super() in `__init__`.
   <details>
   <summary>Show Answer</summary>

   ```python
   class LibraryItem:
       def __init__(self, title, year):
           self.title = title
           self.year = year
           self.is_borrowed = False

       def borrow(self):
           if self.is_borrowed:
               return False
           self.is_borrowed = True
           return True

       def return_item(self):
           self.is_borrowed = False

       def __str__(self):
           status = "B" if self.is_borrowed else "A"
           return f"[{status}] {self.title} ({self.year})"

   class Book(LibraryItem):
       def __init__(self, title, year, author, pages):
           super().__init__(title, year)
           self.author = author
           self.pages = pages

       def __str__(self):
           return f"{super().__str__()} by {self.author}, {self.pages}p"

   class DVD(LibraryItem):
       def __init__(self, title, year, director, duration_min):
           super().__init__(title, year)
           self.director = director
           self.duration_min = duration_min

       def __str__(self):
           return f"{super().__str__()} dir. {self.director}, {self.duration_min}min"

   class Magazine(LibraryItem):
       def __init__(self, title, year, issue_no, month):
           super().__init__(title, year)
           self.issue_no = issue_no
           self.month = month

       def __str__(self):
           return f"{super().__str__()} Vol.{self.issue_no} ({self.month})"

   items = [
       Book("1984", 1949, "Orwell", 328),
       DVD("Inception", 2010, "Nolan", 148),
       Magazine("NatGeo", 2024, 250, "March"),
   ]
   for item in items:
       print(item)
   ```
   </details>

3. **Multiple Inheritance: Flying Car** -- Create classes `Car` (start, stop, drive), `Aircraft` (takeoff, land, fly). Create `FlyingCar` that inherits from both. Implement MRO properly. Use super() to ensure both parents are initialized.
   <details>
   <summary>Show Answer</summary>

   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model
           print(f"Car: {make} {model}")

       def start(self):
           print("Car engine started.")

       def drive(self):
           print("Driving on road.")

   class Aircraft:
       def __init__(self, max_altitude=10000):
           self.max_altitude = max_altitude
           print(f"Aircraft: max altitude {max_altitude}ft")

       def takeoff(self):
           print("Aircraft taking off.")

       def fly(self):
           print("Flying in air.")

   class FlyingCar(Car, Aircraft):
       def __init__(self, make, model, max_altitude=10000):
           Car.__init__(self, make, model)
           Aircraft.__init__(self, max_altitude)
           print("FlyingCar created!")

       def start(self):
           super().start()
           print("FlyingCar systems ready.")

   fc = FlyingCar("Aero", "X1", 5000)
   fc.start()
   fc.drive()
   fc.takeoff()
   fc.fly()
   print(f"MRO: {[c.__name__ for c in FlyingCar.__mro__]}")
   ```
   </details>

4. **Override and Extend** -- Create a base `Logger` class with `log(message, level)` method. Create `FileLogger` (writes to file) and `ConsoleLogger` (prints to console). Both override `log` and extend it with additional formatting. Use super() to call parent's log.
   <details>
   <summary>Show Answer</summary>

   ```python
   class Logger:
       def __init__(self, prefix="[LOG]"):
           self.prefix = prefix

       def log(self, message, level="INFO"):
           print(f"{self.prefix} [{level}] {message}")

   class FileLogger(Logger):
       def __init__(self, filename, prefix="[FILE]"):
           super().__init__(prefix)
           self.filename = filename

       def log(self, message, level="INFO"):
           super().log(message, level)
           with open(self.filename, "a") as f:
               import datetime
               ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               f.write(f"[{ts}] [{level}] {message}\n")
           print(f"(Logged to {self.filename})")

   class ConsoleLogger(Logger):
       def __init__(self, prefix="[CONSOLE]"):
           super().__init__(prefix)
           self._count = 0

       def log(self, message, level="INFO"):
           self._count += 1
           colored = f"\033[92m{self.prefix}\033[0m" if level == "INFO" else \
                     f"\033[93m{self.prefix}\033[0m" if level == "WARN" else \
                     f"\033[91m{self.prefix}\033[0m"
           print(f"{colored} [{level}] #{self._count}: {message}")

   cl = ConsoleLogger()
   cl.log("System started")
   cl.log("Low memory", "WARN")
   cl.log("Disk failure", "ERROR")

   fl = FileLogger("app.log")
   fl.log("App initialized")
   fl.log("Connection lost", "ERROR")
   ```
   </details>

5. **Zoo Hierarchy with isinstance** -- Create `Animal` base with name, age. Subclasses: `Mammal`, `Bird`, `Fish`. Further subclasses: `Dog(Mammal)`, `Eagle(Bird)`, `Salmon(Fish)`. Create a `Zoo` class that holds animals and has methods like `feed_all()`, `list_mammals()`, `count_by_type()`. Use isinstance extensively.
   <details>
   <summary>Show Answer</summary>

   ```python
   class Animal:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def make_sound(self):
           return "..."

       def __str__(self):
           return f"{self.name} ({type(self).__name__}, {self.age}y)"

   class Mammal(Animal): pass
   class Bird(Animal): pass
   class Fish(Animal): pass

   class Dog(Mammal):
       def make_sound(self): return "Woof!"
   class Eagle(Bird):
       def make_sound(self): return "Screech!"
   class Salmon(Fish):
       def make_sound(self): return "Blub!"

   class Zoo:
       def __init__(self, name):
           self.name = name
           self.animals = []

       def add(self, animal):
           self.animals.append(animal)

       def feed_all(self):
           for a in self.animals:
               print(f"Feeding {a.name}... {a.make_sound()}")

       def list_mammals(self):
           return [a for a in self.animals if isinstance(a, Mammal)]

       def count_by_type(self):
           counts = {"Mammal": 0, "Bird": 0, "Fish": 0}
           for a in self.animals:
               if isinstance(a, Mammal): counts["Mammal"] += 1
               if isinstance(a, Bird): counts["Bird"] += 1
               if isinstance(a, Fish): counts["Fish"] += 1
           return counts

   zoo = Zoo("City Zoo")
   zoo.add(Dog("Rex", 3))
   zoo.add(Eagle("Freedom", 5))
   zoo.add(Salmon("Nemo", 1))
   zoo.add(Dog("Max", 2))
   zoo.feed_all()
   print(f"\nMammals: {[a.name for a in zoo.list_mammals()]}")
   print(f"Counts: {zoo.count_by_type()}")
   ```
   </details>
