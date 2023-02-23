import time
import utilities
import math

from graphics import *

class Button:

    button_width = 100
    button_height = 30

    def __init__(self, lower_left, text):
        x = lower_left.getX()
        y = lower_left.getY()
        self.button_rect = Rectangle(
            lower_left,
            Point(x + self.button_width, y + self.button_height))
        self.button_text = Text(Point(x + self.button_width // 2, y + self.button_height // 2), text)

    def draw(self, win):
        self.button_rect.draw(win)
        self.button_text.draw(win)

    def text(self):
        return self.button_text.getText()

    def click(self, pt):
        return utilities.pt_in_rect(pt, self.button_rect)


class Board:

    margin = 10
    square_size = 102
    num_rows = 4
    num_columns = 4
    num_tiles = num_rows * num_columns
    border_size = 1
    board_width = square_size * num_columns + border_size * (num_columns + 1)
    board_height = square_size * num_rows + border_size * (num_rows + 1)
    button_left = board_width + margin
    window_width = margin + board_width + margin + Button.button_width + margin
    window_height = margin + board_height + margin
    image_offset_x = 52
    image_offset_y = 51

    def move_tile(self, tile, position):
        col,row = position
        x = self.image_offset_x + col * (self.square_size + 1)
        y = self.image_offset_y + ((self.num_rows - 1) - row) * (self.square_size + 1)
        cur_pos = self.number_images[tile].getAnchor()
        cur_x = cur_pos.getX()
        cur_y = cur_pos.getY()
        # todo: animate this
        self.number_images[tile].move(x - cur_x, y - cur_y)

    def set_board(self, tiles):
        for image in self.number_images:
            if image != None:
                image.undraw()
        self.position_images = {}
        self.image_positions = [0] * self.num_tiles
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                pos = (col, row)
                tile_idx = row * self.num_columns + col
                tile = tiles[tile_idx]
                self.position_images[pos] = tile
                self.image_positions[tile] = pos
                if tile != 0:
                    self.move_tile(tile, pos)
        for image in self.number_images:
            if image != None:
                image.draw(self.win)

    def __init__(self):
        self.win = GraphWin("16 Puzzle", self.window_width, self.window_height)
        self.win.setCoords(
            -self.margin, -self.margin,
            self.window_width-self.margin, self.window_height - self.margin)

        self.board_rect = Rectangle(Point(0, 0), Point(self.board_width, self.board_height))
        self.board_rect.setFill("white")
        self.board_rect.draw(self.win)

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

        button_offset = Button.button_height + self.margin
        self.done_button  = Button(Point(self.button_left, button_offset * 0), "Done")
        self.save_button  = Button(Point(self.button_left, button_offset * 1), "Save")
        self.solve_button = Button(Point(self.button_left, button_offset * 2), "Solve")
        self.rand_button  = Button(Point(self.button_left, button_offset * 3), "Randomize")
        self.reset_button = Button(Point(self.button_left, button_offset * 4), "Reset")
        self.done_button.draw(self.win)
        self.save_button.draw(self.win)
        self.solve_button.draw(self.win)
        self.rand_button.draw(self.win)
        self.reset_button.draw(self.win)

        self.number_images = [None]
        for i in range(1, self.num_tiles):
            image = Image(Point(0, 0), f"tile_{i}.gif")
            self.number_images.append(image)
        
        self.set_board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])

    def move_to_blank(self, tile):
        blank_pos = self.image_positions[0]
        tile_pos = self.image_positions[tile]
        if abs(blank_pos[0] - tile_pos[0]) + abs(blank_pos[1] - tile_pos[1]) != 1:
            print("invalid move")
        else:
            self.move_tile(tile, blank_pos)
            self.image_positions[tile] = blank_pos
            self.image_positions[0] = tile_pos
            self.position_images[blank_pos] = tile
            self.position_images[tile_pos] = None

    def get_tile_at(self, pos):
        return self.position_images[pos]

    def wait_for_click(self):
        pt = self.win.getMouse()
        if self.done_button.click(pt):
            return self.done_button.text()
        if self.save_button.click(pt):
            return self.save_button.text()
        if self.solve_button.click(pt):
            return self.solve_button.text()
        if self.rand_button.click(pt):
            return self.rand_button.text()
        if self.reset_button.click(pt):
            return self.reset_button.text()
        if utilities.pt_in_rect(pt, self.board_rect):
            col = round(pt.getX()) // self.square_size
            row = round(pt.getY()) // self.square_size
            row = (self.num_rows - 1) - row
            if col in range(self.num_columns) and row in range(self.num_rows):
                return (col,row)

def test():
    board = Board()
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
