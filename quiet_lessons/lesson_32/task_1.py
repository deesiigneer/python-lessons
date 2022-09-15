while True:
    try:
        first_list = map(int, input('Введите перечень цифр через запятую: ').split(','))
        first_list = [i for i in first_list if i % 2 != 0]
        second_list = map(int, input('Введите второй перечень цифр через запятую: ').split(','))
        second_list = [i for i in second_list if i % 2 == 0]
        joined_list = first_list + second_list
        print(f'Результат: {joined_list}')
    except ValueError:
        print('Некорректный тип ввода данных!')
