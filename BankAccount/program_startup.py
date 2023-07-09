from person import Person
from date import Date
from customtime import Time
from money import Money
from bank_account import BankAccount

p = Person("Aram", "Khachatryan", 32, "Male")
p1 = Person("Alen", "Aslanyan", 32, "Male")
d = Date(2023, 6, 24)
t = Time(10, 30, 0)
m = Money("USD", 1000)

account1 = BankAccount("123456789", p, 5000, "USD")
account2 = BankAccount("987654321", p1, 3000, "USD")

print("Deposit")
account1.deposit(m)
print(account1)

print("Withdraw")
account1.withdraw(Money("USD", 2000))
print(account1)

print("Transfer")
account1.transfer(account2, Money("USD", 1000))
print(account1)
print(account2)

END = input("Project ends here")