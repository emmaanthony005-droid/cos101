from Account_oop import Account

class Savings(Account):
    def __init__(self, owner, balance, interest_rate, withdrawal_limit = 100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest: {interest}, New balance: {self.get_balance()}")
    
    def withdrawal_limit(self, amount):
        self.withdrawal_limit = amount
        if amount > self.withdrawal_limit:
            print(f"Withdrawal limit is ${self.withdrawal_limit}")
        else:
            print(f"Your withdrawal limit is ${self.withdrawal_limit}")
            super().withdraw(amount)

print("----Savings Account----")
savings = Savings("Ella", 1000, 0.02,)
savings.deposit(500)
savings.withdrawal_limit(10000)
savings.apply_interest()
