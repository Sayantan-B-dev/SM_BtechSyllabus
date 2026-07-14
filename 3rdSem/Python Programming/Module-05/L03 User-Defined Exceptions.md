# User-Defined Exceptions

**Course:** Python Programming  
**Module:** 5 | **Lecture:** 3  
**Date:** 07-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 561-840

## Why Create Custom Exceptions?

Python's built-in exceptions cover many common error scenarios, but real-world applications often have domain-specific error conditions. Custom exceptions make code more readable, maintainable, and self-documenting.

### Benefits of Custom Exceptions
- Clearer error messages specific to your application domain
- Better error categorization (e.g., `InsufficientFundsError` vs generic `ValueError`)
- Ability to add custom attributes and methods to exception objects
- Precise exception handling in client code

## Creating a Custom Exception Class

To create a custom exception, define a new class that inherits from `Exception` (or any of its subclasses).

### Basic Custom Exception

```python
class CustomError(Exception):
    """Base class for custom exceptions in this application."""
    pass

# Usage
try:
    raise CustomError("Something went wrong in our application.")
except CustomError as e:
    print(f"Caught custom error: {e}")
```

Output:
```
Caught custom error: Something went wrong in our application.
```

### Inheritance Chain

```
BaseException
    +-- Exception
        +-- CustomError (our custom exception)
            +-- MoreSpecificError (more specific)
```

## Example 1: InsufficientFundsError (Banking Application)

This is a practical custom exception for a banking system:

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        message = f"Insufficient funds: balance=${balance:.2f}, "
        message += f"withdrawal=${amount:.2f}, deficit=${self.deficit:.2f}"
        super().__init__(message)


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account[{self.owner}]: ${self.balance:.2f}"


# Test the custom exception
account = BankAccount("Alice", 500)

try:
    account.withdraw(700)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"  Balance: ${e.balance}")
    print(f"  Attempted: ${e.amount}")
    print(f"  Deficit: ${e.deficit}")

print()
# Successful transactions still work
try:
    account.deposit(200)
    account.withdraw(300)
    print(account)
except (ValueError, InsufficientFundsError) as e:
    print(f"Error: {e}")
```

Output:
```
Transaction failed: Insufficient funds: balance=$500.00, withdrawal=$700.00, deficit=$200.00
  Balance: $500.0
  Attempted: $700.0
  Deficit: $200.0

Deposited $200.00. New balance: $700.00
Withdrew $300.00. New balance: $400.00
Account[Alice]: $400.00
```

## Example 2: AgeValidationError

```python
class AgeValidationError(Exception):
    """Raised when an age value fails validation rules."""

    def __init__(self, age, reason=""):
        self.age = age
        self.reason = reason
        message = f"Invalid age '{age}'. {reason}".strip()
        super().__init__(message)


class NegativeAgeError(AgeValidationError):
    """Raised when age is negative."""

    def __init__(self, age):
        super().__init__(age, "Age cannot be negative.")


class AgeTooOldError(AgeValidationError):
    """Raised when age exceeds maximum allowed."""

    def __init__(self, age, max_age=150):
        self.max_age = max_age
        super().__init__(age, f"Age cannot exceed {max_age}.")


class AgeTooYoungError(AgeValidationError):
    """Raised when age is below minimum."""

    def __init__(self, age, min_age=0):
        self.min_age = min_age
        super().__init__(age, f"Age must be at least {min_age}.")


def validate_age(age, min_age=0, max_age=150):
    if not isinstance(age, (int, float)):
        raise AgeValidationError(age, "Age must be a number.")
    if age < 0:
        raise NegativeAgeError(age)
    if age < min_age:
        raise AgeTooYoungError(age, min_age)
    if age > max_age:
        raise AgeTooOldError(age, max_age)
    return True


def register_user(name, age):
    try:
        validate_age(age, min_age=18, max_age=120)
        print(f"User '{name}' registered successfully (age: {age}).")
    except NegativeAgeError:
        print(f"Cannot register '{name}': Age cannot be negative.")
    except AgeTooYoungError as e:
        print(f"Cannot register '{name}': Must be at least {e.min_age}. "
              f"User is {e.age}.")
    except AgeTooOldError as e:
        print(f"Cannot register '{name}': Maximum age is {e.max_age}. "
              f"User is {e.age}.")
    except AgeValidationError as e:
        print(f"Cannot register '{name}': {e}")


# Test cases
register_user("Alice", 25)
register_user("Bob", -5)
register_user("Charlie", 16)
register_user("David", 200)
register_user("Eve", "twenty")
```

Output:
```
User 'Alice' registered successfully (age: 25).
Cannot register 'Bob': Age cannot be negative.
Cannot register 'Charlie': Must be at least 18. User is 16.
Cannot register 'David': Maximum age is 120. User is 200.
Cannot register 'Eve': Invalid age 'twenty'. Age must be a number.
```

## The raise Statement

Use `raise` to explicitly trigger an exception.

### Basic raise Syntax

```python
# Raise with a message
raise ValueError("This is an error message.")

# Raise an existing exception class
error = ValueError("Custom message")
raise error

# Re-raise the current exception (in an except block)
try:
    risky_operation()
except ValueError:
    print("Logging the error...")
    raise  # Re-raises the same exception
```

### Example: raise in Validation

```python
def set_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain an uppercase letter.")
    print("Password set successfully.")

# Test
try:
    set_password("abc")
except ValueError as e:
    print(f"Password rejected: {e}")

try:
    set_password("StrongPass1")
except ValueError as e:
    print(f"Password rejected: {e}")
else:
    print("Password accepted!")
```

Output:
```
Password rejected: Password must be at least 8 characters.
Password set successfully.
Password accepted!
```

## Re-raising Exceptions

Sometimes you want to log an error but let it propagate to a higher-level handler:

```python
def process_data(data):
    try:
        result = data["value"] / data["divisor"]
        return result
    except KeyError as e:
        print(f"[LOG] Missing key: {e}")
        raise  # Re-raise the same exception
    except ZeroDivisionError as e:
        print(f"[LOG] Division by zero with data: {data}")
        raise  # Re-raise the same exception


# Higher-level handler
def main():
    test_cases = [
        {"value": 10, "divisor": 2},
        {"value": 10, "divisor": 0},
        {"value": 10},  # missing 'divisor'
    ]
    for data in test_cases:
        try:
            result = process_data(data)
            print(f"Result: {result}")
        except (KeyError, ZeroDivisionError) as e:
            print(f"[MAIN] Unhandled error: {e}\n")
```

Output:
```
Result: 5.0
[LOG] Division by zero with data: {'value': 10, 'divisor': 0}
[MAIN] Unhandled error: division by zero

[LOG] Missing key: 'divisor'
[MAIN] Unhandled error: 'divisor'
```

## Exception Chaining with raise...from

Use `raise ... from` to chain exceptions, preserving the original cause.

```python
class DatabaseError(Exception):
    """Custom exception for database operations."""
    pass


def connect_to_database():
    # Simulate an OSError
    raise OSError("Port 5432 is already in use.")


def initialize_app():
    try:
        connect_to_database()
    except OSError as e:
        # Chain the original error with our custom exception
        raise DatabaseError("Failed to initialize database connection.") from e


try:
    initialize_app()
except DatabaseError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")
```

Output:
```
Error: Failed to initialize database connection.
Caused by: Port 5432 is already in use.
```

### Without Chaining

```python
try:
    initialize_app()
except OSError as e:
    raise DatabaseError("Failed to initialize.")  # Original error is lost
```

### With Chaining vs Without

```python
# Without chaining -- original traceback is lost
try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("Something went wrong.")
except ValueError as e:
    print(f"Error: {e}")
    print(f"__cause__: {e.__cause__}")  # None
    print(f"__context__: {e.__context__}")  # Set automatically, but not chained

print()

# With chaining -- preserves the original
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Something went wrong.") from e
except ValueError as e:
    print(f"Error: {e}")
    print(f"__cause__: {e.__cause__}")
```

Output:
```
Error: Something went wrong.
__cause__: None
__context__: division by zero

Error: Something went wrong.
__cause__: division by zero
```

## Suppressing Exception Context

Use `raise ... from None` to suppress the automatic exception context:

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.") from None
        # The ZeroDivisionError is completely hidden

try:
    safe_divide(10, 0)
except ValueError as e:
    print(f"Clean error: {e}")
    print(f"__cause__: {e.__cause__}")
```

Output:
```
Clean error: Cannot divide by zero.
__cause__: None
```

## Best Practices for Custom Exceptions

### 1. Inherit from Exception, Not BaseException

