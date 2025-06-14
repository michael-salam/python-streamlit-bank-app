from account import Account

class SavingsAccount(Account):
    def __init__(self, balance, limit):
        Account.__init__(self, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.limit:
            print(f'Error: Cannot withdraw more than the limit of {self.limit}.')
        elif amount > self.balance:
            print('Error: Insufficient balance.')
        else:
            super().withdraw(amount)
            print(f'Withdrew {amount}. New balance: {self.balance}.')