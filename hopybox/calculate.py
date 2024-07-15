import math
import sympy

from math import *


class NumberError(Exception):
    def __init__(self):
        super().__init__("Wrong number type or combination")


class Calculate:
    class Function:
        def __init__(self, function):
            self.x = sympy.symbols("x")
            self.function = function

        def derivative(self, num):
            return sympy.diff(sympy.sympify(self.function), self.x, int(num))

    class Expression:
        def run(self, text):
            return eval(
                text,
                {"__builtins__": None},
                {
                    "sin": sin,
                    "cos": cos,
                    "tan": tan,
                    "sqrt": sqrt,
                    "log": log,
                    "exp": exp,
                    "cbrt": cbrt,
                    "radians": radians,
                    "degrees": degrees,
                    "e": e,
                    "pi": pi,
                    "perm": perm,
                    "abs": abs,
                },
            )

    class Triangle:
        def __init__(self, a, b, c):
            if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
                self.a = a
                self.b = b
                self.c = c
            else:
                raise NumberError

        @property
        def area(self):
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

        @property
        def perimeter(self):
            return self.a + self.b + self.c

    class Circle:
        def __init__(self, radius):
            if radius > 0:
                self.radius = radius
            else:
                raise NumberError

        @property
        def area(self):
            return math.pi * (self.radius**2)

        @property
        def perimeter(self):
            return 2 * math.pi * self.radius

        @property
        def diameter(self):
            return self.radius * 2


calculate = Calculate()
