
from graphics import *

class Button:

    def __init__(self, lower_left, text):
        x = lower_left.getX()
        y = lower_left.getY()
        self.button_rect = Rectangle(
            lower_left,
            Point(x + Board.button_width, y + Board.button_height))
        self.button_text = Text(Point(x + Board.button_width // 2, y + Board.button_height // 2), text)

    def draw(self, win):
        self.button_rect.draw(win)
        self.button_text.draw(win)

    def text(self):
        return self.button_text.getText()

    def click(self, pt):
        ll = self.button_rect.getP1()
        ur = self.button_rect.getP2()
        return ll.getX() <= pt.getX() < ur.getX() and ll.getY() <= pt.getY() < ur.getY()


class Board:

    margin = 10
    square_size = 100
    num_rows = 4
    num_columns = 4
    border_size = 1
    board_width = square_size * num_columns + border_size * (num_columns + 1)
    board_height = square_size * num_rows + border_size * (num_rows + 1)
    button_left = board_width + margin
    button_width = 100
    button_height = 30
    window_width = margin + board_width + margin + button_width + margin
    window_height = margin + board_height + margin

    def __init__(self):
        self.win = GraphWin("16 Puzzle", self.window_width, self.window_height)
        self.win.setCoords(
            -self.margin, -self.margin,
            self.window_width-self.margin, self.window_height - self.margin)

        self.board_rect = Rectangle(Point(0, 0), Point(self.board_width, self.board_height))
        self.lines = []
        for i in range(1, self.num_columns):
            x = i * (self.square_size + 1)
            line = Line(Point(x, 0), Point(x, self.board_height))
            self.lines.append(line)
        for i in range(1, self.num_rows):
            y = i * (self.square_size + 1)
            line = Line(Point(0, y), Point(self.board_width, y))
            self.lines.append(line)

        button_offset = self.button_height + self.margin
        self.done_button  = Button(Point(self.button_left, button_offset * 0), "Done")
        self.save_button  = Button(Point(self.button_left, button_offset * 1), "Save")
        self.solve_button = Button(Point(self.button_left, button_offset * 2), "Solve")
        self.rand_button  = Button(Point(self.button_left, button_offset * 3), "Randomize")

    def draw(self):
        self.board_rect.draw(self.win)
        for line in self.lines:
            line.draw(self.win)
        self.done_button.draw(self.win)
        self.save_button.draw(self.win)
        self.solve_button.draw(self.win)
        self.rand_button.draw(self.win)

    def wait_for_click(self):
        pt = self.win.getMouse()
        if self.done_button.click(pt):
            return self.done_button.text()


def test():
    board = Board()
    board.draw()
    while (True):
        obj = board.wait_for_click()
        if type(obj) == type("") and obj == "Done":
            break


if __name__ == "__main__":
    test()
