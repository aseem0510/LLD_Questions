from typing import Dict
from .Balance import Balance  # assuming Balance class is in balance.py

class UserExpenseBalanceSheet:
    def __init__(self):
        self._user_vs_balance: Dict[str, Balance] = {}
        self._total_your_expense: float = 0.0
        self._total_payment: float = 0.0
        self._total_you_owe: float = 0.0
        self._total_you_get_back: float = 0.0

    @property
    def user_vs_balance(self) -> Dict[str, Balance]:
        return self._user_vs_balance

    @property
    def total_your_expense(self) -> float:
        return self._total_your_expense

    @total_your_expense.setter
    def total_your_expense(self, value: float):
        self._total_your_expense = value

    @property
    def total_payment(self) -> float:
        return self._total_payment

    @total_payment.setter
    def total_payment(self, value: float):
        self._total_payment = value

    @property
    def total_you_owe(self) -> float:
        return self._total_you_owe

    @total_you_owe.setter
    def total_you_owe(self, value: float):
        self._total_you_owe = value

    @property
    def total_you_get_back(self) -> float:
        return self._total_you_get_back

    @total_you_get_back.setter
    def total_you_get_back(self, value: float):
        self._total_you_get_back = value