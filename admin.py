from user import User

class Admin:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.users = []
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Account of {user.name} deleted successfully")
        else:
            print("User not found")

    def list_all_accounts(self):
        return self.users

    def total_available_balance(self):
        total_balance = sum(user.balance for user in self.users)
        return total_balance

    def total_loan_amount(self):
        total_loan = sum(user.loan_taken for user in self.users)
        return total_loan

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        if self.loan_feature:
            print("Loan feature is now enabled")
        else:
            print("Loan feature is now disabled")

