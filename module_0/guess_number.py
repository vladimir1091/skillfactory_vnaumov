import random
import numpy as np


def game_upgraded(number):
    """Усовершенственный алгоритм, угадывающий число, использующий информацию о больше или меньше,
        Функция принимает рандомное число от 0 до 100 и возвращает число попыток"""
    start = 0   # От данного числа алгоритм будет отгадывать
    end = 101   # До данного числа алгоритм будет отгадывать
    count = 0   # Счетчик попыток
    while True:
        count += 1
        predict = random.randint(start, end)
        if predict == number:   # Условия для выхода из цикла, угаданное число
            break
        elif predict > number:  # Если загаданное число > предложенного,
            end = predict       # то в след. попытке алгоритм будет загадывать начиная от него
        else:                   # Если загаданное число < предложенного,
            start = predict     # то в след. попытке алгоритм будет загадывать начиная до него
    return count


def score_game(game_core):
    """Функция запускает игру 1000 раз и выдает средннее колл-во попыток"""
    tries_list = []
    random_list = []
    n = 0
    while n < 1000:
        n += 1
        random_list.append(random.randint(0, 101))
    for number in random_list:
        tries_list.append(game_core(number))
    print(f'Алгоритм угадывает число в среднем за {int(np.mean(tries_list))} попыток')


score_game(game_upgraded)   # Результат: ---> 'Алгоритм угадывает число в среднем за 9 попыток'
