from typing import List
from User.User import User
from Split.Split import Split
from Balance.Balance import Balance
from Balance.UserExpenseBalanceSheet import UserExpenseBalanceSheet

class BalanceSheetController:

    def update_user_expense_balance_sheet(self, payer: User, splits: List[Split], total_expense: float):
        # Step 1: Update total expense paid
        payer_sheet = payer.user_expense_balance_sheet
        payer_sheet.total_payment += total_expense

        # Step 2: Loop through each person who needs to pay
        for split in splits:
            person_who_owes = split.user
            owes_sheet = person_who_owes.user_expense_balance_sheet
            amount_to_pay = split.amount_owe

            if payer.user_id == person_who_owes.user_id:
                # Step 3: If payer is also involved in expense, update their expense share
                payer_sheet.total_your_expense += amount_to_pay
            else:
                # Step 4: Update payer's and ower's balances
                payer_sheet.total_you_get_back += amount_to_pay
                payer_balance = payer_sheet.user_vs_balance.setdefault(person_who_owes.user_id, Balance())
                payer_balance.amount_get_back += amount_to_pay

                owes_sheet.total_you_owe += amount_to_pay
                owes_sheet.total_your_expense += amount_to_pay
                owes_balance = owes_sheet.user_vs_balance.setdefault(payer.user_id, Balance())
                owes_balance.amount_owe += amount_to_pay

    def show_balance_sheet_of_user(self, user: User):
        print("---------------------------------------")
        print(f"Balance sheet of user: {user.user_id}")

        user_sheet = user.user_expense_balance_sheet
        print(f"TotalYourExpense: {user_sheet.total_your_expense}")
        print(f"TotalGetBack: {user_sheet.total_you_get_back}")
        print(f"TotalYourOwe: {user_sheet.total_you_owe}")
        print(f"TotalPaymentMade: {user_sheet.total_payment}")

        for user_id, balance in user_sheet.user_vs_balance.items():
            print(f"userID: {user_id} YouGetBack: {balance.amount_get_back} YouOwe: {balance.amount_owe}")
            net_balance = balance.amount_get_back - balance.amount_owe

            if net_balance > 0:
                print(f"FinalBalanceWithUser: You get back ₹{net_balance}")
            elif net_balance < 0:
                print(f"FinalBalanceWithUser: You owe ₹{-net_balance}")
            else:
                print(f"FinalBalanceWithUser: All settled up with user {user_id}")

        print("---------------------------------------")


    def settle_up(self, payer: User, payee: User, amount: float):
        payer_sheet = payer.user_expense_balance_sheet
        payee_sheet = payee.user_expense_balance_sheet

        payer_balance = payer_sheet.user_vs_balance.get(payee.user_id)
        payee_balance = payee_sheet.user_vs_balance.get(payer.user_id)

        if not payer_balance or payer_balance.amount_owe < amount:
            print(f"Cannot settle ₹{amount}. You owe only ₹{payer_balance.amount_owe if payer_balance else 0}.")
            return

        # Adjust balances
        payer_balance.amount_owe -= amount
        payer_sheet.total_you_owe -= amount

        payee_balance.amount_get_back -= amount
        payee_sheet.total_you_get_back -= amount

        print(f"{payer.user_name} settled ₹{amount} with {payee.user_name}.")
