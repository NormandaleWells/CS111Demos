from graphics import *

import utilities

'''
The Button class represents a user interface
pushbutton that can be clicked to cause some
action within the program.

To use this class, create a Button object
with a given lower-left corner, and for each
mouse click, call the click() method to see
if that click was within the button.
'''

class Button:

    button_width = 100
    button_height = 30

    '''
    Set the size for all future buttons.  This is useful when the
    window is mapped to non-pixel coordiantes.  This is not an
    instance method, it is a class method, so it's called like
    this:
        button.Button.set_button_size(w,h)
    '''
    def set_button_size(width, height):
        Button.button_width = width
        Button.button_height = height

    '''
    Create a button at the given position (lower left),
    with the given text.
    '''
    def __init__(self, lower_left, text):
        x = lower_left.getX()
        y = lower_left.getY()
        self.button_rect = Rectangle(
            lower_left,
            Point(x + self.button_width, y + self.button_height))
        self.button_text = Text(Point(x + self.button_width / 2, y + self.button_height / 2), text)

    '''
    Draw the button on the given GraphWin object.
    '''
    def draw(self, win):
        self.button_rect.draw(win)
        self.button_text.draw(win)

    '''
    Return the text for this button.
    '''
    def text(self):
        return self.button_text.getText()

    '''
    Return True if the given point is in the button,
    False otherwise.
    '''
    def click(self, pt):
        return utilities.pt_in_rect(pt, self.button_rect)


