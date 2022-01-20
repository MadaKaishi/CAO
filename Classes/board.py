import pygame
from .constants import BLACK, COLS, ROWS, SQUARE_SIZE, WHITE
from .piece import Piece
from .window import Window


class OverwriteError(Exception):
    pass


class Board:
    """Class of Board
    This class represents gaming board
    It containts informations about all pieces in game,
    in form of nested lists:
    [[row],[row]...]
    Functions of this class are also able to use GUI to communicate with user
    """
    PADDING = 4

    def __init__(self, board=None) -> "Board":
        """
        Initializes the board object, if board in form of list is given,
        the board is loaded with values contained in it, if not then
        board is created with each tile filled with piece filled with
        empty pieces
        """
        self._board = board
        if self._board is None:  # if no board was given
            self._board = []
            self._crate_board()
        self._last_move = None  # last move is set to none

    def set_last_move(self, piece: "Piece"):
        """
        Sets which piece was placed last
        """
        self._last_move = piece

    def last_move(self):
        """
        Returns information which piece was placed last
        """
        return self._last_move

    def draw_squares(self, win: "Window"):
        """
        Draws board of game
        """
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                x_cord = (row * SQUARE_SIZE) + (self.PADDING/2)
                y_cord = (col * SQUARE_SIZE) + (self.PADDING/2)
                side = SQUARE_SIZE - self.PADDING
                pygame.draw.rect(win, WHITE, (x_cord, y_cord, side, side))

    def _crate_board(self):
        """
        Creates board in form of nested lists filled with empty strings
        Appends self._board variable
        """
        for row in range(ROWS):
            temp_list = []
            for column in range(COLS):
                temp_list.append(Piece(row, column, ""))
            self._board.append(temp_list)

    def place(self, piece: "Piece"):
        """
        Places piece in position given by its row and column
        """
        self._board[piece.row()][piece.col()] = piece
        self.set_last_move(piece)

    def board(self) -> list:
        """
        Returns list representation of the board
        """
        return self._board

    def draw(self, win: "Window"):
        """
        Draws board, then draws pieces on it
        """
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                piece.draw(win)

    def get_symbol_from_tile(self, row: int, col: int) -> str:
        """
        Returns symbol from row and column given
        """
        return self._board[row][col].symbol()
