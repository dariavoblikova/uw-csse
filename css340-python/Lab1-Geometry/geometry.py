import math

class Circle:
    def __init__(self, x = 0, y = 0, radius = 1):
        self.__x = x 
        self.__y = y 
        if radius >= 0:
            self.__radius = radius
        else:
            self.__radius = 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def getRadius(self):
        return self.__radius
    
    def getArea(self):
        return self.__radius * self.__radius * math.pi
        
    def getPerimeter(self):
        return self.__radius * 2 * math.pi

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
    
    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            self.__radius = 1

# this function checks if the point is within circle by comparing the distance between 
# the given point and the center of the circle to the radius of the circle

    def isPointWithinCircle(self, x, y):
        distanceBetweenPointsSquared = (self.__x - x)**2 + (self.__y - y)**2
        return (bool(distanceBetweenPointsSquared <= self.__radius**2))
