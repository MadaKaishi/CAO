class Player:
    def __init__(self, name="Player") -> "Player":
        self._name = name
        self._move_list = []

    def add_move(self, place, symbol):
        self._move_list.append((place, symbol))

    def name(self):
        return self._name

    def move_list(self):
        return self._move_list

    def read_move_list(self):
        move_str = ""
        for index, move in enumerate(self._move_list):
            place, symbol = move
            move_str += f"{index+1}. {place} {symbol}"
        return move_str

