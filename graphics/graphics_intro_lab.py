# This is my implementation of Anya Vostinar's
# Graphincs Intro Lab
# see (https://anyaevostinar.github.io/classes/111-f22/graphics-intro)

from graphics import *
import time

win = GraphWin("My fancy window", 400, 400)

my_point = Point(100,100)
my_point.draw(win)

my_circle = Circle(Point(50, 50), 25)
my_circle.draw(win)
my_circle.setFill("red")

my_rectangle = Rectangle(Point(100,100), Point(200,200))
my_rectangle.setOutline("blue")
my_rectangle.draw(win)

for _ in range(10):
    my_rectangle.move(10, 10)
    time.sleep(0.1)


input("When done, press Enter")
