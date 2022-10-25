import math

class circle():
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        print(2 * self.radius * math.pi)

    def getArea(self):
        print(self.radius * self.radius * math.pi)

    def setRadius(self, radius):
        self.radius = radius 


         
