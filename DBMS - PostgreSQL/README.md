# Database Management & SQL – Learning Notes

This repository documents my learning journey in Database Management Systems (DBMS), database concepts, SQL, relational and NoSQL databases, database design, normalization, queries, joins, functions, indexing, transactions, and PostgreSQL.

# 1. Database Fundamentals

## 1.1 Data
Data refers to raw facts and figures that have not yet been processed or organized. Examples include names, numbers, dates, marks, and employee IDs.

## 1.2 Information
Information is processed and organized data that has meaning and provides useful insights. For example, calculating the average marks of students from their individual marks produces information.

## 1.3 Database
A database is an organized collection of data stored electronically so that it can be easily accessed, managed, updated, and retrieved.

## 1.4 DBMS (Database Management System)
A DBMS is software that allows users and applications to create, store, retrieve, update, and manage databases. Examples include MySQL, PostgreSQL, Oracle, and Microsoft SQL Server.

## 1.5 Why Do We Need a DBMS?
A DBMS helps manage large amounts of data efficiently while reducing duplication and maintaining consistency. It also provides security, data sharing, backup, recovery, and controlled access.

## 1.6 Advantages of DBMS
- Reduces unnecessary data duplication.
- Improves data consistency and accuracy.
- Provides security and access control.
- Supports backup and recovery.
- Allows multiple users to access data.
- Maintains data integrity.

## 1.7 Disadvantages of DBMS
- Can be expensive to develop and maintain.
- Requires technical knowledge and trained professionals.
- Needs storage, memory, and computing resources.
- Database failures can affect multiple applications.
- Complex databases may require significant administration.

# 2. Types of Databases

## 2.1 Hierarchical Database
A hierarchical database organizes data in a tree-like structure, where each child record has one parent. It follows a one-to-many relationship between parent and child records.

### Disadvantages of Hierarchical Database
- Difficult to represent many-to-many relationships.
- Changing the structure can be complicated.
- Data access is highly dependent on predefined paths.

## 2.2 Network Database
A network database organizes data using records connected through links or pointers. Unlike hierarchical databases, a child record can have multiple parent records, supporting many-to-many relationships.

## 2.3 Object-Oriented Database
An object-oriented database stores information as objects instead of traditional rows and columns. It supports object-oriented concepts such as classes, inheritance, and encapsulation.

## 2.4 Centralized Database
A centralized database stores and manages all data at a single central location or server. Users and applications access the database through this central system.

### Advantages of Centralized Database
- Easier administration and maintenance.
- Centralized security and access control.
- Better control over data consistency.
- Simplified backup and recovery.

### Disadvantages of Centralized Database
- Single point of failure.
- Heavy workload can affect performance.
- Users in distant locations may experience higher latency.
- Requires reliable network connectivity.

## 2.5 Distributed Database
A distributed database stores data across multiple interconnected locations or servers while allowing users to access it as one logical database.

### Advantages of Distributed Database
- Improved availability and fault tolerance.
- Data can be accessed from different geographical locations.
- Workloads can be distributed across servers.
- Can improve performance through local data access.

### Disadvantages of Distributed Database
- More complex management and maintenance.
- Data synchronization can be challenging.
- Requires additional security and coordination.
- Network failures can affect communication between locations.

## 2.6 Cloud Database
A cloud database is hosted on cloud infrastructure and accessed through the internet or private networks. It provides scalability, remote access, managed services, and flexible resource allocation.

## 2.7 In-Memory Database
An in-memory database stores data primarily in RAM instead of relying on disk storage for normal operations. This allows extremely fast data retrieval and processing.

### Why Do We Use In-Memory Databases?
- Useful for real-time applications.
- Provides low-latency data access.
- Suitable for caching, gaming, and live analytics.
- Handles frequent read and write operations efficiently.

### Problems with In-Memory Databases
- RAM is more expensive than traditional disk storage.
- Memory capacity is limited.
- Data may be lost if persistence and recovery mechanisms are not configured.
- Large datasets can become expensive to maintain.

