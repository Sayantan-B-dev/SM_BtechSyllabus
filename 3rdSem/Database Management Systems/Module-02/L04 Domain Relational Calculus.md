# Domain Relational Calculus

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 4  
**Date:** 06-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Domain Relational Calculus (DRC)?

Domain Relational Calculus is a **declarative** query language that uses **domain variables** (variables that range over individual attribute values, not entire tuples).

**Notation:** `{ <x1, x2, ..., xn> | COND(x1, x2, ..., xn) }`

This reads as: "The set of all n-tuples `<x1, x2, ..., xn>` such that the condition `COND` is satisfied."

Each `xi` is a domain variable that takes values from the domain of the i-th attribute in the result.

---

## DRC vs TRC: Key Differences

| Aspect | Tuple Calculus (TRC) | Domain Calculus (DRC) |
|--------|---------------------|----------------------|
| Variable ranges over | Entire tuples | Individual attribute values |
| Variable notation | `t` where `t.Attr` | `<x1, x2, ..., xn>` |
| Condition syntax | `Relation(t)` | `Relation(<x1, x2, ..., xn>)` |
| Quantification | `EXISTS t` or `FORALL t` | `EXISTS x` or `FORALL x` |

---

## Sample Data

`EMPLOYEE(EmpID, Name, Dept, Salary)`:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 102 | Bob | HR | 45000 |
| 103 | Charlie | IT | 55000 |
| 104 | Diana | Finance | 70000 |

---

## Simple DRC Queries

**Query 1:** Find all employee IDs and names.

```
{ <id, name> | EMPLOYEE(<id, name, dept, salary>) }
```

Result: `<101, Alice>, <102, Bob>, <103, Charlie>, <104, Diana>`

**Query 2:** Find the names of employees in the IT department.

```
{ <name> | EXISTS id, dept, salary (EMPLOYEE(<id, name, dept, salary>) AND dept = 'IT') }
```

Note: Variables not needed in the output are existentially quantified.

**Query 3:** Find all details of employees earning > 50000.

```
{ <id, name, dept, salary> | EMPLOYEE(<id, name, dept, salary>) AND salary > 50000 }
```

Result: Alice (101), Charlie (103), Diana (104).

---

## Using EXISTS and FORALL in DRC

### Existential Quantifier (EXISTS)

**Query 4:** Find employees whose department is located in New York.

Using `DEPARTMENT(Dept, Location, Budget)`:

```
{ <id, name, dept, salary> | EMPLOYEE(<id, name, dept, salary>) AND
  EXISTS loc, budget (DEPARTMENT(<dept, loc, budget>) AND loc = 'New York') }
```

Result: Alice, Charlie, Diana.

### Universal Quantifier (FORALL)

**Query 5:** Find departments where ALL employees earn > 50000.

```
{ <dept> | EXISTS loc, budget (DEPARTMENT(<dept, loc, budget>)) AND
  FORALL id, name, salary (EMPLOYEE(<id, name, dept, salary>) => salary > 50000) }
```

Result: Finance (the only department where every employee has salary > 50000).

---

## DRC with Multiple Relations

**Query 6:** Find employee names and their department locations.

```
{ <name, loc> | EXISTS id, dept, salary, budget
   (EMPLOYEE(<id, name, dept, salary>) AND
    DEPARTMENT(<dept, loc, budget>)) }
```

Result:
```
Alice, New York
Bob, Chicago
Charlie, New York
Diana, New York
```

**Query 7:** Find employees who earn more than Bob.

```
{ <id, name, dept, salary> | EMPLOYEE(<id, name, dept, salary>) AND
  EXISTS id2, dept2, salary2 (EMPLOYEE(<id2, 'Bob', dept2, salary2>) AND salary > salary2) }
```

Result: Alice (60000 > 45000), Charlie (55000 > 45000), Diana (70000 > 45000).

---

## Safe Expressions in DRC

Same rule as TRC: an expression is safe if it guarantees a finite result.

**Unsafe DRC example:**
```
{ <x, y> | NOT EMPLOYEE(<x, y, z, w>) }
```
This would try to enumerate all pairs that are NOT employee records -- infinite.

**Safe DRC rule:** Every variable in the result must appear in at least one positive relation predicate.

---

## Comparison: RA vs TRC vs DRC

| Feature | Relational Algebra | Tuple Calculus | Domain Calculus |
|---------|--------------------|---------------|-----------------|
| Type | Procedural | Declarative | Declarative |
| Variables | None | Tuple variables | Domain variables |
| Quantifiers | None | EXISTS, FORALL | EXISTS, FORALL |
| Notation | Operators | `{t \| COND(t)}` | `{<x1,...,xn> \| COND}` |
| Expressiveness | Equivalent | Equivalent | Equivalent |
| SQL inspiration | FROM/JOIN | SELECT-FROM-WHERE | -- |

**Codd's Theorem:** RA, TRC, and DRC are all equally expressive (they define the same class of queries, namely the domain-independent relational queries).

---

## Worked Example: Complex Query in DRC

**Query:** Find pairs of employees (by name) where the first earns more than the second, and they work in the same department.

```
{ <name1, name2> | EXISTS id1, dept1, sal1, id2, dept2, sal2
   (EMPLOYEE(<id1, name1, dept1, sal1>) AND
    EMPLOYEE(<id2, name2, dept2, sal2>) AND
    dept1 = dept2 AND
    sal1 > sal2) }
```

Result:
```
Alice, Bob (IT vs HR -- actually different depts, so no)
```

Let's trace with the actual data. The only same-department pairs:

- IT: Alice(60000) > Charlie(55000) -> `<Alice, Charlie>`
- IT: Charlie(55000) > Eve(48000) -> `<Charlie, Eve>` (if Eve exists with 48000 in IT)
- No other same-department salary differences.

---

## Practice Problems

1. Write a DRC query to find the names of all departments.

2. Write a DRC query to find employee IDs of employees who earn less than 50000.

3. Write a DRC query to find the names of employees who work in a department with budget > 300000.

4. What is the key difference between TRC and DRC?

5. Express the query "Find names of employees who work in ALL departments" in DRC (or explain why it cannot be expressed safely).

**Answers:**
1. `{ <dept> | DEPARTMENT(<dept, loc, budget>) }`
2. `{ <id> | EXISTS name, dept, salary (EMPLOYEE(<id, name, dept, salary>) AND salary < 50000) }`
3. `{ <name> | EXISTS id, dept, salary, loc, budget (EMPLOYEE(<id, name, dept, salary>) AND DEPARTMENT(<dept, loc, budget>) AND budget > 300000) }`
4. TRC uses tuple variables that range over entire tuples (e.g., `t.Name`); DRC uses domain variables that range over individual attribute values (e.g., `<name, ...>`).
5. This is difficult because an employee cannot work in ALL departments -- each employee belongs to exactly one department in our schema. A more realistic version: "Find employees who have ALL skills" requires division, which DRC can express using FORALL but it is complex.
