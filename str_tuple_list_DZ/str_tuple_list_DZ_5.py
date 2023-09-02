# 5. С помощью только for сделать задачю 4

goods = {
    'item_1': 45,
    'item_2': 657,
    'item_3': 123
}
header = 15
horizon = '+' + '-' * header + '+' + '-' * header + '+'
summa = 0
print(horizon)

for item in goods:
    template_1 = '|%%(name)%(size)ss' % {'size': header}
    template_2 = '|%%(price)%(size)ss' % {'size': header}
    products = template_1 % {'name': item} + template_2 % {'price': goods[item]} + '|' + '\n'
    print(products + horizon)
    summa += goods[item]

total_price = '|' + (' ' * (header - 4)) + 'Итог|' + (' ' * (header - 3)) + str(summa) + '|' + '\n'
print(total_price + horizon)