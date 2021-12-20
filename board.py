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

    def check_order_win(self, symbol):
        board = self._create_board_in_list_form()
        if self._check_horizontal(board, symbol):
            return True
        if self._check_vertical(board, symbol):
            return True
        if self._check_diagonal(board, symbol):
            return True
        return False

    def _check_horizontal(self, board, symbol):
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        for row in board:
            if row[:size-1] == searched:
                if row != avoided:
                    return True
            if row[1:size] == searched:
                if row != avoided:
                    return True
        return False

    def _check_vertical(self, board, symbol):
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        for i in range(size):
            tem_list = []
            for row in board:
                tem_list.append(row[i])
            if tem_list[:size-1] == searched:
                if tem_list != avoided:
                    return True
            if tem_list[1:size] == searched:
                if tem_list != avoided:
                    return True
        return False

    def _check_diagonal(self, b, symbol):
        searched = [symbol, symbol, symbol, symbol, symbol]
        avoided = [symbol, symbol, symbol, symbol, symbol, symbol]
        diagonal_l_1 = [b[0][0], b[1][1], b[2][2], b[3][3], b[4][4], b[5][5]]
        diagonal_l_2 = [b[0][5], b[1][4], b[2][3], b[3][2], b[4][1], b[5][0]]
        diagonal_s_3 = [b[1][0], b[2][1], b[3][2], b[4][3], b[5][4]]
        diagonal_s_4 = [b[4][0], b[3][1], b[2][2], b[1][3], b[0][4]]
        diagonal_s_5 = [b[5][1], b[4][2], b[3][3], b[2][4], b[5][1]]
        diagonal_s_6 = [b[0][1], b[1][2], b[2][3], b[3][4], b[4][5]]
        diagonal_long = [diagonal_l_1, diagonal_l_2]
        diagonal_short = [diagonal_s_3, diagonal_s_4, diagonal_s_5, diagonal_s_6]
        if searched in diagonal_short:
            return True
        for diagonal in diagonal_long:
            if diagonal[:size-1] == searched:
                if diagonal != avoided:
                    return True
            if diagonal[1:size] == searched:
                if diagonal != avoided:
                    return True


    def _create_board_in_list_form(self):
        final_list = []
        horizontal_values = "abcdef"
        for number in range(1, size+1).__reversed__():
            temporary_list = []
            for letter in horizontal_values:
                dict_value = f"{letter}{number}"
                temporary_list.append(f"{self._board_values[dict_value]}")
            final_list.append(temporary_list)
        return final_list

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
    bo.write_tile("f4", "O")
    bo.write_tile("a5", "O")
    bo.write_tile("f1", "O")
    bo.write_tile("d5", "X")
    print(bo._create_board_in_list_form())
    bo.generate_board()
    print(bo.get_board())
