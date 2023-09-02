# 4. Вывести на экран таблицу из 4 строк: три товара и сумма без использования цикла

goods = {
    'item_1': 45,
    'item_2': 657,
    'item_3': 123
}

horizon = '+' + '-' * 15 + '+' + '-' * 15 + '+' + '\n'
prod_1 = '|%(name)15s' % {'name': 'item_1'} + '|' + '%(price)15i' %{'price': goods['item_1']} + '|' + '\n'
prod_2 = '|%(name)15s' % {'name': 'item_2'} + '|' + '%(price)15i' %{'price': goods['item_2']} + '|' + '\n'
prod_3 = '|%(name)15s' % {'name': 'item_3'} + '|' + '%(price)15i' %{'price': goods['item_3']} + '|' + '\n'
total_price = '|' + (' ' * 10) + 'Итог |' + str(goods['item_1'] + goods['item_2'] + goods['item_3']) + (' ' * 12) + '|' + '\n'
print(horizon + prod_1 + prod_2 + prod_3 + total_price + horizon)