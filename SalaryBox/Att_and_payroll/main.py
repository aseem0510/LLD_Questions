# main.py

from datetime import datetime, timedelta, date
from employees import Employee
from attendance import Attendance, AttendanceManagement
from payroll import PayrollManagement

if __name__ == "__main__":
    am = AttendanceManagement()
    pm = PayrollManagement(am)

    # Add employee
    emp1 = Employee(1, "Alice", "alice@gmail.com", 3000, "Developer", date(2023, 1, 15))
    am.add_employee(emp1)
    pm.add_employee(emp1)

    # Simulate attendance for 30 days (July 2025)
    base_date = datetime(2025, 7, 1)
    for i in range(30):
        curr_date = (base_date + timedelta(days=i)).strftime("%Y-%m-%d")
        key = f"{emp1.emp_id}_{curr_date}"
        att = Attendance(emp1.emp_id, curr_date)

        if i in [5, 12]:  # Leave days
            pass
        elif i in [10, 20]:  # Absent
            att.add_punch_in("09:00:00")
            att.add_punch_out("15:00:00")
        else:
            att.add_punch_in("09:00:00")
            att.add_punch_out("18:30:00")  # Present (9.5 hrs)

        am.attendance[key] = att

    # View attendance
    am.view_attendance(emp1.emp_id)

    # Generate and print payslip
    payslip = pm.generate_payslip(emp1.emp_id, 7, 2025)
    print("\nPayslip:", payslip)
