# Игра "Поле чудес"

word = ['p', 'y', 't', 'h', 'o', 'n']
answer = ''
print('Наша любимая змея?')

while answer != word[0]:
    answer = input('Введите первую букву: ')
print('Верно! Первая буква - ' + answer)

while answer != word[1]:
    answer = input('Введите вторую букву: ')
print('Верно! Вторая буква - ' + answer)

while answer != word[2]:
    answer = input('Введите третью букву: ')
print('Верно! Третья буква - ' + answer)

while answer != word[3]:
    answer = input('Введите четвёртую букву: ')
print('Верно! Четвёртая буква - ' + answer)

while answer != word[4]:
    answer = input('Введите пятую букву: ')
print('Верно! Пятая буква - ' + answer)

while answer != word[5]:
    answer = input('Введите шестую букву: ')
print('Верно! Шестая буква - ' + answer)

answer = ''.join(word)
print('Вы угадали! Правильный ответ - ' + answer)
