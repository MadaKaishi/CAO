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

    def choose_symbol(self):
        possible_symbols = ["X", "O"]
        return choice(possible_symbols)


class EnemyAI(Enemy):
    def __init__(self, name="") -> "Enemy":
        super().__init__(name)

    def move(self):
        pass
