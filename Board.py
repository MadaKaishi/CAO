from constants import BOARD_SIZE as size, TABLE_FILLMENT_HORIZONTAL as fill,TABLE_FILLMENT_VERTICAL as vert


class Board:
    def __init__(self) -> None:
        self._board = ""
        self.generate_dictionary()

    def get_board(self):
        return self._board

    def generate_tile(self, tile_value):
        base = f"{vert} {tile_value} "
        return base

    def generate_board(self):
        board = ""
        for i in range(size):
            board += f"{fill}"*6 + "+\n"
            for value in list(self._board_values.values())[(i*size):size+i*size]:
                board += self.generate_tile(value)
            board += f"{vert}\n"
        board += f"{fill}"*size + "+"
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
        if tile_index not in self._board_values:
            return None
        else:
            return self._board_values[tile_index]

    def write_tile(self, tile_index, txt):
        if tile_index not in self._board_values:
            return None
        else:
            self._board_values[tile_index] = str(txt)


bo = Board()
bo.write_tile("a6", "X")
bo.write_tile("a3", "O")
bo.generate_board()
print(bo.get_board())
