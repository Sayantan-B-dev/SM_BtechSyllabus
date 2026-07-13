# Basics of OOP Concepts in Python

**Course:** Python Programming Lab  
**Module:** 5 | **Lecture:** 6  
**Date:** 30-Oct-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 5  
**Learning Methodology:** Simulation  
**Reference:** Lab Manual

## Lab Objectives

- Implement inheritance to create parent-child class relationships.
- Override methods from the parent class in child classes.
- Build an Animal-Dog-Cat hierarchy and an Employee-Manager inheritance structure.

## Theory

Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). The child class can add new attributes and methods or override existing ones. The syntax is: `class ChildClass(ParentClass):`. This promotes code reuse and establishes an "is-a" relationship (e.g., Dog is an Animal).

Method overriding occurs when a child class defines a method with the same name as in the parent class. The child's version takes precedence. The super() function calls a method from the parent class: `super().__init__(args)` is commonly used in the child's constructor to initialize parent attributes.

Inheritance hierarchies can be multi-level (Animal -> Mammal -> Dog) or multiple (one class inherits from multiple parents). Python supports both. Method Resolution Order (MRO) determines which method is called when there are multiple inheritance paths. The isinstance() function checks if an object is an instance of a class (including subclasses).

## Procedure

1. Create a new Python file named lab30.py.
2. Define an Animal parent class with __init__(name, age) and methods: speak(), describe().
3. Define Dog and Cat subclasses that override the speak() method.
4. Add a unique method to Dog (fetch()) and Cat (purr()).
5. Define an Employee parent class with attributes name, emp_id, salary.
6. Define a Manager subclass that adds department and team_size.
7. Override the __str__() method in both Employee and Manager.
8. Create objects of all classes and test inheritance and polymorphism.

## Source Code

```python
# Module 05 Lab 06: Inheritance and Method Overriding
# Animal-Dog-Cat hierarchy and Employee-Manager inheritance

# --- Animal Hierarchy ---
class Animal:
    """Base class for animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        """Generic animal sound."""
        return "Some generic animal sound"

    def describe(self):
        """Describe the animal."""
        return f"{self.name} is {self.age} years old."

    def __str__(self):
        return f"Animal({self.name}, {self.age})"


class Dog(Animal):
    """Dog class inherits from Animal."""

    def __init__(self, name, age, breed):
        # Call parent constructor
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        """Override: Dog barks."""
        return "Woof! Woof!"

    def fetch(self):
        """Unique Dog method."""
        return f"{self.name} is fetching the ball!"

    def __str__(self):
        return f"Dog({self.name}, {self.age}, {self.breed})"


class Cat(Animal):
    """Cat class inherits from Animal."""

    def speak(self):
        """Override: Cat meows."""
        return "Meow! Meow!"

    def purr(self):
        """Unique Cat method."""
        return f"{self.name} is purring happily."


print("--- Animal Inheritance Demo ---")
animals = [
    Animal("Generic", 5),
    Dog("Buddy", 3, "Golden Retriever"),
    Cat("Whiskers", 2)
]

for animal in animals:
    print(f"\n{animal}")
    print(f"  Describe: {animal.describe()}")
    print(f"  Speak: {animal.speak()}")
    # Call subclass-specific methods using isinstance
    if isinstance(animal, Dog):
        print(f"  Fetch: {animal.fetch()}")
    elif isinstance(animal, Cat):
        print(f"  Purr: {animal.purr()}")

# --- Employee-Manager Hierarchy ---
print("\n\n--- Employee Inheritance Demo ---")

class Employee:
    """Base class for employees."""

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def work(self):
        return f"{self.name} is working on assigned tasks."

    def get_annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"Employee(ID: {self.emp_id}, Name: {self.name}, Salary: ${self.salary:.2f})"


class Manager(Employee):
    """Manager class inherits from Employee."""

    def __init__(self, name, emp_id, salary, department, team_size):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.team_size = team_size

    def work(self):
        """Override: Manager's work is different."""
        return f"{self.name} is managing the {self.department} department."

    def conduct_meeting(self):
        return f"{self.name} is conducting a team meeting."

    def __str__(self):
        return (f"Manager(ID: {self.emp_id}, Name: {self.name}, "
                f"Dept: {self.department}, Salary: ${self.salary:.2f}, "
                f"Team: {self.team_size})")


# Create employees and managers
emp1 = Employee("Alice", "E001", 5000)
emp2 = Employee("Bob", "E002", 4500)
mgr1 = Manager("Charlie", "M001", 8000, "Engineering", 8)
mgr2 = Manager("Diana", "M002", 9000, "Data Science", 5)

# Polymorphism: calling work() on different types
print("\n--- Polymorphism in Action ---")
people = [emp1, emp2, mgr1, mgr2]
for person in people:
    print(f"\n{person}")
    print(f"  Work: {person.work()}")
    if isinstance(person, Manager):
        print(f"  Meeting: {person.conduct_meeting()}")

# Manager-specific features
print(f"\nManager annual salary: ${mgr1.get_annual_salary():.2f}")
```

## Sample Output

```
--- Animal Inheritance Demo ---

Animal(Generic, 5)
  Describe: Generic is 5 years old.
  Speak: Some generic animal sound

Dog(Buddy, 3, Golden Retriever)
  Describe: Buddy is 3 years old.
  Speak: Woof! Woof!
  Fetch: Buddy is fetching the ball!

Cat(Whiskers, 2)
  Describe: Whiskers is 2 years old.
  Speak: Meow! Meow!
  Purr: Whiskers is purring happily.


--- Employee Inheritance Demo ---

--- Polymorphism in Action ---

Employee(ID: E001, Name: Alice, Salary: $5000.00)
  Work: Alice is working on assigned tasks.

Employee(ID: E002, Name: Bob, Salary: $4500.00)
  Work: Bob is working on assigned tasks.

Manager(ID: M001, Name: Charlie, Dept: Engineering, Salary: $8000.00, Team: 8)
  Work: Charlie is managing the Engineering department.
  Meeting: Charlie is conducting a team meeting.

Manager(ID: M002, Name: Diana, Dept: Data Science, Salary: $9000.00, Team: 5)
  Work: Diana is managing the Data Science department.
  Meeting: Diana is conducting a team meeting.

Manager annual salary: $96000.00
```

## Homework

1. Create a Shape base class with an area() method that returns 0. Create Circle and Rectangle subclasses that override area().
2. Create a Vehicle class with attributes make, model, year, and a method info(). Create Car and Motorcycle subclasses that add more specific attributes and override info().
3. Create an InternationalStudent class that inherits from the Student class (from Lab 29) and adds attributes: country, visa_status. Override display_info() to show the additional details.
