from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, second_obj):
        return sqrt(pow(self.x - second_obj.x, 2) + pow(self.y - second_obj.y, 2))


# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
#
# print(p1.dist(p2))
