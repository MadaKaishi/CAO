from classes.enemy import EnemyAI, EnemyRandom
from classes.player import Player


class Game:
    def __init__(self, player_side, gamemode, board) -> "Game":
        self._player_side = player_side
        self._gamemode = gamemode
        if self._gamemode == "1":
            self._enemy = EnemyRandom("Enemy")
        if self._gamemode == "2":
            self._enemy = EnemyAI("Enemy")
        self._board = board
        self._sides = {}

    def player_side(self):
        return self._player_side

    def board(self):
        return self._board

    def gamemode(self):
        return self._gamemode

    def create_player(self):
        name = input("Player name: ")
        return Player(name)

    def create_opponents(self, player):
        if self._player_side == "1":
            self._sides["Order"] = player
            self._sides["Chaos"] = self._enemy
        else:
            self._sides["Order"] = self._enemy
            self._sides["Chaos"] = player
        return self._sides

    def save_board(self, path):
        with open(f"{path}", "a") as filehandle:
            filehandle.write("\n")
            filehandle.write(f"{self._board.get_board_values()}")

    def make_order_turn(self):
        print("Order turn")
        id_1, ch_1 = self._sides["Order"].move(self._board)      # 1. Turn of order
        self._board.write_tile(id_1, ch_1)  # 2. Changing board
        self._board.generate_board()
        print(self._board.get_board())

    def make_chaos_turn(self):
        print("Chaos turn")
        id_2, ch_2 = self._sides["Chaos"].move(self._board)  # 3. Turn of chaos
        self._board.write_tile(id_2, ch_2)  # 4. Changing board
        self._board.generate_board()
        print(self._board.get_board())

    def play(self):
        while not (self.board().chaos_win() or self.board().order_win()):
            self.make_order_turn()
            if self.board().order_win():
                break
            self.make_chaos_turn()