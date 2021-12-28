import pygame
from gui_constants import BLACK, COLS, GREY, ROWS, SQUARE_SIZE, WHITE
from gui_piece import GuiPiece

class GuiBoard:
    def __init__(self) -> "GuiBoard":
        self.board = []
        self.crate_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, WHITE, ((row * SQUARE_SIZE)+2, (col * SQUARE_SIZE)+2, SQUARE_SIZE-4, SQUARE_SIZE-4))

    def crate_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 3:
                    self.board[row].append(GuiPiece(row, col, "O"))
                else:
                    self.board[row].append(GuiPiece(row, col, "X"))

    def place(self, row, column):
        pass

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                piece.draw(win)