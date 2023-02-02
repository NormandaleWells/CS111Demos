import turtle

t = turtle.Turtle()
win = turtle.Screen()

t.hideturtle()

for i in range(1,16):
    win.register_shape(f"tile_{i}.gif")
print(win.getshapes())

t.up()
t.goto(0,0)
t.down()
t.goto(202,0)
t.goto(202,101)
t.goto(0,101)
t.goto(0,0)
t.up()
t.goto(101,0)
t.down()
t.goto(101,101)

t.up()
t.shape("tile_1.gif")
t.goto(51,50)
t.stamp()

t.up()
t.shape("tile_2.gif")
t.goto(152,50)
t.stamp()

win.exitonclick()
