'''Эти люди ходят друг к другу в гости, не пропуская
ни одного дня рождения. Отмечают строго в дату, без
переноса. Приглашаются только знакомые, но они могут привести своих знакомых.

Какого числа Петя познакомится с Катей?                 - у Кости
Сколько человек будет на ближайшем дне рождения Лены?   - 3
Кто будет самым старшим гостем?                         - Костя
Кто самый младший из людей?                             - Петя
Сколько дней до ближайшего дня рождения?                - 69 (у Лены)
Кто туда не придёт?                                     - Петя, Катя
'''
# 1. назначить первого младшим
# 2. 


from datetime import datetime
people = {
    'Вася': {
        'birthday': datetime(2000, 6, 2),
        'friends': ['Катя', 'Лена']},
    'Костя': {
        'birthday': datetime(1965, 4, 17),
        'friends': ['Лена',  'Ира', 'Катя']},
    'Петя': {
        'birthday': datetime(2018, 8, 9),
        'friends': ['Ира']},
    'Лена': {
        'birthday': datetime(1982, 11, 28),
        'friends': ['Вася',  'Костя', 'Ира']},
    'Ира':  {
        'birthday': datetime(1996, 2, 29),
        'friends': ['Костя', 'Петя', 'Лена']},
    'Катя': {
        'birthday': datetime(1953, 5, 31),
        'friends': ['Вася', 'Костя']}
}

imya_ml = 'Вася'
mladshiy = people['Вася']
def mlad(people):
    for imya in people:
        # print(imya, people[imya])
        if mladshiy['birthday'] < people[imya]['birthday']:
            mladshiy = people[imya]
            imya_ml = imya
    return imya_ml

blijaishiy = people['Вася']
def blij(people):
    for imya in people:
        # print(imya, people[imya])
        if mladshiy['birthday'] < people[imya]['birthday']:
            mladshiy = people[imya]
            imya_ml = imya


print(imya_ml)
