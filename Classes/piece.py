import pygame
from .window import Window
from typing import Union
from classes.constants import BLACK, SQUARE_SIZE


class Piece:
    """Class of Piece
    This class represent single piece of game
    """
    PADDING = 10
    X_PADDING = 10
    LINE_THICKNESS = 7

    def __init__(self, row: int, column: int, symbol: str):
        """
        Piece contains attributes:
        row, col, symbol, x, y
        x and y are used to cooperate with GUI windows
        row and col are resposible for placement of piece on board,
        symbol defines the symbol of piece either X or O
        """
        self._row = row
        self._column = column
        self._symbol = symbol
        self._x = 0
        self._y = 0
        self._calc_position()

    def row(self) -> int:
        """Returns row of Piece"""
        return self._row

    def col(self) -> int:
        """Returns column of Piece"""
        return self._column

    def symbol(self) -> str:
        """Retruns symbol of Piece"""
        return self._symbol

    def _calc_position(self):
        """Calculates x and y position based on row and column"""
        self._x = SQUARE_SIZE * self._column + SQUARE_SIZE//2
        self._y = SQUARE_SIZE * self._row + SQUARE_SIZE//2

    def draw_x(self, win: "Window"):
        """
        Draws X on board, that contains of two lines crossing at
        certain angle
        """
        x_left = self._x - (SQUARE_SIZE//2) + self.X_PADDING  # coordinates of left x axis
        x_right = self._x + (SQUARE_SIZE//2) - self.X_PADDING  # coordinates of right x axis
        y_up = self._y - (SQUARE_SIZE//2) + self.X_PADDING  # coordinates of up y axis
        y_down = self._y + (SQUARE_SIZE//2) - self.X_PADDING  # coordinates of down y axis
        pygame.draw.line(win, BLACK, (x_left, y_up), (x_right, y_down), self.LINE_THICKNESS)
        pygame.draw.line(win, BLACK, (x_left, y_down), (x_right, y_up), self.LINE_THICKNESS)

    def draw_circle(self, win: "Window"):
        """
        Draws circle on given window
        """
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self._x, self._y), radius, self.LINE_THICKNESS)

    def draw(self, win: "Window") -> Union[str, None]:
        """
        Draws X or O on window based on symbol of Piece
        """
        if self._symbol == "X":
            self.draw_x(win)
        if self._symbol == "O":
            self.draw_circle(win)
        else:
            return None

    def __repr__(self) -> str:
        """Representation of object is its symbol"""
        return str(self._symbol)
