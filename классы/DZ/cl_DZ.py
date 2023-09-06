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
        return 'город ' + self.__gorod + ', улица ' + self.__ulitca + ', дом ' + self.__dom + ', помещение ' + self.__pomeshenie
    
class Stroenie(Adres):
    def __init__(self, god, podiezdy, etaji, adres):
        self.__god = god
        self.__podiezdy = podiezdy
        self.__etaji = etaji
        self.__adres = adres

    @property
    def opisanie(self):
        return 'год постройки - ' + self.__god + ', количество подъездов - ' + self.__podiezdy + ', количество этажей - ' + self.__etaji + ', адрес: ' + self.__adres        

dom = Stroenie('1964', '1', '10', Adres('Москва', 'Плюшкина', '4', '7'))
acad = Stroenie('1976', '3', '6', Adres('Москва', 'Колотушкина', '7', '94'))
rab = Stroenie('1990', '2', '7', Adres('Москва', 'Пушкина', '1', 'офис-3'))

print(dom.opisanie)
print(acad.opisanie)
print(rab.opisanie)