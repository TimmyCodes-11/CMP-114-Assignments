from account import Account

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

        current = CurrentAccount()
        current.deposit(amount=2000)
        print(self.account_balance)

        current.withdrawal(amount=2000)
        print(self.account_balance)











