from random import choice

from classes.constants import COLS, ROWS


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
        for row in range(ROWS):
            for col in range(COLS):
                if board.board()[col][row].symbol() == "":
                    empty_tiles.append((row, col))
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
