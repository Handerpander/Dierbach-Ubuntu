import math

class Shape:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getXYLoc(self):
        return(self.__x, self.__y)
    
    def setXYLoc(self, x, y):
        self.__x = x
        self.__y = y

    def calcArea(self):
        raise NotImplementedError('Method calcArea not implemented')
    
class Circle(Shape):

    def __init__(self, x, y, r):
        Shape.__init__(self, x, y, r)
        self.__radius = r

    def calcArea(self):
        return math.pi * self.__radius ** 2

class Square(Shape):

    def __init__(self, x, y, s):
        Shape.__init__(self, x, y)
        self.__side = s

    def calcArea(self):
        return self.__side ** 2
    
class Triangle(Shape):

    def __init__(self, x, y, s):
        Shape.__init__(self, x, y)
        self.__side = s

    def calcArea(self):
        return (self.__side ** 2) * math.sqrt(3) / 4.0