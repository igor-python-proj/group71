# Множественное наследование — класс получает методы сразу нескольких родителей.
class Flying:
    def fly(self):
        print(f"Лечу")

class Swimming:
    def swim(self):
        print("Плыву")

# Duck наследует от двух классов сразу и умеет и fly(), и swim().
class Duck(Flying, Swimming):
    pass

donald = Duck()
donald.fly()
donald.swim()

# Миксин — класс-«добавка»: даёт наследникам готовый метод (show_info),
# но сам по себе не полноценный объект. Наследник обязан определить get_info().
class InfoMixin:
    def show_info(self):
        print(self.get_info())

class ObjectWithName:
    def __init__(self, name):
        self.name = name

# миксин указывают первым, затем основной родитель
class Product(InfoMixin, ObjectWithName):
    # каждый наследник сам решает, что именно выводить в show_info
    def get_info(self):
        return f"Товар: {self.name}"

class Room(InfoMixin, ObjectWithName):
    def get_info(self):
        return f"Помещение: {self.name}"

Product("Хлеб").show_info()
Room("Аудитория 4/1").show_info()