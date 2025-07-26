### LLD ###

# Functional Requirements
* Employee Management
  - Add employee
  - Store employee details
* Attendance Management
  - Record punch-in and punch-out
  - Compute attendance summary (Present, Leave, Absent) based on working hours
* Payroll Management
  - Calculate salary using attendance data
  - Apply bonus for full month attendance
  - Apply deductions for absent days
  - Generate payslip

# Non-Functional Requirements
- Performance: Efficient attendance lookup using dictionary (hashmap)
- Modularity:	Clear separation: Models, Attendance, Payroll, Main
- Scalability: Can be extended to include DB or APIs later
- Maintainability: Easy to modify working hours or bonus/deduction logic
- Readability: Follows clean OOP structure
- Extensibility: Can support overtime, shifts, multiple roles, etc.

# UML/Class Diagram
🟨 = class, solid arrow = composition/has-a

- +-------------------+           +------------------------+
|    Employee       |<----------|   AttendanceManagement |
+-------------------+           +------------------------+
| - emp_id: int     |           | - employees: dict      |
| - name: str       |           | - attendance: dict     |
| - email: str      |           +------------------------+
| - base_salary: float          | +add_employee(emp)     |
| - role: str       |           | +punch_in(emp_id)      |
| - join_date: date |           | +punch_out(emp_id)     |
+-------------------+           | +get_attendance_summary|
                                | +view_attendance()     |
                                +-----------+------------+
                                            |
                                            |
                                            v
                                +------------------------+
                                |      Attendance        |
                                +------------------------+
                                | - employee_id: int     |
                                | - date: str            |
                                | - punch_ins: list      |
                                | - punch_outs: list     |
                                +------------------------+
                                | +add_punch_in(time)    |
                                | +add_punch_out(time)   |
                                | +get_entry_exit()      |
                                +------------------------+

+------------------------+
|   PayrollManagement    |<--------+
+------------------------+         |
| - employees: dict               |
| - payslips: list                |
| - payslip_counter: int          |
+------------------------+        |
| +add_employee(emp)             |
| +calculate_salary(emp_id,...)  |
| +generate_payslip(...)         |
+-----------+--------------------+
            |
            v
+------------------------+
|       Payslip          |
+------------------------+
| - payslip_id           |
| - emp_id               |
| - month, year          |
| - basic, deductions    |
| - bonus, net_pay       |
+------------------------+
| +calculate_net_pay()   |
| +generate_payslip()    |
+------------------------+

# SOLID Principles Used
- S - SRP: Each class has a single responsibility: Employee, Attendance, Payroll
- O - OCP: Salary/bonus logic can be extended without modifying base class
- L - LSP: Not explicitly violated (no inheritance hierarchy)
- I - ISP: Not yet needed (few interfaces exist)
- D - DIP: PayrollManagement depends on abstraction of AttendanceManagement logic

# Design Patterns Used
- Composition: PayrollManagement and AttendanceManagement use Employee and Attendance
- Factory (implicit): Payslip generation acts like a factory method: generate_payslip()
- Strategy (optional): If salary computation were extracted (e.g., bonus rules), it could use this

# Potential Future Enhancements (Extensibility)
- Strategy Pattern: for different salary calculation rules (e.g., hourly vs monthly)
- Observer Pattern: notify employee after payslip generation
- DAO Layer: for persistence in DB (separation of storage and business logic)
- REST API: expose functions for frontend or integration


------------------------------------------------------------------------------------------------------------------------------------------------

### HLD ###

# 1. Functional Requirements
- Employee Module: Add, update, view employee details
- Attendance Module: Punch in/out, track multiple entries per day, view attendance history
- Payroll Module: Calculate salary, apply bonus/deductions, generate payslip
- Admin/HR Features: View reports, trigger monthly salary processing, employee-wise reports

# 2. Non-Functional Requirements
- Scalability: Should support hundreds/thousands of employees and millions of attendance logs
- Performance: Payroll generation within seconds for 1,000+ employees
- Reliability: No data loss for attendance/payslip generation
- Auditability: Historical records for employee attendance and salaries
- Security: Access control for HR/Admin vs Employees
- Maintainability: Modular code, easy to plug-in REST APIs or DB

# 3. Capacity Estimation (Light)
- Employees: ~1,000
- Attendance logs: 1,000 employees × 30 days × 12 months = ~360,000 records/year
- Payslips: 1,000 per month → ~12,000 per year
- Punch-ins/outs: Avg 2–3 per day × 1,000 = ~60,000/month

# Conclusion: A relational DB can easily handle this volume with indexing.

# 4. DB Choice — SQL vs NoSQL
<img width="705" height="383" alt="image" src="https://github.com/user-attachments/assets/e4ba07a8-b9bd-4c5d-b38a-3b25d9517183" />

<img width="347" height="591" alt="image" src="https://github.com/user-attachments/assets/f59d115c-d521-464b-acc5-fc5fd66a02b8" />

<img width="830" height="607" alt="image" src="https://github.com/user-attachments/assets/30a67cd8-cdd1-4eb9-b3c9-ea86d5e9ebdb" />

<img width="637" height="597" alt="image" src="https://github.com/user-attachments/assets/4b069eb6-b6ad-400f-82ed-d7e57733e920" />


