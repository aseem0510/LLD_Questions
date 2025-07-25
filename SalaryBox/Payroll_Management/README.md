### LLD ###

# 1. Functional and Non-Functional Requirements

# Functional Requirements
* Add/Edit/Delete Employee details
* Mark attendance (present/absent/leave)
* Calculate monthly salary (based on attendance, leaves, overtime, deductions, bonuses)
* Generate payslip for employees
* View/download payslip
* Admin authentication

# Non-Functional Requirements
* Scalability: Should handle increasing number of employees
* Security: Sensitive data (salary, personal info) must be protected
* Performance: Payslip generation should be quick
* Maintainability: Code should be modular and easy to update
* Usability: Simple and intuitive interface

# 3. SOLID Principles Used
* Single Responsibility: Each class has a single responsibility (Employee handles employee data, Attendance handles attendance, etc.)
* Open/Closed: Classes can be extended (e.g., new salary calculation logic) without modifying existing code.
* Liskov Substitution: If you extend Employee (e.g., for different roles), subclasses can replace base class.
* Interface Segregation: Not directly shown, but methods are grouped logically.
* Dependency Inversion: High-level modules (Payroll) depend on abstractions, not concrete classes.

# 4. Design Pattern Used
* Factory Pattern: For creating Payslip objects.
* Singleton Pattern: For Payroll manager (if needed, to ensure only one instance manages the system).


------------------------------------------------------------------------------------------------------------------------------------------------

### HLD ###

# 1. Functional Requirements
* Employee Management: Add, update, delete, and view employee details.
* Attendance Management: Mark and view daily attendance (present/absent/leave).
* Payroll Calculation: Calculate monthly salary based on attendance, leaves, deductions, and bonuses.
* Payslip Generation: Generate and download payslips for employees.
* Authentication & Authorization: Secure login for admin and employees.
* Reporting: View/download reports (attendance, salary, etc.).

# 2. Non-Functional Requirements
* Scalability: Should support thousands of employees and concurrent users.
* Security: Protect sensitive data (salary, personal info) with encryption and access control.
* Performance: Payslip generation and data retrieval should be fast (<1s for typical queries).
* Availability: System should be available 99.9% of the time.
* Maintainability: Modular codebase for easy updates and bug fixes.
* Usability: Simple, intuitive Ul for both admins and employees.
* Auditability: All changes (salary, attendance, etc.) should be logged.

# 3. Capacity Estimation (High Level)
* Employees: 10,000 (assume for a mid-sized company)
* Attendance Records: 10,000 employees × 365 days = 3.65 million records/year
* Payslips: 10,000 employees × 12 months = 120,000 payslips/year
* API Requests: Peak 100 requests/sec (for attendance marking, payslip viewing, etc.)
* Storage: Each record (employee, attendance, payslip) ~1KB - ~4GB/year (excluding backups, logs, etc.)

# 4. Database Choice: SQL vs NoSQL

# Choose: SQL (Relational Database, e.g., PostgreSQL/MySQL)

# Reasons for SOL:
* Strong Data Consistency: Payroll and attendance require ACID transactions (e.g. salary calculation must be accurate and consistent).
* Structured Data: Employee, attendance, and payslip data are highly structured and relational.
* Complex Queries: SQL supports complex joins and aggregations (e.g. monthly salary, attendance reports).
* Referential Integrity: Foreign key constraints ensure data integrity (e.g.. attendance must reference a valid employee).
* Reporting: SQL is better for generating reports and analytics.

# Why Not NoSQL:
* NoSQL (e.g., MongoDB, Cassandra) is better for unstructured, rapidly changing, or massive scale data (e.g., logs, social feeds). Here, the data is structured and relationships are important.
* Eventual Consistency in NoSQL is not suitable for payroll, where accuracy is critical.

# 6. APIs

# Employee APIs
* POST /employees - Add employee
* GET /employees/{id} - Get employee details
* PUT /employees/{id} — Update employee
* DELETE /employees/{id} -Delete employee

# Attendance APIs
* POST /attendance - Mark attendance
* GET "/attendance?emp_id=&month=&year=" - Get attendance records

# Payslip APls
* POST /payslips/generate — Generate payslip for employee/month
* GET /payslips/{id} - Get payslip details
* GET "/payslips?emp_id=&month=&year=" - List payslips

# Auth APis
* POST /login - Login (admin/employee)
* POST /logout - Logout
