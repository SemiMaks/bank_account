# Класс BankAccount имитирует банковский счёт.

class BankAccount:
    # Метод __init__ принимает аргумент
    # с остатком на счёте.
    # Он присваивается атрибуту __balance.

    # start_balance передаётся в качестве аргумента
    # в метод __init__ , где передаётся в параметр bal.
    def __init__(self, bal):
        self.__balance = bal

    # Метод deposit вносит на счёт вклад.
    # pay передаётся в качестве аргумента в параметр amount.

    def deposit(self, amount):
        self.__balance += amount

    # Метод withdraw снимает сумму со счёта.
    # cash передаётся в качестве аргумента в параметр amount.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка. Недостаточно средств.')

    # Метод get_balance возвращает
    # Остаток средств на счёте.

    def get_balance(self):
        return self.__balance
