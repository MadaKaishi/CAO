from classes.board import Board
from classes.enemy import EnemyAIOrder, EnemyRandom, GameSupposedToBeFinished
from classes.piece import Piece
from classes.constants import ROWS, COLS, BOARD_SIZE as size
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


def test_order_enemy_create():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    assert enemy.name() == "Enemy"
    assert enemy.board() == board


def test_order_enemy_middle_rectangle():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    middle_board = []
    for row in range(ROWS-2):
        temp_list = []
        for col in range(COLS-2):
            temp_list.append("")
        middle_board.append(temp_list)
    enemy_middle = enemy._get_middle_rectangle(board)
    for row in range(size-2):
        for col in range(size-2):
            enemy_middle[row][col] == middle_board[row][col]
