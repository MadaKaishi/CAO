from classes.board import Board
from classes.constants import COLS, ROWS
from classes.piece import Piece


def test_create_board():
    board = Board()
    for row in range(ROWS):
        for col in range(COLS):
            assert board.get_symbol_from_tile(row, col) == ""


def test_place_sth_on_board():
    board = Board()
    piece = Piece(0, 0, "X")
    board.place(piece)
    assert board.get_symbol_from_tile(0, 0) == "X"


def test_load_board():
    board = Board()
    piece = Piece(0, 0, "X")
    board.place(piece)
    board_list = board.board()
    board_2 = Board(board_list)
    assert board_2.board() == board.board()


def test_last_move():
    board = Board()
    piece = Piece(0, 0, "X")
    board.place(piece)
    assert board.last_move() == piece
