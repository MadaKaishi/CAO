from classes.enemy import Enemy, EnemyRandom, GameSupposedToBeFinished
from classes.board import Board
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
    assert enemy.choose_index(board) in board.get_board_values().keys()


def test_enemy_choose_idex_full_board():
    enemy = EnemyRandom()
    board = Board()
    board._create_dictionary_full_of_symbol("X")
    with pytest.raises(GameSupposedToBeFinished):
        enemy.choose_index(board) in board.get_board_values().keys()
