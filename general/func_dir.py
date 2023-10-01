# функция dir отображает имена всех атрибутов объекта
name = 'Sergey'
# print(dir(name))
# print('*' * 100)
# old = 35
# print(dir(old))

# функция id по имени выдаёт адрес в памяти
my_number = 1
print(id(my_number))

print('id name: ', id(name))
print('id my_number: ', id(my_number))

other_num = my_number
print('id other_num: ', id(other_num))