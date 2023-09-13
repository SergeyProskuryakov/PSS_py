# Создать класс Строение с полем Адрес
# (для тех, кто всё понял, Адрес можно сделать не строкой, а классом!)

# Бонус: Продемонстрировать работу с объектами класса
# 1. Объект "Дом" - ваш адрес, инициализация, "переезд" - смена адреса,
#    отображение (получение, property - getter) адреса
# 2. Объект "Академия"
# 3. Объект "Работа"

class Adres:
    def __init__(self, gorod, ulitca, dom, pomeshenie):
        self.__gorod = gorod
        self.__ulitca = ulitca
        self.__dom = dom
        self.__pomeshenie = pomeshenie

    @property
    def adres(self):
        return 'город %(sity)s, улица %(street)s, дом %(building)i, помещение %(room)s' %{
            'sity': self.__gorod,
            'street': self.__ulitca,
            'building': self.__dom,
            'room': self.__pomeshenie
        }
    
class Stroenie:
    def __init__(self, name, god, podiezdy, etaji, adres):
        self.__name = name
        self.__god = god
        self.__podiezdy = podiezdy
        self.__etaji = etaji
        self.__adres = adres

    @property
    def opisanie(self):
        return '''%(build)s: \nгод постройки - %(year)i, \nколичество подъездов - %(entrance)i, 
количество этажей - %(levels)i, \nадрес - %(adress)s''' % {
            'build': self.__name,
            'year': self.__god,
            'entrance': self.__podiezdy,
            'levels': self.__etaji,
            'adress': self.__adres.adres  
        }

dom = Stroenie('дом', 1964, 1, 10, Adres('Москва', 'Плюшкина', 4, '7'))
acad = Stroenie('академия', 1976, 3, 6, Adres('Москва', 'Колотушкина', 7, '94'))
rab = Stroenie('работа', 1990, 2, 7, Adres('Москва', 'Пушкина', 1, 'офис-3'))

print(dom.opisanie)
print(acad.opisanie)
print(rab.opisanie)