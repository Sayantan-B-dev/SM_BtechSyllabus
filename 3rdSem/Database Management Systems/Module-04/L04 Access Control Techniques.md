# Access Control Techniques

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 4  
**Date:** 13-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Overview of Access Control

Access control determines who can access what resources and under what conditions. Three major models are widely used in database systems: Discretionary Access Control (DAC), Mandatory Access Control (MAC), and Role-Based Access Control (RBAC).

## 1. Discretionary Access Control (DAC)

In DAC, the owner of an object (e.g., a table creator) has discretion over who can access it. The owner decides which privileges to grant and to whom.

**Key characteristics:**
- Users can grant and revoke privileges on objects they own.
- Privileges are propagated via GRANT with WITH GRANT OPTION.
- Access rights are specified by the data owner.

**Implementation:** SQL's GRANT/REVOKE mechanism (covered in L03).

**Advantages:**
- Flexible and intuitive.
- Suitable for collaborative environments.

**Disadvantages:**
- No control over information flow. If Alice can read a record and is allowed to grant SELECT, she can give Bob access, and Bob can pass it further. The original owner loses control.
- Vulnerable to Trojan horse attacks: a malicious program running under a user's privileges can leak data.

**Example:**

```sql
-- Owner creates a table
CREATE TABLE project_data (
    project_id INT PRIMARY KEY,
    budget DECIMAL(12,2)
);

-- Owner grants SELECT to Alice
GRANT SELECT ON project_data TO alice;

-- Alice (with GRANT OPTION) grants SELECT to Bob
GRANT SELECT ON project_data TO bob;
```

The owner (who created the table) controls access via ownership. Alice has discretion to pass privileges onward.

## 2. Mandatory Access Control (MAC)

In MAC, access decisions are made by a central authority based on security classifications. Users and data objects are assigned labels (classification levels). The system enforces rules; users cannot override them.

**Key characteristics:**
- Every subject (user) and object (table, row) has a security label.
- Labels form a lattice, e.g., TOP SECRET > SECRET > CONFIDENTIAL > UNCLASSIFIED.
- Access rules are defined by the system, not by individual users.
- Used in military and government systems.

### The Bell-LaPadula Model (BLP)

The Bell-LaPadula model is the foundational MAC model, designed to enforce confidentiality.

**Two core properties:**

```
+-----------------------------+---------------------------------------------+
| Simple Security Property    | No Read Up (NRU): A subject at a given       |
| (No Read Up)                | classification level cannot read an object   |
|                             | with a higher classification.                |
|                             | Example: A SECRET user cannot read TOP       |
|                             | SECRET data.                                 |
+-----------------------------+---------------------------------------------+
| Star Property (* Property)  | No Write Down (NWD): A subject at a given    |
| (No Write Down)             | classification level cannot write to an      |
|                             | object with a lower classification.          |
|                             | Example: A TOP SECRET user cannot write to a |
|                             | CONFIDENTIAL file (prevents leaking).        |
+-----------------------------+---------------------------------------------+
```

```
        TOP SECRET
            |
        SECRET
            |
        CONFIDENTIAL
            |
        UNCLASSIFIED

A user at SECRET can:
  - Read UNCLASSIFIED and CONFIDENTIAL (read down).
  - Read SECRET (read equal).
  - Write to SECRET and TOP SECRET (write up).
  - Cannot write to CONFIDENTIAL or UNCLASSIFIED (no write down).
  - Cannot read TOP SECRET (no read up).
```

**Advantages:**
- Strong security enforced by the system.
- Prevents information leaks even if user programs are malicious.

**Disadvantages:**
- Rigid and complex to administer.
- Not suitable for commercial environments that require flexibility.
- Can interfere with normal operations (e.g., a manager might need to write a lower-classification document).

## 3. Role-Based Access Control (RBAC)

RBAC is the most widely used access control model in commercial database systems. Permissions are associated with roles, and users are assigned to roles.

**Core components:**

```
+-------------+          +-------------+          +-------------+
|   USERS    |---------->|   ROLES    |---------->| PERMISSIONS |
+-------------+          +-------------+          +-------------+
  Many-to-many           Many-to-many
```

- **Permissions:** Rights to perform operations on objects (SELECT, INSERT, etc.).
- **Roles:** Named collections of permissions (e.g., `manager`, `clerk`, `analyst`).
- **Users:** Real people or applications assigned to one or more roles.

### Creating and Managing Roles

```sql
-- Create a role
CREATE ROLE payroll_analyst;

-- Grant privileges to the role
GRANT SELECT ON employees TO payroll_analyst;
GRANT SELECT, UPDATE ON salary_details TO payroll_analyst;

-- Grant the role to a user
GRANT payroll_analyst TO alice;

-- Revoke the role from a user
REVOKE payroll_analyst FROM alice;

-- Drop a role
DROP ROLE payroll_analyst;
```

### Role Hierarchy

Roles can inherit permissions from other roles, creating a hierarchy.

```sql
CREATE ROLE clerk;
CREATE ROLE manager;

-- Grant basic privileges to clerk
GRANT SELECT ON orders TO clerk;

-- Manager inherits clerk's privileges and gets additional ones
GRANT manager TO clerk;  -- in some systems: GRANT clerk TO manager;
GRANT INSERT, UPDATE ON orders TO manager;
```

### Advantages of RBAC

