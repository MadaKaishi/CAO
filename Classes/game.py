from .constants import BOARD_SIZE as size, COLS, FPS, ROWS, WIDTH, HEIGHT, PATH
from .board import Board, OverwriteError
from .piece import Piece
from .enemy import EnemyRandom, EnemyAI
from .window import Window
import pygame
import os


class SymbolError(Exception):
    pass


class SaveCorruptedError(Exception):
    pass


class Game():
    def __init__(self) -> "Game":
        self._board = Board()
        self._turn = "Order"
        self._stop = False
        self._winner = None
        self._after_action = None

    def restart(self):
        self._board = Board()
        self._stop = False
        self._turn = "Order"
        self._winner = None
        self._gamemode = None
        self._enemy = None
        self._side = None
        self._win = None


    def end_action(self):
        return self._after_action

    def board(self):
        return self._board

    def side(self):
        return self._side

    def gamemode(self):
        return self._gamemode

    def win(self):
        return self._win

    def load_board(self, board):
        self._board = board

    def save_game(self):
        with open(f"{PATH}", "w") as f:
            f.write(f"{self._turn}\n")
            f.write(f"{self._side}\n")
            f.write(f"{self._gamemode}\n")
            for row in range(ROWS):
                for col in range(COLS):
                    f.write(f"{self._board.board()[row][col].symbol()}\n")

    def load_game(self):
        with open(f"{PATH}", "r") as f:
            turn = f.readline().rstrip()
            if turn not in ["Chaos", "Order"]:
                raise SaveCorruptedError()
            side = f.readline().rstrip()
            if side not in ["Chaos", "Order"]:
                raise SaveCorruptedError()
            gamemode = f.readline().rstrip()
            if gamemode not in ["Easy", "Hard"]:
                raise SaveCorruptedError()
            board = []
            for row in range(ROWS):
                temp_list = []
                for col in range(COLS):
                    temp_list.append(Piece(row, col, f.readline().rstrip()))
                board.append(temp_list)
            return turn, side, gamemode, Board(board)

    def delete_save(self):
        os.remove(f"{PATH}")

    def order_win(self):
        if self._order_win_one_symbol("X"):
            self._winner = "Order"
            return True
        if self._order_win_one_symbol("O"):
            self._winner = "Order"
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
        self._winner = "Chaos"
        return True

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

    def player_move(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_game()
                    run = False
                    self._stop = True
                    self._after_action = "Exit"
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    row, col = self.win().check_mouse_pos()
                    if not self.position_ocupied(self._board, row, col):
                        self.place_x(self._board, row, col)
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    row, col = self.win().check_mouse_pos()
                    if not self.position_ocupied(self._board, row, col):
                        self.place_circle(self._board, row, col)
                        run = False

    def enemy_move(self):
        row, col = self._enemy.choose_index(self._board)
        symbol = self._enemy.choose_symbol()
        if symbol == "X":
            self.place_x(self._board, row, col)
        elif symbol == "O":
            self.place_circle(self._board, row, col)
        else:
            raise SymbolError("Symbol error occured")

    def order_move(self):
        if self._side == "Order":
            self.player_move()
        else:
            self.enemy_move()

    def chaos_move(self):
        if self._side == "Chaos":
            self.player_move()
        else:
            self.enemy_move()

    def play(self):
        self.board().draw(self._win.win())
        self._win.update()
        self._after_action = "Exit"
        while (not self.order_win() and not self.chaos_win()) and not self._stop:
            pygame.time.Clock().tick(FPS)
            if self._turn == "Order":
                self.order_move()
                self.board().draw(self._win.win())
                self._win.update()
                self._turn = "Chaos"
            if self.order_win():
                break
            if self._turn == "Chaos" and not self._stop:
                self.chaos_move()
                self.board().draw(self._win.win())
                self._win.update()
                self._turn = "Order"
            if self.chaos_win():
                break
        if self._winner is not None:
            if self._winner != self._side:
                self._win.game_window_loose()
            else:
                self._win.game_window_win()
            self._after_action = self._win.end_action()
            if self._after_action == "Retry":
                self.restart()
            else:
                pygame.quit()


    def prepare_game(self):
        self._win = Window(WIDTH, HEIGHT, "Chaos and Order")
        self._win.title_screen()
        if self._win.action() == "New":
            self._win.side_choose_window()
            self._win.difficulty_choose_window()
            self._side = self._win.side()
            self._gamemode = self._win.gamemode()
        elif self._win.action() == "Load":
            try:
                turn, side, game, board = self.load_game()
                self._side = side
                self._gamemode = game
                self._turn = turn
                self._board = board
            except (FileNotFoundError, SaveCorruptedError):
                self._win.side_choose_window()
                self._win.difficulty_choose_window()
                self._side = self._win.side()
                self._gamemode = self._win.gamemode()
        if self._gamemode == "Easy":
            self._enemy = EnemyRandom("Enemy")
        if self._gamemode == "Hard":
            self._enemy = EnemyAI("Enemy")
