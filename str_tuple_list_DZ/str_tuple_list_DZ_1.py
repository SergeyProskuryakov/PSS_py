# 1. Спросить человека маршрут ("как пройти в библиотеку"). 
#    Получить ответ в виде строки. 
#    Сохранить в переменную. 
#    Вывести первое слово ответа на экран

answer = input('Как пройти в библиотеку? ')
words = answer.split()
print(words[0])