from graphics import *
import time

class Flower:

    def create_stem(self):
        stem = Rectangle(self.center, Point(self.center.x + 10, self.center.y + 100))
        stem.setFill("green")
        return stem

    def create_petal(self, dx, dy):
        petal = Circle(self.center, 20)
        petal.move(dx, dy)
        petal.setFill(self.color)
        return petal

    def create_center(self):
        center = Circle(self.center, 10)
        center.setFill("yellow")
        return center

    def __init__(self, center, color):

        self.center = Point(center.x, center.y)
        self.color = color
        self.age = 0
    
        self.stem   = self.create_stem()
        self.petal1 = self.create_petal(-10, -10)
        self.petal2 = self.create_petal( 10, -10)
        self.petal3 = self.create_petal( 10,  10)
        self.petal4 = self.create_petal(-10,  10)
        self.center = self.create_center()

    def draw(self, win):

        self.stem.draw(win)
        self.petal1.draw(win)
        self.petal2.draw(win)
        self.petal3.draw(win)
        self.petal4.draw(win)
        self.center.draw(win)

    def day_passes(self):
        self.age += 1
        if self.age == 5:
            self.stem.undraw()
            self.petal1.undraw()
            self.petal2.undraw()
            self.petal3.undraw()
            self.petal4.undraw()
            self.center.undraw()


def main():

    flowers = []

    win = GraphWin("My fancy window", 400, 400)
    while win.checkKey() != "q":

        point = win.checkMouse()
        if point != None:
            new_flower = Flower(point, "purple")
            new_flower.draw(win)
            flowers.append(new_flower)
        time.sleep(1.0)
        for f in flowers:
            f.day_passes()


if __name__ == "__main__":
    main()
