# Написать программу (декоратор), который спрашивает,
# сколько раз запустить функцию,
# и запускает её нужное количество раз

# name 'i' is not defined
# имя i не определено
# лечение: создать его. Переменная? Фуенкция? Класс?
# переменная. До первого обращения
i = 0   # создали переменную!

'''schetchik = 0
skolko_raz = int(input('Сколько раз повторить функцию?'))
# допустим, пользователь - хороший человек, и введет натуральное число
while schetchik < skolko_raz:
    print('Hello, World')
    schetchik += 1
'''

# Как написать декоратор?
# 1. Необходимость выполнения действий до и после некоторой функции
# 2. Пишем код, который выполняется "вокруг" или "вместо" декорируемой функции
# 3. Формируем конструкцию:

#   имя декоратора ( заменяемая функция )
def how_many_times(skolko_raz):
    def many_times(decorated_func):
        def new_func():
            schetchik = 0
            # Больше не надо его запрашивать у пользователя!
            # skolko_raz = int(input('Сколько раз повторить функцию?'))
            # допустим, пользователь - хороший человек, и введет натуральное число
            while schetchik < skolko_raz:
                decorated_func()
                schetchik += 1
            # you can call old_func(*args, **kwargs)
        return new_func
    return many_times


# privet_mir = many_times(privet_mir)
# privet_mir = how_many_times(45)(privet_mir)

# 1. "Привет, мир"
#@many_times
@how_many_times(45)
def privet_mir():
    print('Hello, World!')

privet_mir()