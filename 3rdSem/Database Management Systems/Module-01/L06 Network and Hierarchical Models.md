# Network and Hierarchical Models

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 6  
**Date:** 21-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### Introduction

Before the relational model became dominant in the 1980s, two major database models were widely used:

1. **Hierarchical Model** -- Developed by IBM in the 1960s for the IMS (Information Management System) project.
2. **Network Model** -- Standardized by the CODASYL DBTG (Conference on Data Systems Languages / Database Task Group) in 1971.

Both models are **record-based** (data is organized as records with fixed fields) and use **pointers/links** to represent relationships. They are collectively known as **navigational database models** because programmers navigate through the data using explicit pointers and paths.

---

### Hierarchical Model

#### Tree Structure

The hierarchical model organizes data in a **tree** structure.

- The **root** is the topmost node.
- Each node is a **segment** (a record type with fields).
- Each parent can have zero or more **children**.
- Each child has **exactly one parent** (except the root).
- Relationships form a **one-to-many** hierarchy.

```
                        +---------------+
                        |  Department   |  (Root segment)
                        | dept_id       |
                        | dept_name     |
                        +---------------+
                               |
                    +----------+----------+
                    |                     |
            +-------+-------+     +-------+-------+
            |   Course      |     |  Instructor   |
            | course_id     |     | instructor_id  |
            | title         |     | name           |
            | credits       |     | salary         |
            +-------+-------+     +---------------+
                    |
          +---------+---------+
          |                   |
    +-----+------+     +------+------+
    |  Section   |     | Textbook   |
    | section_id |     | title       |
    | semester   |     | author      |
    | year       |     +-------------+
    +------------+
```

**Key terminology:**
- **Segment:** A record type (like a table in relational). Each segment has fields.
- **Parent-Child Relationship (PCR):** A 1:N relationship between two segment types.
- **Hierarchical path:** The unique traversal path from root to any segment (e.g., Department -> Course -> Section).
- **Schema:** A hierarchical database schema is a collection of trees (called **database records**).
- **Instance:** A specific occurrence of a segment (like a row).

#### Access Method

Data is accessed by navigating from the **root** downward following the hierarchical paths.

**To retrieve the sections of a specific course in a specific department:**
1. Find the `Department` segment (e.g., by dept_id = 'CS').
2. Navigate down to the child `Course` segments.
3. Find the specific `Course` (e.g., course_id = 'CS301').
4. Navigate down to the child `Section` segments.

**DL/I (Data Language/One) -- IMS query language example:**

```sql
-- Conceptual DL/I traversal
GU  DEPARTMENT (DEPT_ID = 'CS')
    COURSE (COURSE_ID = 'CS301')
    SECTION (*)
```

- `GU` = Get Unique (find one specific record).
- `GN` = Get Next (iterate through siblings).

The programmer must know the exact hierarchical path. This is **procedural/navigational** -- you specify *how* to reach the data, not just *what* data you want.

#### Advantages of the Hierarchical Model

1. **Fast data retrieval** -- Parent-child pointers allow direct traversal without expensive join operations. For hierarchical data (organization charts, product categories), it is very fast.

2. **Simple structure** -- The tree structure is intuitive for representing natural hierarchies.

3. **Data integrity** -- Referential integrity is built-in: a child cannot exist without a parent (the parent is always created first).

4. **Efficient for 1:N relationships** -- One-to-many relationships are handled naturally and efficiently.

5. **Good performance** -- For well-known access patterns (queries following the hierarchy), performance is excellent.

#### Disadvantages of the Hierarchical Model

1. **Structural dependence** -- Changing the hierarchy (e.g., moving a segment from one parent to another) breaks all existing application programs. This is a severe lack of **logical data independence**.

2. **No M:N relationships** -- Many-to-many relationships cannot be directly represented. They require **virtual segments** or data duplication, adding complexity.

3. **Navigational access** -- Programmers must know the physical access path. Ad-hoc queries are difficult.

4. **Data redundancy** -- If a segment logically belongs under multiple parents, its data must be duplicated (or virtual segments used), causing redundancy.

5. **Limited flexibility** -- A rigid hierarchy means one predefined access path. If you need to query data from a different entry point, it is inefficient.

**Example -- Problem with hierarchy:**

Consider a university where:
- An `Instructor` can work in multiple departments.
- A `Student` should be accessible from both `Department` and `Course` paths.

