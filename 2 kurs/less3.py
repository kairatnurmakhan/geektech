#     # __add__ # сложение
#     # __sub__ # вычитание
#     # __mul__ # умножение
#     # __div__ # деление
#     #__str__# информация об обьекте
#     #__repr__# информация о классе
# class Num:
#
#     def __init__(self, num):
#         self.num = num
#
#     def __add__(self, other):
#         print("method __add__ called")
#         self.num += other
#         return Num(self.num)
#
#
#     def __sub__(self, other):
#         print("method __sub__ called")
#         self.num -= other
#         return Num(self.num)
#
#
#     def __str__(self):
#         return f"Num: {self.num}"
#
#
#     def __reor__(self):
#         print(f'Num({self.num}')
#         return
#
#
#
# num1 = Num(20)
# num2 = num1 + 20 - 10
#
# print(num2)
#
#
#
#
#
#
# class A:
#     def method(self):
#         print('Its method in class A')
#
#
# class B:
#     def method_b(self):
#         print("Its method in class B")
#
# class C(A, B):
#     pass
#
# exm_c = C()
#
# print(exm_c)
# exm_c.method_b()

class A:
    def method_a(self):
        print("Its method in class A")


class B(A):
    def method_a(self):
        print("Its method in class B")

class C(A):
    def method_a(self):
        print("Its method in class C")


class D(C, B):
    pass

exm_a = D()
exm_a.method_a()

print(D.mro())

