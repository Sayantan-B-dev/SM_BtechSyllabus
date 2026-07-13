# Creating Classes and Objects

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 5  
**Date:** 12-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## More on Object Creation

When you create an object, Python does the following:
1. Allocates memory for the object
2. Calls `__new__` to create the object (we cover this in L06)
3. Calls `__init__` to initialize the object's attributes
4. Returns the object reference

```python
class Sample:
    def __init__(self, value):
        print(f"Creating Sample object with value={value}")
        self.value = value

obj = Sample(42)
print(f"Object created: {obj}")
print(f"Object value: {obj.value}")
```

Output:
```
Creating Sample object with value=42
Object created: <__main__.Sample object at 0x0000021A3B4D0FD0>
Object value: 42
```

## Class Variables vs Instance Variables

### Memory and Scope Differences

| Feature | Class Variable | Instance Variable |
|---|---|---|
| Defined | Inside class, outside methods | Inside `__init__` via `self` |
| Scope | Shared by all instances | Unique to each instance |
| Access | `ClassName.var` or `self.var` | `self.var` only |
| Modified | Affects all instances (unless shadowed) | Affects only that instance |
| Use Case | Constants, counters, shared config | Object-specific data |

### Detailed Example

```python
class Employee:
    # Class variables
    company_name = "TechCorp"
    location = "New York"
    total_employees = 0

    def __init__(self, name, emp_id, salary):
        # Instance variables
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.is_active = True
        Employee.total_employees += 1

    def display(self):
        print(f"ID: {self.emp_id} | {self.name} | ${self.salary}")
        print(f"Company: {self.company_name} | Location: {Employee.location}")
        print(f"Active: {self.is_active}")

# Create objects
e1 = Employee("Alice", "E001", 50000)
e2 = Employee("Bob", "E002", 60000)
e3 = Employee("Charlie", "E003", 55000)

e1.display()
print()

# Access class variable via class or instance
print(Employee.company_name)  # TechCorp
print(e1.company_name)        # TechCorp (inherits from class)
print(e2.company_name)        # TechCorp
print()

# Modify class variable -- affects all
Employee.location = "San Francisco"
print(e1.location)  # San Francisco
print(e3.location)  # San Francisco
print()

# Modify instance variable -- only affects that instance
e1.location = "Remote"  # Creates instance variable shadowing class variable
print(e1.location)      # Remote (instance)
print(e2.location)      # San Francisco (class)
print(Employee.location) # San Francisco (class unchanged)
```

Output:
```
ID: E001 | Alice | $50000
Company: TechCorp | Location: New York
Active: True

TechCorp
TechCorp
TechCorp

San Francisco
San Francisco

Remote
San Francisco
San Francisco
```

### When to Use Each

```python
# Class variable: default values, shared state
class ConnectionPool:
    max_connections = 10  # All pools share this limit
    active_connections = 0

    def __init__(self, name):
        self.name = name
        self.connections = []  # Instance-specific

    def connect(self):
        if ConnectionPool.active_connections < ConnectionPool.max_connections:
            ConnectionPool.active_connections += 1
            conn_id = f"{self.name}-conn-{len(self.connections)}"
            self.connections.append(conn_id)
            print(f"Connected: {conn_id}")
        else:
            print(f"Max connections ({ConnectionPool.max_connections}) reached!")

pool1 = ConnectionPool("db1")
pool2 = ConnectionPool("db2")

pool1.connect()
pool2.connect()
print(f"Active connections: {ConnectionPool.active_connections}")
```

Output:
```
Connected: db1-conn-0
Connected: db2-conn-0
Active connections: 2
```

## Instance Methods

Instance methods are functions defined inside a class that operate on an instance. They take `self` as the first parameter.

