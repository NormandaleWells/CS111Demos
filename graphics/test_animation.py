import time

from graphics import *

def main():
    win = GraphWin("Animation Test", 200, 200)

    circle1 = Circle(Point(75, 30), 25)
    circle1.setFill("blue")
    circle1.draw(win)

    circle2 = Circle(Point(40, 40), 25)
    circle2.setFill("yellow")
    circle2.draw(win)

    circle1.undraw()
    circle1.draw(win)

    for _ in range(8):
        circle2.move(10, 0)
        time.sleep(0.25)

    line = Line(Point(100, 0), Point(100, 200))
    line.draw(win)

    circle = Circle(Point(25, 100), 25)
    circle.setFill("red")
    circle.draw(win)

    for i in range(25):
        circle.move(5, 0)
        time.sleep(0.25)

    win.getMouse()

if __name__ == "__main__":
    main()
