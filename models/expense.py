from models.user import User
from models.expense_metadata import ExpenseMetadata
from models.split import Split
from models.split import EqualSplit
from models.split import ExactSplit
from models.split import PercentSplit
from abc import ABC, abstractmethod
from enum import Enum

class Expense(ABC):
    def __init__(self, amount, paid_by, splits, metadata):
        self.id = None
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits
        self.metadata = metadata

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_paid_by(self):
        return self.paid_by

    def set_paid_by(self, paid_by):
        self.paid_by = paid_by

    def get_splits(self):
        return self.splits

    def set_splits(self, splits):
        self.splits = splits

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

    @abstractmethod 
    def validate(self):
        pass

class ExpenseType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

class EqualExpense(Expense):
    def __init__(self, amount, paid_by, splits, expense_metadata):
        super().__init__(amount, paid_by, splits, expense_metadata)
        print(self.amount)
        print(self.paid_by)
        print(self.get_paid_by())

    def validate(self):
        for split in self.get_splits():
            if not isinstance(split, EqualSplit):
                return False

        return True

class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits, expense_metadata):
        super().__init__(amount, paid_by, splits, expense_metadata)

    def validate(self):
        for split in self.get_splits():
            if not isinstance(split, ExactSplit):
                return False

        total_amount = self.get_amount()
        sum_split_amount = sum(exact_split.get_amount() for exact_split in self.get_splits())

        return total_amount == sum_split_amount
    
class PercentExpense(Expense):
    def __init__(self, amount, paid_by, splits, expense_metadata):
        super().__init__(amount, paid_by, splits, expense_metadata)

    def validate(self):
        print('************')
        for split in self.get_splits():
            if not isinstance(split, PercentSplit):
                return False

        total_percent = 100
        sum_split_percent = sum(percent_split.get_percent() for percent_split in self.get_splits())

        return total_percent == sum_split_percent
    

