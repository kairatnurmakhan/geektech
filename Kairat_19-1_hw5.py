
import re

class ValidCarNumber:
    def __init__(self, number):
        self.number = number


    def is_valid(self):
        self.number.upper()


        if re.search(r'0([1-9])KG([0-9]{3})([a-zA-Z]{3})' , self.number):
            print(f'Номер {self.number} валидный!')
        else:
            print(f'Номер {self.number} не валидный!')

num1 = ValidCarNumber(input('Введите номер машины: '))

num1.is_valid()

