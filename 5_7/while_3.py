# 1. Перепишите программу, избежав "continue"
# 2. Посчитайте количество верных и неверных ответов, процент ошибок
# 3. ГОРШОЧЕК, НЕ ВАРИ! Поставьте ограничения:
#     a. По количеству заданий
#     b. По максимуму ошибок
#     c. По минимальному проценту ошибок

from random import randint
a = randint(1, 10)
b = randint(1, 10)
while True:
    result = a + b
    answer = int(input('Сколько будет %(a)i + %(b)i = ' % {
        'a': a, 'b': b }))
    if answer != result:
        print('Не правильно, попробуй ещё раз ')
        continue
    print('Верно')
    a = randint(1, 10)
    b = randint(1, 10)
