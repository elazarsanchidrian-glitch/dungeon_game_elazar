from game.monster import Monster


def test_monster_creation():
    monster = Monster("Goblin", 50, 10)

    assert monster.name == "Goblin"
    assert monster.health == 50
    assert monster.max_health == 50
    assert monster.attack_damage == 10


def test_monster_take_damage():
    monster = Monster("Goblin", 50, 10)

    monster.take_damage(20)

    assert monster.health == 30


def test_monster_dies():
    monster = Monster("Goblin", 50, 10)

    monster.take_damage(50)

    assert monster.health == 0
    assert monster.is_alive() is False


def test_monster_is_alive():
    monster = Monster("Goblin", 50, 10)

    assert monster.is_alive() is True

