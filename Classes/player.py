class Player:
    def __init__(self, name) -> "Player":
        self._name = name
        self._move_list = []

    def add_move(self, place, symbol):
        self._move_list.append((place, symbol))

    def read_move_list(self):
        move_str = ""
        for index, move in enumerate(self._move_list):
            place, symbol = move
            move_str += f"{index+1}. {place} {symbol}"
        return move_str

    def player_choose_move_conditions(self, board):
        while True:
            place = input("Choose your next move: ")
            if place in board._board_values.keys():
                break
        while True:
            symbol = input("Choose symbol: ")
            if symbol in ["X", "O"]:
                break
        self.add_move(place, symbol)
        return place, symbol
