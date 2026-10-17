# Множественное наследование
class Flying:
    def fly(self):
        print(f"Лечу")

class Swimming:
    def swim(self):
        print("Плыву")

class Duck(Flying, Swimming):
    pass

donald = Duck()
donald.fly()
donald.swim()

# миксин
class InfoMixin:
    def show_info(self):
        print(self.get_info())

class ObjectWithName:
    def __init__(self, name):
        self.name = name

class Product(InfoMixin, ObjectWithName):
    def get_info(self):
        return f"Товар: {self.name}"

class Room(InfoMixin, ObjectWithName):
    def get_info(self):
        return f"Помещение: {self.name}"

Product("Хлеб").show_info()
Room("Аудитория 4/1").show_info()