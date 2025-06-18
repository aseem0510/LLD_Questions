from typing import List
from User.User import User
from Split.Split import Split
from Expense.ExpenseSplitType import ExpenseSplitType


class Expense:
    def __init__(
        self,
        expense_id: str,
        expense_amount: float,
        description: str,
        paid_by: User,
        split_type: ExpenseSplitType,
        splits: List[Split]
    ):
        self.expense_id: str = expense_id
        self.expense_amount: float = expense_amount
        self.description: str = description
        self.paid_by_user: User = paid_by
        self.split_type: ExpenseSplitType = split_type
        self.split_details: List[Split] = list(splits)  # copy of the list
