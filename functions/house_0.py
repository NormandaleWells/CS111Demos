# adapted from the video in the Functions secitons of Runestone's FOPP
# This version is mostly identical to the version from the video.

import turtle

skippy = turtle.Turtle()
win = turtle.Screen()

skippy.shape("turtle")

house_llx = 0
house_lly = 0
house_size = 200
eve_size = 10

# Draw the square for the whole house.
for _ in range(4):
    skippy.forward(house_size)
    skippy.left(90)

skippy.up()
skippy.goto(house_llx-eve_size, house_size)
skippy.down()

# Draw roof
for _ in range(3):
    skippy.forward(house_size + 2 * eve_size)
    skippy.left(120)

window_size = house_size / 8

skippy.up()
skippy.goto(house_size / 5, house_size / 3)
skippy.down()

# Draw window
for _ in range(4):
    skippy.forward(window_size)
    skippy.left(90)

skippy.up()
skippy.goto(house_size - house_size / 5 - window_size, house_size / 3)
skippy.down()

# Draw window
for _ in range(4):
    skippy.forward(window_size)
    skippy.left(90)

door_width = house_size / 8
door_height = house_size / 3

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
