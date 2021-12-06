from board import Board
import pytest


def test_init_instance():
    bo = Board()
    assert bo.get_parametr_from_tile("a1") == " "


def test_write_tile():
    bo = Board()
    bo.write_tile("a1", "X")
    assert bo.get_parametr_from_tile("a1") == "X"
