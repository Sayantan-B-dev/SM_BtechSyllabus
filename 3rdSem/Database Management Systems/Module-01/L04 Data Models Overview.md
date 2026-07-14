# Data Models Overview

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 4  
**Date:** 16-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### What is a Data Model?

A **data model** is a collection of conceptual tools for describing:
- **Data** -- what data is stored.
- **Relationships** -- how data elements relate to each other.
- **Semantics** -- what the data means and what constraints apply.
- **Consistency constraints** -- rules that data must satisfy.

Think of a data model as the **blueprint** for building a database. Just as an architectural blueprint specifies the structure, dimensions, and materials of a building, a data model specifies the structure, types, and rules for the database.

**Key purpose:** A data model provides a way to represent real-world information in a form that a computer system can manage. It bridges the gap between how humans conceptualize the world and how computers store data.

### Categories of Data Models

Data models are classified into three broad categories based on their level of abstraction:

```
High Abstraction
      |
      |   Conceptual Data Models
      |   (ER Model, Object-Oriented)
      |   -- What the data looks like to the user
      |
      |   Logical Data Models
      |   (Relational, Network, Hierarchical, OO)
      |   -- How data is organized and structured
      |
      |   Physical Data Models
      |   (Storage structures, indexing)
      |   -- How data is actually stored
      |
Low Abstraction
```

#### 1. Conceptual Data Models

**Purpose:** Describe the database at a high level, close to how users perceive data. They are independent of any DBMS or storage technology.

**Features:**
- Use concepts like entities, attributes, and relationships.
- Are easy to understand by non-technical stakeholders.
- Are used during the requirements analysis and design phase.

**Examples:**
- **Entity-Relationship (ER) Model** -- Entities (rectangles), attributes (ovals), relationships (diamonds).
- **Object-Oriented (OO) Model** -- Objects with methods and attributes, classes, inheritance.
- **Semantic Data Model** -- Rich semantic constructs like generalization, aggregation.

#### 2. Logical Data Models

**Purpose:** Describe how data is organized at the logical level, independent of physical storage details. These are the models that DBMS implementations actually use.

**Categories within logical models:**

**Record-Based Models:**
- Represent data as fixed-format records.
- A record consists of fields (attributes).
- The database structure is described using schemas.

**Types:**
- **Relational Model** -- Data in tables (relations), rows (tuples), columns (attributes).
- **Network Model** -- Data as records connected in a graph structure; CODASYL/DBTG standard.
- **Hierarchical Model** -- Data as tree structures with parent-child relationships; IMS (IBM).

**Object-Based Models:**
- **Object-Oriented Model** -- Data as objects (like OOP), with encapsulation, inheritance, and methods.
- **Object-Relational Model** -- Hybrid: relational tables with OO extensions (user-defined types, methods).

#### 3. Physical Data Models

**Purpose:** Describe the details of how data is stored on computer media (disks, SSDs).

**What they specify:**
- File organization (heap, sequential, hash, clustered).
- Index structures (B+ tree, bitmap, hash index).
- Record placement and blocking factors.
- Data compression and encryption techniques.
- Partitioning and sharding strategies.

**Physical models are DBMS-specific.** Oracle's physical storage (tablespaces, datafiles, extents, blocks) differs from PostgreSQL's (relations, pages, tuples).

Users and application programmers typically do not interact with the physical model directly.

### Record-Based Models vs Object-Based Models

| Aspect | Record-Based | Object-Based |
|---|---|---|
| **Core construct** | Fixed-format records | Objects (data + methods) |
| **Data types** | Primitive (INT, VARCHAR, DATE) | User-defined types, complex types |
| **Behavior** | Passive data (no operations) | Active data (encapsulated methods) |
| **Inheritance** | Not supported natively | Full inheritance support |
| **Relationships** | Foreign keys, pointers | References, object identifiers |
| **Query language** | SQL (declarative) | OQL, SQL extensions |
| **Complex data** | Requires normalization (joins) | Nested objects, collections |
| **Examples** | Relational, Network, Hierarchical | ObjectStore, GemStone, ORDBMS (PostgreSQL) |
| **Maturity** | Highly mature, widely used | Niche, specialized use cases |
| **Performance** | Excellent for tabular data | Good for complex data (CAD, GIS) |

### The Relational Model

The most widely used data model (the focus of this course).

**Key constructs:**

| Term | Description | Example |
|---|---|---|
| **Relation** | A table | `Student` table |
| **Tuple** | A row in a relation | One student record |
| **Attribute** | A column in a relation | `student_id`, `name` |
| **Domain** | Set of allowed values for an attribute | `CHAR(9)` for `student_id` |
| **Degree** | Number of attributes | `Student` has degree 5 |
| **Cardinality** | Number of tuples | `Student` has cardinality 1000 |
| **Relation Schema** | Name + attributes + domains | `Student(student_id: CHAR(9), name: VARCHAR(50), ...)` |
| **Relation Instance** | Set of tuples at a given time | The actual rows currently in `Student` |

**Example relation -- Student:**

