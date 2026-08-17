class WalletError(Exception):
    """Базовое исключение для всех ошибок кошелька."""
    pass

class InsufficientFundsError(WalletError):
    """Выбрасывается, когда на счете недостаточно средств."""
    pass

class NegativeAmountError(WalletError):
    """Выбрасывается при попытке операции с отрицательной суммой."""
    pass



class Wallet:
    def __init__(self, balance = 0):
        self._balance = balance 

    @property
    def balance(self):
        return self._balance 

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Сумма для пополнения должна быть положительной")
        self._balance += amount 
        print(f"Счет пополнен на {amount}. Баланс: {self._balance}")

    def withdraw(self, amount): 
        if amount <= 0:
            raise NegativeAmountError("Сумма для пополнения должна быть положительной")

        if self._balance < amount: 
            raise InsufficientFundsError(f"Недостаточно средств. Запрошено: {amount}, доступно: {self._balance}")

        self._balance -= amount
        print(f"Со счета снято {amount}. Баланс: {self._balance}")

my_wallet = Wallet(100)
try:
    print("--- Попытка снять 50 ---")
    my_wallet.withdraw(50) # Успешно

    print("\n--- Попытка снять 200 ---")
    my_wallet.withdraw(200) # InsufficientFundsError

    print("\n--- Этот код не выполнится ---")

except NegativeAmountError as e:
    # Этот блок не сработает, т.к. ошибка другого типа
    print(f"Перехвачена ошибка некорректной суммы: {e}")

except InsufficientFundsError as e:
    # А вот этот блок сработает!
    print(f"Перехвачена ошибка нехватки средств: {e}")
    print("Пожалуйста, пополните ваш кошелек.")

except WalletError as e:
    # Этот блок поймал бы любую из наших ошибок, если бы мы не поймали ее раньше
    print(f"Произошла общая ошибка кошелька: {e}")

finally:
    # Этот блок выполнится в любом случае
    print(f"\nОперация завершена. Итоговый баланс: {my_wallet.balance}")       