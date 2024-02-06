from models.user import User

class Split:
    def __init__(self, user):
        self.user = user
        self.amount = 0.0

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

class EqualSplit(Split):
    def __init__(self, user):
        super().__init__(user)

class ExactSplit(Split):
    def __init__(self, user, amount):
        super().__init__(user)
        self.amount = amount

class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent = percent

    def get_percent(self):
        return self.percent

    def set_percent(self, percent):
        self.percent = percent
