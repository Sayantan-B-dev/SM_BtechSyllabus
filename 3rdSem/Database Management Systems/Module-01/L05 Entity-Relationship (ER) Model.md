# Entity-Relationship (ER) Model

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 5  
**Date:** 16-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### What is the ER Model?

The **Entity-Relationship (ER) model** is a conceptual data model introduced by Peter Chen in 1976. It provides a high-level, intuitive way to describe the data requirements of an organization. The ER model captures:

- The **entities** (things/objects) of interest.
- The **attributes** (properties) of those entities.
- The **relationships** (associations) between entities.
- The **constraints** (rules) on the data.

The ER model is typically used during the **conceptual design phase** to create an **ER diagram (ERD)** that communicates the database structure to stakeholders. It is independent of any specific DBMS.

### Basic Building Blocks

#### Entity

An **entity** is a distinguishable object or concept in the real world that has independent existence.

**Existence types:**
- **Physical entity:** A tangible object (e.g., a specific car, a person, a building).
- **Abstract entity:** A conceptual object (e.g., a course, a bank account, a department).

**Examples:**
- Student "Alice Johnson" (roll: CS2026001)
- Course "Database Systems" (course_id: CS301)
- Car "Toyota Camry 2024" (VIN: JT2BF22K5M0123456)

#### Entity Set

An **entity set** is a collection (set) of entities that share the same properties (attributes). It corresponds to a **table** in the relational model.

**Notation:** Entity sets are represented as **rectangles** in ER diagrams.

**Example:**
```
+-----------+
|  Student  |
+-----------+
```
The `Student` entity set contains all student entities. Each student has the same attributes (student_id, name, dept_id, etc.).

#### Attributes

An **attribute** is a property that describes an entity. Attributes are represented as **ovals** connected to their entity set.

**Types of Attributes:**

1. **Simple vs Composite**
   - **Simple (atomic):** Cannot be divided further.
     - Example: `age`, `salary`, `gender`.
   - **Composite:** Can be divided into sub-parts.
     - Example: `name` can be divided into `first_name`, `middle_name`, `last_name`.
     - Example: `address` can be divided into `street`, `city`, `state`, `zip`.

   ```
   Composite:        name
                    /  |  \
                 first middle last
   ```

2. **Single-Valued vs Multi-Valued**
   - **Single-valued:** One value per entity.
     - Example: `student_id` (one student has exactly one ID).
   - **Multi-valued:** Multiple values per entity.
     - Example: `phone_numbers` (a student can have multiple phone numbers).
     - Example: `degrees` (an instructor may have multiple degrees).

   **Notation:** Multi-valued attributes are represented as **double-lined ovals**.

3. **Derived Attributes**
   - An attribute whose value can be computed from other attributes.
   - Example: `age` can be derived from `date_of_birth` and the current date.
   - Example: `years_of_service` can be derived from `hire_date`.
   - Example: `gpa` can be derived from grades across all enrolled courses.

   **Notation:** Derived attributes are represented as **dashed ovals**.

4. **Key Attribute**
   - An attribute (or set of attributes) that uniquely identifies an entity within an entity set.
   - Example: `student_id` uniquely identifies a student.
   - Example: `registration_number` uniquely identifies a car.

   **Notation:** Key attributes are represented as **underlined** attribute names.

   ```
              +------+
     (student_id)    (name)    (phone_numbers)
        (underline)            (double oval)

        +-----------+
        |  Student  |
        +-----------+
   ```

#### Composite Key

A **composite key** (or compound key) is a key that consists of two or more attributes that together uniquely identify an entity.

- Example: In the `Enrollment` entity set (representing each individual enrollment record), no single attribute is unique. But `(student_id, course_id, semester)` together form a composite key.

- Example: In a `CityWeather` entity set, `(city_name, country_code, date)` could be the composite key -- no one attribute alone is sufficient.

### Relationships

A **relationship** is an association among two or more entities.

- **Relationship instance:** A specific association (e.g., "Alice Johnson takes CS301").
- **Relationship set:** A collection of relationship instances of the same type.

