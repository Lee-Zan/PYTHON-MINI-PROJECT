class BankAccount:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(str(amount) + " deposited to " + self.name + "'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(str(amount) + " withdrawn from " + self.name + "'s account.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print("Account holder: " + self.name + ", Balance: " + str(self.balance))


    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(str(amount) + " transferred from " + self.name + " to " + other_account.name + ".")
        else:
            print("Transfer failed: insufficient balance or invalid amount.")


account1 = BankAccount("Lizan", 50000)
account2 = BankAccount("Ram", 25000)

account1.deposit(5000)
account2.withdraw(10000)

account1.transfer(account2, 7000)

account1.show_balance()
account2.show_balance()