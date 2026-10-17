class Animal:
    def move(self):
        print("я передвигаюсь")

class Swimming(Animal):
    def move(self):
        print("Плыву")
        super().move()

class Flying(Animal):
    def move(self):
        print(f"Лечу")
        super().move()

class Duck(Flying, Swimming):
    def move(self):
        print("лечу и плыву")
        super().move()

donald = Duck()
# MRO - method resolution order - порядок поиска методов
print(Duck.__mro__)
donald.move()
# print("==========")
# bird = Flying()
# bird.move()
# print(Flying.__mro__)
