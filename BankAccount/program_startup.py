from person import Person
from money import Money
from bank_account import BankAccount
from date import Date
from customtime import Time

def check(function):
    if (function == True):
        print(
            f"***Check for transfer***\n"
            f"Money was successfully transfered from\n"
            f"{account1} to\n{account2}.\nAt {d}/{t}"
            f"\n***Thank you for using our system***")


p = Person("Aram", "Khachatryan", 32, "Male")
p1 = Person("Alen", "Aslanyan", 32, "Male")
m = Money("USD", 1000)
d = Date(2023, 7, 10)
t = Time(10, 30, 0)

account1 = BankAccount("123456789", p, 5000, "USD")
account2 = BankAccount("987654321", p1, 3000, "USD")

print("Deposit")
account1.deposit(m)
print(account1)

print("Withdraw")
account1.withdraw(Money("USD", 2000))
print(account1)

print("Transfer")
x = account1.transfer(account2, Money("USD", 1000))
check(x)
END = input("Project ends here")