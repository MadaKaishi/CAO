from random import choice


class GameSupposedToBeFinished(Exception):
    pass


class Enemy:
    def __init__(self, name="") -> "Enemy":
        self._name = name

    def name(self):
        return self._name


class EnemyRandom(Enemy):
    def __init__(self, name="") -> "Enemy":
        super().__init__(name)

    def choose_index(self, board):
        empty_tiles = []
        iterable_board = board.board()
        for row in iterable_board:
            for piece in row:
                if piece.symbol() == "":
                    empty_tiles.append((piece.row(), piece.col()))
        if not empty_tiles:
            raise GameSupposedToBeFinished("Game should be over by now")
        return choice(empty_tiles)

    def choose_symbol(self, board=None):
        possible_symbols = ["X", "O"]
        return choice(possible_symbols)


class EnemyAIOrder(Enemy):
    def __init__(self, name="", board=None) -> "Enemy":
        super().__init__(name)
        self._board = board

    def move(self):
        pass


class EnemyAIChaos(Enemy):
    def __init__(self, name="", board=None) -> "Enemy":
        super().__init__(name)
        self._moves_dict = self.par_movement()
        self._board = board

    def get_last_move(self, board):
        last_placed = board.last_move()
        row = last_placed.row()
        col = last_placed.col()
        sym = last_placed.symbol()
        return row, col, sym

    def choose_index(self, board):
        row, col, _ = self.get_last_move(board)
        rowcol = str(row)+str(col)
        wanted_rowcol = self._moves_dict[rowcol]
        wanted_row = int(wanted_rowcol[0])
        wanted_col = int(wanted_rowcol[1])
        return(wanted_row, wanted_col)

    def choose_symbol(self):
        row, col, sym = self.get_last_move(self._board)
        corner = [(0, 0), (5, 0), (0, 5), (5, 5)]
        if (row, col) not in corner:
            if sym == "X":
                return "O"
            if sym == "O":
                return "X"
        else:
            return sym

    def par_movement(self):
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
