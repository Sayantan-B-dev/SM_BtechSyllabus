# Encapsulation

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 8  
**Date:** 26-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## What is Encapsulation?

Encapsulation is the bundling of data (attributes) and methods that operate on that data into a single unit (class), restricting direct access to some of an object's components. It is a protective mechanism that prevents external code from accidentally modifying internal state.

### Why Encapsulation?

- **Data Protection** -- Prevents invalid or unauthorized modifications
- **Controlled Access** -- Provides controlled interfaces (getters/setters)
- **Implementation Hiding** -- Internal implementation can change without affecting external code
- **Maintainability** -- Reduces coupling between components

## Access Levels in Python

Python does not have strict access modifiers like `private` or `protected` in Java/C++. Instead, it uses naming conventions and name mangling.

| Convention | Name | Access Level |
|---|---|---|
| `name` | Public | Accessible from anywhere |
| `_name` | Protected | Convention: internal use only |
| `__name` | Private (name mangled) | Strongly hint: private |

## Public Members (Default)

By default, all attributes and methods in Python are public.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute

s = Student("Alice", 20)
print(s.name)  # Direct access -- perfectly fine
s.age = 21     # Direct modification -- fine
print(s.age)
```

## Protected Members (Convention)

A single underscore prefix `_` indicates "protected" -- it's a convention meaning "internal use, not part of the public API."

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name      # Public
        self._salary = salary  # Protected (by convention)

    def _calculate_bonus(self):  # Protected method
        return self._salary * 0.10

e = Employee("Alice", 50000)
print(e.name)          # OK
print(e._salary)       # Works, but violates convention
print(e._calculate_bonus())  # Works, but violates convention
```

**Important:** Python does not enforce the protected convention. It is a social contract among developers.

## Private Members and Name Mangling

Double underscore prefix `__` triggers name mangling. Python internally renames `__attr` to `_ClassName__attr`.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Name mangled to _BankAccount__balance

    def __secret_method(self):    # Name mangled to _BankAccount__secret_method
        return "This is secret"

acc = BankAccount("Alice", 1000)
# print(acc.__balance)  # AttributeError!
print(acc._BankAccount__balance)  # Works but strongly discouraged
print(acc._BankAccount__secret_method())
```

Output:
```
1000
This is secret
```

### How Name Mangling Works

```python
class Parent:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"  # Becomes _Parent__private

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private = "child private"  # Becomes _Child__private (different!)

p = Parent()
print(p.public)
print(p._protected)
# print(p.__private)  # Error

c = Child()
print(c.public)        # inherited
print(c._protected)    # inherited
# print(c.__private)  # Refers to _Child__private, not _Parent__private
```

Output:
```
public
protected
```

### Why Name Mangling Exists

Name mangling prevents accidental overriding of attributes in subclasses:

```python
class Base:
    def __init__(self):
        self.__value = 10  # _Base__value

    def get_value(self):
        return self.__value

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__value = 20  # _Derived__value (different attribute!)

obj = Derived()
print(obj.get_value())  # 10 (still reads _Base__value)
print(obj.__dict__)     # {'_Base__value': 10, '_Derived__value': 20}
```

Output:
```
10
{'_Base__value': 10, '_Derived__value': 20}
```

## Getter and Setter Methods (Traditional Approach)

Before the `@property` decorator, getters and setters were implemented as regular methods.

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # Getter
    def get_celsius(self):
        return self._celsius

    # Setter
    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero.")
        self._celsius = value

    # Getter for computed property
    def get_fahrenheit(self):
        return self._celsius * 9/5 + 32

    # Setter for computed property
    def set_fahrenheit(self, value):
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero.")
        self._celsius = celsius

t = Temperature(25)
print(t.get_celsius())
print(t.get_fahrenheit())

t.set_celsius(100)
print(t.get_fahrenheit())

t.set_fahrenheit(32)
print(t.get_celsius())

try:
    t.set_celsius(-300)
except ValueError as e:
    print(f"Error: {e}")
```

Output:
```
25
77.0
212.0
0.0
Error: Temperature below absolute zero.
```

## The `@property` Decorator (Pythonic Approach)

The `@property` decorator allows methods to be accessed like attributes, combining the simplicity of direct access with the control of getters/setters.

### Read-Only Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Read-only radius property."""
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.radius)    # Access like attribute (no parentheses)
print(c.area)      # Computed property
print(c.circumference)

# c.radius = 10    # AttributeError! No setter
```

### Property with Setter

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
        print(f"Radius updated to {value}")

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)

c.radius = 10
print(c.radius)
print(c.area)

try:
    c.radius = -5
except ValueError as e:
    print(f"Error: {e}")
```

