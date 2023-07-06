znam = int(input('Введите число, я найду обратное:'))
try:
    result = 1 / znam
except ZeroDivisionError:
    result = None
if result:
    print('Обратное равно ', result)
