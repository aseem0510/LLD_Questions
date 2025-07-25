# models.py

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
