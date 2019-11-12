from q1 import Point, result


def arr_print(array):
    for x in array:
        print(x)


def average_line(arr_points):
    stored_x = [point.get_x() for point in arr_points]

    stored_x = sorted(stored_x)
    avg = (
                  stored_x[int(len(stored_x) / 2)]
                  + stored_x[int((len(stored_x) / 2) - 1)]
          ) / 2
    print("Average LINE:", avg)
    return avg


def get_distance(a, b):
    x_one = a.get_x()
    y_one = a.get_y()
    x_two = b.get_x()
    y_two = b.get_y()
    result = (((x_two - x_one) ** 2) + (
            (y_two - y_one) ** 2
    )) ** 0.5
    print("RESULT:", result)
    return result


class RecurOne:

    def __init__(self):
        self.arr_points = []
        self.p1 = Point(0, 0, "")
        self.p2 = Point(0, 0, "")
        self.res = result(self.p1, self.p2, 1000)

    def __str__(self):
        return self.name + self.x

    def find_minimum(self, points):
        if len(points) is 1:
            return None
        if len(points) is 2:
            if get_distance(points[0], points[1])< self.res.minDist:
                print("HELLO: ", points[0], points[1], get_distance(points[0], points[1]))
                self.res.a = points[0]
                self.res.b = points[1]
                self.res.minDist = get_distance(points[0], points[1])
            return self.res

        else:
            points_l = []
            points_r = []
            avg_line = average_line(points)
            for x in range(0, len(points)):
                if points[x].get_x() >= avg_line:
                    points_r.append(points[x])
                if points[x].get_x() < avg_line:
                    points_l.append(points[x])
            print("LEFT: ", print_array(points_l))
            print("RIGHT: ", print_array(points_r))
            res_l = self.find_minimum(points_l)
            res_r = self.find_minimum(points_r)
            print(res_l)
            print(res_r)

            if res_l is None or res_r is None:
                rt = result(
                    points_l[0],

                    points_r[0],
                    get_distance(points_l[0],
                                 points_r[0]),
                )
                return rt

            if res_l.minDistance() <= res_r.minDistance():
                minim = res_l.minDist
                check_val= (minim <= self.res.minDist)
                print("LEFT_MIN: ", minim, self.res.minDist, check_val)

                if check_val:
                    self.p1 = res_l.a
                    self.p2 = res_l.b
                    self.res.minDist = minim

            else:
                minim = res_r.minDist
                check_val = (minim <= self.res.minDist)

                print("RIGHT_MIN: ", minim, self.res.minDist, minim < self.res.minDist)
                if check_val:
                    self.res.minDist = minim
                    self.p1 = res_r.a
                    self.p2 = res_r.b

            print("Minimum so far", minim)
            points_in_range = []
            for x in points:
                if (avg_line + (minim / 2)) > x.get_x() > (avg_line - (minim / 2)):
                    points_in_range.append(x)
            self.res = result(self.p1, self.p2, minim)
            ans = self.find_minimum(points_in_range).minDist
            print("ANS:", ans)
            if ans < minim:
                self.res.minDist = ans
            return self.res

    def main(self):
        p_zero = Point(3, 2, "0")
        p_one = Point(-6, 7, "1")
        p_two = Point(-1, 4, "2")
        p_three = Point(2, -2, "3")
        p_four = Point(5, -4, "4")
        p_five = Point(-2, 0, "5")
        p_six = Point(-5, 5, "6")
        p_seven = Point(-8, -5, "7")
        # # p_zero = Point(0, -8, "0")
        # p_one = Point(3, -7, "1")
        # p_two = Point(-3, 5, "2")
        # p_three = Point(6, 1, "3")
        # p_four = Point(1, -2, "4")
        # p_five = Point(7, 6, "5")
        # p_six = Point(5, -5, "6")
        # p_seven = Point(-7, 7, "7")
        self.arr_points.append(p_zero)
        self.arr_points.append(p_one)
        self.arr_points.append(p_two)
        self.arr_points.append(p_three)
        self.arr_points.append(p_four)
        self.arr_points.append(p_five)
        self.arr_points.append(p_six)
        self.arr_points.append(p_seven)
        self.arr_points.sort(key= lambda q: q.x)
        res = self.find_minimum(self.arr_points)
        print("FINAL RESULT:", res)
        return


def print_array(arr_point):
    output = "["
    for i in arr_point:
        output = output + i.get_name() + ","
    output = output + "]"
    return output


if __name__ == "__main__":
    r1 = RecurOne()
    r1.main()
