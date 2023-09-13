# Игра "Поле чудес"

import random

f = open('questions.txt', encoding='UTF-8')
a = open('answers.txt', encoding='UTF-8')

questions = f.read().split('\n') # прочитали весь файл, поделили его на строки
f.close()
q = random.randint(0, len(questions))
answers = a.read().split('\n')
a.close()

word = answers[q]
# word = 'python'
hint = list('*' * len(word))
print(questions[q])
counter = 0
while '*' in hint: # остались неугаданные буквы
    print(''.join(hint))
    answer = input('Введите вашу букву: ')
    new_hint = []
    for i in range(len(word)):
        if word[i] == answer:
            new_hint.append(answer)
        else:
            new_hint.append(hint[i])
            counter += 1
    hint = new_hint

print('Верно, это - ' + word)
print('Вы ошиблись - ' + str(counter) + ' раз')
# ПРОСТОЙ ПРИМЕР
# for letter in word:        
#     if letter == answer:
#         print(answer, end='')
#     else:
#         print('*', end='')

# 1. программа не оповещает о победе (молчит)
# 2. загаданно только одно слово (файл вопросов, файл ответов и случайную выборку из них)
# 3. количество попыток
# 4. ввести ответ целиком
# коды возврата

