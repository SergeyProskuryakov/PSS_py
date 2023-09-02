# 2. Спросить человека размеры поля (х * у), получить их ОДНИМ вводом '7x8', "нарисовать" поле буковками о без использования цикла.

field = input('Введите размеры поля: ')

if ' ' in field:
    xy = field.split(' ')
if 'x' in field:
    xy = field.split('x')
if 'х' in field:
    xy = field.split('х')
if '-' in field:
    xy = field.split('-')
if ' x ' in field:
    xy = field.split(' x ')
if ' х ' in field:
    xy = field.split(' х ')
if ' - ' in field:
    xy = field.split(' - ')

x = int(xy[0])
y = int(xy[1])
print(('o' * x + '\n') * y)