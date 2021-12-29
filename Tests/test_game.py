from classes.enemy import EnemyRandom
from classes.game import Game
from classes.piece import Piece


def test_game_create():
    game = Game("1", "1")
    assert game.gamemode() == "1"
    assert game.side() == "1"
    assert game._enemy.name() == "Enemy"
    assert game._turn == "Order"
    assert not game._stop
    assert game.board().board()[0][0].symbol() == ""


def test_restart():
    game = Game("1", "1")
    piece = Piece(0, 0, "X")
    game.board().place(piece)
    assert game.board().board()[0][0].symbol() == "X"
    game.restart("1", "1")
    assert game.board().board()[0][0].symbol() == ""

def test_win():
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