```python
class Calculator:
    def __init__(self, name):
        self.name = name
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Error")
            return "Error: division by zero"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        print(f"--- {self.name} History ---")
        for entry in self.history:
            print(f"  {entry}")
        print("---")

calc = Calculator("MyCalc")
calc.add(10, 5)
calc.subtract(20, 7)
calc.multiply(3, 4)
calc.divide(100, 0)
calc.divide(100, 3)
calc.show_history()
```

Output:
```
--- MyCalc History ---
  10 + 5 = 15
  20 - 7 = 13
  3 * 4 = 12
  100 / 0 = Error
  100 / 3 = 33.33333333333336
---
```

## Class Methods (@classmethod)

Class methods operate on the class itself rather than instances. They take `cls` as the first parameter (the class). Use the `@classmethod` decorator.

### Use Cases
- Factory methods that create instances
- Accessing/modifying class-level state
- Alternative constructors

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    @classmethod
    def from_string(cls, data_string):
        """Alternative constructor: parse from 'name,age,grade'"""
        name, age, grade = data_string.split(",")
        return cls(name.strip(), int(age.strip()), grade.strip())

    @classmethod
    def create_freshman(cls, name, age):
        """Factory method: creates a freshman student"""
        return cls(name, age, "F")

    @classmethod
    def get_school_info(cls):
        return "Springfield High School - Grade 9-12"

    def __str__(self):
        return f"{self.name} (age {self.age}, grade {self.grade})"


# Using regular constructor
s1 = Student("Alice", 16, "10th")
print(s1)

# Using class method (alternative constructor)
s2 = Student.from_string("Bob, 17, 11th")
print(s2)

# Using factory method
s3 = Student.create_freshman("Charlie", 14)
print(s3)

