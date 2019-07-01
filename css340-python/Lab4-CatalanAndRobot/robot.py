from geometry import Point
import copy

class Robot:

    def robotWest(self, point1, point2, path, count):
        path += 'W'
        p1 = copy.copy(point1)
        p1.moveLeft();
        return self.shortestPaths(p1, point2, path, count)

    def robotEast(self, point1, point2, path, count):
        path += 'E'
        p1 = copy.copy(point1)
        p1.moveRight()
        return self.shortestPaths(p1, point2, path, count)

    def robotSouth(self, point1, point2, path, count):
        path += 'S'
        p1 = copy.copy(point1)
        p1.moveDown()
        return self.shortestPaths(p1, point2, path, count)

    def robotNorth(self, point1, point2, path, count):
        path += 'N'
        p1 = copy.copy(point1)
        p1.moveUp()
        return self.shortestPaths(p1, point2, path, count)


    def shortestPaths(self, point1, point2, path, count):
        if point1 == point2:
            count += 1
            print(path)
            return count
        
        if point1.getY() < point2.getY():
            count = self.robotNorth(point1, point2, path, count)

        if point1.getY() > point2.getY():
            count = self.robotSouth(point1, point2, path, count)

        if point1.getX() < point2.getX():
            count = self.robotEast(point1, point2, path, count)

        if point1.getX() > point2.getX():
            count = self.robotWest(point1, point2, path, count)

        return count