In a pure hierarchy, a `Student` segment can only have one parent, forcing duplication or complex restructuring.

---

### Network Model

#### Graph Structure

The network model extends the hierarchical model by allowing a child to have **multiple parents**, forming a **graph** (or network) structure instead of a tree.

```
                       +-----------+
                       |  Student  |
                       +-----------+
                            |
                   M        |
                 Takes     /
                           /
               +---------+/
               | Section |--------------+
               +---------+              |
                    |                   |
            1       |                   | M
                    |                   |
                Teaches              Listed_in
                    |                   |
                    |M                  |
               +------------+    +-----------+
               | Instructor |    |  Course   |
               +------------+    +-----------+
```

#### Set Concept (Owner-Member)

The fundamental organizing construct in the network model is the **SET**.

A **set** is a named collection of record types that defines a 1:N relationship between two record types:
- **Owner record type** -- The "parent" (one side).
- **Member record type** -- The "child" (many side).

**Syntax:**
```
SET NAME is SetName
OWNER is OwnerRecordType
MEMBER is MemberRecordType
```

**Example -- Defining sets:**
```
RECORD NAME IS Department
    dept_id    PIC X(4)
    dept_name  PIC X(50)

RECORD NAME IS Course
    course_id  PIC X(8)
    title      PIC X(100)
    credits    PIC 9

RECORD NAME IS Instructor
    instructor_id PIC X(5)
    name          PIC X(50)

SET NAME IS Dept_Course
    OWNER IS Department
    MEMBER IS Course

SET NAME IS Dept_Instructor
    OWNER IS Department
    MEMBER IS Instructor
```

#### CODASYL DBTG

The **CODASYL DBTG** (Conference on Data Systems Languages / Database Task Group) published the first standard for the network model in 1971. Key constructs:

1. **Record Type** -- Like a table or segment. A template for data records.

2. **Set Type** -- A named 1:N relationship between two record types.

3. **Set Occurrence** -- A specific instance of a set (e.g., the set of all courses in the CS department).

4. **Singular Set** -- A set with the system as owner, used to access all records of a type (like a full table scan).

5. **Currency Indicator** -- A pointer to the "current" record of each record type, each set, and the run-unit (program). Used for navigational processing.

6. **Mode** -- How membership is maintained:
   - **AUTOMATIC** -- Member is automatically linked to owner on creation.
   - **MANUAL** -- Member is linked explicitly by the programmer.
   - **FIXED** -- Member cannot be moved to another owner.
   - **MANDATORY** -- Member must always belong to some owner.
   - **OPTIONAL** -- Member can exist without an owner.

#### DBTG DML (Navigational Commands)

The network model uses **procedural DML** to navigate through sets.

```sql
-- Locate a department
FIND FIRST Department WHERE dept_id = 'CS'

-- Navigate to the first course in the Dept_Course set
FIND FIRST Course WITHIN Dept_Course

-- Navigate to the next course in the same set
FIND NEXT Course WITHIN Dept_Course

-- Get data from the current record
GET Course

-- Create a new course and connect it to the current department
CONNECT Course TO Dept_Course

-- Disconnect a course from a department
DISCONNECT Course FROM Dept_Course

-- Reconnect a course to a different department
RECONNECT Course WITHIN Dept_Course

-- Remove a record
ERASE Course
```

#### CODASYL Record Access Modes

| Mode | Description |
|---|---|
| **CALC** | Direct access via hash key (like primary key lookup). |
| **VIA SET** | Access via membership in a set (navigation from owner). |
| **SORTED** | Sequential access sorted by key within a set. |
| **INDEXED** | Access via an index on a field. |

#### Advantages of the Network Model

1. **Multiple parent support** -- A record can belong to multiple sets (have multiple parents), enabling M:N relationships and flexible data modeling.

2. **Fast retrieval** -- Direct set pointers provide efficient navigation without joins.

3. **Data integrity** -- Set membership rules enforce consistency.

4. **Flexibility** -- More flexible than the hierarchical model for complex relationships.

5. **Established standard** -- CODASYL DBTG provided a formal standard (unlike the many vendor-specific hierarchical implementations).

#### Disadvantages of the Network Model

1. **Complexity** -- The programmer must understand the set structure, currency indicators, and navigation logic. Application development is significantly harder than with SQL.

2. **Structural dependence** -- Changes to the set structure (adding/removing sets, changing membership) can break existing programs.

