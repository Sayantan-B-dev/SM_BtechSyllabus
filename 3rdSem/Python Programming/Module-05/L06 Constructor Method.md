# Constructor Method

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 6  
**Date:** 14-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## Understanding `__init__`

The `__init__` method is Python's constructor. It is called automatically when an object is created. Its purpose is to initialize the object's attributes.

### What Happens During Object Creation

```python
class Demo:
    def __init__(self, value):
        print(f"__init__ called with value={value}")
        self.value = value

print("Creating object...")
obj = Demo(42)
print(f"Object value: {obj.value}")
```

Output:
```
Creating object...
__init__ called with value=42
Object value: 42
```

### The Full Lifecycle

```python
class LifecycleDemo:
    def __new__(cls, *args, **kwargs):
        print(f"1. __new__ called (allocating memory)")
        instance = super().__new__(cls)
        print(f"2. Instance created at {id(instance)}")
        return instance

    def __init__(self, name):
        print(f"3. __init__ called with name={name}")
        self.name = name

    def __del__(self):
        print(f"4. __del__ called (destroying {self.name})")

print("Step 0: About to create object...")
obj = LifecycleDemo("Test")
print(f"Object created: {obj.name}")
print("Deleting reference...")
del obj
print("Done.")
```

Output:
```
Step 0: About to create object...
1. __new__ called (allocating memory)
2. Instance created at 2653847592832
3. __init__ called with name=Test
Object created: Test
Deleting reference...
4. __del__ called (destroying Test)
Done.
```

## Default Constructor

If you do not define `__init__`, Python provides a default constructor that does nothing.

```python
class Point:
    pass  # No __init__ defined

p = Point()  # Works -- uses default constructor
print(type(p))

# But no attributes are initialized
# p.x = 10  # This would work, but no automatic initialization
```

Output:
```
<class '__main__.Point'>
```

With a manual default constructor:

```python
class Point:
    def __init__(self):
        # Initialize default values
        self.x = 0
        self.y = 0

p = Point()
print(f"Point: ({p.x}, {p.y})")

# We can still assign after creation
p.x = 10
p.y = 20
print(f"Updated: ({p.x}, {p.y})")
```

Output:
```
Point: (0, 0)
Updated: (10, 20)
```

## Parameterized Constructor

A parameterized constructor accepts arguments to initialize instance attributes with specific values.

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# All objects get their own dimensions
r1 = Rectangle(10, 5)
r2 = Rectangle(7, 3)

print(f"R1: {r1.length}x{r1.width}, Area={r1.area()}")
print(f"R2: {r2.length}x{r2.width}, Area={r2.area()}")
```

Output:
```
R1: 10x5, Area=50
R2: 7x3, Area=21
```

## Constructor Overloading? Workaround with Default Arguments

Python does NOT support constructor overloading (defining multiple `__init__` methods with different signatures). The last definition would override the previous ones.

```python
class MyClass:
    def __init__(self, a):
        print(f"First __init__ with a={a}")
        self.a = a

    def __init__(self, a, b):  # Overrides the first one!
        print(f"Second __init__ with a={a}, b={b}")
        self.a = a
        self.b = b

# Only the second __init__ exists
obj = MyClass(1, 2)  # Works
# obj = MyClass(1)  # Would fail (missing b argument)
```

### Workaround 1: Default Parameters

```python
class Student:
    def __init__(self, name, age=None, grade=None):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        parts = [f"Name: {self.name}"]
        if self.age is not None:
            parts.append(f"Age: {self.age}")
        if self.grade is not None:
            parts.append(f"Grade: {self.grade}")
        return ", ".join(parts)

# Multiple ways to create Student objects
s1 = Student("Alice")                    # Name only
s2 = Student("Bob", 20)                  # Name + age
s3 = Student("Charlie", 19, "A")         # Name + age + grade
s4 = Student("Diana", grade="B")         # Name + grade (keyword arg)

print(s1)
print(s2)
print(s3)
print(s4)
```

Output:
```
Name: Alice
Name: Bob, Age: 20
Name: Charlie, Age: 19, Grade: A
Name: Diana, Grade: B
```

### Workaround 2: Variable Arguments

```python
class ShoppingCart:
    def __init__(self, *items):
        self.items = list(items)
        self.total = 0

    def add(self, *new_items):
        self.items.extend(new_items)

    def __str__(self):
        return f"Cart({len(self.items)} items): {self.items}"

