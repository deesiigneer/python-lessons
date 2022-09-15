while True:
    try:
        limit = int(input('Введите лимит: '))
        summa = sum(i for i in range(limit + 1) if i % 3 == 0 or i % 5 == 0)
        print(summa)
    except ValueError:
        print('Некорректный тип ввода данных!')
