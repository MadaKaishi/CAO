from classes.constants import COLS, ROWS
from classes.enemy import Enemy, EnemyRandom, GameSupposedToBeFinished
from classes.board import Board
from classes.piece import Piece
import pytest


def test_create_enemy():
    enemy = Enemy("AI")
    assert enemy.name() == "AI"


def test_create_enemy_random():
    enemy = EnemyRandom("Ai")
    assert enemy.name() == "Ai"


def test_enemy_random_choose_symbol():
    enemy = EnemyRandom()
    assert enemy.choose_symbol() in ["X", "O"]


def test_enemy_random_choose_index():
    enemy = EnemyRandom()
    board = Board()
    row, col = enemy.choose_index(board)
    assert row in range(ROWS)
    assert col in range(COLS)


def test_enemy_choose_idex_full_board():
    enemy = EnemyRandom()
    board = Board()
    for row in range(ROWS):
        for col in range(COLS):
            piece = Piece(row, col, "X")
            board.place(piece)
    with pytest.raises(GameSupposedToBeFinished):
        enemy.choose_index(board)
