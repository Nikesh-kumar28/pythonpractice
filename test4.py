# Bank Account Management System Using OOP

# Class to represent a bank account
class BankAccount:
    def __init__(self, name, mobile, age, dob, balance):
        self.name = name
        self.mobile = mobile
        self.age = age
        self.dob = dob
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print("Deposit successful!")
            print("Amount Deposited: Rs.", amount)
            print("Updated Balance: Rs.", self.balance)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
            print("Available Balance: Rs.", self.balance)
        else:
            self.balance -= amount
            print("Withdrawal successful!")
            print("Amount Withdrawn: Rs.", amount)
            print("Remaining Balance: Rs.", self.balance)

    # Display account details
    def display_details(self):
        print("\n------ Account Details ------")
        print("Customer Name:", self.name)
        print("Mobile Number:", self.mobile)
        print("Age:", self.age)
        print("Date of Birth:", self.dob)
        print("Account Balance: Rs.", self.balance)
        print("-----------------------------")

    # Check account balance
    def check_balance(self):
        print("Current Account Balance: Rs.", self.balance)


# List to store all bank accounts
accounts = []


# Search account using mobile number
def find_account(mobile):
    for account in accounts:
        if account.mobile == mobile:
            return account
    return None


# Create a new account
def create_account():
    name = input("Enter Customer Name: ").strip()
    if not name:
        print("Error: Customer name cannot be empty.")
        return

    mobile = input("Enter Mobile Number: ").strip()

    if not mobile.isdigit() or len(mobile) != 10:
        print("Error: Enter a valid 10-digit mobile number.")
        return

    if find_account(mobile) is not None:
        print("Error: Mobile number already registered.")
        return

    try:
        age = int(input("Enter Age: "))
        if age <= 0 or age > 120:
            print("Error: Age must be between 1 and 120.")
            return

        dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
        if not dob:
            print("Error: Date of birth cannot be empty.")
            return

        balance = float(input("Enter Initial Balance: "))
        if balance < 0:
            print("Error: Initial balance cannot be negative.")
            return

        account = BankAccount(name, mobile, age, dob, balance)
        accounts.append(account)
        print("Account created successfully!")

    except ValueError:
        print("Error: Please enter valid numeric values.")


# Find account and perform an operation
def get_selected_account():
    mobile = input("Enter Mobile Number: ").strip()
    account = find_account(mobile)

    if account is None:
        print("No account found for the entered mobile number.")

    return account


# Main menu
while True:
    print("\n========================================")
    print("     BANK ACCOUNT MANAGEMENT SYSTEM")
    print("========================================")
    print("A. Create New Account")
    print("B. Check Account Details")
    print("C. Deposit Money")
    print("D. Withdraw Money")
    print("E. Check Account Balance")
    print("F. Display All Accounts")
    print("G. Exit")

    choice = input("Enter your choice: ").strip().upper()

    if choice == "A":
        create_account()

    elif choice == "B":
        account = get_selected_account()
        if account is not None:
            account.display_details()

    elif choice == "C":
        account = get_selected_account()
        if account is not None:
            try:
                amount = float(input("Enter Deposit Amount: "))
                account.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid amount.")

    elif choice == "D":
        account = get_selected_account()
        if account is not None:
            try:
                amount = float(input("Enter Withdrawal Amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid amount.")

    elif choice == "E":
        account = get_selected_account()
        if account is not None:
            account.check_balance()

    elif choice == "F":
        if not accounts:
            print("No accounts available.")
        else:
            for account in accounts:
                account.display_details()

    elif choice == "G":
        print("Thank you for using the Bank Account Management System!")
        break

    else:
        print("Invalid choice! Please select A, B, C, D, E, F, or G.")a
        
