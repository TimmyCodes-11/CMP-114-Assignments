from account import Account

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

        savings = SavingsAccount()
        savings.deposit(amount=2000)
        print(self.account_balance)

        savings.withdrawal(amount=2000)
        print(self.account_balance)