**Notation:** Relationships are represented as **diamonds** in ER diagrams.

```
  Student -----< Takes >------ Course
```

#### Degree of a Relationship

The **degree** of a relationship is the number of entity sets participating in it.

1. **Unary (Degree 1)** -- A relationship involving a single entity set.
   - Also called a **recursive relationship**.
   - Example: "Employee *manages* Employee" (a manager is also an employee).
   - Example: "Course *prerequisite* Course" (a course has another course as prereq).

   ```
        |manages|
        /       \
   +---------+  /
   | Employee |-/
   +---------+
   ```

2. **Binary (Degree 2)** -- A relationship involving two entity sets.
   - The most common type.
   - Example: "Student *takes* Course".
   - Example: "Customer *buys* Product".

   ```
   +---------+               +--------+
   | Student |------<Takes>--| Course |
   +---------+               +--------+
   ```

3. **Ternary (Degree 3)** -- A relationship involving three entity sets.
   - Example: "Doctor *prescribes* Medicine *to* Patient".
   - Example: "Customer *buys* Product *from* Store".

   ```
         +----------+
         |  Doctor  |
         +----------+
              |
              | prescribes
              |
        +----------+
        | Medicine |---------<Prescribes>---------+
        +----------+                              |
                                                  |
                                           +-----------+
                                           |  Patient  |
                                           +-----------+
   ```

4. **Higher degrees (n-ary):** Relationships involving more than 3 entity sets are possible but rare and complex.

### Cardinality Ratios

Cardinality ratio specifies the maximum number of relationship instances an entity can participate in.

For a binary relationship between entity sets A and B:

| Ratio | Meaning | Example |
|---|---|---|
| **1:1** (One-to-One) | Each entity in A relates to at most one entity in B, and vice versa. | A student has exactly one student ID card. A student ID card belongs to exactly one student. |
| **1:N** (One-to-Many) | Each entity in A can relate to many entities in B. Each entity in B relates to at most one entity in A. | One department has many students. One student belongs to exactly one department. |
| **M:N** (Many-to-Many) | Each entity in A can relate to many entities in B, and vice versa. | Many students can take many courses. Many courses are taken by many students. |

**Diagram notation:**
```
1:1
  +-------+  1---------1  +-------+
  |   A   |---------------|   B   |
  +-------+               +-------+

1:N
  +-------+  1---------N  +-------+
  |   A   |---------------|   B   |
  +-------+               +-------+

M:N
  +-------+  M---------N  +-------+
  |   A   |---------------|   B   |
  +-------+               +-------+
```

### ER Diagram -- Full Example: Student-Course Database

Let us build the ER diagram for a simplified university system:

**Entity Sets:**
- `Student` with attributes: `student_id` (key), `name` (composite: first, last), `phone_numbers` (multi-valued), `date_of_birth`, `age` (derived).
- `Course` with attributes: `course_id` (key), `title`, `credits`.
- `Department` with attributes: `dept_id` (key), `name`, `building`.
- `Instructor` with attributes: `instructor_id` (key), `name`, `phone`.

**Relationships:**
- `Takes` -- between `Student` and `Section` (M:N). Students take sections; sections have many students.
- `Teaches` -- between `Instructor` and `Section` (1:N). One instructor teaches many sections; one section is taught by one instructor.
- `Belongs_To` -- between `Student` and `Department` (N:1). Many students belong to one department.
- `Offers` -- between `Department` and `Course` (1:N). One department offers many courses.
- `Prerequisite` -- unary on `Course` (M:N). A course can have many prerequisites and be a prerequisite for many courses.

**ASCII ER Diagram:**

```
                    +------------------+
                    |   Department     |
                    +------------------+
                    | *dept_id (key)   |
                    |  name            |
                    |  building        |
                    +------------------+
                         |       |
                    1    |       |    1
                         |       |
                     Belongs_To  Offers
                         |N      |
                         |       |N
                    +---------+  |
                    | Student |  |
                    +---------+  |
                    |*student_id| |
                    | first_name| |
                    | last_name | |
                    | phone.....| |
                    | dob       | |
                    | age (der) | |
                    +---------+  |
                         |       |
                    M    |       |
                         |       |
                      Takes      |
                         |N      |
                         |       |
                    +---------+  |
                    | Section |  |
                    +---------+  |
                    |*sec_id   |<-+
                    | semester |
                    | year     |
                    +---------+
                         |
                    1    |
                         |
                      Teaches
                         |
                         |N
                    +-------------+
                    | Instructor  |
                    +-------------+
                    |*instructor_id|
                    | name        |
                    +-------------+

Course entity set (with unary Prerequisite):
                        
                    +---------+
                    | Course  |
                    +---------+
                    |*course_id|
                    | title   |
                    | credits |
                    +---------+
                      |      |
                     M|      |N
                      |      |
                 Prerequisite
```

### ER Diagram -- Extended Notation Summary

| Construct | Chen Notation | Often Described As |
|---|---|---|
| Entity set | Rectangle | `[Student]` |
| Relationship | Diamond | `<Takes>` |
| Attribute | Oval | `(student_id)` |
| Key attribute | Oval with underline | `(student_id)` underlined |
| Multi-valued attr | Double oval | `((phone))` |
| Derived attr | Dashed oval | `--(age)--` |
| Composite attr | Oval with child ovals | `name -> first, last` |
| Weak entity set | Double rectangle | No key attribute of its own |
| Identifying relation | Double diamond | Connects weak to strong |
| Total participation | Double line | All entities must participate |
| Cardinality | 1, N, M labels | On edges near entity |

### Key Concepts Recap

- **Entity** = a real-world object.
- **Entity set** = collection of similar entities (like a table).
- **Attribute** = property describing an entity.
- **Relationship** = association between entities.
- **Relationship set** = collection of similar relationships.
- **Degree** = number of entity sets in a relationship (unary=1, binary=2, ternary=3).
- **Cardinality ratio** = how many of one entity can relate to another (1:1, 1:N, M:N).
- **Composite key** = two or more attributes used together as a key.
- **Weak entity set** = an entity set without a key attribute of its own; identified via a **partial key** combined with the key of its **owner entity set** (e.g., `Dependent` of an `Employee`).

### Summary

- The ER model is a conceptual tool for database design.
- It uses entities (rectangles), attributes (ovals), and relationships (diamonds).
- Understanding attribute types (simple, composite, derived, multi-valued, key) is essential.
- Cardinality ratios (1:1, 1:N, M:N) define the constraints on relationships.
- The ER diagram serves as a blueprint that can be transformed into relational tables in the next design phase.

---

## Practice Problems

**1.** In a hospital database, identify the entities, attributes, and relationships. Draw an ER diagram conceptually.
<details>
<summary>Answer</summary>
Entities: Patient (patient_id, name, dob, phone), Doctor (doctor_id, name, specialty), Appointment (appt_id, date, time). Relationships: Doctor *has* Appointment (1:N), Patient *books* Appointment (1:N). Ternary: Doctor *treats* Patient *in* Appointment.
</details>

**2.** What is the degree of a relationship? Give one example of a unary, binary, and ternary relationship.
<details>
<summary>Answer</summary>
Degree = number of entity sets participating. Unary: Employee *manages* Employee. Binary: Student *enrolls* Course. Ternary: Customer *buys* Product *from* Store.
</details>

**3.** Differentiate between simple and composite attributes with examples.
<details>
<summary>Answer</summary>
Simple: cannot be divided (e.g., `age`). Composite: can be divided (e.g., `Address` -> street, city, state, zip).
</details>

**4.** A student can be enrolled in multiple courses, and a course can have multiple students. What is the cardinality ratio?
<details>
<summary>Answer</summary>
M:N (Many-to-Many). This requires a junction/intersection table like `Enrollment(student_id, course_id)` when converting to relational schema.
</details>

**5.** Define composite key. Give an example.
<details>
<summary>Answer</summary>
A composite key is a combination of two or more attributes that uniquely identifies a record. Example: In `Enrollment`, the composite key is `(student_id, course_id, semester)` because a student can take multiple courses and the same course across different semesters.
</details>
