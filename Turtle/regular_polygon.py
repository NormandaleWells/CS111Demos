import turtle

num_sides = int(input("Number of sides: "))
side_size = int(input("Size of each side: "))

angle = 180 - (num_sides - 2) * 180 / num_sides
print(num_sides, angle)

color_str = "red green blue yellow magenta cyan black"
colors = color_str.split()

# create the turtle
wn = turtle.Screen()
t = turtle.Turtle()

# move down a little, and move a little to the left
# so that we're centered better.
t.up()
t.right(90)
t.forward(200)
t.left(90)
t.forward(-side_size / 2)
t.down()

# draw the polygon
color_idx = 0
for i in range(num_sides):

    # use the next color, and increment the color index
    t.color(colors[color_idx])
    color_idx += 1
    if color_idx == len(colors):
        color_idx = 0

    # draw this side, and turn
    t.forward(side_size)
    t.left(angle)

wn.exitonclick()
