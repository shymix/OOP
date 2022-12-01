from fractions import Fraction


class Rational:
    def __init__(self, first: int = 1, second: int = 1):
        if not isinstance(first, int):
            raise TypeError
        if not isinstance(second, int):
            raise TypeError
        self.__a = Fraction(first, second)

    def divide_view(self):
        return self.__a

    def point_view(self):
        return self.__a.numerator / self.__a.denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            num = self.__a.numerator * other.__a.denominator + other.__a.numerator * self.__a.denominator
            denom = self.__a.denominator * other.__a.denominator
            a = Rational(num, denom)
            return a.divide_view()
        if isinstance(other, int):
            a = Rational(self.__a.numerator + other * self.__a.denominator, self.__a.denominator)
            return a.divide_view()

    def __sub__(self, other):
        if isinstance(other, Rational):
            num = self.__a.numerator * other.__a.denominator - other.__a.numerator * self.__a.denominator
            denom = self.__a.denominator * other.__a.denominator
            a = Rational(num, denom)
            return a.divide_view()
        if isinstance(other, int):
            a = Rational(self.__a.numerator - other * self.__a.denominator, self.__a.denominator)
            return a.divide_view()

    def __mul__(self, other):
        if isinstance(other, Rational):
            num = self.__a.numerator * other.__a.numerator
            denom = self.__a.denominator * other.__a.denominator
            a = Rational(num, denom)
            return a.divide_view()
        if isinstance(other, int):
            a = Rational(self.__a.numerator * other, self.__a.denominator)
            return a.divide_view()

    def __truediv__(self, other):
        if isinstance(other, Rational):
            num = self.__a.numerator * other.__a.denominator
            denom = self.__a.denominator * other.__a.numerator
            a = Rational(num, denom)
            return a.divide_view()
        if isinstance(other, int):
            a = Rational(self.__a.numerator, self.__a.denominator * other)
            return a.divide_view()

    def __eq__(self, other):
        if isinstance(other, Rational):
            if(self.__a == other.__a):
                return f'They are equal'
            else:
                return f'They are not equal'
        if isinstance(other, int):
            if (self.__a == other):
                return f'They are equal'
            else:
                return f'They are not equal'


a = Rational(25, 100)
b = Rational(33, 99)
c = 2

print(a + b)
print(a + c)

print(a - b)
print(a - c)

print(a * b)
print(a * c)

print(a / b)
print(a / c)

print(a == b)
