# Усложнение: человек вводит своё имя.
# В "базе данных" хранится для каждого человека количество взятых дней отпуска. {'Вася': 42}

sotrudnyki = {
    'Катя': 30,
    'Вася': 42,
    'Маша': 24,
    'Петя': 15
}
name_sotrudnika = input('Введите имя сотрудника (Катя, Вася, Маша, Петя): ')
first_month = int(input('Первый месяц (1-12): '))
second_month = int(input('Последний месяц (1-12): '))
day = (second_month - first_month) * 2   # если изначально у него стандартный отпуск, то +28 (или сколько там он должен быть)

if name_sotrudnika:
    sotrudnyki[name_sotrudnika] -= day

print('Дни отпуска сотрудника', name_sotrudnika, ':', sotrudnyki[name_sotrudnika])