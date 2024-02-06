from models.user import User
from models.expense import Expense
from models.expense_metadata import ExpenseMetadata
from models.expense import ExpenseType
from models.split import Split
from services.expense_service import ExpenseService

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.user_map = {}
        self.balance_sheet = {}

    def add_user(self, user):
        self.user_map[user.get_id()] = user
        self.balance_sheet[user.get_id()] = {}

    def add_expense(self, expense_type, amount, paid_by_id, splits, expense_metadata):
        paid_by = self.user_map.get(paid_by_id)
        expense = ExpenseService.create_expense(expense_type, amount, paid_by, splits, expense_metadata)
        if expense.validate():
                self.expenses.append(expense)
        else:
                print('Invalid input')
                return None
        

        for split in expense.get_splits():
            paid_to_id = split.get_user().get_id()

            balances = self.balance_sheet[paid_by_id]
            balances[paid_to_id] = balances.get(paid_to_id, 0.0) + split.get_amount()

            balances = self.balance_sheet[paid_to_id]
            balances[paid_by_id] = balances.get(paid_by_id, 0.0) - split.get_amount()

    def show_balance(self, user_id):
        is_empty = True
        for paid_to_id, amount in self.balance_sheet[user_id].items():
            if amount != 0:
                is_empty = False
                self.print_balance(user_id, paid_to_id, amount)

        if is_empty:
            print("No balances")

    def show_balances(self):
        is_empty = True
        for user_id, balances in self.balance_sheet.items():
            for paid_to_id, amount in balances.items():
                if amount > 0:
                    is_empty = False
                    self.print_balance(user_id, paid_to_id, amount)

        if is_empty:
            print("No balances")

    def print_balance(self, user1_id, user2_id, amount):
        user1_name = self.user_map[user1_id].get_name()
        user2_name = self.user_map[user2_id].get_name()
        if amount < 0:
            print(f"{user1_name} owes {user2_name}: {abs(amount)}")
        elif amount > 0:
            print(f"{user2_name} owes {user1_name}: {abs(amount)}")
