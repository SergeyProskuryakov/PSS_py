# 5. С помощью только for сделать задачю 4

goods = {
    'item_1': 45,
    'item_2': 657,
    'item_3': 123
}
horizon = '+' + '-' * 15 + '+' + '-' * 15 + '+'
summa = 0
print(horizon)

for item in goods:
    products = '|%(name)15s' % {'name': item} + '|' + '%(price)15i' %{'price': goods[item]} + '|' + '\n'
    print(products + horizon)
    summa += goods[item]
    
total_price = '|' + (' ' * 10) + 'Итог |' + (' ' * 12) + str(summa) + '|' + '\n'
print(total_price + horizon)