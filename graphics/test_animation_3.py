'''
This sample program demonstrates the use of the
autoFlush parameter in the GraphWin constructor.
The autoFlush parameter is controlled by the
auto_flush variable in main().

The program creates 500 circles and enters a loop
that runs 1000 times.  With each loop iteration
each circle is moved a random amount.

With auto_flush == True, the entire screen is
redrawn EVERY TIME ANY CIRCLE IS MOVED!  So each
loop iteration involves 500 moves, each of which
redraws 500 circles.  This can take a considerable
amount of time.

With auto_flush = False, the circles are moved
without being redrawn, and a called to update()
at the end of the loop performs the actual drawing.
Therefore each circle is drawn only once per loop,
a substantial saving of time.

The update() function has a parameter which specifies
the desired framerate.  Each time update() is called,
it will wait until 1/framerate seconds has elapsed
since the last call to update().

On my laptop (11th gen Intel i7 running at 2.8 GHz)
with auto_flush=True the program takes 2:50 to run,
for an effective frame rate of less than 6 frames
per second.  With auto_flush=False, it takes 33
seconds (30 frames/sec) to run, which indicates that
redrawing the 500 circles once each takes less than
1/30 of a second.
'''
import random

from graphics import *

def main():
    auto_flush = False

    win = GraphWin("Mapping Test", 800, 800, autoflush=auto_flush)
    win.setCoords(0.0, 0.0, 1.0, 1.0)

    colors = ["red", "green", "blue", "yellow", "purple"]

    num_circles = 500

    circles = []
    for i in range(num_circles):
        x = random.random() * 0.8 + 0.1
        y = random.random() * 0.8 + 0.1
        circle = Circle(Point(x,y), 0.025)
        circle.setFill(colors[i % len(colors)])
        circles.append(circle)

    for circle in circles:
        circle.draw(win)

    for _ in range(1000):
        for circle in circles:
            dx = random.random() * 0.02 - 0.01
            dy = random.random() * 0.02 - 0.01
            circle.move(dx, dy)
        if not auto_flush:
            update(30)

    win.close()    # Close window when done

if __name__ == "__main__":
    main()