```python
# CORRECT
class MyError(Exception):
    pass

# INCORRECT -- don't inherit from BaseException
class MyError(BaseException):
    pass
```

### 2. Keep the Exception Hierarchy Shallow

```python
# GOOD: flat hierarchy
class PaymentError(Exception): pass
class InsufficientFundsError(PaymentError): pass
class CardDeclinedError(PaymentError): pass
class NetworkError(PaymentError): pass

# AVOID: overly deep hierarchy
class Error(Exception): pass
class PaymentError(Error): pass
class CardError(PaymentError): pass
class CreditCardError(CardError): pass
class VisaError(CreditCardError): pass  # Too specific
```

### 3. Add Useful Context as Attributes

```python
class ProductNotFoundError(Exception):
    def __init__(self, product_id, inventory):
        self.product_id = product_id
        self.inventory = inventory
        message = f"Product ID '{product_id}' not found. "
        message += f"Available IDs: {list(inventory.keys())}"
        super().__init__(message)

inventory = {"A001": "Laptop", "B002": "Mouse", "C003": "Keyboard"}

def find_product(pid):
    if pid not in inventory:
        raise ProductNotFoundError(pid, inventory)
    return inventory[pid]

try:
    print(find_product("X999"))
except ProductNotFoundError as e:
    print(f"Error: {e}")
    print(f"Requested ID: {e.product_id}")
```

### 4. Document Custom Exceptions

```python
class ConfigurationError(Exception):
    """Raised when application configuration is invalid.

    Attributes:
        config_key -- the key that caused the error
        expected -- the expected type/format
        received -- the actual value received
    """

    def __init__(self, config_key, expected, received):
        self.config_key = config_key
        self.expected = expected
        self.received = received
        super().__init__(
            f"Invalid config '{config_key}': "
            f"expected {expected}, got {received!r}"
        )
```

### 5. Create a Base Exception for Each Module

```python
# module: payment.py

class PaymentError(Exception):
    """Base exception for payment-related errors."""
    pass

class InsufficientFundsError(PaymentError):
    """Raised when account balance is too low."""
    pass

class CardExpiredError(PaymentError):
    """Raised when credit card has expired."""
    pass

class FraudDetectedError(PaymentError):
    """Raised when transaction is flagged as suspicious."""
    pass


# Client code can catch all payment errors with one except
def process_payment(amount):
    try:
        charge_card(amount)
    except PaymentError as e:
        print(f"Payment failed: {e}")
        return False
    else:
        print("Payment successful!")
        return True
```

## Complete Example: Custom Exception Class Hierarchy

```python
class EmployeeError(Exception):
    """Base exception for employee management."""
    pass

class EmployeeNotFoundError(EmployeeError):
    def __init__(self, emp_id):
        self.emp_id = emp_id
        super().__init__(f"Employee with ID '{emp_id}' not found.")

class DuplicateEmployeeError(EmployeeError):
    def __init__(self, emp_id):
        self.emp_id = emp_id
        super().__init__(f"Employee with ID '{emp_id}' already exists.")

class InvalidSalaryError(EmployeeError):
    def __init__(self, salary, reason=""):
        self.salary = salary
        super().__init__(f"Invalid salary ${salary}: {reason}")


class EmployeeManager:
    def __init__(self):
        self._employees = {}

    def add_employee(self, emp_id, name, salary):
        if emp_id in self._employees:
            raise DuplicateEmployeeError(emp_id)
        if salary < 0:
            raise InvalidSalaryError(salary, "Salary cannot be negative.")
        if salary > 1_000_000:
            raise InvalidSalaryError(salary, "Salary exceeds maximum.")
        self._employees[emp_id] = {"name": name, "salary": salary}
        print(f"Added: {name} (ID: {emp_id})")

    def get_employee(self, emp_id):
        if emp_id not in self._employees:
            raise EmployeeNotFoundError(emp_id)
        return self._employees[emp_id]

    def update_salary(self, emp_id, new_salary):
        if emp_id not in self._employees:
            raise EmployeeNotFoundError(emp_id)
        if new_salary < 0:
            raise InvalidSalaryError(new_salary, "Salary cannot be negative.")
        self._employees[emp_id]["salary"] = new_salary
        print(f"Updated salary for {emp_id} to ${new_salary}")


# Test the hierarchy
manager = EmployeeManager()

tests = [
    ("add", "E001", "Alice", 50000),
    ("add", "E002", "Bob", -100),         # InvalidSalaryError
    ("add", "E001", "Charlie", 60000),    # DuplicateEmployeeError
    ("get", "E999"),                      # EmployeeNotFoundError
    ("salary", "E001", 2_000_000),        # InvalidSalaryError
]

for test in tests:
    try:
        if test[0] == "add":
            manager.add_employee(*test[1:])
        elif test[0] == "get":
            emp = manager.get_employee(test[1])
            print(f"Found: {emp}")
        elif test[0] == "salary":
            manager.update_salary(*test[1:])
    except EmployeeNotFoundError as e:
        print(f"Lookup Error: {e}")
    except DuplicateEmployeeError as e:
        print(f"Duplicate Error: {e}")
    except InvalidSalaryError as e:
        print(f"Salary Error: {e}")
    except EmployeeError as e:
        print(f"General Employee Error: {e}")
```

