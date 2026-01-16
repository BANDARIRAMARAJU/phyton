import os
os.system('cls' if os.name == 'nt' else 'clear')
class Bank:
    def __init__(self):
        self.__balance = 1000   # private

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank()
b.show_balance()
