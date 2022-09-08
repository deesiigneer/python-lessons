while True:
    try:
        number = int(input('Введите число: '))
        for num_in_diapason in range(number + 1):
            if num_in_diapason % 2 == 0:
                print(f'{num_in_diapason} is EVEN')
            else:
                print(f'{num_in_diapason} is ODD')
    except ValueError:
        print('Некорректный тип ввода данных!')