3. **No ad-hoc querying** -- Queries must be pre-programmed. End users cannot easily ask questions.

4. **Implementation complexity** -- The DBMS itself is complex to build (maintaining pointers, handling currency, etc.).

5. **Little data independence** -- The logical and physical structure are tightly coupled.

### Comparison: Hierarchical vs Network

| Aspect | Hierarchical Model | Network Model |
|---|---|---|
| **Structure** | Tree (single parent per child) | Graph (multiple parents per child) |
| **Relationship representation** | Parent-child pointers | Named sets (owner-member) |
| **M:N relationships** | Not directly supported | Supported via multiple sets |
| **Navigation** | Root-to-leaf path | Set-based traversal |
| **Flexibility** | Low -- rigid hierarchy | Medium -- multiple access paths |
| **Complexity** | Medium | High |
| **Data independence** | Low (structural changes break code) | Low (structural changes break code) |
| **Standard** | IMS (IBM proprietary) | CODASYL DBTG (open standard) |
| **Query language** | DL/I (procedural) | DBTG DML (procedural) |
| **Popularity** | Legacy -- still used in banking | Legacy -- mostly retired |
| **Performance for hierarchical data** | Excellent | Good |
| **Subschema support** | Limited (logical databases) | Yes (subschema defines user view) |

### Comparison: Both vs Relational Model

| Aspect | Navigational Models (Hierarchical + Network) | Relational Model |
|---|---|---|
| **Query method** | Procedural (navigate with pointers) | Declarative (what, not how) |
| **Data independence** | Low -- access path is fixed in code | High -- DBMS optimizes independently |
| **Ad-hoc query** | Not possible (requires programmer) | Easy (SQL by end users) |
| **Ease of development** | Hard -- navigate step by step | Easy -- write SELECT statements |
| **Integrity** | Built into set structure | Declarative constraints |
| **Flexibility** | Tight coupling of structure and application | Loose coupling |
| **Performance** | Excellent for known paths | Good (optimizer chooses path) |

### Why Navigational Models Declined

1. **Rise of the relational model** (Codd, 1970) provided a simpler, mathematical foundation.
2. **SQL became standard** -- a declarative, high-level language.
3. **Data independence** -- relational separation of logical and physical levels.
4. **Ad-hoc querying** -- business users could query data directly without programming.
5. **Hardware improvements** made relational join performance acceptable.
6. **Maintenance costs** -- navigational applications were expensive to modify.

### Legacy Relevance

Despite being mostly superseded, these models are still historically important:
- **IMS** (Hierarchical) is still used by many large banks and insurance companies for core transaction processing.
- **IDMS** (Network/Codasyl) was used by the US government and large enterprises.
- Understanding them helps in appreciating **why the relational model won** and what trade-offs were made.
- NoSQL graph databases (Neo4j) revive some network model ideas but with modern query languages like Cypher.

---

## Practice Problems

**1.** What is the fundamental structural difference between the hierarchical and network models?
<details>
<summary>Answer</summary>
Hierarchical is a tree structure where each child has exactly one parent. Network is a graph structure where a child can have multiple parents via membership in multiple sets.
</details>

**2.** How are M:N relationships handled in the hierarchical model?
<details>
<summary>Answer</summary>
They are not directly supported. Workarounds include data duplication (storing the same segment under multiple parents) or using virtual segments (logical pointers), both of which introduce complexity and potential inconsistency.
</details>

**3.** Define the "set" concept in the network model. What are its components?
<details>
<summary>Answer</summary>
A set is a named 1:N relationship between record types. It has an OWNER (the "one" side) and MEMBER(s) (the "many" side). Each set occurrence links one owner record to zero or more member records.
</details>

**4.** Why do the hierarchical and network models have poor data independence?
<details>
<summary>Answer</summary>
Because application programs embed the navigational access paths (pointers, tree paths, set traversal). If the database structure changes (e.g., a segment is moved, or a set is reorganized), the programs must be rewritten to follow the new paths.
</details>

**5.** Compare navigational models (hierarchical/network) with the relational model in terms of query approach and ease of use.
<details>
<summary>Answer</summary>
Navigational models use procedural DML -- the programmer explicitly navigates from record to record using pointers/currency indicators (how to get data). The relational model uses declarative SQL -- the user specifies what data is needed, and the DBMS optimizer determines how to retrieve it. SQL is far easier for ad-hoc queries and non-programmers.
</details>