## 2.8 Time-Series Database
A time-series database is designed to store and analyze data collected over time. Examples include server monitoring metrics, stock prices, temperature readings, and sensor data.

# 3. Relational and NoSQL Databases

## 3.1 Relational Database
A relational database stores data in tables consisting of rows and columns. Tables can be connected using primary keys and foreign keys.

## 3.2 NoSQL Database
NoSQL databases store data using flexible structures instead of relying exclusively on traditional relational tables. They are useful for large-scale applications, flexible data models, and distributed systems.

## 3.3 Relational Database vs NoSQL Database

| Relational Database | NoSQL Database |
|---|---|
| Stores data in tables | Uses different data models |
| Usually has a predefined schema | Often supports flexible schemas |
| Uses SQL | Uses database-specific query methods |
| Supports relationships through keys | Relationships may be handled differently |
| Commonly uses ACID transactions | Consistency and transactions depend on the database |
| Examples: MySQL, PostgreSQL | Examples: MongoDB, Redis, Neo4j |

## 3.4 Types of NoSQL Databases

### Key-Value Database
Stores data as key-value pairs, where each unique key identifies its associated value. Examples include Redis and Amazon DynamoDB.

### Document Database
Stores data in document formats such as JSON or BSON. Examples include MongoDB and Couchbase.

### Graph Database
Stores data using nodes, edges, and properties to represent relationships between entities. Examples include Neo4j and Amazon Neptune.

### Wide-Column Database
Stores data in rows with flexible column groupings rather than traditional fixed relational tables. Examples include Apache Cassandra and HBase.

# 4. OLTP, OLAP and Columnar Databases

## 4.1 OLTP (Online Transaction Processing)
OLTP systems handle frequent, small, real-time database transactions such as inserting orders, updating customer records, and processing payments.

## 4.2 OLAP (Online Analytical Processing)
OLAP systems are designed to analyze large amounts of historical data and perform complex queries for reporting, business intelligence, and decision-making.

## 4.3 OLTP vs OLAP

| OLTP | OLAP |
|---|---|
| Handles daily transactions | Handles analytical queries |
| Frequent INSERT, UPDATE, DELETE | Mostly complex SELECT queries |
| Current operational data | Historical and aggregated data |
| Fast individual transactions | Fast analytical processing |
| Example: Banking transactions | Example: Monthly sales analysis |

## 4.4 Columnar Database
A columnar database stores data by columns rather than storing complete rows together. It is useful for analytical workloads because queries can read only the required columns.

# 5. Relational Database Keys

Keys help uniquely identify records and establish relationships between database tables.

## 5.1 Primary Key
A primary key uniquely identifies each row in a table. It cannot contain NULL values or duplicate values.

## 5.2 Foreign Key
A foreign key is a column or group of columns that references a candidate key, usually the primary key, in another or the same table. It helps maintain referential integrity.

## 5.3 Super Key
A super key is any set of one or more columns that can uniquely identify a row in a table. It may contain additional unnecessary columns.

## 5.4 Maximum Super Key
A maximum or maximal super key is a super key that cannot have any additional attributes removed while remaining a super key only if it is minimal. The standard term for this is actually a candidate key; a super key that is not minimal may contain redundant attributes.

## 5.5 Possible Super Keys
Possible super keys are different combinations of columns that can uniquely identify records in a table. Every candidate key is a super key, but not every super key is a candidate key.

## 5.6 Candidate Key
A candidate key is a minimal super key that uniquely identifies each record. A table can have multiple candidate keys, but only one is selected as its primary key.

## 5.7 Alternate Key
An alternate key is a candidate key that is not selected as the primary key. It can still uniquely identify records.

## 5.8 Composite Key
A composite key consists of two or more columns that together uniquely identify a record. No individual column necessarily provides uniqueness.

## 5.9 Simple Key
A simple key consists of a single column that uniquely identifies a record.

