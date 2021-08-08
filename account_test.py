# Эта программа демонстрирует класс BankAccount

import bank_account


def main():
    # Получить начальный остаток.

    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount
    saving = bank_account.BankAccount(start_bal)

    # Внести на счёт зарплату пользователя.
    pay = float(input('Сколько вы получили?: '))
    print('Вношу деньги на счёт...')
    saving.deposit(pay)

    # Показать остаток.
    print('Ваш остаток на банковском счёте составляет: ', format(saving.get_balance(), '.2f'), sep='')

    # Получить сумму для снятия с банковского счёта.
    cash = float(input('Сколько Вы хотите снять со счёта?:'))
    print('Пытаюсь снять запрашиваемую сумму со счёта...')
    saving.withdraw(cash)

    # Показать остаток.
    print('Ваш остаток на счёте составляет: ', format(saving.get_balance(), '.2f'), sep='')


# Вызываем главную функцию.
main()
