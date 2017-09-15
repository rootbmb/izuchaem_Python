ages = [1, 3, 10, 17, 25, 67]

for age in ages:


    if age < 2:
        print('Младенец')
    elif age >= 2 and age < 4:
        print('Малыш')
    elif age >= 4 and age < 13:
        print('Ребенок')
    elif age >=13 and age < 20:
        print('Подросток')
    elif age >= 20 and age < 65:
        print('Взрослый')
    elif age >= 65:
        print('Пожилой')
