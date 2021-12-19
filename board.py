from constants import BOARD_SIZE as size, TABLE_FILLMENT_HORIZONTAL as fill
from constants import TABLE_FILLMENT_VERTICAL as vert


class OutOfRangeError(Exception):
    pass


class Board:
    def __init__(self) -> None:
        self._board = ""
        self.generate_dictionary()

    def get_board(self):
        return self._board

    def generate_tile(self, tile_value):
        base = f"{vert} {tile_value} "
        return base

    def _check_if_in_range(self, tile_index: str):
        possible_values = self._board_values.keys()
        if tile_index not in possible_values:
            raise OutOfRangeError("Tile is out of range")

    def generate_board(self):
        board = ""
        for i in range(size):
            board += "  " + f"{fill}"*size + "+\n"
            board += str(size-i) + " "
            for value in list(self._board_values.values())[(i*size):size+i*size]:
                board += self.generate_tile(value)
            board += f"{vert}\n"
        board += "  " + f"{fill}"*size + "+\n"
        board += "    A   B   C   D   E   F"
        self._board = board

    def generate_dictionary(self):
        self._board_values = {}
        horizontal_values = "abcdef"
        for number in range(1, size+1).__reversed__():
            for letter in horizontal_values:
                self._board_values[f"{letter}{number}"] = " "
        return self._board_values

    def get_board_values(self):
        return self._board_values

    def get_parametr_from_tile(self, tile_index):
        self._check_if_in_range(tile_index)
        if tile_index not in self._board_values:
            return None
        else:
            return self._board_values[tile_index]

    def write_tile(self, tile_index, txt):
        self._check_if_in_range(tile_index)
        if tile_index not in self._board_values:
            return None
        else:
            self._board_values[tile_index] = str(txt)

if __name__ == "__main__":
    bo = Board()
    bo.write_tile("a6", "X")
    bo.write_tile("a3", "O")
    bo.write_tile("a2", "O")
    bo.write_tile("a1", "O")
    bo.write_tile("a4", "O")
    bo.write_tile("a5", "O")
    bo.write_tile("f1", "O")
    bo.write_tile("d5", "X")
    bo.generate_board()
    print(bo.get_board())
