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


def test_win_x():
    bo = Board()
    bo.write_tile("a1", "X")
    bo.write_tile("b1", "X")
    bo.write_tile("c1", "X")
    bo.write_tile("d1", "X")
    bo.write_tile("e1", "X")
    assert bo.check_order_win("X")


def test_win_x_2():
    bo = Board()
    bo.write_tile("f1", "X")
    bo.write_tile("b1", "X")
    bo.write_tile("c1", "X")
    bo.write_tile("d1", "X")
    bo.write_tile("e1", "X")
    assert bo.check_order_win("X")


def test_win_vertical():
    bo = Board()
    bo.write_tile("a1", "X")
    bo.write_tile("a2", "X")
    bo.write_tile("a3", "X")
    bo.write_tile("a4", "X")
    bo.write_tile("a5", "X")
    bo.write_tile("a6", "O")
    assert bo.check_order_win("X")
