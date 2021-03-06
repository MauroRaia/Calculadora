# -*- coding: utf-8 -*-
import math

class Logic_Unit():

    def __init__(self):
        self.result = 0
        self.fnum = 0
        self.snum = 0

    def logWithBase(self, x):
        r = math.log(x, 10)
        self.result = r

    def cos(self, x):
        r = math.cos(x)
        self.result = r

    def sin(self, x):
        r = math.sin(x)
        self.result = r

    def tan(self, x):
        r = math.tan(x)
        self.result = r

    def squareRoot(self, x):
        r = math.sqrt(x)
        self.result = r

    def exponent(self, x,):
        r = (x ** 2)
        self.result = r

    def exponentX(self, x, y):
        r = (x ** y)
        self.result = r



