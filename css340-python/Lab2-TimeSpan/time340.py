import math

class TimeSpan:

    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60

    def __init__(self, seconds = 0, minutes = None, hours = None):
        self.__seconds = round(seconds)
        if minutes is not None:
            self.__minutes = minutes
        else:
            self.__minutes = 0
        if hours is not None:
            self.__hours = hours
        else:
            self.__hours = 0
        self.simplify()
    
    def simplify(self):
        if self.__hours != math.trunc(self.__hours):
            if self.__hours > 0:
                self.__minutes += round((self.__hours % math.trunc(self.__hours)) * self.MINUTES_IN_HOUR)
            if self.__hours < 0:
                self.__minutes -= round((abs(self.__hours) % abs(math.trunc(self.__hours))) * self.MINUTES_IN_HOUR)
            self.__hours = math.trunc(self.__hours)

        if self.__minutes != math.trunc(self.__minutes):
            if self.__minutes > 0:
                self.__seconds += round((self.__minutes % math.trunc(self.__minutes)) * self.SECONDS_IN_MINUTE)
            if self.__minutes < 0:
                self.__seconds -= round((abs(self.__minutes) % abs(math.trunc(self.__minutes))) * self.SECONDS_IN_MINUTE)
            self.__minutes = math.trunc(self.__minutes)

        if self.__seconds != math.trunc(self.__seconds):
            self.__seconds = round(self.__seconds)

        if self.__seconds >= self.SECONDS_IN_MINUTE:
            self.__minutes += self.__seconds // self.SECONDS_IN_MINUTE
            self.__seconds = self.__seconds % self.SECONDS_IN_MINUTE
        if self.__seconds <= -self.SECONDS_IN_MINUTE:
            self.__minutes += math.trunc(self.__seconds / self.SECONDS_IN_MINUTE)
            self.__seconds = -(-self.__seconds % self.SECONDS_IN_MINUTE)

        if self.__minutes >= self.MINUTES_IN_HOUR:
            self.__hours += self.__minutes // self.MINUTES_IN_HOUR
            self.__minutes = self.__minutes % self.MINUTES_IN_HOUR
        if self.__minutes <= -self.MINUTES_IN_HOUR:
            self.__hours += math.trunc(self.__minutes / self.MINUTES_IN_HOUR)
            self.__minutes = -(-self.__minutes % self.MINUTES_IN_HOUR)

        if self.__minutes < 0 and self.__hours > 0:
            self.__hours = self.__hours - 1
            self.__minutes = self.MINUTES_IN_HOUR + self.__minutes

        if self.__seconds < 0 and self.__minutes > 0:
            self.__minutes = self.__minutes - 1
            self.__seconds = self.SECONDS_IN_MINUTE + self.__seconds


    def getHours(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    def setTime(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
        self.simplify()
        return True

    def __add__(self, rhs):
        tempDur = TimeSpan()
        tempDur.setTime(self.getSeconds() + rhs.getSeconds(), self.getMinutes() + rhs.getMinutes(), self.getHours() + rhs.getHours())
        return tempDur


    def __sub__(self, rhs):
        tempDur = TimeSpan()
        tempDur.setTime(self.getSeconds() - rhs.getSeconds(), self.getMinutes() - rhs.getMinutes(), self.getHours() - rhs.getHours())
        return tempDur

    def __neg__(self):
        self.__seconds = self.__seconds * (-1)
        self.__minutes = self.__minutes * (-1)
        self.__hours = self.__hours * (-1)
        self.simplify()
        return self

    def __lt__(self, rhs):
        if self.getHours() < rhs.getHours():
            return True
        elif self.getHours() == rhs.getHours():
            if self.getMinutes() < rhs.getMinutes():
                return True
            elif self.getMinutes() == rhs.getMinutes():
                if self.getSeconds() < rhs.getSeconds():
                    return True
        return False
    
    def __eq__(self, rhs):
        if self.getSeconds() == rhs.getSeconds() and self.getMinutes() == rhs.getMinutes() and self.getHours() == rhs.getHours():
            return True
        else:
            return False

    def __le__(self, rhs):
        if self < rhs or self == rhs:
            return True
        else:
            return False

    def __ne__(self, rhs):
        if self == rhs:
            return False
        else:
            return True

    def __ge__(self, rhs):
        if self > rhs or self == rhs:
            return True
        else:
            return False

    def __gt__(self, rhs):
        if self < rhs:
            return False
        else:
            return True

    def __str__(self):
        return "Hours: " + str(self.__hours) + ", Minutes: " + str(self.__minutes) + ", Seconds: " + str(self.__seconds)



