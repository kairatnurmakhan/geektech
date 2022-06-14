from datetime import datetime as dt
start = dt.now()
print(start)
from random import randint as rd
attempts = 0
numb = ""
random = rd(1, 101)
while numb != random:
    try:
        attempts +=1
        numb = int(input('Введите число:'))
        print(random)

        if 1 > numb or numb > 100:
            raise
        elif numb < random:
            print(f'> {numb}')
            continue
        elif numb > random:
            print(f'< {numb}')
            continue
        else:
            print('Браво, ты угадал!')
            break

    except ValueError:
        print('Только цифры')
        attempts-=1
    except RuntimeError:
        print('Вводите только числа 1 до 100')
        attempts -= 1
result = (dt.now() - start)
print(f'Количество попыток: {attempts}')
print(f'Время игры: {result}')

