
class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"


    def __add__(self, other):
        self.numerator += other
        self.denumerator += other
        print(f"method add {self.numerator}/{self.denumerator} called")

    def __sub__(self, other):
        self.numerator -= other
        self.denumerator -= other
        print(f"method sub {self.numerator}/{self.denumerator} called")


    def __mul__(self, other):
        self.numerator *= other
        self.denumerator *= other
        print(f"method mul {self.numerator}/{self.denumerator} called")


    def __floordiv__(self, other):
        self.numerator //= other
        self.denumerator //= other
        print(f"method floordiv {self.numerator}/{self.denumerator} called")

num = Fraction(15, 4)
print(f"Its Fraction {num}")

num_add = num + 2
num_sub = num - 4
num_mul = num * 2
num_floordiv = num // 3




