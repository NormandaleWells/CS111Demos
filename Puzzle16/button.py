from graphics import *

import utilities

'''
The Button class represents one of the buttons on the right-hand
margin of the window.  No buttons are predefined by the board; it
is up to the Game class to tell the Board to create the buttons.
'''
class Button:

    button_width = 100
    button_height = 30

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
        self.button_text = Text(Point(x + self.button_width // 2, y + self.button_height // 2), text)

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

    '''
    Undraw the button.
    '''
    def draw(self):
        self.button_rect.undraw()
        self.button_text.undraw()
