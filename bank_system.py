from admin import Admin


class BankSystem:
    def __init__(self):
        self.admin = None

    def create_admin_account(self):
        print("Creating Admin Account:")
        name = input("Enter admin name: ")
        email = input("Enter admin email: ")
        address = input("Enter admin address: ")
        self.admin = Admin(name, email, address)

    def create_user_account(self):
        if self.admin:
            print("\nCreating User Account:")
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            address = input("Enter user address: ")
            account_type = input("Enter account type (Savings/Current): ")
            self.admin.create_account(name, email, address, account_type)
            print("User account created successfully.")
        else:
            print("Admin account not created yet.")

    def perform_admin_tasks(self):
        if self.admin:
            print("\nPerforming Admin Tasks:")
            print("1. Delete User Account")
            print("2. List All User Accounts")
            print("3. Check Total Available Balance")
            print("4. Check Total Loan Amount")
            print("5. Toggle Loan Feature")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.delete_user_account()
            elif choice == "2":
                self.list_all_user_accounts()
            elif choice == "3":
                self.check_total_available_balance()
            elif choice == "4":
                self.check_total_loan_amount()
            elif choice == "5":
                self.toggle_loan_feature()
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Admin account not created yet.")

    def perform_user_tasks(self):
        email = input("Enter your email: ")
        user = self.find_user_by_email(email)
        if user:
            print("\nPerforming User Tasks:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Check Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                user.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                user.withdraw(amount)
            elif choice == "3":
                print("Your balance:", user.check_balance())
            elif choice == "4":
                print("Your transaction history:")
                print("\n".join(user.check_transaction_history()))
            elif choice == "5":
                amount = float(input("Enter the loan amount: "))
                user.take_loan(amount)
            elif choice == "6":
                recipient_email = input("Enter recipient's email: ")
                recipient = self.find_user_by_email(recipient_email)
                if recipient:
                    amount = float(input("Enter the amount to transfer: "))
                    user.transfer(amount, recipient)
                else:
                    print("Recipient account not found.")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("User not found.")

    def delete_user_account(self):
        if self.admin:
            print("\nDeleting User Account:")
            email = input("Enter user email to delete account: ")
            user = self.find_user_by_email(email)
            if user:
                self.admin.delete_account(user)
            else:
                print("User not found.")
        else:
            print("Admin account not created yet.")

    def list_all_user_accounts(self):
        if self.admin:
            print("\nList of All User Accounts:")
            accounts = self.admin.list_all_accounts()
            for account in accounts:
                print(account.name, account.email)
        else:
            print("Admin account not created yet.")

    def check_total_available_balance(self):
        if self.admin:
            print("\nTotal Available Balance:", self.admin.total_available_balance())
        else:
            print("Admin account not created yet.")

    def check_total_loan_amount(self):
        if self.admin:
            print("\nTotal Loan Amount:", self.admin.total_loan_amount())
        else:
            print("Admin account not created yet.")

    def toggle_loan_feature(self):
        if self.admin:
            self.admin.toggle_loan_feature()
        else:
            print("Admin account not created yet.")

    def find_user_by_email(self, email):
        if self.admin:
            for user in self.admin.list_all_accounts():
                if user.email == email:
                    return user
        return None
