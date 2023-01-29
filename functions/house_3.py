'''
Adapted from the video in the Functions secitons of Runestone's FOPP.
    draw_square calls draw_rectangle
    set turtle to "classic"
    hide turtle at end
    set up screen size and world coordinates
        set_up_screen() function
'''

import turtle

skippy = turtle.Turtle()
win = turtle.Screen()
skippy.shape("classic")

house_llx = 0
house_lly = 0
house_size = 200
eve_size = 10
window_size = house_size / 8
door_width = house_size / 8
door_height = house_size / 3


# set up the screen size and world coordinates.  The screen size is
# the width/height plus twice the margin, and the origin is set to
# (margin,margin) from the bottom left.
def set_up_screen(s, width, height, margin):
    s.setup(width + 2 * margin, height + 2 * margin)
    s.screensize(width + margin * 2, height + margin * 2)
    s.setworldcoordinates(-margin, -margin, width + margin, height + margin)


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


# draw a square with the given size, and with its lower-left
# corner at (x,y).
def draw_square(t, size, x, y):
    draw_rectangle(t, size, size, x, y)


# set up the screen to allow a margin twice the size of the eves
set_up_screen(win, house_size * 2, house_size * 2, eve_size * 2)

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

skippy.hideturtle()

win.exitonclick()
