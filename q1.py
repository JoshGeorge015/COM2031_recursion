class Point:
    # int x
    # int y
    # str name

    def __init__(self, new_x, new_y, new_name):
        self.x = new_x
        self.y = new_y
        self.name = new_name

    def get_name(self):
        return str(self.name)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return str(self.name)


class result:

    # Point a, Point b
    # def __init__(Point A, Point B, dist):
    def __init__(self, A, B, dist):

        self.a = A
        self.b = B
        self.minDist = dist

    # def __init__(self, dist):
    #     self.minDist = dist
    def minDistance(self):
        return float(self.minDist)

    def __str__(self):
        return "result [a=" + self.a.name + ", b=" + self.b.name + ", minDistance=" + str(self.minDist) + "]"



if __name__ == '__main__':
    p = Point(1,2,"fat")
    p2 = Point(1, 3, "THat")

    r = result(p,p2,1)
    print(p.name)