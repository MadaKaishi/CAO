from random import choice
from tkinter.tix import ROW
from .board import Board
from .constants import BOARD_SIZE as size, COLS, ROWS


class GameSupposedToBeFinished(Exception):
    pass


class Enemy:
    def __init__(self, name=""):
        self._name = name

    def name(self) -> str:
        return self._name


class EnemyRandom(Enemy):
    def __init__(self, name=""):
        super().__init__(name)

    def choose_index(self, board: "Board") -> tuple:
        empty_tiles = []
        iterable_board = board.board()
        for row in iterable_board:
            for piece in row:
                if piece.symbol() == "":
                    empty_tiles.append((piece.row(), piece.col()))
        if not empty_tiles:
            raise GameSupposedToBeFinished("Game should be over by now")
        return choice(empty_tiles)

    def choose_symbol(self, board=None) -> str:
        possible_symbols = ["X", "O"]
        return choice(possible_symbols)


class EnemyAIOrder(Enemy):
    def __init__(self, name="", board=None):
        super().__init__(name)
        self._board = board

    def board(self):
        return self._board

    def choose_index(self, board: "Board"):
        # scan middle 4 x 4 of board
        middle_rect = self._get_middle_rectangle(board)
        # search for possibilities of placing 4 in row
        index, action = self._analize_middle_square(middle_rect, "X", "O")
        # chooses the best location
        if action == "row":
            empty_tiles = []
            for col in range(1, COLS-1):
                if middle_rect[index+1, col] == "":
                    empty_tiles.append((index+1, col))
            return choice(empty_tiles)
        if action == "col":
            empty_tiles = []
            for row in range(1, ROWS-1):
                if middle_rect[row, index+1] == "":
                    empty_tiles.append((row, index+1))
            return choice(empty_tiles)
        if action == "diag":


    def choose_symbol(self):
        pass

    def _get_middle_rectangle(self, board: "Board"):
        list_board = board.board()
        middle_rect = []
        middle_rows = list_board[1:5]
        for row in middle_rows:
            temp_list = []
            for col in range(1, COLS-1):
                temp_list.append(row[col].symbol())
            middle_rect.append(temp_list)
        return middle_rect

    def _analize_middle_square(self, middle_square: list, symbol_1, symbol_2):
        row_best = self._analize_rows(middle_square, symbol_1, symbol_2)
        col_best = self._analize_cols(middle_square, symbol_1, symbol_2)
        diag_best = self._analize_diagonals(middle_square, symbol_1, symbol_2)
        best = max(row_best, col_best, diag_best)
        if best == row_best:
            action = "row"
        if best == col_best:
            action == "col"
        if best == diag_best:
            action = "diag"
        return best, action

    def _analize_rows(self, middle_square: list, symbol_1, symbol_2):
        row_tiers = {}
        for row in range(ROWS-2):
            tier = 0
            for piece in middle_square[row]:
                if piece == f"{symbol_1}":
                    tier += 1
                if piece == f"{symbol_2}":
                    tier = 0
                    break
            row_tiers[row] = (tier, symbol_1)
            tier = 0
            for piece in middle_square[row]:
                if piece == f"{symbol_2}":
                    tier += 1
                if piece == f"{symbol_1}":
                    tier = 0
                    break
            row_tiers[row] = (tier, symbol_2)
        # checks what row is the best (if tie then first one)
        for key in row_tiers:
            actual = 0
            row = 0
            if row_tiers[key][0] > actual:
                row = key
        return row

    def _analize_cols(self, middle_square: list, symbol_1, symbol_2):
        column_list = []
        for col in range(COLS-2):
            temp_list = []
            for row in range(ROWS-2):
                temp_list.append(middle_square[row][col])
            column_list.append(temp_list)
        col_best = self._analize_rows(column_list, symbol_1, symbol_2)
        return col_best

    def _analize_diagonals(self, middle_square: list, symbol_1, symbol_2):
        diagonal_tiers = {}
        diagonal_1 = []
        diagonal_2 = []
        for row in range(ROWS-2):
            for col in range(COLS-2):
                diagonal_1.append(middle_square[row][col])
                diagonal_2.append(middle_square[ROWS-row][col])
        diagonals = [diagonal_1, diagonal_2]
        for diagonal in diagonals:
            tier = 0
            for piece in diagonal:
                if piece == f"{symbol_1}":
                    tier += 1
                if piece == f"{symbol_2}":
                    tier = 0
                    break
            diagonal_tiers[row] = (tier, symbol_1)
            tier = 0
            for piece in diagonal:
                if piece == f"{symbol_2}":
                    tier += 1
                if piece == f"{symbol_1}":
                    tier = 0
                    break
            diagonal_tiers[row] = (tier, symbol_2)
        for key in diagonal_tiers:
            actual = 0
            row = 0
            if diagonal_tiers[key][0] > actual:
                row = key
        return row


class EnemyAIChaos(Enemy):
    def __init__(self, name="", board=None):
        super().__init__(name)
        self._moves_dict = self.par_movement()
        self._board = board

    def board(self):
        return self._board

    def get_last_move(self, board: "Board") -> tuple:
        last_placed = board.last_move()
        row = last_placed.row()
        col = last_placed.col()
        sym = last_placed.symbol()
        return row, col, sym

    def choose_index(self, board: "Board") -> tuple:
        row, col, _ = self.get_last_move(board)
        rowcol = str(row)+str(col)
        wanted_rowcol = self._moves_dict[rowcol]
        wanted_row = int(wanted_rowcol[0])
        wanted_col = int(wanted_rowcol[1])
        return(wanted_row, wanted_col)

    def choose_symbol(self) -> str:
        row, col, sym = self.get_last_move(self._board)
        corner = [(0, 0), (5, 0), (0, 5), (5, 5)]
        if (row, col) not in corner:
            if sym == "X":
                return "O"
            if sym == "O":
                return "X"
        else:
            return sym

    def par_movement(self) -> dict:
        moves_dictionary = {
            "00": "55",
            "01": "45",
            "02": "03",
            "03": "02",
            "04": "40",
            "05": "50",
            "10": "54",
            "11": "31",
            "12": "14",
            "13": "33",
            "14": "12",
            "15": "51",
            "20": "30",
            "21": "23",
            "22": "42",
            "23": "21",
            "24": "44",
            "25": "35",
            "30": "20",
            "31": "11",
            "32": "34",
            "33": "13",
            "34": "32",
            "35": "25",
            "40": "04",
            "41": "43",
            "42": "22",
            "43": "41",
            "44": "24",
            "45": "01",
            "50": "05",
            "51": "15",
            "52": "53",
            "53": "52",
            "54": "10",
            "55": "00"
        }
        return moves_dictionary
