while True:
    try:
        free_cup = int(input('Сколько чашек кофе желаете?: ')) // 6
        print(f'Кол-во бонусных чашек: {free_cup}')
    except ValueError:
        print('Ошибочка получается...')
