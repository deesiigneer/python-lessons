while True:
    try:
        for star in range(int(input('Введите кол-во строк: '))):
            print(f'*' * (star + 1))
    except ValueError:
        print('Ошибочка получается...')
