from .constants import BOARD_SIZE as size, SQUARE_SIZE, FPS
from .board import Board, OverwriteError
from .piece import Piece
from .enemy import EnemyRandom, EnemyAI
import pygame

class SymbolError(Exception):
    pass


class Game():
    def __init__(self, side=None, gamemode=None, win=None) -> "Game":
        self._board = Board()
        self._side = side
        self._gamemode = gamemode
        self._win = win
        if self._gamemode == "1":
            self._enemy = EnemyRandom("Enemy")
        if self._gamemode == "2":
            self._enemy = EnemyAI("Enemy")
        self._turn = "Order"
        self._stop = False

    def restart(self, side, gamemode):
        self._board = Board()
        self._side = side
        self._gamemode = gamemode
        self._stop = False
        self._turn = "Order"

    def board(self):
        return self._board

    def side(self):
        return self._side

    def gamemode(self):
        return self._gamemode

    def load_board(self, board):
        self._board = board

    def order_win(self):
        if self._order_win_one_symbol("X"):
            return True
        if self._order_win_one_symbol("O"):
            return True
        return False

    def _order_win_one_symbol(self, symbol):
        piece_board = self._board.board()
        board = []
        for row in piece_board:
            temp_list = []
            for piece in row:
                temp_list.append(piece.symbol())
            board.append(temp_list)
        if self._check_horizontal(board, symbol):
            return True
        if self._check_vertical(board, symbol):
            return True
        if self._check_diagonal(board, symbol):
            return True
        return False

    def _check_horizontal(self, board, symbol):
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        for row in board:
            if row[:size-1] == searched:
                if row != avoided:
                    return True
            if row[1:size] == searched:
                if row != avoided:
                    return True
        return False

    def _check_diagonal(self, b, symbol):
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        diagonal_l_1 = [b[0][0], b[1][1], b[2][2], b[3][3], b[4][4], b[5][5]]
        diagonal_l_2 = [b[0][5], b[1][4], b[2][3], b[3][2], b[4][1], b[5][0]]
        diagonal_s_3 = [b[1][0], b[2][1], b[3][2], b[4][3], b[5][4]]
        diagonal_s_4 = [b[4][0], b[3][1], b[2][2], b[1][3], b[0][4]]
        diagonal_s_5 = [b[5][1], b[4][2], b[3][3], b[2][4], b[5][1]]
        diagonal_s_6 = [b[0][1], b[1][2], b[2][3], b[3][4], b[4][5]]
        dia_long = [diagonal_l_1, diagonal_l_2]
        dia_short = [diagonal_s_3, diagonal_s_4, diagonal_s_5, diagonal_s_6]
        if searched in dia_short:
            return True
        for diagonal in dia_long:
            if diagonal[:size-1] == searched:
                if diagonal != avoided:
                    return True
            if diagonal[1:size] == searched:
                if diagonal != avoided:
                    return True

    def _check_vertical(self, board, symbol):
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        for i in range(size):
            tem_list = []
            for row in board:
                tem_list.append(row[i])
            if tem_list[:size-1] == searched:
                if tem_list != avoided:
                    return True
            if tem_list[1:size] == searched:
                if tem_list != avoided:
                    return True
        return False

    def chaos_win(self):
        for row in self._board.board():
            for piece in row:
                if piece.symbol() == "":
                    return False
        return True

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y//SQUARE_SIZE
        col = x//SQUARE_SIZE
        return int(row), int(col)

    def place_circle(self, board, row, col):
        if self.position_ocupied(board, row, col):
            raise OverwriteError()
        piece = Piece(row, col, "O")
        board.place(piece)

    def place_x(self, board, row, col):
        if self.position_ocupied(board, row, col):
            raise OverwriteError()
        piece = Piece(row, col, "X")
        board.place(piece)

    def position_ocupied(self, board, row, col):
        piece = board.board()[row][col]
        if piece.symbol() == "":
            return False
        return True

    def check_mouse_pos(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_mouse(pos)
        return row, col

    def player_turn(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self._stop = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    row, col = self.check_mouse_pos()
                    if not self.position_ocupied(self._board, row, col):
                        self.place_x(self._board, row, col)
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    row, col = self.check_mouse_pos()
                    if not self.position_ocupied(self._board, row, col):
                        self.place_circle(self._board, row, col)
                        run = False

    def enemy_turn(self):
        row, col = self._enemy.choose_index(self._board)
        symbol = self._enemy.choose_symbol()
        if symbol == "X":
            self.place_x(self._board, row, col)
        elif symbol == "O":
            self.place_circle(self._board, row, col)
        else:
            raise SymbolError("Symbol error occured")

    def order_move(self):
        if self._side == "1":
            self.player_turn()
        else:
            self.enemy_turn()

    def chaos_move(self):
        if self._side == "2":
            self.player_turn()
        else:
            self.enemy_turn()

    def play(self):
        self.board().draw(self._win)
        pygame.display.update()
        while (not self.order_win() or not self.chaos_win()) and not self._stop:
            pygame.time.Clock().tick(FPS)
            if self._turn == "Order":
                self.order_move()
                self.board().draw(self._win)
                pygame.display.update()
                self._turn = "Chaos"
            if self.order_win():
                break
            if self._turn == "Chaos":
                self.chaos_move()
                self.board().draw(self._win)
                pygame.display.update()
                self._turn = "Order"
        pass
