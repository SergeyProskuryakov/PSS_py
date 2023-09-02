# 1. Выяснить, какие номера символов не совпадают в двух введенных строках (вернуть список)
# 2. Выяснить, сколько символов второй строки встречается в первой
# 3. Создать случайную строку заданной длины из неповторяющихся символов
# 4. Запросить пользователя строку. Проверить её на соответствие "алфавиту" (самое простое - цифры)
# 5. Красиво оформить игру по алгоритму:
#   5.1. сгенерить строку
#   5.2. в цикле: спросить попытку, проверить и выдать диагностику


# БЫКИ И КОРОВЫ
# Загадывается последовательность (ЧИСЛО) из n-символов
# Игрок высказывает предположение
# И получает диагностику: 
    # быки - символы, стоящие на своих местах,
    # коровы - символы, присутствующие, но не на своём месте
# Подсчитывается количество попыток
# Предлагается новая игра
# Важно: грамотная запись - 1 бык, 3 быка, 11 быков
# Упрощение: угадать 4-х значное число, сравнивая на равенство

import random
import word_forms

### Функция загадывания числа из НЕповторяющихся цифр ###
def create_number_func(nums='0123456789', nums_len=4):
    result = ''.join(random.sample(nums, nums_len))
    return result

def sum_bulls_func(bulls_number, bulls_trying):
    bulls = 0
    for i in range(len(bulls_number)):
        if bulls_number[i] == bulls_trying[i]:
            bulls += 1
    return bulls

def sum_cows_func(cows_number, cows_trying):
    cows = 0
    for i in range(len(cows_number)):
        if cows_trying[i] in cows_number and cows_trying[i] != cows_number[i]:
            cows += 1
    return cows

def main_func():
    number = create_number_func()
    print(number)
    sum_trying = 0
    trying = '0'
    while trying != number:
        sum_trying += 1
        trying = input('Введите 4-х значное число: ')
        if not trying.isdigit():
            print('Играем только числами!')
        if len(trying) == len(number):
            bulls = sum_bulls_func(number, trying)
            cows = sum_cows_func(number, trying)
            print(bulls, ' бык' + word_forms.word_forms_func(bulls, ['', 'а', 'ов']))
            print(cows, ' коров' + word_forms.word_forms_func(cows, ['а', 'ы', '']))
    return sum_trying

len_number = 4
answer = 'да'

while answer == 'да' or answer == 'lf' or answer == 'da' or answer == 'вф':
    sum_trying = main_func()
    print('Угадал за ', sum_trying , ' попыт' + word_forms.word_forms_func(sum_trying, ['ку', 'ки', 'ок']))
    answer = input('Сыграем ещё раз? ')

print('Спасибо за игру! В следующий раз победю я...')