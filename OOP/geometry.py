import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def mid_point(self, other_pt):
        dx = other_pt.x - self.x
        dy = other_pt.y - self.y
        return Point(self.x + dx / 2, self.y + dy / 2)


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius
