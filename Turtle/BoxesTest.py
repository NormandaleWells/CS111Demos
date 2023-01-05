import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.fillcolor("hotpink")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
for _ in range(4):
    t.right(90)
    t.forward(100)
t.end_fill()
wn.exitonclick()
