class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. Cannot withdraw {amount}. Available balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Example:
account = BankAccount("Kami Ilyassova", 100)
account.deposit(50)      
account.withdraw(30)     
account.withdraw(150)    