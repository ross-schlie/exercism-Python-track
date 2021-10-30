"""exercism complex numbers module."""

import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        """
        The sum of two complex numbers involves adding their real and imaginary parts separately:
        `(a + i * b) + (c + i * d) = (a + c) + (b + d) * i`,
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        """
        Multiplication result is by definition
        `(a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i`.
        """

        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        """
        The difference of two complex numbers involves subtracting their real and imaginary parts separately:
        `(a + i * b) - (c + i * d) = (a - c) + (b - d) * i`.
        """
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        """
        Dividing a complex number `a + i * b` by another `c + i * d` gives:
        `(a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i`.
        """

        real = self.real * other.real + self.imaginary * other.imaginary
        real = real / (other.real ** 2 + other.imaginary ** 2)

        imaginary = self.imaginary * other.real - self.real * other.imaginary
        imaginary = imaginary / (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        """
        The absolute value of a complex number `z = a + b * i`
        is a real number `|z| = sqrt(a^2 + b^2)`.
        """
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        """The conjugate of the number `a + b * i` is the number `a - b * i`."""
        self.imaginary = self.imaginary * -1
        return self

    def exp(self):
        """
        Raising e to a complex exponent can be expressed as `e^(a + i * b) = e^a * e^(i * b)`,
        the last term of which is given by Euler's formula `e^(i * b) = cos(b) + i * sin(b)`.
        """
        # a = int(math.exp(self.real))
        # eulers_f = math.cos(self.imaginary) + math.sin(self.imaginary)
        # b = int(math.exp(eulers_f))
        # return ComplexNumber(a * eulers_f, 0)
        a = math.e ** self.real
        eulers_f = math.cos(self.imaginary) + -1 * math.sin(self.imaginary)
        a = a * int(eulers_f)
        return ComplexNumber(a, 0)
