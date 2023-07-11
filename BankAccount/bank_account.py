import uuid

from money import Money
from hash import Hasher


class BankAccount:
    def __init__(self, owner, balance, currency):
        self.account_number = uuid.uuid4().int
        self.owner = owner
        self.password = ""
        self.balance = balance
        self.currency = currency
        self.amount = 0

    def __repr__(self):
        return "Account Number: {}\nOwner: {}\nBalance: {} {}".format(
            self.account_number, self.owner, self.balance, self.currency
        )

    def create_password(self):
        password = input("Enter your bank account password please\n")
        hasher = Hasher()
        self.password = hasher.hash_string(password)
        print("***Your password was successfully saved***")

    def get_password(self):
        print(f"***Hashed password is\n{self.password}***")

    def deposit(self, amount):
        if isinstance(amount, Money):
            if amount.currency == self.currency:
                self.balance += amount.amount
            else:
                converted_amount = amount.exchange(self.currency)
                self.balance += converted_amount.amount
        else:
            print("Invalid amount type.")

    def withdraw(self, amount):
        if isinstance(amount, Money):
            if amount.currency == self.currency:
                if amount.amount <= self.balance:
                    self.balance -= amount.amount
                else:
                    print("Insufficient balance.")
            else:
                print("Currency mismatch.")
        else:
            print("Invalid amount type.")

    def transfer(self, destination_account, amount):
        if isinstance(amount, Money):
            if amount.currency == self.currency:
                if amount.amount <= self.balance:
                    self.balance -= amount.amount
                    self.amount = amount
                    destination_account.balance += amount.amount
                    return True
                else:
                    print("Insufficient balance.")
                    return False
            else:
                print("Currency mismatch.")
                return False
        else:
            print("Invalid amount type.")
            return False
