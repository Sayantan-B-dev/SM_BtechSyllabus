# Employee Management System- Concept of MongoDB and NoSQL.

**Course:** Database Management Systems Lab  
**Module:** 5 | **Lecture:** 6  
**Date:** 02-Nov-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use MongoDB aggregation pipeline: $match, $group, $sort.
- Create indexes in MongoDB for query performance.
- Compare MongoDB and MySQL for the Employee database use case.

## Theory / Concept

The aggregation pipeline in MongoDB processes documents through a series of stages: $match filters documents, $group groups them by a specified key with accumulator expressions ($sum, $avg, $max, $min, $count), and $sort orders results. Indexes in MongoDB improve query performance and are created using createIndex(). Choosing between MongoDB and MySQL depends on data structure, scalability needs, and query patterns.

## SQL Code

```javascript
// MongoDB aggregation pipeline examples
use EmployeeDB

// Insert sample data for aggregation
db.employees.insertMany([
    {
        emp_id: 1, emp_name: "Ravi Sharma", department: "IT",
        job_role: "Software Engineer", salary: 87500, status: "Active",
        experience_years: 6, projects: ["ERP", "CRM"]
    },
    {
        emp_id: 2, emp_name: "Priya Mehta", department: "IT",
        job_role: "Senior Developer", salary: 109500, status: "Active",
        experience_years: 8, projects: ["ERP", "Data Migration"]
    },
    {
        emp_id: 3, emp_name: "Amit Joshi", department: "Finance",
        job_role: "Accountant", salary: 55000, status: "Active",
        experience_years: 4, projects: ["Audit"]
    },
    {
        emp_id: 4, emp_name: "Sneha Kapoor", department: "Finance",
        job_role: "Finance Manager", salary: 85000, status: "Active",
        experience_years: 7, projects: ["Audit", "ERP"]
    },
    {
        emp_id: 5, emp_name: "Vikram Singh", department: "HR",
        job_role: "HR Executive", salary: 50000, status: "Active",
        experience_years: 3, projects: ["Wellness"]
    },
    {
        emp_id: 6, emp_name: "Ananya Das", department: "IT",
        job_role: "DevOps Engineer", salary: 93000, status: "Active",
        experience_years: 5, projects: ["ERP", "Cloud"]
    },
    {
        emp_id: 7, emp_name: "Rohit Verma", department: "Sales",
        job_role: "Sales Rep", salary: 72000, status: "Active",
        experience_years: 2, projects: ["CRM"]
    }
])

// Aggregation Pipeline Stage 1: $match (filter by department)
db.employees.aggregate([
    { $match: { department: "IT" } },
    { $sort: { salary: -1 } }
])

// Aggregation Pipeline Stage 2: $group (average salary by department)
db.employees.aggregate([
    {
        $group: {
            _id: "$department",
            avg_salary: { $avg: "$salary" },
            total_salary: { $sum: "$salary" },
            employee_count: { $sum: 1 },
            max_salary: { $max: "$salary" },
            min_salary: { $min: "$salary" }
        }
    },
    { $sort: { avg_salary: -1 } }
])

// Aggregation Pipeline Stage 3: $match + $group + $sort
db.employees.aggregate([
    { $match: { status: "Active" } },
    {
        $group: {
            _id: "$department",
            emp_count: { $sum: 1 },
            avg_salary: { $avg: "$salary" }
        }
    },
    { $match: { emp_count: { $gte: 2 } } },
    { $sort: { avg_salary: -1 } }
])

// Aggregation Pipeline Stage 4: $unwind (expand arrays) + $group
db.employees.aggregate([
    { $unwind: "$projects" },
    {
        $group: {
            _id: "$projects",
            employees: { $push: "$emp_name" },
            count: { $sum: 1 }
        }
    },
    { $sort: { count: -1 } }
])

// Creating indexes
// Single field index
db.employees.createIndex({ department: 1 })

// Compound index
db.employees.createIndex({ department: 1, salary: -1 })

// Unique index
db.employees.createIndex({ emp_id: 1 }, { unique: true })

// Text index for text search
db.employees.createIndex({ emp_name: "text", job_role: "text" })

// View all indexes
db.employees.getIndexes()

// Explain query execution plan
db.employees.find({ department: "IT", salary: { $gt: 80000 } }).explain("executionStats")

// MongoDB vs MySQL comparison queries
// MySQL: SELECT department, AVG(salary) FROM Employee GROUP BY department HAVING COUNT(*) > 2;
// MongoDB equivalent:
db.employees.aggregate([
    { $group: { _id: "$department", avg_salary: { $avg: "$salary" }, count: { $sum: 1 } } },
    { $match: { count: { $gt: 2 } } }
])
```

