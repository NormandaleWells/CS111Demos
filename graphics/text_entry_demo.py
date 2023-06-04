#
# This demonstrates the use of an Entry
# object to get text from the user in
# a graphical way.
#
# It also shows how to use the Button
# class.  Note that if you use the Button
# class you also need to have utilities.py
# in the same directory.

from graphics import *
import button

def main():
    win = GraphWin("text entry demo", 400, 400)

    done_button = button.Button(Point(50, 350), "Done")
    done_button.draw(win)

    enter_button = button.Button(Point(50, 300), "Enter")
    enter_button.draw(win)

    label = Text(Point(150, 100), "# players")
    label.draw(win)

    text_entry = Entry(Point(250, 100), 10)
    text_entry.draw(win)
 
    text = Text(Point(200,150), "")
    done = False
    while not done:
        pt = win.getMouse()
        if done_button.click(pt):
            done = True
        elif enter_button.click(pt):
            text.undraw()
            s = text_entry.getText()
            text = Text(Point(200, 150), f'setting up a {s} player game')
            text.draw(win)

    done_button.undraw()
    enter_button.undraw()

if __name__ == "__main__":
    main()
