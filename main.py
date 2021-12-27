from classes.board import Board
from classes.game import Game


def choose_side():
    while True:
        side = input("Choose side:\n1.Order\n2.Chaos\nPress q to quit\n")
        possible_inputs = ["1", "2"]
        if side in possible_inputs:
            break
        if side == "q":
            side = None
            break
    return side


def choose_gamemode():
    while True:
        gamemode = input("Choose gamemode:\n1.Enemy does random moves\n2.Enemy does advanced moves\nPress q to quit\n")
        possible_inputs = ["1", "2"]
        if gamemode in possible_inputs:
            break
        if gamemode == "q":
            gamemode = None
            break
    return gamemode


def create_game():
    side = choose_side()
    if None is side:
        return None
    gamemode = choose_gamemode()
    if None is gamemode:
        return None


if __name__ == "__main__":
    side = choose_side()
    if side == "q":
        exit()
    gamemode = choose_gamemode()
    if gamemode == "q":
        exit()
    board = Board()
    game = Game(side, gamemode, board)
    player = game.create_player()
    game.create_opponents(player)
    print(game.board().get_board())
    game.play()
    if side == "1":
        if game.board().chaos_win():
            print(f"{player.name()} Loose!")
        else:
            print(f"{player.name()} Won!")
    if side == "2":
        if game.board().order_win():
            print(f"{player.name()} Loose!")
        else:
            print(f"{player.name()} Won!")
