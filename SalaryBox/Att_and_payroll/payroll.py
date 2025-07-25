# payroll.py

from employees import Employee
from attendance import AttendanceManagement

class Payslip:
    def __init__(self, payslip_id, emp_id, month, year, basic, deductions, bonus):
        self.payslip_id = payslip_id
        self.emp_id = emp_id
        self.month = month
        self.year = year
        self.basic = basic
        self.deductions = deductions
        self.bonus = bonus
        self.net_pay = self.calculate_net_pay()

    def calculate_net_pay(self):
        return self.basic + self.bonus - self.deductions

    def generate_payslip(self):
        return {
            "payslip_id": self.payslip_id,
            "emp_id": self.emp_id,
            "month": self.month,
            "year": self.year,
            "basic": self.basic,
            "deductions": self.deductions,
            "bonus": self.bonus,
            "net_pay": self.net_pay
        }

class PayrollManagement:
    def __init__(self, attendance_manager: AttendanceManagement):
        self.employees = {}
        self.attendance_manager = attendance_manager
        self.payslips = []
        self.payslip_counter = 1

    def add_employee(self, emp: Employee):
        self.employees[emp.emp_id] = emp

    def calculate_salary(self, emp_id, month, year):
        if emp_id not in self.employees:
            raise ValueError("Employee not found")

        emp = self.employees[emp_id]
        total_days = 30
        present, leave, absent = self.attendance_manager.get_attendance_summary(emp_id, month, year)

        per_day_salary = emp.base_salary / total_days
        deductions = absent * per_day_salary
        bonus = 0
        if present + leave == total_days:
            bonus = emp.base_salary * 0.1

        return emp.base_salary, deductions, bonus

    def generate_payslip(self, emp_id, month, year):
        basic, deductions, bonus = self.calculate_salary(emp_id, month, year)
        payslip = Payslip(self.payslip_counter, emp_id, month, year, basic, deductions, bonus)
        self.payslips.append(payslip)
        self.payslip_counter += 1
        return payslip.generate_payslip()
