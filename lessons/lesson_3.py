class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        # атрибуты с __ называются приватные
        self.__password = password
        # атрибуты с _ называются защищенные
        self._balance = balance

    def get_balance(self, user_login, user_pass):
        if self.login == user_login and self.__password == user_pass:
            return self._balance
        return "Не верный логин или пароль !!"

    def __reset_pass(self):
        self.__password = "1234"
        return f"{self.login} Пароль сброшен новый пароль 1234!!"

    def new_pass(self, old_pass):
        if old_pass == self.__password:
            return self.__reset_pass()
        return "Неверный старый пароль !!"

ardager = BankAccount("ardager_dev", "2638", 1000)
# print(ardager.get_balance("ardager_dev", "2638"))
# print(ardager._BankAccount__password)
# print(ardager._BankAccount__reset_pass())
# print(ardager._BankAccount__password)

from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def move(self);
        pass
    @abstractmethod
    def voce(selt):
        pass

class Dog(Animal):
    def move(self):
        print('Steps')
    def voce(self):
        print("Gaf Gaf")
class Cat:
    def move(self):
        print('Step')
    def voce(self):
        print("May MAy")

# gufi = Dog()
