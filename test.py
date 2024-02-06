from models.user import User
from models.expense import ExpenseType
from models.split import EqualSplit
from models.split import ExactSplit
from models.split import PercentSplit
from models.split import Split
from controllers.expense_controller import ExpenseManager

import sys

class Driver:
    def __init__(self):
        self.expense_manager = ExpenseManager()

    def main(self):
        self.expense_manager.add_user(User("u1", "User1", "nishu@gmail.com", "9543259909"))
        self.expense_manager.add_user(User("u2", "User2", "saeffas_kumar@gmail.com", "9109340329"))
        self.expense_manager.add_user(User("u3", "User3", "skjtfek_df@gmail.com", "9664237939"))
        self.expense_manager.add_user(User("u4", "User4", "bsoaei@gmail.com", "9886343210"))

        while True:
            command = input()
            commands = command.split(" ")
            command_type = commands[0]
            if command_type == "SHOW":
                if len(commands) == 1:
                    self.expense_manager.show_balances()
                else:
                    self.expense_manager.show_balance(commands[1])
            elif command_type == "EXPENSE":
                paid_by = commands[1]
                amount = float(commands[2])
                no_of_users = int(commands[3])
                expense_type = commands[4]
                splits = []
                if expense_type == "EQUAL":
                    for i in range(no_of_users):
                        splits.append(EqualSplit(self.expense_manager.user_map[commands[5 + i]]))
                        EqualSplit.validate()
                    self.expense_manager.add_expense(ExpenseType.EQUAL, amount, paid_by, splits, None)
                elif expense_type == "EXACT":
                    for i in range(no_of_users):
                        splits.append(ExactSplit(self.expense_manager.user_map[commands[5 + i]], float(commands[5 + no_of_users + i])))
                    self.expense_manager.add_expense(ExpenseType.EXACT, amount, paid_by, splits, None)
                elif expense_type == "PERCENT":
                    for i in range(no_of_users):
                        splits.append(PercentSplit(self.expense_manager.user_map[commands[5 + i]], float(commands[5 + no_of_users + i])))
                    self.expense_manager.add_expense(ExpenseType.PERCENT, amount, paid_by, splits, None)
                    

if __name__ == "__main__":
    driver = Driver()
    driver.main()
