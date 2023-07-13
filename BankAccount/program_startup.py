from person import Person
from money import Money
from bank_account import BankAccount
from date import Date
from customtime import Time


def check(function):
    if function is True:
        print(
            f"***Check for transfer***\n"
            f"Money was successfully transferred from\n"
             
            f"{account1} to\n{account2}\nAmount is {account1.amount}.\nCommission is "
            f"{account1.system_balance}\nAt {d}/{t}"
            f"\n***Thank you for using our system***")
    else:
        print(f"***Check for transfer***\n"
              f"Money was not transferred.\n"
              f"Please review your bank account"
              f"\n***Thank you for using our system***")


p = Person("Aram", "Khachatryan", 32, "Male")
p1 = Person("Alen", "Aslanyan", 32, "Male")
m = Money("USD", 1000)
d = Date(2023, 7, 12)
t = Time(10, 30, 0)

account1 = BankAccount(p, 5000, "USD")
account2 = BankAccount(p1, 3000, "USD")
account1.create_password()
account1.get_password()
print(account1.balance)
account1.take_off_money(300)
print(account1.balance)

x = account1.transfer(account2, Money("USD", 1000))
check(x)
END = input("Project ends here")
