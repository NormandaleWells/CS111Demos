#
# This program shows one way of handling the graphics for
# a board game.  The idea presented here is to remap the
# screen to allow for an NxN array of squares to be drawn
# using a coordinate system in which the bottom-left
# square is (0,0) to (1,1), the next square to the right
# is (1,0) to (2,1), etc.
#
#  (0,2)    (1.2)
#   +---------+---------+ (2,2)
#   |         |         |
#   | box 0,1 | box 1,1 |
#   |         |         |
#   +--------_+---------+ (2,1)
#   |         |         |
#   | box 0,0 | box 1,0 |
#   |         |         |
#   +---------+---------+
#  (0,0)             (2,0)
#
# This way, the center of each square is at (x.5,y.5) where
# x and y are the integer coordinates of the box.  Also,
# mouse clicks will be returned as (x.d,y,d), so we just
# need to truncate the number to an int to get the box
# coordinates.

from graphics import *

import button

class Board:

    # Set up initially for a 2x2 grid of square boxes, with
    # a 15-pixel border.  After setCoords() is called to
    # set up the coordinate system, everything needs to be
    # scaled by 1/box_size.
    board_width = 4         # number of squares across
    board_height = 4        # number of squares high
    box_size = 100          # square size in pixels
    margin = 15             # margin in pixels
    button_width = 80       # button width in pixels
    button_height = 30      # button height in pixels

    def __init__(self):
        x_size = self.board_width * self.box_size + self.button_width + self.margin * 3
        y_size = self.board_height * self.box_size + self.margin * 2
        
        self.win = GraphWin("Generic Game Board", x_size, y_size)

        # After remapping, 1.0 is box_size pixels.  The local variables
        # 'margin', 'button_width', and 'button'height' are all adjusted
        # for the window scale.
        margin = self.margin / self.box_size
        button_width = self.button_width / self.box_size
        button_height = self.button_height / self.box_size
        self.win.setCoords(-margin, -margin, self.board_width + margin + button_width + margin, self.board_height + margin)

        # All buttons created here must be scaled by the box_size.
        # Note that set_button_size() is not an instance method; that
        # is, it does not refer to any specific instance.  Rather, it
        # is a class method, meaning it applies to the class itself.
        button.Button.set_button_size(button_width, button_height)

        # Draw the vertical box separators.
        for i in range(self.board_width+1):
            l = Line(Point(i,0), Point(i,self.board_height))
            l.draw(self.win)

        # Draw the horizontal box separators.
        for i in range(self.board_height+1):
            l = Line(Point(0,i), Point(self.board_width,i))
            l.draw(self.win)

        # Create the Done button.
        button_x = self.board_width + margin
        self.done_button = button.Button(Point(button_x, 0), "Done")
        self.done_button.draw(self.win)

    '''
    wait_for_click() waits for the user to click an area of the
    screen and returns either a tuple containing the coordinates
    of the box that was clicked, or the string "done" if the
    Done button was clicked.
    '''
    def wait_for_click(self):
        while True:
            pt = self.win.getMouse()
            if self.done_button.click(pt):
                return "done"
            
            # Because of the margin we set up, we could get a
            # negative coordinate.  Since Python rounds toward
            # 0.0 when converted an int to a float, we need to
            # check that here first.
            if pt.getX() >= 0 and pt.getY() >= 0:
                x = int(pt.getX())
                y = int(pt.getY())
                # The margin may also cause a mouse click to be
                # outside the game board, so we only get out if
                # we know we clicked a box.
                if x < self.board_width and y < self.board_height:
                    break
        return (x,y)

class Game:

    def __init__(self):
        self.board = Board()

    def run(self):
        while True:
            square = self.board.wait_for_click()
            if square == "done":
                break
            print(f"Box clicked was {square[0]},{square[1]}")
            if square[0] < 0 or square[1] < 0:
                break

if __name__ == "__main__":
    g = Game()
    g.run()