### Property with Deleter

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
del c.radius
```

## Complete Example: BankAccount with Encapsulation

```python
class BankAccount:
    """Bank account with encapsulated balance."""

    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder  # Public
        self._account_number = account_number  # Protected
        self.__balance = initial_balance       # Private
        self.__transaction_history = []        # Private

    # --- Public interface ---

    @property
    def balance(self):
        """Read-only balance property."""
        return self.__balance

    @property
    def account_number(self):
        """Read-only masked account number."""
        return "XXXX" + self._account_number[-4:]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__log_transaction("DEPOSIT", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__log_transaction("WITHDRAW", amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    def get_statement(self):
        """Return list of recent transactions."""
        return self.__transaction_history[-10:]

    def transfer_to(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount.")
        self.withdraw(amount)
        target_account.deposit(amount)
        print(f"Transferred ${amount:.2f} to {target_account.account_holder}")

    # --- Private helpers ---

    def __log_transaction(self, ttype, amount):
        """Private: logs a transaction."""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {ttype}: ${amount:.2f} (bal: ${self.__balance:.2f})"
        self.__transaction_history.append(entry)

    # --- String representation (public) ---

    def __str__(self):
        return (f"Account[{self.account_number}] "
                f"{self.account_holder}: ${self.__balance:.2f}")


# Usage
alice = BankAccount("Alice", "12345678", 1000)
bob = BankAccount("Bob", "87654321", 500)

print(alice)
print(f"Balance: ${alice.balance}")

alice.deposit(500)
alice.withdraw(200)
alice.transfer_to(bob, 300)

print(f"\n{alice}")
print(f"{bob}")

print("\nRecent transactions:")
for t in alice.get_statement():
    print(f"  {t}")

# Encapsulation prevents:
# alice.__balance = 1000000        # AttributeError
# alice.__log_transaction(...)     # AttributeError
print(f"\nCan access __balance? {hasattr(alice, '__balance')}")
print(f"Can access _BankAccount__balance? "
      f"{hasattr(alice, '_BankAccount__balance')}")
```

Output:
```
Account[XXXX5678] Alice: $1000.00
Balance: $1000.0
Deposited $500.00. New balance: $1500.00
Withdrew $200.00. New balance: $1300.00
Withdrew $300.00. New balance: $1000.00
Deposited $300.00. New balance: $800.00
Transferred $300.00 to Bob

Account[XXXX5678] Alice: $1000.00
Account[XXXX8765] Bob: $800.00

Recent transactions:
  [2026-10-26 10:00:00] DEPOSIT: $500.00 (bal: $1500.00)
  [2026-10-26 10:00:00] WITHDRAW: $200.00 (bal: $1300.00)
  [2026-10-26 10:00:00] WITHDRAW: $300.00 (bal: $1000.00)

Can access __balance? False
Can access _BankAccount__balance? True
```

## Property Patterns

### Pattern 1: Validation on Set

```python
class Person:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.name = name    # Uses setter
        self.age = age      # Uses setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Age must be a number.")
        if value < 0 or value > 150:
            raise ValueError(f"Age {value} out of range (0-150).")
        self._age = value

    def __str__(self):
        return f"{self.name} ({self.age})"

p = Person("Alice", 25)
print(p)

try:
    p.age = 200
except ValueError as e:
    print(f"Error: {e}")

try:
    p.name = ""
except ValueError as e:
    print(f"Error: {e}")
```

### Pattern 2: Computed Properties

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

    @property
    def is_square(self):
        return self._width == self._height

r = Rectangle(10, 5)
print(f"Area: {r.area}, Perimeter: {r.perimeter}")
print(f"Is square? {r.is_square}")

r.width = 5
print(f"Now is square? {r.is_square}")
```

### Pattern 3: Lazy (Cached) Properties

```python
class DataProcessor:
    def __init__(self, data):
        self._data = data
        self._cached_result = None

    @property
    def data(self):
        """Read-only access to data."""
        return self._data

    @property
    def processed(self):
        """Lazy computed property -- cached after first access."""
        if self._cached_result is None:
            print("Computing processed result...")
            self._cached_result = (
                sum(self._data),
                sum(self._data) / len(self._data),
                max(self._data),
                min(self._data)
            )
        return self._cached_result

dp = DataProcessor([10, 20, 30, 40, 50])

# First access -- computation happens
total, avg, mx, mn = dp.processed
print(f"Total: {total}, Avg: {avg}, Max: {mx}, Min: {mn}")

# Second access -- cached
total, avg, mx, mn = dp.processed
print("(Used cached result)")
```

### Pattern 4: Property with Backward Compatibility

```python
class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        """Full name (computed from first + last)."""
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, value):
        """Allow setting full name (parses into first/last)."""
        parts = value.split(" ", 1)
        self._first_name = parts[0]
        self._last_name = parts[1] if len(parts) > 1 else ""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

u = User("John", "Doe")
print(u.full_name)

u.full_name = "Jane Smith"
print(f"First: {u.first_name}, Last: {u.last_name}")
```

## Encapsulation vs Performance

Properties add a method call overhead. For simple attribute access without logic, direct public attributes are fine.

```python
import time

class WithProperty:
    def __init__(self):
        self._value = 42

    @property
    def value(self):
        return self._value

class WithDirectAccess:
    def __init__(self):
        self.value = 42

# Time comparison
wp = WithProperty()
da = WithDirectAccess()

start = time.perf_counter()
for _ in range(10_000_000):
    _ = wp.value
property_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(10_000_000):
    _ = da.value
direct_time = time.perf_counter() - start

print(f"Property: {property_time:.3f}s")
print(f"Direct: {direct_time:.3f}s")
print(f"Overhead: {((property_time/direct_time)-1)*100:.1f}%")
```

## Best Practices

1. **Start with public attributes, add properties later when needed**
2. **Use `@property` for computed or validated attributes**
3. **Use `__` (double underscore) only to avoid name clashes in inheritance**
4. **Use `_` (single underscore) for internal implementation details**
5. **Never access `__name` from outside (even though Python allows it)**

## Practice Problems

1. **Student Grade with Encapsulation** -- Create a `StudentGrade` class with private `_name`, `_grades` (list). Provide public methods: `add_grade(score)`, `average` (property), `letter_grade` (property), `name` (property with validation).
   <details>
   <summary>Show Answer</summary>

   ```python
   class StudentGrade:
       def __init__(self, name):
           self._name = None
           self._grades = []
           self.name = name

       @property
       def name(self):
           return self._name

       @name.setter
       def name(self, value):
           if not value or not value.strip():
               raise ValueError("Name cannot be empty.")
           self._name = value.strip()

       def add_grade(self, score):
           if not isinstance(score, (int, float)):
               raise TypeError("Score must be numeric.")
           if score < 0 or score > 100:
               raise ValueError("Score must be 0-100.")
           self._grades.append(score)

       @property
       def average(self):
           if not self._grades:
               return 0
           return sum(self._grades) / len(self._grades)

       @property
       def letter_grade(self):
           avg = self.average
           if avg >= 90: return "A"
           if avg >= 80: return "B"
           if avg >= 70: return "C"
           if avg >= 60: return "D"
           return "F"

   s = StudentGrade("Alice")
   s.add_grade(85)
   s.add_grade(90)
   s.add_grade(78)
   print(f"{s.name}: avg={s.average:.1f}, grade={s.letter_grade}")
   ```
   </details>

2. **Secure Password Container** -- Create a `PasswordVault` class that stores passwords in a private `__passwords` dict. Public methods: `set_password(service, pwd)`, `get_password(service)` (returns masked: "****"), `validate_password(service, pwd)` (returns bool). Never expose the actual password.
   <details>
   <summary>Show Answer</summary>

   ```python
   class PasswordVault:
       def __init__(self):
           self.__passwords = {}

       def set_password(self, service, password):
           if len(password) < 4:
               raise ValueError("Password too short.")
           self.__passwords[service] = password
           print(f"Password set for '{service}'.")

       def get_password(self, service):
           if service not in self.__passwords:
               return None
           pwd = self.__passwords[service]
           return pwd[:2] + "*" * (len(pwd) - 4) + pwd[-2:]

       def validate_password(self, service, password):
           stored = self.__passwords.get(service)
           if stored is None:
               return False
           return stored == password

   vault = PasswordVault()
   vault.set_password("email", "MySecureP@ss1")
   print(f"Masked: {vault.get_password('email')}")
   print(f"Valid? {vault.validate_password('email', 'MySecureP@ss1')}")
   print(f"Valid? {vault.validate_password('email', 'wrong')}")
   ```
   </details>

3. **Inventory System** -- Create an `InventoryItem` class with private `_name`, `_quantity`, `_price`. Properties: `name` (read-only), `quantity` (validated non-negative), `price` (validated positive). Method: `total_value` (computed property). Prevent direct modification of internal data.
   <details>
   <summary>Show Answer</summary>

   ```python
   class InventoryItem:
       def __init__(self, name, quantity, price):
           self._name = None
           self._quantity = 0
           self._price = 0.0
           self._name = name
           self.quantity = quantity
           self.price = price

       @property
       def name(self):
           return self._name

       @property
       def quantity(self):
           return self._quantity

       @quantity.setter
       def quantity(self, value):
           if not isinstance(value, int) or value < 0:
               raise ValueError("Quantity must be non-negative integer.")
           self._quantity = value

       @property
       def price(self):
           return self._price

       @price.setter
       def price(self, value):
           if not isinstance(value, (int, float)) or value <= 0:
               raise ValueError("Price must be positive.")
           self._price = float(value)

       @property
       def total_value(self):
           return self._quantity * self._price

       def __str__(self):
           return f"{self._name}: qty={self._quantity}, price=${self._price:.2f}"

   item = InventoryItem("Laptop", 10, 999.99)
   print(f"{item.name}: {item.total_value}")
   item.quantity = 5
   print(f"Updated: {item.total_value}")
   ```
   </details>

4. **Timer with Encapsulation** -- Create a `Timer` class with private `_start_time`, `_elapsed`. Public methods: `start()`, `stop()`, `reset()`. Property: `elapsed` (returns formatted string "HH:MM:SS"). Prevent direct access to timestamps.
   <details>
   <summary>Show Answer</summary>

   ```python
   import time

   class Timer:
       def __init__(self):
           self._start_time = None
           self._elapsed = 0.0
           self._running = False

       def start(self):
           if self._running:
               raise RuntimeError("Timer already running.")
           self._start_time = time.perf_counter()
           self._running = True
           print("Timer started.")

       def stop(self):
           if not self._running:
               raise RuntimeError("Timer not running.")
           self._elapsed += time.perf_counter() - self._start_time
           self._running = False
           print(f"Timer stopped. Elapsed: {self.elapsed}")

       def reset(self):
           self._elapsed = 0.0
           self._running = False
           self._start_time = None
           print("Timer reset.")

       @property
       def elapsed(self):
           total = self._elapsed
           if self._running:
               total += time.perf_counter() - self._start_time
           hours = int(total // 3600)
           minutes = int((total % 3600) // 60)
           seconds = int(total % 60)
           ms = int((total * 100) % 100)
           return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:02d}"

   t = Timer()
   t.start()
   time.sleep(0.1)
   t.stop()
   print(f"Final: {t.elapsed}")
   ```
   </details>

5. **BankAccount with Daily Limit** -- Extend BankAccount with a daily withdrawal limit. Private attributes: `__daily_limit`, `__withdrawn_today`. Property: `daily_limit` (read/write, validated). Override `withdraw` to check daily limit. Add `reset_daily_limit()`.
   <details>
   <summary>Show Answer</summary>

   ```python
   import datetime

   class BankAccount:
       def __init__(self, owner, balance=0, daily_limit=500):
           self.owner = owner
           self.__balance = balance
           self.__daily_limit = daily_limit
           self.__withdrawn_today = 0
           self.__last_date = datetime.date.today()

       @property
       def balance(self):
           return self.__balance

       @property
       def daily_limit(self):
           self.__check_date()
           return self.__daily_limit

       @daily_limit.setter
       def daily_limit(self, value):
           if value < 0:
               raise ValueError("Daily limit cannot be negative.")
           self.__daily_limit = value

       def __check_date(self):
           today = datetime.date.today()
           if self.__last_date != today:
               self.__withdrawn_today = 0
               self.__last_date = today

       def deposit(self, amount):
           if amount <= 0:
               raise ValueError("Amount must be positive.")
           self.__balance += amount
           print(f"Deposited ${amount}. Balance: ${self.__balance}")

       def withdraw(self, amount):
           if amount <= 0:
               raise ValueError("Amount must be positive.")
           if amount > self.__balance:
               raise ValueError("Insufficient funds.")
           self.__check_date()
           remaining = self.__daily_limit - self.__withdrawn_today
           if amount > remaining:
               raise ValueError(f"Daily limit ${self.__daily_limit}, "
                                f"${remaining} remaining today.")
           self.__balance -= amount
           self.__withdrawn_today += amount
           print(f"Withdrew ${amount}. Balance: ${self.__balance}")
           return True

       def reset_daily(self):
           self.__withdrawn_today = 0
           print("Daily counter reset.")

   acc = BankAccount("Alice", 1000, 300)
   acc.withdraw(200)
   acc.withdraw(100)
   try:
       acc.withdraw(50)
   except ValueError as e:
       print(f"Error: {e}")
   ```
   </details>
