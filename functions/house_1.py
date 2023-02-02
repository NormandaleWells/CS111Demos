'''
Adapted from the video in the Functions secitons of Runestone's FOPP
Changes from house_0.py:
    moved all constants to same block of code
    implemented draw_square()
    used draw_square() to draw the house and windows
'''

import turtle

skippy = turtle.Turtle()
win = turtle.Screen()

skippy.shape("turtle")

house_llx = 0
house_lly = 0
house_size = 200
eve_size = 10
window_size = house_size / 8
door_width = house_size / 8
door_height = house_size / 3

# draw a square with the given size, and with its lower-left
# corner at (x,y).
def draw_square(t, size, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(4):
        t.forward(size)
        t.left(90)

# Draw the square for the whole house.
draw_square(skippy, house_size, 0, 0)

skippy.up()
skippy.goto(house_llx-eve_size, house_size)
skippy.down()

# Draw roof
for _ in range(3):
    skippy.forward(house_size + 2 * eve_size)
    skippy.left(120)

# Draw window
draw_square(skippy, window_size, house_size / 5, house_size / 3)

# Draw window
draw_square(skippy, window_size, house_size - house_size / 5 - window_size, house_size / 3)

skippy.up()
skippy.goto(house_size / 2 - door_width / 2, 0)
skippy.down()

# Draw door
for i in range(4):
    if i % 2 == 0:
        skippy.forward(door_width)
    else:
        skippy.forward(door_height)
    skippy.left(90)

win.exitonclick()
