import sys
from robot import Robot
from geometry import Point


#robot = Point(1, 2)
#treasure = Point(3, 5)

#r = Robot()
#count = r.shortestPaths(robot, treasure, "", 0)
#print("Number of paths: " + str(count))


if __name__ == "__main__":
    robot = Point(int(sys.argv[1]), int(sys.argv[2]))
    treasure = Point(int(sys.argv[3]), int(sys.argv[4]))

    r = Robot()
    count = r.shortestPaths(robot, treasure, "", 0)
    print("Number of paths: " + str(count))