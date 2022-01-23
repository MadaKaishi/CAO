from pygame.constants import K_ESCAPE
from .constants import BOARD_SIZE as size, COLS, FPS, ROWS, WIDTH, HEIGHT, PATH
from .board import Board, OverwriteError
from .piece import Piece
from .enemy import EnemyRandom, EnemyAIOrder, EnemyAIChaos
from .window import Window
from typing import Union
import pygame
import os


class SymbolError(Exception):
    """
    Error that occures when symbol is other than X or O
    """
    pass


class SaveCorruptedError(Exception):
    """
    Error that occures when save is not present or data that
    it containes is corrupted
    """
    pass


class Game():
    """
    Class game represents game of Chaos and Order
    Its the main calss of this program
    It is connected to other classes like:\n
    -Border\n
    -Piece\n
    -Enemy\n
    -Window\n
    Based on its methods and methods used in other classes it handles the game
    """
    def __init__(self):
        """
        Initiates the game with:
        empyt board,
        turn is set to be played as order,
        stop is set as false,
        winner is set as None,
        action_after_finishing game is set as none
        """
        self._board = Board()
        self._turn = "Order"
        self._stop = False
        self._winner = None
        self._after_action = None

    def _restart(self):
        """
        Restarts the game, makes an empty board, and
        set other variables as default
        """
        self._board = Board()  # board is empty
        self._stop = False
        self._turn = "Order"
        self._winner = None
        self._gamemode = None
        self._enemy = None
        self._side = None

    def end_action(self) -> Union[str, None]:
        """
        Returns value of self._after_action
        """
        return self._after_action

    def board(self) -> "Board":
        """
        Returns value of self._board
        """
        return self._board

    def side(self) -> Union[str, None]:
        """
        Returns value of self._side
        """
        return self._side

    def gamemode(self) -> Union[str, None]:
        """
        Returns value of self._gamemode
        """
        return self._gamemode

    def win(self) -> Union["Window", None]:
        """
        Returns value of self._win (window)
        """
        return self._win

    def load_board(self, board: "Board"):
        """
        Sets value of self._board to board
        """
        self._board = board

    def save_game(self):
        """
        Saves game file localted in path specified in constants file\n
        Each line in file represents one position
        """
        with open(f"{PATH}", "w") as f:
            f.write(f"{self._turn}\n")  # which turn is it
            f.write(f"{self._side}\n")  # what side is player playing
            f.write(f"{self._gamemode}\n")  # what difficulty player is playing
            for row in range(ROWS):
                for col in range(COLS):
                    # symbol of each piece, starting with upper row
                    f.write(f"{self._board.board()[row][col].symbol()}\n")

    def _load_game(self) -> tuple:
        """
        Loads game setups from file that location is described by path
        in constants
        """
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
        """Deletes save"""
        os.remove(f"{PATH}")

    def order_win(self) -> bool:
        """Check if order wins with any symbol"""
        if self._order_win_one_symbol("X"):
            self._winner = "Order"
            return True
        if self._order_win_one_symbol("O"):
            self._winner = "Order"
            return True
        return False

    def _order_win_one_symbol(self, symbol: str) -> bool:
        """
        Checks if order order met winning conditons
        with symbol given as argument
        """
        piece_board = self._board.board()
        board = []
        for row in piece_board:
            temp_list = []
            for piece in row:
                temp_list.append(piece.symbol())
            board.append(temp_list)
        if self._check_horizontal(board, symbol):  # check if win in rows
            return True
        if self._check_vertical(board, symbol):  # check if win in cols
            return True
        if self._check_diagonal(board, symbol):  # check if win in diagonals
            return True
        return False  # if conditions are not met, returns false

    def _check_horizontal(self, board: "Board", symbol: str) -> bool:
        """
        Checks if order wins along horizontal axis
        Return True if conditions are met
        """
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        for row in board:
            if row[:size-1] == searched:
                if row != avoided:  # if there are not 6 symbols in the row
                    return True
            if row[1:size] == searched:
                if row != avoided:  # if there are not 6 symbols in the row
                    return True
        return False

    def _check_diagonal(self, board: "Board", symbol: str) -> bool:
        """
        Check if order wins along diagonal axis.
        There are 6 diagonals, 2 long and 4 short
        Returns true if contitions are met
        """
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        diagonal_long_1 = []
        diagonal_long_2 = []
        diagonal_short_1 = []
        diagonal_short_2 = []
        diagonal_short_3 = []
        diagonal_short_4 = []
        for index in range(size):
            diagonal_long_1.append(board[index][index])
            diagonal_long_2.append(board[index][size-1-index])
        for index in range(size-1):
            diagonal_short_1.append(board[index+1][index])
            diagonal_short_2.append(board[index][index+1])
            diagonal_short_3.append(board[size-1-(index+1)][index])
            diagonal_short_4.append(board[size-1-index][index+1])
        dia_long = [diagonal_long_1, diagonal_long_2]
        dia_short = [diagonal_short_1, diagonal_short_2,
                     diagonal_short_3, diagonal_short_4]
        if searched in dia_short:
            return True
        for diagonal in dia_long:
            if diagonal[:size-1] == searched:
                if diagonal != avoided:  # if there  are not 6 symbols
                    return True
            if diagonal[1:size] == searched:
                if diagonal != avoided:  # if there are not 6 symbols
                    return True

    def _check_vertical(self, board: "Board", symbol: str) -> bool:
        """
        Check if order wins along vertical axis
        Returns True if conditions are met
        """
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        for i in range(size):
            tem_list = []
            for row in board:
                tem_list.append(row[i])
            if tem_list[:size-1] == searched:
                if tem_list != avoided:  # if there are not 6 symbols
                    return True
            if tem_list[1:size] == searched:
                if tem_list != avoided:  # if there are not 6 symbols
                    return True
        return False

    def chaos_win(self) -> bool:
        """
        Check if chaos win
        Returns True if conditions are met
        """
        for row in self._board.board():
            for piece in row:  # if the board is not full
                if piece.symbol() == "":
                    return False  # returns false
        self._winner = "Chaos"  # else sets the winner as chaos
        return True

    def _choose_enemy_based_on_modes(self):
        """
        Based on self._gamemode and self._side chooses
        enemy to play against in game
        sets enemy to self._enemy
        """
        if self._gamemode == "Easy":
            self._enemy = EnemyRandom("EnemyRandom")
        if self._gamemode == "Hard":
            if self._side == "Order":
                self._enemy = EnemyAIChaos("EnemyAIChaos", self._board)
            if self._side == "Chaos":
                self._enemy = EnemyAIOrder("EnemyAIOrder", self._board)

    def _place_circle(self, board: "Board", row: int, col: int):
        """
        Places circle on board
        """
        if self.position_ocupied(board, row, col):
            raise OverwriteError()
        piece = Piece(row, col, "O")
        board.set_last_move(piece)
        board.place(piece)

    def _place_x(self, board: "Board", row: int, col: int):
        """
        Places x on board
        """
        if self.position_ocupied(board, row, col):
            raise OverwriteError()
        piece = Piece(row, col, "X")
        board.set_last_move(piece)
        board.place(piece)

    def position_ocupied(self, board: "Board", row: int, col: int) -> bool:
        """
        Returns True if position defined as row and col on
        given board is occupied
        """
        piece = board.board()[row][col]
        if piece.symbol() == "":
            return False
        return True

    def player_move(self):
        """
        Allows player to move that consist of:
        -choosing a tile on board
        -based on placement of mouse on the board player chooses tile
        -based on click the symbol is chosen:
            *  right click -> circle
            *  left click -> x
        """
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # when player left
                    self.save_game()
                    run = False
                    self._stop = True
                    self._after_action = "Exit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:  # when esc is pressed
                        self.save_game()
                        self._stop = True
                        self._after_action = "Exit"
                        run = False
                        pygame.quit()
                # when left button is pressed
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    row, col = self.win().check_mouse_pos()
                    if not self.position_ocupied(self._board, row, col):
                        self._place_x(self._board, row, col)
                        run = False
                # when right button is pressed
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    row, col = self.win().check_mouse_pos()
                    if not self.position_ocupied(self._board, row, col):
                        self._place_circle(self._board, row, col)
                        run = False

    def enemy_move(self):
        """
        Allows for enemy to place its piece on board:
        piece is selecteda by enemy methods
        This function only places element on board
        """
        row, col = self._enemy.choose_index(self._board)
        symbol = self._enemy.choose_symbol()
        if symbol == "X":
            self._place_x(self._board, row, col)
        elif symbol == "O":
            self._place_circle(self._board, row, col)
        else:
            raise SymbolError("Symbol error occured")

    def order_move(self):
        """
        Allows enemy or player assosiated with order to move
        """
        if self._side == "Order":
            self.player_move()
        else:
            self.enemy_move()

    def chaos_move(self):
        """
        Allows player assosiated with chaos to move
        """
        if self._side == "Chaos":
            self.player_move()
        else:
            self.enemy_move()

    def play(self):
        """
        Main method of this class:
        allows for game to be played,
        handles the board manipulation both by player and opponent,
        order and chaos plays in turns, if game is interrupted by
        leaving it, board and data needed to recreate it is saved to file
        """
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
        if self._winner is not None:  # when game ended
            if os.path.isfile(f"{PATH}"):
                self.delete_save()  # file is deleted
            if self._winner != self._side:
                self._win.game_window_lose()
            else:
                self._win.game_window_win()
            self._after_action = self._win.end_action()
            if self._after_action == "Retry":
                self._restart()
            else:
                pygame.quit()

    def prepare_game(self):
        """
        Prepares data needed to start the game:
        if save file is avaliable game can be loaded from file,
        if save is not avaliable or players selects new game
        this method gathers data about:
        side of player, difficulty of enemy using GUIs
        """
        self._win = Window(WIDTH, HEIGHT, "Chaos and Order")
        self._win.title_screen()
        if self._win.action() == "New":
            self._win.side_choose_window()
            self._win.difficulty_choose_window()
            self._side = self._win.side()
            self._gamemode = self._win.gamemode()
        elif self._win.action() == "Load":
            try:
                turn, side, game, board = self._load_game()
                self._side = side
                self._gamemode = game
                self._turn = turn
                self._board = board
            except (FileNotFoundError, SaveCorruptedError):
                self._win.side_choose_window()
                self._win.difficulty_choose_window()
                self._side = self._win.side()
                self._gamemode = self._win.gamemode()
        self._choose_enemy_based_on_modes()

    def prepare_retry(self):
        """
        This method gathers data to replay the game
        """
        self._win.side_choose_window()
        self._win.difficulty_choose_window()
        self._side = self._win.side()
        self._gamemode = self._win.gamemode()
        self._choose_enemy_based_on_modes()
