# 1. С клавиатуры вводятся числа. Остановиться, как только введён ноль. Посчитать количество введенных чисел
# 2. Усложнение: остановиться, как только введен "просто Enter"

vsego = 0

vvod = input('Введите число: ')
if vvod != '':
    while vvod != 0:
        vsego += 1
        vvod = int(input('Введите число: '))
    print(vsego)
else:
    print('вы ничего не ввели')