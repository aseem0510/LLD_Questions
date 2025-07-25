### LLD ###

# 1. Functional and Non-Functional Requirements

# Functional Requirements
1. Employee Management
  * Add employees to the system.
2. Attendance Punching
  * Employees can punch in and punch out any number of times per day.
  * Each punch-in and punch-out is timestamped.
3. Attendance Viewing
  * Employees (or admin) can view their attendance for any day.
  * The first punch-in is considered the entry time, and the last punch-out is the exit time for the day.
  * All punch-in and punch-out times are visible for audit.

# Non-Functional Requirements
1. Reliability: Attendance data must be accurately recorded and retrievable.
2. Scalability: Should support many employees and high-frequency punching.
3. Performance: Punching and viewing attendance should be fast (real-time).
4. Usability: Simple interface for punching and viewing.
5. Extensibility: Easy to add features like reporting, authentication, or admin roles.
6. Data Integrity: No data loss or corruption, even with rapid or repeated punches.

# 3. SOLID Principles & Design Patterns Used

# SOLID Principles
* Single Responsibility Principle (SRP):
  - "Employee" handles employee data only.
  - "Attendance" handles attendance records for a single employee on a single day.
  - "AttendanceManagement" manages the overall system and coordinates between employees and attendance records.
* Open/Closed Principle (OCP):
  - Classes can be extended (e.g., add new attendance features) without modifying existing code.
* Liskov Substitution Principle (LSP):
  - If you subclass " Employee" (e.g., for Admin), it will work wherever "Employee" is used
* Interface Segregation Principle (ISP):
  - Not directly shown, but each class exposes only relevant methods.
* Dependency Inversion Principle (DIP):
  - High-level module ("AttendanceManagement") depends on abstractions (" Employee"", "Attendance"), not on concrete implementations.

# Design Patterns
* Factory Pattern (Potential):
  - Could be used for creating "Employee" or "Attendance" objects, though not explicity implemented here.
* Singleton Pattern (Potential):
  - "AttendanceManagement" could be made a singleton to ensure only one instance manages the system.
* Composition:
  - "AttendanceManagement" composes 'Employee' and "Attendance' objects.


------------------------------------------------------------------------------------------------------------------------------------------------

### HLD ###

# 1. Functional Requirements
1. Employee Registration & Management
  * Add, update, and view employee details.
2. Attendance Punching
  * Employees can punch in and punch out any number of times per day.
  * Each punch is timestamped and stored.
3. Attendance Viewing
  * Employees and admins can view attendance records.
  * System shows first punch-in as entry and last punch-out as exit for the day.
  * All punch-in and punch-out times are visible.
4. (Optional for HLD) Authentication
  * Secure login for employees and admins.

# 2. Non-Functional Requirements
* Reliability: Accurate and consistent attendance data.
* Scalability: Support for thousands of employees and high-frequency punching.
* Performance: Real-time punch and view operations (<1s latency).
* Security: Secure access to attendance data.
* Availability: 99.9% uptime.
* Extensibility: Easy to add features (e.g., reporting, leave management).
* Auditability: All punches are logged and auditable.

# 3. Capacity Estimation (High Level)
* Employees: 10,000 (scalable to 100,000)
* Punches per day per employee: 10 (max)
* Total punches per day: 100,000 (10,000 x 10)
* Attendance records per year: ~36.5 million (100,000 x 365)
* Data size per punch: ~200 bytes (with metadata)
* Annual storage: ~7.3 GB (36.5M x 200 bytes)

# 4. Database Choice: SQL vs NoSQL

# SQL (Relational Database)

# Why Choose SQL:
* Strong Consistency: Attendance data must be accurate and consistent.
* Relational Data: Employees and attendance records have clear relationships (one-to-many)-
* ACID Transactions: Ensures no lost or duplicate punches.
* Structured Queries: Easy to generate reports, filter by date/employee, etc.
* Mature Ecosystem: Tools for backup, scaling, and security.

# Why Not NoSQL:
* NoSQL is better for unstructured, schema-less, or highly distributed data.
* Attendance data is structured and relational.
* NoSQL eventual consistency is not ideal for attendance (risk of data loss or duplication).
# Recommended DB: SQL (e.g., PostgreSQL, MySQL)

# 6. APIs

# Employee APis
- POST /employees- Add employee
- GET /employees/{id} - Get employee details
# Attendance APis
- POST /attendance/punch-in - Punch in (body: employee_id)
- POST /attendance/punch-out - Punch out (body: employee_id)
- GET /attendance/{employee_id}/{date} - Get attendance for a day
- GET /attendance/{employee_id} - Get all attendance for employee
