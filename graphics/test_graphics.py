from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)

    c = Circle(Point(50,50), 10)
    c.draw(win)

    image = Image(Point(500,500), "BackinTime.png")
    image.draw(win)

    win.getMouse() # Pause to view result

    win.close()    # Close window when done

if __name__ == "__main__":
    main()