## 5.10 Natural Key
A natural key is a key based on an existing real-world attribute, such as an email address or passport number.

## 5.11 Surrogate Key
A surrogate key is an artificially generated identifier that has no direct business meaning. Examples include auto-incrementing IDs and generated UUIDs.

## 5.12 Unique Key
A unique key constraint ensures that duplicate values are not allowed in a column or combination of columns. NULL handling depends on the database system.

## 5.13 Secondary Key
A secondary key is a column or combination of columns used to retrieve or search records based on attributes other than the primary key. It does not necessarily guarantee uniqueness.

# 6. ER Diagram (Entity Relationship Diagram)

An ER diagram is a visual representation of database entities, their attributes, and the relationships between them. It is used during database design to understand how data should be organized.

## 6.1 Entity
An entity is a real-world object or concept about which data is stored. Examples include Student, Employee, Department, and Product.

## 6.2 Strong Entity
A strong entity has its own primary key and can exist independently of other entities.

## 6.3 Weak Entity
A weak entity cannot be uniquely identified using its own attributes alone and depends on a strong entity for identification. It generally uses an identifying relationship and the owner's key.

## 6.4 Attribute
An attribute describes a property of an entity. For example, a Student entity may have Student_ID, Name, Age, and Email.

## 6.5 Composite Attribute
A composite attribute can be divided into smaller meaningful attributes. For example, Address can be divided into Street, City, State, and PIN Code.

## 6.6 Multivalued Attribute
A multivalued attribute can contain multiple values for a single entity. For example, one employee may have multiple phone numbers.

## 6.7 Derived Attribute
A derived attribute is calculated from another attribute instead of being directly stored. For example, Age can be calculated using Date of Birth.

## 6.8 Relationship
A relationship describes how two or more entities are associated with each other. For example, a Student enrolls in a Course.

# 7. Database Normalization

Normalization is the process of organizing database tables to reduce data duplication and prevent insertion, update, and deletion anomalies. It involves dividing large tables into smaller related tables while maintaining data integrity.

## 7.1 First Normal Form (1NF)
A table is in 1NF when every column contains atomic (indivisible) values and there are no repeating groups or multiple values stored in a single cell.

## 7.2 Second Normal Form (2NF)
A table is in 2NF when it is already in 1NF and every non-key attribute depends on the entire candidate key rather than only part of a composite candidate key.

## 7.3 Third Normal Form (3NF)
A table is in 3NF when it is already in 2NF and non-key attributes do not have inappropriate transitive dependencies on candidate keys.

## 7.4 Boyce-Codd Normal Form (BCNF)
BCNF is a stronger form of 3NF where every determinant must be a candidate key or super key. It helps eliminate certain types of redundancy that may remain in 3NF.

# 8. SQL (Structured Query Language)

SQL is a standard language used to communicate with relational databases. It allows users to create database structures, insert data, retrieve records, update information, and manage permissions.

# 9. SQL Data Types

Data types define the kind of values that can be stored in a database column.

## 9.1 Numeric Data Types

- **SMALLINT:** Stores small-range integer values.
- **INTEGER / INT:** Stores whole numbers without decimal places.
- **BIGINT:** Stores large-range integer values.
- **DECIMAL / NUMERIC:** Stores exact decimal values, commonly used for money and financial calculations.
- **FLOAT:** Stores approximate floating-point numbers.
- **DOUBLE PRECISION:** Stores approximate numbers with greater precision than typical single-precision floating-point values.

## 9.2 String Data Types

- **CHAR:** Stores fixed-length character strings.
- **VARCHAR:** Stores variable-length character strings with a defined maximum length.
- **TEXT:** Stores variable-length text, often used for longer content.

## 9.3 Date and Time Data Types

- **DATE:** Stores calendar dates.
- **TIME:** Stores time of day.
- **DATETIME:** Stores both date and time in databases that support this type, such as MySQL.
- **TIMESTAMP:** Stores date and time values; exact timezone and storage behavior depend on the database.

