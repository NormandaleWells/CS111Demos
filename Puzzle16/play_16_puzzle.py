import random

import board

class Game:

    start_position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    def __init__(self):
        self.puzzle = board.Board()
        # TODO: create the buttons here

    def reset(self):
        positions = self.start_position[:]
        self.puzzle.set_board(positions)

    def randomize(self):
        positions = self.start_position[:]
        random.shuffle(positions)
        self.puzzle.set_board(positions)

    def handle_button(self, button_name):
        if button_name == "Done":
            return True
        elif button_name == "Randomize":
            self.randomize()
        elif button_name == "Reset":
            self.reset()
        return False

    def handle_tile(self, tile_pos):
        tile = self.puzzle.get_tile_at(tile_pos)
        self.puzzle.move_to_blank(tile)

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
