from enums.Currency import Currency

class Account:
    count = 0

    def __init__(self, currency: Currency, bank) -> None:
        Account.count += 1
        self.ACCOUNT_ID = Account.count
        self.CURRENCY = currency
        self.__balance: float = 0

    def get_balance(self):
        return self.__balance

    # Those methodes should only be called via instances of a class Bank
    def withdraw(self, amount: float):
        if self.__balance < amount: return False 
        self.__balance -= amount
        return True

    def receive(self, amount: float):
        self.__balance =+ amount

