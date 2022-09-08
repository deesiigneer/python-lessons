while True:
    try:
        count_stars = int(input('Введите кол-во строк: '))
        for _ in range(count_stars):
            print('*' * (_ + 1))
    except ValueError:
        print('Некорректный тип ввода данных!')
