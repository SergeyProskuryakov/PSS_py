# создаём новый скрипт
# в нём должна быть функция
# которая печатает текущий момент времени

# написать декоратор, который печатает после функции в зависимости
# от времени суток 'доброе утро' и тд

# Как написать декоратор?
# 1. Необходимость выполнения действий до и после некоторой функции
# 2. Пишем код, который выполняется "вокруг" или "вместо" декорируемой функции
# 3. Формируем конструкцию:
#   имя декоратора ( заменяемая функция )
import time
from datetime import datetime

def hello(decorated_func):
    def new_func(*args, **kwargs):
        decorated_func(*args, **kwargs)
        every_day()
    return new_func()

@hello
def time_now():
    print('время', time.localtime())
time_now()

def every_day ():
    hr = datetime.now().time().hour
    if hr >= 6 and hr <= 11:
        print('доброе утро')
    if hr >= 12 and hr <= 16:
        print('добрый день')
    if hr >= 17 and hr <= 22:
        print('добрый вечер')
    if hr >= 23 or hr <= 5:
        print('доброй ночи')


def how_many_time():
    print(datetime.now())

how_many_time()
