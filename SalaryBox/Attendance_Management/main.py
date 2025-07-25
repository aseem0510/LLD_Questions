from datetime import datetime
import time

class Attendance:
    def __init__(self, employee_id, date):
        self.id = f"{employee_id}_{date}"
        self.employee_id = employee_id
        self.date = date
        self.punch_ins = []
        self.punch_outs = []
    
    def add_punch_in(self, time):
        self.punch_ins.append(time)
        return True

    def add_punch_out(self, time):
        self.punch_outs.append(time)
        return True
    
    def get_entry_exit(self):
        entry = self.punch_ins[0] if self.punch_ins else None
        exit = self.punch_outs[-1] if self.punch_outs else None
        return entry, exit
    
    def __repr__(self):
        entry, exit = self.get_entry_exit()
        return (f"Attendance(date={self.date}, entry={entry}, exit={exit}, " f"punch_ins={self.punch_ins}, punch_outs={self.punch_outs})")


class Employee:
    def __init__(self, emp_id, name, role="employee"):
        self.id = emp_id
        self.name = name
        self.role = role
    
    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, role={self.role})"

class AttendanceManagement:
    def __init__(self):
        self.employees = {}
        self.attendance = {}

    def add_employee(self, emp):
        self.employees[emp.id] = emp

    def punch_in(self, emp_id):
        today = datetime.now().strftime("%Y-%m-%d")
        key = f"{emp_id}_{today}"
        now = datetime.now().strftime("%H:%M:%S")

        if key not in self.attendance:
            self.attendance[key] = Attendance(emp_id, today)
        self.attendance[key].add_punch_in(now)
        print(f"{self.employees[emp_id].name} punched in at {now}")
    

    def punch_out(self, emp_id):
        today = datetime.now().strftime("%Y-%m-%d")
        key = f"{emp_id}_{today}"
        now = datetime.now().strftime("%H:%M:%S")

        if key not in self.attendance:
            self.attendance[key] = Attendance(emp_id, today)
        self.attendance[key].add_punch_out(now)
        print(f"{self.employees[emp_id].name} punched out at {now}")


    def view_attendance(self, emp_id):
        print(f"Attendance for {self.employees[emp_id].name}:")
        for att in self.attendance.values():
            if att.employee_id == emp_id:
                print(att)
    
    def view_all_attendance(self):
        print("All Attendance Records:")
        for att in self.attendance.values():
            print(f"Employee: {self.employees[att.employee_id].name}, {att}")


if __name__ == "__main__":
    am = AttendanceManagement()
    
    # Adding employees
    emp1 = Employee(1, "Alice")
    emp2 = Employee(2, "Bob")
    
    am.add_employee(emp1)
    am.add_employee(emp2)
    
    # Punching in and out
    am.punch_in(1)
    time.sleep(1)

    am.punch_out(1)
    time.sleep(1)

    am.punch_in(1)
    time.sleep(1)

    am.punch_in(2)
    time.sleep(1)

    am.punch_out(2)
    time.sleep(1)

    am.punch_out(2)
    time.sleep(1)  

    am.punch_in(1)
    time.sleep(1)

    am.punch_in(2)
    time.sleep(1)

    am.punch_out(2)
    time.sleep(1)  

    am.punch_out(1)
    time.sleep(1)

    am.punch_in(1)
    time.sleep(1)

    am.punch_out(2)
    time.sleep(1)

    # Viewing attendance records
    am.view_attendance(1)
    am.view_attendance(2)
    
    # Viewing all attendance records
    am.view_all_attendance()