import pygame
from .constants import BLACK, COLS, ROWS, SQUARE_SIZE, WHITE
from .piece import Piece


class OverwriteError(Exception):
    pass


class Board:
    def __init__(self, board=None) -> "Board":
        self._board = board
        if self._board is None:
            self._board = []
            self.crate_board()
        self._last_move = None

    def set_last_move(self, piece):
        self._last_move = piece

    def last_move(self):
        return self._last_move

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, WHITE, ((row * SQUARE_SIZE)+2, (col * SQUARE_SIZE)+2, SQUARE_SIZE-4, SQUARE_SIZE-4))

    def crate_board(self):
        for row in range(ROWS):
            temp_list = []
            for column in range(COLS):
                temp_list.append(Piece(row, column, ""))
            self._board.append(temp_list)

    def place(self, piece):
        self._board[piece.row()][piece.col()] = piece

    def board(self):
        return self._board

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                piece.draw(win)

    def get_symbol_from_tile(self, row, col):
        return self._board[row][col].symbol()
