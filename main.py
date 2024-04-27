from bank_system import BankSystem


def main():
    bank_system = BankSystem()
    bank_system.create_admin_account()

    while True:
        print("\n1. Create User Account")
        print("2. Perform Admin Tasks")
        print("3. Perform User Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            bank_system.create_user_account()
        elif choice == "2":
            bank_system.perform_admin_tasks()
        elif choice == "3":
            bank_system.perform_user_tasks()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()