Output:
```
Added: Alice (ID: E001)
Salary Error: Invalid salary $-100: Salary cannot be negative.
Duplicate Error: Employee with ID 'E001' already exists.
Lookup Error: Employee with ID 'E999' not found.
Salary Error: Invalid salary $2000000: Salary exceeds maximum.
```

## Practice Problems

1. **Withdrawal System** -- Create a custom exception `OverdraftError` with attributes `balance`, `withdrawal_amount`, and `overdraft_limit`. Create a `BankAccount` class with a configurable overdraft limit. Raise `OverdraftError` when withdrawal exceeds balance + overdraft limit.
   <details>
   <summary>Show Answer</summary>

   ```python
   class OverdraftError(Exception):
       def __init__(self, balance, withdrawal_amount, overdraft_limit):
           self.balance = balance
           self.withdrawal_amount = withdrawal_amount
           self.overdraft_limit = overdraft_limit
           available = balance + overdraft_limit
           deficit = withdrawal_amount - available
           super().__init__(
               f"Overdraft limit exceeded: balance={balance}, "
               f"overdraft_limit={overdraft_limit}, "
               f"available={available}, deficit={deficit}"
           )

   class BankAccount:
       def __init__(self, owner, balance=0, overdraft_limit=100):
           self.owner = owner
           self.balance = balance
           self.overdraft_limit = overdraft_limit

       def withdraw(self, amount):
           available = self.balance + self.overdraft_limit
           if amount > available:
               raise OverdraftError(self.balance, amount, self.overdraft_limit)
           self.balance -= amount
           print(f"Withdrew {amount}. Balance: {self.balance}")

   acc = BankAccount("Alice", 500, 200)
   try:
       acc.withdraw(800)
   except OverdraftError as e:
       print(f"Overdraft denied: {e}")
   ```
   </details>

2. **Grade Validator** -- Create a hierarchy of exceptions: `GradeError` (base), `InvalidGradeValueError` (grade not between 0-100), `InvalidGradeTypeError` (not a number). Write a function `process_grade(value)` that validates and returns a letter grade (A, B, C, D, F).
   <details>
   <summary>Show Answer</summary>

   ```python
   class GradeError(Exception): pass
   class InvalidGradeValueError(GradeError): pass
   class InvalidGradeTypeError(GradeError): pass

   def letter_grade(score):
       if not isinstance(score, (int, float)):
           raise InvalidGradeTypeError(f"Grade must be numeric, got {type(score)}")
       if score < 0 or score > 100:
           raise InvalidGradeValueError(f"Grade {score} not in range 0-100")
       if score >= 90: return "A"
       if score >= 80: return "B"
       if score >= 70: return "C"
       if score >= 60: return "D"
       return "F"

   def process_grade(value):
       try:
           grade = letter_grade(value)
           print(f"Score {value} -> Grade {grade}")
       except GradeError as e:
           print(f"Error: {e}")

   process_grade(85)
   process_grade(105)
   process_grade("hello")
   ```
   </details>

