from classes.constants import COLS, ROWS
from classes.enemy import EnemyRandom
from classes.game import Game
from classes.piece import Piece


def test_game_create():
    game = Game()
    assert game._turn == "Order"
    assert not game._stop
    assert game.board().board()[0][0].symbol() == ""


def test_restart():
    game = Game()
    piece = Piece(0, 0, "X")
    game.board().place(piece)
    assert game.board().board()[0][0].symbol() == "X"
    game._restart()
    assert game.board().board()[0][0].symbol() == ""


def test_game_opponent_choose_easy():
    game = Game()
    game._gamemode = "Easy"
    game._choose_enemy_based_on_modes()
    assert game._enemy.name() == "EnemyRandom"


def test_game_opponent_choose_AIChaos():
    game = Game()
    game._gamemode = "Hard"
    game._side = "Order"
    game._choose_enemy_based_on_modes()
    assert game._enemy.name() == "EnemyAIChaos"


def test_game_opponent_choose_AIOrder():
    game = Game()
    game._gamemode = "Hard"
    game._side = "Chaos"
    game._choose_enemy_based_on_modes()
    assert game._enemy.name() == "EnemyAIOrder"
# Testing if game catches win conditions
# Down are just coded win conditions

def test_win_vert():
    game = Game()
    p1 = Piece(0, 0, "X")
    p2 = Piece(1, 0, "X")
    p3 = Piece(2, 0, "X")
    p4 = Piece(3, 0, "X")
    p5 = Piece(4, 0, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_win_vert_ver2():
    game = Game()
    p1 = Piece(5, 0, "X")
    p2 = Piece(1, 0, "X")
    p3 = Piece(2, 0, "X")
    p4 = Piece(3, 0, "X")
    p5 = Piece(4, 0, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_win_horizontal():
    game = Game()
    p1 = Piece(0, 0, "X")
    p2 = Piece(0, 1, "X")
    p3 = Piece(0, 2, "X")
    p4 = Piece(0, 3, "X")
    p5 = Piece(0, 4, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()

def test_win_hotizontal_ver2():
    game = Game()
    p1 = Piece(0, 5, "X")
    p2 = Piece(0, 1, "X")
    p3 = Piece(0, 2, "X")
    p4 = Piece(0, 3, "X")
    p5 = Piece(0, 4, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_not_win_6_in_horizontal():
    game = Game()
    p1 = Piece(0, 0, "X")
    p2 = Piece(0, 1, "X")
    p3 = Piece(0, 2, "X")
    p4 = Piece(0, 3, "X")
    p5 = Piece(0, 4, "X")
    p6 = Piece(0, 5, "X")
    piece_list = [p1, p2, p3, p4, p5, p6]
    for piece in piece_list:
        game.board().place(piece)
    assert not game.order_win()


def test_not_win_6_in_vertical():
    game = Game()
    p1 = Piece(0, 0, "X")
    p2 = Piece(1, 0, "X")
    p3 = Piece(2, 0, "X")
    p4 = Piece(3, 0, "X")
    p5 = Piece(4, 0, "X")
    p6 = Piece(5, 0, "X")
    piece_list = [p1, p2, p3, p4, p5, p6]
    for piece in piece_list:
        game.board().place(piece)
    assert not game.order_win()


def test_long_diag_1():
    game = Game()
    p1 = Piece(0, 0, "X")
    p2 = Piece(1, 1, "X")
    p3 = Piece(2, 2, "X")
    p4 = Piece(3, 3, "X")
    p5 = Piece(4, 4, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_long_diag_1_ver2():
    game = Game()
    p1 = Piece(5, 5, "X")
    p2 = Piece(1, 1, "X")
    p3 = Piece(2, 2, "X")
    p4 = Piece(3, 3, "X")
    p5 = Piece(4, 4, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_long_diag_1_loose():
    game = Game()
    p1 = Piece(0, 0, "X")
    p2 = Piece(1, 1, "X")
    p3 = Piece(2, 2, "X")
    p4 = Piece(3, 3, "X")
    p5 = Piece(4, 4, "X")
    p6 = Piece(5, 5, "X")
    piece_list = [p1, p2, p3, p4, p5, p6]
    for piece in piece_list:
        game.board().place(piece)
    assert not game.order_win()


def test_long_diag_2():
    game = Game()
    p1 = Piece(0, 5, "X")
    p2 = Piece(1, 4, "X")
    p3 = Piece(2, 3, "X")
    p4 = Piece(3, 2, "X")
    p5 = Piece(4, 1, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_long_diag_2_ver_2():
    game = Game()
    p1 = Piece(5, 0, "X")
    p2 = Piece(1, 4, "X")
    p3 = Piece(2, 3, "X")
    p4 = Piece(3, 2, "X")
    p5 = Piece(4, 1, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_long_diag_2_loose():
    game = Game()
    p1 = Piece(0, 5, "X")
    p2 = Piece(1, 4, "X")
    p3 = Piece(2, 3, "X")
    p4 = Piece(3, 2, "X")
    p5 = Piece(4, 1, "X")
    p6 = Piece(5, 0, "X")
    piece_list = [p1, p2, p3, p4, p5, p6]
    for piece in piece_list:
        game.board().place(piece)
    assert not game.order_win()


def test_diag_short_1():
    game = Game()
    p1 = Piece(0, 4, "X")
    p2 = Piece(1, 3, "X")
    p3 = Piece(2, 2, "X")
    p4 = Piece(3, 1, "X")
    p5 = Piece(4, 0, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_diag_short_2():
    game = Game()
    p1 = Piece(1, 5, "X")
    p2 = Piece(2, 4, "X")
    p3 = Piece(3, 3, "X")
    p4 = Piece(4, 2, "X")
    p5 = Piece(5, 1, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_diag_short_3():
    game = Game()
    p1 = Piece(0, 1, "X")
    p2 = Piece(1, 2, "X")
    p3 = Piece(2, 3, "X")
    p4 = Piece(3, 4, "X")
    p5 = Piece(4, 5, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_diag_short_4():
    game = Game()
    p1 = Piece(1, 0, "X")
    p2 = Piece(2, 1, "X")
    p3 = Piece(3, 2, "X")
    p4 = Piece(4, 3, "X")
    p5 = Piece(5, 4, "X")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert game.order_win()


def test_chaos_loose():
    game = Game()
    p1 = Piece(1, 0, "X")
    p2 = Piece(2, 1, "X")
    p3 = Piece(3, 2, "O")
    p4 = Piece(4, 3, "X")
    p5 = Piece(5, 4, "O")
    piece_list = [p1, p2, p3, p4, p5]
    for piece in piece_list:
        game.board().place(piece)
    assert not game.chaos_win()


def test_chaos_win_all_X():
    game = Game()
    for row in range(ROWS):
        for col in range(COLS):
            piece = Piece(row, col, "X")
            game.board().place(piece)
    assert game.chaos_win()
