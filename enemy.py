from board import Board

class Enemy:
    def __init__(self, name) -> "Enemy":
        self._name = name

    def name(self):
        return self._name

    def place_tile(self, board, coordinates, symbol):
        board.write_tile(coordinates, symbol)


class EnemyRandom(Enemy):
    def __init__(self, name) -> "Enemy":
        super().__init__(name)

    def


class EnemyAI(Enemy):
    pass