3. **Shopping Cart** -- Create custom exceptions for an e-commerce cart: `CartError` (base), `ItemNotFoundError`, `OutOfStockError` (with `available` attribute), `CartFullError`. Implement a `ShoppingCart` class with `add_item`, `remove_item`, and `checkout` methods.
   <details>
   <summary>Show Answer</summary>

   ```python
   class CartError(Exception): pass
   class ItemNotFoundError(CartError): pass
   class OutOfStockError(CartError):
       def __init__(self, item, available):
           self.available = available
           super().__init__(f"'{item}' out of stock. Available: {available}")
   class CartFullError(CartError): pass

   class ShoppingCart:
       def __init__(self, max_items=5):
           self.items = {}
           self.max_items = max_items

       def add_item(self, name, quantity=1, stock=10):
           if len(self.items) >= self.max_items:
               raise CartFullError(f"Cart full (max {self.max_items} items)")
           if stock < quantity:
               raise OutOfStockError(name, stock)
           self.items[name] = self.items.get(name, 0) + quantity
           print(f"Added {quantity}x {name}. Cart: {self.items}")

       def remove_item(self, name):
           if name not in self.items:
               raise ItemNotFoundError(f"'{name}' not in cart")
           del self.items[name]
           print(f"Removed {name}. Cart: {self.items}")

   cart = ShoppingCart()
   cart.add_item("Laptop", 1, 5)
   cart.add_item("Mouse", 2, 3)
   cart.remove_item("Mouse")
   try:
       cart.remove_item("Keyboard")
   except ItemNotFoundError as e:
       print(f"Error: {e}")
   ```
   </details>

4. **Configuration Parser** -- Write a config parser that raises custom exceptions: `ConfigError` (base), `ConfigKeyError` (missing key), `ConfigTypeError` (wrong type), `ConfigValueError` (invalid value). Parse a dictionary config and validate it.
   <details>
   <summary>Show Answer</summary>

   ```python
   class ConfigError(Exception): pass
   class ConfigKeyError(ConfigError): pass
   class ConfigTypeError(ConfigError): pass
   class ConfigValueError(ConfigError): pass

   expected_schema = {
       "host": str,
       "port": int,
       "debug": bool,
       "max_connections": int,
   }

   def validate_config(config):
       for key, expected_type in expected_schema.items():
           if key not in config:
               raise ConfigKeyError(f"Missing required key: '{key}'")
           if not isinstance(config[key], expected_type):
               raise ConfigTypeError(
                   f"'{key}' should be {expected_type.__name__}, "
                   f"got {type(config[key]).__name__}"
               )
       port = config["port"]
       if port < 1 or port > 65535:
           raise ConfigValueError(f"Port {port} out of range (1-65535)")
       if config.get("max_connections", 0) < 1:
           raise ConfigValueError("max_connections must be >= 1")
       print("Config is valid!")

   validate_config({"host": "localhost", "port": 8080, "debug": True, "max_connections": 10})
   try:
       validate_config({"host": "localhost", "port": 99999, "debug": True, "max_connections": 10})
   except ConfigValueError as e:
       print(f"Config error: {e}")
   ```
   </details>

5. **File Validation System** -- Create exceptions: `FileValidationError` (base), `FileSizeExceededError` (with `max_size`), `InvalidExtensionError` (with `allowed`), `FileEmptyError`. Write a function `validate_file(filename, max_mb=10, allowed_extensions=None)` that validates a file before processing.
   <details>
   <summary>Show Answer</summary>

   ```python
   import os

   class FileValidationError(Exception): pass
   class FileSizeExceededError(FileValidationError):
       def __init__(self, filename, size_mb, max_size):
           super().__init__(f"{filename} is {size_mb:.1f}MB (max {max_size}MB)")
   class InvalidExtensionError(FileValidationError):
       def __init__(self, filename, allowed):
           super().__init__(f"{filename}: allowed extensions: {allowed}")
   class FileEmptyError(FileValidationError): pass

   def validate_file(filename, max_mb=10, allowed_extensions=None):
       if allowed_extensions is None:
           allowed_extensions = [".txt", ".csv", ".json"]
       ext = os.path.splitext(filename)[1].lower()
       if ext not in allowed_extensions:
           raise InvalidExtensionError(filename, allowed_extensions)
       if not os.path.exists(filename):
           raise FileValidationError(f"{filename} does not exist")
       size_mb = os.path.getsize(filename) / (1024 * 1024)
       if size_mb > max_mb:
           raise FileSizeExceededError(filename, size_mb, max_mb)
       if os.path.getsize(filename) == 0:
           raise FileEmptyError(f"{filename} is empty")
       print(f"{filename}: valid ({size_mb:.2f}MB)")

   open("test.txt", "w").write("hello")
   validate_file("test.txt")
   validate_file("test.txt", max_mb=0.001)
   ```
   </details>
