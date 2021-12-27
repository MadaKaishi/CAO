from player import Player


class Game:
    def __init__(self, player_side, gamemode, board) -> "Game":
        self._player_side = player_side
        self._gamemode = gamemode
        self._board = board

    def player_side(self):
        return self._player_side

    def gamemode(self):
        return self._gamemode

    def create_player(self):
        name = input("Player name: ")
        return Player(name)

    def create_opponents(self, player, enemy):
        self._sides = {}
        if self._player_side == "Order":
            self._sides["Order"] = player
            self._sides["Chaos"] = enemy
        else:
            self._sides["Order"] = enemy
            self._sides["Chaos"] = player
        return self._sides

    def save_board(self, path):
        with open(f"{path}", "a") as filehandle:
            filehandle.write("\n")
            filehandle.write(f"{self._board.get_board_values()}")
