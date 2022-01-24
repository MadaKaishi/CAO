from random import choice
from .board import Board
from .constants import BOARD_SIZE as size, COLS, ROWS


class GameSupposedToBeFinished(Exception):
    pass


class Enemy:
    """Class Enemy:\n
    Basic class that is further developed in more advanced enemy variants.
    Only argument is its name
    """
    def __init__(self, name=""):
        """
        Initializes enemy object
        """
        self._name = name

    def name(self) -> str:
        """
        Returns name of enemy
        """
        return self._name


class EnemyRandom(Enemy):
    """
    Class EnemyRandom:
    it is derrived from Enemy class,
    its enemy that makes random moves, placing
    random symbols on empty fields on board
    """
    def __init__(self, name=""):
        """Initializes RandomEnemy object"""
        super().__init__(name)

    def choose_index(self, board: "Board") -> tuple:
        """
        Specifies which tiles are empty and the choosess one of them.
        Returns tuple of row and column of tile chosen
        If bot have to choose form full board, GameSupposedToBeFinished error
        is raised
        """
        empty_tiles = []
        iterable_board = board.board()
        for row in iterable_board:
            for piece in row:
                if piece.symbol() == "":
                    empty_tiles.append((piece.row(), piece.col()))
        if not empty_tiles:  # if bot will play if there are no empty tiles
            raise GameSupposedToBeFinished("Game should be over by now")
        return choice(empty_tiles)

    def choose_symbol(self, board=None) -> str:
        """
        Chooses random symbol (between X and O)
        """
        possible_symbols = ["X", "O"]
        return choice(possible_symbols)