| Feature               | Benefit                                                    |
|-----------------------|------------------------------------------------------------|
| Simplified admin      | Grant/revoke roles, not individual permissions per user.   |
| Policy-neutral        | Works for many organization structures.                    |
| Least privilege       | Assign only the roles needed for the job.                  |
| Separation of duties  | Design conflicting roles that cannot be held by one user.  |
| Auditable             | Role assignments are easy to review.                       |

### Example: University Database

```sql
-- Create roles
CREATE ROLE student;
CREATE ROLE instructor;
CREATE ROLE admin;

-- Grant permissions to roles
GRANT SELECT ON course_catalog TO student;
GRANT SELECT, INSERT ON enrollments TO student;

GRANT SELECT, INSERT, UPDATE ON course_catalog TO instructor;
GRANT SELECT, INSERT, UPDATE ON enrollments TO instructor;
GRANT SELECT ON student_records TO instructor;

GRANT ALL PRIVILEGES ON ALL TABLES TO admin;

-- Assign users to roles
GRANT student TO alice;
GRANT instructor TO bob;
GRANT admin TO carol;
```

If a new student `dave` joins, simply execute `GRANT student TO dave;` -- all student permissions are automatically applied.

## Comparison Table

| Criterion              | DAC                          | MAC                          | RBAC                          |
|------------------------|------------------------------|------------------------------|-------------------------------|
| Who controls access?  | Object owner                 | Central authority            | Administrator via roles       |
| Flexibility           | High                         | Low                          | Medium                        |
| Security level        | Low to medium                | High                         | Medium to high                |
| Ease of administration| Easy for small systems       | Complex                      | Moderate                      |
| User discretion       | Yes (can grant to others)    | No                           | No (admin assigns roles)      |
| Information flow      | Not controlled               | Strictly controlled          | Indirectly controlled         |
| Use cases             | Small teams, collaborative   | Military, government         | Enterprise, commercial        |
| SQL support           | GRANT/REVOKE                 | Some DBMS (Oracle Label Security)| CREATE ROLE, GRANT ROLE   |

## Summary

- **DAC** gives ownership control via GRANT/REVOKE. Flexible but weak for high-security environments.
- **MAC** uses classification labels and enforces No Read Up / No Write Down (Bell-LaPadula). Strong but rigid.
- **RBAC** uses roles as intermediaries between users and permissions. It is the most practical model for enterprise databases.
- Modern DBMS often combine these models (e.g., RBAC with some DAC features).

---

## Practice Problems

1. Explain the Bell-LaPadula model. What do "no read up" and "no write down" mean? Why is "no write down" necessary?
   <details>
   <summary>Show Answer</summary>
   Bell-LaPadula is a MAC model enforcing confidentiality. **No read up:** A subject cannot read data at a higher classification level (prevents access to secrets). **No write down:** A subject cannot write data to a lower classification level (prevents leaking high-classification data to low-classification users). "No write down" is necessary to prevent a high-level user from accidentally or maliciously declassifying sensitive information by writing it to a lower-level object.
   </details>
2. Create an RBAC setup for a hospital with roles: doctor, nurse, pharmacist, and administrator. Write SQL to create the roles and grant appropriate permissions.
   <details>
   <summary>Show Answer</summary>
   ```sql
   CREATE ROLE doctor;
   CREATE ROLE nurse;
   CREATE ROLE pharmacist;
   CREATE ROLE admin;

   GRANT SELECT, INSERT, UPDATE ON patients TO doctor;
   GRANT SELECT, UPDATE ON patients TO nurse;
   GRANT SELECT ON prescriptions TO pharmacist;
   GRANT ALL PRIVILEGES ON ALL TABLES TO admin;

   GRANT doctor TO alice;
   GRANT nurse TO bob;
   GRANT pharmacist TO charlie;
   GRANT admin TO diana;
   ```
   </details>
3. Compare DAC, MAC, and RBAC in a table. Which model would you recommend for a bank's transaction database and why?
   <details>
   <summary>Show Answer</summary>
   | Feature | DAC | MAC | RBAC |
   |---------|-----|-----|------|
   | Policy control | Data owner | Central authority | Role-based |
   | Flexibility | High | Low | Medium |
   | Security level | Low | High | Medium-High |
   | Admin overhead | Low | High | Medium |
   | Use case | Personal files | Military | Enterprise |

   **Recommendation:** RBAC — banks have well-defined roles (teller, manager, auditor) and need a balance of security and manageability.
   </details>
4. What is a Trojan horse attack in the context of DAC? How does MAC prevent it?
   <details>
   <summary>Show Answer</summary>
   In DAC, a Trojan horse is a malicious program running with a user's privileges that reads sensitive files and writes the data to a publicly accessible file accessible to the attacker. MAC prevents this because even if the user runs the Trojan, the "no write down" rule stops the program from writing high-classification data to a low-classification file, regardless of the user's intentions.
   </details>
5. Write SQL statements to create a role `sales_team`, grant it SELECT and INSERT on the `customers` table and SELECT on `products`, and assign it to users `kumar` and `priya`.
   <details>
   <summary>Show Answer</summary>
   ```sql
   CREATE ROLE sales_team;
   GRANT SELECT, INSERT ON customers TO sales_team;
   GRANT SELECT ON products TO sales_team;
   GRANT sales_team TO kumar, priya;
   ```
   </details>
