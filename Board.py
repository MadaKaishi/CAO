class Board:
    def __init__(self, size) -> None:
        self._size = size
        self._board = ""

    def generate_board(self):
        a1 = " "
        tail = ""
        tail += f" --- \n| {a1} | \n---"

    def print_board(self):
        print(self._board)
