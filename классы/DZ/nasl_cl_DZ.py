# 1. Проверить, как в питоне реализовано множественное наследование.
# Интересует проблема одинаковых полей и методов в паре родительских классов.
# Как они унаследуются? Как получить доступ к обоим?

# 2. Рассмотреть проблему "ромбовидного" наследования

# 3. Задача для всех, строго по наследованию одного класса:

# Создать класс "помещение"
# У него должны быть указаны приватно ширина, длина, высота,
# количество дверей и окон - "защищённо" (через одно подчеркивание)

# Создать наследные классы:
# зрительный зал (ряды и стулья в рядах)
# учебный класс (кол-во компьютеров)
# Спортивный зал

# Методы: __str__

# Желательно унаследовать и использовать родительские __init__ и __str__,
# используя функцию super()

class Pomeshenie:

    def __init__(self, name, shirina, dlina, visota, dveri, okna):
        self.__name = name
        self.__shirina = shirina
        self.__dlina = dlina
        self.__visota = visota
        self._dveri = dveri
        self._okna = okna

    def __str__(self):
        return '\n' + ("*" * 30) + '\n\n{0}:\nплощадь - {1},\nвысота - {2},\nколичество окон - {3},\nдверей - {4}'.format(
            self.__name, (self.__dlina * self.__shirina), self.__visota, self._okna, self._dveri) 

class Zritelniy_zal(Pomeshenie):

    def __init__(self, name, shirina, dlina, visota, dveri, okna, ryad, stulya):
        super().__init__(name, shirina, dlina, visota, dveri, okna)
        self.__ryad = ryad
        self.__stulya = stulya

    @property
    def zrit(self):
        return '\nколичество рядов - {0},\nколичество стульев - {1}'.format(self.__ryad, self.__stulya)

class Uchebniy_class(Zritelniy_zal):

    def __init__(self, name, shirina, dlina, visota, dveri, okna, stulya, komp):
        super().__init__(name, shirina, dlina, visota, dveri, okna, stulya)
        self.__komp = komp

    @property
    def uch(self):
        return '\nколичество компьютеров - {0}'.format(self.__komp)

class Sportzal(Pomeshenie):

    def __init__(self, name, shirina, dlina, visota, dveri, okna, fizrukov):
        super().__init__(name, shirina, dlina, visota, dveri, okna)
        self._fizrukov = fizrukov

    @property
    def fiz(self):
        return '\nколичество физруков - {0}'.format(self._fizrukov)
    

zritelniy_zal = Zritelniy_zal('зрительный зал', 20, 15, 4, 2, 1, 5, 30)
print(zritelniy_zal, zritelniy_zal.zrit)

uchebniy_class = Uchebniy_class('учебный класс', 20, 20, 4, 1, 5, 15, 15)
print(uchebniy_class, uchebniy_class.uch)

sportzal = Sportzal('спортзал', 70, 50, 7, 3, 12, 3)
print(sportzal, sportzal.fiz)