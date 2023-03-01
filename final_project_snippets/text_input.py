'''
This program demonstrates two features of the graphics.py module.

(1) How to get text input via an Entry object
(2) How special keys are returned from checkKey()
'''
from graphics import *


def main():
    win = GraphWin("Text Input Sample", 400, 200)

    '''
    Create the prompt for the edit box.  Find the correct
    position requires some experimentation.
    '''
    speed_prompt = Text(Point(150, 100), "Speed")
    speed_prompt.draw(win)

    '''
    Create the edit box with room for 10 characters.
    '''
    speed_entry = Entry(Point(300,100), 10)
    speed_entry.draw(win)

    '''
    Create the text object to show the current value.
    '''
    cur_speed_text = Text(Point(200, 150), "Current speed:")
    cur_speed_text.draw(win)

    while True:

        ''' Wait for a key.  If it's a q, quit. '''
        c = win.checkKey()
        if c == 'q':
            break

        ''' Print the result from checkKey.  Try hitting enter and escape. '''
        if c != "":
            print(c)

        ''' One a mouse click, get the text value and display it. '''
        pt = win.checkMouse()
        if pt != None:
            new_speed = speed_entry.getText()
            cur_speed_text.setText(f"Current speed: {new_speed}")

    win.close()

if __name__ == "__main__":
    main()
