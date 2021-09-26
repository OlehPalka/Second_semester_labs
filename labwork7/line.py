"""
This module contains point and line classes
"""


class Point:
    """
    Clas which creates points.
    """

    def __init__(self, x, y):
        self.x_0 = x
        self.y_0 = y

    def __eq__(self, obj):
        """
        Redefining == method.
        """
        if isinstance(obj, Point):
            if self.x_0 == obj.x_0 and self.y_0 == obj.y_0:
                return True
            else:
                return False
        else:
            return False


class Line:
    """
    This class creates lines.
    """

    def __init__(self, point_line):
        self.point_line = point_line
        self.y_points = {self.point_line[0].y_0, self.point_line[1].y_0}
        self.x_points = {self.point_line[0].x_0, self.point_line[1].x_0}

    def __eq__(self, obj):
        """
        Redefining == method.
        """
        if isinstance(obj, Line):
            if abs(self.point_line[0].x_0 - self.point_line[0].y_0) == \
                    abs(obj.point_line[0].x_0 - obj.point_line[0].y_0):
                return True
            else:
                return False
        else:
            return False

    def intersect(self, line):
        """
        Method which check intersection of two lines.
        """

        a = self.point_line[0].y_0 - self.point_line[1].y_0
        b = self.point_line[1].x_0 - self.point_line[0].x_0
        c = -((self.point_line[0].x_0 * self.point_line[1].y_0) -
              (self.point_line[1].x_0 * self.point_line[0].y_0))
        a_1 = line.point_line[0].y_0 - line.point_line[1].y_0
        b_1 = line.point_line[1].x_0 - line.point_line[0].x_0
        c_1 = -((line.point_line[0].x_0 * line.point_line[1].y_0) -
                (line.point_line[1].x_0 * line.point_line[0].y_0))

        d = (a * b_1) - (b * a_1)
        d_x = (c * b_1) - (b * c_1)
        d_y = (a * c_1) - (c * a_1)
        if d != 0:
            result_x = d_x / d
            result_y = d_y / d
            return Point(result_x, result_y)
        elif self.point_line[1].x_0 == self.point_line[0].x_0 == \
                line.point_line[0].x_0 == line.point_line[1].x_0 or\
                self.point_line[1].y_0 == self.point_line[0].y_0 == \
                line.point_line[0].y_0 == line.point_line[1].y_0:
            return self
        elif abs(self.point_line[0].x_0 - self.point_line[0].y_0) == \
                abs(line.point_line[1].x_0 - line.point_line[1].y_0):
            return self
        else:
            return None


# def __eq__(self, obj):
#     """
#     Redefining == method.
#     """
#     if isinstance(obj, Point):
#         if self.x == obj.x and self.y == obj.y:
#             return True
#         else:
#             return False

#     if isinstance(obj, Line):
#         if self.x_points == obj.x_points and self.y_points == obj.y_points:
#             return True
#         else:
#             return False
class Demo:
    def __init__(self):
        self.__b = 1

    def display(self):
        return self.__b


class Test:
    def __init__(self):
        self.x = 0


class Derived_Test(Test):
    def __init__(self):
        self.y = 1


def main():
    b = Derived_Test()
    print(b.x, b.y)


main()