# Using class method for class-level info
print(Student.get_school_info())
```

Output:
```
Alice (age 16, grade 10th)
Bob (age 17, grade 11th)
Charlie (age 14, grade F)
Springfield High School - Grade 9-12
```

### Practical Example: Class Method for Configuration

```python
class DatabaseConfig:
    _config = {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "secret",
        "database": "mydb"
    }

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def default(cls):
        """Return a config with default settings."""
        return cls(**cls._config)

    @classmethod
    def from_file(cls, filename):
        """Load config from a file."""
        config = {}
        with open(filename, "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return cls(**config)

    @classmethod
    def update_default(cls, key, value):
        """Update default configuration."""
        cls._config[key] = value

    def __str__(self):
        return f"DB({self.host}:{self.port}/{self.database})"


# Use default config
default_db = DatabaseConfig.default()
print(default_db)

# Update default
DatabaseConfig.update_default("port", 3306)
print(DatabaseConfig.default())
```

## Static Methods (@staticmethod)

Static methods do not receive `self` or `cls`. They behave like regular functions but are namespaced inside the class for organizational purposes.

### Use Cases
- Utility functions related to the class
- Operations that do not depend on instance or class state

```python
class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_odd(n):
        return n % 2 != 0

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Negative numbers not allowed.")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

# Call without creating an instance
print(MathUtils.is_even(10))
print(MathUtils.is_odd(7))
print(MathUtils.factorial(5))
print(MathUtils.gcd(48, 18))
```

Output:
```
True
True
120
6
```

### Practical Example: Static Methods in a Class

```python
class Validator:
    @staticmethod
    def validate_email(email):
        if "@" not in email or "." not in email:
            return False
        local, domain = email.rsplit("@", 1)
        if not local or not domain:
            return False
        if "." not in domain:
            return False
        return True

    @staticmethod
    def validate_age(age):
        if not isinstance(age, (int, float)):
            return False
        return 0 <= age <= 150

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False, "Too short"
        if not any(c.isupper() for c in password):
            return False, "Need uppercase"
        if not any(c.isdigit() for c in password):
            return False, "Need digit"
        return True, "Valid"

class User:
    def __init__(self, email, age, password):
        if not Validator.validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        if not Validator.validate_age(age):
            raise ValueError(f"Invalid age: {age}")
        is_valid, msg = Validator.validate_password(password)
        if not is_valid:
            raise ValueError(f"Invalid password: {msg}")
        self.email = email
        self.age = age
        self.password = password
        print(f"User created: {email}")

User("alice@example.com", 25, "StrongPass1")
try:
    User("invalid-email", 25, "StrongPass1")
except ValueError as e:
    print(f"Error: {e}")
```

Output:
```
User created: alice@example.com
Error: Invalid email: invalid-email
```

## Comparison: Instance, Class, and Static Methods

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First param | `self` (instance) | `cls` (class) | None |
| Access instance data | Yes | No | No |
| Access class data | Yes | Yes | No (via class name) |
| Can be called on class | No (needs instance) | Yes | Yes |
| Can be called on instance | Yes | Yes | Yes |

```python
class Demo:
    class_var = "shared"

    def __init__(self, value):
        self.instance_var = value

    def instance_method(self):
        return f"Instance: {self.instance_var}, Class: {self.class_var}"

    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"

    @staticmethod
    def static_method():
        return "Static: no access to instance or class"

obj = Demo("my_value")
print(obj.instance_method())
print(Demo.class_method())
print(obj.class_method())   # Can call on instance too
print(Demo.static_method())
print(obj.static_method())  # Can call on instance too
```

Output:
```
Instance: my_value, Class: shared
Class: shared
Class: shared
Static: no access to instance or class
Static: no access to instance or class
```

## Property Decorators (@property, @setter, @deleter)

Properties allow you to define methods that are accessed like attributes, enabling controlled access to instance data.

### @property (Getter)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Protected attribute

    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    @property
    def area(self):
        """Computed property: area = pi * r^2"""
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        """Computed property: circumference = 2 * pi * r"""
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.radius)        # Access like an attribute (no parentheses)
print(c.area)          # Computed on-the-fly
print(c.circumference) # Computed on-the-fly
```

Output:
```
5
78.53975
31.4159
```

### @setter (Setter)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value
        print(f"Radius set to {value}")

c = Circle(5)
print(c.radius)

c.radius = 10  # Calls the setter
print(c.radius)

try:
    c.radius = -5  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

Output:
```
5
Radius set to 10
10
Error: Radius cannot be negative.
```

### @deleter (Deleter)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @radius.deleter
    def radius(self):
        print(f"Deleting radius (was {self._radius})")
        del self._radius

c = Circle(5)
print(c.radius)
del c.radius  # Calls the deleter
# print(c.radius)  # Would raise AttributeError
```

Output:
```
5
Deleting radius (was 5)
```

### Complete Property Example: Temperature with Validation

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero.")
        self._celsius = celsius

    @property
    def kelvin(self):
        return self._celsius + 273.15

    def __str__(self):
        return f"{self.celsius:.1f}C = {self.fahrenheit:.1f}F"

t = Temperature(25)
print(t)
print(f"Kelvin: {t.kelvin:.2f}K")

t.celsius = 100
print(f"Boiling: {t.fahrenheit:.1f}F")

t.fahrenheit = 32
print(f"Freezing: {t.celsius:.1f}C")

try:
    t.celsius = -300
except ValueError as e:
    print(f"Error: {e}")
```

Output:
```
25.0C = 77.0F
Kelvin: 298.15K
Boiling: 212.0F
Freezing: 0.0C
Error: Temperature below absolute zero.
```

## Summary: Method Type Decision Table

| Situation | Method Type |
|---|---|
| Operates on instance data (`self.xxx`) | Instance method |
| Creates instances (factory) | Class method |
| Needs class-level state, not instance | Class method |
| Utility function, no `self`/`cls` needed | Static method |
| Controlled attribute access | Property |
| Computed attribute (read-only) | Property |
| Validation on attribute set | Property setter |

## Practice Problems

1. **Product Inventory System** -- Create a `Product` class with class variable `tax_rate = 0.08`. Instance attributes: name, price, quantity. Instance methods: `total_cost()` (price * qty), `total_with_tax()` (total * (1+tax)). Class method: `set_tax_rate(new_rate)`. Static method: `convert_currency(amount, rate)`.

2. **Employee Management** -- Create an `Employee` class. Class variable: `company`. Class method: `from_csv(csv_line)` factory. Static method: `is_valid_email(email)`. Instance method: `yearly_cost()` returns salary + benefits.

3. **Rectangle with Properties** -- Create a `Rectangle` class with `_width` and `_height` as private attributes. Use `@property` for `width`, `height`, `area`, `perimeter`. Validate that width/height are positive in setters.

4. **BankAccount with Properties** -- Create a `BankAccount` class with a `_balance` attribute. Property `balance` (read-only). Property `formatted_balance` returns "$X,XXX.XX". Method `deposit` and `withdraw` (validate in methods, not setter).

5. **Student Management System** -- Create `Student` with class variable `school`, class method `from_string(data)`, static method `calculate_grade(marks_list)`, instance method `display()`. Use property for `average` that computes from `marks` list.

---

## Practice Problems

1. **Product Inventory System**

```python
class Product:
    tax_rate = 0.08

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def total_with_tax(self):
        return self.total_cost() * (1 + Product.tax_rate)

    @classmethod
    def set_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    @staticmethod
    def convert_currency(amount, rate):
        return amount * rate

p = Product("Laptop", 1000, 2)
print(f"Total: ${p.total_cost()}")
print(f"With tax: ${p.total_with_tax():.2f}")
Product.set_tax_rate(0.10)
print(f"With new tax: ${p.total_with_tax():.2f}")
print(f"EUR: {Product.convert_currency(1000, 0.85):.2f}")
```

2. **Employee Management**

```python
class Employee:
    company = "TechCorp"

    def __init__(self, name, salary, benefits=0):
        self.name = name
        self.salary = salary
        self.benefits = benefits

    @classmethod
    def from_csv(cls, csv_line):
        name, salary, benefits = csv_line.split(",")
        return cls(name.strip(), float(salary.strip()), float(benefits.strip()))

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email.split("@")[-1]

    def yearly_cost(self):
        return self.salary + self.benefits

e = Employee.from_csv("Alice, 50000, 10000")
print(f"{e.name}: ${e.yearly_cost()}")
print(f"Is valid? {Employee.is_valid_email('alice@test.com')}")
```

3. **Rectangle with Properties**

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

r = Rectangle(10, 5)
print(f"Area: {r.area}, Perimeter: {r.perimeter}")
r.width = 20
print(f"New area: {r.area}")
```

4. **BankAccount with Properties**

```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @property
    def formatted_balance(self):
        return f"${self._balance:,.2f}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self.formatted_balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self.formatted_balance}")

acc = BankAccount("Alice", 1000)
print(acc.formatted_balance)
acc.deposit(500)
acc.withdraw(200)
print(f"Balance: {acc.balance}")
```

5. **Student Management System**

```python
class Student:
    school = "Greenwood High"

    def __init__(self, name, marks=None):
        self.name = name
        self.marks = marks if marks else []

    @classmethod
    def from_string(cls, data):
        name, *marks = data.split(",")
        return cls(name.strip(), [float(m) for m in marks])

    @staticmethod
    def calculate_grade(marks_list):
        if not marks_list:
            return "N/A"
        avg = sum(marks_list) / len(marks_list)
        if avg >= 90: return "A"
        if avg >= 80: return "B"
        if avg >= 70: return "C"
        if avg >= 60: return "D"
        return "F"

    @property
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Student: {self.name}")
        print(f"School: {Student.school}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average:.1f}")
        print(f"Grade: {Student.calculate_grade(self.marks)}")

s = Student("Alice", [85, 90, 78, 92])
s.display()

s2 = Student.from_string("Bob, 75, 80, 88")
s2.display()
```