# Varying number of arguments
cart1 = ShoppingCart()
cart2 = ShoppingCart("apple")
cart3 = ShoppingCart("apple", "banana", "cherry")

print(cart1)
print(cart2)
print(cart3)
cart3.add("date", "elderberry")
print(cart3)
```

Output:
```
Cart(0 items): []
Cart(1 items): ['apple']
Cart(3 items): ['apple', 'banana', 'cherry']
Cart(5 items): ['apple', 'banana', 'cherry', 'date', 'elderberry']
```

### Workaround 3: Class Methods as Alternative Constructors

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_full_name(cls, full_name, age):
        """Create from 'First Last' string."""
        first, last = full_name.split()
        return cls(first, last, age)

    @classmethod
    def from_dict(cls, data):
        """Create from dictionary."""
        return cls(data["first"], data["last"], data["age"])

    @classmethod
    def child(cls, first_name, last_name):
        """Create a child (age defaults to 0)."""
        return cls(first_name, last_name, 0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

p1 = Person("John", "Doe", 30)
p2 = Person.from_full_name("Jane Smith", 25)
p3 = Person.from_dict({"first": "Bob", "last": "Brown", "age": 40})
p4 = Person.child("Timmy", "Jones")

print(p1)
print(p2)
print(p3)
print(p4)
```

Output:
```
John Doe (30)
Jane Smith (25)
Bob Brown (40)
Timmy Jones (0)
```

## The `__new__` Method (Object Creation)

`__new__` is responsible for creating and returning a new instance of the class. It runs before `__init__`.

### `__new__` vs `__init__`

| Feature | `__new__` | `__init__` |
|---|---|---|
| When called | First (memory allocation) | Second (initialization) |
| Purpose | Create the object | Initialize the object |
| Must return | The instance | Nothing (None) |
| First param | `cls` (class) | `self` (instance) |
| When to override | Rarely (metaprogramming, singletons) | Almost always |

```python
class CustomClass:
    def __new__(cls, *args, **kwargs):
        print(f"1. __new__ called with args={args}")
        instance = super().__new__(cls)
        print(f"2. Instance created: {id(instance)}")
        return instance

    def __init__(self, value):
        print(f"3. __init__ called with value={value}")
        self.value = value

obj = CustomClass(42)
print(f"4. Object ready: {obj.value}")
```

Output:
```
1. __new__ called with args=(42,)
2. Instance created: 2653847592832
3. __init__ called with value=42
4. Object ready: 42
```

### Using `__new__` with Immutable Types

`__new__` is necessary when subclassing immutable types like `int`, `str`, `tuple` because they cannot be initialized in `__init__`.

```python
class PositiveInteger(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Value must be non-negative.")
        return super().__new__(cls, value)

    def __init__(self, value):
        # int's __init__ is a no-op for subclasses
        pass

n1 = PositiveInteger(5)
print(n1, type(n1))

try:
    n2 = PositiveInteger(-5)
except ValueError as e:
    print(f"Error: {e}")
```

Output:
```
5 <class '__main__.PositiveInteger'>
Error: Value must be non-negative.
```

## Singleton Pattern Using `__new__`

The Singleton pattern ensures a class has only one instance and provides a global point of access to it.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the singleton instance...")
            cls._instance = super().__new__(cls)
        else:
            print("Returning existing singleton instance...")
        return cls._instance

    def __init__(self, name="Default"):
        if not hasattr(self, "_initialized"):
            self.name = name
            self._initialized = True
            print(f"  Initialized with name={name}")
        else:
            print(f"  Already initialized (name={self.name})")

# Test singleton behavior
s1 = Singleton("First")
s2 = Singleton("Second")
s3 = Singleton()

print(f"s1 is s2: {s1 is s2}")  # True -- same object
print(f"s1.name: {s1.name}")     # "First" -- not overwritten
print(f"s2.name: {s2.name}")     # "First" -- same object
```

Output:
```
Creating the singleton instance...
  Initialized with name=First
Returning existing singleton instance...
  Already initialized (name=First)
Returning existing singleton instance...
  Already initialized (name=First)
s1 is s2: True
s1.name: First
s2.name: First
```

### Practical Singleton: Configuration Manager

```python
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = {}
            cls._instance._initialized = False
        return cls._instance

    def load(self, filename="config.txt"):
        if self._initialized:
            print("Config already loaded.")
            return
        try:
            with open(filename, "r") as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split("=", 1)
                        self._config[key.strip()] = value.strip()
            self._initialized = True
            print(f"Loaded {len(self._config)} config values.")
        except FileNotFoundError:
            print(f"Config file '{filename}' not found. Using defaults.")
            self._config = {"theme": "dark", "language": "en"}
            self._initialized = True

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        self._config[key] = value

    def __str__(self):
        return str(self._config)


