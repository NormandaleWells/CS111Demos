import random

import board

'''
The Game class represents the game itself.  To use this,
just create a Game object and call the run() method.
'''
class Game:

    '''
    The starting configuration of the game.  Tile 1 is in the upper
    left corner, and the blank is at the bottom right.
    THIS MUST NOT BE MODIFIED!  If you need to modify it (to
    randomize it, for instance), you must make a copy.
    '''
    start_position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    def __init__(self):

        # Create the game board with the standard initial
        # configuration.
        self.puzzle = board.Board(self.start_position[:])

        # Add the buttons we need.
        self.puzzle.add_button("Done")
        # self.puzzle.add_button("Save")
        # self.puzzle.add_button("Load")
        self.puzzle.add_button("Solve")
        self.puzzle.add_button("Reset")
        self.puzzle.add_button("Randomize")

    '''
    Respond to a Reset command by resetting the board to
    its standard initial configuation.
    '''
    def reset(self):
        positions = self.start_position[:]
        self.puzzle.set_board(positions)

    '''
    Repond to a Randomize command by randomizing the
    standard start position.
    NOTE: This current may produce an unwinnable
    configuration!
    '''
    def randomize(self):
        positions = self.start_position[:]
        random.shuffle(positions)
        self.puzzle.set_board(positions)

    '''
    Respond to a button click.
    '''
    def handle_button(self, button_name):
        if button_name == "Done":
            return True
        elif button_name == "Randomize":
            self.randomize()
        elif button_name == "Reset":
            self.reset()
        return False

    '''
    Respond to the click of a tile by moving this
    tile to the blank position.
    '''
    def handle_tile(self, tile_pos):
        tile = self.puzzle.get_tile_at(tile_pos)
        self.puzzle.move_to_blank(tile)

    '''
    Run the game!
    '''
    def run(self):
        while (True):
            obj = self.puzzle.wait_for_click()
            if type(obj) == type(""):
                if self.handle_button(obj):
                    break
            elif type(obj) == type((0,0)):
                self.handle_tile(obj)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
