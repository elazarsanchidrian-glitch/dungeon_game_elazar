def test_player_creation():
    player = Player("Elazar")

    assert player.name == "Elazar"
    assert player.health == 100
    assert player.inventory == []
    assert player.gold == 0


def test_add_item():
    player = Player("Elazar")
    item = Item("Sword", "A sword.", 50)

    player.add_item(item)

    assert item in player.inventory


def test_warrior_attack_damage():
    player = Player("Elazar")
    player.character_class = "Warrior"

    assert player.get_attack_damage() == 30