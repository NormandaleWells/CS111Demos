import turtle


board_ll_x = -200
board_ll_y = -200
square_size = 100
tile_offset_x = 51      # determined experimentally
tile_offset_y = 50      # determined experimentally


# set up the screen size and world coordinates.  The screen size is
# the width/height plus twice the margin, and the origin is set to
# (margin,margin) from the bottom left.
# NOTE: It appears that the width and height provided to .setup()
# include the window borders.  We're better off not trying to set
# the window size.
def set_up_screen(s, width, height, margin):
    margin2 = margin * 2
#    s.setup(width + margin2, height + margin2)
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


# Return the pixel position to place the tile at the
# the given row and column.  Both are in [0..3], with
# rows starting at the top.
def calc_tile_position(col, row):
    row = 3 - row
    return (
        board_ll_y + col * (square_size+1) + tile_offset_x,
        board_ll_x + row * (square_size+1) + tile_offset_y
        )


def draw_tile(t, col, row, num):
    t.up()
    t.shape(f"tile_{num}.gif")
    tile_pos = calc_tile_position(row, col)
    t.goto(tile_pos[0], tile_pos[1])
    t.stamp()

t = turtle.Turtle()
win = turtle.Screen()

#set_up_screen(win, (square_size+1) * 4, (square_size+1) * 4, 10)

for i in range(1,16):
    win.register_shape(f"tile_{i}.gif")
print(win.getshapes())

t.speed('fastest')
t.hideturtle()

draw_board(t, board_ll_x, board_ll_y, square_size, 4, 4)

draw_tile(t, 0, 0, 1)
draw_tile(t, 0, 1, 2)
draw_tile(t, 0, 2, 3)
draw_tile(t, 0, 3, 4)
draw_tile(t, 1, 0, 5)
draw_tile(t, 1, 1, 6)
draw_tile(t, 1, 2, 7)
draw_tile(t, 1, 3, 8)

'''
t.up()
t.shape("tile_2.gif")
t.goto(165,55)
t.stamp()
'''

win.exitonclick()