## Expected Output

```
> db.employees.aggregate([ { $match: { department: "IT" } }, { $sort: { salary: -1 } } ])
[
    { "_id": "...", "emp_id": 2, "emp_name": "Priya Mehta", "salary": 109500, ... },
    { "_id": "...", "emp_id": 6, "emp_name": "Ananya Das", "salary": 93000, ... },
    { "_id": "...", "emp_id": 1, "emp_name": "Ravi Sharma", "salary": 87500, ... }
]

> db.employees.aggregate([
    { $group: { _id: "$department", avg_salary: { $avg: "$salary" }, employee_count: { $sum: 1 } } },
    { $sort: { avg_salary: -1 } }
])
[
    { "_id": "IT", "avg_salary": 96666.67, "employee_count": 3 },
    { "_id": "Finance", "avg_salary": 70000, "employee_count": 2 },
    { "_id": "Sales", "avg_salary": 72000, "employee_count": 1 },
    { "_id": "HR", "avg_salary": 50000, "employee_count": 1 }
]

> db.employees.aggregate([
    { $unwind: "$projects" },
    { $group: { _id: "$projects", employees: { $push: "$emp_name" }, count: { $sum: 1 } } },
    { $sort: { count: -1 } }
])
[
    { "_id": "ERP", "employees": ["Ravi Sharma", "Priya Mehta", "Sneha Kapoor", "Ananya Das"], "count": 4 },
    { "_id": "CRM", "employees": ["Ravi Sharma", "Rohit Verma"], "count": 2 },
    { "_id": "Audit", "employees": ["Amit Joshi", "Sneha Kapoor"], "count": 2 },
    { "_id": "Data Migration", "employees": ["Priya Mehta"], "count": 1 },
    { "_id": "Cloud", "employees": ["Ananya Das"], "count": 1 },
    { "_id": "Wellness", "employees": ["Vikram Singh"], "count": 1 }
]

> db.employees.createIndex({ department: 1, salary: -1 })
{
    "createdCollectionAutomatically": false,
    "numIndexesBefore": 2,
    "numIndexesAfter": 3,
    "ok": 1
}

> db.employees.getIndexes()
[
    { "v": 2, "key": { "_id": 1 }, "name": "_id_" },
    { "v": 2, "key": { "department": 1 }, "name": "department_1" },
    { "v": 2, "key": { "department": 1, "salary": -1 }, "name": "department_1_salary_-1" },
    { "v": 2, "key": { "emp_id": 1 }, "name": "emp_id_1", "unique": true },
    { "v": 2, "key": { "_fts": "text", "_ftsx": 1 }, "name": "emp_name_text_job_role_text" }
]
```

## MongoDB vs MySQL: When to Use Each

| Criteria                    | MySQL (Relational)                          | MongoDB (Document)                             |
|-----------------------------|---------------------------------------------|-----------------------------------------------|
| Schema                      | Fixed, requires migrations                  | Flexible, schema-less                         |
| Relationships               | Complex JOINs, referential integrity        | Embedding or referencing                      |
| Transactions                | Full ACID support                           | Multi-document ACID (v4.0+)                   |
| Query Complexity            | Rich SQL with joins, subqueries             | Aggregation pipeline, limited joins           |
| Scalability                 | Vertical (master-slave replication)         | Horizontal (auto-sharding)                    |
| Data Structure              | Highly normalized                           | Denormalized, self-contained documents        |
| Best For                    | Structured data, reporting, financial apps  | Rapid prototyping, hierarchical data, IoT     |
| Employee DB Example         | Normalized: Employee, Dept, Project tables  | Single collection with embedded arrays/skills |

## Homework / Practice

1. Write an aggregation pipeline to find the total salary expense for each job role, sorted by total expense descending.
2. Create a compound index on (department, status, salary) and verify it using getIndexes().
3. Convert the following MySQL query to a MongoDB aggregation pipeline: SELECT department, job_role, COUNT(*) FROM Employee GROUP BY department, job_role HAVING COUNT(*) > 1.
