try:
    n1 = int(input('Введите первое число: '))
    n2 = int(input('Введите второе число: '))

    a = []
    a.append(n1)
    a.append(n2)

    print("большее число:",(max(a)))

except ValueError:
    print('')
