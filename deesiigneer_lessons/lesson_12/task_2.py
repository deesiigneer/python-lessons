while True:
    try:
        for number in range(int(input('введите любое число: ')) + 1):
            print(f'{number} is EVEN') if number % 2 == 0 else print(f'{number} is ODD')
    except ValueError:
        print('Некорректный тип ввода данных!')
