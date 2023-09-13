# Инициализация и другие методы
# Поле - переменная в классе
# Метод - функция в классе

from datetime import datetime

class Human:

    # Инициализатор. Потому что конструктор - __new__ отвечает за выделение памяти
    def __init__(self, name, data):
        # 1 отличие. init - не конструтор!
        # 2 отличие. ПЕРВЫЙ ПАРАМЕТР ЗАПИСЫВАЕТСЯ ЯВНО! (В Js this передается неявно)
        # self - ОБЫЧНО указатель на себя, если метод вызван от объекта или при создании
        # self.dt = datetime(1986, 8, 6)  #??????
        self.data = data
        self.name = name
        self.surname = ''
#        self.change_surname('Баринова')

    def change_surname(self, surname):
        self.surname = surname  # создавать поля за пределами __init__ - плохая идея.
        # Однако, можно создать это поле в __init__ с начальным значением и потом
        # поменять, когда потребуется

# Что изменилось?
woman = Human('Вера')  # - как и раньше? Нет, нужен параметр
# woman.dt = '1999.4.3'
# А как же self?
# он берется в момент создания объекта и сразу передается в инициализатор
# print(woman.dt)
#print(woman.surname)
woman.change_surname('Баринова')
print(woman.surname)
print(woman.name)

# Поля ТЕХНИЧЕСКИ могут быть созданы в теле ЛЮБОГО метода

man = Human('Саша')
man.data = '1996.7.5'

print(man.data)





