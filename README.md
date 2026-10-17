# group-71-1

Учебный проект: объектно-ориентированное программирование на Python.

## Структура

| Файл | Содержание |
| --- | --- |
| `lessons/car.py` | Класс `Car`: объекты, атрибуты, методы, `self` |
| `lessons/other_cars.py` | Наследование и полиморфизм: `ElectricCar`, `SportCar` |
| `lessons/lesson_3.py` | Инкапсуляция (приватные атрибуты), абстрактные классы |
| `lessons/lesson_4.py` | Магические методы (`__call__`, `__add__` и др.) |
| `lessons/lesson_4_2.py` | Атрибуты класса, `@property`, `@staticmethod`, `@classmethod` |
| `lessons/lesson_5.py` | Множественное наследование, миксины |
| `lessons/lesson_5_2.py` | MRO — порядок поиска методов |
| `lessons/my_decorators.py` | Декораторы |
| `lessons/database.py` | Работа с базой данных SQLite |
| `homeworks/homework_1.py` | Домашняя работа |

## Запуск

Из корня проекта выполняйте файлы по одному:

```
python lessons\car.py
python lessons\lesson_3.py
python lessons\database.py
```

Если кириллица выводится «кракозябрами», установите кодировку перед запуском:

```
set PYTHONIOENCODING=utf-8
```
