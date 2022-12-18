class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):

        if self.numerator == 0:
            value = ' gives you 0!'

        elif self.denominator == 0:
            value = ' denominator != 0'

        elif self.numerator == self.denominator:
            value =" %d" % (self.numerator)
        else:
            value ="%d/%d" % (self.numerator, self.denominator)
        return value


    def __add__(self, num):
        if isinstance(num, int):
            num = Fraction(num)
        return Fraction(self.numerator * num.denominator +
                    self.denominator * num.numerator,
                    self.denominator * num.denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)