# В общественном транспорте действует система скидок. Если Вы старше 50 лет или младше 14-ти - проезд бесплатный.
# Если Вы студент(14-24 года), проезд за полцены. Программа предлагает ввести год рождения и тариф
# "час", "неделя", "месяц" или "год". Час стоит 60 рублей, неделя 300 рублей, месяц 1000 рублей и год 10 тысяч
# для взрослого человека, не попадающего в льготную категорию. Вычислить стоимость проездного указанного тарифа
# для рассматриваемого гражданина и вывести сообщение на экран.

chelovek = {
    'den': 60,
    'nedelya': 300,
    'mesyac': 1000,
    'god': 10000
}
vozrast = int(input('сколько Вам лет? '))

# бесплатные
if (vozrast < 14) or (vozrast >= 50):
    print('besplatno')

tarif = int(input('какой тариф нада? день - 1, неделя - 2, месяц - 3, год - 4 '))

# человек
if ((24 < vozrast) and (vozrast < 50)) and (tarif == 1):
    print(chelovek['den'])
if ((24 < vozrast) and (vozrast < 50)) and (tarif == 2):
    print(chelovek['nedelya'])
if ((24 < vozrast) and (vozrast < 50)) and (tarif == 3):
    print(chelovek['mesyac'])
if ((24 < vozrast) and (vozrast < 50)) and (tarif == 4):
    print(chelovek['god'])

# студент
if ((14 <= vozrast) and (vozrast <= 24)) and (tarif == 1):
    print(chelovek['den'] // 2)
if ((14 <= vozrast) and (vozrast <= 24)) and (tarif == 2):
    print(chelovek['nedelya'] // 2)
if ((14 <= vozrast) and (vozrast <= 24)) and (tarif == 3):
    print(chelovek['mesyac'] // 2)
if ((14 <= vozrast) and (vozrast <= 24)) and (tarif == 4):
    print(chelovek['god'] // 2)