# Both references point to the same object
config1 = ConfigManager()
config2 = ConfigManager()

config1.load()
config2.set("debug", "true")

print(config1)  # Includes debug=true
print(f"Same object: {config1 is config2}")
```

## Constructor Best Practices

### 1. Keep `__init__` Simple -- Only Assignments

```python
# GOOD
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# AVOID (don't do heavy work in __init__)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.db_connect()   # Heavy work -- not ideal
        self.load_grades()  # Better in a separate method
```

### 2. Validate Input in Constructor

```python
class Account:
    def __init__(self, account_number, balance=0):
        if not isinstance(account_number, str) or len(account_number) < 5:
            raise ValueError("Invalid account number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.balance = balance

# Valid
acc = Account("ACC-001", 1000)

# Invalid
try:
    acc2 = Account("X", -50)
except ValueError as e:
    print(f"Error: {e}")
```

### 3. Use Immutable Defaults Carefully

```python
# BAD -- mutable default argument
class ShoppingCart:
    def __init__(self, items=[]):  # Same list shared by ALL instances!
        self.items = items

cart1 = ShoppingCart()
cart2 = ShoppingCart()
cart1.items.append("apple")
print(cart2.items)  # ['apple'] -- shared!

# GOOD -- use None and create new list
class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items is not None else []

cart1 = ShoppingCart()
cart2 = ShoppingCart()
cart1.items.append("apple")
print(cart2.items)  # [] -- separate list
```

### 4. Document Parameters

```python
class Employee:
    """Represents an employee in the system.

    Args:
        emp_id: Unique employee identifier (str)
        name: Full name of the employee (str)
        department: Department code (str)
        salary: Annual salary in USD (float)
    """
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
```

## Complete Example: Employee Management

```python
class Employee:
    company = "TechCorp"
    _id_counter = 1000

    def __init__(self, name, department, salary):
        # Validate inputs
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.emp_id = f"EMP{Employee._id_counter}"
        Employee._id_counter += 1
        self.name = name
        self.department = department
        self.salary = salary
        self.is_active = True

    def __str__(self):
        return f"{self.emp_id}: {self.name} ({self.department}) - ${self.salary}"

    def __repr__(self):
        return f"Employee('{self.name}', '{self.department}', {self.salary})"


class Manager(Employee):
    def __init__(self, name, department, salary, team_size=0):
        super().__init__(name, department, salary)
        self.team_size = team_size
        self.bonus = 0.10  # 10% bonus

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Manager of {self.team_size} people | "
                f"Bonus: {self.bonus*100:.0f}%")


# Create employees
e1 = Employee("Alice", "Engineering", 75000)
e2 = Employee("Bob", "Marketing", 65000)
m1 = Manager("Charlie", "Engineering", 95000, 8)

print(e1)
print(e2)
print(m1)

# Demonstrate that each Employee gets unique ID
e3 = Employee("Diana", "HR", 55000)
print(f"\nIDs: {e1.emp_id}, {e2.emp_id}, {e3.emp_id}, {m1.emp_id}")
```

Output:
```
EMP1000: Alice (Engineering) - $75000
EMP1001: Bob (Marketing) - $65000
EMP1002: Charlie (Engineering) - $95000 | Manager of 8 people | Bonus: 10%

IDs: EMP1000, EMP1001, EMP1003, EMP1002
```

## Practice Problems

1. **Book Constructor with Validation** -- Create a `Book` class with `__init__` that validates: title (non-empty string), author (non-empty string), isbn (13-digit string or int), pages (positive int), year (between 1450 and current year). Raise `ValueError` for invalid data.

2. **Multiple Constructor Patterns** -- Create a `Time` class that can be constructed from (hours, minutes), from a string "HH:MM", or from total minutes. Use default arguments and class methods.

3. **Singleton Logger** -- Implement a `Logger` singleton using `__new__`. It should have a `log(level, message)` method and store all log entries in a list. The `__init__` should only initialize once.

4. **Immutable Point** -- Create a `Point2D` class that subclasses `tuple` to create immutable 2D points. Implement `__new__` to accept x, y and store them. Add a `distance_from_origin()` method.

5. **Database Connection Pool** -- Create a `ConnectionPool` class where each pool has a max size. Use `__new__` to manage a fixed number of connections. Implement `acquire()` and `release()` methods.

---

## Practice Problems

1. **Book Constructor with Validation**

```python
class Book:
    def __init__(self, title, author, isbn, pages, year):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        if not author or not author.strip():
            raise ValueError("Author cannot be empty.")
        isbn_str = str(isbn).replace("-", "")
        if len(isbn_str) != 13 or not isbn_str.isdigit():
            raise ValueError("ISBN must be 13 digits.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be positive integer.")
        if not isinstance(year, int) or year < 1450 or year > 2026:
            raise ValueError(f"Year {year} out of range.")
        self.title = title
        self.author = author
        self.isbn = isbn_str
        self.pages = pages
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

