# 2. Напишите программу, которая спрашивает год рождения и в случае выхода его за разумные
#    земные значения требует повторить ввод. Считаем, что человек живет не более 200 лет и к компьютеру раньше двух лет не подходит.

final_year = 2023
god_rojd = input('ваш год рождения: ')
god_rojd = int(god_rojd)
while (god_rojd >= final_year) or (god_rojd < 1800):
    god_rojd = int(input('ваш год рождения: '))
