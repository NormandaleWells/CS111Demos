import time

from graphics import *

win = GraphWin("Animation Test", 200, 200)

line = Line(Point(100, 0), Point(100, 200))
line.draw(win)

circle = Circle(Point(25, 100), 25)
circle.setFill("red")
circle.draw(win)

for i in range(25):
    circle.move(5, 0)
    time.sleep(1)

win.getMouse()
