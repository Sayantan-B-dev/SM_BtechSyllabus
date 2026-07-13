# Tuple Relational Calculus

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 3  
**Date:** 04-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Tuple Relational Calculus (TRC)?

Tuple Relational Calculus is a **declarative** query language for the relational model. Unlike relational algebra, which specifies *how* to get data (procedure), TRC specifies *what* data is wanted (description).

**Notation:** `{ t | CONDITION(t) }`

This reads as: "The set of all tuples `t` such that `CONDITION(t)` is true."

`t` is a **tuple variable** that ranges over all possible tuples. The condition restricts which tuples are included in the result.

---

## Basic Structure of TRC Queries

```
{ t | Relation(t) AND condition_on_attributes(t) }
```

**Example:** Find all employees who earn more than 50000:

```
{ e | EMPLOYEE(e) AND e.Salary > 50000 }
```

This returns the complete tuples of all employees with salary > 50000.

To return **only specific attributes**, we use existential quantification or the dot notation on the tuple variable. But basic TRC returns whole tuples. To project specific attributes, we can use a modified form:

```
{ e.Name | EMPLOYEE(e) AND e.Salary > 50000 }
```

---

## Sample Data for Examples

`EMPLOYEE(EmpID, Name, Dept, Salary)`:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 102 | Bob | HR | 45000 |
| 103 | Charlie | IT | 55000 |
| 104 | Diana | Finance | 70000 |
| 105 | Eve | IT | 48000 |

`DEPARTMENT(Dept, Location, Budget)`:

| Dept | Location | Budget |
|------|----------|--------|
| IT | New York | 500000 |
| HR | Chicago | 200000 |
| Finance | New York | 400000 |

---

## Simple TRC Queries

**Query 1:** Find all employees in the IT department.

```
{ e | EMPLOYEE(e) AND e.Dept = 'IT' }
```

Result: Alice, Charlie, Eve.

**Query 2:** Find the names of employees in IT.

```
{ e.Name | EMPLOYEE(e) AND e.Dept = 'IT' }
```

Result: Alice, Charlie, Eve.

---

## Quantifiers in TRC

TRC uses two quantifiers to express more complex conditions:

### Existential Quantifier (EXISTS)

`EXISTS t (CONDITION(t))` is true if there exists at least one tuple `t` satisfying the condition.

**Query 3:** Find employees whose department is located in New York.

```
{ e | EMPLOYEE(e) AND EXISTS d (DEPARTMENT(d) AND d.Dept = e.Dept AND d.Location = 'New York') }
```

This reads: "Find employee tuples `e` such that there exists a department tuple `d` where the department name matches the employee's department and the location is New York."

Result: Alice (IT), Charlie (IT), Eve (IT), Diana (Finance).

**Query 4:** Find names of employees whose department budget > 300000.

```
{ e.Name | EMPLOYEE(e) AND EXISTS d (DEPARTMENT(d) AND d.Dept = e.Dept AND d.Budget > 300000) }
```

Result: Alice, Charlie, Eve, Diana.

### Universal Quantifier (FORALL)

`FORALL t (CONDITION(t))` is true if the condition holds for ALL tuples `t`.

**Query 5:** Find departments where every employee earns > 50000.

```
{ d.Dept | DEPARTMENT(d) AND (FORALL e (EMPLOYEE(e) AND e.Dept = d.Dept => e.Salary > 50000)) }
```

This reads: "Find department names `d` such that for all employees `e`, if `e` works in department `d`, then `e.Salary > 50000`."

The implication `=>` (if-then) is crucial. If no employee works in a department, the condition `FORALL e (EMPLOYEE(e) AND e.Dept = d.Dept => e.Salary > 50000)` is vacuously true.

Result: Only Finance (Diana earns 70000 > 50000, and she is the only employee there). IT fails because Eve earns 48000. HR fails because Bob earns 45000.

---

## Safe Expressions

A TRC expression is **safe** if it guarantees a finite result. Unsafe expressions can produce infinite results.

**Unsafe example:**

```
{ t | NOT EMPLOYEE(t) }
```

This would try to return all possible tuples that are NOT in the EMPLOYEE table -- which is infinite.

**Safe expression rule:** All tuples in the result must be drawn from a limited set of values, typically those appearing in the database or in the query itself.

Most practical TRC queries are safe when every variable is restricted by a relation predicate.

---

## Comparison: TRC vs Relational Algebra

| Aspect | Relational Algebra | Tuple Relational Calculus |
|--------|-------------------|--------------------------|
| Nature | Procedural | Declarative |
| Focus | HOW to get data | WHAT data to get |
| Operations | Operators like `sigma`, `pi`, `bowtie` | Formulas with quantifiers |
| Variables | No variables | Tuple variables with quantifiers |
| Expressiveness | Equivalent to TRC | Equivalent to RA |
| Ease of writing | Requires step-by-step | More intuitive for simple queries |

**Equivalence:** For every relational algebra expression, there is an equivalent TRC expression, and vice versa (Codd's theorem). They have the same expressive power.

---

## Additional TRC Examples

**Query 6:** Find employees who earn more than the average salary (note: TRC cannot directly compute aggregate -- this shows a limitation).

TRC cannot express aggregate queries directly. This requires extensions.

**Query 7:** Find employees who work in a department with budget > any department in Chicago.

```
{ e | EMPLOYEE(e) AND EXISTS d1 (DEPARTMENT(d1) AND d1.Dept = e.Dept AND d1.Budget > SOME (SELECT budget FROM department WHERE location = 'Chicago')) }
```

But this involves a subquery. In pure TRC:

```
{ e | EMPLOYEE(e) AND EXISTS d1 (DEPARTMENT(d1) AND d1.Dept = e.Dept AND EXISTS d2 (DEPARTMENT(d2) AND d2.Location = 'Chicago' AND d1.Budget > d2.Budget)) }
```

---

## TRC in SQL Context

SQL's SELECT-FROM-WHERE structure is inspired by TRC:

```sql
SELECT e.Name
FROM Employee e
WHERE e.Salary > 50000
```

The `FROM Employee e` gives the tuple variable `e`. The `WHERE e.Salary > 50000` is the condition. The `SELECT e.Name` is the projection.

Correlated subqueries in SQL directly correspond to EXISTS quantifiers in TRC:

```sql
SELECT e.Name
FROM Employee e
WHERE EXISTS (
    SELECT * FROM Department d
    WHERE d.Dept = e.Dept AND d.Location = 'New York'
)
```

This is exactly the TRC query from Query 3.

---

## Practice Problems

1. Write a TRC query to find the names of all employees who work in the HR department.

2. Write a TRC query to find departments that have at least one employee earning more than 60000.

3. Write a TRC query to find employees who do NOT work in the IT department.

4. What makes a TRC expression unsafe? Give an example.

5. Convert the following RA expression to TRC: `pi_Name(sigma_Salary > 50000(EMPLOYEE))`

**Answers:**
1. `{ e.Name | EMPLOYEE(e) AND e.Dept = 'HR' }`
2. `{ d.Dept | DEPARTMENT(d) AND EXISTS e (EMPLOYEE(e) AND e.Dept = d.Dept AND e.Salary > 60000) }`
3. `{ e | EMPLOYEE(e) AND NOT (e.Dept = 'IT') }` or `{ e | EMPLOYEE(e) AND e.Dept != 'IT' }`
4. An expression is unsafe if it can produce infinite results, e.g., `{ t | NOT R(t) }` would try to enumerate all tuples not in R, which is infinite.
5. `{ e.Name | EMPLOYEE(e) AND e.Salary > 50000 }`
