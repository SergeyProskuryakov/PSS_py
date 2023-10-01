name = 'sErgey'

# перевод в верхний регистр всех символов
print(name.upper())

# перевод в нижний регистр всех символов
print(name.lower())

# в верхний регистр первого символа
print(name.capitalize())

# использование нескольких методов сразу
print(name.lower().capitalize())

# функция len() - возвращает длину строки
print(len(name))
print(name[0])
print(name[2:4])

# -------------------------------------------- #

my_comment = 'This is my short comment'
print(len(my_comment))
print(my_comment.replace('short', 'long'))
print(my_comment)
print(my_comment.count(' '))