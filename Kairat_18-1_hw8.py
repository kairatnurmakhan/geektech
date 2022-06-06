from random import randint as rd
from datetime import datetime as dt
name = input("Укажите имя:")
attempts = int(input('Сколько попыток?'))
count = 0
start = dt.now()
with open('results.txt', 'a', encoding="utf-8") as fl:
    while True:
        try:
            if count == attempts:
                print('Попытки закончились!')
                break
            else:
                count +=1
                a = rd(1, 9)
                b = rd(1, 9)
                answer = int(input(f'{a} * {b} = ?'))
                right_answer = a * b
                print(right_answer)
                if answer == right_answer:
                    fl.write(f'{a} * {b} = {answer} ({right_answer}) правильно\n')
                else:
                    fl.write(f'{a} * {b} = {answer} ({right_answer}) неправильно\n')
        except ValueError:
                print('Только цифры')
                count -= 1
    fl.write(f'Было {count} попыток, потраченное время {dt.now() - start}, имя: {name}\n')
         

    
