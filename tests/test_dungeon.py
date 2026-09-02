from game.dungeon import Dungeon


def test_dungeon_starts_at_zero():
    dungeon = Dungeon()

    assert dungeon.get_position() == (0, 0)


def test_move_east():
    dungeon = Dungeon()

    assert dungeon.move("east") is True
    assert dungeon.get_position() == (1, 0)


def test_invalid_direction():
    dungeon = Dungeon()

    assert dungeon.move("banana") is False
    assert dungeon.get_position() == (0, 0)