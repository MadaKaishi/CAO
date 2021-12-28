import pygame

from gui_constants import BLACK, SQUARE_SIZE


class GuiPiece:
    PADDING = 10
    X_PADDING = 10
    LINE_THICKNESS = 7

    def __init__(self, row, column, symbol) -> "GuiPiece":
        self._row = row
        self._column = column
        self._symbol = symbol
        self._x = 0
        self._y = 0
        self.calc_position()

    def row(self):
        return self._row

    def col(self):
        return self._column

    def symbol(self):
        return self._symbol

    def calc_position(self):
        self._x = SQUARE_SIZE * self._column + SQUARE_SIZE//2
        self._y = SQUARE_SIZE * self._row + SQUARE_SIZE//2

    def draw_x(self, win):
        x_left = self._x - (SQUARE_SIZE//2) + self.X_PADDING
        x_right = self._x + (SQUARE_SIZE//2) - self.X_PADDING
        y_up = self._y - (SQUARE_SIZE//2) + self.X_PADDING
        y_down = self._y + (SQUARE_SIZE//2) - self.X_PADDING
        pygame.draw.line(win, BLACK, (x_left, y_up), (x_right, y_down), self.LINE_THICKNESS)
        pygame.draw.line(win, BLACK, (x_left, y_down), (x_right, y_up), self.LINE_THICKNESS)

    def draw_circle(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self._x, self._y), radius, self.LINE_THICKNESS)

    def draw(self, win):
        if self._symbol == "X":
            self.draw_x(win)
        if self._symbol == "O":
            self.draw_circle(win)
        else:
            return None

    def __repr__(self) -> str:
        return str(self._symbol)
