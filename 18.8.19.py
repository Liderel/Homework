summa = 0
bilet = int(input('Количество билетов: '))
for count in range(bilet):
    count += 1
    age = int(input(f'Возраст для {count} билета: '))
    if age < 18:
        print('Проход бесплатен')
    elif 18 <= age < 25:
        summa += 990
        print('Стоимость билета: 990 руб.')
    elif age >= 25:
        summa += 1390
        print('Стоимость билета: 1390 руб.')

if bilet <= 3:
    print(f'К оплате {summa} руб. ')
else:
    skidka = summa * 10 / 100
    summa = summa - skidka
    print(f'К оплате {summa} руб. Ваша скидка: {skidka} руб.')