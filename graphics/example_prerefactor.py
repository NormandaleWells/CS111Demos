from graphics import *

win = GraphWin("My fancy window", 400, 400)

flower_center = Point(200, 200)
stem = Rectangle(flower_center, Point(210, 300))

stem.setFill("green")
stem.draw(win)

petal1 = Circle(flower_center, 20)
petal1.move(-10, -10)
petal1.setFill("purple")
petal1.draw(win)

petal2 = Circle(flower_center, 20)
petal2.move(10, -10)
petal2.setFill("purple")
petal2.draw(win)

petal3 = Circle(flower_center, 20)
petal3.move(10, 10)
petal3.setFill("purple")
petal3.draw(win)

petal4 = Circle(flower_center, 20)
petal4.move(-10, 10)
petal4.setFill("purple")
petal4.draw(win)

center = Circle(flower_center, 10)
center.setFill("yellow")
center.draw(win)



input("Press Enter when done")