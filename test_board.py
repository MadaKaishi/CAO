from board import Board, OutOfRangeError
import pytest


def test_init_instance():
    bo = Board()
    assert bo.get_parametr_from_tile("a1") == " "


def test_write_tile():
    bo = Board()
    bo.write_tile("a1", "X")
    assert bo.get_parametr_from_tile("a1") == "X"


def test_tile_out_of_range():
    bo = Board()
    with pytest.raises(OutOfRangeError):
        bo.write_tile("a7", "X")


def test_read_out_of_range():
    bo = Board()
    bo.write_tile("a1", "X")
    with pytest.raises(OutOfRangeError):
        bo.get_parametr_from_tile("a7")
