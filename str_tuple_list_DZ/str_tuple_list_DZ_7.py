#  Нарисовать только границу поля и пустую серединку.
#  С помощью только while сделать задачю 3

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
top_and_bottom = 'o' * x
middle = ('o' + (' ' * (x - 2)) + 'o')
i = 0
print(top_and_bottom)

while i < (y - 2):
    print(middle)
    i += 1

print(top_and_bottom)

