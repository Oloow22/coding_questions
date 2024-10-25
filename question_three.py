class BankAccount:
    
    
    def __init__(self, account_number, account_holder, balance):
        #initiate the account class with all the relevant properties
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def calculate_interest(self):
        #calculate the interest and apply it to the amount
        interest_rate = 0.05
        interest = self.balance * interest_rate
        self.balance += interest
        return interest

account = BankAccount(12345, "Mike", 1000)

# Calculate and apply interest
interest = account.calculate_interest()

# Print updated balance
print(f"Updated Balance: {account.balance}")