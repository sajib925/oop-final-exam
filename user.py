

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_limit = 2

    def generate_account_number(self):
        return hash(self.email) % 1000000

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_limit > 0:
            self.loan_taken += amount
            self.balance += amount
            self.loan_limit -= 1
            self.transaction_history.append(f"Loan taken: ${amount}")
        else:
            print("You've already taken the maximum number of loans")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            recipient.balance += amount
            self.balance -= amount
            self.transaction_history.append(f"Transferred: ${amount} to {recipient.name}")
        else:
            print("Insufficient funds to transfer")
