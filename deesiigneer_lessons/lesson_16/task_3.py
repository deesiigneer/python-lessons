while True:
    try:
        chicken, cow, pig = map(int, input('Введите кол-во кур, коров и свиней через пробел: ').split())
        print(f'Кол-во ног всех животных: {(chicken*2)+(cow+pig)*4}')
    except ValueError:
        print('Ошибочка получается...')