## 9.4 Boolean Data Type
BOOLEAN stores logical values such as TRUE and FALSE. Some database systems internally represent these values using other data types.

## 9.5 Binary Data Types

- **BINARY:** Stores fixed-length binary data.
- **VARBINARY:** Stores variable-length binary data.
- **BLOB (Binary Large Object):** Stores large binary objects such as images, audio, and documents.

## 9.6 Special Data Types

- **JSON / JSONB:** Stores structured JSON data; JSONB is PostgreSQL's binary-oriented JSON representation.
- **UUID:** Stores universally unique identifiers.
- **ARRAY:** Stores multiple values of the same element type in a single column in PostgreSQL.
- **INET:** Stores IPv4 or IPv6 network addresses in PostgreSQL.
- **ENUM:** Stores one value selected from a predefined set of values.
- **SET:** MySQL data type that allows multiple values from a predefined collection to be selected.

# 10. MySQL Data Types

MySQL provides data types for storing numbers, strings, dates, times, and binary information. Examples include INT, BIGINT, DECIMAL, FLOAT, DOUBLE, CHAR, VARCHAR, TEXT, DATE, DATETIME, TIMESTAMP, BLOB, ENUM, and SET.

# 11. SQL Constraints

Constraints are rules applied to database columns or tables to maintain data accuracy and integrity.

## 11.1 NOT NULL
Ensures that a column cannot contain NULL values. Every record must provide a value for that column.

## 11.2 UNIQUE
Ensures that values in a column or combination of columns are unique. It prevents duplicate values according to the database's NULL-handling rules.

## 11.3 PRIMARY KEY
Uniquely identifies every record in a table. It combines uniqueness and NOT NULL requirements.

## 11.4 CHECK
Ensures that inserted or updated values satisfy a specified condition. For example, Age must be greater than or equal to 18.

## 11.5 Referential Integrity
Ensures that relationships between tables remain valid through foreign key constraints. It prevents references to records that do not exist, subject to the configured actions.

## 11.6 DEFAULT
Automatically assigns a predefined value when no value is provided during insertion. For example, an employee's status can default to 'Active'.

# 12. SQL Command Categories

SQL commands are divided into different categories based on their purpose.

## 12.1 DDL (Data Definition Language)
DDL commands define and modify the structure of database objects such as tables and schemas.

- **CREATE:** Creates a new database object.
- **ALTER:** Modifies an existing database object.
- **DROP:** Permanently removes a database object.
- **TRUNCATE:** Removes all rows from a table while retaining its structure.

## 12.2 DML (Data Manipulation Language)
DML commands are used to insert, modify, and delete records stored in database tables.

- **INSERT:** Adds new records.
- **UPDATE:** Modifies existing records.
- **DELETE:** Removes selected records.

## 12.3 DQL (Data Query Language)
DQL is used to retrieve information from database tables.

- **SELECT:** Retrieves data from one or more tables.

## 12.4 DCL (Data Control Language)
DCL commands manage database permissions and access privileges.

- **GRANT:** Provides permissions to database users.
- **REVOKE:** Removes previously granted permissions.

## 12.5 TCL (Transaction Control Language)
TCL commands manage database transactions and control when changes become permanent.

- **COMMIT:** Permanently saves transaction changes.
- **ROLLBACK:** Reverses uncommitted transaction changes.
- **SAVEPOINT:** Creates a checkpoint within a transaction to which a partial rollback can be performed.

# 13. SQL CRUD Operations

CRUD represents the four basic operations performed on database records.

- **Create:** INSERT adds new records.
- **Read:** SELECT retrieves existing records.
- **Update:** UPDATE modifies existing records.
- **Delete:** DELETE removes records.

# 14. SQL SELECT Queries

## 14.1 SELECT Specific Columns
Retrieves only the requested columns instead of fetching every column from a table.

