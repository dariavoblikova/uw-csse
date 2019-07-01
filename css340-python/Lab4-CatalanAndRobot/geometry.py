class Point:
    def __init__(self, x = 0, y =0):
        self.__x = x
        self.__y = y

    def moveDown(self):
        self.__y -= 1
    def moveUp(self):
        self.__y += 1
    def moveLeft(self):
        self.__x -= 1
    def moveRight(self):
        self.__x += 1
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y =y

    def __eq__(point1, point2):
        if point1.__x == point2.__x and point1.__y == point2.__y:
            return True
        else:
            return False

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"