| student_id | name | dept_id | tot_cred |
|---|---|---|---|
| CS2026001 | Alice Johnson | CS | 60 |
| EE2026002 | Bob Smith | EE | 45 |
| CS2026003 | Charlie Brown | CS | 75 |

**Formal definition:**

A relation is a subset of a Cartesian product of domains. Let domains `D1, D2, ..., Dn` be sets. A relation `r` is a set of `n`-tuples `(d1, d2, ..., dn)` where each `di` belongs to `Di`.

- `R = {(v1, v2, ..., vn) | vi in Di}`

**Properties of relations:**
- The order of tuples is irrelevant (a set, not a list).
- The order of attributes is irrelevant (columns can be reordered).
- All tuples are distinct (no duplicate rows).
- Each attribute has a unique name within the relation.
- Each attribute value is atomic (1NF requirement).

### Brief Comparison of All Major Data Models

| Feature | Relational | Network | Hierarchical | Object-Oriented | ER (Conceptual) |
|---|---|---|---|---|---|
| **Structure** | Tables (relations) | Graph (sets) | Tree (segments) | Classes (objects) | Entities + relationships |
| **Relationship representation** | Foreign keys + joins | Sets (owner-member links) | Parent-child pointers | Object references | Diamonds (relationships) |
| **Navigation** | Declarative (SQL) | Navigational (DML commands) | Navigational (hierarchical paths) | Navigational + declarative | Not applicable (design only) |
| **Data independence** | High | Low (structural changes break code) | Low (access paths fixed) | High (encapsulation) | Not applicable |
| **Flexibility** | High (ad-hoc queries) | Moderate | Low (fixed hierarchy) | High (complex types) | High (design flexibility) |
| **Complexity for user** | Low (SQL is simple) | High (requires pointers) | High (requires knowledge of paths) | Moderate | Low (visual diagrams) |
| **Performance** | Moderate (join overhead) | High (direct pointers) | High (tree traversal) | Good for complex objects | Conceptual only |
| **Ad-hoc query support** | Excellent (SQL) | Poor | Poor | Good (OQL) | Not applicable |
| **Current popularity** | Dominant (95%+ of market) | Legacy (few systems) | Legacy (IMS still in use) | Niche (CAD, telecom) | Universal (used in design) |
| **Standardization** | SQL standard (ISO/ANSI) | CODASYL DBTG (defunct) | IMS-specific | ODMG (defunct) | ER extensions (Chen notation) |

### Choosing a Data Model

The choice depends on the application:

- **Business applications (ERP, CRM, banking, e-commerce):** Relational model -- SQL is well-supported, data integrity is strong, ad-hoc querying is easy.

- **Complex engineering/CAD/CAM:** Object-oriented model -- complex objects with inheritance and methods match the problem domain.

- **Geographic Information Systems (GIS):** Object-relational model (PostGIS) -- spatial data types + relational querying.

- **Legacy mainframe systems:** Hierarchical (IMS) or Network (IDMS) -- these still exist in banking and telecom but are being phased out.

- **Design/planning phase:** ER model -- it is used to create a conceptual blueprint before choosing a logical model.

- **Big Data / unstructured data:** NoSQL models (document, key-value, graph, column-family) -- these are outside the scope of this course but are important in modern systems.

### Summary

- A **data model** provides the tools to describe the structure, relationships, constraints, and semantics of data.
- **Conceptual models** (ER, OO) are used during design -- they are abstract and user-friendly.
- **Logical models** (Relational, Network, Hierarchical) define the actual organization of data in a DBMS.
- **Physical models** describe storage details (indexes, file organization) and are DBMS-specific.
- The **Relational Model** dominates the industry due to its simplicity, declarative querying (SQL), and strong theoretical foundation.
- Understanding all models is important for historical context and for choosing the right tool for the job.

---

## Practice Problems

**1.** Define a data model. Why is it important in database design?
<details>
<summary>Show Answer</summary>
A data model is a collection of concepts for describing data, relationships, semantics, and constraints. It is important because it provides a systematic way to represent real-world information in a database, ensuring that the design is consistent, complete, and understandable by both designers and users.
</details>

**2.** List the three categories of data models based on abstraction level and give one example of each.
<details>
<summary>Show Answer</summary>
Conceptual (ER model), Logical (Relational model), Physical (Storage and indexing model).
</details>

**3.** In the relational model, define: relation, tuple, attribute, domain, degree, cardinality.
<details>
<summary>Show Answer</summary>
Relation = table; Tuple = row; Attribute = column; Domain = set of allowed values for an attribute; Degree = number of attributes; Cardinality = number of tuples.
</details>

**4.** What is the difference between a record-based model and an object-based model?
<details>
<summary>Show Answer</summary>
Record-based models (Relational, Network, Hierarchical) organize data as fixed-format records with primitive data types and passive data. Object-based models treat data as objects that encapsulate both state and behavior, supporting inheritance, polymorphism, and complex user-defined types.
</details>

**5.** Why does the relational model dominate the database industry today?
<details>
<summary>Show Answer</summary>
Simplicity (tables are intuitive), strong theoretical foundation (set theory, predicate logic), declarative query language (SQL), high data independence, support for ad-hoc queries, robust integrity constraints, and extensive vendor support and standardization.
</details>
