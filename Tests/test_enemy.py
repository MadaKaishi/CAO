from classes.board import Board
from classes.enemy import Enemy, EnemyAIChaos, EnemyAIOrder, EnemyRandom, GameSupposedToBeFinished
from classes.piece import Piece
from classes.constants import ROWS, COLS, BOARD_SIZE as size
import pytest


# enemy tests

def test_enemy():
    enemy = Enemy("Enemy")
    assert enemy.name() == "Enemy"


# enemy random tests

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


#  enemy order AI tests

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


def test_orde_enemy_make_move():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    for _ in range(4):
        row, col = enemy.choose_index(board)
        piece = Piece(row, col, "X")
        board.place(piece)
        assert row in range(6)
        assert col in range(6)


def test_order_enemy_choose_index_x():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    piece_1 = Piece(1, 1, "X")
    piece_2 = Piece(1, 2, "X")
    board.place(piece_1)
    board.place(piece_2)
    index = enemy.choose_index(board)
    assert index == (1, 3) or index == (1, 4)
    assert enemy.choose_symbol() == "X"


def test_order_enemy_choose_index_o():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    piece_1 = Piece(3, 1, "O")
    piece_2 = Piece(3, 2, "O")
    board.place(piece_1)
    board.place(piece_2)
    index = enemy.choose_index(board)
    assert index == (3, 3) or index == (3, 4)
    assert enemy.choose_symbol() == "O"


def test_order_enemy_finisher_move_O():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    p_1 = Piece(3, 1, "O")
    p_2 = Piece(3, 2, "O")
    p_3 = Piece(3, 3, "O")
    p_4 = Piece(3, 4, "O")
    pieces = [p_1, p_2, p_3, p_4]
    for piece in pieces:
        board.place(piece)
    index = enemy.choose_index(board)
    assert index == (3, 0) or index == (3, 5)
    assert enemy.choose_symbol() == "O"


def test_order_enemy_finisher_move_X():
    board = Board()
    enemy = EnemyAIOrder("Enemy", board)
    p_1 = Piece(3, 1, "X")
    p_2 = Piece(3, 2, "X")
    p_3 = Piece(3, 3, "X")
    p_4 = Piece(3, 4, "X")
    pieces = [p_1, p_2, p_3, p_4]
    for piece in pieces:
        board.place(piece)
    index = enemy.choose_index(board)
    assert index == (3, 0) or index == (3, 5)
    assert enemy.choose_symbol() == "X"


# test enemy AI chaos

def test_enemy_chaos_AI_create():
    enemy = EnemyAIChaos("Enemy")
    assert enemy.name() == "Enemy"
    assert enemy.board() is None


def test_enemy_AI_test_response_corner():
    board = Board()
    enemy = EnemyAIChaos("Enemy", board)
    piece = Piece(0, 0, "X")
    board.place(piece)
    board.set_last_move(piece)
    assert enemy.choose_index(board) == (5, 5)
    assert enemy.choose_symbol() == ("X")


def test_enemy_AI_test_response_not_corner():
    board = Board()
    enemy = EnemyAIChaos("Enemy", board)
    piece = Piece(1, 1, "X")
    board.place(piece)
    board.set_last_move(piece)
    assert enemy.choose_index(board) == (3, 1)
    assert enemy.choose_symbol() == ("O")
