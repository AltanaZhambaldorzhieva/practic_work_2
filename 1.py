silver = 96
gold = silver/16
total_income = int(input('Сумма с продаж: '))
price_silver = 48
price_gold = (total_income - (silver*price_silver))/gold
print('Стоимость золотых часов равна:', int(price_gold))
