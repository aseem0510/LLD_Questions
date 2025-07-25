from datetime import date

class Employee:
    def __init__(self, emp_id, name, email, base_salary, role, join_date):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.role = role
        self.join_date = join_date
    
    def get_details(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "email": self.email,
            "base_salary": self.base_salary,
            "role": self.role,
            "join_date": self.join_date
        }

class Attendance:
    def __init__(self, emp_id, date, status):
        self.emp_id = emp_id
        self.date = date
        self.status = status

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
    def __init__(self):
        self.employees = {}
        self.attendance_records = []
        self.payslips = []
        self.payslip_counter = 1
    
    def add_employee(self, emp):
        self.employees[emp.emp_id] = emp
    
    def mark_attendance(self, emp_id, att_date, status):
        attendance = Attendance(emp_id, att_date, status)
        self.attendance_records.append(attendance)
    
    def calculate_salary(self, emp_id, month, year):
        if emp_id not in self.employees:
            raise ValueError("Employee not found")
        
        emp = self.employees[emp_id]

        total_days = 30  # Assuming a month has 30 days for simplicity
        present_days = sum(1 for att in self.attendance_records if att.emp_id == emp_id and att.date.month == month and att.date.year == year and att.status == 'Present')
        leave_days = sum(1 for att in self.attendance_records if att.emp_id == emp_id and att.date.month == month and att.date.year == year and att.status == 'Leave')
        absent_days = total_days - present_days - leave_days

        # Simple salary calculation
        per_day_salary = emp.base_salary / total_days
        deductions = absent_days * per_day_salary
        bonus = 0
        if present_days == total_days:
            bonus = emp.base_salary * 0.1 # 10% bonus for full attendance
        
        return emp.base_salary, deductions, bonus
    
    def generate_payslip(self, emp_id, month, year):
        basic, deductions, bonus = self.calculate_salary(emp_id, month, year)
        payslip = Payslip(self.payslip_counter, emp_id, month, year, basic, deductions, bonus)
        self.payslips.append(payslip)
        self.payslip_counter += 1
        return payslip.generate_payslip()

if __name__ == "__main__":
    payroll = PayrollManagement()
    
    # Adding employees
    emp1 = Employee(1, "Alice", "alice@gmail.com", 3000, "Developer", date(2023, 1, 15))
    payroll.add_employee(emp1)

    # Marking attendance for 30 days
    for day in range(1, 31):
        payroll.mark_attendance(1, date(2025, 7, day), 'Present')
    
    payslip = payroll.generate_payslip(1, 7, 2025)
    print("Payslip:", payslip)