## 14.2 SELECT Multiple Columns
Retrieves two or more specified columns in a single query.

## 14.3 SELECT Single Column
Retrieves values from one particular column in a table.

## 14.4 SELECT with WHERE
Filters records based on a specified condition. Only rows satisfying the condition are returned.

## 14.5 SELECT DISTINCT
Returns unique values by eliminating duplicate rows from the selected result.

## 14.6 ORDER BY
Sorts query results in ascending (ASC) or descending (DESC) order.

## 14.7 LIMIT
Restricts the number of records returned by a query. It is useful for retrieving a limited number of results.

## 14.8 Column Aliases
Assigns temporary alternative names to columns or calculated expressions in query results using AS.

## 14.9 Calculations Using SELECT
Performs arithmetic operations directly inside SELECT statements without modifying the original database records.

## 14.10 SELECT with Functions
Uses built-in SQL functions to manipulate, calculate, or transform values while retrieving records.

## 14.11 SELECT with GROUP BY
Groups rows containing the same values in specified columns. It is commonly used with aggregate functions such as COUNT, SUM, AVG, MIN, and MAX.

## 14.12 SELECT with HAVING
Filters grouped results based on conditions applied after GROUP BY. Unlike WHERE, HAVING is commonly used to filter aggregated results.

## 14.13 SELECT with JOIN
Combines related records from two or more tables using matching columns or specified join conditions.

# 15. DCL Commands and Permissions

## 15.1 GRANT
GRANT provides specific database permissions to a user or role. Permissions can include SELECT, INSERT, UPDATE, and DELETE.

## 15.2 GRANT Multiple Permissions
Multiple permissions can be assigned to a user in one GRANT statement. This reduces the need to execute separate permission commands.

## 15.3 GRANT ALL PRIVILEGES
GRANT ALL PRIVILEGES provides all applicable privileges within the specified database object or scope. The exact permissions depend on the database system and the user's administrative privileges.

## 15.4 REVOKE
REVOKE removes permissions previously granted to a database user or role. It helps administrators control access to database resources.

## 15.5 REVOKE Multiple Permissions
Multiple permissions can be removed using a single REVOKE statement. This allows administrators to efficiently update user access.

# 16. TCL Commands and Transactions

## 16.1 COMMIT
COMMIT saves all changes made during the current transaction permanently.

## 16.2 ROLLBACK
ROLLBACK reverses changes made during the current uncommitted transaction.

## 16.3 SAVEPOINT
SAVEPOINT creates a named checkpoint within a transaction. ROLLBACK TO SAVEPOINT allows partial rollback without undoing the entire transaction.

# 17. SQL JOINs

JOINs combine records from multiple tables based on related columns or conditions.

## 17.1 INNER JOIN
Returns only records that have matching values in both tables.

## 17.2 LEFT JOIN / LEFT OUTER JOIN
Returns all records from the left table and matching records from the right table. Unmatched right-side columns contain NULL values.

## 17.3 RIGHT JOIN / RIGHT OUTER JOIN
Returns all records from the right table and matching records from the left table. Unmatched left-side columns contain NULL values.

## 17.4 FULL OUTER JOIN
Returns all records from both tables, including matching and non-matching records. Missing matches are represented using NULL values.

## 17.5 CROSS JOIN
Returns the Cartesian product of two tables, combining every row from the first table with every row from the second table.

## 17.6 SELF JOIN
Joins a table with itself using aliases. It is useful for representing relationships such as employees and their managers.

## 17.7 NATURAL JOIN
Automatically joins two tables using columns that have the same names and compatible data types. It should be used carefully because unintended same-named columns can affect the result.

# 18. SQL Functions

SQL functions perform operations on values and return calculated results.

## 18.1 String Functions
String functions manipulate text values. Examples include UPPER(), LOWER(), LENGTH(), CONCAT(), SUBSTRING(), TRIM(), and REPLACE().

