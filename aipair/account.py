# create Account class and provide the following details:
# acno, customer, balance
# provide the following methods:
# deposit(amount), withdraw(amount), get_balance() 
# provide __str__, __eq__ , __gt__ methods 

class Account:
    def __init__(self, acno, customer, balance):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account No: {self.acno}, Customer: {self.customer}, Balance: {self.balance}"

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.acno == other.acno
        return False

    def __gt__(self, other):
        if isinstance(other, Account):
            return self.balance > other.balance
        return NotImplemented
    


a = Account(12345, "John Doe", 1000)
print(a)  # Account No: 12345, Customer: John Doe, Balance:

