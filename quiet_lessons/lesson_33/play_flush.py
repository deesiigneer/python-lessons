table_cards = ['A_S', 'J_H', '7_D', '8_D', '10_D']
hand_cards = ['J_D', '3_D']
print(f'Карты на столе: {table_cards}')
print(f'Карты на руках: {hand_cards}')
sum_cards = table_cards + hand_cards
sum_cards = [i[-1] for i in sum_cards]
no_duplicates = set(sum_cards)
for i in no_duplicates:
    if sum_cards.count(i) == 5:
        print('У вас флеш!')