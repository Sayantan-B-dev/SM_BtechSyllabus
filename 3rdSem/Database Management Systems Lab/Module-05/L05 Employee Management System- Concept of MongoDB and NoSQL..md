# Employee Management System- Concept of MongoDB and NoSQL.

**Course:** Database Management Systems Lab  
**Module:** 5 | **Lecture:** 5  
**Date:** 02-Nov-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand NoSQL databases and MongoDB fundamentals.
- Perform CRUD operations in MongoDB: insertOne(), find(), updateOne(), deleteOne().
- Compare the Employee collection in MongoDB vs the Employee table in MySQL.

## Theory / Concept

NoSQL databases are non-relational, designed for flexible schemas, horizontal scaling, and handling large volumes of unstructured data. MongoDB is a document-oriented NoSQL database where data is stored as BSON documents (similar to JSON) in collections (analogous to tables in MySQL). Documents are flexible -- each document can have different fields. CRUD operations in MongoDB use methods like insertOne(), find(), updateOne(), and deleteOne().

## SQL Code

```javascript
// MongoDB shell commands for Employee Management

// Switch to EmployeeDB database (created automatically on first use)
use EmployeeDB

// CRUD Operation 1: CREATE (insertOne - single document)
db.employees.insertOne({
    emp_id: 1,
    emp_name: "Ravi Sharma",
    email: "ravi.sharma@company.com",
    phone: "9000000001",
    department: "IT",
    job_role: "Software Engineer",
    salary: 87500.00,
    hire_date: new Date("2020-06-15"),
    skills: ["Java", "SQL", "Python"],
    address: {
        street: "123 Tech Park",
        city: "New York",
        zip: "10001"
    },
    status: "Active"
})

// CRUD Operation 2: CREATE (insertMany - multiple documents)
db.employees.insertMany([
    {
        emp_id: 2,
        emp_name: "Priya Mehta",
        email: "priya.mehta@company.com",
        department: "IT",
        job_role: "Senior Developer",
        salary: 109500.00,
        hire_date: new Date("2018-03-01"),
        skills: ["Java", "Spring", "Microservices"],
        status: "Active"
    },
    {
        emp_id: 3,
        emp_name: "Amit Joshi",
        email: "amit.joshi@company.com",
        department: "Finance",
        job_role: "Accountant",
        salary: 55000.00,
        hire_date: new Date("2021-09-10"),
        skills: ["Accounting", "Excel", "Tally"],
        status: "Active"
    }
])

// CRUD Operation 3: READ (find all documents)
db.employees.find()

// READ with pretty print
db.employees.find().pretty()

// READ with filter
db.employees.find({ department: "IT" })

// READ with projection (select specific fields)
db.employees.find(
    { department: "IT" },
    { emp_name: 1, job_role: 1, salary: 1, _id: 0 }
)

// READ - find one document
db.employees.findOne({ emp_id: 1 })

// CRUD Operation 4: UPDATE (updateOne)
db.employees.updateOne(
    { emp_name: "Ravi Sharma" },
    { $set: { salary: 92000.00 } }
)

// UPDATE with multiple fields
db.employees.updateOne(
    { emp_id: 3 },
    {
        $set: { job_role: "Senior Accountant", salary: 65000.00 },
        $push: { skills: "Financial Analysis" }
    }
)

// UPDATE - increment operator
db.employees.updateOne(
    { emp_name: "Priya Mehta" },
    { $inc: { salary: 5000 } }
)

// CRUD Operation 5: DELETE (deleteOne)
db.employees.deleteOne({ emp_name: "Amit Joshi" })

// DELETE many
db.employees.deleteMany({ status: "Resigned" })

// Verify remaining documents
db.employees.find().pretty()
print("Total employees:", db.employees.countDocuments())
```

## Expected Output

```
> use EmployeeDB
switched to db EmployeeDB

> db.employees.insertOne({ ... })
{
    "acknowledged": true,
    "insertedId": ObjectId("672a1b2c3d4e5f6a7b8c9d0e")
}

> db.employees.find({ department: "IT" }, { emp_name: 1, job_role: 1, salary: 1, _id: 0 })
[
    { "emp_name": "Ravi Sharma", "job_role": "Software Engineer", "salary": 87500 },
    { "emp_name": "Priya Mehta", "job_role": "Senior Developer", "salary": 109500 }
]

> db.employees.findOne({ emp_id: 1 })
{
    "_id": ObjectId("..."),
    "emp_id": 1,
    "emp_name": "Ravi Sharma",
    "email": "ravi.sharma@company.com",
    "phone": "9000000001",
    "department": "IT",
    "job_role": "Software Engineer",
    "salary": 87500,
    "hire_date": ISODate("2020-06-15T00:00:00Z"),
    "skills": [ "Java", "SQL", "Python" ],
    "address": { "street": "123 Tech Park", "city": "New York", "zip": "10001" },
    "status": "Active"
}

> db.employees.updateOne({ emp_name: "Ravi Sharma" }, { $set: { salary: 92000 } })
{
    "acknowledged": true,
    "matchedCount": 1,
    "modifiedCount": 1
}

> db.employees.deleteOne({ emp_name: "Amit Joshi" })
{ "acknowledged": true, "deletedCount": 1 }

> print("Total employees:", db.employees.countDocuments())
Total employees: 3
```

## Comparison: MySQL vs MongoDB

| Feature              | MySQL (Employee Table)              | MongoDB (employees Collection)            |
|----------------------|-------------------------------------|-------------------------------------------|
| Schema               | Fixed, predefined columns            | Flexible, documents can vary               |
| Data Format          | Rows with columns                    | BSON documents (JSON-like)                |
| Relationships        | Foreign keys, JOINs                  | Embedded documents or references           |
| Query Language       | SQL                                  | MongoDB Query Language (JSON-based)       |
| Scalability          | Vertical scaling primarily           | Horizontal scaling (sharding)             |
| Schema Changes       | ALTER TABLE required                 | Collections accept varied fields naturally |
| Example: Skills      | Separate table or concatenated string| Array field within document                |
| Example: Address     | Separate columns                     | Embedded document                          |

## Homework / Practice

1. Insert 5 employee documents into MongoDB with varying fields (some with address, some with skills array).
2. Write a query to find all employees with salary greater than 80000.
3. Update all employees in the IT department to add a new skill "MongoDB" to their skills array using updateMany().
