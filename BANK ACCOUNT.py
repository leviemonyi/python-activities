class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: ${amount}"

    def check_balance(self):
        return f"Current balance: ${self.balance}"

    def customer_details(self):
        return (f"Customer Name: {self.customer_name}\n"
                f"Account Number: {self.account_number}\n"
                f"Date of Opening: {self.date_of_opening}\n"
                f"Balance: ${self.balance}")
                
 # Creating a bank account instance
account = BankAccount(account_number="123456789", customer_name="LEVI", date_of_opening="2024-11-11", balance=1000)

# Depositing money
print(account.deposit(500))  # Output: Deposited: $500

# Withdrawing money
print(account.withdraw(200))  # Output: Withdrawn: $200
print(account.withdraw(1500)) # Output: Insufficient balance

# Checking balance
print(account.check_balance())  # Output: Current balance: $1300

# Printing customer details
print(account.customer_details())
               
