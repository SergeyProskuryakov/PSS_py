# Бинарный поиск: Вы загадываете число от 1 до 1000 и записываете его в тетрадь.
# Компьютер задаёт вам только вопросы типа "число больше 70?" или "число меньше 25?" Вы честно отвечаете "да" или "нет". 
# Компьютер должен угадать ваше число. Сколько попыток ему потребовалось? Это количество зависит от загаданного числа?

min_number = 1
max_number = 1000
counter = 0
number = (min_number + max_number) // 2 

print('ПРОГРАММА ПРИНИМАЕТ ТОЛЬКО ОТВЕТЫ "да" И "нет"')
print(f'Число больше {number} ?', end=' ')
question = input('')
while min_number != max_number:
    if question == 'да':
        min_number = number
        counter += 1
        print(f'Число больше {number} ?', end=' ')
        question = input('')
    elif question == 'нет':
        max_number = number
        counter += 1
        print(f'Число больше {number} ?', end=' ')
        question = input('')
    else:
        print('Вводите только "да" или "нет"')
print('я угадал, это ', number)