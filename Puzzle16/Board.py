'''
This module contains the Board class, which maintains the board state
and move/redraws tiles when necessary.

TODO: Separate this into two classes: Board and GameWindow.
'''

import time
import utilities
import math

from graphics import *

import button

'''
The Board class represents the board along with any buttons defined
by the game.  It is responsible for keeping track of the state of
the board (which tile is in which position), moving tiles as needed,
and drawing the board.

It is expected that only one Board object would exist.
'''
class Board:

    '''
    These constants define all the parameters need for
    drawing the board.  They are:

        margin          - the size of the margin separating the
                          board from the window edges, and
                          separating the buttons from the board
                          and each other
        square_size     - The size of each square on the board.
                          There's a slight kludge here.  The
                          square size is set two pixels larger
                          than needed, since there appears to
                          be some round-off error when mapping
                          an image center to the center of a
                          box.
        num_rows        - the number of rows of tiles.
        num_columns     - the number of columns of tiles.
        num_tiles       - the toal number of tiles
        border_size     - width of the border between tiles
        fence_post      - used to document fencepost situations
        board_width     - the total width of the board
        board_height    - the total board height for num_rows
        board_width     - the total board width for num_columns
        button_left     - the left edge of the buttons
        window_width    - the minimum window width need to hold
                          all the tiles
        window_height   - the minimum window height need to hold
                          all the tiles
        image_offset_x  - the x delta from the lower left corner
                          of a tile's rectangle to the center of
                          the tile image
        image_offset_y  - the y delta from the lower left corner
                          of a tile's rectangle to the center of
                          the tile image
    '''
    margin = 10
    square_size = 102
    num_rows = 4
    num_columns = 4
    num_tiles = num_rows * num_columns
    border_size = 1
    fence_post = 1
    board_width = square_size * num_columns + border_size * (num_columns + fence_post)
    board_height = square_size * num_rows + border_size * (num_rows + fence_post)
    button_left = board_width + margin
    window_width = margin + board_width + margin + button.Button.button_width + margin
    window_height = margin + board_height + margin
    image_offset_x = 52
    image_offset_y = 51

    '''
    move_tile - move the given tile to the given (col,row) position

    This method does not check to verify that the target position is
    currently empty; it just moves the image.
    '''
    def move_tile(self, tile, position):

        # Unpack the position tuple and calculate the x and y coordinates
        # of the lower left corner of that position.  Note that rows are
        # number from top to bottom.
        col,row = position
        x = self.image_offset_x + col * (self.square_size + self.border_size)
        y = self.image_offset_y + ((self.num_rows - 1) - row) * (self.square_size + self.border_size)

        # Get the current position of the tile we're moving.
        cur_pos = self.number_images[tile].getAnchor()
        cur_x = cur_pos.getX()
        cur_y = cur_pos.getY()

        # Move the image its current position to the new one.  Note that
        # the move() method requires a delta, not an absolute position.
        # todo: animate this
        self.number_images[tile].move(x - cur_x, y - cur_y)

    '''
    set_board - set up the board state

    The 'tiles' argument is a list of 16 tile IDs.  tiles[0] is the tile
    to place at the upper left, the rest go across and then down.  This
    also updates the state of the board given by the position_images and
    image_positions instance variables.
    '''
    def set_board(self, tiles):

        # Undraw all the tile images
        for image in self.number_images:
            if image != None:
                image.undraw()

        # Empty the dictionary mapping positions to images, and
        # re-create the list of tile positions.  In the list
        # of tile positions, [0] is the location of the blank
        # tile, and the others are indexed by the tile number.
        self.position_images = {}
        self.image_positions = [0] * self.num_tiles

        # For each row and column...
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                # Create a tuple for this position and figure
                # out the index in the tile list for this
                # position.
                pos = (col, row)
                tile_idx = row * self.num_columns + col

                # Get the tile ID for this position, and
                # update position_images and image_positions.
                tile = tiles[tile_idx]
                self.position_images[pos] = tile
                self.image_positions[tile] = pos

                # If this is not the blank tile, move it.
                if tile != 0:
                    self.move_tile(tile, pos)
        
        # Redraw all the tile images.
        for image in self.number_images:
            if image != None:
                image.draw(self.win)

    '''
    Initialize a new board.
    '''
    def __init__(self, initial_state):

        # Create the window, and reset its coordinate system
        # so that (0,0) is the lower-left corner of the rectangle
        # containing the tiles.
        self.win = GraphWin("16 Puzzle", self.window_width, self.window_height)
        self.win.setCoords(
            -self.margin, -self.margin,
            self.window_width-self.margin, self.window_height - self.margin)

        # Create the rectangle around the board, and set its
        # background to white to match the tile image background.
        self.board_rect = Rectangle(Point(0, 0), Point(self.board_width, self.board_height))
        self.board_rect.setFill("white")
        self.board_rect.draw(self.win)

        # Create the vertical and horizontal lines separating the tiles.
        self.lines = []
        for i in range(1, self.num_columns):
            x = i * (self.square_size + 1)
            line = Line(Point(x, 0), Point(x, self.board_height))
            self.lines.append(line)
        for i in range(1, self.num_rows):
            y = i * (self.square_size + 1)
            line = Line(Point(0, y), Point(self.board_width, y))
            self.lines.append(line)
        for line in self.lines:
            line.draw(self.win)

        # Read in the tile images.
        self.number_images = [None]
        for i in range(1, self.num_tiles):
            image = Image(Point(0, 0), f"tile_{i}.gif")
            self.number_images.append(image)

        # Set up the initial board position.        
        self.set_board(initial_state)

        # We don't predefine any buttons.
        self.buttons = []

    '''
    Add a button to the window.  The buttons are stacked to
    the right of the tile rectangle.  The first button added
    is on the bottom, and the rest stack on top.
    '''
    def add_button(self, text):
        button_offset = button.Button.button_height + self.margin
        b = button.Button(Point(self.button_left, button_offset * len(self.buttons)), text)
        b.draw(self.win)
        self.buttons.append(b)

    '''
    Move the given tile to the blank position, and update
    the board state.  If the given tile is not adjacent
    to the blank, an error message is displayed and nothing
    is changed.
    '''
    def move_to_blank(self, tile):

        # Get the position of this tile and the blank tile.
        blank_pos = self.image_positions[0]
        tile_pos = self.image_positions[tile]

        # Make sure they are exactly one space apart.
        if abs(blank_pos[0] - tile_pos[0]) + abs(blank_pos[1] - tile_pos[1]) != 1:
            print("invalid move")
        else:
            # Move the tile image, and update the game state
            # by swapping the positions of the given tile
            # and the blank.
            self.move_tile(tile, blank_pos)
            self.image_positions[tile] = blank_pos
            self.image_positions[0] = tile_pos
            self.position_images[blank_pos] = tile
            self.position_images[tile_pos] = None

    '''
    Return the ID of the tile at the given position.
    '''
    def get_tile_at(self, pos):
        return self.position_images[pos]

    '''
    Wait for a mouse click, and return either
        (1) the name of the button that was clicked, or
        (2) the position of the tile that was clicked
            as a (col,row) tuple, or
        (3) None if nothing important was clicked.
    '''
    def wait_for_click(self):

        # Wait for a click.
        pt = self.win.getMouse()

        # Check to see if this click was over a button.
        for button in self.buttons:
            if button.click(pt):
                return button.text()
        
        # If this click was over the board, determine which
        # tile position it was over.  Note that due to
        # round-off error, we could get a value outside
        # the legal range, so we need to check for that.
        if utilities.pt_in_rect(pt, self.board_rect):
            col = round(pt.getX()) // self.square_size
            row = round(pt.getY()) // self.square_size
            row = (self.num_rows - 1) - row
            if col in range(self.num_columns) and row in range(self.num_rows):
                return (col,row)

def test():

    # Test the board class by creating a board and
    # a Done button, and moving tiles until Done is
    # clicked.
    board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    board.add_button("Done")
    while (True):
        obj = board.wait_for_click()
        if type(obj) == type(""):
            print(f"{obj} button clicked")
            if obj == "Done":
                break
        elif type(obj) == type((0,0)):
            tile = board.get_tile_at(obj)
            board.move_to_blank(tile)

if __name__ == "__main__":
    test()