class EnemyAIOrder(Enemy):
    """Class: EnemyAIOrder
    Class represents advanced enemy that plays on order side.
    Its movement are determined by analyzing middle 4 x 4 square.
    """
    def __init__(self, name: str = "", board: "Board" = None):
        """Initializes EnemyAIOrder object"""
        super().__init__(name)
        self._board = board
        self._tiers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0]]

    def board(self) -> str:
        """Returns self._board argument"""
        return self._board

    def choose_index(self, board: "Board") -> tuple:
        """
        Chooses index based on square analize
        """
        # scan middle 4 x 4 of board
        middle_rect = self._get_middle_rectangle(board)
        self._middle_rect = middle_rect
        self._middle_square_full = False
        # prepares the tuple of row and col
        index_tuple = self._prepare_index_from_middle_rect(board, middle_rect)
        return index_tuple

    def _prepare_index_from_middle_rect(self, board: list, middle_rect: list):
        """
        Prepares row and column based on tier list
        represented by board argument.
        """
        repeat = True
        while repeat:  # while repetition is needed
            repeat = False  # set repeat to False to avoid permanent loop
            collection, index, value = self._analize_middle_square(middle_rect, "X", "O")
            if value == -1:  # if there are not any good movements avaliable
                empty_tiles = []
                for row in range(ROWS):
                    for col in range(COLS):
                        if board.board()[row][col].symbol() == "":
                            empty_tiles.append((row, col))
                            self._middle_square_full = True
                return choice(empty_tiles)  # choose random tile
            if collection == 0:  # if best result is in rows
                if value == 4:  # if win is avaliable
                    if board.board()[index+1][0].symbol() == "":
                        chosen = (index+1, 0)
                    elif board.board()[index+1][COLS-1].symbol() == "":
                        chosen = (index+1, COLS-1)
                    else:
                        # if places that gives win are taken
                        self._tiers[collection][index] = -1  # sets tier of this row and column to -1
                        repeat = True  # repetition of choosing row and column is needed
                else:
                    empty_tiles = []
                    for col in range(COLS-2):
                        if middle_rect[index][col] == "":
                            empty_tiles.append((index+1, col+1))
                    chosen = choice(empty_tiles)
            if collection == 1:  # if best tier is contained in collumns
                if value == 4:
                    if board.board()[0][index+1].symbol() == "":
                        chosen = (0, index+1)
                    elif board.board()[ROWS-1][index+1].symbol() == "":
                        chosen = (ROWS-1, index+1)
                    else:
                        self._tiers[collection][index] = -1
                        repeat = True
                else:
                    empty_tiles = []
                    for row in range(ROWS-2):
                        if middle_rect[row][index] == "":
                            empty_tiles.append((row+1, index+1))
                    chosen = choice(empty_tiles)
            if collection == 2:  # if best tier is contained in diagonals
                empty_tiles = []
                if index == 0:  # if its first diagonal
                    if value == 4:
                        if board.board()[0][0].symbol() == "":
                            chosen = (0, 0)
                        elif board.board()[ROWS-1][COLS-1].symbol() == "":
                            chosen = (ROWS-1, COLS-1)
                        else:
                            self._tiers[collection][index] = -1
                            repeat = True
                    else:
                        for rowcol in range(size-2):
                            if middle_rect[rowcol][rowcol] == "":
                                empty_tiles.append((rowcol+1, rowcol+1))
                        chosen = choice(empty_tiles)
                if index == 1:  # if its second diagonal
                    if value == 4:
                        if board.board()[ROWS-1][0].symbol() == "":
                            return (ROWS-1, 0)
                        elif board.board()[0][COLS-1].symbol() == "":
                            chosen = (0, COLS-1)
                        else:
                            self._tiers[collection][index] = -1
                            repeat = True
                    else:
                        for rowcol in range(size-2):
                            if middle_rect[size-3-rowcol][rowcol] == "":
                                empty_tiles.append((size-3-rowcol+1, rowcol+1))
                        chosen = choice(empty_tiles)
        self._choose_symbol_atributes = collection, index
        return chosen

    def choose_symbol(self) -> str:
        """
        Chooses symbol based on position determined by choose_index
        """
        if self._middle_square_full:  # if there are no possibilities in middle 4 x 4 square
            return choice(["X", "O"])
        collection, index = self._choose_symbol_atributes
        if collection == 0:  # if best action is to place piece in rows
            if "X" in self._middle_rect[index]:
                return "X"
            else:
                return "O"
        if collection == 1:  # if best action is to place piece in columns
            symbols_form_column = []
            for row in range(size-2):
                symbols_form_column.append(self._middle_rect[row][index])
            if "X" in symbols_form_column:
                return "X"
            else:
                return "O"
        if collection == 2:  # if best action is to place piece on diagonals
            if index == 0:  # diagonal 1
                for rowcol in range(size-2):
                    if self._middle_rect[rowcol][rowcol] == "X":
                        return "X"
                return "O"
            if index == 1:  # diaognal 2
                for rowcol in range(size-2):
                    if self._middle_rect[size-3-rowcol][rowcol] == "X":
                        return "X"
                return "O"

    def _get_middle_rectangle(self, board: "Board") -> list:
        """Returns symbols from middle 4 x 4 rectangle in nested list form"""
        list_board = board.board()
        middle_rect = []
        middle_rows = list_board[1:(size-1)]
        for row in middle_rows:
            temp_list = []
            for col in range(1, COLS-1):
                temp_list.append(row[col].symbol())
            middle_rect.append(temp_list)
        return middle_rect

    def _analize_middle_square(self, middle_square: list, symbol_1: str, symbol_2: str) -> tuple:
        """
        Updates tiers of rows, columns and diagonals and chooses best option,
        based on not disturbed same symbol appearance
        """
        # upadtes tiers for rows
        self._analize_rows(middle_square, symbol_1, symbol_2)
        # upadtes tiers for collumns
        self._analize_cols(middle_square, symbol_1, symbol_2)
        # upadted tiers for diagonals
        self._analize_diagonals(middle_square, symbol_1, symbol_2)
        best = -1
        best_collection = 0
        best_index = 0
        for index_1, collection in enumerate(self._tiers):
            for index_2, tier in enumerate(collection):
                if tier >= best:
                    best_collection = index_1
                    best_index = index_2
                    best = tier
        return best_collection, best_index, best

    def _analize_rows(self, middle_square: list, symbol_1: str, symbol_2: str):
        """Analize rows and updates self._tiers[0]"""
        row_tier_list = self._get_tier_list_from_board(middle_square, symbol_1, symbol_2)
        row_list = self._tiers[0]
        new_row_list = []
        for index in range(len(row_list)):
            if row_list[index] != -1:  # if not disturbed by other symbol
                new_row_list.append(row_tier_list[index])
            else:
                new_row_list.append(-1)
        self._tiers[0] = new_row_list

    def _analize_cols(self, middle_square: list, symbol_1: str, symbol_2: str):
        """Analize collumns and updates self._tiers[1]"""
        column_list = []
        for col in range(COLS-2):
            temp_list = []
            for row in range(ROWS-2):
                temp_list.append(middle_square[row][col])
            column_list.append(temp_list)
        col_tier_list = self._get_tier_list_from_board(column_list, symbol_1, symbol_2)
        col_list = self._tiers[1]
        new_col_list = []
        for index in range(len(col_list)):
            if col_list[index] != -1:
                new_col_list.append(col_tier_list[index])
            else:
                new_col_list.append(-1)
        self._tiers[1] = new_col_list

    def _analize_diagonals(self, middle_square: list, symbol_1: str, symbol_2: str):
        """Analize diagonals and updates self._tiers[2]"""
        diagonal_1 = []
        diagonal_2 = []
        for index in range(size-2):
            diagonal_1.append(middle_square[index][index])
            diagonal_2.append(middle_square[ROWS-3-index][index])
        diagonals = [diagonal_1, diagonal_2]
        diagonal_tier_list = self._get_tier_list_from_board(diagonals, symbol_1, symbol_2)
        diag_list = self._tiers[2]
        new_diag_list = []
        for index in range(len(diag_list)):
            if diag_list[index] != -1:
                new_diag_list.append(diagonal_tier_list[index])
            else:
                new_diag_list.append(-1)
        self._tiers[2] = new_diag_list

    def _get_tier_list_from_board(self, symbol_list: list, symbol_1: str, symbol_2: str) -> list:
        """
        When its given list of collections it analizes each collection,
        tier of each collection is based on not disturbed appearance of one
        symbol, if second symbol appears in collecion its tier is placed
        as -1 and its not taken in consideration when indexes are chosen
        """
        tier_list = []
        for collection in symbol_list:
            tier_1 = 0
            tier_2 = 0
            for piece in collection:
                if piece == symbol_1:
                    tier_1 += 1
                if piece != symbol_1 and piece != "":
                    tier_1 = -1
                    break
            for piece in collection:
                if piece == symbol_2:
                    tier_2 += 1
                if piece != symbol_2 and piece != "":
                    tier_2 = -1
                    break
            tier_list.append(max(tier_1, tier_2))
        return tier_list


