import pygame
from classes.constants import BLACK, COLS, ROWS, SQUARE_SIZE, WHITE
from .gui_piece import Piece


class Board:
    def __init__(self) -> "Board":
        self._board = []
        self.crate_board()

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

    def place(self, row, column, piece):
        self._board[row][column] = piece

    def board(self):
        return self._board

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                piece.draw(win)

    def get_symbol_from_tile(self, row, col):
        return self._board[row][col]
