from typing import List
from Expense.Expense import Expense
from Expense.ExpenseSplitType import ExpenseSplitType
from Split.Split import Split
from User.User import User
from Controllers.BalanceSheetController import BalanceSheetController
from Split.SplitStratigies.EqualExpenseSplit import EqualExpenseSplit
from Split.SplitStratigies.UnequalExpenseSplit import UnequalExpenseSplit
from Split.SplitStratigies.PercentageExpenseSplit import PercentageExpenseSplit


class ExpenseController:
    def __init__(self):
        self.balance_sheet_controller = BalanceSheetController()

    def create_expense(
        self,
        expense_id: str,
        description: str,
        expense_amount: float,
        split_details: List[Split],
        split_type: ExpenseSplitType,
        paid_by_user: User
    ) -> Expense:

        if split_type == ExpenseSplitType.EQUAL:
            expense_split = EqualExpenseSplit()
        elif split_type == ExpenseSplitType.UNEQUAL:
            expense_split = UnequalExpenseSplit()
        elif split_type == ExpenseSplitType.PERCENTAGE:
            expense_split = PercentageExpenseSplit()
        else:
            raise ValueError("Invalid split type")

        expense_split.validate_split_request(split_details, expense_amount)

        expense = Expense(
            expense_id=expense_id,
            expense_amount=expense_amount,
            description=description,
            paid_by=paid_by_user,
            split_type=split_type,
            splits=split_details
        )

        self.balance_sheet_controller.update_user_expense_balance_sheet(
            paid_by_user, split_details, expense_amount
        )

        return expense
