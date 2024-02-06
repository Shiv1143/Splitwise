from models.user import User
from models.expense import Expense
from models.expense import ExpenseType
from models.expense import ExactExpense
from models.expense import PercentExpense
from models.expense import EqualExpense
from models.split import Split
from models.split import PercentSplit

class ExpenseService:
    @staticmethod
    def create_expense(expense_type, amount, paid_by, splits, expense_metadata):
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.PERCENT:
            for split in splits:
                percent_split = split  # Assuming PercentSplit is the base class for all percent-based splits
                split.set_amount((amount * percent_split.get_percent()) / 100.0)
            return PercentExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount / total_splits, 2)
            for split in splits:
                print(split.amount)
                split.amount = split_amount
            splits[0].amount += amount - split_amount * total_splits
            return EqualExpense(amount, paid_by, splits, expense_metadata)
        else:
            return None
