while True:
    try:
        current_hand = list(input('Введите карты на руке через запятую: ').split(','))
        dict_weight = {'2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
                       '7': 0, '8': 0, '9': 0,
                       '10': -1, 'J': -1, 'Q': - 1, 'A': -1}
        cards_sum = sum([dict_weight[i] for i in current_hand])
        print(f'Сумма карт на руке = {cards_sum}')
    except KeyError:
        print('Присутствует несуществующая карта!')
