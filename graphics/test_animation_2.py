'''
This sample program demonstrates two things:

(1) Using .setCoords() to set the window coordinates
(2) Using autoflush-False and update() to do animation
    at a specific framerate

The program creates 5 circles, and moves each one a
random amount with each timeframe.  To change the
timeframe, edit the update() call; the argument
provided to update() is the number of frames per
second at which you want the animation to run.
'''
import random
import time

from graphics import *

def main():
    win = GraphWin("Mapping Test", 800, 800, autoflush=True)
    win.setCoords(0.0, 0.0, 1.0, 1.0)

    pts = [
            Point(0.25, 0.25),
            Point(0.75, 0.25),
            Point(0.25, 0.75),
            Point(0.75, 0.75),
            Point(0.5, 0.5)]
    colors = ["red", "green", "blue", "yellow", "purple"]

    circles = []
    for i in range(len(pts)):
        circle = Circle(pts[i], 0.1)
        circle.setFill(colors[i])
        circles.append(circle)

    for circle in circles:
        circle.draw(win)

    for _ in range(1000):
        for circle in circles:
            dx = random.random() * 0.02 - 0.01
            dy = random.random() * 0.02 - 0.01
            circle.move(dx, dy)
        #time.sleep(0.03)
        #update(30)

    win.close()    # Close window when done

if __name__ == "__main__":
    main()
