from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Error: Insuffiecient funds')
        else:
            super().withdraw(amount)
            print(f'Success: You have withdrawn {amount}. New balance is {self.balance}.')