class BankAccount:

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        if amount < 0:
            print("Amount cannot be negative")
            return
        balance += amount

    def withdrawal(self, amount):
        if amount <= 0:
            print("Amount cannot be negative")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def bankFees(self):
        fee = self.balance * (5/100)
        self.balance -= fee

    def display(self):
        print("Account Number :", self.accountNumber)
        print("Account Name   :", self.name)
        print("Account Balance:", self.balance, "₹")


# Create account
newAccount = BankAccount(2178514584, "Mandy", 2800)

# Withdraw ₹700
newAccount.withdrawal(700)

# Display account details
newAccount.display()

# Apply 5% bank fee
newAccount.bankFees()
newAccount.display()
