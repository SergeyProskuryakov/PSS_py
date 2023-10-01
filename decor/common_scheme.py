# Как написать декоратор?
# 1. Необходимость выполнения действий до и после некоторой функции
# 2. Пишем код, который выполняется "вокруг" или "вместо" декорируемой функции
# 3. Формируем конструкцию:

#   имя декоратора ( заменяемая функция )
def decorator_name(decorated_func):
    def new_func(*args, **kwargs): pass
        # function body
        # you can call old_func(*args, **kwargs)
    return new_func

@decorator_name
def old_func(any_you_want, arguments, are, allowed): pass
    # old function body

# Применяем декоратор нужное количество раз



