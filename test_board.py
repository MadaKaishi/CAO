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
    bo.write_tile("f1", "O")
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


def test_not_win_with_6_in_vertical():
    bo = Board()
    bo.write_tile("b1", "X")
    bo.write_tile("b2", "X")
    bo.write_tile("b3", "X")
    bo.write_tile("b4", "X")
    bo.write_tile("b5", "X")
    bo.write_tile("b6", "X")
    assert not bo.check_order_win("X")


def test_not_win_with_6_in_horizontal():
    bo = Board()
    bo.write_tile("a1", "X")
    bo.write_tile("b1", "X")
    bo.write_tile("c1", "X")
    bo.write_tile("d1", "X")
    bo.write_tile("e1", "X")
    bo.write_tile("f1", "X")
    assert not bo.check_order_win("X")


def test_diagonal_long_1_option():
    bo = Board()
    bo.write_tile("a1", "X")
    bo.write_tile("b2", "X")
    bo.write_tile("c3", "X")
    bo.write_tile("d4", "X")
    bo.write_tile("e5", "X")
    assert bo.check_order_win("X")

def test_diagonal_long_2_option():
    bo = Board()
    bo.write_tile("f6", "X")
    bo.write_tile("b2", "X")
    bo.write_tile("c3", "X")
    bo.write_tile("d4", "X")
    bo.write_tile("e5", "X")
    assert bo.check_order_win("X")


def test_diagonal_long_3_option():
    bo = Board()
    bo.write_tile("a6", "X")
    bo.write_tile("b5", "X")
    bo.write_tile("c4", "X")
    bo.write_tile("d3", "X")
    bo.write_tile("e2", "X")
    assert bo.check_order_win("X")


def test_diagonal_long_4_option():
    bo = Board()
    bo.write_tile("f1", "X")
    bo.write_tile("b5", "X")
    bo.write_tile("c4", "X")
    bo.write_tile("d3", "X")
    bo.write_tile("e2", "X")
    assert bo.check_order_win("X")


def test_diagonal_long_5_option_lose():
    bo = Board()
    bo.write_tile("f1", "X")
    bo.write_tile("b5", "X")
    bo.write_tile("c4", "X")
    bo.write_tile("d3", "X")
    bo.write_tile("e2", "X")
    bo.write_tile("a6", "X")
    assert not bo.check_order_win("X")


def test_diagonal_long_6_option_lose():
    bo = Board()
    bo.write_tile("a1", "X")
    bo.write_tile("b2", "X")
    bo.write_tile("c3", "X")
    bo.write_tile("d4", "X")
    bo.write_tile("e5", "X")
    bo.write_tile("f6", "X")
    assert not bo.check_order_win("X")


def test_diagonal_short_1():
    bo = Board()
    bo.write_tile("a5", "X")
    bo.write_tile("b4", "X")
    bo.write_tile("c3", "X")
    bo.write_tile("d2", "X")
    bo.write_tile("e1", "X")
    assert bo.check_order_win("X")


def test_diagonal_short_2():
    bo = Board()
    bo.write_tile("b6", "X")
    bo.write_tile("c5", "X")
    bo.write_tile("d4", "X")
    bo.write_tile("e3", "X")
    bo.write_tile("f2", "X")
    assert bo.check_order_win("X")


def test_diagonal_short_3():
    bo = Board()
    bo.write_tile("e6", "X")
    bo.write_tile("d5", "X")
    bo.write_tile("c4", "X")
    bo.write_tile("b3", "X")
    bo.write_tile("a2", "X")
    assert bo.check_order_win("X")


def test_diagonal_short_4():
    bo = Board()
    bo.write_tile("b1", "X")
    bo.write_tile("c2", "X")
    bo.write_tile("d3", "X")
    bo.write_tile("e4", "X")
    bo.write_tile("f5", "X")
    assert bo.check_order_win("X")