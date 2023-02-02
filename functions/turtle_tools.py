import turtle


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
