import math


class Point:

    # A couple class variables.
    origin_x = 0
    origin_y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # get_x() and get_y() are not really necessary, since
    # (in Python) all code has direct access to instance
    # variables.  We could also use the @property decorator
    # here, but that's beyond the scope of this course.

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def dist_to(self, other_pt):
        dx = other_pt.x - self.x
        dy = other_pt.y - self.y
        return math.sqrt(dx * dx + dy * dy)

    def distance_from_origin(self):
        x = self.x
        y = self.y
        return math.sqrt(x * x + y * y)
    
    def __str__(self):
        return f"({self.x},{self.y})"


def mid_point(pt1, pt2):
    dx = pt1.x - pt2.x
    dy = pt1.y - pt2.y
    return Point(pt2.x + dx / 2, pt2.y + dy / 2)


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius
