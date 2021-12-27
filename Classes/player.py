class Player:
    def __init__(self, name) -> "Player":
        self._name = name
        self._move_list = []

    def add_move(self, place, symbol):
        self._move_list.append((place, symbol))

    def name(self):
        return self._name

    def read_move_list(self):
        move_str = ""
        for index, move in enumerate(self._move_list):
            place, symbol = move
            move_str += f"{index+1}. {place} {symbol}"
        return move_str

    def move(self, board):
        possible_moves = []
        for key in board.get_board_values():
            if board.get_board_values()[key] == " ":
                possible_moves.append(f"{key}")
        while True:
            place = input("Choose your next move: ")
            if place in board.get_board_values().keys():
                if place in possible_moves:
                    break
        while True:
            symbol = input("Choose symbol: ")
            if symbol in ["X", "O"]:
                break
        self.add_move(place, symbol)
        return place, symbol