## 18.2 Numeric Functions
Numeric functions perform mathematical operations on numerical values. Examples include ROUND(), CEIL(), FLOOR(), ABS(), MOD(), and POWER().

## 18.3 Date Functions
Date functions work with date and time values. Examples include CURRENT_DATE, CURRENT_TIMESTAMP, EXTRACT(), and date arithmetic functions.

## 18.4 Conditional Functions
Conditional functions return results based on specified conditions. Examples include CASE WHEN and database-specific functions such as IF() in MySQL.

## 18.5 COALESCE
COALESCE returns the first non-NULL value from a list of expressions. It is commonly used to replace missing values with meaningful defaults.

# 19. SQL Subqueries

A subquery is a query written inside another SQL query. It allows the result of one query to be used by another query for filtering, calculations, or data retrieval.

## 19.1 Scalar Subquery
A scalar subquery returns exactly one value, usually one row and one column. It can be used in SELECT, WHERE, or other expressions that expect a single value.

## 19.2 Single-Row Subquery
A single-row subquery returns at most one row and can return multiple columns. It is commonly used with comparison operators such as =, >, and <.

## 19.3 Multiple-Row Subquery
A multiple-row subquery returns more than one row. It is commonly used with IN, ANY, and ALL operators.

## 19.4 Correlated Subquery
A correlated subquery depends on values from the outer query and is logically evaluated for each relevant outer row.

## 19.5 Non-Correlated Subquery
A non-correlated subquery does not depend on the outer query. It can execute independently and its result is used by the outer query.

## 19.6 Why Use Correlated Subqueries?
Correlated subqueries are useful when a calculation or condition must be evaluated separately for each outer record. For example, finding employees whose salary is greater than the average salary of their own department.

## 19.7 Subquery in WHERE
A subquery inside WHERE filters records based on the result of another query. It can use operators such as IN, EXISTS, and comparison operators.

## 19.8 Subquery in FROM
A subquery inside FROM creates a derived table that can be queried like a regular table. It is useful for organizing intermediate results.

## 19.9 Subquery in SELECT
A subquery inside SELECT calculates an additional value for each returned row. It is often used for scalar calculations and comparisons.

## 19.10 Subquery in JOIN
A subquery can be used as a derived table in a JOIN operation. It helps combine a main table with pre-filtered or aggregated query results.

## 19.11 Nested Subquery
A nested subquery is a query placed inside another subquery, creating multiple levels of query execution. It is useful for solving complex data retrieval problems.

# 20. Logical Operators in SQL

Logical operators combine or modify conditions in SQL queries.

- **AND:** Returns records when all specified conditions are TRUE.
- **OR:** Returns records when at least one specified condition is TRUE.
- **NOT:** Reverses the result of a condition.

# 21. Database Indexing

Indexing is a technique used to improve the speed of data retrieval by creating an additional data structure that helps locate records efficiently. However, indexes require additional storage and can slow down INSERT, UPDATE, and DELETE operations.

## 21.1 B-Tree Index
A B-Tree index organizes values in a balanced tree structure. It supports equality searches, range queries, and sorting efficiently.

## 21.2 Hash Index
A hash index uses a hash function to locate values quickly. It is mainly useful for equality comparisons and generally does not support range queries efficiently.

## 21.3 Unique Index
A unique index ensures that indexed values or combinations of values remain unique. It prevents duplicate entries in the indexed columns.

## 21.4 Composite Index
A composite index is created on two or more columns. It improves queries that filter or sort using the indexed columns in an appropriate order.

## 21.5 Clustered Index
A clustered index determines how table data is physically or logically organized according to the database's storage implementation. A table generally has one clustered organization.

## 21.6 Non-Clustered Index
A non-clustered index stores a separate index structure containing indexed values and references to the corresponding table records. A table can have multiple non-clustered indexes.

## 21.7 Partial / Filtered Index
A partial index indexes only records that satisfy a specified condition. In PostgreSQL, this is called a partial index and can reduce index size when only certain rows are frequently queried.