class EnemyAIChaos(Enemy):
    """Class: EnemyAIChaos:
    class that represents advanced enemy playing on chaos side,
    movements are determined by reaction to last placed piece by player
    """
    def __init__(self, name: str = "", board: "Board" = None):
        """
        Initializes EnemyAIChaos
        """
        super().__init__(name)
        self._moves_dict = self._par_movement()
        self._board = board

    def board(self) -> "Board":
        """Returns self._board"""
        return self._board

    def _get_last_move(self, board: "Board") -> tuple:
        """Returns row, col and symbol of last piece placed"""
        last_placed = board.last_move()
        row = last_placed.row()
        col = last_placed.col()
        sym = last_placed.symbol()
        return row, col, sym

    def choose_index(self, board: "Board") -> tuple:
        """Chooses row and column based on last piece placed"""
        row, col, _ = self._get_last_move(board)
        rowcol = str(row)+str(col)
        wanted_rowcol = self._moves_dict[rowcol]
        wanted_row = int(wanted_rowcol[0])
        wanted_col = int(wanted_rowcol[1])
        return(wanted_row, wanted_col)

    def choose_symbol(self) -> str:
        """Returns symbol based on last piece placed"""
        row, col, sym = self._get_last_move(self._board)
        corner = [(0, 0), (5, 0), (0, 5), (5, 5)]
        if (row, col) not in corner:
            if sym == "X":
                return "O"
            if sym == "O":
                return "X"
        else:
            return sym

    def _par_movement(self) -> dict:
        """Creates dictionary of best chaos responses"""
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
