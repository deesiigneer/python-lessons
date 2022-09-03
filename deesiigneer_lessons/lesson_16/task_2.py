while True:
    try:
        x, y = map(int, input('Введите координат для первой точки через пробел: ').split())
        x1, y1 = map(int, input('Введите значение координат для второй точки через пробел: ').split())
        from math import sqrt
        print(round(sqrt((x-x1)**2+(y-y1)**2), 3))
    except ValueError:
        print('Ошибочка получается...')
