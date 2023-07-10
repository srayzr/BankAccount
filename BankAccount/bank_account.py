from money import Money

class BankAccount:
    def __init__(self, account_number, owner, balance, currency):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def __repr__(self):
        return "Account Number: {}\nOwner: {}\nBalance: {} {}".format(
            self.account_number, self.owner, self.balance, self.currency
        )

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
                    destination_account.balance += amount.amount
                    return True
                else:
                    print("Insufficient balance.")
            else:
                print("Currency mismatch.")
        else:
            print("Invalid amount type.")