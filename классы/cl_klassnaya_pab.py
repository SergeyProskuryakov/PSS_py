# 1. Классная работа:
# Класс дробь.
# Реализовать:
# сумму, разность, произведение и частное двух обыкновенных дробей
# печать объектов класса дробь
# Искать в интернете алгоритм сокращения дроби - не нужно
# Если не знаете сами, пропустите этот шаг

# Магические методы арифметических операторов +, - sub, * mul, / div
    # def __add__(self, other):
        # предполагается, что объект нашего класса расположен слева от плюсика
        # return str(self) + str(other)

#    def __radd__(other, self):
#        # предполагается, что объект нашего класса расположен СПРАВА от плюсика
#        return str(self) + str(other)

    # def __radd__(b, a):
        # предполагается, что объект нашего класса расположен СПРАВА от плюсика
        # return str(a) + str(b)

    # ВЫ НЕ МОЖЕТЕ НАЗНАЧИТЬ СВОЙ ЗНАЧОЧЕК!

    # [] __getitem__(self, key)
    # in __contains__(self, item)   item in self

class Drob:
    def __init__(self, ch, zn):
        self.__ch = ch
        self.__zn = zn

    def __str__(self):
        return ' ' + str(self.__ch) + ' \n---\n ' + str(self.__zn) 
        #return str(self.__ch) + '/' + str(self.__zn)
    def __add__(self, other):
       return Drob(28 + 21, 49)
    str(self) + str(other)
    
d = Drob(4, 7)
f = Drob(3, 7)
print(d)