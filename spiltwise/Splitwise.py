from User.UserController import UserController
from Controllers.GroupController import GroupController
from Controllers.BalanceSheetController import BalanceSheetController
from Group.Group import Group
from Split.Split import Split
from Expense.ExpenseSplitType import ExpenseSplitType
from User.User import User


class Splitwise:
    _instance = None  # Singleton instance

    def __init__(self):
        if Splitwise._instance is not None:
            raise Exception("This class is a singleton!")
        self.user_controller = UserController()
        self.group_controller = GroupController()
        self.balance_sheet_controller = BalanceSheetController()
        Splitwise._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Splitwise()
        return cls._instance

    def run_splitwise_demo(self):
        self.setup_users_and_group()

        # Step 1: Add members to the group
        group = self.group_controller.get_group("G1001")
        group.add_member(self.user_controller.get_user("U2001"))  # Bob
        group.add_member(self.user_controller.get_user("U3001"))  # Charlie

        # Step 2: Create expenses within the group
        group.create_expense(
            "Exp1001", "Breakfast", 900,
            [
                Split(self.user_controller.get_user("U1001"), 300),  # Alice
                Split(self.user_controller.get_user("U2001"), 300),  # Bob
                Split(self.user_controller.get_user("U3001"), 300),  # Charlie
            ],
            ExpenseSplitType.EQUAL,
            self.user_controller.get_user("U1001")  # Paid by Alice
        )

        group.create_expense(
            "Exp1002", "Lunch", 500,
            [
                Split(self.user_controller.get_user("U1001"), 400),  # Alice
                Split(self.user_controller.get_user("U2001"), 100),  # Bob
            ],
            ExpenseSplitType.UNEQUAL,
            self.user_controller.get_user("U2001")  # Paid by Bob
        )

        # Step 3: Display balance sheets
        for user in self.user_controller.get_all_users():
            self.balance_sheet_controller.show_balance_sheet_of_user(user)

    def setup_users_and_group(self):
        self.register_users()
        self.group_controller.create_new_group("G1001", "Outing with Friends", self.user_controller.get_user("U1001"))

    def register_users(self):
        self.user_controller.add_user(User("U1001", "Alice"))
        self.user_controller.add_user(User("U2001", "Bob"))
        self.user_controller.add_user(User("U3001", "Charlie"))
