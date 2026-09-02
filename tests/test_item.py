from game.item import Item


def test_item_creation():
    item = Item("Sword", "A sharp sword.", 50)

    assert item.name == "Sword"
    assert item.description == "A sharp sword."
    assert item.value == 50


def test_item_string():
    item = Item("Sword", "A sharp sword.", 50)

    assert str(item) == "Sword"
