
from graphics import *

import button

def main():
    win = GraphWin("Animation Test", 400, 400)

    done_button = button.Button(Point(50, 350), "Done")
    done_button.draw(win)

    enter_button = button.Button(Point(50, 300), "Enter")
    enter_button.draw(win)

    text_entry = Entry(Point(200, 100), 20)
    text_entry.draw(win)

    text = Text(Point(200, 150), "")
    text.draw(win)

    done = False
    while not done:
        pt = win.getMouse()
        if done_button.click(pt):
            done = True
        elif enter_button.click(pt):
            s = text_entry.getText()
            text.undraw()
            text = Text(Point(200, 150), s)
            text.draw(win)
            text_entry.setText("")


if __name__ == "__main__":
    main()
