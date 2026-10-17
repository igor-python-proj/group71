class Animal:
    def move(self):
        print("я передвигаюсь")

class Swimming(Animal):
    # переопределяем move и через super() вызываем реализацию родителя
    def move(self):
        print("Плыву")
        super().move()

class Flying(Animal):
    def move(self):
        print(f"Лечу")
        super().move()

# порядок родителей важен: он задаёт MRO — цепочку поиска методов
class Duck(Flying, Swimming):
    def move(self):
        print("лечу и плыву")
        super().move()

donald = Duck()
# MRO - method resolution order - порядок поиска методов
print(Duck.__mro__)
# super() идет по цепочке MRO: Duck -> Flying -> Swimming -> Animal,
# поэтому сработают все четыре реализации move по очереди.
donald.move()
# print("==========")
# bird = Flying()
# bird.move()
# print(Flying.__mro__)
