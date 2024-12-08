
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")

 
atm = ATM(1000)
atm.deposit(-200)
atm.withdraw(1500)
atm.withdraw(500)
