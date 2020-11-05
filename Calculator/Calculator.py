from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squaring import squaring
from Calculator.SquareRoot import squareRoot
from Calculator.GetLength import getLength



class Calculator:

    result = 0;

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self, a,b):
        self.result = multiplication(a,b)
        return self.result
    def divide(self, a, b, length):
        self.result = division(a,b, length)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def sqrt(self, a, length):
        self.result = squareRoot(a, length)
        return self.result

    def length(self, a):
        return getLength(a)