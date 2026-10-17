
# Декоратор — функция, которая принимает другую функцию и возвращает новую,
# добавляя действия до и после её вызова, не меняя код самой функции.
def log_action(func):
    # wrapper — «обёртка»: заменит собой исходную функцию.
    # *args, **kwargs принимают любые аргументы и передают их дальше без изменений.
    def wrapper(*args, **kwargs):
        print("Начало операции")
        # вызываем исходную функцию и сохраняем её результат
        result = func(*args, **kwargs)
        print("Конец операции")
        # возвращаем результат, чтобы функция работала как раньше
        return result
    # декоратор возвращает новую функцию вместо исходной
    return wrapper

def make_order(x):
    print("Заказ создан", x)
    return 100

def do_something():
    print("other function")
    return "OK"

# Ручное применение декоратора: make_order теперь обёртка вокруг исходной функции.
make_order = log_action(make_order)
print(make_order)
order = make_order(122222)
print(order)
# Тот же декоратор для другой функции.
# Обычно пишут короче: над функцией ставят @log_action — это то же самое.
do_something = log_action(do_something)
res = do_something()
print(res)


# make_order()