try:
    b = Book("1984", "George Orwell", "9780451524935", 328, 1949)
    print(b)
    Book("", "Author", "123", -5, 100)  # Should fail
except ValueError as e:
    print(f"Error: {e}")
```

2. **Multiple Constructor Patterns**

```python
class Time:
    def __init__(self, hours=0, minutes=0):
        self._validate(hours, minutes)
        self.hours = hours
        self.minutes = minutes

    @classmethod
    def from_string(cls, time_str):
        parts = time_str.split(":")
        if len(parts) != 2:
            raise ValueError("Use format HH:MM")
        return cls(int(parts[0]), int(parts[1]))

    @classmethod
    def from_total_minutes(cls, total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return cls(hours, minutes)

    def _validate(self, h, m):
        if not (0 <= h < 24):
            raise ValueError(f"Hours {h} out of range (0-23)")
        if not (0 <= m < 60):
            raise ValueError(f"Minutes {m} out of range (0-59)")

    def total_minutes(self):
        return self.hours * 60 + self.minutes

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

t1 = Time(14, 30)
t2 = Time.from_string("09:15")
t3 = Time.from_total_minutes(450)

print(t1, t2, t3)
```

3. **Singleton Logger**

```python
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._log_entries = []
            self._initialized = True

    def log(self, level, message):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level.upper()}] {message}"
        self._log_entries.append(entry)
        print(entry)

    def get_logs(self):
        return self._log_entries

logger1 = Logger()
logger2 = Logger()
logger1.log("INFO", "Application started")
logger2.log("WARN", "Low disk space")
print(f"Same instance: {logger1 is logger2}")
print(f"All logs ({len(logger1.get_logs())}):")
for log in logger1.get_logs():
    print(f"  {log}")
```

4. **Immutable Point**

```python
class Point2D(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    def __init__(self, x, y):
        # tuple is immutable, so __init__ is a no-op
        pass

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point2D(3, 4)
print(f"Point: {p}")
print(f"x={p.x}, y={p.y}")
print(f"Distance from origin: {p.distance_from_origin()}")
print(f"Is tuple: {isinstance(p, tuple)}")

try:
    p.x = 10  # Should fail -- immutable
except AttributeError as e:
    print(f"Cannot modify: {e}")
```

5. **Database Connection Pool**

```python
class ConnectionPool:
    _instances = {}

    def __new__(cls, pool_name, max_size=5):
        if pool_name not in cls._instances:
            instance = super().__new__(cls)
            instance.pool_name = pool_name
            instance.max_size = max_size
            instance._available = list(range(max_size))
            instance._in_use = set()
            instance._initialized = True
            cls._instances[pool_name] = instance
            print(f"Created pool '{pool_name}' (max {max_size})")
        return cls._instances[pool_name]

    def acquire(self):
        if not self._available:
            print(f"Pool '{self.pool_name}' exhausted!")
            return None
        conn_id = self._available.pop(0)
        self._in_use.add(conn_id)
        print(f"Acquired connection {conn_id} "
              f"(available: {len(self._available)})")
        return conn_id

    def release(self, conn_id):
        if conn_id not in self._in_use:
            print(f"Connection {conn_id} not in use!")
            return
        self._in_use.remove(conn_id)
        self._available.append(conn_id)
        print(f"Released connection {conn_id} "
              f"(available: {len(self._available)})")

pool1 = ConnectionPool("db-main", 3)
pool2 = ConnectionPool("db-main")  # Same pool
print(f"Same pool: {pool1 is pool2}")

c1 = pool1.acquire()
c2 = pool1.acquire()
c3 = pool1.acquire()
c4 = pool1.acquire()  # Should be None
pool1.release(c1)
pool1.acquire()
```
