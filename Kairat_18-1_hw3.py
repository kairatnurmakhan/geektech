data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
data = list(data_tuple)
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
letters.append(numbers.pop(1))
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'
del numbers[0]
numbers = sorted(numbers)
numbers.insert(1, 2)
numbers = [i ** 2 for i in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
