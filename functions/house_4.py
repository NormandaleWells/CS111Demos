'''
Adapted from the video in the Functions secitons of Runestone's FOPP
Changes from house_3.py:
	moved drawing functions to turtle_tools.py
    minimized window width
    doubled house size
'''

import turtle
import turtle_tools as tt

skippy = turtle.Turtle()
win = turtle.Screen()
skippy.shape("classic")

house_llx = 0
house_lly = 0
house_size = 400
eve_size = 10
window_size = house_size / 8
door_width = house_size / 8
door_height = house_size / 3


# set up the screen to allow a margin twice the size of the eves
tt.set_up_screen(win, house_size, house_size * 2, eve_size * 2)

# Draw the square for the whole house.
tt.draw_square(skippy, house_size, 0, 0)

# Draw a triangle for the roof.
tt.draw_triangle(skippy, house_size + 2 * eve_size, house_llx-eve_size, house_size)

# Draw window
tt.draw_square(skippy, window_size, house_size / 5, house_size / 3)

# Draw window
tt.draw_square(skippy, window_size, house_size - house_size / 5 - window_size, house_size / 3)

# Draw door
tt.draw_rectangle(skippy, door_width, door_height, house_size / 2 - door_width / 2, 0)

skippy.hideturtle()

win.exitonclick()
