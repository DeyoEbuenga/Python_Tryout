class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


account = BankAccount("Bank name: "+"\"Deyo Villanueva\"\n", 5000)
print(account.get_name())
print(account.get_balance())
account.deposit(1500)
print(account.get_balance())
account.withdraw(5000)
print(account.get_balance())

print("\n\"thanks for viewing your account!\"")
