from classes.player import Player


def test_create():
    player = Player("Adam")
    assert player.name() == "Adam"


def test_move_list():
    player = Player("Adam")
    player.add_move("a1", "X")
    assert player.move_list() == [("a1", "X")]
