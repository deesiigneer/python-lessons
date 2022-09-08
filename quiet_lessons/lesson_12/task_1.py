while True:
    try:
        count_stars = int(input('Введите кол-во строк: '))
        for _ in range(count_stars + 1):
            print('*' * _)
    except ValueError:
        print('Некорректный тип ввода данных!')
