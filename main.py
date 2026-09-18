class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0.0
        self.menu()

    def authenticate(self) -> bool:
        """Helper method to verify PIN and prevent access if unset."""
        if not self.pin:
            print("No PIN found. Please create a PIN first.")
            return False
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        print("Incorrect PIN. Please try again.")
        return False

    def menu(self):
        while True:
            user_input = input("""
Hi, How can I help you today?
1. Press 1 to create a new PIN
2. Press 2 to change PIN
3. Press 3 to check balance
4. Press 4 to deposit money
5. Press 5 to withdraw money
6. Press 6 or anything else to exit
> """)

            match user_input:
                case "1":
                    self.create_pin()
                case "2":
                    self.change_pin()
                case "3":
                    self.check_balance()
                case "4":
                    self.deposit()
                case "5":
                    self.withdraw()
                case _:
                    print("Thank you for using our ATM. Goodbye!")
                    break  # Gracefully ends the loop and session

    def create_pin(self):
        self.pin = input("Enter your new PIN: ")
        print("Your new PIN has been created successfully.")

    def change_pin(self):
        if not self.authenticate():
            return
        self.pin = input("Enter your new PIN: ")
        print("Your PIN has been changed successfully.")

    def check_balance(self):
        if not self.authenticate():
            return
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self):
        if not self.authenticate():
            return
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

    def withdraw(self):
        if not self.authenticate():
            return
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Please enter a valid amount to withdraw.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")


obj = ATM()