## 21.8 Single-Column Index
A single-column index is created on one table column. It improves queries that frequently search or sort using that column.

## 21.9 Primary Key Index
A primary key is supported by an index to enforce uniqueness and enable efficient record lookups. In PostgreSQL, defining a primary key automatically creates a unique B-tree index by default.

# 22. SQL Views

A view is a virtual table created using the result of a SELECT query. It helps simplify complex queries, control data access, and present selected information without necessarily storing a separate copy of the data.

## 22.1 Creating a View
CREATE VIEW creates a named virtual table based on a SELECT statement. Users can query it like a regular table.

## 22.2 Deleting a View
DROP VIEW removes an existing view from the database. It does not automatically delete the underlying tables or their records.

# 23. Database Transactions

A transaction is a group of database operations treated as a single logical unit of work. It ensures that related operations are completed successfully or rolled back when necessary.

## 23.1 ACID Properties

### Atomicity
Ensures that all operations in a transaction succeed together or none of them are applied. Partial transaction completion is avoided.

### Consistency
Ensures that a transaction moves the database from one valid state to another while maintaining defined integrity rules.

### Isolation
Ensures that concurrent transactions do not interfere with one another in ways that violate the configured isolation level.

### Durability
Ensures that committed transaction changes survive system failures, using mechanisms such as transaction logs and recovery.

# 24. Database Schema

A schema defines the logical structure and organization of a database. It includes database objects such as tables, columns, relationships, views, and constraints.

## 24.1 Types of Database Schemas

### Physical Schema
Describes how data is physically stored, including files, indexes, storage structures, and access methods.

### Logical Schema
Describes the logical organization of data, including tables, attributes, relationships, and constraints.

### External Schema
Describes how individual users or applications view and access specific parts of the database.

# 25. Database Permissions and Security

Database security protects stored information against unauthorized access, modification, and deletion. It uses authentication, authorization, roles, privileges, encryption, and auditing to protect database resources.

# 26. Triggers

A trigger is a database object that automatically executes a specified function or action when a particular database event occurs. Triggers are useful for auditing, enforcing business rules, and maintaining data consistency.

## 26.1 Three Main Trigger Events

### INSERT Trigger
Executes when new records are inserted into a table. It can be used to record new entries in an audit log.

### UPDATE Trigger
Executes when existing records are modified. It can track changes or maintain related information.

### DELETE Trigger
Executes when records are deleted from a table. It can maintain deletion logs or perform related operations.

# 27. Functional Dependency

Functional dependency describes a relationship between attributes in a database table where one attribute or group of attributes determines another attribute.

For example, Student_ID → Student_Name means that a Student_ID uniquely determines the corresponding Student_Name.

Functional dependencies are important in identifying candidate keys and performing database normalization.

# 28. PostgreSQL

PostgreSQL is an open-source relational database management system known for reliability, extensibility, and strong SQL support. It supports relational data, JSON/JSONB, arrays, UUIDs, custom data types, indexing, transactions, and advanced querying.

## 28.1 Features of PostgreSQL
- Open-source and highly extensible.
- Supports ACID-compliant transactions.
- Supports primary keys, foreign keys, and constraints.
- Provides advanced indexing techniques.
- Supports JSON and JSONB data.
- Supports complex queries, joins, and subqueries.
- Provides functions, triggers, and stored procedures.
- Supports concurrent database access through MVCC (Multi-Version Concurrency Control).

---

## Learning Goals

Through these topics, I aim to understand:

- Database fundamentals and database architecture.
- Relational and NoSQL database models.
- Database design using ER diagrams and normalization.
- SQL commands and CRUD operations.
- Joins, functions, subqueries, and indexing.
- Transactions, ACID properties, and database security.
- PostgreSQL concepts and practical database operations.

**Note:** These are learning notes and conceptual explanations. Practical SQL examples, exercises, and implementation details can be added as I progress.