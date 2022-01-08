from classes.board import Board
from classes.enemy import EnemyRandom, GameSupposedToBeFinished
from classes.piece import Piece
from classes.constants import ROWS, COLS
import pytest

def test_enemy_random_create():
    enemy = EnemyRandom("Enemy")
    assert enemy.name() == "Enemy"


def test_enemy_move():
    board = Board()
    enemy = EnemyRandom()
    assert enemy.choose_symbol(board) in ["X", "O"]


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
