import turtle


# set up the screen size and world coordinates.  The screen size is
# the width/height plus twice the margin, and the origin is set to
# (margin,margin) from the bottom left.
def set_up_screen(s, width, height, margin):
    margin2 = margin * 2
    s.setup(width + margin2, height + margin2)
    s.screensize(width + margin2, height + margin2)
    s.setworldcoordinates(-margin, -margin, width + margin, height + margin)


def draw_board(t, x_ll, y_ll, square_size, x_squares, y_squares):
    ss1 = square_size + 1
    for i in range(x_squares+1):
        t.up()
        t.goto(x_ll + i * ss1, y_ll)
        t.down()
        t.goto(x_ll + i * ss1, y_ll + y_squares * ss1)
    for i in range(y_squares+1):
        t.up()
        t.goto(x_ll, y_ll + i * ss1)
        t.down()
        t.goto(x_ll + x_squares * ss1, y_ll + i * ss1)

square_size = 110

t = turtle.Turtle()
win = turtle.Screen()

#set_up_screen(win, (square_size+1) * 4, (square_size+1) * 4, 10)

for i in range(1,16):
    win.register_shape(f"tile_{i}.gif")
print(win.getshapes())

t.speed('fastest')
t.hideturtle()

#draw_board(t, 0, 0, square_size, 4, 4)
t.up()
t.goto(  0,   0)
t.down()
t.goto(101,   0)
t.goto(101, 101)
t.goto(  0, 101)
t.goto(  0,   0)

t.up()
t.shape("tile_1.gif")
t.goto(51,50)
t.stamp()

'''
t.up()
t.shape("tile_2.gif")
t.goto(165,55)
t.stamp()
'''

win.exitonclick()
