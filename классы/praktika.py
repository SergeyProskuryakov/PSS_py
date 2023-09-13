# написать класс для подключения к почтовому клиенту
class Client:
    def __init__(self, login, domen):
        self.__login = login
        self.__domen = domen
    
    @property
    def adres(self):
        return self.__login + '@' + self.__domen

au = Client('alisawera', 'gmail.com')
print(au.adres)