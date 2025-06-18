from typing import List
from Expense.Expense import Expense
from User.User import User
from Split.Split import Split
from Expense.ExpenseSplitType import ExpenseSplitType
from Controllers.ExpenseController import ExpenseController


class Group:
    def __init__(self):
        self.group_id: str = ""
        self.group_name: str = ""
        self.group_members: List[User] = []
        self.expense_list: List[Expense] = []
        self.expense_controller = ExpenseController()

    def add_member(self, member: User):
        if member in self.group_members:
            print(f"User {member.user_name} is already a member of the group!")
        else:
            self.group_members.append(member)
            print(f"User {member.user_name} added to the group.")

    def get_group_id(self) -> str:
        return self.group_id

    def set_group_id(self, group_id: str):
        self.group_id = group_id

    def set_group_name(self, group_name: str):
        self.group_name = group_name

    def get_expenses(self) -> List[Expense]:
        return self.expense_list

    def get_group_members(self) -> List[User]:
        return self.group_members

    def create_expense(
        self,
        expense_id: str,
        description: str,
        expense_amount: float,
        split_details: List[Split],
        split_type: ExpenseSplitType,
        paid_by_user: User
    ) -> Expense:
        expense = self.expense_controller.create_expense(
            expense_id, description, expense_amount, split_details, split_type, paid_by_user
        )
        self.expense_list.append(expense)
        return expense
