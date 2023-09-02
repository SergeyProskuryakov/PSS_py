# 3. Нарисовать только границу поля и пустую серединку.

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
top_and_bottom = 'o' * x + '\n'
middle = ('o' + (' ' * (x - 2)) + 'o' + '\n') * (y - 2)
print(top_and_bottom + middle + top_and_bottom)