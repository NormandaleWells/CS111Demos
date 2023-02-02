'''
Adapted from the video in the Functions secitons of Runestone's FOPP
Changes from house_1.py:
    implemented draw_triangle()
    implemented draw_rectangle()
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

# draw an equilateral triangle with the given size, and with
# its lower-left corner at (x,y).
def draw_triangle(t, size, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(3):
        t.forward(size)
        t.left(120)

# draw a rectangle with the given size, and with its lower-left
# corner at (x,y).
def draw_rectangle(t, width, height, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(4):
        if i % 2 == 0:
            t.forward(width)
        else:
            t.forward(height)
        t.left(90)

# Draw the square for the whole house.
draw_square(skippy, house_size, 0, 0)

# Draw a triangle for the roof.
draw_triangle(skippy, house_size + 2 * eve_size, house_llx-eve_size, house_size)

# Draw window
draw_square(skippy, window_size, house_size / 5, house_size / 3)

# Draw window
draw_square(skippy, window_size, house_size - house_size / 5 - window_size, house_size / 3)

# Draw door
draw_rectangle(skippy, door_width, door_height, house_size / 2 - door_width / 2, 0)

win.exitonclick()
