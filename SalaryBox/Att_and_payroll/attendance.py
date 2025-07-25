# attendance.py

from datetime import datetime
from employees import Employee

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
        return (f"Attendance(date={self.date}, entry={entry}, exit={exit}, "
                f"punch_ins={self.punch_ins}, punch_outs={self.punch_outs})")

class AttendanceManagement:
    def __init__(self):
        self.employees = {}
        self.attendance = {}

    def add_employee(self, emp: Employee):
        self.employees[emp.emp_id] = emp

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

    def get_attendance_summary(self, emp_id, month, year):
        present = 0
        leave = 0
        absent = 0

        for att in self.attendance.values():
            if att.employee_id != emp_id:
                continue

            att_date = datetime.strptime(att.date, "%Y-%m-%d")
            if att_date.month == month and att_date.year == year:
                entry_str, exit_str = att.get_entry_exit()
                if entry_str is None and exit_str is None:
                    leave += 1
                elif entry_str and exit_str:
                    entry_time = datetime.strptime(entry_str, "%H:%M:%S")
                    exit_time = datetime.strptime(exit_str, "%H:%M:%S")
                    duration = (exit_time - entry_time).total_seconds() / 3600.0
                    if duration >= 9:
                        present += 1
                    else:
                        absent += 1
                else:
                    absent += 1
        return present, leave, absent

    def view_attendance(self, emp_id):
        print(f"Attendance for {self.employees[emp_id].name}:")
        for att in self.attendance.values():
            if att.employee_id == emp_id:
                print(att)

    def view_all_attendance(self):
        print("All Attendance Records:")
        for att in self.attendance.values():
            print(f"Employee: {self.employees[att.employee_id].name}, {att}")
