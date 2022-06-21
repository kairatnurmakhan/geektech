#Написать функцию, которая возвращает первое слово из полученного предложения.
def word(text="Hello wold"):
      if text.isdigit():
            return False
      lst = text.split()
      return lst[0]
words = input("Enter words: ")
print(word(words))



#Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое.
 def middle_arif(*args):
      return sum(args) // len(args)
numbers = middle_arif(31, 32, 3, 4, 5, 23, 4, 23)
print(numbers)


#Написать функцию, проверяющую надежность пароля.
def check_pass(password: str):
      if len(password) > 6:
            if (not password.isalpha()) and (not password.isdigit()):
                  return True
      return False

x = input("Enter password: ")
print(check_pass(x))
